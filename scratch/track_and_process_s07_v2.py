import json
import os
import shutil
import subprocess
import time
import urllib.request

req_id = "f2b990f5-0f32-40df-904d-92983c42e03f"
sid = "f7a00991-a11d-4ff9-a739-d789e4c977f6"
req_url = f"http://127.0.0.1:8100/api/requests/{req_id}"

print("Polling request S07 v2:", req_id)
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
                art_sheet = r"C:\Users\Admin\.gemini\antigravity-ide\brain\a1f3435b-3364-4982-a831-1b88fba9287e\s07_review_sheet_v2.jpg"
                shutil.copyfile(sheet_path, art_sheet)
                print("Copied review sheet to artifact:", art_sheet)
                
                break

            elif status == "FAILED":
                print(f"Generation FAILED: {err}")
                break

    except Exception as e:
        print("Error checking status:", e)

    time.sleep(15)
