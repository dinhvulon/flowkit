#!/usr/bin/env python3
"""
Download all generated assets for Heian 1000:
- Reference images: output/heian_kyoto_1000/references/
- Scene images: output/heian_kyoto_1000/images/
- Scene videos: output/heian_kyoto_1000/videos/
"""
import os
import sys
import sqlite3
import urllib.request
from pathlib import Path

# Force UTF-8 stdout on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
OUT_DIR = BASE_DIR / "output" / "heian_kyoto_1000"
REFS_DIR = OUT_DIR / "references"
IMAGES_DIR = OUT_DIR / "images"
VIDEOS_DIR = OUT_DIR / "videos"

for d in (REFS_DIR, IMAGES_DIR, VIDEOS_DIR):
    d.mkdir(parents=True, exist_ok=True)

con = sqlite3.connect(BASE_DIR / "flow_agent.db")
cur = con.cursor()

# 1. Download References
print("[*] Downloading Reference Images...")
cur.execute("SELECT name, reference_image_url, media_id FROM character")
for name, url, mid in cur.fetchall():
    if not url:
        continue
    safe_name = name.lower().replace(" ", "_").replace("-", "_")
    target = REFS_DIR / f"{safe_name}_{mid[:8]}.jpg"
    if not target.exists():
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as resp:
            target.write_bytes(resp.read())
        print(f"  [OK] Saved ref: {target.name} ({target.stat().st_size // 1024} KB)")
    else:
        print(f"  - Exists: {target.name}")

# 2. Download Scene Images
print("\n[*] Downloading Scene Images...")
cur.execute("SELECT display_order, vertical_image_url, vertical_image_media_id FROM scene ORDER BY display_order")
for order, url, mid in cur.fetchall():
    if not url:
        continue
    target = IMAGES_DIR / f"scene_{order:02d}_{mid[:8]}.jpg"
    if not target.exists():
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as resp:
            target.write_bytes(resp.read())
        print(f"  [OK] Saved image: {target.name} ({target.stat().st_size // 1024} KB)")
    else:
        print(f"  - Exists: {target.name}")

# 3. Download Scene Videos
print("\n[*] Downloading Scene Videos...")
cur.execute("SELECT display_order, vertical_video_url, vertical_video_media_id FROM scene ORDER BY display_order")
for order, url, mid in cur.fetchall():
    if not url:
        continue
    target = VIDEOS_DIR / f"scene_{order:02d}_{mid[:8]}.mp4"
    if not target.exists():
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as resp:
            target.write_bytes(resp.read())
        print(f"  [OK] Saved video: {target.name} ({target.stat().st_size // (1024 * 1024):.1f} MB)")
    else:
        print(f"  - Exists: {target.name}")

con.close()
print("\n[+] All Heian 1000 assets downloaded successfully to:", OUT_DIR)
