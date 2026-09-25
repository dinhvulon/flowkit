import json
import os
import sqlite3
import sys
import time
import urllib.request

sys.stdout.reconfigure(encoding="utf-8")

reqs = [
    ("6a92729a-7154-481e-aedc-a40e71d3d31b", 1),
    ("d9bcb25b-df63-4523-a61a-8c6c56a89908", 8)
]

print("Monitoring REGENERATE_IMAGE for Scene 01 and 08...")

for poll in range(1, 30):
    time.sleep(3)
    all_done = True
    statuses = []
    for rid, sidx in reqs:
        try:
            data = json.loads(urllib.request.urlopen(f"http://127.0.0.1:8100/api/requests/{rid}").read())
            st = data.get("status")
            statuses.append(f"Scene {sidx:02d}:{st}")
            if st in ("PENDING", "PROCESSING"):
                all_done = False
        except Exception as e:
            all_done = False
            statuses.append(f"Scene {sidx:02d}:err")
    print(f"Poll {poll:02d}: " + ", ".join(statuses))
    if all_done:
        print("Both Scene 01 and Scene 08 regeneration completed!")
        break

# Download updated images
PROJECT_DIR = os.path.join("output", "time_travel_vlog_hanging_gardens_of_babylon_570_bc")
IMAGES_DIR = os.path.join(PROJECT_DIR, "images")
ART_IMG_DIR = r"C:\Users\Administrator\.gemini\antigravity-ide\brain\e22150ce-4262-4e3c-8619-a7731a7f7c3a\images"

conn = sqlite3.connect("flow_agent.db")
c = conn.cursor()

for rid, sidx in reqs:
    order = sidx - 1
    c.execute("""
        SELECT horizontal_image_url, horizontal_image_media_id
        FROM scene
        WHERE video_id = '71909a60-29f7-460e-807c-ed48b8a12ad1' AND display_order = ?
    """, (order,))
    row = c.fetchone()
    if row and row[0]:
        url, mid = row[0], row[1]
        fname = f"scene_{sidx:02d}.jpg"
        p1 = os.path.join(IMAGES_DIR, fname)
        p2 = os.path.join(ART_IMG_DIR, fname)
        headers = {"User-Agent": "Mozilla/5.0"}
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                data = resp.read()
                with open(p1, "wb") as f:
                    f.write(data)
                with open(p2, "wb") as f:
                    f.write(data)
                print(f"[UPDATED] Scene {sidx:02d} ({mid[:8]}): {len(data)/1024:.1f} KB downloaded!")
        except Exception as e:
            print(f"[ERROR] Failed to download Scene {sidx:02d}: {e}")

# Update galleries
os.system(f'"{sys.executable}" scripts/generate_review_html.py')
os.system(f'"{sys.executable}" scripts/write_review_artifact.py')
print("Galleries refreshed with new photorealistic images!")
