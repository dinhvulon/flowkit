#!/usr/bin/env python3
"""Paper edit for FlowKit scripts — timecode, runtime and retention checks before any Flow credit is spent.

Reads one or more of (concatenated in the order given, e.g. episodes of one film):
  * a storyboard markdown file (`output/<slug>/script.md`) with tables whose header has `Clip` and `Dur`
    (fk-film storyboard format: Clip | Dur | Shot | Ref | SF | ... | Hình | Thoại | Từ | Việc | Beat | Dựng)
  * a screenplay JSON from /fk-scriptwriter (`{"scenes": [...]}`, Section O.1)

Word-count rules:
  * markdown storyboard -> CLAUDE.md Rule 49 table (0)
  * screenplay JSON     -> /fk-scriptwriter Section J for 8s narrator scenes (vi 18-22, en 20-24,
                           scenes with dialogue 12-16); Rule 49 for other durations

Writes a markdown report and prints a short summary.
Default report path: `paper_edit.md` next to a markdown input, `<stem>_paper_edit.md` next to a JSON input,
`paper_edit_combined.md` next to the first file when several inputs are given.
Exit code: 0 = no errors, 1 = errors found (warnings never fail).

Usage:
  python tools/paper_edit.py output/<slug>/script.md
  python tools/paper_edit.py .omc/research/<slug>_ep01_script.json --lang en
  python tools/paper_edit.py ep01.json ep02.json ep03.json --out output/<slug>/paper_edit.md
"""

import argparse
import json
import re
import sys
from pathlib import Path

# CLAUDE.md Rule 49 table (0): duration -> (usable seconds after trim, allowed word ranges)
RULE49 = {
    4: (3.5, [(0, 0), (6, 8)]),
    6: (5.0, [(12, 15)]),
    8: (7.0, [(18, 22)]),
    10: (9.0, [(24, 28)]),
}
# /fk-scriptwriter Section J (7.0s window, 8s clips only)
SECTION_J = {"vi": (18, 22), "en": (20, 24), "dialogue": (12, 16)}
DEFAULT_SCREENPLAY_DURATION = 8
HOOK_RE = re.compile(r"(?<!không phải )(?<!not a )\b(re-?hook|rh|hook)\b", re.IGNORECASE)
SILENT_RE = re.compile(r"sonic|0 từ|im lặng|silen|không thoại|no dialogue", re.IGNORECASE)
CHAIN_RE = re.compile(r"^(.*\d)([a-z])$")
SECONDS_RE = re.compile(r"^~?(\d+(?:\.\d+)?)\s*s$")
PACKAGE_RE = re.compile(r"^\s*-?\s*\*\*Package:?\*\*:?\s*(.+)$", re.IGNORECASE)


def clean(cell):
    return re.sub(r"\*+", "", "" if cell is None else str(cell)).strip()


def count_words(text):
    text = re.sub(r"\(.*?\)", " ", text or "")          # drop "(0 từ, Sonic Isolation)" style notes
    text = text.replace("/", " ").replace("—", " ")
    return len([w for w in text.split() if re.search(r"\w", w)])


def fmt_tc(seconds):
    m, s = divmod(seconds, 60)
    return f"{int(m)}:{s:04.1f}"


def find_col(header, *names):
    for i, h in enumerate(header):
        if any(n in h for n in names):
            return i
    return None


def split_row(line):
    line = line.replace("\\|", "\u0000")                  # escaped pipes stay inside the cell
    return [c.strip().replace("\u0000", "|") for c in line.strip().strip("|").split("|")]


def parse_markdown(path, notes):
    clips, section, package = [], "", None
    header, cols = None, {}
    for n, raw in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
        line = raw.strip()
        pm = PACKAGE_RE.match(line)
        if pm and package is None:
            package = pm.group(1).strip()
        if line.startswith("#"):
            section = line.lstrip("#").strip()
            header = None
            continue
        if not line.startswith("|"):
            header = None
            continue
        cells = split_row(line)
        if header is None:
            low = [clean(c).lower() for c in cells]
            ci = next((i for i, h in enumerate(low) if h.startswith("clip")), None)
            di = next((i for i, h in enumerate(low) if h.startswith("dur")), None)
            if ci is not None and di is not None:
                header = low
                cols = {
                    "clip": ci, "dur": di,
                    "shot": find_col(low, "shot"),
                    "sf": next((i for i, h in enumerate(low) if h == "sf"), None),
                    "visual": find_col(low, "hình", "visual"),
                    "audio": find_col(low, "thoại", "dialogue", "narrator"),
                    "words": next((i for i, h in enumerate(low) if h in ("từ", "words", "số từ")), None),
                    "job": find_col(low, "việc"),
                    "beat": find_col(low, "beat"),
                    "edit": find_col(low, "dựng"),
                }
                if cols["audio"] is None:
                    notes["errors"].append(f"{path.name}:{n}: bảng clip không có cột thoại (Thoại/Dialogue/Narrator) — không kiểm được số từ.")
            continue
        if set("".join(cells)) <= set("-: "):
            continue  # separator row
        if len(cells) != len(header):
            notes["warns"].append(f"{path.name}:{n}: dòng có {len(cells)} ô, header có {len(header)} ô — cột có thể bị lệch.")
        get = lambda k: clean(cells[cols[k]]) if cols.get(k) is not None and cols[k] < len(cells) else ""
        clips.append({
            "id": get("clip"), "section": section, "dur_raw": get("dur"), "shot": get("shot"), "sf": get("sf"),
            "visual": get("visual"), "audio": get("audio"), "words_raw": get("words"),
            "job": get("job"), "beat": get("beat"), "edit": get("edit"),
            "has_audio_col": cols["audio"] is not None, "mode": "rule49",
        })
    return clips, package


def parse_screenplay(path, lang):
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    lang = (lang or data.get("language") or data.get("lang") or data.get("dialogue_language") or "vi").lower()[:2]
    clips = []
    for sc in data.get("scenes") or []:
        sc = sc or {}
        clips.append({
            "id": clean(sc.get("display_order", len(clips))), "section": clean(data.get("title")),
            "dur_raw": clean(sc.get("duration") or DEFAULT_SCREENPLAY_DURATION),
            "shot": clean(sc.get("framing")), "sf": "", "visual": clean(sc.get("prompt")),
            "audio": clean(sc.get("narrator_text")), "words_raw": "", "job": clean(sc.get("scene_type")),
            "beat": clean(sc.get("beat")), "edit": "", "has_audio_col": True,
            "mode": "section_j", "lang": lang, "has_dialogue": bool(sc.get("has_dialogue")),
        })
    return clips, data.get("package")


def allowed_ranges(c):
    if c["mode"] == "section_j" and c["dur"] == 8:
        if c.get("has_dialogue"):
            return [(0, 0), SECTION_J["dialogue"]], "Section J (cảnh có thoại)"
        return [(0, 0), SECTION_J.get(c.get("lang"), SECTION_J["vi"])], f"Section J ({c.get('lang')})"
    return RULE49[c["dur"]][1], "Rule 49"


def fmt_ranges(ranges):
    return " hoặc ".join(f"{lo}–{hi}" if lo != hi else str(lo) for lo, hi in ranges)


def analyse(clips, rehook_max, promise_window, notes):
    errors, warns, infos = notes["errors"], notes["warns"], []
    t = 0.0
    gen_by_dur, sf_count = {}, {}
    for c in clips:
        m = re.search(r"(\d+)", c["dur_raw"])
        c["dur"] = int(m.group(1)) if m else None
        em = SECONDS_RE.match(c["edit"])
        if em:
            c["usable"] = float(em.group(1))
        elif c["dur"] in RULE49:
            c["usable"] = RULE49[c["dur"]][0]
            if c["edit"]:
                infos.append(f"`{c['id']}`: cột Dựng `{c['edit'][:40]}` không phải số giây — lấy {c['usable']}s theo bảng Rule 49.")
        else:
            c["usable"] = 0.0
            warns.append(f"`{c['id']}`: không đọc được thời lượng (Dur=`{c['dur_raw']}`, Dựng=`{c['edit'][:40]}`) — tính 0s.")
        if c["dur"] is not None:
            gen_by_dur[c["dur"]] = gen_by_dur.get(c["dur"], 0) + 1
        if c["sf"][:1].isalpha():
            key = c["sf"][:1].upper()
            sf_count[key] = sf_count.get(key, 0) + 1
        c["start"] = t
        t += c["usable"]

        actual = count_words(c["audio"])
        wm = re.search(r"\d+", c["words_raw"])
        declared = int(wm.group(0)) if wm else None
        c["words"] = actual if c["has_audio_col"] else (declared or 0)
        if declared is not None and c["has_audio_col"] and abs(declared - actual) > 1:
            warns.append(f"`{c['id']}`: cột Từ ghi {declared} nhưng thoại đếm được {actual} từ.")
        if c["dur"] in RULE49 and c["has_audio_col"]:
            ranges, source = allowed_ranges(c)
            silent_note = bool(SILENT_RE.search(" ".join([c["audio"], c["beat"], c["visual"]])))
            for label, value in (("thoại đếm được", actual), ("cột Từ", declared)):
                if value is None:
                    continue
                if value == 0 and c["dur"] != 4 and c["mode"] == "rule49":
                    if not silent_note:
                        warns.append(f"`{c['id']}` ({c['dur']}s): 0 từ mà không ghi Sonic Isolation / im lặng — Rule 49 chỉ cho 0 từ ở clip 4s hoặc cảnh Sonic Isolation.")
                    break
                if not any(lo <= value <= hi for lo, hi in ranges + ([(0, 0)] if c["mode"] == "rule49" else [])):
                    errors.append(f"`{c['id']}` ({c['dur']}s): {label} {value} từ — {source} cho phép {fmt_ranges(ranges)}.")
                    break
        elif c["dur"] is not None and c["dur"] not in RULE49:
            errors.append(f"`{c['id']}`: duration {c['dur']}s không có trong bảng Rule 49 (4/6/8/10).")
        c["hook"] = bool(HOOK_RE.search(" ".join([c["beat"], c["job"], c["edit"]])))

    total = t

    # Blocks (Rule 42): a 4s chain a/b/c, or a clip whose Start Frame is the previous clip's
    # last frame (SF = P, Rule 65), continues the previous block.
    blocks = []
    for c in clips:
        cm = CHAIN_RE.match(c["id"])
        base = cm.group(1) if cm else c["id"]
        continues = blocks and ((cm and blocks[-1]["base"] == base) or c["sf"][:1].upper() == "P")
        if continues:
            blocks[-1]["clips"].append(c)
        else:
            blocks.append({"base": base, "clips": [c]})
    for a, b in zip(blocks, blocks[1:]):
        last, first = a["clips"][-1], b["clips"][0]
        if last["shot"] and last["shot"].lower() == first["shot"].lower():
            warns.append(f"`{last['id']}` → `{first['id']}`: hai khối liền nhau cùng Shot `{last['shot']}` (Rule 42 / Quality Gate #9).")
    run = 0
    for b in blocks:
        run = run + 1 if "selfie" in b["clips"][0]["shot"].lower() else 0
        if run == 3:
            warns.append(f"`{b['clips'][0]['id']}`: khối selfie thứ 3 liên tiếp (Rule 42).")

    # Re-hook cadence.
    hooks = [c for c in clips if c["hook"]]
    marks = [0.0] + [c["start"] for c in hooks] + [total]
    gaps = [(a, b) for a, b in zip(marks, marks[1:]) if b - a > rehook_max]
    step = (min(60.0, rehook_max) + rehook_max) / 2  # middle of the 60–max window
    suggestions = []
    for a, b in gaps:
        warns.append(f"Không có móc giữ chân trong {fmt_tc(a)}–{fmt_tc(b)} ({b - a:.0f}s > {rehook_max:.0f}s).")
        target = a + step
        while target < b - 30:
            cand = [c["id"] for c in clips if target - 15 <= c["start"] <= target + 15]
            suggestions.append((target, cand))
            target += step
    if not hooks:
        infos.append("Không clip nào có nhãn `Hook`/`RH`/`Re-hook` ở cột Beat/Việc/Dựng — chưa có bản đồ móc giữ chân.")

    promise = [c for c in clips if c["start"] < promise_window]
    return {
        "total": total, "gen_by_dur": gen_by_dur, "sf_count": sf_count, "errors": errors, "warns": warns,
        "infos": infos, "hooks": hooks, "promise": promise, "suggestions": suggestions,
    }


def report(names, clips, res, package, promise_window):
    gen_total = sum(res["gen_by_dur"].values())
    out = [f"# Paper edit — {', '.join(f'`{n}`' for n in names)}", ""]
    out.append(f"- **Thời lượng dùng được:** {fmt_tc(res['total'])} ({res['total']:.1f}s, {len(clips)} dòng clip)")
    mix = " · ".join(f"{n}×{d}s" for d, n in sorted(res["gen_by_dur"].items()))
    out.append(f"- **Số lần sinh video (ước tính, chưa tính regen):** {gen_total} = {mix or '—'}")
    if res["sf_count"]:
        sf = res["sf_count"]
        imgs = sf.get("G", 0) + sf.get("E", 0)
        detail = " · ".join(f"{k} {v}" for k, v in sorted(sf.items()))
        out.append(f"- **Start Frame cần sinh ảnh (G + E):** {imgs} ({detail}; P = khung cuối clip trước, không sinh). Chưa tính ảnh ref.")
    else:
        out.append("- **Start Frame / ảnh ref:** không có cột SF — agent PHẢI tự cộng số ảnh cần sinh khi hỏi user (Rule 29).")
    out.append(f"- **Lỗi:** {len(res['errors'])} · **Cảnh báo:** {len(res['warns'])}")
    out.append(f"- **Gói (package):** {json.dumps(package, ensure_ascii=False) if isinstance(package, dict) else (package or 'UNKNOWN — chưa có gói')}")
    out.append("")

    sections = {}
    for c in clips:
        s = sections.setdefault(c["section"], [0, 0.0, c["start"]])
        s[0] += 1
        s[1] += c["usable"]
    out += ["## Thời lượng theo phần", "", "| Phần | Clip | Dựng | Bắt đầu |", "|---|---|---|---|"]
    for name, (n, sec, start) in sections.items():
        out.append(f"| {name or '—'} | {n} | {sec:.1f}s | {fmt_tc(start)} |")
    out.append("")

    out += [f"## Lời hứa trong {promise_window:.0f}s đầu (đối chiếu với gói)", "",
            "| TC | Clip | Hình | Thoại |", "|---|---|---|---|"]
    for c in res["promise"]:
        out.append(f"| {fmt_tc(c['start'])} | {c['id']} | {c['visual'][:140]} | {c['audio'][:140]} |")
    out.append("")

    out += ["## Bản đồ móc giữ chân", ""]
    if res["hooks"]:
        out += ["| TC | Clip | Beat |", "|---|---|---|"]
        for c in res["hooks"]:
            out.append(f"| {fmt_tc(c['start'])} | {c['id']} | {c['beat'][:120]} |")
    else:
        out.append("_Chưa có nhãn móc giữ chân._")
    out.append("")
    if res["suggestions"]:
        out += ["**Vị trí đề xuất đặt `RH`** (±15s quanh mốc; agent chọn clip có tin mới / nguy hiểm mới / câu hỏi mới):", "",
                "| Mốc | Clip ứng viên |", "|---|---|"]
        for target, cand in res["suggestions"]:
            out.append(f"| {fmt_tc(target)} | {', '.join(cand) or '— (không clip nào bắt đầu trong cửa sổ)'} |")
        out.append("")

    for title, items in (("Lỗi (phải sửa trước khi sinh)", res["errors"]),
                         ("Cảnh báo", res["warns"]), ("Ghi chú", res["infos"])):
        out += [f"## {title}", ""] + ([f"- {x}" for x in items] or ["- Không có."]) + [""]

    out += ["## Dòng thời gian AV", "",
            "| TC | Clip | Dur | Dựng | Shot | Hình | Thoại | Từ | Beat |",
            "|---|---|---|---|---|---|---|---|---|"]
    for c in clips:
        flag = " 🔁" if c["hook"] else ""
        out.append(
            f"| {fmt_tc(c['start'])} | {c['id']}{flag} | {c['dur_raw']} | {c['usable']:.1f}s | {c['shot']} | "
            f"{c['visual'][:110]} | {c['audio'][:110]} | {c['words']} | {c['beat'][:80]} |"
        )
    out.append("")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("files", type=Path, nargs="+")
    ap.add_argument("--out", type=Path)
    ap.add_argument("--lang", choices=["vi", "en"], help="ngôn ngữ narrator cho screenplay JSON (mặc định: field language trong JSON, hoặc vi)")
    ap.add_argument("--rehook-max", type=float, default=90.0, help="khoảng cách tối đa giữa hai móc giữ chân (giây)")
    ap.add_argument("--promise-window", type=float, default=30.0, help="cửa sổ trả lời hứa của gói (giây)")
    args = ap.parse_args()

    notes = {"errors": [], "warns": []}
    clips, package = [], None
    for f in args.files:
        if f.suffix.lower() == ".json":
            part, pkg = parse_screenplay(f, args.lang)
        else:
            part, pkg = parse_markdown(f, notes)
        clips += part
        package = package or pkg
    if not clips:
        sys.exit(f"Không tìm thấy bảng clip (header có 'Clip' và 'Dur') hoặc scenes trong {', '.join(map(str, args.files))}")

    res = analyse(clips, args.rehook_max, args.promise_window, notes)
    first = args.files[0]
    if args.out:
        out = args.out
    elif len(args.files) > 1:
        out = first.with_name("paper_edit_combined.md")
    elif first.suffix.lower() == ".json":
        out = first.with_name(f"{first.stem}_paper_edit.md")
    else:
        out = first.with_name("paper_edit.md")
    out.write_text(report([f.name for f in args.files], clips, res, package, args.promise_window), encoding="utf-8")

    print(f"Runtime {fmt_tc(res['total'])} · {sum(res['gen_by_dur'].values())} lần sinh video · "
          f"{len(res['errors'])} lỗi · {len(res['warns'])} cảnh báo → {out}")
    sys.exit(1 if res["errors"] else 0)


if __name__ == "__main__":
    main()
