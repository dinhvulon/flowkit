import os
import subprocess
import sys
import shutil

sys.stdout.reconfigure(encoding="utf-8")

proj_dir = "output/time_travel_vlog_ancient_babylon_570_bc"
scenes_dir = os.path.join(proj_dir, "scenes")
final_out = os.path.join(proj_dir, "time_travel_vlog_ancient_babylon_570_bc_final.mp4")
brain_out = r"C:\Users\Administrator\.gemini\antigravity-ide\brain\e22150ce-4262-4e3c-8619-a7731a7f7c3a\babylon_570bc_final_vlog.mp4"

# Find and sort all scene files
files = sorted([f for f in os.listdir(scenes_dir) if f.startswith("scene_") and f.endswith(".mp4")])
print(f"Found {len(files)} scene video files.")

concat_txt_path = os.path.join(proj_dir, "concat.txt")
with open(concat_txt_path, "w", encoding="utf-8") as f:
    for filename in files:
        full_path = os.path.abspath(os.path.join(scenes_dir, filename)).replace("\\", "/")
        f.write(f"file '{full_path}'\n")

print(f"Wrote concat list to {concat_txt_path}")

cmd = [
    "ffmpeg", "-y",
    "-f", "concat",
    "-safe", "0",
    "-i", concat_txt_path,
    "-c", "copy",
    "-movflags", "+faststart",
    final_out
]

print("Running ffmpeg concat...", flush=True)
res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode != 0:
    print("Direct copy concat failed, trying re-encode concat...", flush=True)
    cmd_reencode = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", concat_txt_path,
        "-c:v", "libx264", "-preset", "fast", "-crf", "18",
        "-r", "24", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart",
        final_out
    ]
    res2 = subprocess.run(cmd_reencode, capture_output=True, text=True)
    if res2.returncode != 0:
        print("Re-encode concat failed:", res2.stderr)
        sys.exit(1)

print(f"Final video successfully created at: {final_out}")
file_size_mb = os.path.getsize(final_out) / (1024 * 1024)
print(f"File size: {file_size_mb:.1f} MB")

# Probe duration
probe_cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", final_out]
dur_res = subprocess.run(probe_cmd, capture_output=True, text=True)
duration_secs = float(dur_res.stdout.strip())
mins = int(duration_secs // 60)
secs = int(duration_secs % 60)
print(f"Total Duration: {mins:02d}:{secs:02d} ({duration_secs:.1f} seconds)")

# Copy to brain artifacts
shutil.copy(final_out, brain_out)
print(f"Copied to brain artifacts: {brain_out}")
