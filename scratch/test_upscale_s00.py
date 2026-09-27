import urllib.request
import json
import time
import os

url = "http://127.0.0.1:8100/api/requests"
body = {
    "type": "UPSCALE_VIDEO",
    "scene_id": "65c455e7-6a75-4340-a359-aafe5ba7d383",
    "project_id": "aae54cfc-ea42-4c63-8f9d-440b0b9ddd86",
    "video_id": "19cbad31-3cd4-49f8-80de-874c1093a8b4",
    "orientation": "HORIZONTAL"
}

data = json.dumps(body).encode('utf-8')
req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"}, method="POST")

try:
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        print("Submit response:", json.dumps(res, indent=2))
        req_id = res["id"]
except urllib.error.HTTPError as e:
    print("Submit error:", e.code, e.read().decode('utf-8'))
    exit(1)

print(f"\nTracking upscale request for S00 (request ID: {req_id})...")
start_time = time.time()
while True:
    track_url = f"http://127.0.0.1:8100/api/requests/{req_id}"
    try:
        with urllib.request.urlopen(track_url) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            status = data.get("status")
            err = data.get("error_message")
            media_id = data.get("media_id")
            out_url = data.get("output_url")
            elapsed = int(time.time() - start_time)
            print(f"[{elapsed}s] Status: {status} | media_id: {media_id} | error: {err}")
            
            if status == "COMPLETED":
                print(f"\nS00 UPSCALE COMPLETED! Media ID: {media_id}, URL: {out_url}")
                break
            elif status == "FAILED":
                print(f"\nS00 UPSCALE FAILED: {err}")
                break
    except Exception as e:
        print("Polling error:", e)
        
    time.sleep(10)
