import sqlite3
import json
import urllib.request
import os
import sys
import time
import shutil

# Ensure flowkit root in sys.path
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from agent.services.watermark import remove_watermark_image

PID = "ac50c619-1b31-4847-95d6-5379d02554c7"
VID = "dc2afa55-8a7f-42c3-bf8c-a13f580b6830"
ORI = "HORIZONTAL"

TARGETS = [
    {
        "index": 4,
        "sid": "54ede954-6208-45cb-9081-547b08c6fa05",
        "prompt": (
            "Cinematic wide low-angle documentary shot in ancient Babylon. Young female traveler Mia is "
            "ALREADY standing in the lower-right third of the frame, wearing her signature desert-sand linen "
            "tunic with golden woven sash and blonde ponytail, looking up in awe at an enormous monumental ancient "
            "wooden chain-of-buckets water pump system creaking beside a massive baked-brick aqueduct pillar. "
            "Glistening river water pours continuously from wooden buckets into a high stone canal under bright morning "
            "sunlight. Pure ancient Mesopotamian hydraulic engineering. Negative: empty scene, modern clothes, "
            "smartphone, metal pipes, modern machinery, extra hands, distorted fingers."
        ),
        "video_prompt": (
            "0-3s: The camera holds low as river water cascades from the colossal wooden chain-of-buckets wheel "
            "creaking steadily overhead. Mia turns her head from looking up at the wheel toward the camera lens. "
            "3-7s: Mia shields her eyes from the sun with one hand, shouting excitedly over the roaring water "
            "\"Look at this mechanical chain pump! 2,500 years ago, lifting thousands of gallons into the desert sky "
            "every hour!\" 7-10s: Cool water spray mists over the lens as she points upward along the massive brick "
            "channel. Audio: loud creaking wood, splashing water, no background music. Keep character dialogue and "
            "natural ambient sounds. Negative: walking into frame, pop-in, subtitles, captions, watermark, text on screen, "
            "logo, blurry faces, distorted hands."
        ),
        "characters": ["Mia", "Mia Outfit"]
    },
    {
        "index": 18,
        "sid": "333498aa-1a8b-44bd-be73-f5812ad58149",
        "prompt": (
            "Cinematic ultra-wide documentary shot on the high summit terrace of the Hanging Gardens of Babylon. "
            "Young female traveler Mia is ALREADY standing under a sun-drenched marble floral archway draped with "
            "blooming pink climbing roses in the left third of the frame, wearing her signature desert-sand linen "
            "tunic and ponytail, gazing out in total awe at azure mountain water cascading into carved turquoise "
            "limestone pools eighty feet in the air. Below in the background, ancient Babylonian temples stretch "
            "under radiant afternoon desert light. Pure archaeological wonder. Negative: empty terrace, modern clothes, "
            "smartphone, extra hands, distorted fingers, pop-in."
        ),
        "video_prompt": (
            "0-3s: Mia steps gently forward from under the floral archway out onto the sun-drenched marble terrace "
            "where azure water cascades into carved turquoise basins. 3-7s: She turns her camera across the blooming "
            "climbing roses, whispering in total awe \"Look at this... an entire river oasis floating eighty feet in the "
            "sky above the Mesopotamian desert.\" 7-10s: The camera tilts down toward the sparkling pools where red rose "
            "petals drift on the crystal water. Audio: gentle roaring waterfalls, light breeze, no background music. "
            "Keep character dialogue and natural ambient sounds. Negative: stepping into empty frame, subtitles, captions, "
            "watermark, text on screen, logo, blurry faces, distorted hands."
        ),
        "characters": ["Mia", "Mia Outfit"]
    },
    {
        "index": 22,
        "sid": "ecbc519b-9d85-4117-8d69-ba4960f65c51",
        "prompt": (
            "Majestic documentary wide shot from the absolute summit terrace of the Hanging Gardens of Babylon. "
            "Young traveler Mia is ALREADY leaning against the ancient limestone parapet in the right third of the "
            "frame, wearing her desert-sand tunic and golden sash with blonde hair catching amber golden-hour light. "
            "Her body is angled slightly toward the breathtaking panorama of ancient Babylon stretching below: the "
            "gleaming blue-glazed Ishtar Gate, the colossal 90-meter Etemenanki ziggurat tower, and the golden winding "
            "Euphrates river under sunset sky. Pure cinematic epic scale. Negative: empty frame, modern buildings, "
            "power lines, smartphone, extra limbs, distorted fingers."
        ),
        "video_prompt": (
            "0-3s: Sweeping cinematic handheld pan from the peak terrace showing the grand panorama of ancient Babylon "
            "bathed in amber golden-hour light, then settling on Mia turning her face toward the camera. 3-7s: Mia smiles "
            "with deep emotion, her eyes shining in the sunset \"Behold... all of Babylon from the crown of the ancient "
            "world! The blue glazed Ishtar Gate, the towering Etemenanki ziggurat, and the Euphrates glowing like gold.\" "
            "7-10s: The warm sunset breeze sweeps across the terraced palms as the golden sun dips toward the Mesopotamian "
            "horizon. Audio: warm desert wind, emotional voice, no background music. Keep character dialogue and natural "
            "ambient sounds. Negative: walking into frame, pop-in, subtitles, captions, watermark, text on screen, logo, "
            "blurry faces, distorted hands."
        ),
        "characters": ["Mia", "Mia Outfit"]
    }
]

images_dir = r"output/time_travel_vlog_ancient_babylon_570_bc/images"
art_images_dir = r"C:\Users\Administrator\.gemini\antigravity-ide\brain\e22150ce-4262-4e3c-8619-a7731a7f7c3a\images"
os.makedirs(images_dir, exist_ok=True)
os.makedirs(art_images_dir, exist_ok=True)

def step1_patch_db():
    print("=" * 60)
    print("STEP 1: Patching prompts and entities in DB for Scenes 04, 18, 22...")
    print("=" * 60)
    conn = sqlite3.connect("flow_agent.db")
    c = conn.cursor()
    for t in TARGETS:
        c.execute("""
            UPDATE scene 
            SET prompt = ?, video_prompt = ?, character_names = ?, 
                horizontal_image_status = 'PENDING', vertical_image_status = 'PENDING'
            WHERE id = ?
        """, (t["prompt"], t["video_prompt"], json.dumps(t["characters"]), t["sid"]))
        print(f"  [+] Patched Scene {t['index']:02d} ({t['sid'][:8]})")
    conn.commit()
    conn.close()

def step2_submit_requests():
    print("\n" + "=" * 60)
    print("STEP 2: Submitting REGENERATE_IMAGE batch request...")
    print("=" * 60)
    reqs = []
    for t in TARGETS:
        reqs.append({
            "type": "REGENERATE_IMAGE",
            "scene_id": t["sid"],
            "project_id": PID,
            "video_id": VID,
            "orientation": ORI
        })
    payload = {"requests": reqs}
    req = urllib.request.Request(
        "http://127.0.0.1:8100/api/requests/batch",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
    print(f"  [+] Batch submitted: {len(res)} requests queued.")
    return [r["id"] for r in res]

def step3_poll_completion(request_ids):
    print("\n" + "=" * 60)
    print("STEP 3: Polling for image generation completion...")
    print("=" * 60)
    start_time = time.time()
    while True:
        conn = sqlite3.connect("flow_agent.db")
        c = conn.cursor()
        placeholders = ",".join("?" for _ in request_ids)
        c.execute(f"SELECT id, status, output_url, media_id, error_message FROM request WHERE id IN ({placeholders})", request_ids)
        rows = c.fetchall()
        conn.close()
        
        statuses = [r[1] for r in rows]
        completed = sum(1 for st in statuses if st == "COMPLETED")
        failed = sum(1 for st in statuses if st == "FAILED")
        
        print(f"[{time.strftime('%H:%M:%S')}] Progress: {completed}/{len(request_ids)} completed, {failed} failed. Elapsed: {int(time.time() - start_time)}s")
        if completed == len(request_ids):
            print("  [+] All 3 images completed successfully!")
            return rows
        if failed > 0 and (completed + failed) == len(request_ids):
            print(f"  [!] Some requests failed: {rows}")
            return rows
        time.sleep(8)

def step4_process_and_upload(req_rows):
    print("\n" + "=" * 60)
    print("STEP 4: Downloading raw frames, de-watermarking, and re-uploading...")
    print("=" * 60)
    
    # Map request_id to target
    req_map = {r[0]: (r[2], r[3]) for r in req_rows} # req_id -> (url, media_id)
    
    conn = sqlite3.connect("flow_agent.db")
    c = conn.cursor()
    
    for t in TARGETS:
        sidx = t["index"]
        sid = t["sid"]
        
        # Get latest completed request for this scene
        c.execute("SELECT output_url, media_id FROM request WHERE scene_id=? AND type='REGENERATE_IMAGE' AND status='COMPLETED' ORDER BY created_at DESC LIMIT 1", (sid,))
        res = c.fetchone()
        if not res or not res[0]:
            print(f"  [!] Scene {sidx:02d} has no valid output_url!")
            continue
            
        raw_url, orig_mid = res
        raw_filename = f"scene_{sidx:02d}_raw.jpg"
        clean_filename = f"scene_{sidx:02d}.jpg"
        raw_path = os.path.join(images_dir, raw_filename)
        clean_path = os.path.join(images_dir, clean_filename)
        art_path = os.path.join(art_images_dir, clean_filename)
        
        print(f"\n[Scene {sidx:02d}] Downloading raw image: {raw_url[:60]}...")
        req = urllib.request.Request(raw_url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            with open(raw_path, "wb") as f:
                f.write(resp.read())
                
        print(f"  [Scene {sidx:02d}] Removing Google watermark logo...")
        remove_watermark_image(raw_path, clean_path)
        shutil.copy2(clean_path, art_path)
        
        print(f"  [Scene {sidx:02d}] Uploading clean image to Google Flow...")
        up_payload = {"file_path": clean_path, "project_id": PID, "file_name": clean_filename}
        up_req = urllib.request.Request(
            "http://127.0.0.1:8100/api/flow/upload-image",
            data=json.dumps(up_payload).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(up_req, timeout=40) as u_resp:
            u_data = json.loads(u_resp.read())
            clean_mid = u_data.get("media_id")
            
        print(f"  [Scene {sidx:02d}] Clean media_id obtained: {clean_mid}")
        
        # Update scene in DB
        c.execute("""
            UPDATE scene 
            SET horizontal_image_media_id = ?, horizontal_image_status = 'COMPLETED'
            WHERE id = ?
        """, (clean_mid, sid))
        conn.commit()
        print(f"  [Scene {sidx:02d}] Scene record updated in database.")
        
    conn.close()

if __name__ == "__main__":
    step1_patch_db()
    req_ids = step2_submit_requests()
    req_rows = step3_poll_completion(req_ids)
    step4_process_and_upload(req_rows)
    print("\n✅ All 3 target start frames successfully updated, cleaned, and uploaded!")
