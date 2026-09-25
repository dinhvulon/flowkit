import urllib.request
import json
import os
import shutil
import sqlite3
import sys

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from agent.services.watermark import remove_watermark_image

PID = "ac50c619-1b31-4847-95d6-5379d02554c7"
SID = "e2976cc7-5a59-41c3-a573-b7e3616ed969"
raw_url = "https://flow-content.google/image/1128d51d-959c-4a77-a758-0505868919cf?Expires=1790349235&KeyName=labs-flow-prod-cdn-key&Signature=JHNiNt5dN4-O0NNvcscu1m_RyQI"

images_dir = r"output/time_travel_vlog_ancient_babylon_570_bc/images"
raw_path = os.path.join(images_dir, "scene_15_raw.jpg")
clean_path = os.path.join(images_dir, "scene_15.jpg")
art_path = r"C:\Users\Administrator\.gemini\antigravity-ide\brain\e22150ce-4262-4e3c-8619-a7731a7f7c3a\images\scene_15.jpg"

print("[1] Downloading raw scene 15 image...")
req = urllib.request.Request(raw_url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req) as resp:
    with open(raw_path, "wb") as f:
        f.write(resp.read())
print("  -> Downloaded.")

print("[2] Removing watermark logo from scene 15 image...")
remove_watermark_image(raw_path, clean_path)
shutil.copy2(clean_path, art_path)
print("  -> Watermark removed and saved to artifacts.")

print("[3] Uploading clean image to Google Flow...")
up_payload = {"file_path": clean_path, "project_id": PID, "file_name": "scene_15.jpg"}
up_req = urllib.request.Request(
    "http://127.0.0.1:8100/api/flow/upload-image",
    data=json.dumps(up_payload).encode("utf-8"),
    headers={"Content-Type": "application/json"}
)
with urllib.request.urlopen(up_req) as u_resp:
    res = json.loads(u_resp.read())
    clean_mid = res.get("media_id")
print(f"  -> Clean media_id for Scene 15: {clean_mid}")

print("[4] Updating scene record in DB...")
conn = sqlite3.connect("flow_agent.db")
c = conn.cursor()
c.execute("UPDATE scene SET horizontal_image_media_id=?, horizontal_image_status='COMPLETED' WHERE id=?", (clean_mid, SID))
conn.commit()
conn.close()
print("  -> Scene 15 updated successfully.")
