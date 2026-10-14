"""Build prompts_act1..5.json + vn.json for Hell Creek 66 Ma v2 and run structural checks."""
import json, re, sys
from common import ORDER, ROWS, IDX, build, OUT
import act1, act2, act3, act4, act5
from vi_es import VI
from added_lines import ADDED

DATA = {}
for m in (act1, act2, act3, act4, act5):
    DATA.update(m.CLIPS)
for _c, (_lines, _deliv, _audio, _vi) in ADDED.items():  # user 2026-10-14: 17 formerly silent clips now talk
    DATA[_c] = dict(DATA[_c], deliv=_deliv, audio=_audio)
    DATA[_c].pop("silence", None)
    VI[_c] = _vi
missing = [c for c in ORDER if c not in DATA]
extra = [c for c in DATA if c not in ORDER]
assert not missing and not extra, (missing, extra)

MICRO = ("Even when standing still it keeps continuous living micro-motion: ribs rising and falling with each "
         "breath, eyes blinking, skin twitching at flies, small weight shifts; it never freezes like a statue.")

clips = []
for i, cid in enumerate(ORDER):
    d = DATA[cid]
    head = None
    if ROWS[cid]["sf"] == "P":
        prev = ORDER[i - 1]
        head = {"prev": prev, "opens": d.get("opens") or d["inplace"]}
        a_, b_ = DATA[prev]["cam"], d["cam"]
        assert a_.startswith(b_) or b_.startswith(a_), f"chain camera drift {prev}->{cid}"
        assert (DATA[prev].get("refs_override") or ROWS[prev]["refs"]) == (d.get("refs_override") or ROWS[cid]["refs"]), f"chain ref drift {prev}->{cid}"
    c = build(cid, d, head)
    for ch in c["characters"]:
        if ch["name"] not in ("Nora", "Nora's hands (first-person)", "the Edmontosaurus carcass"):
            ch["state"] = (ch["state"] + " " + MICRO).strip()
    clips.append(c)

# Rule 42: no 3 selfies in a row; no 2 consecutive clips with same angle + size (a 4s chain counts as one block)
warn = []
blocks = []
for c in clips:
    kind, sz = [x.strip() for x in ROWS[c["clip_id"]]["shot"].split("·")]
    if ROWS[c["clip_id"]]["sf"] == "P":
        continue
    blocks.append((c["clip_id"], kind, sz))
for a, b in zip(blocks, blocks[1:]):
    if a[1:] == b[1:]:
        warn.append(f"same angle+size consecutive: {a[0]} -> {b[0]} ({a[1]} {a[2]})")
for a, b, c3 in zip(blocks, blocks[1:], blocks[2:]):
    if a[1] == b[1] == c3[1] == "SELFIE":
        warn.append(f"3 selfies in a row: {a[0]},{b[0]},{c3[0]}")

ACT = lambda cid: ("act1" if cid.startswith(("EST-01", "A1")) else "act2" if cid.startswith(("A2", "EST-02"))
                   else "act3" if cid.startswith(("A3", "EST-03")) else "act4" if cid.startswith(("A4", "MASTER")) else "act5")
files = {}
vn = []
for c in clips:
    vi = c.pop("_vi")
    files.setdefault(ACT(c["clip_id"]), []).append(c)
    r = ROWS[c["clip_id"]]
    vn.append({"clip_id": c["clip_id"], "duration": c["duration"], "shot": r["shot"], "refs": c["refs"],
               "start_frame": c["start_frame"]["type"], "hinh": vi["hinh"], "beat": vi["beat"],
               "thoai": [{"t": d["t"], "es": d["line"], "vi": v} for d, v in zip(c["speech"].get("dialogue", []), VI.get(c["clip_id"], []))],
               "so_tu": r["words"]})
    if r["lines"] and len(VI.get(c["clip_id"], [])) != len(r["lines"]):
        warn.append(f"vi translation count mismatch {c['clip_id']}")
for k, v in files.items():
    (OUT / f"prompts_{k}.json").write_text(json.dumps(v, indent=2, ensure_ascii=False), encoding="utf-8")
(OUT / "vn.json").write_text(json.dumps(vn, indent=2, ensure_ascii=False), encoding="utf-8")
print({k: len(v) for k, v in files.items()}, "total", len(clips))
print("\n".join(warn) or "structure checks: OK")
