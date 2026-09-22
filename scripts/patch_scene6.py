import urllib.request
import json

sid = "b11e9cfe-c5ec-4f60-9619-b8d63dfbd709"
clean_prompt = (
    "0-3s: Ducking low behind a coastal sand dune, she flinches as a whistling arrow flies overhead "
    "followed by the sound of bronze gongs. 3-6s: She turns to the lens, face tense, clutching her collar "
    "against the biting sea gale. 6-8s: Whispering urgently and somberly straight into the camera: "
    '"変な太鼓の音が響いてる。日本の戦い方と全然違う。名乗りを上げる前に、矢が一斉に飛んでくるんだって。" '
    "Audio: Whistle of arrows, clashing bronze gongs, heavy gusts of coastal wind. No background music."
)

url = f"http://127.0.0.1:8100/api/scenes/{sid}"
data = json.dumps({"video_prompt": clean_prompt}).encode("utf-8")
req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"}, method="PATCH")
with urllib.request.urlopen(req) as resp:
    print("Patched Scene 6:", resp.status)
