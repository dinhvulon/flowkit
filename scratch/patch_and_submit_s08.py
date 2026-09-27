import json
import os
import shutil
import subprocess
import time
import urllib.request

sid = "3f75f697-9c4a-4a91-8dec-9f6c45e5cbbd"
pid = "aae54cfc-ea42-4c63-8f9d-440b0b9ddd86"
vid = "19cbad31-3cd4-49f8-80de-874c1093a8b4"

refined_prompt = """Handheld amateur documentary vlog footage, natural wide-angle lens, clean full edge-to-edge frame, photorealistic documentary realism.
[00:00–00:02] At the same wooden table of the bread stall in Atlantis, 9600 BC, the smiling Bread Vendor in a linen tunic leans in beside Mia and places a clay cup of ancient wine mixed with water on the table.
[00:02–00:06] The Bread Vendor smiles warmly and says "Pie, xene! Hydor kai oinos." Mia reacts with pleasantly surprised wide eyes, lifts the clay cup with her hand and takes a small sip, smiling back in appreciation.
[00:06–00:08] Mia reaches her hand directly toward the camera lens and lifts the camera up from the table; the camera swings quickly to the right with heavy horizontal motion blur.
Filmed as a locked-off static wide shot from table level facing Mia, until she grabs the camera at the end.
Warm morning sunlight under the linen canopy, soft glow from the clay bread oven.
Clean full-screen video with absolutely no camera UI, no record button, no phone frame, and no modern items. The Bread Vendor and Mia interact naturally. Authentic documentary vlog aesthetic.

Audio: market street chatter, crackling oven fire.
SFX: clay cup on wood, a rapid camera whoosh sound at the end."""

# 1. PATCH scene
patch_url = f"http://127.0.0.1:8100/api/scenes/{sid}"
patch_data = json.dumps({
    "video_prompt": refined_prompt,
    "horizontal_video_status": "PENDING"
}).encode('utf-8')
req = urllib.request.Request(patch_url, data=patch_data, headers={"Content-Type": "application/json"}, method="PATCH")
with urllib.request.urlopen(req) as resp:
    res = json.loads(resp.read().decode('utf-8'))
    print("PATCH S08 Status:", resp.status)
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
    print(f"\nNEW_S08_REQ_ID={new_req_id}")

# 3. Track and process
req_url = f"http://127.0.0.1:8100/api/requests/{new_req_id}"
print("Polling request S08:", new_req_id)
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
                raw_mp4 = os.path.join(out_dir, f"scene_08_{sid[:8]}.mp4")
                clean_mp4 = os.path.join(out_dir, f"scene_08_{sid[:8]}_clean.mp4")
                
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
                frames_dir = os.path.join(out_dir, f"scene_08_{sid[:8]}_frames")
                os.makedirs(frames_dir, exist_ok=True)
                frame_pattern = os.path.join(frames_dir, "frame_%02d.jpg")
                print("Extracting frames to:", frames_dir)
                subprocess.run([
                    "ffmpeg", "-y", "-i", clean_mp4,
                    "-vf", "fps=6/8,scale=960:540",
                    frame_pattern
                ])
                
                # Make review sheet grid
                sheet_path = os.path.join(out_dir, f"scene_08_{sid[:8]}_review_sheet.jpg")
                subprocess.run([
                    "ffmpeg", "-y", "-i", clean_mp4,
                    "-vf", "fps=6/8,scale=640:360,tile=3x2",
                    sheet_path
                ])
                print("Review sheet created at:", sheet_path)
                
                # Copy to artifact
                art_sheet = r"C:\Users\Admin\.gemini\antigravity-ide\brain\a1f3435b-3364-4982-a831-1b88fba9287e\s08_review_sheet.jpg"
                shutil.copyfile(sheet_path, art_sheet)
                print("Copied review sheet to artifact:", art_sheet)
                
                break

            elif status == "FAILED":
                print(f"Generation FAILED: {err}")
                break

    except Exception as e:
        print("Error checking status:", e)

    time.sleep(15)
