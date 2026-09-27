import json
import urllib.request

sid = "d0f437eb-1974-4590-83f6-8785c944a322"
url = f"http://127.0.0.1:8100/api/scenes/{sid}"

video_prompt = """Handheld smartphone selfie-stick vlog footage, ultra-wide 0.5x front camera, slight lens distortion, photorealistic documentary realism.
[00:00–00:02] Mia stands beside a market stall in Atlantis, 9600 BC, piled with dull silver tin ingots, a bronze balance scale with stone weights and sacks of grain; the merchant holds up an ingot and eyes her hair suspiciously.
[00:02–00:06] She leans close to the lens. Mia whispers conspiratorially "No coins anywhere. They trade by weight... tin, oil, grain."
[00:06–00:08] Silent, she ducks forward under a striped red and white linen awning and the cloth sweeps over the lens, filling the frame.
The camera is handheld at arm's length on the selfie stick, with subtle shake.
Warm mid-morning sun filtered through linen awnings.
The phone is the camera, so no phone appears anywhere in the frame. Mia never vanishes: she only leaves the frame when the camera itself moves away from her. The locals wear ancient linen tunics and everything around is ancient, with no modern buildings or vehicles. No coins are used; goods are traded by weight. Only Mia speaks. No subtitles or text appear on screen. This looks like real footage, not a movie or a 3D render.

Audio: haggling voices in an unknown ancient language, market bustle.
SFX: clinking metal on the scale pans, rustling linen."""

data = json.dumps({"video_prompt": video_prompt}).encode('utf-8')
req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"}, method="PATCH")
with urllib.request.urlopen(req) as resp:
    res = json.loads(resp.read().decode('utf-8'))
    print("PATCH S06 Status:", resp.status)
    print("Updated S06 video_prompt:", res.get("video_prompt")[:100], "...")
