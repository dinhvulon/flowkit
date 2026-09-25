import urllib.request
import json
import re
import sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

vid = "71909a60-29f7-460e-807c-ed48b8a12ad1"
script_path = r"c:\flowkit\output\babylon_570bc\script.md"

with open(script_path, "r", encoding="utf-8") as f:
    content = f.read()

# Extract the JSON block
json_match = re.search(r"```json\s*(\[\s*\{.*?\}\s*\])\s*```", content, re.DOTALL)
if not json_match:
    print("Could not find JSON block in script.md")
    exit(1)

clips = json.loads(json_match.group(1))
print(f"Loaded {len(clips)} clips from script.md")

# Fetch current scenes from API
with urllib.request.urlopen(f"http://127.0.0.1:8100/api/scenes?video_id={vid}") as r:
    scenes = json.loads(r.read())

scenes.sort(key=lambda s: s["display_order"])
print(f"Fetched {len(scenes)} scenes from API")

for i, clip in enumerate(clips):
    if i >= len(scenes):
        break
    s = scenes[i]
    sid = s["id"]
    patch_data = {
        "prompt": clip["prompt"],
        "video_prompt": clip["video_prompt"],
        "character_names": clip.get("character_names", ["Mia"]),
        "transition_prompt": clip.get("transition_out", "")
    }
    
    req = urllib.request.Request(
        f"http://127.0.0.1:8100/api/scenes/{sid}",
        data=json.dumps(patch_data).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="PATCH"
    )
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        print(f"Patched Scene {i+1} ({sid[:8]}): Beat {clip['beat']} - {clip['role']}")

# Also update project title / description to mention Hanging Gardens
pid = "6224591f-b884-42f2-8f57-613bc86d66fb"
proj_patch = {
    "name": "Time Travel Vlog — Hanging Gardens of Babylon (570 BC)",
    "description": "POV time-travel vlog exploring the legendary Hanging Gardens of Babylon in 570 BC during the reign of Nebuchadnezzar II and Queen Amytis of Media."
}
req_proj = urllib.request.Request(
    f"http://127.0.0.1:8100/api/projects/{pid}",
    data=json.dumps(proj_patch).encode("utf-8"),
    headers={"Content-Type": "application/json"},
    method="PATCH"
)
with urllib.request.urlopen(req_proj) as resp:
    print("Updated project title and description successfully.")

# Also update video title
vid_patch = {
    "title": "I Time Traveled to the Hanging Gardens of Babylon in 570 BC! (Vlog)"
}
req_vid = urllib.request.Request(
    f"http://127.0.0.1:8100/api/videos/{vid}",
    data=json.dumps(vid_patch).encode("utf-8"),
    headers={"Content-Type": "application/json"},
    method="PATCH"
)
with urllib.request.urlopen(req_vid) as resp:
    print("Updated video title successfully.")
