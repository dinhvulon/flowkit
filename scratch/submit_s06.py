import json
import urllib.request
import sqlite3

# 1. Check queue
conn = sqlite3.connect('flow_agent.db')
cur = conn.cursor()
cur.execute("SELECT id, type, status, scene_id FROM request WHERE status IN ('PENDING', 'PROCESSING')")
rows = cur.fetchall()
print("Current active requests:", rows)

# 2. Submit batch for S06
req_body = {
    "requests": [
        {
            "type": "GENERATE_VIDEO_REFS",
            "scene_id": "d0f437eb-1974-4590-83f6-8785c944a322",
            "project_id": "aae54cfc-ea42-4c63-8f9d-440b0b9ddd86",
            "video_id": "19cbad31-3cd4-49f8-80de-874c1093a8b4",
            "orientation": "HORIZONTAL"
        }
    ]
}

url = "http://127.0.0.1:8100/api/requests/batch"
data = json.dumps(req_body).encode('utf-8')
req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"}, method="POST")

with urllib.request.urlopen(req) as resp:
    res = json.loads(resp.read().decode('utf-8'))
    print("Submit response:", json.dumps(res, indent=2))
