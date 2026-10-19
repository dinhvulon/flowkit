#!/usr/bin/env python3
"""Dialogue check for generated clips — listen with Whisper and compare against the prompt's lines.

Part of /fk-review-video. For each clip it:
  * transcribes the clip audio with faster-whisper (word timestamps, VAD on)
  * matches every expected native line (video_prompt JSON -> speech.dialogue; post_vo lines are
    added in the edit, so they are NOT expected in the clip) to the transcript
  * scores word accuracy, checks the line sits inside its "t" window, flags cut-off endings
  * reports extra speech (anything left unmatched, or any speech in a clip that should be silent)
  * estimates each line's pitch and checks it against the speaker's voice (female/male Gemini voice)

Expected lines come from one of:
  --scene-id <SID>                 video_prompt fetched from the FlowKit API (http://127.0.0.1:8100)
  --prompt-file <f.json> --clip <ID>   a prompts JSON (list of clip objects or one object)
  --expect "Nora|kore|0-4s|Let go. I am."   repeatable; voice and window optional ("Nora||0-4s|...")

Usage:
  python tools/review_dialogue.py output/embers/scenes/scene_001_RA-02_49c1a6a2.mp4 --scene-id 49c1a6a2-...
  python tools/review_dialogue.py clip.mp4 --prompt-file output/embers/prompts_v7.json --clip RA-02 --json out.json

Exit code: 0 = every line passes, 1 = at least one problem, 2 = could not run.
Pitch is a rough hint: voice mismatches are printed as "?" warnings for a human to listen to; they never fail.
Needs ffmpeg on PATH and `pip install faster-whisper` (model downloads on first run).
"""

import argparse
import difflib
import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

import numpy as np

SR = 16000
API = "http://127.0.0.1:8100"
# Gemini TTS library voices used by FlowKit (first word of voice_description) -> expected register.
VOICE_SEX = {
    "kore": "F", "erinome": "F", "laomedeia": "F", "aoede": "F", "leda": "F", "zephyr": "F", "callirrhoe": "F",
    "autonoe": "F", "despina": "F", "gacrux": "F", "pulcherrima": "F", "vindemiatrix": "F", "sulafat": "F", "achernar": "F",
    "fenrir": "M", "algenib": "M", "sadaltager": "M", "alnilam": "M", "puck": "M", "charon": "M", "orus": "M",
    "enceladus": "M", "iapetus": "M", "umbriel": "M", "algieba": "M", "rasalgethi": "M", "achird": "M", "zubenelgenubi": "M",
    "sadachbia": "M", "schedar": "M",
}
MALE_MAX_HZ, FEMALE_MIN_HZ = 210.0, 140.0   # rough pitch is only a hint: warn outside these, never fail
ACC_PASS = 0.80             # word accuracy needed per line
WINDOW_SLACK_S = 0.75       # allowed drift outside the "t" window


ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen " \
       "seventeen eighteen nineteen".split()
TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()


def num_words(n):
    """Spell 0-9999 the way a script writes it, so Whisper's "20" matches "twenty"."""
    if n < 20:
        return [ONES[n]]
    if n < 100:
        return [TENS[n // 10]] + ([ONES[n % 10]] if n % 10 else [])
    if n < 1000:
        return [ONES[n // 100], "hundred"] + (num_words(n % 100) if n % 100 else [])
    return num_words(n // 1000) + ["thousand"] + (num_words(n % 1000) if n % 1000 else [])


def norm_words(text):
    """Lowercase words with apostrophes dropped ("Keller's" == "kellers") and digits spelled out."""
    text = re.sub(r"\(.*?\)", " ", text or "")
    text = re.sub(r"(?<=\d),(?=\d{3})", "", text.lower()).replace("’", "").replace("'", "")
    out = []
    for w in re.sub(r"[^a-z0-9 ]+", " ", text).split():
        out += num_words(int(w)) if w.isdigit() and int(w) < 10000 else [w]
    return out


def parse_window(t):
    m = re.match(r"\s*([\d.]+)\s*-\s*([\d.]+)\s*s?\s*$", t or "")
    return (float(m.group(1)), float(m.group(2))) if m else None


def load_audio(path):
    cmd = ["ffmpeg", "-v", "error", "-i", str(path), "-vn", "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0


def median_f0(audio, t0, t1):
    """Rough median pitch (Hz) of voiced 40 ms frames between t0 and t1, autocorrelation method."""
    seg = audio[int(max(0, t0) * SR):int(max(t0, t1) * SR)]
    frame, hop, f0s = int(0.04 * SR), int(0.01 * SR), []
    lo, hi = int(SR / 400), int(SR / 70)            # search 70-400 Hz
    for i in range(0, len(seg) - frame, hop):
        x = seg[i:i + frame]
        if np.sqrt(np.mean(x * x)) < 0.02:          # skip silence
            continue
        x = x - x.mean()
        ac = np.correlate(x, x, "full")[frame - 1:]
        if ac[0] <= 0:
            continue
        lag = lo + int(np.argmax(ac[lo:hi]))
        if ac[lag] / ac[0] > 0.45:                  # voiced enough
            f0s.append(SR / lag)
    return float(np.median(f0s)) if len(f0s) >= 5 else None


def expected_from_prompt(vp):
    if isinstance(vp, str):
        vp = json.loads(vp)
    speech = vp.get("speech") or {}
    voices = speech.get("voices") or {}
    lines = [{"speaker": d.get("speaker", ""), "voice": voices.get(d.get("speaker", ""), ""),
              "window": parse_window(d.get("t")), "line": d.get("line", "")} for d in speech.get("dialogue") or []]
    duration = vp.get("duration")
    return lines, duration


def get_expected(args):
    if args.expect:
        out = []
        for e in args.expect:
            parts = e.split("|")
            if len(parts) != 4:
                sys.exit("--expect must be 'Speaker|voice|0-4s|line'")
            out.append({"speaker": parts[0], "voice": parts[1], "window": parse_window(parts[2]), "line": parts[3]})
        return out, None
    if args.scene_id:
        with urllib.request.urlopen(f"{API}/api/scenes/{args.scene_id}", timeout=30) as r:
            scene = json.loads(r.read())
        lines, dur = expected_from_prompt(scene.get("video_prompt") or "{}")
        return lines, dur or scene.get("duration")
    if args.prompt_file:
        data = json.loads(Path(args.prompt_file).read_text(encoding="utf-8"))
        clips = data if isinstance(data, list) else [data]
        clip = next((c for c in clips if not args.clip or c.get("clip_id") == args.clip), None)
        if clip is None:
            sys.exit(f"clip {args.clip} not found in {args.prompt_file}")
        return expected_from_prompt(clip)
    return [], None


def transcribe(audio, model_name, device):
    from faster_whisper import WhisperModel
    model = WhisperModel(model_name, device=device, compute_type="int8" if device == "cpu" else "float16")
    segments, info = model.transcribe(audio, language="en", word_timestamps=True, vad_filter=True,
                                      condition_on_previous_text=False, beam_size=5)
    words = []
    for seg in segments:
        for w in seg.words or []:
            for tok in norm_words(w.word):
                words.append({"w": tok, "start": float(w.start), "end": float(w.end)})
    return words


def best_span(words, target, used):
    """Best contiguous run of unused transcript words for the target word list. Returns (ratio, i, j)."""
    best = (0.0, None, None)
    n, m = len(words), len(target)
    for i in range(n):
        if i in used:
            continue
        for j in range(i + max(1, m // 2), min(n, i + m * 2) + 1):
            if any(k in used for k in range(i, j)):
                break
            ratio = difflib.SequenceMatcher(None, target, [x["w"] for x in words[i:j]]).ratio()
            if ratio > best[0]:
                best = (ratio, i, j)
    return best


def review(video, expected, clip_duration, model_name, device):
    audio = load_audio(video)
    clip_len = len(audio) / SR
    words = transcribe(audio, model_name, device)
    used, rows, problems = set(), [], []
    for e in expected:
        target = norm_words(e["line"])
        ratio, i, j = best_span(words, target, used) if target else (0.0, None, None)
        row = {"speaker": e["speaker"], "voice": e["voice"], "expected": e["line"],
               "window": e["window"], "heard": "", "accuracy": round(ratio, 2), "start": None, "end": None,
               "f0_hz": None, "sex": None, "issues": [], "warnings": []}
        if i is None or ratio < 0.3:
            row["issues"].append("MISSING: line not heard")
        else:
            used.update(range(i, j))
            span = words[i:j]
            row.update(heard=" ".join(x["w"] for x in span), start=round(span[0]["start"], 2), end=round(span[-1]["end"], 2))
            if ratio < ACC_PASS:
                row["issues"].append(f"WORDS: accuracy {ratio:.0%} < {ACC_PASS:.0%}")
            if target and span[-1]["w"] != target[-1] and target[-1] not in [x["w"] for x in span[-3:]]:
                row["issues"].append("CUT-OFF: last word missing")
            if span[-1]["end"] > clip_len - 0.15:
                row["issues"].append("CUT-OFF: speech runs into the clip end")
            if e["window"]:
                a, b = e["window"]
                if span[0]["start"] < a - WINDOW_SLACK_S or span[-1]["end"] > b + WINDOW_SLACK_S:
                    row["issues"].append(f"TIMING: heard {span[0]['start']:.1f}-{span[-1]['end']:.1f}s, planned {a:g}-{b:g}s")
            f0 = median_f0(audio, span[0]["start"], span[-1]["end"])
            row["f0_hz"] = round(f0) if f0 else None
            row["sex"] = VOICE_SEX.get((e["voice"] or "").lower())
            if f0 and row["sex"] == "M" and f0 > MALE_MAX_HZ:
                row["warnings"].append(f"VOICE?: {e['speaker']} ({e['voice']}, male) pitch {f0:.0f} Hz is high for a male voice - listen")
            if f0 and row["sex"] == "F" and f0 < FEMALE_MIN_HZ:
                row["warnings"].append(f"VOICE?: {e['speaker']} ({e['voice']}, female) pitch {f0:.0f} Hz is low for a female voice - listen")
        problems += [f"{e['speaker']}: {x}" for x in row["issues"]]
        rows.append(row)
    # relative check: in a mixed clip every male line should sit clearly below every female line
    males = [r for r in rows if r["sex"] == "M" and r["f0_hz"]]
    females = [r for r in rows if r["sex"] == "F" and r["f0_hz"]]
    for m in males:
        for f in females:
            if m["f0_hz"] > f["f0_hz"] * 0.9:
                m["warnings"].append(f"VOICE?: {m['speaker']} ({m['f0_hz']} Hz) is not clearly lower than "
                                     f"{f['speaker']} ({f['f0_hz']} Hz) - listen: are the two voices swapped or the same?")
    warnings = [f"{r['speaker']}: {w}" for r in rows for w in r["warnings"]]
    extra = [x for k, x in enumerate(words) if k not in used]
    extra_text = " ".join(x["w"] for x in extra)
    if extra and len(extra) >= 3:
        problems.append(f"EXTRA SPEECH ({extra[0]['start']:.1f}-{extra[-1]['end']:.1f}s): \"{extra_text}\"")
    if not expected and words:
        problems.append(f"SPEECH IN A SILENT CLIP: \"{' '.join(x['w'] for x in words)}\"")
    return {"video": str(video), "clip_seconds": round(clip_len, 2), "planned_seconds": clip_duration,
            "transcript": " ".join(x["w"] for x in words), "lines": rows, "extra_speech": extra_text,
            "problems": problems, "warnings": warnings, "pass": not problems}


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("video", type=Path)
    ap.add_argument("--scene-id")
    ap.add_argument("--prompt-file")
    ap.add_argument("--clip")
    ap.add_argument("--expect", action="append")
    ap.add_argument("--model", default="small.en", help="faster-whisper model (tiny.en, base.en, small.en, medium.en)")
    ap.add_argument("--device", default="cpu")
    ap.add_argument("--json", type=Path, help="write the full report here")
    args = ap.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if not args.video.exists():
        print(f"no such file: {args.video}"); sys.exit(2)
    expected, dur = get_expected(args)
    try:
        rep = review(args.video, expected, dur, args.model, args.device)
    except (subprocess.CalledProcessError, ImportError) as e:
        print(f"could not run: {e}"); sys.exit(2)
    print(f"Transcript: {rep['transcript'] or '(no speech)'}")
    for r in rep["lines"]:
        when = f"{r['start']}-{r['end']}s" if r["start"] is not None else "-"
        f0 = f"{r['f0_hz']} Hz" if r["f0_hz"] else "-"
        print(f"- {r['speaker']} ({r['voice'] or '?'}) {when} acc {r['accuracy']:.0%} pitch {f0}: \"{r['heard']}\"")
        for i in r["issues"]:
            print(f"    ! {i}")
        for w in r["warnings"]:
            print(f"    ? {w}")
    if rep["extra_speech"]:
        print(f"Unmatched words: \"{rep['extra_speech']}\"")
    print("PASS" if rep["pass"] else "FAIL: " + "; ".join(rep["problems"]))
    if args.json:
        args.json.write_text(json.dumps(rep, indent=1, ensure_ascii=False), encoding="utf-8")
    sys.exit(0 if rep["pass"] else 1)


if __name__ == "__main__":
    main()
