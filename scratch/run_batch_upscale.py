import json
import os
import subprocess
import time
import urllib.request

pid = "aae54cfc-ea42-4c63-8f9d-440b0b9ddd86"
vid = "19cbad31-3cd4-49f8-80de-874c1093a8b4"
out_dir = r"c:\flowkit\output\atlantis-9600bc\scenes"
os.makedirs(out_dir, exist_ok=True)

# 9 scenes to upscale
scenes_to_upscale = [
    {"order": 0, "sid": "65c455e7-f9da-499f-bcbc-c32a4263b040"},
    {"order": 2, "sid": "b513bfc5-bc05-48cd-b185-06d05b1b2006"},
    {"order": 3, "sid": "8bc44e3b-9fd4-4a42-a963-c02c94dfa4da"},
    {"order": 4, "sid": "e9c2c3bd-2c5b-4254-8d61-8d8140cc4c38"},
    {"order": 5, "sid": "91c768b3-18eb-40b9-939e-d50e071749f2"},
    {"order": 6, "sid": "d0f437eb-1974-4590-83f6-8785c944a322"},
    {"order": 7, "sid": "f7a00991-a11d-4ff9-a739-d789e4c977f6"},
    {"order": 8, "sid": "3f75f697-9c4a-4a91-8dec-9f6c45e5cbbd"},
    {"order": 31, "sid": "ded3ef1c-7dfc-44b0-a0dc-0c6b23ee3fab"},
]

batch_body = {
    "requests": [
        {
            "type": "UPSCALE_VIDEO",
            "scene_id": s["sid"],
            "project_id": pid,
            "video_id": vid,
            "orientation": "HORIZONTAL"
        }
        for s in scenes_to_upscale
    ]
}

print(f"Submitting batch of {len(scenes_to_upscale)} upscale requests to FlowKit server...")
req_data = json.dumps(batch_body).encode("utf-8")
submit_url = "http://127.0.0.1:8100/api/requests/batch"
req = urllib.request.Request(submit_url, data=req_data, headers={"Content-Type": "application/json"}, method="POST")

try:
    with urllib.request.urlopen(req) as resp:
        submitted = json.loads(resp.read().decode("utf-8"))
        print(f"Successfully submitted {len(submitted)} requests to worker queue.")
        for item in submitted:
            print(f"  - Req ID: {item.get('id', '')[:8]} | Scene: {item.get('scene_id', '')[:8]} | Status: {item.get('status')}")
except Exception as e:
    print(f"Error submitting batch: {e}")
    exit(1)

# Polling loop
status_url = f"http://127.0.0.1:8100/api/requests/batch-status?video_id={vid}&type=UPSCALE_VIDEO"
print(f"\nMonitoring batch status via {status_url}...")

completed_sids = set()
start_time = time.time()

while True:
    try:
        with urllib.request.urlopen(status_url) as resp:
            status_data = json.loads(resp.read().decode("utf-8"))
            elapsed = int(time.time() - start_time)
            print(f"[{elapsed}s] Total: {status_data.get('total')}, Pending: {status_data.get('pending')}, "
                  f"Processing: {status_data.get('processing')}, Completed: {status_data.get('completed')}, "
                  f"Failed: {status_data.get('failed')}, Done: {status_data.get('done')}")

            # Check individual scene completion
            for s in scenes_to_upscale:
                sid = s["sid"]
                if sid in completed_sids:
                    continue
                
                scene_url = f"http://127.0.0.1:8100/api/scenes/{sid}"
                try:
                    with urllib.request.urlopen(scene_url) as sc_resp:
                        sc_data = json.loads(sc_resp.read().decode("utf-8"))
                        up_status = sc_data.get("horizontal_upscale_status")
                        up_url = sc_data.get("horizontal_upscale_url")
                        up_media = sc_data.get("horizontal_upscale_media_id")
                        
                        if up_status == "COMPLETED" and up_url:
                            completed_sids.add(sid)
                            order = s["order"]
                            local_1080p = os.path.join(out_dir, f"scene_{order:02d}_{sid[:8]}_1080p.mp4")
                            print(f"\n>>> Scene S{order:02d} ({sid[:8]}) UPSCALE COMPLETED! Media ID: {up_media}")
                            
                            # If up_url is remote http, download it
                            if up_url.startswith("http"):
                                print(f"Downloading 1080p video to {local_1080p}...")
                                urllib.request.urlretrieve(up_url, local_1080p)
                                print(f"Downloaded. Size: {os.path.getsize(local_1080p)} bytes.")
                            elif os.path.exists(up_url) and up_url != local_1080p:
                                import shutil
                                shutil.copyfile(up_url, local_1080p)
                            
                            # Probe resolution
                            probe_target = local_1080p if os.path.exists(local_1080p) else up_url
                            res = subprocess.run([
                                "ffprobe", "-v", "error", "-select_streams", "v:0",
                                "-show_entries", "stream=width,height,codec_name",
                                "-of", "csv=p=0", probe_target
                            ], capture_output=True, text=True)
                            print(f"FFPROBE resolution for S{order:02d}: {res.stdout.strip()}")
                            
                except Exception as sc_err:
                    pass

            if status_data.get("done"):
                print("\n=== ALL BATCH UPSCALE REQUESTS COMPLETED! ===")
                break

    except Exception as e:
        print(f"Error checking batch status: {e}")

    time.sleep(15)
