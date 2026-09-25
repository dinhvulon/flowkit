import urllib.request
import json
import time
import sqlite3
import os

PID = "ac50c619-1b31-4847-95d6-5379d02554c7"
VID = "dc2afa55-8a7f-42c3-bf8c-a13f580b6830"
ORI = "HORIZONTAL"

TARGET_SCENES = [
    ("Scene 03", "27404416-f641-4587-8340-f0f40c8ef3b7", 3),
    ("Scene 08", "1d8003fe-1fe6-4a00-9f33-2a16fc1d873b", 8),
    ("Scene 10", "9fd3ec6d-b8bd-4343-abf2-2239c8c85f08", 10),
    ("Scene 12", "7bd21651-e8cd-44c1-9259-202e2425ed0f", 12),
    ("Scene 15", "e2976cc7-5a59-41c3-a573-b7e3616ed969", 15),
    ("Scene 16", "19a26b18-4b08-40c0-897b-99b36ca5b421", 16),
    ("Scene 20", "0fa349bb-c3db-4049-bab8-de4ddf0c3a8a", 20),
    ("Scene 23", "5695d17a-2861-4987-81c6-8070caaa682c", 23),
]

outdir = os.path.join("output", "time_travel_vlog_ancient_babylon_570_bc", "scenes")
os.makedirs(outdir, exist_ok=True)

downloaded = set()
retry_counts = {sid: 0 for _, sid, _ in TARGET_SCENES}
max_retries = 5

start_time = time.time()
print(f"Monitoring 8 target scenes video generation...")

while True:
    conn = sqlite3.connect("flow_agent.db")
    cur = conn.cursor()
    
    all_done = True
    any_failed = False

    for name, sid, idx in TARGET_SCENES:
        cur.execute("SELECT horizontal_video_status, horizontal_video_url, horizontal_video_media_id FROM scene WHERE id=?", (sid,))
        row = cur.fetchone()
        status, v_url, v_mid = row if row else (None, None, None)
        
        # Check active requests for error
        cur.execute("SELECT status, error_message FROM request WHERE scene_id=? AND type='GENERATE_VIDEO' ORDER BY created_at DESC LIMIT 1", (sid,))
        req_row = cur.fetchone()
        req_status, err_msg = req_row if req_row else (None, None)

        if status == "COMPLETED" and v_url:
            target_path = os.path.join(outdir, f"scene_{idx:02d}_{sid[:8]}.mp4")
            if sid not in downloaded:
                print(f"[{time.strftime('%H:%M:%S')}] {name} COMPLETED! Media ID: {v_mid}. Downloading to {target_path}...")
                try:
                    urllib.request.urlretrieve(v_url, target_path)
                    sz = os.path.getsize(target_path)
                    print(f"[{time.strftime('%H:%M:%S')}] {name} downloaded successfully ({sz} bytes).")
                    downloaded.add(sid)
                except Exception as e:
                    print(f"Error downloading {name}: {e}")
        elif req_status == "FAILED" or status == "FAILED":
            if retry_counts[sid] < max_retries:
                retry_counts[sid] += 1
                print(f"[{time.strftime('%H:%M:%S')}] {name} FAILED: {err_msg}. Auto-retrying ({retry_counts[sid]}/{max_retries})...")
                # Reset and resubmit
                cur.execute("UPDATE scene SET horizontal_video_status='PENDING' WHERE id=?", (sid,))
                conn.commit()
                resub_payload = {
                    "requests": [{
                        "type": "GENERATE_VIDEO",
                        "scene_id": sid,
                        "project_id": PID,
                        "video_id": VID,
                        "orientation": ORI
                    }]
                }
                req_data = json.dumps(resub_payload).encode('utf-8')
                req_obj = urllib.request.Request(
                    "http://127.0.0.1:8100/api/requests/batch",
                    data=req_data,
                    headers={"Content-Type": "application/json"}
                )
                try:
                    urllib.request.urlopen(req_obj)
                except Exception as ex:
                    print(f"Failed to resubmit {name}: {ex}")
                all_done = False
            else:
                print(f"[{time.strftime('%H:%M:%S')}] {name} reached max retries ({max_retries})!")
                any_failed = True
        else:
            all_done = False

    conn.close()

    print(f"[{time.strftime('%H:%M:%S')}] Progress: {len(downloaded)}/{len(TARGET_SCENES)} downloaded. Elapsed: {int(time.time() - start_time)}s")

    if len(downloaded) == len(TARGET_SCENES):
        print("ALL 8 TARGET VIDEOS COMPLETED AND DOWNLOADED!")
        break

    if any_failed:
        print("Some scenes failed permanently.")
        break

    time.sleep(15)
