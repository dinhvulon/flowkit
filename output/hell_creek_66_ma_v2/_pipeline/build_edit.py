"""Build the edit (Rule 66) for Hell Creek 66Ma v2 -- no upscale (user 2026-10-16).

Act 1 = hell_creek_act1_1080p.mp4 (final, already joined) -- used as-is.
Act 2+ = 720p clips in scenes/ -> remove_watermark_video -> scenes_clean/*_clean.mp4
          -> trim (Rule 49 in-points + review cuts) -> lanczos 1920x1080, 24fps segment.
A2-R3 is dropped (user). Chain followers (PREV_LAST_FRAME) start at 0.04s so the seam stays continuous.

  python build_edit.py prep 2 3 4        # clean + trim every clip of these acts (idempotent)
  python build_edit.py render v2 2 3 4   # concat Act1 + segments, -14 LUFS / -1 dBTP -> edit/edit_v2.mp4 (+ EDL)
edit_v1 (16/10) = acts 2 3. Never re-render a delivered version; pick the next vN.
"""
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path("C:/flowkit")
OUT = ROOT / "output/hell_creek_66_ma_v2"
SRC, CLEAN, EDIT, WORK = OUT / "scenes", OUT / "scenes_clean", OUT / "edit", OUT / "edit/work"
WORK.mkdir(parents=True, exist_ok=True)
CLEAN.mkdir(exist_ok=True)
sys.path.insert(0, str(ROOT))
ACTS = (2, 3)  # overridden by the act numbers on the command line
SKIP = {"A2-R3"}
# review cuts: A3-08 jumps at 3s, A3-W1 background jumps at ~5.2s, A2-10 hard cut at 2.46s,
# A2-13 (regen 16/10) arm drifts after 5.2s
IN_PT = {"A3-08": 0.5, "A2-10": 2.5, "A4-17": 2.2}
OUT_PT = {"A3-08": 3.0, "A3-W1": 5.0, "A2-13": 5.2,
          "A4-01": 3.5, "A4-11": 2.7, "A4-16": 5.5, "MASTER": 8.5}  # Act 4 review trims (user OK 16/10)
# Act 1 (final file) minus 87.65-90.55s: the triceratops tumble (user 16/10). edit_v1 used it whole;
# edit_v2 also dropped the Nora-in-mud clip (90.55-97.56), which the user wants kept.
ACT1_KEEP = [(0, 87.65), (90.55, 106.57)]


def clips():
    out = []
    for act in ACTS:
        for c in json.loads((OUT / f"prompts_act{act}.json").read_text(encoding="utf-8")):
            cid = c["clip_id"]
            if cid in SKIP:
                continue
            src = sorted(p for p in SRC.glob(f"scene_*_{cid}_*.mp4")
                         if re.fullmatch(rf"scene_\d+_{re.escape(cid)}_[0-9a-f]{{8}}\.mp4", p.name))
            if len(src) > 1:
                sys.exit(f"{cid}: several files {[p.name for p in src]}")
            follower = (c.get("start_frame") or {}).get("type") == "PREV_LAST_FRAME"
            d = c["duration"]
            t_in = IN_PT.get(cid, 0.04 if follower else (0.5 if d == 4 else 1.0))
            out.append(dict(act=act, cid=cid, t_in=t_in, t_out=OUT_PT.get(cid, d), src=src[0] if src else None))
    return out


def run(cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def prep():
    from agent.services.watermark import remove_watermark_video
    missing = []
    for c in clips():
        seg = WORK / f"A{c['act']}_{c['cid']}_seg.mp4"
        if seg.exists():
            continue
        if not c["src"]:
            missing.append(c["cid"]); continue
        clean = CLEAN / (c["src"].stem + "_clean.mp4")
        if not clean.exists():
            remove_watermark_video(str(c["src"]), str(clean))
        run(["ffmpeg", "-y", "-ss", str(c["t_in"]), "-i", str(clean), "-t", f"{c['t_out'] - c['t_in']:.3f}",
             "-vf", "scale=1920:1080:flags=lanczos,fps=24,format=yuv420p,setsar=1",
             "-af", "aresample=48000,aformat=channel_layouts=stereo",
             "-c:v", "libx264", "-preset", "medium", "-crf", "17", "-c:a", "aac", "-b:a", "192k", str(seg)])
        print("prepped", c["cid"], flush=True)
    print("missing:", missing or "none", flush=True)
    return missing


def dur(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                                capture_output=True, text=True).stdout.strip())


def render(ver):
    final = EDIT / f"edit_{ver}.mp4"
    if final.exists():
        sys.exit(f"{final.name} exists; pick a new version")
    if prep():
        sys.exit("clips missing; not rendering")
    a1 = []
    for i, (s, e) in enumerate(ACT1_KEEP, 1):
        p = WORK / f"A1_part{i}.mp4"
        if not p.exists():
            run(["ffmpeg", "-y", "-ss", str(s), "-to", str(e), "-i", str(OUT / "hell_creek_act1_1080p.mp4"),
                 "-vf", "fps=24,format=yuv420p,setsar=1", "-af", "aresample=48000,aformat=channel_layouts=stereo",
                 "-c:v", "libx264", "-preset", "medium", "-crf", "17", "-c:a", "aac", "-b:a", "192k", str(p)])
        a1.append(("A1", f"ACT1_{s:g}-{e:g}", p))
    parts = a1 + [(f"A{c['act']}", c["cid"], WORK / f"A{c['act']}_{c['cid']}_seg.mp4") for c in clips()]
    edl, t = ["act,clip,source,start,end,length"], 0.0
    for act, cid, p in parts:
        d = dur(p); edl.append(f"{act},{cid},{p.name},{t:.2f},{t + d:.2f},{d:.2f}"); t += d
    (EDIT / f"edit_{ver}_edl.csv").write_text("\n".join(edl), encoding="utf-8")
    lst = WORK / f"concat_{ver}.txt"
    lst.write_text("".join(f"file '{p.as_posix()}'\n" for _, _, p in parts), encoding="utf-8")
    raw = WORK / f"edit_{ver}_raw.mp4"
    # re-encode concat: Act 1 and the segments come from different encoders
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(lst),
         "-vf", "fps=24,format=yuv420p,setsar=1", "-c:v", "libx264", "-preset", "medium", "-crf", "17",
         "-af", "aresample=48000", "-c:a", "aac", "-b:a", "192k", str(raw)])
    m = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(raw), "-af", "loudnorm=I=-14:TP=-1:LRA=11:print_format=json",
                        "-f", "null", "-"], capture_output=True, text=True).stderr
    j = json.loads(m[m.rindex("{"):m.rindex("}") + 1])
    ln = (f"loudnorm=I=-14:TP=-1:LRA=11:measured_I={j['input_i']}:measured_TP={j['input_tp']}:"
          f"measured_LRA={j['input_lra']}:measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true")
    run(["ffmpeg", "-y", "-i", str(raw), "-c:v", "copy", "-af", ln + ",aresample=48000", "-c:a", "aac", "-b:a", "192k",
         "-movflags", "+faststart", str(final)])
    print("rendered", final, f"{t:.1f}s", flush=True)


if __name__ == "__main__":
    nums = [a for a in sys.argv[2:] if a.isdigit()]
    ACTS = tuple(int(a) for a in nums) or (2, 3)
    prep() if sys.argv[1] == "prep" else render(sys.argv[2])
