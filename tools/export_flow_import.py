"""Export a FlowKit project as a manual-import JSON (kich-ban-vlog template).

Fallback for when Google blocks automated generation
(PUBLIC_ERROR_UNUSUAL_ACTIVITY): the project is rebuilt by hand in the import
tool from this file. Template: .agents/skills/time-travel-vlog/references/
flow-import-template.json.

R2V mapping: there are no start frames, so each video node references the
entity images it needs (image_ref parts + refImageIds) and leaves `sources`
empty. Entities with a local image become `upload` nodes; the rest become
`image` nodes whose prompt is the entity description.

Usage:
  python tools/export_flow_import.py <project_id> [--video <vid>] [--main Mia]
      [--upload "Mia=C:/path/face.jpg"]... [--refs-dir output/<slug>/refs]
      [--script output/<slug>/script.md] [--out output/<slug>]
      [--time-capsule "Atlantis, 9600 BC — ..."] [--market "YouTube, ..."]
"""
import argparse
import json
import re
import shutil
import urllib.request
from pathlib import Path

API = "http://127.0.0.1:8100"
DIALOGUE_VERBS = r"(?:says|whispers|shouts|gasps|yells|exclaims|murmurs|asks|replies)"


def get(path):
    with urllib.request.urlopen(API + path, timeout=60) as r:
        return json.loads(r.read())


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def voice_parts(desc):
    """'Achernar — soft, …' -> ('achernar', 'soft, …')."""
    desc = (desc or "").strip()
    if not desc:
        return None, ""
    first, _, rest = desc.partition(" ")
    return first.rstrip("—:,-").lower(), rest.lstrip("—:,- ").strip()


def script_dialogue(script_path):
    """clip order -> {speaker, line} from Clip JSON blocks in script.md."""
    if not script_path:
        return {}
    text = Path(script_path).read_text(encoding="utf-8")
    out = {}
    for block in re.findall(r"```json\n(\{.*?\})\n```", text, re.S):
        clip = json.loads(block)
        if "dialogue" in clip:
            idx = int(re.sub(r"\D", "", clip["clip_id"])) - 1
            out[idx] = clip["dialogue"]
    return out


def prompt_dialogue(video_prompt):
    m = re.search(rf"(?:The )?([A-Z][\w ]+?) {DIALOGUE_VERBS}[^:\n]*: ([^\n]+)", video_prompt or "")
    if not m:
        return None
    return {"speaker": m.group(1).strip(), "line": m.group(2).strip()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project_id")
    ap.add_argument("--video")
    ap.add_argument("--main", help="vlogger entity name (default: first character with a voice)")
    ap.add_argument("--upload", action="append", default=[], help='"Entity=path/to/image.jpg"')
    ap.add_argument("--refs-dir", help="dir with <entity-slug>_clean.jpg / .jpg images to use as uploads")
    ap.add_argument("--script", help="script.md with Clip JSON (exact dialogue per clip)")
    ap.add_argument("--out", default="output")
    ap.add_argument("--time-capsule")
    ap.add_argument("--market", default="YouTube, history / edutainment")
    args = ap.parse_args()

    project = get(f"/api/projects/{args.project_id}")
    entities = get(f"/api/projects/{args.project_id}/characters")
    videos = get(f"/api/videos?project_id={args.project_id}")
    video = next(v for v in videos if not args.video or v["id"] == args.video)
    scenes = sorted(get(f"/api/scenes?video_id={video['id']}"), key=lambda s: s["display_order"])
    horizontal = (video.get("orientation") or "HORIZONTAL") == "HORIZONTAL"
    video_aspect = "16:9" if horizontal else "9:16"

    slug = slugify(project["name"])
    base = Path(args.out) / "kich-ban-vlog" / slug
    (base / "base-ref").mkdir(parents=True, exist_ok=True)

    uploads = dict(u.split("=", 1) for u in args.upload)
    if args.refs_dir:
        for e in entities:
            if e["name"] in uploads:
                continue
            stem = e["name"].lower().replace(" ", "_")
            for cand in (f"{stem}_clean.jpg", f"{stem}.jpg"):
                p = Path(args.refs_dir) / cand
                if p.exists():
                    uploads[e["name"]] = str(p)
                    break

    main_ent = next((e for e in entities if e["name"] == args.main), None) or next(
        (e for e in entities if e["entity_type"] == "character" and e.get("voice_description")),
        next(e for e in entities if e["entity_type"] == "character"))
    voice_id, voice_desc = voice_parts(main_ent.get("voice_description"))

    # ── entity nodes ────────────────────────────────────────────────────
    nodes, edges, node_of = [], [], {}
    asset_type = {"character": "character", "visual_asset": "prop", "location": "location"}
    for i, e in enumerate(sorted(entities, key=lambda e: (e["name"] != main_ent["name"],
                                                          e["entity_type"], e["name"]))):
        nid = f"img-{slugify(e['name'])}"
        node_of[e["name"]] = nid
        pos = {"x": 40 + 540 * (i // 6), "y": 40 + 460 * (i % 6)}
        atype = asset_type.get(e["entity_type"], e["entity_type"])
        if e["name"] in uploads:
            src = Path(uploads[e["name"]])
            dest = base / "base-ref" / f"{slugify(e['name'])}{src.suffix.lower()}"
            shutil.copyfile(src, dest)
            nodes.append({
                "id": nid, "kind": "upload", "position": pos, "assetType": atype,
                "title": f"{'👤' if atype == 'character' else '🏛️'} Ref — {e['name']} (upload)",
                "file": f"kich-ban-vlog/{slug}/base-ref/{dest.name}",
            })
        else:
            landscape = e["entity_type"] == "location"
            framing = ("Single reference photograph of the location, wide establishing view, no people in the foreground."
                       if landscape else
                       "Single reference photograph, full subject clearly visible, centred, plain neutral background."
                       if e["entity_type"] != "character" else
                       "Single reference photograph of ONE person, front view, waist-up to full body, looking at the camera, plain light grey seamless background.")
            nodes.append({
                "id": nid, "kind": "image", "position": pos, "assetType": atype,
                "displayName": e["name"],
                "title": f"{'👤' if atype == 'character' else '🏛️'} Ref — {e['name']}",
                "promptParts": [{"kind": "text", "text":
                    f"{framing}\n{e.get('description') or e['name']}\n"
                    "Photorealistic, natural available light, real texture, documentary realism. "
                    "One single frame, no text, no labels, no watermark, crisp 4K, NOT a 3D render, NOT CGI."}],
                "refImageIds": [], "aspectRatio": "16:9" if landscape else "9:16",
                "imageCount": 1, "images": [], "selectedImageIndex": 0, "imageModelName": "NARWHAL",
            })

    # ── video nodes ─────────────────────────────────────────────────────
    exact = script_dialogue(args.script)
    main_lines = []
    video_x = 40 + 540 * ((len(entities) - 1) // 6 + 1)
    for i, s in enumerate(scenes):
        names = s.get("character_names") or []
        if isinstance(names, str):
            names = json.loads(names)
        refs = [node_of[n] for n in names if n in node_of]
        vp = s.get("video_prompt") or s.get("prompt") or ""
        parts = [{"kind": "text", "text": "[INGREDIENTS] "}]
        for n in names:
            if n in node_of:
                parts.append({"kind": "image_ref", "nodeId": node_of[n], "handle": f"{n.upper()} REFERENCE"})
                parts.append({"kind": "text", "text": f" - {n}. "})
        parts.append({"kind": "text", "text": "\n\n" + vp})
        dur = int(float(s.get("duration") or 8))
        vid = f"vid-{i + 1:03d}"
        dlg = exact.get(i) or prompt_dialogue(vp)
        speaker = (dlg or {}).get("speaker", "").replace("(off-screen)", "").strip()
        node = {
            "id": vid, "kind": "video",
            "position": {"x": video_x + 540 * (i // 6), "y": 40 + 460 * (i % 6)},
            "title": f"🎬 Clip {i + 1} — {'nói: ' + speaker if dlg else 'không thoại'} ({dur}s)",
            "promptParts": parts, "refImageIds": refs, "sources": [],
            "aspectRatio": video_aspect, "videoLength": dur, "model": f"abra_r2v_{dur}s",
        }
        if dlg:
            node["dialog"] = dlg["line"]
            if speaker == main_ent["name"]:
                node.update({"voiceId": voice_id, "voiceCharId": "char-main"})
                if dlg.get("delivery"):
                    node["voicePerformance"] = dlg["delivery"]
                main_lines.append(dlg["line"])
            else:
                node["speaker"] = speaker
        nodes.append(node)
        edges += [{"from": r, "to": vid, "type": "ref"} for r in refs]

    total = sum(int(float(s.get("duration") or 8)) for s in scenes)
    doc = {
        "version": 1,
        "name": project["name"],
        "meta": {
            "concept": project.get("description") or project.get("story") or project["name"],
            "author": "skill:fk-time-travel-vlog",
            "target_market": args.market,
            "style": "photorealistic smartphone-shot POV selfie vlog, handheld, ultra-wide 0.5x front camera, "
                     "deep focus, documentary realism",
            "time_capsule": args.time_capsule or project["name"],
            "total_duration_target": f"{total}s ({len(scenes)} clip, R2V ingredients, không start frame)",
        },
        "characters": [{
            "id": "char-main", "name": main_ent["name"], "role": "vlogger",
            "voiceId": voice_id, "voiceDesc": voice_desc, "voicePerformance": voice_desc,
            "voiceSampleLines": main_lines[:3],
        }],
        "nodes": nodes,
        "edges": edges,
    }
    out = base / f"{slug}.json"
    out.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    ups = sum(1 for n in nodes if n["kind"] == "upload")
    print(f"{out}  ({ups} upload, {len(nodes) - ups - len(scenes)} image, {len(scenes)} video, {len(edges)} edges)")


if __name__ == "__main__":
    main()
