import sys
import json
import time
import urllib.request
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

PID = "195a112e-7537-4b61-b3c6-03188e4f12d1"
BASE_URL = f"http://127.0.0.1:8100/api/projects/{PID}/generate-thumbnail"

variants = [
    {
        "filename": "thumbnail_v1.png",
        "prompt": (
            "YouTube thumbnail, bold yellow text in Vietnamese clearly \"1274 ĐỔ BỘ!\" at top center in thick sans-serif font with red outline, "
            "smaller white text in Vietnamese clearly \"QUÂN MÔNG CỔ TẤN CÔNG NHẬT BẢN\" below in bold font with black shadow, "
            "vlogger female character face 40% of frame looking into lens with extreme awe and shock, "
            "wearing rough indigo hemp kosode, dramatic Hakata bay beach background with distant smoke, "
            "4K, HDR, high contrast, sharp focus, 1280x720 16:9 format"
        ),
        "character_names": ["Vlogger"],
        "aspect_ratio": "LANDSCAPE"
    },
    {
        "filename": "thumbnail_v2.png",
        "prompt": (
            "YouTube thumbnail, bold golden text in Vietnamese clearly \"SẤM SÉT VỊNH HAKATA!\" at upper left in thick font with dark outline, "
            "smaller white text in Vietnamese clearly \"CƠN BÃO THẦN CỨU NƯỚC NHẬT\" below with shadow, "
            "epic cinematic battle scene, Kamakura cavalry samurai in ornate O-yoroi armor on horseback galloping on Hakata beach, "
            "violent crashing ocean waves and dark storm clouds, 4K, HDR, highly detailed, 1280x720 16:9 format"
        ),
        "character_names": ["Kamakura Cavalry Samurai"],
        "aspect_ratio": "LANDSCAPE"
    },
    {
        "filename": "thumbnail_v3.png",
        "prompt": (
            "YouTube thumbnail, bold bright red text in Vietnamese clearly \"900 CHIẾN THUYỀN!\" at top in heavy sans-serif font with white outline, "
            "smaller yellow text in Vietnamese clearly \"HẠM ĐỘI NGUYÊN MÔNG ĐỔ BỘ\" below with shadow, "
            "vast dark Mongol invasion warships with black dragon banners filling Hakata Bay horizon, "
            "vlogger in foreground looking out at the terrifying armada in disbelief, 4K, 1280x720 16:9 format"
        ),
        "character_names": ["Vlogger"],
        "aspect_ratio": "LANDSCAPE"
    },
    {
        "filename": "thumbnail_v4.png",
        "prompt": (
            "YouTube thumbnail, bold orange text in Vietnamese clearly \"VŨ KHÍ BÍ MẬT 1274!\" at upper center with black drop shadow, "
            "smaller white text in Vietnamese clearly \"QUẢ BOM THUỐC NỔ ĐẦU TIÊN\" below in clean bold font, "
            "close-up of a spherical iron Tetsuhau bomb with smoking fuse on sandy ground, "
            "dramatic fiery explosion light in background, historical warfare, 4K, 1280x720 16:9 format"
        ),
        "character_names": ["Tetsuhau Explosive Bomb"],
        "aspect_ratio": "LANDSCAPE"
    }
]

for idx, var in enumerate(variants, 1):
    print(f"[*] Generating Thumbnail Variant {idx}: {var['filename']}...")
    payload = {
        "prompt": var["prompt"],
        "character_names": var["character_names"],
        "aspect_ratio": var["aspect_ratio"],
        "output_filename": var["filename"]
    }
    req = urllib.request.Request(
        BASE_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            res_data = json.loads(resp.read())
            print(f"    [+] Variant {idx} generated successfully! Output: {res_data.get('output_path')}")
    except Exception as e:
        print(f"    [!] Variant {idx} failed: {e}")
    time.sleep(8)

print("\n[+] Thumbnail generation completed.")
