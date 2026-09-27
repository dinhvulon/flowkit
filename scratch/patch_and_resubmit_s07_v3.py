import json
import os
import shutil
import subprocess
import time
import urllib.request

sid = "f7a00991-a11d-4ff9-a739-d789e4c977f6"
pid = "aae54cfc-ea42-4c63-8f9d-440b0b9ddd86"
vid = "19cbad31-3cd4-49f8-80de-874c1093a8b4"

refined_prompt = """Handheld amateur documentary vlog footage, natural wide-angle lens, clean full edge-to-edge frame, photorealistic documentary realism.
[00:00–00:02] Clean static frame facing Mia seated at a rough wooden table at an open-air bread stall in Atlantis, 9600 BC. The smiling Bread Vendor places a fresh warm flat barley loaf and a bowl of figs and goat cheese in front of Mia.
[00:02–00:05] Mia picks up the flat barley bread with her hands, dips a piece into the olive oil bowl, and takes a clear, deliberate bite, chewing happily with genuine delight.
[00:05–00:08] Mia looks straight at the camera with a satisfied smile and says "Barley bread, figs, goat cheese. Honestly? Five stars." In the background, the Bread Vendor tends the glowing domed clay oven.
Filmed as a locked-off static wide shot from table level facing Mia.
Warm morning sunlight under the linen canopy, soft warm glow from the clay bread oven.
Clean full-screen video with absolutely no camera UI, no record button, no phone frame, and no floating hands. Mia never vanishes. The food is flat barley bread, figs and goat cheese in olive oil. Authentic documentary vlog aesthetic.

Audio: market street chatter, crackling wood fire.
SFX: wooden plate placed on table, bread tearing, clay bowl on wood."""

# 1. PATCH scene
patch_url = f"http://127.0.0.1:8100/api/scenes/{sid}"
patch_data = json.dumps({
    "video_prompt": refined_prompt,
    "horizontal_video_status": "PENDING"
}).encode('utf-8')
req = urllib.request.Request(patch_url, data=patch_data, headers={"Content-Type": "application/json"}, method="PATCH")
with urllib.request.urlopen(req) as resp:
    res = json.loads(resp.read().decode('utf-8'))
    print("PATCH Status:", resp.status)
    print("Reset horizontal_video_status to:", res.get("horizontal_video_status"))

# 2. Resubmit request
req_body = {
    "requests": [
        {
            "type": "GENERATE_VIDEO_REFS",
            "scene_id": sid,
            "project_id": pid,
            "video_id": vid,
            "orientation": "HORIZONTAL"
        }
    ]
}
batch_url = "http://127.0.0.1:8100/api/requests/batch"
data = json.dumps(req_body).encode('utf-8')
breq = urllib.request.Request(batch_url, data=data, headers={"Content-Type": "application/json"}, method="POST")
with urllib.request.urlopen(breq) as resp:
    bres = json.loads(resp.read().decode('utf-8'))
    print("Submit response:", json.dumps(bres, indent=2))
    new_req_id = bres[0]["id"]
    print(f"\nNEW_S07_REQ_ID={new_req_id}")

# 3. Track and process
req_url = f"http://127.0.0.1:8100/api/requests/{new_req_id}"
print("Polling request S07 v3:", new_req_id)
start_time = time.time()

while True:
    try:
        with urllib.request.urlopen(req_url) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            status = data.get("status")
            err = data.get("error_message")
            media_id = data.get("media_id")
            out_url = data.get("output_url")
            elapsed = int(time.time() - start_time)
            print(f"[{elapsed}s] Status: {status}")

            if status == "COMPLETED":
                print(f"Generation COMPLETED! Media ID: {media_id}")
                
                scene_url = f"http://127.0.0.1:8100/api/scenes/{sid}"
                with urllib.request.urlopen(scene_url) as sresp:
                    sdata = json.loads(sresp.read().decode('utf-8'))
                    video_url = sdata.get("horizontal_video_url") or out_url
                
                out_dir = r"c:\flowkit\output\atlantis-9600bc\scenes"
                os.makedirs(out_dir, exist_ok=True)
                raw_mp4 = os.path.join(out_dir, f"scene_07_{sid[:8]}.mp4")
                clean_mp4 = os.path.join(out_dir, f"scene_07_{sid[:8]}_clean.mp4")
                
                print("Downloading raw video to:", raw_mp4)
                urllib.request.urlretrieve(video_url, raw_mp4)
                print("Raw video downloaded. Size:", os.path.getsize(raw_mp4), "bytes")
                
                # Run remove_watermark_from_link.py
                print("Running watermark removal...")
                subprocess.run([
                    "python", "tools/remove_watermark_from_link.py",
                    raw_mp4
                ])
                
                # Extract 6 frames
                frames_dir = os.path.join(out_dir, f"scene_07_{sid[:8]}_frames")
                os.makedirs(frames_dir, exist_ok=True)
                frame_pattern = os.path.join(frames_dir, "frame_%02d.jpg")
                print("Extracting frames to:", frames_dir)
                subprocess.run([
                    "ffmpeg", "-y", "-i", clean_mp4,
                    "-vf", "fps=6/8,scale=960:540",
                    frame_pattern
                ])
                
                # Make review sheet grid
                sheet_path = os.path.join(out_dir, f"scene_07_{sid[:8]}_review_sheet.jpg")
                subprocess.run([
                    "ffmpeg", "-y", "-i", clean_mp4,
                    "-vf", "fps=6/8,scale=640:360,tile=3x2",
                    sheet_path
                ])
                print("Review sheet created at:", sheet_path)
                
                # Copy to artifact
                art_sheet = r"C:\Users\Admin\.gemini\antigravity-ide\brain\a1f3435b-3364-4982-a831-1b88fba9287e\s07_review_sheet_v3.jpg"
                shutil.copyfile(sheet_path, art_sheet)
                print("Copied review sheet to artifact:", art_sheet)
                
                break

            elif status == "FAILED":
                print(f"Generation FAILED: {err}")
                break

    except Exception as e:
        print("Error checking status:", e)

    time.sleep(15)
