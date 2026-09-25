import json
import urllib.request
import sqlite3
import os
import sys
import time
import subprocess
import shutil
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8")

flowkit_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if flowkit_root not in sys.path:
    sys.path.insert(0, flowkit_root)

from agent.services.watermark import remove_watermark_image

pid = "ac50c619-1b31-4847-95d6-5379d02554c7"
vid = "dc2afa55-8a7f-42c3-bf8c-a13f580b6830"

p_out = json.loads(urllib.request.urlopen(f"http://127.0.0.1:8100/api/projects/{pid}/output-dir").read())
project_dir = p_out.get("path")
images_dir = os.path.join(project_dir, "images")
scenes_dir = os.path.join(project_dir, "scenes")
final_out = os.path.join(project_dir, "time_travel_vlog_ancient_babylon_570_bc_final.mp4")
brain_out = r"C:\Users\Administrator\.gemini\antigravity-ide\brain\e22150ce-4262-4e3c-8619-a7731a7f7c3a\babylon_570bc_final_vlog.mp4"
art_images_dir = r"C:\Users\Administrator\.gemini\antigravity-ide\brain\e22150ce-4262-4e3c-8619-a7731a7f7c3a\images"

# 1. Update character_names to include ["Mia", "Mia Outfit"] for all scenes
print("1. Updating character_names across all scenes to ['Mia', 'Mia Outfit']...", flush=True)
conn = sqlite3.connect("flow_agent.db")
conn.execute("UPDATE scene SET character_names = '[\"Mia\", \"Mia Outfit\"]' WHERE video_id = ?", (vid,))
conn.commit()

# Specific Scene Updates requested by User
# Scene 03 (order 2): Boatman rowing quffa boat carrying saplings
# Scene 08 (order 7): Propped camera, no phone on table, Mia eating fig
# Scene 10 (order 9): Delicate female hand holding silver wire shekel
# Scene 12 (order 11): Only ONE female traveler (Mia) looking at two guards
# Scene 15 (order 14): Sprinting behind waterfall, hands empty, no lantern
# Scene 16 (order 15): Relieved inside upper nursery, closing wooden door, hands empty
# Scene 20 (order 19): 0.5x vlog on cantilevered balcony, right hand empty pointing, no phone
# Scene 23 (order 22): Seated on stone balustrade at sunset, hands resting/waving, no selfie phone

updates = {
    2: { # Scene 03
        "prompt": "First-person POV looking out over the shimmering green waters of the Euphrates river, an ancient muscular Babylonian boatman in a coarse linen loincloth standing inside a circular black bitumen-coated quffa boat, vigorously rowing with a broad wooden paddle, ferrying rich alluvial soil and young palm saplings toward the stone palace docks in ancient Babylon. Cinematic natural daylight, documentary realism. Negative: empty boat, no boatman, motorboat, modern clothes, smartphone.",
        "video_prompt": '0-3s: First-person eye-level POV tracking an ancient Babylonian boatman standing inside a circular black bitumen quffa boat, rowing steadily with a broad wooden paddle across the shimmering Euphrates river. 3-7s: Mia\'s voice speaks with deep fascination "Every single drop of water and every basket of rich soil feeding those rooftop trees starts right here from this river." 7-10s: The circular boat glides toward a timber dock as the camera pans toward the stone masonry of the royal aqueduct. Audio: no background music. Keep character dialogue and natural ambient sounds. Negative: empty boat, modern boat, subtitles, captions, watermark, text on screen, logo, blurry faces.',
        "character_names": [] # No Mia visible in frame, just the boatman
    },
    7: { # Scene 08
        "prompt": "Cinematic eye-level documentary medium shot of a young traveler Mia seated relaxed on a woven reed stool at a rustic ancient wooden table on a shaded terrace of Babylon, wearing a deep-cream linen tunic with woven waist sash. She smiles naturally facing the camera while holding a fresh split ripe purple fig in one hand, flatbread and an earthenware clay water cup resting on the wooden table. Sun-dappled warm natural lighting filtering through grapevines overhead. Negative: smartphone, mobile phone on table, modern tech, selfie stick, tripod, clamp, phone holder.",
        "video_prompt": '0-3s: Fixed static eye-level camera shot of Mia sitting relaxed at a rustic wooden table, taking a delicate bite of a fresh ripe fig. 3-7s: Mia closes her eyes in pure culinary delight, looking into the camera lens with a happy smile "Honestly, tasting a fig picked directly from the Hanging Gardens of Babylon? This is absolute bucket-list perfection." 7-10s: She takes a sip of water from her unglazed clay cup, smiling warmly toward the camera. Audio: no background music. Keep character dialogue and natural ambient sounds. Negative: smartphone, mobile phone on table, selfie stick, phone clamp, subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.',
        "character_names": ["Mia", "Mia Outfit"]
    },
    9: { # Scene 10
        "prompt": "First-person POV looking down at an ancient bronze pan balance on a carved stone pedestal in Babylon. The slender, delicate female hand of a young traveler Mia with natural light skin tone and linen sleeve cuff holds a small coiled silver wire clipping (ancient shekel) over the scale, while an ancient Babylonian merchant in fringed wool robes places hematite stone seed weights on the opposite bronze pan. Depth of field, authentic ancient market detail. Negative: hairy male hand, rough hand, distorted fingers, extra fingers, smartphone.",
        "video_prompt": '0-3s: First-person POV as Mia\'s delicate female hand enters the frame holding a coiled silver wire as the merchant carefully balances stone weights on the bronze pan. 3-7s: Mia whispers in fascination "No minted coins here in 570 BC... just little curls of silver wire called shekels, weighed by hand to trade for rare mountain spices." 7-10s: The merchant hands her a bundle of fragrant mountain herbs; the camera tilts smoothly up toward a grand stone stairway. Audio: no background music. Keep character dialogue and natural ambient sounds. Negative: male hand, modern coins, subtitles, captions, watermark, text on screen, logo, distorted fingers.',
        "character_names": ["Mia", "Mia Outfit"]
    },
    11: { # Scene 12
        "prompt": "Cinematic medium shot of ONE single young female traveler Mia seen from behind and 3/4 profile, honey-blonde ponytail, deep-cream linen tunic with woven waist sash. She stands alone on a monumental stone terrace overlooking a lush garden of blooming lilies and pomegranate trees, looking ahead toward two tall male Babylonian imperial guards in bronze scale armor and conical helmets standing guard fifty feet away. Only ONE female traveler in frame. Negative: two girls, two female travelers, clone, twin, duplicate person, second woman, smartphone.",
        "video_prompt": '0-3s: Camera opens on the back of Mia\'s honey-blonde ponytail as she stands alone on the terrace, turning her head slightly to see two tall Babylonian guards standing guard in the distance. 3-7s: Her eyes widen in shock as she whispers "Look at this grand terrace... an explosion of royal flowers! But wait... armed imperial guards are patrolling right ahead!" 7-10s: She ducks swiftly to the right, crouching low behind an ornamental carved limestone column. Audio: no background music. Keep character dialogue and natural ambient sounds. Negative: two women, clone, duplicate character, subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.',
        "character_names": ["Mia", "Mia Outfit"]
    },
    14: { # Scene 15
        "prompt": "High-energy dynamic action shot of a young traveler Mia sprinting full speed through a misty vaulted stone gallery directly behind an ancient roaring waterfall in the Hanging Gardens of Babylon. Water spray glistening in air, wall-mounted bronze torches illuminating the wet stone walls in the background. Mia is running with both hands completely empty, athletic running posture, terrified yet determined facial expression, honey-blonde ponytail flying behind her, wearing deep-cream linen tunic. Negative: handheld lantern, holding lamp, carrying torch, flashlight, modern clothes, smartphone.",
        "video_prompt": '0-3s: High-energy chase camera tracking Mia sprinting with both hands empty through a shadowy stone gallery directly behind a thundering curtain of falling water. 3-7s: Water spray drenches her face; she glances backward into the camera, panting heavily "Running for my life behind a 2,500-year-old waterfall... completely terrifying but insane!" 7-10s: She leaps over a stone water sluice, dodging sharply around a mossy arched corner into an upper courtyard. Audio: no background music. Keep character dialogue and natural ambient sounds. Negative: holding lantern, lamp in hand, subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.',
        "character_names": ["Mia", "Mia Outfit"]
    },
    15: { # Scene 16
        "prompt": "Cinematic eye-level shot of a young traveler Mia stepping inside a quiet sheltered botanical nursery on an upper garden terrace of Babylon, surrounded by earthenware terracotta pots with date palm saplings and woven reed shade awnings. She pulls shut a weathered cedar wooden door with a quiet latch, pressing her back against the sun-baked mudbrick wall, exhaling with deep relief, both hands completely empty, wearing deep-cream linen tunic with woven sash. Warm afternoon sunlight streaming through wooden slats. Negative: modern door, modern pots, distorted hands, smartphone.",
        "video_prompt": '0-3s: Mia steps through a weathered cedar gate, pulls it shut until the wooden latch clicks, and slides down against the sun-baked mudbrick wall. 3-7s: She takes deep shuddering breaths, pressing a trembling hand to her chest "Okay... we lost them. The guards just thundered down toward the lower barracks. We\'re safe in the upper nursery." 7-10s: The loud pursuit fades into distant courtyard echoes, replaced by gentle afternoon bird calls in the quiet nursery. Audio: no background music. Keep character dialogue and natural ambient sounds. Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.',
        "character_names": ["Mia", "Mia Outfit"]
    },
    19: { # Scene 20
        "prompt": "Ultra-wide 0.5x front-camera vlog shot of a young traveler Mia standing on a massive cantilevered stone balcony jutting out over ancient Babylon, lush blooming flowering vines draping over the parapet. Mia looks directly into the camera lens with a radiant smile; her right arm is extended toward the viewer with her hand open and relaxed, her left hand gesturing toward the breathtaking view of Babylon spreading out below. Negative: smartphone in hand, holding phone, cell phone, selfie stick, phone case, modern gadget.",
        "video_prompt": '0-3s: Ultra-wide 0.5x vlog camera looking at Mia standing on the cantilevered stone balcony as desert winds whip through lush climbing vines and her blonde ponytail. 3-7s: Mia beams directly into the camera lens with an engaging smile "Historical myth busted: the gardens weren\'t \'hanging\' on ropes! The Greek term \'kremastos\' means \'overhanging\'—just like these dramatic terraces jutting out over the city!" 7-10s: She turns smoothly to walk toward the sparkling summit fountain pool in the background. Audio: no background music. Keep character dialogue and natural ambient sounds. Negative: holding phone in hand, smartphone, selfie stick, subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.',
        "character_names": ["Mia", "Mia Outfit"]
    },
    22: { # Scene 23
        "prompt": "Cinematic eye-level documentary shot of a young traveler Mia seated peacefully on an ancient carved stone balustrade draped with wild pink roses, wearing her signature deep-cream linen tunic and woven sash. She faces the camera smiling with heartfelt warmth, both hands resting gently and naturally on the warm stone ledge beside her. Behind her, the Euphrates river glitters under a breathtaking golden, amber, and violet sunset sky over ancient Babylon. Completely hands-free, peaceful candid travel vlog portrait. Negative: holding smartphone, selfie stick, mobile phone, phone clamp, camera in hand, modern gadget.",
        "video_prompt": '0-3s: Static eye-level camera shot looking at Mia seated peacefully on the stone parapet as the sky turns into rich violet, amber, and gold. 3-7s: Mia gazes warmly into the lens, speaking with heartfelt sincerity "A wonder built entirely out of love for a queen who longed for home. Ancient Babylon in 570 BC is unforgettable. Where should we travel next?" 7-10s: She smiles softly, gives a gentle wave toward the camera with her right hand, and the scene peacefully fades into evening twilight. Audio: no background music. Keep character dialogue and natural ambient sounds. Negative: holding phone, smartphone, selfie stick, subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.',
        "character_names": ["Mia", "Mia Outfit"]
    }
}

target_scene_ids = []
for order, data in updates.items():
    c = conn.cursor()
    c.execute("SELECT id FROM scene WHERE video_id = ? AND display_order = ?", (vid, order))
    row = c.fetchone()
    if row:
        sid = row[0]
        target_scene_ids.append((order + 1, sid, data))
        conn.execute("""
            UPDATE scene
            SET prompt = ?, video_prompt = ?, character_names = ?
            WHERE id = ?
        """, (data["prompt"], data["video_prompt"], json.dumps(data["character_names"]), sid))

conn.commit()
conn.close()

print(f"2. Updated prompts for {len(target_scene_ids)} scenes in database.")

# 3. Submit REGENERATE_IMAGE batch
batch_img_requests = []
for sidx, sid, data in target_scene_ids:
    batch_img_requests.append({
        "type": "REGENERATE_IMAGE",
        "scene_id": sid,
        "project_id": pid,
        "video_id": vid,
        "orientation": "HORIZONTAL"
    })

print(f"3. Submitting REGENERATE_IMAGE batch for scenes: {[s[0] for s in target_scene_ids]}...", flush=True)
req = urllib.request.Request(
    "http://127.0.0.1:8100/api/requests/batch",
    data=json.dumps({"requests": batch_img_requests}).encode("utf-8"),
    headers={"Content-Type": "application/json"}
)
with urllib.request.urlopen(req) as resp:
    res = json.loads(resp.read())
    print(f"Batch submitted! Response count: {len(res)}", flush=True)

# 4. Poll image batch status
print("4. Polling image generation status...", flush=True)
poll_url = f"http://127.0.0.1:8100/api/requests/batch-status?video_id={vid}&type=GENERATE_IMAGE"

for p in range(1, 45):
    time.sleep(10)
    try:
        bs_resp = json.loads(urllib.request.urlopen(poll_url).read())
        completed = bs_resp.get("completed", 0)
        pending = bs_resp.get("pending", 0)
        processing = bs_resp.get("processing", 0)
        failed = bs_resp.get("failed", 0)
        is_done = bs_resp.get("done", False)

        print(f"  [Poll {p:02d}] Completed: {completed} | Processing: {processing} | Pending: {pending} | Failed: {failed}", flush=True)
        if is_done or (pending == 0 and processing == 0):
            print("Image regeneration completed!", flush=True)
            break
    except Exception as e:
        print(f"  [Poll {p:02d}] Polling error: {e}", flush=True)

# 5. Download raw images, remove watermarks, and upload clean images to Google Flow
print("\n5. Downloading, inpainting watermark, and re-uploading clean start frames...", flush=True)

for sidx, sid, data in target_scene_ids:
    raw_filename = f"scene_{sidx:02d}_raw.jpg"
    clean_filename = f"scene_{sidx:02d}.jpg"
    raw_path = os.path.join(images_dir, raw_filename)
    clean_path = os.path.join(images_dir, clean_filename)
    art_path = os.path.join(art_images_dir, clean_filename)

    # Get fresh horizontal_image_url from DB
    conn = sqlite3.connect("flow_agent.db")
    c = conn.cursor()
    c.execute("SELECT horizontal_image_url FROM scene WHERE id = ?", (sid,))
    img_url = c.fetchone()[0]
    conn.close()

    if img_url:
        try:
            h = {"User-Agent": "Mozilla/5.0"}
            dl_req = urllib.request.Request(img_url, headers=h)
            with urllib.request.urlopen(dl_req, timeout=30) as d_resp:
                with open(raw_path, "wb") as f:
                    f.write(d_resp.read())
            remove_watermark_image(raw_path, clean_path)
            shutil.copy(clean_path, art_path)
            print(f"  [Scene {sidx:02d}] Inpainted clean image saved.", flush=True)
        except Exception as e:
            print(f"  [Scene {sidx:02d}] Inpaint error: {e}", flush=True)

    # Upload clean image to Google Flow
    if os.path.exists(clean_path):
        for retry in range(4):
            try:
                up_payload = {
                    "file_path": clean_path,
                    "project_id": pid,
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

                print(f"  [Scene {sidx:02d}] Uploaded clean frame! New media_id: {clean_mid}", flush=True)

                # Patch SQLite
                conn = sqlite3.connect("flow_agent.db")
                conn.execute("UPDATE scene SET horizontal_image_media_id = ?, horizontal_image_status = 'COMPLETED' WHERE id = ?", (clean_mid, sid))
                conn.commit()
                conn.close()
                break
            except Exception as e:
                print(f"  [Scene {sidx:02d}] Upload retry {retry+1} error: {e}", flush=True)
                time.sleep(3)

# 6. Submit REGENERATE_VIDEO batch for the 8 scenes
print("\n6. Submitting REGENERATE_VIDEO batch for the 8 updated scenes...", flush=True)

# Reset video status in DB to PENDING
conn = sqlite3.connect("flow_agent.db")
conn.execute("UPDATE scene SET horizontal_video_status = 'PENDING', horizontal_video_url = NULL, horizontal_video_media_id = NULL WHERE id IN ({})".format(','.join('?' * len(target_scene_ids))), [s[1] for s in target_scene_ids])
conn.commit()
conn.close()

batch_video_requests = []
for sidx, sid, data in target_scene_ids:
    batch_video_requests.append({
        "type": "REGENERATE_VIDEO",
        "scene_id": sid,
        "project_id": pid,
        "video_id": vid,
        "orientation": "HORIZONTAL"
    })

req = urllib.request.Request(
    "http://127.0.0.1:8100/api/requests/batch",
    data=json.dumps({"requests": batch_video_requests}).encode("utf-8"),
    headers={"Content-Type": "application/json"}
)
with urllib.request.urlopen(req) as resp:
    res = json.loads(resp.read())
    print(f"Video batch submitted! Response count: {len(res)}", flush=True)

# 7. Monitor video generation and download completed videos
print("\n7. Monitoring video generation and downloading updated clips...", flush=True)
downloaded_vids = set()

for poll in range(1, 60):
    time.sleep(15)
    now_str = datetime.now().strftime("%H:%M:%S")

    conn = sqlite3.connect("flow_agent.db")
    c = conn.cursor()
    c.execute("""
        SELECT display_order+1, id, horizontal_video_status, horizontal_video_url
        FROM scene
        WHERE id IN ({})
    """.format(','.join('?' * len(target_scene_ids))), [s[1] for s in target_scene_ids])
    v_rows = c.fetchall()
    conn.close()

    completed_count = 0
    for sidx, sid, vstatus, vurl in v_rows:
        if vstatus == "COMPLETED":
            completed_count += 1
            if sid not in downloaded_vids and vurl:
                local_filename = f"scene_{sidx:02d}_{sid[:8]}.mp4"
                local_path = os.path.join(scenes_dir, local_filename)
                try:
                    h = {"User-Agent": "Mozilla/5.0"}
                    dl_req = urllib.request.Request(vurl, headers=h)
                    with urllib.request.urlopen(dl_req, timeout=60) as v_resp:
                        with open(local_path, "wb") as vf:
                            vf.write(v_resp.read())
                    downloaded_vids.add(sid)
                    print(f"[{now_str}] [Scene {sidx:02d}] Updated video downloaded successfully!", flush=True)
                except Exception as e:
                    print(f"[{now_str}] [Scene {sidx:02d}] Video download error: {e}", flush=True)

    print(f"[{now_str}] Video progress: {completed_count}/{len(target_scene_ids)} completed", flush=True)
    if completed_count == len(target_scene_ids) and len(downloaded_vids) == len(target_scene_ids):
        print("All updated videos generated and downloaded!", flush=True)
        break

# 8. Re-concatenate into final video
print("\n8. Re-concatenating all 23 scene videos into final master cut...", flush=True)
files = sorted([f for f in os.listdir(scenes_dir) if f.startswith("scene_") and f.endswith(".mp4")])
concat_txt_path = os.path.join(project_dir, "concat.txt")
with open(concat_txt_path, "w", encoding="utf-8") as f:
    for filename in files:
        full_path = os.path.abspath(os.path.join(scenes_dir, filename)).replace("\\", "/")
        f.write(f"file '{full_path}'\n")

cmd = [
    "ffmpeg", "-y",
    "-f", "concat",
    "-safe", "0",
    "-i", concat_txt_path,
    "-c", "copy",
    "-movflags", "+faststart",
    final_out
]
res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode != 0:
    cmd_reencode = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", concat_txt_path,
        "-c:v", "libx264", "-preset", "fast", "-crf", "18",
        "-r", "24", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart",
        final_out
    ]
    subprocess.run(cmd_reencode, capture_output=True, text=True)

shutil.copy(final_out, brain_out)
print(f"Final master cut updated: {final_out} ({os.path.getsize(final_out)/(1024*1024):.1f} MB)")
print("ALL DONE!")
