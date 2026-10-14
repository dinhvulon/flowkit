"""Start Frames in waves of 3 (user 2026-10-14): submit 3, wait until all 3 finish, post-process, next 3.
Resumable: clips already cleaned in start_frame_log.json are skipped. Stops on QUOTA / UNUSUAL_ACTIVITY.
Frames with Nora's face use image-only refs [Nora, Nora Body, location] (restored after)."""
import html, json, sqlite3, subprocess, sys, time
from pathlib import Path
import httpx

API = "http://127.0.0.1:8100"
ROOT = Path("C:/flowkit")
OUT = ROOT / "output/hell_creek_66_ma_v2"
IMG = OUT / "images"; IMG.mkdir(exist_ok=True)
LOG = OUT / "start_frame_log.json"
WAVE = 3
st = json.loads((OUT / "project_state.json").read_text(encoding="utf-8"))
pid, vid, sids = st["project_id"], st["video_id"], st["scene_ids"]
clips = {c["clip_id"]: c for a in range(1, 6) for c in json.loads((OUT / f"prompts_act{a}.json").read_text(encoding="utf-8"))}
log = json.loads(LOG.read_text(encoding="utf-8")) if LOG.exists() else {}
http = httpx.Client(timeout=900, follow_redirects=True)


def save():
    LOG.write_text(json.dumps(log, indent=2), encoding="utf-8")


def is_face(c):
    return bool(c["characters"]) and c["characters"][0]["name"] == "Nora"


def post(cid):
    sc = http.get(f"{API}/api/scenes/{sids[cid]}").json()
    raw = IMG / f"{cid}.jpg"
    raw.write_bytes(http.get(sc["horizontal_image_url"]).content)
    subprocess.run([sys.executable, str(ROOT / "tools/remove_watermark_from_image.py"), str(raw)], check=True,
                   cwd=str(ROOT), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    clean = IMG / f"{cid}_clean.jpg"
    with open(clean, "rb") as f:
        up = http.post(f"{API}/api/flow/upload-image-file", files={"file": (clean.name, f, "image/jpeg")}, data={"project_id": pid})
    up.raise_for_status(); mid = up.json()["media_id"]
    http.patch(f"{API}/api/scenes/{sids[cid]}", json={"horizontal_image_media_id": mid}).raise_for_status()
    log[cid].update(raw_media_id=sc.get("horizontal_image_media_id"), clean_media_id=mid); save()


def page():
    cards = []
    for cid, c in clips.items():
        e = log.get(cid)
        if not e:
            continue
        f = IMG / f"{cid}_clean.jpg"
        body = (f'<a href="images/{f.name}" target=_blank><img src="images/{f.name}"></a>' if f.exists()
                else f'<div class=empty>{html.escape(e.get("error") or e["status"])}</div>')
        cards.append(f"<div class=card><h3>{cid} · {html.escape(c['scene_name'])} <span>{c['duration']}s · "
                     f"{'Nora' if is_face(c) else 'no face'}</span></h3>{body}<p>{html.escape(c['shot'])}</p></div>")
    done = sum(1 for e in log.values() if e.get("clean_media_id"))
    (OUT / "review_images.html").write_text(
        f"""<!doctype html><meta charset=utf-8><title>Hell Creek v2 start frames</title>
<style>body{{background:#111;color:#ddd;font:14px system-ui;margin:16px}}.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(480px,1fr));gap:16px}}
.card{{background:#1b1b1b;padding:10px;border-radius:8px}}img{{width:100%;border-radius:4px}}h3{{margin:4px 0 8px}}h3 span{{font-size:12px;color:#9c9}}p{{font-size:12px;color:#aaa}}
.empty{{padding:60px;text-align:center;color:#c77;background:#222}}</style><h1>Start Frames — {done}/{len(todo_all)}</h1><div class=grid>{''.join(cards)}</div>""",
        encoding="utf-8")


# optional act filter: python gen_sf_waves.py act1   (act1 = EST-01 + A1-*)
ACTS = {"act1": ("EST-01", "A1-"), "act2": ("A2-", "EST-02"), "act3": ("A3-", "EST-03"), "act4": ("A4-", "MASTER"), "act5": ("A5-",)}
sel = [a for a in sys.argv[1:] if a in ACTS]
todo_all = [c for c, v in clips.items() if v["start_frame"]["type"] == "GENERATE_IMAGE"
            and (not sel or any(c.startswith(ACTS[a]) for a in sel))]
# --regen=EST-01,A1-01 : force a fresh image for these clips
REGEN = set(sum([a.split("=", 1)[1].split(",") for a in sys.argv[1:] if a.startswith("--regen=")], []))
for c in REGEN:
    log.pop(c, None)
save()
todo = [c for c in todo_all if not (log.get(c) or {}).get("clean_media_id")]
print(f"{len(todo_all)} frames total, {len(todo)} to do, waves of {WAVE}", flush=True)

for w in range(0, len(todo), WAVE):
    wave = todo[w:w + WAVE]
    restore = {}
    for cid in wave:
        img_refs = clips[cid]["start_frame"].get("image_refs", clips[cid]["refs"])
        if img_refs != clips[cid]["refs"]:
            restore[cid] = clips[cid]["refs"]
            http.patch(f"{API}/api/scenes/{sids[cid]}", json={"character_names": img_refs}).raise_for_status()
    r = http.post(f"{API}/api/requests/batch", json={"requests": [
        {"type": "REGENERATE_IMAGE" if c in REGEN else "GENERATE_IMAGE", "scene_id": sids[c], "project_id": pid, "video_id": vid, "orientation": "HORIZONTAL"} for c in wave]})
    r.raise_for_status()
    rid = {c: q["id"] for c, q in zip(wave, r.json())}
    print(time.strftime("%H:%M:%S"), f"wave {w // WAVE + 1}: {wave}", flush=True)
    stop = None
    while True:
        done = 0
        for cid, i in rid.items():
            q = http.get(f"{API}/api/requests/{i}").json()
            err = q.get("error_message") or ""
            if q["status"] in ("COMPLETED", "FAILED"):
                done += 1
                if cid not in log or log[cid].get("request_id") != i:
                    log[cid] = {"request_id": i, "status": q["status"], "error": err or None}; save()
            if any(k in err.upper() for k in ("QUOTA", "UNUSUAL_ACTIVITY")):
                stop = err
        if stop or done == len(rid):
            break
        time.sleep(20)
    for cid, refs in restore.items():
        http.patch(f"{API}/api/scenes/{sids[cid]}", json={"character_names": refs}).raise_for_status()
    for cid in wave:
        if log.get(cid, {}).get("status") == "COMPLETED" and not log[cid].get("clean_media_id"):
            try:
                post(cid); print("  ", cid, "clean ->", log[cid]["clean_media_id"], flush=True)
            except Exception as ex:
                print("  ", cid, "post-process error:", ex, flush=True)
        elif log.get(cid, {}).get("status") == "FAILED":
            print("  ", cid, "FAILED:", (log[cid].get("error") or "")[:200], flush=True)
    page()
    if stop:
        conn = sqlite3.connect(str(ROOT / "flow_agent.db"))
        n = conn.execute("UPDATE request SET status='FAILED', error_message='stopped by gen_sf_waves' "
                         "WHERE status IN ('PENDING','PROCESSING') AND video_id=?", (vid,)).rowcount
        conn.commit(); print("STOP:", stop[:200], "| flushed", n, flush=True); sys.exit(1)
print("ALL DONE", flush=True)
