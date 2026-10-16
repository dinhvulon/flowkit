"""Create the FlowKit scenes (111 since A1-03 was dropped 2026-10-15) from prompts_act1..5.json (no generation).
Idempotent via project_state.scene_ids."""
import json
from pathlib import Path
import httpx

API = "http://127.0.0.1:8100"
OUT = Path("C:/flowkit/output/hell_creek_66_ma_v2")
SP = OUT / "project_state.json"
st = json.loads(SP.read_text(encoding="utf-8"))
vid = st["video_id"]
ids = st.setdefault("scene_ids", {})
http = httpx.Client(timeout=60)

clips = [c for a in range(1, 6) for c in json.loads((OUT / f"prompts_act{a}.json").read_text(encoding="utf-8"))]
assert len(clips) == 111 and "A1-03" not in {c["clip_id"] for c in clips}
existing = {s["id"] for s in http.get(f"{API}/api/scenes", params={"video_id": vid}).json()}
for order, c in enumerate(clips):
    cid = c["clip_id"]
    vp = json.dumps({k: v for k, v in c.items() if k != "start_frame"}, ensure_ascii=False, separators=(",", ":"))
    sf = c["start_frame"]
    if ids.get(cid) not in existing:
        body = {"video_id": vid, "display_order": order, "prompt": f"{cid} - {c['scene_name']}. {c['shot']}",
                "video_prompt": vp, "character_names": c["refs"], "chain_type": "ROOT"}
        if sf.get("image_prompt"):
            body["image_prompt"] = sf["image_prompt"]
        r = http.post(f"{API}/api/scenes", json=body); r.raise_for_status()
        ids[cid] = r.json()["id"]
        SP.write_text(json.dumps(st, indent=2, ensure_ascii=False), encoding="utf-8")
    narr = " ".join(d["line"] for d in c["speech"].get("dialogue", []))
    r = http.patch(f"{API}/api/scenes/{ids[cid]}", json={"duration": c["duration"], "narrator_text": narr})
    r.raise_for_status()

# verify
got = {s["id"]: s for s in http.get(f"{API}/api/scenes", params={"video_id": vid}).json()}
bad = []
for c in clips:
    s = got.get(ids[c["clip_id"]])
    if not s or float(s.get("duration") or 0) != c["duration"] or s.get("character_names") != c["refs"]:
        bad.append(c["clip_id"])
print("scenes in video:", len(got), "| mapped:", len(ids), "| mismatches:", bad or "none")
