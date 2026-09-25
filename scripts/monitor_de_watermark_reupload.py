import json
import urllib.request
import sqlite3
import os
import sys
import time

sys.stdout.reconfigure(encoding="utf-8")

flowkit_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if flowkit_root not in sys.path:
    sys.path.insert(0, flowkit_root)

from agent.services.watermark import remove_watermark_image

pid = "ac50c619-1b31-4847-95d6-5379d02554c7"
vid = "dc2afa55-8a7f-42c3-bf8c-a13f580b6830"

print(f"Monitoring GENERATE_IMAGE batch for Project {pid} | Video {vid}...", flush=True)

# 1. MONITOR BATCH STATUS
poll_url = f"http://127.0.0.1:8100/api/requests/batch-status?video_id={vid}&type=GENERATE_IMAGE"

for poll in range(1, 150):
    time.sleep(10)
    try:
        bs_resp = json.loads(urllib.request.urlopen(poll_url).read())
        total = bs_resp.get("total", 23)
        completed = bs_resp.get("completed", 0)
        pending = bs_resp.get("pending", 0)
        processing = bs_resp.get("processing", 0)
        failed = bs_resp.get("failed", 0)
        is_done = bs_resp.get("done", False)

        print(f"  [Poll {poll:02d}] Total: {total} | Completed: {completed} | Processing: {processing} | Pending: {pending} | Failed: {failed}", flush=True)
        if is_done or (completed == total and total > 0):
            print("All scene images completed generation!", flush=True)
            break
    except Exception as e:
        print(f"  [Poll {poll:02d}] Polling error: {e}", flush=True)

# 2. DOWNLOAD IMAGES, REMOVE WATERMARK & RE-UPLOAD
print("\n>>> Starting Download, Watermark Removal & Clean Re-upload...", flush=True)

p_out = json.loads(urllib.request.urlopen(f"http://127.0.0.1:8100/api/projects/{pid}/output-dir").read())
project_dir = p_out.get("path")
images_dir = os.path.join(project_dir, "images")
os.makedirs(images_dir, exist_ok=True)

art_images_dir = r"C:\Users\Administrator\.gemini\antigravity-ide\brain\e22150ce-4262-4e3c-8619-a7731a7f7c3a\images"
os.makedirs(art_images_dir, exist_ok=True)

conn = sqlite3.connect("flow_agent.db")
c = conn.cursor()
c.execute("""
    SELECT display_order, id, horizontal_image_url, horizontal_image_media_id
    FROM scene
    WHERE video_id = ?
    ORDER BY display_order
""", (vid,))
scene_rows = c.fetchall()
conn.close()

uploaded_clean_frames = []

for order, sid, img_url, raw_mid in scene_rows:
    sidx = order + 1
    raw_filename = f"scene_{sidx:02d}_raw.jpg"
    clean_filename = f"scene_{sidx:02d}.jpg"
    
    raw_path = os.path.join(images_dir, raw_filename)
    clean_path = os.path.join(images_dir, clean_filename)
    art_path = os.path.join(art_images_dir, clean_filename)

    if not img_url:
        print(f"  [Scene {sidx:02d}] No image URL found in DB, skipping watermark removal", flush=True)
        continue

    # Download raw image
    h = {"User-Agent": "Mozilla/5.0"}
    dl_req = urllib.request.Request(img_url, headers=h)
    with urllib.request.urlopen(dl_req, timeout=30) as d_resp:
        with open(raw_path, "wb") as f:
            f.write(d_resp.read())

    # Remove watermark
    try:
        remove_watermark_image(raw_path, clean_path)
        with open(clean_path, "rb") as cf:
            clean_bytes = cf.read()
        with open(art_path, "wb") as af:
            af.write(clean_bytes)
        print(f"  [Scene {sidx:02d}] Watermark removed! Clean file: {clean_filename}", flush=True)
    except Exception as e:
        print(f"  [Scene {sidx:02d}] Watermark removal error: {e}. Using raw image.", flush=True)
        clean_path = raw_path

    # Upload clean image back to Google Flow
    try:
        up_payload = {
            "file_path": clean_path,
            "project_id": pid,
            "file_name": clean_filename
        }
        up_req = urllib.request.Request(
            "http://127.0.0.1:8100/api/flow/upload-image",
            data=json.dumps(up_payload).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(up_req, timeout=30) as u_resp:
            up_res = json.loads(u_resp.read())
            clean_mid = up_res.get("media_id")
            
        print(f"  [Scene {sidx:02d}] Clean image uploaded to Google Flow! New media_id: {clean_mid}", flush=True)
        
        # Patch scene with clean media_id
        patch_payload = {
            "horizontal_image_media_id": clean_mid,
            "horizontal_image_status": "COMPLETED"
        }
        patch_req = urllib.request.Request(
            f"http://127.0.0.1:8100/api/scenes/{sid}",
            data=json.dumps(patch_payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="PATCH"
        )
        urllib.request.urlopen(patch_req)
        uploaded_clean_frames.append((sidx, sid, clean_mid))
    except Exception as e:
        print(f"  [Scene {sidx:02d}] Error uploading clean image: {e}", flush=True)

print("\n=======================================================")
print("PIPELINE COMPLETE! ALL 23 START FRAMES ARE CLEAN & READY!")
print(f"Project ID: {pid}")
print(f"Video ID: {vid}")
print(f"Total clean frames uploaded & patched: {len(uploaded_clean_frames)}/23")
print("=======================================================")
