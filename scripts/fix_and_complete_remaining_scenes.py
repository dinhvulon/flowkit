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

# 1. Update character_names to only ["Mia"] for all scenes in this video
print("1. Updating character_names to ['Mia'] across all scenes...", flush=True)
conn = sqlite3.connect("flow_agent.db")
conn.execute("UPDATE scene SET character_names = '[\"Mia\"]' WHERE video_id = ?", (vid,))
conn.commit()

# Find the scenes that need generation
c = conn.cursor()
c.execute("""
    SELECT s.id, s.display_order
    FROM scene s
    WHERE s.video_id = ? AND (s.horizontal_image_media_id IS NULL OR s.horizontal_image_status != 'COMPLETED')
    ORDER BY s.display_order
""", (vid,))
scenes_needing_gen = c.fetchall()
conn.close()

print(f"Scenes needing image generation ({len(scenes_needing_gen)}): {[r[1]+1 for r in scenes_needing_gen]}", flush=True)

# 2. Resubmit REGENERATE_IMAGE for these scenes
requests_payload = []
for sid, order in scenes_needing_gen:
    requests_payload.append({
        "type": "REGENERATE_IMAGE",
        "scene_id": sid,
        "project_id": pid,
        "video_id": vid,
        "orientation": "HORIZONTAL"
    })

if requests_payload:
    print(f"2. Submitting REGENERATE_IMAGE for {len(requests_payload)} scenes...", flush=True)
    req = urllib.request.Request(
        "http://127.0.0.1:8100/api/requests/batch",
        data=json.dumps({"requests": requests_payload}).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read())
        print(f"Submitted batch successfully! Response count: {len(res)}", flush=True)

    # 3. Poll batch status until completed
    print("3. Monitoring batch image generation...", flush=True)
    poll_url = f"http://127.0.0.1:8100/api/requests/batch-status?video_id={vid}&type=GENERATE_IMAGE"

    for poll in range(1, 60):
        time.sleep(10)
        try:
            bs_resp = json.loads(urllib.request.urlopen(poll_url).read())
            total = bs_resp.get("total", len(requests_payload))
            completed = bs_resp.get("completed", 0)
            pending = bs_resp.get("pending", 0)
            processing = bs_resp.get("processing", 0)
            failed = bs_resp.get("failed", 0)
            is_done = bs_resp.get("done", False)

            print(f"  [Poll {poll:02d}] Completed: {completed} | Processing: {processing} | Pending: {pending} | Failed: {failed}", flush=True)
            if is_done or (pending == 0 and processing == 0):
                print("All regeneration requests finished!", flush=True)
                break
        except Exception as e:
            print(f"  [Poll {poll:02d}] Error: {e}", flush=True)

# 4. Download, de-watermark, and re-upload for all scenes currently missing clean media_id
print("\n4. Downloading, de-watermarking, and uploading clean frames...", flush=True)

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
all_scenes = c.fetchall()
conn.close()

for order, sid, img_url, cur_mid in all_scenes:
    sidx = order + 1
    raw_filename = f"scene_{sidx:02d}_raw.jpg"
    clean_filename = f"scene_{sidx:02d}.jpg"
    
    raw_path = os.path.join(images_dir, raw_filename)
    clean_path = os.path.join(images_dir, clean_filename)
    art_path = os.path.join(art_images_dir, clean_filename)

    # Check if scene was already successfully uploaded
    # If the clean file exists and is uploaded, check if we need to do it
    if not img_url and not os.path.exists(clean_path):
        print(f"  [Scene {sidx:02d}] Still no image URL and no clean file found", flush=True)
        continue

    # Download raw if not exists or if recently regenerated
    if img_url:
        try:
            h = {"User-Agent": "Mozilla/5.0"}
            dl_req = urllib.request.Request(img_url, headers=h)
            with urllib.request.urlopen(dl_req, timeout=30) as d_resp:
                with open(raw_path, "wb") as f:
                    f.write(d_resp.read())
            # Remove watermark
            remove_watermark_image(raw_path, clean_path)
            with open(clean_path, "rb") as cf:
                clean_bytes = cf.read()
            with open(art_path, "wb") as af:
                af.write(clean_bytes)
            print(f"  [Scene {sidx:02d}] Watermark removed! Clean file saved.", flush=True)
        except Exception as e:
            print(f"  [Scene {sidx:02d}] De-watermark step note: {e}", flush=True)

    # If clean file exists, upload to Google Flow to get clean media_id
    if os.path.exists(clean_path):
        for retry in range(3):
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
                with urllib.request.urlopen(up_req, timeout=35) as u_resp:
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
                break
            except Exception as e:
                print(f"  [Scene {sidx:02d}] Upload attempt {retry+1} error: {e}", flush=True)
                time.sleep(3)

# 5. Final Status Count
conn = sqlite3.connect("flow_agent.db")
c = conn.cursor()
c.execute("""
    SELECT count(*), horizontal_image_status
    FROM scene
    WHERE video_id = ?
    GROUP BY horizontal_image_status
""", (vid,))
final_stats = c.fetchall()
conn.close()

print("\n=======================================================")
print(f"FINAL SCENE IMAGE STATUS: {final_stats}")
print(f"Project ID: {pid}")
print(f"Video ID: {vid}")
print("=======================================================")
