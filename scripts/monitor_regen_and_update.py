import json
import os
import shutil
import sqlite3
import sys
import time
import urllib.request

sys.stdout.reconfigure(encoding="utf-8")

PROJECT_DIR = os.path.join("output", "time_travel_vlog_hanging_gardens_of_babylon_570_bc")
IMAGES_DIR = os.path.join(PROJECT_DIR, "images")
ART_IMG_DIR = r"C:\Users\Administrator\.gemini\antigravity-ide\brain\e22150ce-4262-4e3c-8619-a7731a7f7c3a\images"

req_ids = [
    "72a72a6f-59d8-4508-a656-f537ecbe9210", # Scene 01
    "afc430e1-2d78-4dfd-a4e7-5dfa560d00a2", # Scene 03
    "8194b66b-9732-4206-8d68-d2de9e6b9c05", # Scene 04
    "a6744766-6360-4281-89db-c43b4b6a5b07", # Scene 08
    "8baf06fc-ae6e-4da6-a3d4-0d918f50ad65", # Scene 10
    "d427b11c-5d3a-41b5-a920-4a1d4ad4f099", # Scene 17
    "edeaa10e-c01d-45d5-bf6f-2ec8752ae1d5", # Scene 19
    "181e1120-e027-4e52-851d-ae293fc29d11"  # Scene 20
]

target_scenes = [1, 3, 4, 8, 10, 17, 19, 20]

print("Monitoring 8 REGENERATE_IMAGE requests...")

for poll in range(1, 60):
    time.sleep(4)
    all_done = True
    statuses = []
    for rid in req_ids:
        try:
            r = urllib.request.urlopen(f"http://127.0.0.1:8100/api/requests/{rid}", timeout=5)
            data = json.loads(r.read())
            st = data.get("status")
            statuses.append(f"{rid[:6]}:{st}")
            if st in ("PENDING", "PROCESSING"):
                all_done = False
        except Exception:
            all_done = False

    print(f"Poll {poll:02d}: " + ", ".join(statuses))
    if all_done:
        print("All 8 regeneration requests completed!")
        break

# Re-download the 8 newly generated scene images
conn = sqlite3.connect("flow_agent.db")
c = conn.cursor()
for idx in target_scenes:
    order = idx - 1
    c.execute("""
        SELECT horizontal_image_url, horizontal_image_media_id
        FROM scene
        WHERE video_id = '71909a60-29f7-460e-807c-ed48b8a12ad1' AND display_order = ?
    """, (order,))
    row = c.fetchone()
    if row and row[0]:
        url = row[0]
        filename = f"scene_{idx:02d}.jpg"
        dest1 = os.path.join(IMAGES_DIR, filename)
        dest2 = os.path.join(ART_IMG_DIR, filename)
        headers = {"User-Agent": "Mozilla/5.0"}
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                data = resp.read()
                with open(dest1, "wb") as f:
                    f.write(data)
                with open(dest2, "wb") as f:
                    f.write(data)
                print(f"[UPDATED] Scene {idx:02d} ({len(data)} bytes) overwritten with new image!")
        except Exception as e:
            print(f"[ERROR] Failed to download new Scene {idx:02d}: {e}")

# Re-run generator scripts to update HTML and MD
os.system(f'"{sys.executable}" scripts/generate_review_html.py')
os.system(f'"{sys.executable}" scripts/write_review_artifact.py')
print("All galleries updated with fresh images!")
