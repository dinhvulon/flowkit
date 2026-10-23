# Triển Khai Trong FlowKit — Omni Flash R2V Ingredients Workflow (Phim Điện Ảnh)

> **Quy chuẩn `/fk-film`:** Tài liệu này quy định quy trình kỹ thuật vận hành dự án phim điện ảnh ngôi thứ ba trên FlowKit (Bước 6–9 của `SKILL.md`), sử dụng kiến trúc **Pure References (`GENERATE_VIDEO_REFS` — Omni Flash `abra_r2v_<N>s`)** kết hợp **Storyboard 2×2 (Rule 69)** và **24-Frame Review Gate (Rule 73)**.

> **Xác nhận trước mỗi bước sinh (Rule 29):** Trước bất kỳ lệnh nào khiến Google Flow sinh media (ảnh ref, ảnh Storyboard 2×2, video R2V, sinh lại, upscale 1080p), báo rõ sẽ sinh những gì, số lượng bao nhiêu, và **chờ User đồng ý**. Xong mỗi bước phải DỪNG và trình kết quả cho User duyệt.

---

## 1. Quy Trình 2 Nhánh Nối Cảnh Chuẩn Điện Ảnh (Rule 65 & Rule 69)

| Loại cảnh | Cơ chế neo hình ảnh | Quy trình thực thi |
| :--- | :--- | :--- |
| **Loại 2: Cảnh mở đầu / Chuyển cảnh / Đổi góc máy** | **Storyboard 2×2 (`STORYBOARD`)** | Sinh 1 ảnh Storyboard 2×2 (4 panel 16:9 theo thời gian) qua `/fk-storyboard`, bắt buộc truyền `source_media_id` từ ảnh ref nhân vật/bối cảnh có sẵn. Tẩy logo ➔ upload lấy UUID sạch làm entity `<CLIP> Storyboard` ➔ Visual Audit đọc 4 panel chỉnh lại `video_prompt` ➔ gửi `GENERATE_VIDEO_REFS`. |
| **Loại 1: Cảnh nối tiếp trực tiếp cùng góc máy (Chain)** | **Khung cuối cảnh trước (`PREV_LAST_FRAME`)** | Không sinh ảnh mới. Dùng `ffmpeg` trích xuất frame cuối cùng của video cảnh trước đã duyệt ➔ chạy `tools/remove_watermark_from_image.py` ➔ upload lấy UUID sạch làm ref khung mở đầu cho cảnh tiếp theo. |

- **Cấm tuyệt đối sinh ảnh Start Frame 1 khung đơn lẻ** cho các cảnh phim có nhân vật/hành động.
- Không dùng `/fk-gen-chain-videos` (Veo start+end frame cũ không hỗ trợ trên Batch API).

---

## 2. Ánh Xạ Từ `prompts.json` Vào Cơ Sở Dữ Liệu FlowKit

Mỗi đối tượng trong `prompts_act*.json` (đã qua `/fk-script-to-prompts`, `/fk-review-prompt`, và `python tools/lint_prompt.py`) được nạp vào scene của FlowKit như sau:

| Trường trong `prompts.json` | Trường trong FlowKit (`scene`) | Quy tắc bắt buộc |
| :--- | :--- | :--- |
| `refs` | `character_names` | Danh sách tên entity tham chiếu (tối đa 7): `["<Tên>", "<Tên> Body", "<Sinh vật/Đạo cụ>", "<Bối cảnh>", "<CLIP> Storyboard"]` |
| Toàn bộ đối tượng JSON (đã resolve `{{ref:...}}` thành `{{media:<uuid>\|<name>}}`) | `video_prompt` | Chuỗi JSON hoàn chỉnh tuân thủ `prompt-lock.md` Mục A & B |
| Prompt tạo tấm Storyboard 2×2 (4 panel 16:9) | `image_prompt` (và `prompt`) | Có câu khóa `"STORYBOARD OF FOUR MOMENTS IN TIME"`, mô tả rõ Panel 1..4 và truyền `source_media_id` |
| `duration` (`4`, `6`, `8`, hoặc `10`) | `duration` | Bắt buộc `PATCH /api/scenes/{sid}` trường `duration` sau khi tạo scene (nếu thiếu sẽ mặc định thành 10s) |
| Tổng hợp câu thoại trong `speech.dialogue` | `narrator_text` | Khớp chính xác số từ theo Rule 49 |

---

## 3. Pre-Flight & Khởi Tạo Dự Án Phim

### 3.1. Kiểm tra kết nối & dọn hàng đợi cũ (Rule 21, Rule 31)
```bash
curl -s http://127.0.0.1:8100/health          # {"extension_connected": true}
curl -s http://127.0.0.1:8100/api/flow/status # {"transport": "batch", ...}
python -c "import sqlite3; conn = sqlite3.connect('flow_agent.db'); conn.execute('UPDATE request SET status=\'FAILED\' WHERE status=\'PENDING\''); conn.commit()"
```
Nếu gặp bất kỳ lỗi kết nối hoặc lỗi worker nào, gọi ngay `/fk-doctor`.

### 3.2. Tạo Project với hệ thống nhân vật đa giọng nói
```bash
curl -X POST http://127.0.0.1:8100/api/projects -H "Content-Type: application/json" -d '{
  "name": "The Golden Tree — Cinematic Adventure Film",
  "story": "<Tóm tắt Premise, Controlling Idea và 3 Hồi từ story-bible.md>",
  "material": "realistic",
  "allow_voice": true,
  "characters": [
    {"name": "Nora", "entity_type": "character", "description": "<CHARACTER_LOCK 35mm live-action>", "voice_description": "kore — firm, resolute, mid-pitched commanding female seafarer voice"},
    {"name": "Nora Body", "entity_type": "character", "description": "<16:9 turnaround sheet dressed in seafarer costume>"},
    {"name": "Castor", "entity_type": "character", "description": "<CHARACTER_LOCK 35mm live-action>", "voice_description": "alnilam — firm, gritty mid-low male warrior voice"},
    {"name": "Castor Body", "entity_type": "character", "description": "<16:9 turnaround sheet dressed in bronze-studded leather armor>"},
    {"name": "Omen Fish", "entity_type": "character", "description": "<16:9 3-panel practical SFX creature turnaround sheet, 1.8m 80kg>"},
    {"name": "Galleon Deck", "entity_type": "visual_asset", "description": "<16:9 wide establishing photograph of weathered wooden galleon deck, strictly NO humans>"}
  ]
}'
```
- **Lưu ý quan trọng:** Các bối cảnh cần giữ đồng nhất phải khai báo `entity_type: "visual_asset"` để worker đính kèm vào R2V `imageInputs`. Các công trình kiến trúc / đạo cụ vô tri tuân thủ Rule 34 (`strictly NO humans, NO scale figures`).

---

## 4. Sinh & Chuẩn Hóa Bộ Reference (Bước 6 — Cổng Duyệt 1)

1. Dùng `/fk-character-design` (Rule 58, Rule 72) tạo prompt chuẩn 35mm Live-Action / Practical SFX Turnaround Sheet 16:9 cho toàn bộ nhân vật, Body đã mặc trang phục (Rule 46), sinh vật chủ chốt và bối cảnh.
2. Sau khi ảnh sinh xong, thực hiện **Quy trình 4 bước Clean-Before-Video-Gen (Rule 28)**:
   - Tải ảnh gốc về `output/<slug>/images/<name>.jpg`.
   - Chạy `python tools/remove_watermark_from_image.py "output/<slug>/images/<name>.jpg"` ➔ tạo `<name>_clean.jpg`, sau đó **xóa ngay file gốc còn logo**.
   - Upload `<name>_clean.jpg` qua `POST /api/flow/upload-image` lấy UUID sạch.
   - Gán UUID sạch vào entity và kiểm tra không còn ID dạng `CAMS...` (`/fk-fix-uuids`).
3. **DỪNG — Trình User duyệt toàn bộ ảnh Reference.**

---

## 5. Sinh Storyboard 2×2 & Visual Audit (Bước 6.5 — Cổng Duyệt 2)

1. Với các cảnh chuyển (Rule 65 Loại 2), gửi request `GENERATE_IMAGE` / `REGENERATE_IMAGE` kèm `source_media_id` (UUID ảnh ref nhân vật chính/bối cảnh).
2. Khi ảnh Storyboard 2×2 sinh xong: tải về ➔ chạy `remove_watermark_from_image.py` ➔ xóa ảnh gốc còn logo ➔ upload bản `_clean.jpg` lấy UUID sạch ➔ gán vào entity `<CLIP> Storyboard`.
3. **Thực hiện Visual Audit bắt buộc (Rule 69 (7) & Rule 74):**
   - Xem trực tiếp ảnh `<CLIP>_storyboard_clean.jpg`.
   - Kiểm tra 4 panel: có bị nhân đôi lan can/nhân vật không? Góc máy giữa các panel cắt cảnh có đủ độ lệch `> 45°–90°` không? Nhân vật chỉ tay bằng tay trái hay tay phải? Khuôn mặt có lộ rõ 100% không?
   - Cập nhật lại `video_prompt` (resolve toàn bộ `{{ref:...}}` thành `{{media:<uuid>|<name>}}`) và chạy `python tools/lint_prompt.py` đạt 0 lỗi.
4. **DỪNG — Trình ảnh Storyboard 2×2 sạch và kết quả Visual Audit cho User duyệt trước khi sinh video.**

---

## 6. Sinh Video R2V, Review 24 Frames + Whisper & Hậu Kỳ 1080p (Bước 7–10)

1. **Sinh video R2V (`GENERATE_VIDEO_REFS`):**
   - Sau khi User duyệt Storyboard 2×2, gửi request `GENERATE_VIDEO_REFS`. Server tự giãn cách 45–60s giữa mọi request tới Flow (Rule 10).
2. **Tải bản 720p thô & Kiểm toán 24 Frames + Whisper (Rule 18, 32, 67, 73):**
   - Tải video 720p về `output/<slug>/scenes/`. **Chưa xóa logo ở bước này.**
   - Dùng `ffmpeg` trích xuất **đúng 24 frames** (`fps=24/<duration>`) và ghép **Contact Sheet 6×4 (`tile=6x4`)**:
     ```bash
     ffmpeg -y -i <clip>.mp4 -vf "fps=24/<duration>" -q:v 2 <dir>/frame_%02d.jpg
     ffmpeg -y -i "<dir>/frame_%02d.jpg" -vf "tile=6x4" -q:v 2 <dir>/contact_sheet_24frames.jpg
     ```
   - Chạy `python tools/review_dialogue.py` (Whisper, Rule 67) để kiểm tra khớp thoại.
   - Chấm điểm AI Review Scorecard 6 tiêu chí trên 24 frames, mở Review Board (`python tools/review_server.py 8200`), và **DỪNG chờ User duyệt từng cảnh**.
3. **Upscale 1080p & Xóa Logo (Chỉ cho cảnh đã được User duyệt — Rule 18):**
   - Gửi `UPSCALE_VIDEO` (`p0UkFb`) ➔ tải về `output/<slug>/1080/<clip>_1080p.mp4`.
   - Chạy `remove_watermark_video` trực tiếp trên bản 1080p ➔ `<clip>_1080p_clean.mp4`.
4. **Dựng Hậu Kỳ Điện Ảnh:**
   - Phối hợp bắt buộc `/video-editing` (Rule 66), `/fk-capcut-edit`, `/fk-cinematic-transitions`, `/fk-sound-design`, và `/fk-concat` để cắt bỏ dead air, nối J-cut/L-cut, lồng nhạc/SFX và master chuẩn `−14 LUFS`.
