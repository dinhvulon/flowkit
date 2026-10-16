"""Resolve {{ref:<entity>}} -> {{media:<uuid>|<uploaded file name>}} and PATCH scenes (no generation).
Usage: python push_prompts.py [CLIP_ID ...]   (default: all 112)"""
import json, re, sys
from pathlib import Path
import httpx

API = "http://127.0.0.1:8100"
OUT = Path("C:/flowkit/output/hell_creek_66_ma_v2")
st = json.loads((OUT / "project_state.json").read_text(encoding="utf-8"))
http = httpx.Client(timeout=60)
CODE = {"Nora": "N", "Nora Body": "NB", "Nora Hand": "NH", "Bò Đực": "BD", "Con Cái Già": "CG", "Con Non": "CN",
        "T. rex": "TR", "Acheroraptor": "AR", "Edmontosaurus": "ED", "Borealosuchus": "BS", "Infernodrakon": "IN",
        "Edmontosaurus Carcass": "CA", "Hell Creek Bank": "LB", "Hell Creek Game Corridor": "LC", "Hell Creek Waterhole": "LW",
        "Turtle Shell Flask": "TF"}
chars = {c["name"]: c for c in http.get(f"{API}/api/projects/{st['project_id']}/characters").json()}


def fname(name):  # the file name each ref was uploaded with
    return "nora_main_clean.jpg" if name == "Nora" else f"{CODE[name]}_clean.jpg"


def resolve(text):
    def sub(m):
        n = m.group(1).strip()
        return "{{media:%s|%s}}" % (chars[n]["media_id"], fname(n))
    return re.sub(r"\{\{ref:([^}]+)\}\}", sub, text)


# Approved Start Frames (user review gate) become the opening shot of the R2V video, mentioned inline (Rule 64).
SFLOG = OUT / "start_frame_log.json"
sflog = json.loads(SFLOG.read_text(encoding="utf-8")) if SFLOG.exists() else {}
APPROVED_P = OUT / "start_frame_approved.json"
approved = set(json.loads(APPROVED_P.read_text(encoding="utf-8"))) if APPROVED_P.exists() else set()


def opening(cid):
    e = sflog.get(cid) or {}
    if cid in approved and e.get("clean_media_id"):
        return ("OPENING FRAME LOCK: the video opens exactly on {{media:%s|%s_clean.jpg}} (same place, same light, same outfit, "
                "same positions) and moves on from there." % (e["clean_media_id"], cid))
    return None


want = set(sys.argv[1:])
n = 0
for a in range(1, 6):
    for c in json.loads((OUT / f"prompts_act{a}.json").read_text(encoding="utf-8")):
        if want and c["clip_id"] not in want:
            continue
        vp = {k: v for k, v in c.items() if k != "start_frame"}
        op = opening(c["clip_id"])
        if op:
            vp = {"opening_frame": op, **vp}
        body = {"video_prompt": resolve(json.dumps(vp, ensure_ascii=False, separators=(",", ":")))}
        body["narrator_text"] = " ".join(d["line"] for d in c["speech"].get("dialogue", []))
        body["duration"] = c["duration"]
        body["character_names"] = c["refs"]
        if c["start_frame"].get("image_prompt"):
            body["image_prompt"] = resolve(c["start_frame"]["image_prompt"])
        http.patch(f"{API}/api/scenes/{st['scene_ids'][c['clip_id']]}", json=body).raise_for_status()
        n += 1
        if want:
            print(c["clip_id"], body.get("image_prompt", "")[:700])
print("patched", n)
