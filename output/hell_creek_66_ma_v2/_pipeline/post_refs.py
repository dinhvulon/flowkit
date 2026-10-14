"""For every COMPLETED ref in ref_gen_log.json not yet cleaned: download -> remove watermark ->
upload clean -> PATCH media_id. Then (re)build output/<slug>/review_refs.html. No generation credits."""
import html, json, shutil, subprocess, sys
from pathlib import Path
import httpx

API = "http://127.0.0.1:8100"
ROOT = Path("C:/flowkit")
OUT = ROOT / "output/hell_creek_66_ma_v2"
REFS = OUT / "refs"; REFS.mkdir(exist_ok=True)
LOG = OUT / "ref_gen_log.json"
st = json.loads((OUT / "project_state.json").read_text(encoding="utf-8"))
pid, ids = st["project_id"], st["character_ids"]
log = json.loads(LOG.read_text(encoding="utf-8"))
CLOG = OUT / "ref_clean_log.json"
clog = json.loads(CLOG.read_text(encoding="utf-8")) if CLOG.exists() else {}
rp = {e["code"]: e for e in json.loads((OUT / "ref_prompts.json").read_text(encoding="utf-8"))["reference_entities"]}
http = httpx.Client(timeout=900, follow_redirects=True)

for code, e in log.items():
    if code == "account" or e.get("status") != "COMPLETED" or code in clog:
        continue
    raw = REFS / f"{code}.jpg"
    if not raw.exists():
        ch = http.get(f"{API}/api/characters/{ids[code]}").json()
        url = ch.get("reference_image_url") or e.get("url")
        r = http.get(url); r.raise_for_status(); raw.write_bytes(r.content)
    clean = REFS / f"{code}_clean.jpg"
    if not clean.exists():
        subprocess.run([sys.executable, str(ROOT / "tools/remove_watermark_from_image.py"), str(raw)],
                       check=True, cwd=str(ROOT))
    with open(clean, "rb") as f:
        r = http.post(f"{API}/api/flow/upload-image-file", files={"file": (clean.name, f, "image/jpeg")},
                      data={"project_id": pid})
    r.raise_for_status(); mid = r.json()["media_id"]
    http.patch(f"{API}/api/characters/{ids[code]}", json={"media_id": mid}).raise_for_status()
    clog[code] = {"raw_media_id": e.get("media_id"), "clean_media_id": mid}
    CLOG.write_text(json.dumps(clog, indent=2), encoding="utf-8")
    if code == "NB":
        shutil.copy(clean, ROOT / "uploads/nora_body_cretaceous_dressed_clean.jpg")
    print(code, "clean ->", mid, flush=True)

# review page
cards = []
order = ["N", "NB", "NH", "BD", "CG", "CN", "TR", "AR", "ED", "BS", "IN", "CA", "LB", "LC", "LW"]
for code in order:
    e = log.get(code, {}); name = rp[code]["entity_name"]
    if code == "N":
        img, status = "refs/N_clean.jpg", "UPLOAD"
    else:
        f = REFS / f"{code}_clean.jpg"
        img, status = (f"refs/{f.name}" if f.exists() else ""), e.get("status", "chưa sinh")
    dna = rp[code].get("dna") or {}
    lock = "<br>".join(f"<b>{html.escape(k)}</b>: {html.escape(v)}" for k, v in dna.items())
    cards.append(f"""<div class=card><h3>{code} · {html.escape(name)} <span class=s>{html.escape(status)}</span></h3>
{f'<a href="{img}" target=_blank><img src="{img}"></a>' if img else '<div class=empty>' + html.escape(e.get('error') or 'chưa có ảnh') + '</div>'}
<div class=dna>{lock}</div></div>""")
(OUT / "review_refs.html").write_text(f"""<!doctype html><meta charset=utf-8><title>Hell Creek v2 refs</title>
<style>body{{background:#111;color:#ddd;font:14px system-ui;margin:16px}}.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(520px,1fr));gap:16px}}
.card{{background:#1b1b1b;padding:10px;border-radius:8px}}img{{width:100%;border-radius:4px}}h3{{margin:4px 0 8px}}.s{{font-size:12px;color:#9c9}}
.dna{{font-size:12px;color:#aaa;margin-top:6px}}.empty{{padding:60px;text-align:center;color:#c77;background:#222}}</style>
<h1>Hell Creek 66 Ma v2 — ảnh ref (tài khoản mới)</h1><div class=grid>{''.join(cards)}</div>""", encoding="utf-8")
print("review page ->", OUT / "review_refs.html")
