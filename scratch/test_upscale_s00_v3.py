import json
import urllib.request
import time

body = {
    "type": "UPSCALE_VIDEO",
    "scene_id": "65c455e7-f9da-499f-bcbc-c32a4263b040",
    "project_id": "aae54cfc-ea42-4c63-8f9d-440b0b9ddd86",
    "video_id": "19cbad31-3cd4-49f8-80de-874c1093a8b4",
    "orientation": "HORIZONTAL"
}

req_data = json.dumps(body).encode("utf-8")
submit_url = "http://127.0.0.1:8100/api/requests"
req = urllib.request.Request(submit_url, data=req_data, headers={"Content-Type": "application/json"}, method="POST")

try:
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        print("S00 upscale submitted successfully:", json.dumps(res, indent=2))
        req_id = res["id"]
except Exception as e:
    print("Submit error:", e)
    exit(1)

print(f"\nMonitoring S00 upscale request {req_id}...")
for i in range(12):
    time.sleep(5)
    track_url = f"http://127.0.0.1:8100/api/requests/{req_id}"
    try:
        with urllib.request.urlopen(track_url) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            status = data.get("status")
            err = data.get("error_message")
            media_id = data.get("media_id")
            out_url = data.get("output_url")
            print(f"[{i*5+5}s] status={status} | media_id={media_id} | error={err}")
            if status == "COMPLETED":
                print(f"\nSUCCESS! 1080p URL: {out_url}")
                break
            elif status == "FAILED":
                print(f"\nFAILED: {err}")
                break
    except Exception as e:
        print("Poll error:", e)
