#!/usr/bin/env python3
"""
Concatenate all scene videos for Kamakura 1274 into a final vertical 9:16 vlog video.
"""
import sys
import shutil
import subprocess
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
OUT_DIR = BASE_DIR / "output" / "kamakura_1274_mongol_invasion_hakata_bay_pov_vlog"
SCENES_DIR = OUT_DIR / "scenes"
NORM_DIR = OUT_DIR / "norm"
FINAL_FILE = OUT_DIR / "kamakura_1274_final.mp4"

ffmpeg_bin = shutil.which("ffmpeg") or "ffmpeg"

def run_concat():
    NORM_DIR.mkdir(parents=True, exist_ok=True)
    video_files = sorted(list(SCENES_DIR.glob("scene_*.mp4")))
    if not video_files:
        print("[!] No scene videos found in:", SCENES_DIR)
        return False

    print(f"[*] Found {len(video_files)} scene videos to concatenate:")
    for v in video_files:
        print(f"  - {v.name} ({v.stat().st_size / (1024*1024):.1f} MB)")

    # 1. Normalize each scene video (1080x1920, 24fps, yuv420p, aac)
    norm_files = []
    for idx, v in enumerate(video_files):
        out_norm = NORM_DIR / f"norm_{v.name}"
        norm_files.append(out_norm)
        if not out_norm.exists() or out_norm.stat().st_size == 0:
            print(f"[*] Normalizing {v.name} -> {out_norm.name}...")
            cmd = [
                ffmpeg_bin, "-y",
                "-i", str(v),
                "-c:v", "libx264", "-preset", "fast", "-crf", "18",
                "-vf", "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2",
                "-r", "24", "-pix_fmt", "yuv420p",
                "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                "-movflags", "+faststart",
                str(out_norm)
            ]
            res = subprocess.run(cmd, capture_output=True, text=True)
            if res.returncode != 0:
                print(f"[!] Normalization error for {v.name}:", res.stderr[-500:])
                return False
        else:
            print(f"  - Normalized already exists: {out_norm.name}")

    # 2. Write concat list
    concat_list_file = NORM_DIR / "concat_list.txt"
    with open(concat_list_file, "w", encoding="utf-8") as f:
        for nf in norm_files:
            escaped_path = str(nf.resolve()).replace("\\", "/")
            f.write(f"file '{escaped_path}'\n")

    # 3. Concat demuxer
    print(f"[*] Concatenating {len(norm_files)} normalized videos into {FINAL_FILE.name}...")
    concat_cmd = [
        ffmpeg_bin, "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", str(concat_list_file),
        "-c", "copy",
        "-movflags", "+faststart",
        str(FINAL_FILE)
    ]
    res = subprocess.run(concat_cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("[!] Concat error:", res.stderr[-500:])
        return False

    final_size_mb = FINAL_FILE.stat().st_size / (1024 * 1024)
    print(f"\n[+] Success! Final video created: {FINAL_FILE} ({final_size_mb:.1f} MB)")
    return True

if __name__ == "__main__":
    success = run_concat()
    sys.exit(0 if success else 1)
