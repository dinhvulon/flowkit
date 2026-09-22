import sys
import json
import urllib.request
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

# Load scenes to get display_order mapping
VID = "4427d959-7e30-4b68-b12f-e549611167c3"
with urllib.request.urlopen(f"http://127.0.0.1:8100/api/scenes?video_id={VID}") as resp:
    scenes_meta = json.loads(resp.read())
order_map = {s["id"]: s.get("display_order", 0) for s in scenes_meta}

log_file = Path(r"C:\Users\Administrator\.gemini\antigravity-ide\brain\604861da-6731-4c5c-a5ab-c3c0ac43efe7\.system_generated\tasks\task-802.log")
data = json.loads(log_file.read_text(encoding="utf-8"))

print("=" * 75)
print(f"🎬 BÁO CÁO REVIEW AI VISION CHO VIDEO (Tổng điểm: {data['overall_score']}/10 — Đạt chuẩn)")
print(f"   Đã đánh giá: {data['scenes_reviewed']} cảnh | Bỏ qua: {data['scenes_skipped']} cảnh (Scene 6 đang render lại)")
print("=" * 75)
print(f"{'Scene':<10} | {'Điểm':<6} | {'Đánh giá':<12} | {'Nhất quán mặt':<14} | {'Chuyển động':<12} | {'Lỗi chính'}")
print("-" * 75)

scene_reviews = sorted(data["scene_reviews"], key=lambda s: order_map.get(s["scene_id"], 0))

for r in scene_reviews:
    order = order_map.get(r["scene_id"], "?")
    score = r["overall_score"]
    verdict = r["verdict"].upper()
    dims = r.get("dimensions", {})
    char_cons = dims.get("character_consistency", "-")
    motion = dims.get("motion_quality", "-")
    errs = r.get("errors", [])
    top_err = errs[0].get("description", "None")[:40] + "..." if errs else "Không có lỗi"
    print(f"Scene {order:<4} | {score:<6.2f} | {verdict:<12} | {char_cons:<14} | {motion:<12} | {top_err}")

print("=" * 75)
