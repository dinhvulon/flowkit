#!/usr/bin/env python3
"""Intro trailer (hook montage) helper for /fk-capcut-edit.

Two steps, run when the user asks for an intro trailer:

  scan   Measure loudness, loudness jumps and motion in every clip and list the
         most intense moments as candidates (JSON + one preview frame each).
         Claude reads the frames and the dialogue, proposes a cut list, and the
         user approves it before anything is built.

  build  Cut every approved segment to its own file (import into CapCut in
         name order) and assemble a draft trailer per version (e.g. 30s, 45s)
         with black beats, placeholder SFX, optional music and the year card.
         Also writes a timeline .md with source in/out per segment, so the
         final polish can be done in CapCut from the original clips.

Usage:
  python trailer_cuts.py scan output/<slug>/1080 --skip 1.0 \
      --clips-json output/<slug>/clips.json --out output/<slug>/trailer
  python trailer_cuts.py build output/<slug>/trailer/cutlist.json [--version 30s]

Cut list format: see skills/fk-capcut-edit/references/trailer-intro.md §5.
Needs ffmpeg/ffprobe on PATH and numpy. Writes nothing outside --out / the
cut list's out_dir.
"""

import argparse
import json
import math
import re
import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np

AUDIO_SR = 16000  # analysis only
GRID = 0.1  # seconds per analysis step
MOTION_FPS = 12
FONT_CANDIDATES = [
    "C:/Windows/Fonts/ariblk.ttf",
    "C:/Windows/Fonts/arialbd.ttf",
    "/Library/Fonts/Arial Black.ttf",
    "/usr/share/fonts/truetype/msttcorefonts/Arial_Black.ttf",
]


# ── helpers ──────────────────────────────────────────────────────────────

def run(cmd, capture=False):
    res = subprocess.run(cmd, stdout=subprocess.PIPE if capture else None,
                         stderr=subprocess.PIPE)
    if res.returncode != 0:
        sys.stderr.write(res.stderr.decode("utf-8", "replace")[-2000:])
        raise SystemExit(f"ffmpeg failed: {' '.join(map(str, cmd[:6]))} …")
    return res.stdout


def probe(path):
    out = run(["ffprobe", "-v", "error", "-show_entries",
               "format=duration:stream=codec_type,width,height,r_frame_rate",
               "-of", "json", str(path)], capture=True)
    info = json.loads(out)
    streams = info.get("streams", [])
    v = next((s for s in streams if s["codec_type"] == "video"), {})
    num, den = (v.get("r_frame_rate", "24/1").split("/") + ["1"])[:2]
    return {
        "duration": float(info["format"]["duration"]),
        "has_audio": any(s["codec_type"] == "audio" for s in streams),
        "fps": float(num) / float(den or 1),
        "width": v.get("width"), "height": v.get("height"),
    }


def scene_no(path):
    m = re.search(r"scene_(\d+)", Path(path).name)
    return int(m.group(1)) if m else None


def ff_path(p):
    """Escape a path for use inside an ffmpeg filter argument."""
    return str(Path(p).resolve()).replace("\\", "/").replace(":", "\\:").replace("'", "\\'")


def fmt_tc(t):
    m, s = divmod(max(t, 0.0), 60)
    return f"{int(m)}:{s:04.1f}"


# ── scan ─────────────────────────────────────────────────────────────────

def audio_envelope(path, has_audio, duration):
    n = int(math.ceil(duration / GRID))
    if not has_audio:
        return np.full(n, -90.0)
    raw = run(["ffmpeg", "-v", "error", "-i", str(path), "-vn", "-ac", "1",
               "-ar", str(AUDIO_SR), "-f", "s16le", "-"], capture=True)
    x = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
    hop = int(AUDIO_SR * GRID)
    env = np.full(n, -90.0)
    for i in range(min(n, len(x) // hop + 1)):
        seg = x[i * hop:(i + 1) * hop]
        if len(seg):
            rms = float(np.sqrt(np.mean(seg ** 2)))
            env[i] = 20 * math.log10(rms + 1e-9)
    return env


def motion_envelope(path, duration):
    w, h = 64, 36
    raw = run(["ffmpeg", "-v", "error", "-i", str(path), "-an", "-vf",
               f"fps={MOTION_FPS},scale={w}:{h},format=gray", "-f", "rawvideo", "-"],
              capture=True)
    frames = np.frombuffer(raw, dtype=np.uint8).reshape(-1, h, w).astype(np.float32)
    diff = np.zeros(len(frames))
    if len(frames) > 1:
        diff[1:] = np.mean(np.abs(frames[1:] - frames[:-1]), axis=(1, 2))
    n = int(math.ceil(duration / GRID))
    t_frames = np.arange(len(frames)) / MOTION_FPS
    return np.interp(np.arange(n) * GRID, t_frames, diff) if len(frames) else np.zeros(n)


def norm(a, lo, hi):
    return np.clip((a - lo) / (hi - lo + 1e-9), 0, 1)


def load_dialogue(clips_json):
    if not clips_json or not Path(clips_json).exists():
        return {}
    data = json.loads(Path(clips_json).read_text(encoding="utf-8"))
    rows = data if isinstance(data, list) else data.get("clips", [])
    out = {}
    for r in rows:
        k = r.get("clip_number") or r.get("order")
        if k is not None:
            out[int(k)] = {"label": r.get("label") or r.get("scene_name") or "",
                           "line": r.get("narrator_text") or ""}
    return out


def cmd_scan(args):
    src = Path(args.clips_dir)
    clips = sorted(p for p in src.glob("*.mp4") if p.is_file())
    if args.pattern:
        clips = [p for p in clips if re.search(args.pattern, p.name)]
    if not clips:
        raise SystemExit(f"No .mp4 in {src}")
    out_dir = Path(args.out)
    frames_dir = out_dir / "candidates"
    frames_dir.mkdir(parents=True, exist_ok=True)
    dialogue = load_dialogue(args.clips_json)

    per_clip = []
    for p in clips:
        info = probe(p)
        a = audio_envelope(p, info["has_audio"], info["duration"])
        m = motion_envelope(p, info["duration"])
        n = min(len(a), len(m))
        per_clip.append((p, info, a[:n], m[:n]))
        print(f"scanned {p.name} ({info['duration']:.1f}s)", file=sys.stderr)

    # Normalise across the whole project so the most intense clips rank first.
    all_a = np.concatenate([c[2] for c in per_clip])
    all_m = np.concatenate([c[3] for c in per_clip])
    a_lo, a_hi = np.percentile(all_a[all_a > -80] if (all_a > -80).any() else all_a, [10, 99])
    m_lo, m_hi = np.percentile(all_m, [10, 99])

    cands = []
    for p, info, a, m in per_clip:
        loud = norm(a, a_lo, a_hi)
        jump = np.zeros_like(loud)
        k = int(0.5 / GRID)  # loudness rise over the previous 0.5s
        jump[k:] = np.clip(loud[k:] - loud[:-k], 0, 1)
        mot = norm(m, m_lo, m_hi)
        score = 0.45 * loud + 0.30 * jump + 0.25 * mot
        # Smooth over ~0.3s so single-sample spikes don't win.
        score = np.convolve(score, np.ones(3) / 3, mode="same")
        dur = info["duration"]
        valid = np.array([(args.skip + 0.4) <= i * GRID <= dur - 0.4 for i in range(len(score))])
        s = np.where(valid, score, -1)
        picked = []
        for _ in range(args.per_clip):
            i = int(np.argmax(s))
            if s[i] <= 0:
                break
            picked.append(i)
            lo, hi = max(0, i - int(args.min_gap / GRID)), i + int(args.min_gap / GRID) + 1
            s[lo:hi] = -1
        no = scene_no(p)
        for i in picked:
            t = i * GRID
            cin = round(max(args.skip, t - args.pre), 2)
            cout = round(min(dur, t + args.post), 2)
            d = dialogue.get(no, {})
            cands.append({
                "clip": p.as_posix(), "scene": no, "peak": round(t, 2),
                "in": cin, "out": cout, "score": round(float(score[i]), 3),
                "loud_db": round(float(a[i]), 1), "motion": round(float(mot[i]), 2),
                "label": d.get("label", ""), "line": d.get("line", ""),
            })

    cands.sort(key=lambda c: c["score"], reverse=True)
    for rank, c in enumerate(cands, 1):
        c["rank"] = rank
        jpg = frames_dir / f"{rank:02d}_scene{c['scene'] or 0:02d}_{c['peak']:.1f}s.jpg"
        run(["ffmpeg", "-v", "error", "-y", "-ss", str(c["peak"]), "-i", c["clip"],
             "-frames:v", "1", "-vf", "scale=480:-2", "-q:v", "4", str(jpg)])
        c["frame"] = jpg.as_posix()

    out_json = out_dir / "candidates.json"
    out_json.write_text(json.dumps(cands, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{'#':>3} {'score':>5} {'scene':>5} {'peak':>5}  in–out      dB    motion  label")
    for c in cands[:args.top]:
        print(f"{c['rank']:>3} {c['score']:>5.2f} {c['scene'] or '-':>5} {c['peak']:>5.1f}  "
              f"{c['in']:.1f}–{c['out']:.1f}  {c['loud_db']:>6.1f} {c['motion']:>5.2f}  {c['label'][:40]}")
    print(f"\n{len(cands)} candidates → {out_json}\nframes → {frames_dir}")


# ── build ────────────────────────────────────────────────────────────────

def atempo_chain(speed):
    parts, s = [], speed
    while s > 2.0:
        parts.append("atempo=2.0")
        s /= 2.0
    while s < 0.5:
        parts.append("atempo=0.5")
        s /= 0.5
    parts.append(f"atempo={s:.4f}")
    return ",".join(parts)


def find_font():
    return next((f for f in FONT_CANDIDATES if Path(f).exists()), None)


def drawtext(text, tmp_dir, idx, h):
    tf = tmp_dir / f"text_{idx:02d}.txt"
    tf.write_text(text, encoding="utf-8")
    font = find_font()
    font_arg = f"fontfile='{ff_path(font)}':" if font else ""
    size = int(h / 18)
    return (f",drawtext={font_arg}textfile='{ff_path(tf)}':fontcolor=white:fontsize={size}:"
            f"borderw=3:bordercolor=black:x=(w-tw)/2:y=h*0.08")


def render_segment(seg, idx, base, cut_dir, tmp_dir, W, H, FPS):
    if "black" in seg:
        frames = max(1, round(float(seg["black"]) * FPS))
        dur = frames / FPS
        name = f"{idx:02d}_black_{dur:.2f}s.mp4"
        vf = f"[0:v]format=yuv420p{drawtext(seg['text'], tmp_dir, idx, H) if seg.get('text') else ''}[v]"
        cmd = ["ffmpeg", "-v", "error", "-y",
               "-f", "lavfi", "-i", f"color=c=black:s={W}x{H}:r={FPS}:d={dur}",
               "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
               "-filter_complex", vf, "-map", "[v]", "-map", "1:a"]
        src_info = None
    else:
        clip = (base / seg["clip"]).resolve()
        if not clip.exists():
            raise SystemExit(f"Segment {idx}: clip not found: {clip}")
        info = probe(clip)
        cin, cout = float(seg["in"]), float(seg["out"])
        if not (0 <= cin < cout <= info["duration"] + 0.05):
            raise SystemExit(f"Segment {idx}: in/out {cin}-{cout} outside 0-{info['duration']:.2f} ({clip.name})")
        speed = float(seg.get("speed", 1.0))
        frames = max(1, round((cout - cin) / speed * FPS))
        dur = frames / FPS
        name = f"{idx:02d}_scene{scene_no(clip) or 0:02d}_{cin:.2f}-{cout:.2f}.mp4"
        text = drawtext(seg["text"], tmp_dir, idx, H) if seg.get("text") else ""
        zoom = float(seg.get("zoom", 1.0))
        zoom_f = (f",scale=iw*{zoom}:ih*{zoom},crop={W}:{H}" if zoom > 1.0 else "")
        vchain = (f"[0:v]setpts=(PTS-STARTPTS)/{speed},fps={FPS},"
                  f"scale={W}:{H}:force_original_aspect_ratio=decrease,"
                  f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2{zoom_f},setsar=1{text},format=yuv420p[v]")
        mute = seg.get("audio", "keep") == "mute" or not info["has_audio"]
        if mute:
            achain = "[1:a]anull[a]"
            ainputs = ["-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo"]
        else:
            g = float(seg.get("gain_db", 0))
            fade_out = max(0.0, dur - 0.012)
            achain = (f"[0:a]asetpts=PTS-STARTPTS,{atempo_chain(speed)},aresample=48000,"
                      f"aformat=channel_layouts=stereo,volume={g}dB,"
                      f"afade=t=in:d=0.012,afade=t=out:st={fade_out:.3f}:d=0.012,apad[a]")
            ainputs = []
        cmd = ["ffmpeg", "-v", "error", "-y", "-ss", f"{cin:.3f}", "-t", f"{cout - cin:.3f}",
               "-i", str(clip), *ainputs,
               "-filter_complex", f"{vchain};{achain}", "-map", "[v]", "-map", "[a]"]
        src_info = {"clip": seg["clip"], "in": cin, "out": cout, "speed": speed}
    out = cut_dir / name
    cmd += ["-t", f"{dur:.4f}", "-c:v", "libx264", "-preset", "fast", "-crf", "16",
            "-r", str(FPS), "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
            "-ar", "48000", str(out)]
    run(cmd)
    return out, dur, src_info


SFX_SYNTH = {
    # Placeholders for the draft only; swap for CapCut library SFX in the polish.
    "impact": ("aevalsrc=exprs='0.85*sin(2*PI*52*t)*exp(-4.5*t)+0.45*sin(2*PI*104*t)*exp(-8*t)"
               "+0.5*(random(0)*2-1)*exp(-35*t)':s=48000:d=1.4", 0.0),
    "whoosh": ("anoisesrc=d=0.8:c=pink:r=48000:a=0.9,bandpass=f=900:width_type=o:w=2,"
               "volume='pow(sin(PI*t/0.8),3)':eval=frame", 0.45),
    "riser": ("aevalsrc=exprs='0.35*sin(2*PI*(120*t+180*t*t))*(t/2)+0.25*(random(0)*2-1)*pow(t/2,2)'"
              ":s=48000:d=2.0", 2.0),
}


def sfx_file(kind, sfx_dir):
    sfx_dir.mkdir(parents=True, exist_ok=True)
    out = sfx_dir / f"{kind}.wav"
    if not out.exists():
        src, _ = SFX_SYNTH[kind]
        run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", src,
             "-af", "aformat=channel_layouts=stereo,alimiter=limit=0.9:level=0", str(out)])
    return out


def build_version(cfg, version, segs, base, out_dir):
    W, H, FPS = int(cfg.get("width", 1920)), int(cfg.get("height", 1080)), int(cfg.get("fps", 24))
    vdir = out_dir / version
    cut_dir, tmp_dir = vdir / "cuts", vdir / "_tmp"
    if cut_dir.exists():
        shutil.rmtree(cut_dir)
    cut_dir.mkdir(parents=True)
    tmp_dir.mkdir(parents=True, exist_ok=True)

    rendered, t, sfx_events, rows = [], 0.0, [], []
    for idx, seg in enumerate(segs, 1):
        path, dur, src = render_segment(seg, idx, base, cut_dir, tmp_dir, W, H, FPS)
        rendered.append(path)
        for s in seg.get("sfx", []):
            s = {"type": s} if isinstance(s, str) else dict(s)
            kind = s["type"]
            if kind in SFX_SYNTH:
                f, lead = sfx_file(kind, out_dir / "sfx"), SFX_SYNTH[kind][1]
            else:
                f, lead = (base / kind).resolve(), float(s.get("lead", 0))
            start = max(0.0, t - lead + float(s.get("offset", 0)))
            sfx_events.append((f, start, float(s.get("gain_db", -8 if kind == "impact" else -10)), kind))
        rows.append((idx, t, t + dur, src, seg))
        t += dur
    total = t

    # Assemble: concat all segments, mix placeholder SFX and optional music.
    inputs, fc = [], []
    for p in rendered:
        inputs += ["-i", str(p)]
    n = len(rendered)
    fc.append("".join(f"[{i}:v][{i}:a]" for i in range(n)) + f"concat=n={n}:v=1:a=1[v][a0]")
    mix = ["[a0]"]
    k = n
    for f, start, gain, _ in sfx_events:
        inputs += ["-i", str(f)]
        ms = int(start * 1000)
        fc.append(f"[{k}:a]aformat=channel_layouts=stereo,aresample=48000,volume={gain}dB,"
                  f"adelay={ms}|{ms}[s{k}]")
        mix.append(f"[s{k}]")
        k += 1
    music = cfg.get("music")
    if music:
        mf = (base / music["file"]).resolve()
        inputs += ["-stream_loop", "-1", "-i", str(mf)]
        mstart = float(music.get("start", 0))
        fc.append(f"[{k}:a]atrim=start={mstart}:duration={total:.3f},asetpts=PTS-STARTPTS,"
                  f"aformat=channel_layouts=stereo,aresample=48000,volume={float(music.get('gain_db', -18))}dB,"
                  f"afade=t=out:st={max(0, total - 0.4):.3f}:d=0.4[mu]")
        mix.append("[mu]")
    # Preview at YouTube loudness so drafts compare fairly; the real master is
    # still the ffmpeg loudnorm step in SKILL.md, run on the CapCut export.
    loud = ",loudnorm=I=-14:LRA=11:TP=-1.0,aresample=48000,alimiter=limit=0.89:level=0" if cfg.get("loudnorm", True) else ""
    fc.append(f"{''.join(mix)}amix=inputs={len(mix)}:normalize=0:duration=first,"
              f"alimiter=limit=0.95:level=0{loud}[a]")
    draft = out_dir / f"trailer_{version}.mp4"
    run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(fc),
         "-map", "[v]", "-map", "[a]", "-t", f"{total:.4f}", "-c:v", "libx264",
         "-preset", "fast", "-crf", "18", "-r", str(FPS), "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", str(draft)])
    shutil.rmtree(tmp_dir, ignore_errors=True)

    # Timeline sheet for the CapCut polish.
    md = [f"# Trailer {version} — {fmt_tc(total)} ({len(segs)} đoạn)", "",
          f"Bản nháp: `{draft.name}` · đoạn cắt sẵn: `{version}/cuts/` (import theo thứ tự tên).",
          "SFX trong bản nháp là âm tạm do script tổng hợp; khi dựng thật, thay bằng Sound effects của CapCut.", "",
          "| # | TL | Dài | Nguồn | Vào–ra (nguồn) | Tốc độ | Chữ | SFX | Ghi chú |",
          "|---|---|---|---|---|---|---|---|---|"]
    for idx, a, b, src, seg in rows:
        sfx = ", ".join(s if isinstance(s, str) else s["type"] for s in seg.get("sfx", []))
        if src:
            name = Path(src["clip"]).name
            io = f"{src['in']:.2f}–{src['out']:.2f}"
            sp = f"{src['speed']:g}×"
        else:
            name, io, sp = "ĐEN", "—", "—"
        md.append(f"| {idx} | {fmt_tc(a)}–{fmt_tc(b)} | {b - a:.2f}s | {name} | {io} | {sp} | "
                  f"{seg.get('text', '')} | {sfx} | {seg.get('note', '')} |")
    (out_dir / f"trailer_{version}_timeline.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"{version}: {fmt_tc(total)} · {len(segs)} segments → {draft}")
    return draft


def cmd_build(args):
    cl = Path(args.cutlist).resolve()
    cfg = json.loads(cl.read_text(encoding="utf-8"))
    base = (cl.parent / cfg.get("project_dir", "..")).resolve()
    out_dir = (cl.parent / cfg.get("out_dir", ".")).resolve()
    versions = cfg["versions"]
    names = [args.version] if args.version else list(versions)
    for v in names:
        if v not in versions:
            raise SystemExit(f"Version '{v}' not in cut list (have: {', '.join(versions)})")
        build_version(cfg, v, versions[v], base, out_dir)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("scan", help="rank intense moments across clips")
    s.add_argument("clips_dir")
    s.add_argument("--out", required=True, help="output folder (e.g. output/<slug>/trailer)")
    s.add_argument("--clips-json", help="clips.json to attach labels / dialogue")
    s.add_argument("--pattern", help="regex on file name, e.g. 'clean' to skip raw files")
    s.add_argument("--skip", type=float, default=1.0, help="ignore the first N seconds (Rule 49)")
    s.add_argument("--per-clip", type=int, default=2, help="max candidates per clip")
    s.add_argument("--min-gap", type=float, default=2.0, help="min seconds between picks in a clip")
    s.add_argument("--pre", type=float, default=0.6, help="seconds kept before the peak")
    s.add_argument("--post", type=float, default=1.0, help="seconds kept after the peak")
    s.add_argument("--top", type=int, default=30, help="rows printed")
    s.set_defaults(func=cmd_scan)
    b = sub.add_parser("build", help="cut segments and assemble draft trailer(s)")
    b.add_argument("cutlist")
    b.add_argument("--version", help="build only this version (default: all)")
    b.set_defaults(func=cmd_build)
    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
