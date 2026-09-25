import json
import os
import sys
import time
import urllib.request
import urllib.error

sys.stdout.reconfigure(encoding="utf-8")

PROJECT_ID = "6224591f-b884-42f2-8f57-613bc86d66fb"
VIDEO_ID = "71909a60-29f7-460e-807c-ed48b8a12ad1"
OUT_DIR = os.path.join("output", "time_travel_vlog_hanging_gardens_of_babylon_570_bc", "scenes")
os.makedirs(OUT_DIR, exist_ok=True)

BASE_URL = "http://127.0.0.1:8100"

downloaded = set()
retries = {}

def get_scenes():
    url = f"{BASE_URL}/api/scenes?video_id={VIDEO_ID}"
    req = urllib.request.urlopen(url)
    return json.loads(req.read())

def download_file(url, target_path):
    temp_path = target_path + ".tmp"
    headers = {"User-Agent": "Mozilla/5.0"}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=60) as response, open(temp_path, "wb") as out_file:
        out_file.write(response.read())
    os.replace(temp_path, target_path)

def retry_video(sid):
    count = retries.get(sid, 0)
    if count >= 5:
        print(f"[RETRY MAX REACHED] Scene {sid[:8]} failed 5 times, stopping retry.")
        return False
    retries[sid] = count + 1
    print(f"[AUTO-RETRY] Retrying video for scene {sid[:8]} (attempt {retries[sid]}/5)...")
    payload = {
        "requests": [
            {
                "type": "REGENERATE_VIDEO",
                "scene_id": sid,
                "project_id": PROJECT_ID,
                "video_id": VIDEO_ID,
                "orientation": "HORIZONTAL"
            }
        ]
    }
    req = urllib.request.Request(
        f"{BASE_URL}/api/requests/batch",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    try:
        resp = urllib.request.urlopen(req)
        print(f"[AUTO-RETRY] Submitted retry for {sid[:8]}")
        return True
    except Exception as e:
        print(f"[AUTO-RETRY ERROR] {e}")
        return False

print(f"Starting video monitor and rolling download for video {VIDEO_ID}...")

MAX_POLLS = 120 # ~30-40 minutes max
for poll in range(1, MAX_POLLS + 1):
    time.sleep(15)
    try:
        scenes = get_scenes()
    except Exception as e:
        print(f"Error fetching scenes: {e}")
        continue

    total = len(scenes)
    completed = 0
    failed = 0
    processing = 0
    pending = 0

    for s in scenes:
        sid = s["id"]
        idx = s.get("display_order", 0) + 1
        status = s.get("horizontal_video_status")
        video_url = s.get("horizontal_video_url")
        media_id = s.get("horizontal_video_media_id")

        if status == "COMPLETED" and video_url:
            completed += 1
            filename = f"scene_{idx:03d}_{sid}.mp4"
            target_path = os.path.join(OUT_DIR, filename)
            if sid not in downloaded:
                if not os.path.exists(target_path) or os.path.getsize(target_path) == 0:
                    try:
                        print(f"[{completed}/{total}] Downloading Scene {idx:02d} ({media_id[:8]}) -> {filename}...")
                        download_file(video_url, target_path)
                        size_mb = os.path.getsize(target_path) / (1024 * 1024)
                        print(f"✓ Scene {idx:02d} downloaded successfully ({size_mb:.2f} MB)")
                    except Exception as e:
                        print(f"✗ Failed to download Scene {idx:02d}: {e}")
                downloaded.add(sid)
        elif status == "FAILED":
            failed += 1
            # Check if retry needed
            if sid not in retries or retries[sid] < 5:
                retry_video(sid)
        elif status == "PROCESSING":
            processing += 1
        else:
            pending += 1

    print(f"Poll {poll:02d}: Total={total} | Completed={completed} | Processing={processing} | Pending={pending} | Failed={failed}")

    if completed == total:
        print(f"★ ALL {total} SCENE VIDEOS GENERATED AND DOWNLOADED TO DISK!")
        break
