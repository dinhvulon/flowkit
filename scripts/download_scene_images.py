import sqlite3
import os
import sys
import urllib.request
import json

sys.stdout.reconfigure(encoding="utf-8")

PROJECT_DIR = os.path.join("output", "time_travel_vlog_hanging_gardens_of_babylon_570_bc")
IMAGES_DIR = os.path.join(PROJECT_DIR, "images")
os.makedirs(IMAGES_DIR, exist_ok=True)

conn = sqlite3.connect("flow_agent.db")
c = conn.cursor()
c.execute("""
    SELECT display_order, id, horizontal_image_media_id, horizontal_image_url, prompt, narrator_text, chain_type, character_names
    FROM scene
    WHERE video_id = '71909a60-29f7-460e-807c-ed48b8a12ad1'
    ORDER BY display_order ASC
""")
scenes = c.fetchall()
print(f"Found {len(scenes)} scenes to download images for.")

downloaded_count = 0
scene_metadata = []

for s in scenes:
    order, sid, mid, url, prompt, narrator, chain_type, char_names = s
    idx = order + 1
    filename = f"scene_{idx:02d}.jpg"
    filepath = os.path.join(IMAGES_DIR, filename)

    if not url:
        print(f"Scene {idx:02d}: No URL in database!")
        continue

    headers = {"User-Agent": "Mozilla/5.0"}
    req = urllib.request.Request(url, headers=headers)
    success = False
    try:
        with urllib.request.urlopen(req, timeout=25) as resp:
            data = resp.read()
            with open(filepath, "wb") as f:
                f.write(data)
            downloaded_count += 1
            size_kb = len(data) / 1024
            print(f"[OK] Scene {idx:02d} ({size_kb:.1f} KB) -> {filename}")
            success = True
    except Exception as e:
        print(f"[ERROR] Scene {idx:02d} failed: {e}")

    scene_metadata.append({
        "index": idx,
        "scene_id": sid,
        "media_id": mid,
        "filename": filename,
        "filepath": filepath,
        "chain_type": chain_type,
        "characters": char_names,
        "prompt": prompt,
        "narrator": narrator,
        "downloaded": success
    })

meta_path = os.path.join(IMAGES_DIR, "images_meta.json")
with open(meta_path, "w", encoding="utf-8") as f:
    json.dump(scene_metadata, f, ensure_ascii=False, indent=2)

print(f"=== Successfully downloaded {downloaded_count}/{len(scenes)} images to {IMAGES_DIR} ===")
