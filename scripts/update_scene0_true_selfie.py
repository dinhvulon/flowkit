import json
import urllib.request
import time
import os
import shutil

sid = "5fc05aeb-c42e-4721-828f-7dcd560a9104"
pid = "6224591f-b884-42f2-8f57-613bc86d66fb"
vid = "71909a60-29f7-460e-807c-ed48b8a12ad1"

clean_image_prompt = (
    "Handheld selfie vlog shot of a young traveler smiling warmly with bright eyes directly into the camera on the dirt riverbank of ancient Babylon under bright morning sunlight, an ancient wooden ox-cart with large wooden wheels rolling past on the dusty road behind her, the Euphrates river and the distant terraced Hanging Gardens rising in the background. "
    "Photorealistic documentary realism, natural skin texture, cinematic desert daylight, authentic ancient linen clothing, 8k resolution, no 2D, no drawing, no illustration, no painting."
)

clean_video_prompt = (
    '0-3s: Handheld ultra-wide 0.5x selfie camera with subtle natural hand shake. Mia looks directly into the lens smiling warmly on the sunlit Euphrates riverbank as an ancient wooden ox-cart rumbles past in the background. '
    '3-7s: Mia leans in slightly toward the camera, speaking with sparkling eyes in a cheerful conversational tone "You guys... welcome to Babylon, 570 BC! And right behind me is the legendary Hanging Gardens!" '
    '7-10s: She gestures with her free hand, panning the selfie camera slightly to reveal the breathtaking green terraces of the gardens and the shimmering river under the desert sun. '
    'Audio: no background music. Keep character dialogue and natural ambient sounds. '
    'Negative: second smartphone, floating phone, phone clamp, subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands, morphing.'
)

print("1. Patching Scene 0 with true 0.5x selfie prompts...", flush=True)
url = f"http://127.0.0.1:8100/api/scenes/{sid}"
data = json.dumps({
    "prompt": clean_image_prompt,
    "video_prompt": clean_video_prompt,
    "duration": 10.0,
    "narrator_text": "You guys... welcome to Babylon, 570 BC! And right behind me is the legendary Hanging Gardens!"
}).encode("utf-8")
req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"}, method="PATCH")
with urllib.request.urlopen(req) as resp:
    print(f"Patched Scene 0: status={resp.status}", flush=True)

print("2. Submitting REGENERATE_IMAGE for Scene 0...", flush=True)
req_payload = {
    "type": "REGENERATE_IMAGE",
    "scene_id": sid,
    "project_id": pid,
    "video_id": vid,
    "orientation": "HORIZONTAL"
}
req2 = urllib.request.Request(
    "http://127.0.0.1:8100/api/requests",
    data=json.dumps(req_payload).encode("utf-8"),
    headers={"Content-Type": "application/json"}
)
with urllib.request.urlopen(req2) as resp:
    res = json.loads(resp.read())
    req_id = res.get("id")
    print(f"Submitted REGENERATE_IMAGE request ID: {req_id} (status={res.get('status')})", flush=True)

print(f"3. Monitoring request {req_id}...", flush=True)
new_media_id = None
new_image_url = None

for poll in range(1, 40):
    time.sleep(3)
    try:
        r_data = json.loads(urllib.request.urlopen(f"http://127.0.0.1:8100/api/requests/{req_id}").read())
        st = r_data.get("status")
        print(f"  Poll {poll:02d}: status={st}", flush=True)
        if st == "COMPLETED":
            break
        elif st == "FAILED":
            print(f"Request failed: {r_data.get('error')}", flush=True)
            exit(1)
    except Exception as e:
        print(f"  Poll error: {e}", flush=True)

# Fetch new scene info
scene_info = json.loads(urllib.request.urlopen(f"http://127.0.0.1:8100/api/scenes/{sid}").read())
new_image_url = scene_info.get("horizontal_image_url")
new_media_id = scene_info.get("horizontal_image_media_id")
print(f"New Image Media ID: {new_media_id}", flush=True)
print(f"New Image URL: {new_image_url}", flush=True)

# Download image
dest1 = os.path.abspath("output/time_travel_vlog_hanging_gardens_of_babylon_570_bc/images/scene_01.jpg")
dest2 = r"C:\Users\Administrator\.gemini\antigravity-ide\brain\e22150ce-4262-4e3c-8619-a7731a7f7c3a\images\scene_01.jpg"

print(f"Downloading new start frame to {dest1}...", flush=True)
h = {"User-Agent": "Mozilla/5.0"}
dl_req = urllib.request.Request(new_image_url, headers=h)
with urllib.request.urlopen(dl_req, timeout=30) as resp:
    img_data = resp.read()
    with open(dest1, "wb") as f:
        f.write(img_data)
    with open(dest2, "wb") as f:
        f.write(img_data)

print(f"SUCCESS! Downloaded {len(img_data)/1024:.1f} KB to both paths.", flush=True)
