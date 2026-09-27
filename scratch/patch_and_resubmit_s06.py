import json
import urllib.request
import time

sid = "d0f437eb-1974-4590-83f6-8785c944a322"
pid = "aae54cfc-ea42-4c63-8f9d-440b0b9ddd86"
vid = "19cbad31-3cd4-49f8-80de-874c1093a8b4"

refined_prompt = """Handheld smartphone front-camera vlog footage, ultra-wide 0.5x lens, slight wide-angle barrel distortion, photorealistic documentary realism.
[00:00–00:02] Mia holds the camera at arm's length with her right arm extended toward the bottom-right edge of the frame. She stands beside an ancient market stall in Atlantis, 9600 BC, piled with dull silver tin ingots, a bronze balance scale with stone weights and sacks of grain; the merchant holds up an ingot and looks at her.
[00:02–00:06] She leans in close to the camera lens. Mia whispers conspiratorially "No coins anywhere. They trade by weight... tin, oil, grain."
[00:06–00:08] Silent, she ducks forward under a hanging striped red and white linen awning; the linen fabric sweeps directly across the lens, wiping across and completely filling the entire screen.
Mia holds the camera herself with her extended arm with natural subtle handheld shake.
Warm mid-morning sunlight filtered through linen awnings.
The camera is the phone itself recording from Mia's hand, so the viewer looks directly at Mia and the market; no phone, no case, no mount, and no selfie stick appear anywhere in the shot. Mia never vanishes: she only leaves the frame when ducking under the awning. The locals wear ancient linen tunics and everything around is ancient, with no modern objects. Only Mia speaks. No subtitles or text appear on screen. Real footage aesthetic.

Audio: haggling voices in an unknown ancient language, market bustle.
SFX: clinking metal on the scale pans, rustling linen fabric wiping the lens."""

# 1. PATCH scene
patch_url = f"http://127.0.0.1:8100/api/scenes/{sid}"
patch_data = json.dumps({
    "video_prompt": refined_prompt,
    "horizontal_video_status": "PENDING"
}).encode('utf-8')
req = urllib.request.Request(patch_url, data=patch_data, headers={"Content-Type": "application/json"}, method="PATCH")
with urllib.request.urlopen(req) as resp:
    res = json.loads(resp.read().decode('utf-8'))
    print("PATCH Status:", resp.status)
    print("Reset horizontal_video_status to:", res.get("horizontal_video_status"))

# 2. Resubmit request
req_body = {
    "requests": [
        {
            "type": "GENERATE_VIDEO_REFS",
            "scene_id": sid,
            "project_id": pid,
            "video_id": vid,
            "orientation": "HORIZONTAL"
        }
    ]
}
batch_url = "http://127.0.0.1:8100/api/requests/batch"
data = json.dumps(req_body).encode('utf-8')
breq = urllib.request.Request(batch_url, data=data, headers={"Content-Type": "application/json"}, method="POST")
with urllib.request.urlopen(breq) as resp:
    bres = json.loads(resp.read().decode('utf-8'))
    print("Submit response:", json.dumps(bres, indent=2))
    new_req_id = bres[0]["id"]
    print(f"\nNEW_REQ_ID={new_req_id}")
