import json
import os
import sqlite3
import sys

sys.stdout.reconfigure(encoding="utf-8")

ART_DIR = r"C:\Users\Administrator\.gemini\antigravity-ide\brain\e22150ce-4262-4e3c-8619-a7731a7f7c3a"
TARGET_MD = os.path.join(ART_DIR, "scene_images_review.md")

conn = sqlite3.connect("flow_agent.db")
c = conn.cursor()
c.execute("""
    SELECT display_order, id, horizontal_image_media_id, prompt, video_prompt, narrator_text, chain_type, character_names
    FROM scene
    WHERE video_id = '71909a60-29f7-460e-807c-ed48b8a12ad1'
    ORDER BY display_order ASC
""")
rows = c.fetchall()

beats = [
    ("Beat 1", "The Shock Arrival (Cú ngã xuyên không đến Cổng Ishtar)", "Act 1: Arrival & Orientation"),
    ("Beat 2", "Orientation & Disbelief (Chạm vào gạch men ngọc lưu ly xanh biếc)", "Act 1: Arrival & Orientation"),
    ("Beat 3", "First Contact (Né tránh xe thồ lương thực & đoàn lính Babylon)", "Act 1: Arrival & Orientation"),
    ("Beat 4", "Grand Reveal 1 (Tầm nhìn bao quát Vườn Treo vươn lên mây trời)", "Act 2: The Approach"),
    ("Beat 5", "Tasting Ancient Babylon (Thử quả chà là tươi và bánh mật ong)", "Act 2: The Approach"),
    ("Beat 6", "Sensory Immersion (Hương nhựa thông tuyết tùng & hương trầm)", "Act 2: The Approach"),
    ("Beat 7", "The Crowded Market (Len lỏi qua khu chợ ồn ào)", "Act 2: The Approach"),
    ("Beat 8", "Table Prop-up Dining (Gác máy ăn bánh dẹt nướng lò đất)", "Act 3: Deep Culture Dive"),
    ("Beat 9", "Curiosity Detour (Chạm trán người thợ khắc chữ hình nêm)", "Act 3: Deep Culture Dive"),
    ("Beat 10", "Ancient Tech (Đồng hồ nước Klepsydra nhỏ giọt)", "Act 3: Deep Culture Dive"),
    ("Beat 11", "Ascending the Base (Bước lên chân tháp đá Vườn Treo)", "Act 4: Entering the Wonders"),
    ("Beat 12", "Archimedes Screw (Bộ máy trục xoắn guồng nước sông Euphrates)", "Act 4: Entering the Wonders"),
    ("Beat 13", "The Shaded Archways (Lối đi vòm gạch mát lạnh rủ dây leo)", "Act 4: Entering the Wonders"),
    ("Beat 14", "Grand Reveal 2 (Tầng thượng uy nghi của Hoàng hậu Amytis)", "Act 4: Entering the Wonders"),
    ("Beat 15", "Suspense / Tension (Vệ binh hoàng gia tuần tra - Mia nấp)", "Act 5: Conflict & Discovery"),
    ("Beat 16", "The Escape (Luồn qua cửa hẹp rực rỡ hoa dạ yến thảo)", "Act 5: Conflict & Discovery"),
    ("Beat 17", "Safe Sanctuary (Góc vườn bí mật ngập tràn hoa hồng Media)", "Act 5: Conflict & Discovery"),
    ("Beat 18", "The Hydraulic Wonder (Cận cảnh hệ thống dẫn nước ngầm trong tường gạch)", "Act 6: Climax Wonder"),
    ("Beat 19", "Grand Reveal 3 (Tầng thượng tuyệt đỉnh nhìn ra dòng Euphrates)", "Act 6: Climax Wonder"),
    ("Beat 20", "Golden Hour Sunset (Hoàng hôn vàng rực nhuộm đỏ Lưỡng Hà)", "Act 6: Climax Wonder"),
    ("Beat 21", "Touching Euphrates Water (Chạm tay vào dòng nước trong vắt)", "Act 7: Decompression & Return"),
    ("Beat 22", "Decompression Ox-cart Ride (Ngồi trên xe bò nhìn lại kỳ quan)", "Act 7: Decompression & Return"),
    ("Beat 23", "Final Sign-off & Temporal Glitch (Tạm biệt khán giả & hiệu ứng glitch)", "Act 7: Decompression & Return")
]

lines = [
    "# 🏛️ Bảng Review Khung Ảnh Đầu (Scene Images) — Vườn Treo Babylon (570 TCN)",
    "",
    "> [!NOTE]",
    "> Toàn bộ **23 hình ảnh khung đầu** (16:9 Landscape) đã được sinh và tải về lưu trữ cục bộ. Hãy xem qua từng hình ảnh bên dưới. Bạn có thể yêu cầu **gen lại bất kỳ cảnh nào** kèm ghi chú chỉnh sửa prompt.",
    "",
    "## 📊 Tổng Quan Dự Án",
    "- **Dự án**: `Time Travel Vlog — Hanging Gardens of Babylon (570 BC)`",
    "- **Project ID**: `6224591f-b884-42f2-8f57-613bc86d66fb`",
    "- **Video ID**: `71909a60-29f7-460e-807c-ed48b8a12ad1`",
    "- **Nhân vật chính**: `Mia` (Face UUID: `3904fece-f12e-47ef-9018-361f1a74f315`)",
    "- **Tổng số phân cảnh**: 23 beats chuẩn cấu trúc 7 Hồi Time-Travel Vlog",
    "",
    "---",
    ""
]

current_act = ""
for i, r in enumerate(rows):
    order, sid, mid, prompt, vprompt, narrator, chain_type, char_names = r
    idx = order + 1
    beat_info = beats[i] if i < len(beats) else (f"Beat {idx}", "Scene", "General")
    act = beat_info[2]

    if act != current_act:
        current_act = act
        lines.append(f"## 🎬 {current_act}")
        lines.append("")

    img_abs = f"/C:/Users/Administrator/.gemini/antigravity-ide/brain/e22150ce-4262-4e3c-8619-a7731a7f7c3a/images/scene_{idx:02d}.jpg"
    lines.append(f"### Cảnh {idx:02d}: {beat_info[1]}")
    lines.append(f"![Cảnh {idx:02d} - {beat_info[1]}]({img_abs})")
    lines.append("")
    lines.append(f"- **Mã phân cảnh / Beat**: `{beat_info[0]}` | **Chain Type**: `{chain_type}`")
    lines.append(f"- **Scene ID**: `{sid}` | **Media UUID**: `{mid}`")
    lines.append(f"- **Prompt khung ảnh đầu**:")
    lines.append(f"  > `{prompt}`")
    lines.append(f"- **Video Prompt (8s Veo 3)**:")
    lines.append(f"  > `{vprompt}`")
    if narrator:
        lines.append(f"- **Lời thoại / Thuyết minh**:")
        lines.append(f"  > *\"{narrator}\"*")
    lines.append("")
    lines.append("---")
    lines.append("")

content = "\n".join(lines)
with open(TARGET_MD, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Generated review artifact: {TARGET_MD}")
