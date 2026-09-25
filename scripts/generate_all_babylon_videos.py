import json
import urllib.request
import sqlite3
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

pid = "ac50c619-1b31-4847-95d6-5379d02554c7"
vid = "dc2afa55-8a7f-42c3-bf8c-a13f580b6830"

conn = sqlite3.connect("flow_agent.db")
c = conn.cursor()
c.execute("""
    SELECT id, display_order, horizontal_image_media_id
    FROM scene
    WHERE video_id = ?
    ORDER BY display_order ASC
""", (vid,))
scenes = c.fetchall()
conn.close()

requests_payload = []
for sid, order, mid in scenes:
    requests_payload.append({
        "type": "GENERATE_VIDEO",
        "scene_id": sid,
        "project_id": pid,
        "video_id": vid,
        "orientation": "HORIZONTAL"
    })

print(f"Submitting GENERATE_VIDEO batch for {len(requests_payload)} scenes...")
req = urllib.request.Request(
    "http://127.0.0.1:8100/api/requests/batch",
    data=json.dumps({"requests": requests_payload}).encode("utf-8"),
    headers={"Content-Type": "application/json"}
)
with urllib.request.urlopen(req) as resp:
    res = json.loads(resp.read())
    print(f"Submitted batch successfully! Response: {res}")
