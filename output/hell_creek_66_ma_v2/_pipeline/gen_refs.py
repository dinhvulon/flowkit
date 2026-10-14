"""Submit the 14 ref requests in one batch and watch them; stop on QUOTA / UNUSUAL_ACTIVITY.
Usage: python gen_refs.py [CODE ...]   (default: all 14)"""
import json, sqlite3, sys, time
from pathlib import Path
import httpx

API = "http://127.0.0.1:8100"
OUT = Path("C:/flowkit/output/hell_creek_66_ma_v2")
LOG = OUT / "ref_gen_log.json"
st = json.loads((OUT / "project_state.json").read_text(encoding="utf-8"))
pid, ids = st["project_id"], st["character_ids"]
codes = sys.argv[1:] or ["NB", "NH", "BD", "CG", "CN", "TR", "AR", "ED", "BS", "IN", "CA", "LB", "LC", "LW"]
http = httpx.Client(timeout=120)

reqs = []
for c in codes:
    if c == "NB":
        reqs.append({"type": "EDIT_CHARACTER_IMAGE", "character_id": ids[c], "project_id": pid,
                     "source_media_id": st["uploads"]["nora_body_bare"], "orientation": "HORIZONTAL"})
    else:
        reqs.append({"type": "REGENERATE_CHARACTER_IMAGE", "character_id": ids[c], "project_id": pid,
                     "orientation": "HORIZONTAL"})
r = http.post(f"{API}/api/requests/batch", json={"requests": reqs}); r.raise_for_status()
rid = {c: q["id"] for c, q in zip(codes, r.json())}
print("submitted", rid, flush=True)

log = json.loads(LOG.read_text(encoding="utf-8")) if LOG.exists() else {}
log["account"] = "new account 2026-10-14"


def flush():
    conn = sqlite3.connect("C:/flowkit/flow_agent.db")
    n = conn.execute("UPDATE request SET status='FAILED', error_message='stopped by gen_refs (quota/unusual)' "
                     "WHERE status IN ('PENDING','PROCESSING') AND project_id=?", (pid,)).rowcount
    conn.commit(); conn.close(); return n


while True:
    done, stop = 0, None
    for c, i in rid.items():
        q = http.get(f"{API}/api/requests/{i}").json()
        s, err = q.get("status"), q.get("error_message") or ""
        if s in ("COMPLETED", "FAILED"):
            done += 1
            ch = http.get(f"{API}/api/characters/{ids[c]}").json()
            log[c] = {"request_id": i, "status": s, "media_id": ch.get("media_id") if s == "COMPLETED" else None,
                      "url": ch.get("reference_image_url") if s == "COMPLETED" else None, "error": err or None}
        if any(k in err.upper() for k in ("QUOTA", "UNUSUAL_ACTIVITY")):
            stop = err
    LOG.write_text(json.dumps(log, indent=2), encoding="utf-8")
    print(time.strftime("%H:%M:%S"), f"{done}/{len(rid)}",
          {c: log.get(c, {}).get("status", "...") for c in rid}, flush=True)
    if stop:
        print("STOP:", stop, "flushed", flush(), flush=True); break
    if done == len(rid):
        break
    time.sleep(60)
print("FINISHED", flush=True)
