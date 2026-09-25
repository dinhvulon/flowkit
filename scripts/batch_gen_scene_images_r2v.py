import json
import os
import shutil
import sqlite3
import sys
import time
import urllib.request
from pathlib import Path

BASE_DIR = Path(r"c:\flowkit")
OUT_DIR = BASE_DIR / "output" / "time_travel_vlog_ancient_babylon_570_bc_v2"
IMAGES_DIR = OUT_DIR / "images"
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

PROJECT_ID = "a808f4bb-ae6e-4ea8-9af8-0d79783d508f"
VIDEO_ID = "03a609d2-54d9-4fbf-95d4-eadb8ea3d9cb"
API_BASE = "http://127.0.0.1:8100"

sys.path.insert(0, str(BASE_DIR))
from agent.services.watermark import remove_watermark_image


def step1_submit_batch():
    conn = sqlite3.connect(str(BASE_DIR / "flow_agent.db"))
    rows = conn.execute(
        """
        SELECT id, display_order FROM scene
        WHERE video_id = ?
        ORDER BY display_order
    """,
        (VIDEO_ID,),
    ).fetchall()
    conn.close()

    print(f"Found {len(rows)} scenes to queue for GENERATE_IMAGE.")
    requests = []
    for sid, d_order in rows:
        requests.append(
            {
                "type": "GENERATE_IMAGE",
                "scene_id": sid,
                "project_id": PROJECT_ID,
                "video_id": VIDEO_ID,
                "orientation": "HORIZONTAL",
            }
        )

    payload = {"requests": requests}
    req = urllib.request.Request(
        f"{API_BASE}/api/requests/batch",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        print(f"Batch queued: {res}")


def step2_poll_and_process():
    processed_sids = set()
    total_scenes = 24
    start_time = time.time()

    print("\nStarting polling and rolling download & de-watermark...")
    while True:
        try:
            status_url = f"{API_BASE}/api/requests/batch-status?video_id={VIDEO_ID}&type=GENERATE_IMAGE"
            with urllib.request.urlopen(status_url, timeout=10) as resp:
                status_data = json.loads(resp.read().decode("utf-8"))

            completed = status_data.get("completed", 0)
            failed = status_data.get("failed", 0)
            pending = status_data.get("pending", 0)
            processing = status_data.get("processing", 0)
            is_done = status_data.get("done", False)

            elapsed = int(time.time() - start_time)
            print(
                f"[{time.strftime('%H:%M:%S')}] Completed: {completed}/{total_scenes}, Processing: {processing}, Pending: {pending}, Failed: {failed} (Elapsed: {elapsed}s)"
            )

            # Check DB for completed scenes not yet processed
            conn = sqlite3.connect(str(BASE_DIR / "flow_agent.db"))
            rows = conn.execute(
                """
                SELECT id, display_order, horizontal_image_url, horizontal_image_media_id
                FROM scene
                WHERE video_id = ? AND horizontal_image_status = 'COMPLETED'
                ORDER BY display_order
            """,
                (VIDEO_ID,),
            ).fetchall()
            conn.close()

            for sid, d_order, url, mid in rows:
                if sid not in processed_sids and url:
                    processed_sids.add(sid)
                    raw_path = IMAGES_DIR / f"scene_{d_order:02d}_raw.jpg"
                    clean_path = IMAGES_DIR / f"scene_{d_order:02d}.jpg"

                    print(
                        f"\n>>> Scene {d_order:02d} completed ({mid[:8]}...). Downloading..."
                    )
                    try:
                        # Download raw
                        urllib.request.urlretrieve(url, str(raw_path))

                        # Clean watermark
                        remove_watermark_image(
                            str(raw_path), output_path=str(clean_path)
                        )
                        print(
                            f"  [+] Watermark removed -> {clean_path.name}"
                        )
                    except Exception as e:
                        print(f"  [!] Error processing scene {d_order:02d}: {e}")

            if is_done and len(processed_sids) >= (total_scenes - failed):
                print(
                    f"\nAll requests completed! Successfully processed {len(processed_sids)} images."
                )
                break

            time.sleep(8)
        except Exception as exc:
            print(f"Poll loop exception: {exc}")
            time.sleep(8)


if __name__ == "__main__":
    step1_submit_batch()
    step2_poll_and_process()
