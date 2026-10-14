"""R2V videos one at a time (memory: wait for the previous video, then ~30s). Approved Start Frames are mentioned
inline as the opening frame (push_prompts.py). Chain links (P) get the last frame of the previous clip's video.
Stops on QUOTA / UNUSUAL_ACTIVITY. Raw 720p only (no upscale, no watermark removal on video — Rule 18).
Usage: python gen_videos.py A1-12a A1-12b A1-12c EST-01 ...  [--regen]"""
import json, sqlite3, subprocess, sys, time
from pathlib import Path
import httpx

API = "http://127.0.0.1:8100"
ROOT = Path("C:/flowkit")
OUT = ROOT / "output/hell_creek_66_ma_v2"
SC = OUT / "scenes"; SC.mkdir(exist_ok=True)
IMG = OUT / "images"
H = Path(__file__).parent
st = json.loads((OUT / "project_state.json").read_text(encoding="utf-8"))
pid, vid, sids = st["project_id"], st["video_id"], st["scene_ids"]
order = {c: i for i, c in enumerate(sids)}
clips = {c["clip_id"]: c for a in range(1, 6) for c in json.loads((OUT / f"prompts_act{a}.json").read_text(encoding="utf-8"))}
SFLOG, APPR, VLOG = OUT / "start_frame_log.json", OUT / "start_frame_approved.json", OUT / "video_log.json"
http = httpx.Client(timeout=900, follow_redirects=True)
args = [a for a in sys.argv[1:] if not a.startswith("--")]
vlog = json.loads(VLOG.read_text(encoding="utf-8")) if VLOG.exists() else {}


def jload(p, d):
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else d


def video_file(cid):
    return SC / f"scene_{order[cid]:03d}_{cid}_{sids[cid][:8]}.mp4"


def last_frame_as_start(cid, prev):
    """Chain link: last frame of prev's video -> watermark removal -> upload -> approved start frame of cid."""
    raw = IMG / f"{cid}.jpg"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-sseof", "-0.08", "-i", str(video_file(prev)), "-frames:v", "1",
                    "-q:v", "2", str(raw)], check=True)
    subprocess.run([sys.executable, str(ROOT / "tools/remove_watermark_from_image.py"), str(raw)], check=True,
                   cwd=str(ROOT), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    clean = IMG / f"{cid}_clean.jpg"
    with open(clean, "rb") as f:
        up = http.post(f"{API}/api/flow/upload-image-file", files={"file": (clean.name, f, "image/jpeg")}, data={"project_id": pid})
    up.raise_for_status(); mid = up.json()["media_id"]
    http.patch(f"{API}/api/scenes/{sids[cid]}", json={"horizontal_image_media_id": mid}).raise_for_status()
    sf = jload(SFLOG, {}); sf[cid] = {"status": "COMPLETED", "clean_media_id": mid, "source": f"last frame of {prev}"}
    SFLOG.write_text(json.dumps(sf, indent=2), encoding="utf-8")
    ap = set(jload(APPR, [])); ap.add(cid); APPR.write_text(json.dumps(sorted(ap), indent=2), encoding="utf-8")
    return mid


SLOTS = 3  # user 2026-10-14: three videos at a time; chain links still wait for their previous link


def inflight_request(sid):
    for q in http.get(f"{API}/api/requests", params={"video_id": vid}).json():
        if q.get("scene_id") == sid and q["type"] == "GENERATE_VIDEO_REFS" and q["status"] in ("PENDING", "PROCESSING"):
            return q["id"]
    return None


def start(cid):
    sid = sids[cid]
    rid = inflight_request(sid)
    if rid:
        print(time.strftime("%H:%M:%S"), cid, "adopted in-flight request", rid, flush=True)
        return rid
    if clips[cid]["start_frame"]["type"] == "PREV_LAST_FRAME":
        prev = clips[cid]["start_frame"]["note"].split()[-1]
        print(cid, "start frame = last frame of", prev, "->", last_frame_as_start(cid, prev), flush=True)
    subprocess.run([sys.executable, str(H / "push_prompts.py"), cid], check=True, stdout=subprocess.DEVNULL,
                   env={"PYTHONIOENCODING": "utf-8", **__import__("os").environ})
    http.patch(f"{API}/api/scenes/{sid}", json={"horizontal_video_status": "PENDING"}).raise_for_status()
    r = http.post(f"{API}/api/requests/batch", json={"requests": [{"type": "GENERATE_VIDEO_REFS", "scene_id": sid,
        "project_id": pid, "video_id": vid, "orientation": "HORIZONTAL"}]})
    r.raise_for_status(); rid = r.json()[0]["id"]
    print(time.strftime("%H:%M:%S"), cid, "submitted", flush=True)
    return rid


def ready(cid):
    sf = clips[cid]["start_frame"]
    if sf["type"] != "PREV_LAST_FRAME":
        return True
    prev = sf["note"].split()[-1]
    return video_file(prev).exists() and (vlog.get(prev) or {}).get("status") == "COMPLETED"


queue = [c for c in args if "--regen" in sys.argv or not (vlog.get(c) or {}).get("file")]
running = {}
while queue or running:
    for cid in list(queue):
        if len(running) >= SLOTS:
            break
        if ready(cid):
            queue.remove(cid); running[cid] = start(cid)
    if not running:
        print("STOP: nothing runnable (a chain link is waiting on a failed clip):", queue, flush=True); sys.exit(1)
    time.sleep(30)
    for cid, rid in list(running.items()):
        q = http.get(f"{API}/api/requests/{rid}").json()
        err = q.get("error_message") or ""
        if any(k in err.upper() for k in ("QUOTA", "UNUSUAL_ACTIVITY")):
            conn = sqlite3.connect(str(ROOT / "flow_agent.db"))
            conn.execute("UPDATE request SET status='FAILED', error_message='stopped by gen_videos' "
                         "WHERE status IN ('PENDING','PROCESSING') AND video_id=?", (vid,))
            conn.commit(); print(cid, "STOP:", err[:200], flush=True); sys.exit(1)
        if q["status"] not in ("COMPLETED", "FAILED"):
            continue
        del running[cid]
        if q["status"] == "FAILED":
            vlog[cid] = {"request_id": rid, "status": "FAILED", "error": err}
            print(cid, "FAILED:", err[:200], flush=True)
        else:
            s = http.get(f"{API}/api/scenes/{sids[cid]}").json()
            f = video_file(cid); f.write_bytes(http.get(s["horizontal_video_url"]).content)
            vlog[cid] = {"request_id": rid, "status": "COMPLETED", "media_id": s.get("horizontal_video_media_id"), "file": f.name}
            print(time.strftime("%H:%M:%S"), cid, "done ->", f.name, flush=True)
        VLOG.write_text(json.dumps(vlog, indent=2), encoding="utf-8")
print("ALL DONE", flush=True)
