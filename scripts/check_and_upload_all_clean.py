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

p_out = json.loads(urllib.request.urlopen(f"http://127.0.0.1:8100/api/projects/{pid}/output-dir").read())
project_dir = p_out.get("path")
images_dir = os.path.join(project_dir, "images")
os.makedirs(images_dir, exist_ok=True)

art_images_dir = r"C:\Users\Administrator\.gemini\antigravity-ide\brain\e22150ce-4262-4e3c-8619-a7731a7f7c3a\images"
os.makedirs(art_images_dir, exist_ok=True)

# Mapping file to remember which media_ids are clean uploads
map_path = os.path.join(images_dir, "clean_media_ids.json")
if os.path.exists(map_path):
    with open(map_path, "r", encoding="utf-8") as f:
        clean_map = json.load(f)
else:
    clean_map = {}

conn = sqlite3.connect("flow_agent.db")
c = conn.cursor()
c.execute("""
    SELECT display_order, id, horizontal_image_url, horizontal_image_media_id
    FROM scene
    WHERE video_id = ?
    ORDER BY display_order
""", (vid,))
scenes = c.fetchall()
conn.close()

print(f"Checking {len(scenes)} scenes...")

for order, sid, img_url, cur_mid in scenes:
    sidx = order + 1
    raw_filename = f"scene_{sidx:02d}_raw.jpg"
    clean_filename = f"scene_{sidx:02d}.jpg"
    
    raw_path = os.path.join(images_dir, raw_filename)
    clean_path = os.path.join(images_dir, clean_filename)
    art_path = os.path.join(art_images_dir, clean_filename)

    # 1. Download raw if needed
    if not os.path.exists(raw_path) and img_url:
        print(f"[Scene {sidx:02d}] Downloading raw image from URL...", flush=True)
        try:
            h = {"User-Agent": "Mozilla/5.0"}
            dl_req = urllib.request.Request(img_url, headers=h)
            with urllib.request.urlopen(dl_req, timeout=30) as d_resp:
                with open(raw_path, "wb") as f:
                    f.write(d_resp.read())
        except Exception as e:
            print(f"  [Scene {sidx:02d}] Error downloading raw: {e}", flush=True)

    # 2. De-watermark if clean doesn't exist
    if os.path.exists(raw_path) and not os.path.exists(clean_path):
        print(f"[Scene {sidx:02d}] Removing watermark...", flush=True)
        try:
            remove_watermark_image(raw_path, clean_path)
            print(f"  [Scene {sidx:02d}] Watermark removed!", flush=True)
        except Exception as e:
            print(f"  [Scene {sidx:02d}] Error removing watermark: {e}", flush=True)

    # Sync to brain artifacts directory
    if os.path.exists(clean_path):
        try:
            with open(clean_path, "rb") as cf:
                clean_bytes = cf.read()
            with open(art_path, "wb") as af:
                af.write(clean_bytes)
        except Exception as e:
            pass

    # 3. Check if uploaded to Google Flow
    already_clean = str(sidx) in clean_map
    if not already_clean and os.path.exists(clean_path):
        print(f"[Scene {sidx:02d}] Uploading clean image to Google Flow...", flush=True)
        uploaded = False
        for retry in range(4):
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
                with urllib.request.urlopen(up_req, timeout=45) as u_resp:
                    up_res = json.loads(u_resp.read())
                    clean_mid = up_res.get("media_id")
                
                print(f"  [Scene {sidx:02d}] Uploaded successfully! Clean media_id: {clean_mid}", flush=True)
                clean_map[str(sidx)] = clean_mid
                with open(map_path, "w", encoding="utf-8") as f:
                    json.dump(clean_map, f, indent=2)

                # Patch DB
                conn = sqlite3.connect("flow_agent.db")
                conn.execute("""
                    UPDATE scene
                    SET horizontal_image_media_id = ?, horizontal_image_status = 'COMPLETED'
                    WHERE id = ?
                """, (clean_mid, sid))
                conn.commit()
                conn.close()

                # Patch API
                try:
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
                except Exception:
                    pass

                uploaded = True
                break
            except Exception as e:
                print(f"  [Scene {sidx:02d}] Upload retry {retry+1} error: {e}", flush=True)
                time.sleep(3)
        if not uploaded:
            print(f"  [Scene {sidx:02d}] FAILED to upload clean image after retries!", flush=True)
    elif already_clean:
        print(f"[Scene {sidx:02d}] Already has clean uploaded media_id: {clean_map[str(sidx)]}", flush=True)
        # Ensure DB has it
        clean_mid = clean_map[str(sidx)]
        conn = sqlite3.connect("flow_agent.db")
        conn.execute("""
            UPDATE scene
            SET horizontal_image_media_id = ?, horizontal_image_status = 'COMPLETED'
            WHERE id = ?
        """, (clean_mid, sid))
        conn.commit()
        conn.close()

print("\nFinished scan. Checking total clean uploaded count...")
print(f"Total clean uploads recorded: {len(clean_map)} / {len(scenes)}")
