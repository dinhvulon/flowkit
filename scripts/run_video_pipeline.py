import json
import urllib.request
import sqlite3
import os
import sys
import time
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8")

pid = "ac50c619-1b31-4847-95d6-5379d02554c7"
vid = "dc2afa55-8a7f-42c3-bf8c-a13f580b6830"
p_out = json.loads(urllib.request.urlopen(f"http://127.0.0.1:8100/api/projects/{pid}/output-dir").read())
project_dir = p_out.get("path")
scenes_dir = os.path.join(project_dir, "scenes")
os.makedirs(scenes_dir, exist_ok=True)

brain_scenes_dir = r"C:\Users\Administrator\.gemini\antigravity-ide\brain\e22150ce-4262-4e3c-8619-a7731a7f7c3a\scenes"
os.makedirs(brain_scenes_dir, exist_ok=True)

print(f"[{datetime.now().strftime('%H:%M:%S')}] 1. Checking scenes ready for video generation...", flush=True)

conn = sqlite3.connect("flow_agent.db")
c = conn.cursor()
c.execute("""
    SELECT id, display_order, horizontal_image_media_id, horizontal_video_status
    FROM scene
    WHERE video_id = ?
    ORDER BY display_order ASC
""", (vid,))
scenes = c.fetchall()
conn.close()

print(f"Total scenes: {len(scenes)}", flush=True)

# Pre-flight check
for sid, order, img_mid, vstatus in scenes:
    if not img_mid:
        raise RuntimeError(f"Scene {order+1} is missing horizontal_image_media_id!")

# Build batch request payload
requests_payload = []
for sid, order, img_mid, vstatus in scenes:
    if vstatus != "COMPLETED":
        requests_payload.append({
            "type": "GENERATE_VIDEO",
            "scene_id": sid,
            "project_id": pid,
            "video_id": vid,
            "orientation": "HORIZONTAL"
        })

print(f"[{datetime.now().strftime('%H:%M:%S')}] 2. Submitting GENERATE_VIDEO batch for {len(requests_payload)} scenes...", flush=True)
req = urllib.request.Request(
    "http://127.0.0.1:8100/api/requests/batch",
    data=json.dumps({"requests": requests_payload}).encode("utf-8"),
    headers={"Content-Type": "application/json"}
)
with urllib.request.urlopen(req) as resp:
    res = json.loads(resp.read())
    print(f"Batch submitted! Response count: {len(res)}", flush=True)

# Polling and rolling download loop
downloaded = set()
retries = {sid: 0 for sid, order, img_mid, vstatus in scenes}
max_retries = 5

print(f"[{datetime.now().strftime('%H:%M:%S')}] 3. Monitoring video generation and performing rolling downloads...", flush=True)

poll_url = f"http://127.0.0.1:8100/api/requests/batch-status?video_id={vid}&type=GENERATE_VIDEO"

while True:
    time.sleep(15)
    now_str = datetime.now().strftime("%H:%M:%S")

    # Check batch status
    try:
        bs_resp = json.loads(urllib.request.urlopen(poll_url).read())
        total = bs_resp.get("total", len(scenes))
        completed = bs_resp.get("completed", 0)
        pending = bs_resp.get("pending", 0)
        processing = bs_resp.get("processing", 0)
        failed = bs_resp.get("failed", 0)
        is_done = bs_resp.get("done", False)
    except Exception as e:
        print(f"[{now_str}] Error polling batch status: {e}", flush=True)
        completed, pending, processing, failed, is_done = 0, 0, 0, 0, False

    # Check database scenes for completed videos & rolling download
    conn = sqlite3.connect("flow_agent.db")
    c = conn.cursor()
    c.execute("""
        SELECT id, display_order, horizontal_video_status, horizontal_video_url, horizontal_video_media_id
        FROM scene
        WHERE video_id = ?
        ORDER BY display_order ASC
    """, (vid,))
    current_scenes = c.fetchall()
    conn.close()

    completed_in_db = 0
    for sid, order, vstatus, vurl, vmid in current_scenes:
        sidx = order + 1
        local_filename = f"scene_{sidx:02d}_{sid[:8]}.mp4"
        local_path = os.path.join(scenes_dir, local_filename)
        brain_path = os.path.join(brain_scenes_dir, f"scene_{sidx:02d}.mp4")

        if vstatus == "COMPLETED":
            completed_in_db += 1
            if sid not in downloaded:
                if vurl:
                    print(f"[{now_str}] [Scene {sidx:02d}] Video COMPLETED! Downloading...", flush=True)
                    try:
                        h = {"User-Agent": "Mozilla/5.0"}
                        dl_req = urllib.request.Request(vurl, headers=h)
                        with urllib.request.urlopen(dl_req, timeout=60) as v_resp:
                            video_bytes = v_resp.read()
                            with open(local_path, "wb") as vf:
                                vf.write(video_bytes)
                            with open(brain_path, "wb") as bf:
                                bf.write(video_bytes)
                        downloaded.add(sid)
                        print(f"[{now_str}] [Scene {sidx:02d}] Successfully downloaded ({len(video_bytes)/(1024*1024):.1f} MB)", flush=True)
                    except Exception as e:
                        print(f"[{now_str}] [Scene {sidx:02d}] Download error: {e}", flush=True)
                elif os.path.exists(local_path):
                    downloaded.add(sid)

        elif vstatus == "FAILED":
            if retries[sid] < max_retries:
                retries[sid] += 1
                print(f"[{now_str}] [Scene {sidx:02d}] FAILED. Auto-retrying (attempt {retries[sid]}/{max_retries})...", flush=True)
                retry_payload = {
                    "requests": [{
                        "type": "GENERATE_VIDEO",
                        "scene_id": sid,
                        "project_id": pid,
                        "video_id": vid,
                        "orientation": "HORIZONTAL"
                    }]
                }
                try:
                    r_req = urllib.request.Request(
                        "http://127.0.0.1:8100/api/requests/batch",
                        data=json.dumps(retry_payload).encode("utf-8"),
                        headers={"Content-Type": "application/json"}
                    )
                    urllib.request.urlopen(r_req)
                except Exception as re:
                    print(f"[{now_str}] [Scene {sidx:02d}] Retry submission error: {re}", flush=True)
            else:
                print(f"[{now_str}] [Scene {sidx:02d}] FAILED permanently after {max_retries} retries!", flush=True)

    print(f"[{now_str}] Status: Completed={completed_in_db}/23 | Processing={processing} | Pending={pending} | Downloaded={len(downloaded)}/23", flush=True)

    if completed_in_db == len(scenes) and len(downloaded) == len(scenes):
        print(f"[{now_str}] ALL {len(scenes)} VIDEOS GENERATED AND DOWNLOADED LOCALLY!", flush=True)
        break

    # If queue is done and all scenes either completed or exhausted retries
    if is_done and pending == 0 and processing == 0:
        all_resolved = True
        for sid, order, vstatus, vurl, vmid in current_scenes:
            if vstatus != "COMPLETED" and retries[sid] < max_retries:
                all_resolved = False
                break
        if all_resolved:
            print(f"[{now_str}] Queue finished. Completed: {completed_in_db}/{len(scenes)}", flush=True)
            break

print("\n=======================================================")
print(f"VIDEO GENERATION FINISHED: {len(downloaded)}/{len(scenes)} downloaded")
print(f"Scenes directory: {scenes_dir}")
print("=======================================================")
