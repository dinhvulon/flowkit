import json
import urllib.request

sid = "f7a00991-a11d-4ff9-a739-d789e4c977f6"
pid = "aae54cfc-ea42-4c63-8f9d-440b0b9ddd86"
vid = "19cbad31-3cd4-49f8-80de-874c1093a8b4"

refined_prompt = """Handheld amateur documentary vlog footage, natural wide-angle lens, clean full edge-to-edge frame, photorealistic documentary realism.
[00:00–00:02] A striped red and white linen cloth sweeps up and away from the camera lens, revealing Mia seated at a rough wooden table of an open-air bread stall in Atlantis, 9600 BC, flat barley loaves, fresh figs and goat cheese in olive oil before her.
[00:02–00:06] She tears a piece of warm flat bread, dips it in the oil and bites into a fig, eyes widening with joy. Mia says with her mouth full "Barley bread, figs, goat cheese in olive oil. Honestly? Five stars."
[00:06–00:08] She chews happily in silence while the Bread Vendor in an ancient linen tunic tends a glowing domed clay oven behind her.
Filmed as a locked-off static wide shot from table level facing Mia.
Warm morning sunlight under the linen canopy, soft warm glow from the clay bread oven.
Clean full-screen video with absolutely no camera UI, no record button, no battery icon, no phone screen border, and no text or overlays. Mia never vanishes. The locals wear ancient linen tunics and everything is ancient, with no modern items. The food is only flat barley bread, figs and goat cheese in olive oil. Only Mia speaks. Real footage aesthetic.

Audio: market street chatter, crackling wood fire.
SFX: linen cloth lifting away, bread tearing, clay bowl on wood."""

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
    print(f"\nNEW_S07_REQ_ID={new_req_id}")
