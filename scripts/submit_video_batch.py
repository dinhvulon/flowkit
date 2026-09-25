import urllib.request
import json
import time
import sqlite3
import os

PID = "ac50c619-1b31-4847-95d6-5379d02554c7"
VID = "dc2afa55-8a7f-42c3-bf8c-a13f580b6830"
ORI = "HORIZONTAL"

TARGET_SCENES = [
    ("Scene 03", "27404416-f641-4587-8340-f0f40c8ef3b7", 3),
    ("Scene 08", "1d8003fe-1fe6-4a00-9f33-2a16fc1d873b", 8),
    ("Scene 10", "9fd3ec6d-b8bd-4343-abf2-2239c8c85f08", 10),
    ("Scene 12", "7bd21651-e8cd-44c1-9259-202e2425ed0f", 12),
    ("Scene 15", "e2976cc7-5a59-41c3-a573-b7e3616ed969", 15),
    ("Scene 16", "19a26b18-4b08-40c0-897b-99b36ca5b421", 16),
    ("Scene 20", "0fa349bb-c3db-4049-bab8-de4ddf0c3a8a", 20),
    ("Scene 23", "5695d17a-2861-4987-81c6-8070caaa682c", 23),
]

# Ensure scenes directory exists
outdir = os.path.join("output", "time_travel_vlog_ancient_babylon_570_bc", "scenes")
os.makedirs(outdir, exist_ok=True)

# 1. Reset status in DB to PENDING if needed
conn = sqlite3.connect("flow_agent.db")
cur = conn.cursor()
for name, sid, idx in TARGET_SCENES:
    cur.execute("UPDATE scene SET horizontal_video_status='PENDING', horizontal_video_media_id=NULL WHERE id=?", (sid,))
conn.commit()

# 2. Build requests payload
requests_payload = {
    "requests": [
        {
            "type": "GENERATE_VIDEO",
            "scene_id": sid,
            "project_id": PID,
            "video_id": VID,
            "orientation": ORI
        }
        for name, sid, idx in TARGET_SCENES
    ]
}

req_data = json.dumps(requests_payload).encode('utf-8')
req = urllib.request.Request(
    "http://127.0.0.1:8100/api/requests/batch",
    data=req_data,
    headers={"Content-Type": "application/json"}
)

try:
    resp = urllib.request.urlopen(req)
    created = json.loads(resp.read().decode())
    print(f"Submitted batch of {len(created)} video requests successfully.")
except Exception as e:
    print(f"Failed to submit batch: {e}")
    exit(1)
