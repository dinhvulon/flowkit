import json
import urllib.request

sid = "b11e9cfe-c5ec-4f60-9619-b8d63dfbd709"
pid = "195a112e-7537-4b61-b3c6-03188e4f12d1"
vid = "4427d959-7e30-4b68-b12f-e549611167c3"

clean_image_prompt = (
    "Real RAW photograph, shot on Canon EOS R5, 35mm lens, natural available light. "
    "Authentic smartphone selfie photograph, vertical 9:16, 28mm front camera. "
    "TIGHT WAIST-UP SELFIE FRAMING. PAN-FOCUS f/8-f/11, ZERO BOKEH. "
    "Chilly darkening afternoon light. Vlogger ducking down low behind a coastal sand ridge on Hakata Bay beach. "
    "Hand near collar clutching her indigo hemp tunic against the biting wind. "
    "In the background, sweeping sandy coast and grey ocean waves. "
    "STRICT ETHNICITY LOCK: 100% native Japanese."
)

clean_video_prompt = (
    "0-3s: Ducking low behind a coastal sand dune, she flinches as the wind howls overhead followed by the distant sound of bronze gongs. "
    "3-6s: She turns to the lens, face tense, clutching her collar against the biting sea gale. "
    "6-8s: Whispering urgently and somberly straight into the camera: "
    '"変な太鼓の音が響いてる。日本の戦い方と全然違う。名乗りを上げる前に、矢が一斉に飛んでくるんだって。" '
    "Audio: Wind whistling over sand dunes, distant clashing gongs, heavy gusts of coastal wind. No background music."
)

# 1. Patch scene prompts
url = f"http://127.0.0.1:8100/api/scenes/{sid}"
data = json.dumps({"prompt": clean_image_prompt, "video_prompt": clean_video_prompt}).encode("utf-8")
req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"}, method="PATCH")
with urllib.request.urlopen(req) as resp:
    print("[+] Patched Scene 6 prompts:", resp.status)

# 2. Submit REGENERATE_IMAGE
req_payload = {
    "type": "REGENERATE_IMAGE",
    "scene_id": sid,
    "project_id": pid,
    "video_id": vid,
    "orientation": "VERTICAL"
}
req2 = urllib.request.Request(
    "http://127.0.0.1:8100/api/requests",
    data=json.dumps(req_payload).encode("utf-8"),
    headers={"Content-Type": "application/json"}
)
with urllib.request.urlopen(req2) as resp:
    res = json.loads(resp.read())
    print(f"[+] Submitted REGENERATE_IMAGE request: {res.get('id')} status={res.get('status')}")
