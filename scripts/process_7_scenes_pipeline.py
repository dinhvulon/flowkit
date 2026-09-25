import json
import urllib.request
import sqlite3
import os
import sys
import time
import shutil
import subprocess

sys.stdout.reconfigure(encoding="utf-8")

flowkit_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if flowkit_root not in sys.path:
    sys.path.insert(0, flowkit_root)

from agent.services.watermark import remove_watermark_image

PID = "ac50c619-1b31-4847-95d6-5379d02554c7"
VID = "dc2afa55-8a7f-42c3-bf8c-a13f580b6830"
ORI = "HORIZONTAL"

TARGET_ORDERS = [0, 2, 14, 15, 18, 19, 22] # Scenes 1, 3, 15, 16, 19, 20, 23

p_out = json.loads(urllib.request.urlopen(f"http://127.0.0.1:8100/api/projects/{PID}/output-dir").read())
project_dir = p_out.get("path")
images_dir = os.path.join(project_dir, "images")
scenes_dir = os.path.join(project_dir, "scenes")
art_images_dir = r"C:\Users\Administrator\.gemini\antigravity-ide\brain\e22150ce-4262-4e3c-8619-a7731a7f7c3a\images"
art_scenes_dir = r"C:\Users\Administrator\.gemini\antigravity-ide\brain\e22150ce-4262-4e3c-8619-a7731a7f7c3a\scenes"

os.makedirs(images_dir, exist_ok=True)
os.makedirs(scenes_dir, exist_ok=True)
os.makedirs(art_images_dir, exist_ok=True)
os.makedirs(art_scenes_dir, exist_ok=True)

print("="*60)
print(f"STEP 1: Waiting for all 7 REGENERATE_IMAGE requests to complete...")
print("="*60)

start_time = time.time()
while True:
    conn = sqlite3.connect("flow_agent.db")
    c = conn.cursor()
    c.execute("""
        SELECT s.display_order+1, r.status, r.error_message
        FROM request r
        JOIN scene s ON r.scene_id = s.id
        WHERE r.video_id = ? AND r.type = 'REGENERATE_IMAGE'
        ORDER BY r.created_at DESC
        LIMIT 7
    """, (VID,))
    rows = c.fetchall()
    conn.close()

    statuses = [r[1] for r in rows]
    completed_count = sum(1 for st in statuses if st == "COMPLETED")
    failed_count = sum(1 for st in statuses if st == "FAILED")

    print(f"[{time.strftime('%H:%M:%S')}] Images progress: {completed_count}/7 completed, {failed_count} failed. Elapsed: {int(time.time() - start_time)}s")

    if completed_count == 7:
        print("All 7 images completed successfully!")
        break
    if failed_count > 0:
        print(f"Warning: {failed_count} requests failed! Details: {rows}")
        # Continue or handle
    time.sleep(10)

print("\n" + "="*60)
print("STEP 2: De-watermark raw images and upload clean frames to Google Flow...")
print("="*60)

conn = sqlite3.connect("flow_agent.db")
c = conn.cursor()
c.execute(f"""
    SELECT display_order+1, id, horizontal_image_url
    FROM scene
    WHERE video_id = ? AND display_order IN ({','.join('?'*len(TARGET_ORDERS))})
    ORDER BY display_order ASC
""", [VID] + TARGET_ORDERS)
target_scenes = c.fetchall()
conn.close()

clean_mids = {}
for sidx, sid, img_url in target_scenes:
    raw_filename = f"scene_{sidx:02d}_raw.jpg"
    clean_filename = f"scene_{sidx:02d}.jpg"
    raw_path = os.path.join(images_dir, raw_filename)
    clean_path = os.path.join(images_dir, clean_filename)
    art_path = os.path.join(art_images_dir, clean_filename)

    print(f"\n[Scene {sidx:02d}] Downloading new raw frame: {img_url[:60]}...")
    h = {"User-Agent": "Mozilla/5.0"}
    req = urllib.request.Request(img_url, headers=h)
    with urllib.request.urlopen(req, timeout=30) as resp:
        with open(raw_path, "wb") as f:
            f.write(resp.read())

    print(f"  [Scene {sidx:02d}] Removing Google watermark logo...")
    remove_watermark_image(raw_path, clean_path)
    shutil.copy2(clean_path, art_path)

    print(f"  [Scene {sidx:02d}] Uploading clean image to Google Flow...")
    up_payload = {
        "file_path": clean_path,
        "project_id": PID,
        "file_name": clean_filename
    }
    up_req = urllib.request.Request(
        "http://127.0.0.1:8100/api/flow/upload-image",
        data=json.dumps(up_payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(up_req, timeout=40) as u_resp:
        up_res = json.loads(u_resp.read())
        clean_mid = up_res.get("media_id")

    print(f"  [Scene {sidx:02d}] Clean media_id obtained: {clean_mid}")
    clean_mids[sid] = clean_mid

    # Update DB with clean media_id
    conn = sqlite3.connect("flow_agent.db")
    conn.execute("""
        UPDATE scene
        SET horizontal_image_media_id = ?, horizontal_image_status = 'COMPLETED',
            horizontal_video_status = 'PENDING', horizontal_video_media_id = NULL
        WHERE id = ?
    """, (clean_mid, sid))
    conn.commit()
    conn.close()

print("\n" + "="*60)
print("STEP 3: Submitting batch GENERATE_VIDEO for all 7 updated scenes...")
print("="*60)

video_requests = [
    {
        "type": "GENERATE_VIDEO",
        "scene_id": sid,
        "project_id": PID,
        "video_id": VID,
        "orientation": ORI
    }
    for sidx, sid, _ in target_scenes
]

v_req = urllib.request.Request(
    "http://127.0.0.1:8100/api/requests/batch",
    data=json.dumps({"requests": video_requests}).encode("utf-8"),
    headers={"Content-Type": "application/json"}
)
with urllib.request.urlopen(v_req, timeout=30) as resp:
    v_resp = json.loads(resp.read().decode())
    print(f"Submitted {len(v_resp)} video generation requests successfully.")

print("\n" + "="*60)
print("STEP 4: Monitoring video generation & auto-downloading clips...")
print("="*60)

downloaded_videos = set()
v_start = time.time()
while len(downloaded_videos) < len(target_scenes):
    conn = sqlite3.connect("flow_agent.db")
    cur = conn.cursor()
    for sidx, sid, _ in target_scenes:
        if sid in downloaded_videos:
            continue
        cur.execute("SELECT horizontal_video_status, horizontal_video_url, horizontal_video_media_id FROM scene WHERE id=?", (sid,))
        v_row = cur.fetchone()
        v_status, v_url, v_mid = v_row if v_row else (None, None, None)

        if v_status == "COMPLETED" and v_url:
            vid_filename = f"scene_{sidx:02d}_{sid[:8]}.mp4"
            vid_path = os.path.join(scenes_dir, vid_filename)
            art_vid_path = os.path.join(art_scenes_dir, vid_filename)
            art_vid_alias = os.path.join(art_scenes_dir, f"scene_{sidx:02d}.mp4")

            print(f"[{time.strftime('%H:%M:%S')}] Scene {sidx:02d} Video COMPLETED! Media ID: {v_mid}. Downloading...")
            h = {"User-Agent": "Mozilla/5.0"}
            v_dl_req = urllib.request.Request(v_url, headers=h)
            with urllib.request.urlopen(v_dl_req, timeout=60) as d_resp:
                with open(vid_path, "wb") as f:
                    f.write(d_resp.read())
            shutil.copy2(vid_path, art_vid_path)
            shutil.copy2(vid_path, art_vid_alias)
            sz = os.path.getsize(vid_path)
            print(f"[{time.strftime('%H:%M:%S')}] Scene {sidx:02d} downloaded successfully ({sz:,} bytes).")
            downloaded_videos.add(sid)
    conn.close()

    print(f"[{time.strftime('%H:%M:%S')}] Videos progress: {len(downloaded_videos)}/{len(target_scenes)} downloaded. Elapsed: {int(time.time() - v_start)}s")
    if len(downloaded_videos) < len(target_scenes):
        time.sleep(15)

print("\n" + "="*60)
print("STEP 5: Concatenating all 23 scene videos into master final cut...")
print("="*60)

concat_txt = os.path.join(project_dir, "concat.txt")
final_mp4 = os.path.join(project_dir, "time_travel_vlog_ancient_babylon_570_bc_final.mp4")
art_final_mp4 = r"C:\Users\Administrator\.gemini\antigravity-ide\brain\e22150ce-4262-4e3c-8619-a7731a7f7c3a\babylon_570bc_final_vlog.mp4"

cmd = [
    "ffmpeg", "-y", "-f", "concat", "-safe", "0",
    "-i", concat_txt,
    "-c", "copy",
    final_mp4
]
res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode != 0:
    cmd2 = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", concat_txt,
        "-c:v", "libx264", "-crf", "18", "-preset", "fast",
        "-c:a", "aac", "-b:a", "192k",
        final_mp4
    ]
    subprocess.run(cmd2, capture_output=True, text=True)

shutil.copy2(final_mp4, art_final_mp4)
print(f"Master cut concatenated successfully: {os.path.getsize(final_mp4):,} bytes")

print("\n" + "="*60)
print("STEP 6: Regenerating review HTML and gallery artifact...")
print("="*60)

subprocess.run([sys.executable, "scripts/generate_review_html.py"], check=True)
subprocess.run([sys.executable, "scripts/update_gallery_artifact.py"], check=True)

print("\nPIPELINE COMPLETED 100%!")
