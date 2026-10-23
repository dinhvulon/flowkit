# Quy tắc Khóa Prompt Video Phim Điện Ảnh: Bắt buộc Structured JSON, Bộ Skill `sw-*` + `fk-*` & Chạy Linter (`tools/lint_prompt.py`)

> **QUY TẮC BẮT BUỘC CHO MỌI AGENT KHI VIẾT HOẶC SỬA PROMPT VIDEO TRONG FLOWKIT (`/fk-film`):**
> Áp dụng cho cả Antigravity (`agy`), Gemini và Claude (`claude`).

Khi tạo mới hoặc cập nhật bất kỳ `video_prompt` hoặc `image_prompt` nào (`POST /api/scenes`, `PATCH /api/scenes`, hoặc submit lệnh sinh qua batch API):

### 1. BẮT BUỘC ĐIỀU PHỐI BỘ SKILL `sw-*` VÀ `fk-*` TRƯỚC KHI VIẾT PROMPT
- **Kịch bản & Cấu trúc (`sw-*`):** Mọi cảnh phải xuất phát từ `story-bible.md` và `script.md` đã được thiết kế bằng `/sw-workflow`, `/sw-premise-theme`, `/sw-genre-anatomy`, `/sw-story-structure`, `/sw-truby-anatomy`, `/sw-character-conflict`, `/sw-scene-craft`, `/sw-dialogue`, `/sw-format-adaptation`, và kiểm toán nhịp qua `/fk-paper-edit`.
- **Thiết kế Nhân vật & Sinh vật (`/fk-character-design`, Rule 58, Rule 72):** Mọi ảnh reference cho nhân vật (`<Tên>`, `<Tên> Body`) và sinh vật chủ chốt phải là Turnaround Sheet 16:9 chụp người thật 35mm (Live-Action) hoặc mô hình practical animatronic SFX. Tuyệt đối cấm từ khóa 2D (`study`, `sketch`, `concept art`, `drawing`, `illustration`, `CGI render`).
- **Storyboard 2×2 (`/fk-storyboard`, Rule 69, Rule 74):** Mọi cảnh chuyển / mở đầu (Rule 65 Loại 2) bắt buộc sinh ảnh Storyboard 2×2 có truyền `source_media_id` từ ảnh ref có sẵn, tẩy watermark (Rule 28), upload lấy UUID sạch, và thực hiện **Visual Audit đọc 4 panel thực tế** trước khi khóa `video_prompt`.

### 2. BẮT BUỘC DÙNG CẤU TRÚC STRUCTURED JSON CỦA PHIM NGÔI THỨ BA (`/fk-prompt-lock`)
Mỗi `video_prompt` phải là một đối tượng JSON hợp lệ gồm đủ 13 trường theo `skills/fk-film/references/prompt-lock.md`:
- `clip_id`, `scene_name`, `duration` (`4/6/8/10`), `aspect_ratio`, `refs` (tối đa 7 entity).
- `start_frame` & `storyboard`: Khóa `"STORYBOARD OF FOUR MOMENTS IN TIME"` trỏ chip `{{media:<uuid>|<CLIP> Storyboard.jpg}}` (hoặc `PREV_LAST_FRAME` cho cảnh nối tiếp cùng góc máy).
- `camera`: Góc máy điện ảnh ngôi thứ ba (`"third-person cinematic camera; the camera itself is never seen"`), ống kính Panavision Anamorphic 35mm, khẩu độ `deep focus f/8`. Chỉ định rõ các mốc **crisp hard cut** giữa các panel có góc máy lệch `> 45°–90°` (Rule 74 (1), (5)).
- `style` & `setting`: Chất phim 35mm chống CGI; khóa rõ `SPATIAL LOCK (INSIDE vs. OUTSIDE)` trên boong tàu/mạn thuyền/vách đá (Rule 74 (3)).
- `characters`: Khóa khuôn mặt 1:1 và trang phục thuần ảnh ref qua chip `{{media:...}}` (Rule 60, 64).
- `timeline_action`: Chia đúng mốc theo `duration`; cô lập nhân vật xuất hiện một mình (`Strictly [Name] alone in this shot; [Other] is completely off-screen` — Rule 74 (2)); tách riêng cú máy chỉ tay ngắn (`Point Shot`) với cú máy lộ mục tiêu (`Reveal Shot`) qua Hard Cut; giữ khuôn mặt lộ rõ 100% (`NO hands covering face or cheeks` — Rule 74 (6)).
- `speech`: Đa giọng nói Pinhole (`speech.voices`), khớp nguyên văn `script.md` và chuẩn số từ Rule 49 (`4s: 0/6-8; 6s: 12-15; 8s: 18-22; 10s: 24-28`).
- `post_vo`, `dramatic_craft` (`beat`, `value_turn`, `subtext`, `prop_and_detail`), `props_lock` (kèm `CREATURE & PROP SCALE/MASS LOCK` — Rule 74 (4)), `audio`, và `negative_constraints`.

### 3. BẮT BUỘC CHẠY PROMPT LINTER & `/fk-review-prompt` TRƯỚC KHI LƯU VÀ SINH
Trước khi lưu prompt vào database (`flow_agent.db`) hoặc gửi bất kỳ request sinh video nào (`GENERATE_VIDEO_REFS`), Agent **BẮT BUỘC PHẢI CHẠY LỆNH KIỂM TRA**:
```bash
python tools/lint_prompt.py output/<slug>/prompts_act1.json
# Hoặc kiểm tra scene đã lưu:
python tools/lint_prompt.py --scene <scene_id>
```
Nếu có bất kỳ lỗi nào (`CRITICAL` hoặc `HIGH`): **CẤM GỬI LỆNH SINH VIDEO**. Agent phải sửa prompt đạt `errors=0` mới được tiếp tục!
