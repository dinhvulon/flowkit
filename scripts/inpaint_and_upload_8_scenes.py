import json
import urllib.request
import sqlite3
import os
import sys
import time
import shutil

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
art_images_dir = r"C:\Users\Administrator\.gemini\antigravity-ide\brain\e22150ce-4262-4e3c-8619-a7731a7f7c3a\images"

target_orders = [2, 7, 9, 11, 14, 15, 19, 22] # 1-based: [3, 8, 10, 12, 15, 16, 20, 23]

conn = sqlite3.connect("flow_agent.db")
c = conn.cursor()
c.execute("""
    SELECT display_order+1, id, horizontal_image_url
    FROM scene
    WHERE video_id = ? AND display_order IN ({})
    ORDER BY display_order ASC
""".format(','.join('?' * len(target_orders))), [vid] + target_orders)
scenes = c.fetchall()
conn.close()

print(f"Processing {len(scenes)} updated scenes...")

clean_media_ids = {}

for sidx, sid, img_url in scenes:
    raw_filename = f"scene_{sidx:02d}_raw.jpg"
    clean_filename = f"scene_{sidx:02d}.jpg"
    raw_path = os.path.join(images_dir, raw_filename)
    clean_path = os.path.join(images_dir, clean_filename)
    art_path = os.path.join(art_images_dir, clean_filename)

    print(f"\n[Scene {sidx:02d}] Downloading new raw image: {img_url[:60]}...", flush=True)
    h = {"User-Agent": "Mozilla/5.0"}
    dl_req = urllib.request.Request(img_url, headers=h)
    with urllib.request.urlopen(dl_req, timeout=30) as d_resp:
        with open(raw_path, "wb") as f:
            f.write(d_resp.read())

    print(f"  [Scene {sidx:02d}] Removing watermark logo...", flush=True)
    remove_watermark_image(raw_path, clean_path)
    shutil.copy(clean_path, art_path)

    print(f"  [Scene {sidx:02d}] Uploading clean frame to Google Flow...", flush=True)
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
    with urllib.request.urlopen(up_req, timeout=40) as u_resp:
        up_res = json.loads(u_resp.read())
        clean_mid = up_res.get("media_id")

    print(f"  [Scene {sidx:02d}] Clean media_id obtained: {clean_mid}", flush=True)
    clean_media_ids[sidx] = clean_mid

    # Update DB
    conn = sqlite3.connect("flow_agent.db")
    conn.execute("""
        UPDATE scene
        SET horizontal_image_media_id = ?, horizontal_image_status = 'COMPLETED'
        WHERE id = ?
    """, (clean_mid, sid))
    conn.commit()
    conn.close()

print("\nAll 8 scenes downloaded, inpainted, and clean media_ids updated in DB!")
print(clean_media_ids)
