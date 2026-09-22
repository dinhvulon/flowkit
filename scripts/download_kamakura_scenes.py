import sys
import json
import urllib.request
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

VID = "4427d959-7e30-4b68-b12f-e549611167c3"
OUTDIR = Path("output/kamakura_1274_mongol_invasion_hakata_bay_pov_vlog/scenes")
OUTDIR.mkdir(parents=True, exist_ok=True)

url = f"http://127.0.0.1:8100/api/scenes?video_id={VID}"
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as resp:
    scenes = json.loads(resp.read())

scenes = sorted(scenes, key=lambda s: s.get("display_order", 0))

print(f"Total scenes: {len(scenes)}")
for s in scenes:
    order = s.get("display_order", 0)
    sid = s["id"]
    status = s.get("vertical_video_status")
    video_url = s.get("vertical_video_url")
    filename = f"scene_{order:03d}_{sid}.mp4"
    dest = OUTDIR / filename

    if dest.exists() and dest.stat().st_size > 100000:
        print(f"  [=] Scene {order} ({status}) already downloaded: {filename} ({dest.stat().st_size // (1024*1024):.1f} MB)")
        continue

    if status == "COMPLETED" and video_url:
        print(f"  [*] Downloading Scene {order} ({status}) -> {filename}...")
        try:
            urllib.request.urlretrieve(video_url, dest)
            print(f"      Downloaded {dest.stat().st_size // 1024} KB")
        except Exception as e:
            print(f"      [!] Download failed for Scene {order}: {e}")
    else:
        print(f"  [-] Scene {order} not ready yet: status={status}")
