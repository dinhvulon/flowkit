import sqlite3
import json
import urllib.request
import os
import sys

# Ensure flowkit root in sys.path
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from agent.services.watermark import remove_watermark_image

PID = "ac50c619-1b31-4847-95d6-5379d02554c7"
VID = "dc2afa55-8a7f-42c3-bf8c-a13f580b6830"
SID_15 = "e2976cc7-5a59-41c3-a573-b7e3616ed969"
OUTDIR = "output/time_travel_vlog_ancient_babylon_570_bc"

NEW_PROMPT = (
    "Dynamic first-person selfie vlog photograph, wide-angle 0.5x front camera lens, shot handheld "
    "by young female traveler Mia while running at full speed for her life. Mia holds the camera firmly "
    "in her outstretched hand pointing directly back at her own face and upper torso as she sprints through "
    "a vaulted limestone gallery behind a thundering cascade of falling water in the Hanging Gardens of Babylon. "
    "Her honey-blonde ponytail whips wildly with motion blur, wide panicked alert eyes, breathless parted lips, "
    "flushed cheeks, wearing her signature desert-sand linen tunic with golden woven sash. Water spray and droplets "
    "hit the camera lens creating realistic wet lens flares. In the shadowy background corridor behind the waterfall, "
    "the menacing silhouettes of Babylonian palace guards with bronze helmets and spears are seen in hot pursuit. "
    "Authentic found-footage vlog urgency, natural torchlight reflecting on wet flagstones. "
    "Negative: holding lantern, lamp in hand, carrying flashlight, third person perspective, tripod, "
    "modern phone in frame, extra hands, distorted fingers, peaceful, static."
)

NEW_VIDEO_PROMPT = (
    "0-3s: Intense handheld front-facing phone camera selfie angle with heavy running camera shake and footstep "
    "vibrations as Mia sprints frantically through the wet stone gallery behind the roaring waterfall. "
    "3-7s: Water droplets splatter across the phone lens; Mia glances terrified over her shoulder at the armed guards "
    "pursuing in the shadowy background, panting heavily into the microphone \"They're right behind me! Running behind "
    "the waterfall—keep up!\" 7-10s: She veers sharply around a wet limestone archway into an upper stairwell, her face "
    "illuminated by flickering bronze torchlight as footsteps and distant Akkadian shouts echo off the wet walls. "
    "Audio: no background music. Keep character dialogue and natural ambient sounds. Negative: holding lantern, "
    "lamp in hand, third person shot, subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands."
)

def step1_patch_scene():
    conn = sqlite3.connect("flow_agent.db")
    c = conn.cursor()
    c.execute(
        "UPDATE scene SET prompt=?, video_prompt=?, character_names=?, horizontal_image_status='PENDING', vertical_image_status='PENDING' WHERE id=?",
        (NEW_PROMPT, NEW_VIDEO_PROMPT, json.dumps(["Mia", "Mia Outfit"]), SID_15)
    )
    conn.commit()
    conn.close()
    print("[1] Patched Scene 15 prompt & video_prompt with selfie running vlog perspective.")

def step2_submit_gen_image():
    payload = {
        "requests": [
            {
                "type": "REGENERATE_IMAGE",
                "scene_id": SID_15,
                "project_id": PID,
                "video_id": VID,
                "orientation": "HORIZONTAL"
            }
        ]
    }
    req = urllib.request.Request(
        "http://127.0.0.1:8100/api/requests/batch",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
    print(f"[2] Submitted REGENERATE_IMAGE for Scene 15: {res}")

if __name__ == "__main__":
    step1_patch_scene()
    step2_submit_gen_image()
