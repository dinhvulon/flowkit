import sys
import json
import time
import subprocess
import urllib.request
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

PID = "195a112e-7537-4b61-b3c6-03188e4f12d1"
BASE_URL = f"http://127.0.0.1:8100/api/projects/{PID}/generate-thumbnail"
OUT_DIR = Path("output/kamakura_1274_mongol_invasion_hakata_bay_pov_vlog/thumbnails")
OUT_DIR.mkdir(parents=True, exist_ok=True)

variants = [
    {
        "filename": "thumbnail_ja_v1.png",
        "prompt": (
            "YouTube thumbnail, bold yellow text in Japanese clearly \"1274年博多湾！\" at top center in thick sans-serif gothic font with red outline, "
            "smaller white text in Japanese clearly \"元軍が日本に上陸した瞬間\" below in bold font with black shadow, "
            "vlogger female character face taking up 40% of frame looking directly into lens with extreme awe and shock, "
            "wearing rough 1274 Kamakura indigo hemp kosode, dramatic beach background with rising smoke and pine trees, "
            "4K, HDR, high contrast, sharp focus, 1280x720 16:9 format"
        ),
        "character_names": ["Vlogger"],
        "aspect_ratio": "LANDSCAPE"
    },
    {
        "filename": "thumbnail_ja_v2.png",
        "prompt": (
            "YouTube thumbnail, bold golden text in Japanese clearly \"神風前夜！\" at upper left in thick brush calligraphy font with dark outline, "
            "smaller white text in Japanese clearly \"鎌倉武士の決死の反撃\" below in bold gothic font with shadow, "
            "epic cinematic battle scene, Kamakura cavalry samurai in ornate O-yoroi armor galloping on beach with drawn bow, "
            "violent crashing ocean waves and dark storm tempest clouds, 4K, HDR, 1280x720 16:9 format"
        ),
        "character_names": ["Kamakura Cavalry Samurai"],
        "aspect_ratio": "LANDSCAPE"
    },
    {
        "filename": "thumbnail_ja_v3.png",
        "prompt": (
            "YouTube thumbnail, bold bright crimson text in Japanese clearly \"900隻の大船団！\" at top in heavy bold font with white outline, "
            "smaller yellow text in Japanese clearly \"迫り来る元寇の脅威\" below with shadow, "
            "vast terrifying Mongol invasion warships with black flags covering Hakata Bay horizon, "
            "vlogger in foreground looking out at the massive fleet in disbelief, 4K, 1280x720 16:9 format"
        ),
        "character_names": ["Vlogger"],
        "aspect_ratio": "LANDSCAPE"
    },
    {
        "filename": "thumbnail_ja_v4.png",
        "prompt": (
            "YouTube thumbnail, bold flame orange text in Japanese clearly \"謎の爆弾・てつはう！\" at upper center with dark drop shadow, "
            "smaller white text in Japanese clearly \"日本を震撼させた火薬兵器\" below in clean bold font, "
            "close-up of a spherical iron Tetsuhau bomb with smoking fuse on coastal sand, "
            "dramatic fiery explosion light in background, historical warfare, 4K, 1280x720 16:9 format"
        ),
        "character_names": ["Tetsuhau Explosive Bomb"],
        "aspect_ratio": "LANDSCAPE"
    }
]

for idx, var in enumerate(variants, 1):
    print(f"[*] Generating Japanese Thumbnail Variant {idx}: {var['filename']}...")
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
            print(f"    [+] Variant {idx} generated successfully!")
    except Exception as e:
        print(f"    [!] Variant {idx} failed: {e}")
    time.sleep(8)

# Resize to standard 1280x720 YouTube format
print("\n[*] Resizing Japanese thumbnails to 1280x720...")
for i in range(1, 5):
    src = OUT_DIR / f"thumbnail_ja_v{i}.png"
    dst = OUT_DIR / f"thumbnail_ja_v{i}_yt.png"
    if src.exists():
        subprocess.run([
            "ffmpeg", "-y", "-i", str(src),
            "-vf", "scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2:color=black",
            str(dst)
        ], capture_output=True)
        print(f"  [+] Resized: {dst.name} ({dst.stat().st_size // 1024} KB)")

print("\n[+] All Japanese thumbnails ready!")
