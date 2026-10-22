"""Cut one panel out of a 2x2 storyboard sheet and scale it to a 16:9 opening frame.

Usage:
    python skills/fk-storyboard/scripts/crop_panel.py <sheet.jpg> --panel 1 --out <p1.jpg>

Panels are numbered in reading order: 1 top-left, 2 top-right, 3 bottom-left, 4 bottom-right.
The black gutters are found by looking for the darkest thin band near the middle of the
sheet; if none is found the sheet is split exactly in half.
"""
import argparse
from pathlib import Path

from PIL import Image


def _gutter(profile, size):
    """Return (start, end) of the darkest band within the middle 20% of one axis."""
    lo, hi = int(size * 0.4), int(size * 0.6)
    window = profile[lo:hi]
    if not window:
        return size // 2, size // 2
    darkest = min(window)
    if darkest > 40:  # no real gutter: split in half
        return size // 2, size // 2
    idx = [lo + i for i, v in enumerate(window) if v <= darkest + 15]
    return min(idx), max(idx) + 1


def crop_panel(sheet: Path, panel: int, out: Path, width: int, height: int):
    im = Image.open(sheet).convert("RGB")
    w, h = im.size
    gray = im.convert("L")
    px = gray.load()
    cols = [sum(px[x, y] for y in range(0, h, 4)) / len(range(0, h, 4)) for x in range(w)]
    rows = [sum(px[x, y] for x in range(0, w, 4)) / len(range(0, w, 4)) for y in range(h)]
    cx0, cx1 = _gutter(cols, w)
    ry0, ry1 = _gutter(rows, h)
    boxes = {1: (0, 0, cx0, ry0), 2: (cx1, 0, w, ry0), 3: (0, ry1, cx0, h), 4: (cx1, ry1, w, h)}
    box = boxes[panel]
    # trim a few pixels so no gutter edge survives the crop
    box = (box[0] + 2, box[1] + 2, box[2] - 2, box[3] - 2)
    im.crop(box).resize((width, height), Image.LANCZOS).save(out, quality=95)
    print(f"panel {panel}: box {box} -> {out} ({width}x{height})")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("sheet", type=Path)
    ap.add_argument("--panel", type=int, default=1, choices=[1, 2, 3, 4])
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--size", default="1376x768", help="output WxH, default 1376x768 (Flow 16:9)")
    a = ap.parse_args()
    W, H = (int(v) for v in a.size.lower().split("x"))
    crop_panel(a.sheet, a.panel, a.out, W, H)
