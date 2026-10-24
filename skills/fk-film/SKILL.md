---
name: fk-film
description: Narrative film & series orchestrator (third-person cinematic, structured JSON prompts, Storyboard 2x2, Omni Flash R2V). BẮT BUỘC điều phối 100% bộ skill biên kịch sw-* và toàn bộ bộ skill điện ảnh fk-* để tạo Story Bible, Kịch bản, Character/Creature Turnaround Sheets, Storyboard 2x2, Prompt Video JSON, Sinh & Review Video 24 Frames + Whisper, và Hậu kỳ.
---

# fk-film — Quy Trình Đạo Diễn & Sản Xuất Phim Điện Ảnh Ngôi Thứ Ba (Narrative Film & Series Orchestrator)

Skill điều phối **tổng thể và bắt buộc** để làm **phim điện ảnh hoặc series kể chuyện ngôi thứ ba** trên Google Flow / Omni Flash R2V: từ nghiên cứu đề tài, xây dựng `story-bible.md`, viết kịch bản phân cảnh `script.md`, kiểm toán dựng trên giấy (`paper_edit.md`), thiết kế Character & Creature Turnaround Sheets 16:9, thiết kế & sinh **Storyboard 2×2** cho mọi cảnh chuyển, chuyển thể sang **Structured Prompt JSON (`prompts.json`)**, kiểm toán `lint_prompt.py`, sinh video R2V, chấm điểm 24 frames + Whisper, upscale 1080p, xóa watermark và dựng hậu kỳ xuất bản.

> **NGUYÊN TẮC CỐT LÕI (BẮT BUỘC 100%):**
> 1. **100% Điện ảnh ngôi thứ ba (`Third-Person Cinematic Film`):** Máy quay là ống kính điện ảnh 35mm khách quan (`"third-person cinematic camera; the camera itself is never seen"`). **TUYỆT ĐỐI CẤM** mọi góc quay hay ngôn ngữ vlog/selfie/điện thoại.
> 2. **BẮT BUỘC dùng bộ Skill Biên Kịch `sw-*` và các Skill Điều Phối `fk-*`:** Không bao giờ tự viết kịch bản, thiết kế nhân vật, storyboard hay prompt video một cách tự phát (ad-hoc). Mỗi bước trong 12 bước dưới đây **BẮT BUỘC** phải kích hoạt và tuân thủ đúng các skill `sw-*` và `fk-*` được chỉ định.

---

## Bảng Ma Trận Điều Phối Toàn Bộ Skill Bắt Buộc (`sw-*` + `fk-*`)

| Giai đoạn | Các Skill BẮT BUỘC Kích Hoạt & Áp Dụng | Đầu ra bắt buộc (Deliverables) |
| :--- | :--- | :--- |
| **0. Nghiên cứu & Xác thực** | `/fk-research` (Rule 14, Rule 15) + [`references/era-research.md`](references/era-research.md) | `.omc/research/<topic>.md` |
| **1. Kiến trúc Câu chuyện (`Story Bible`)** | **Bắt buộc điều phối qua `/sw-workflow`:**<br>• Phim lẻ / Điện ảnh: `/sw-premise-theme`, `/sw-genre-anatomy`, `/sw-story-structure`, `/sw-truby-anatomy`, `/sw-character-conflict`<br>• Series nhiều tập: thêm `/sw-series-engine-bible`, `/sw-series-structure`, `/sw-writers-room`<br>• Đối chiếu cấu trúc & phong cách (tùy thể loại): `/sw-american-case-studies`, `/sw-series-case-studies`, `/sw-japanese-screenwriting`, `/sw-korean-french-screenwriting`, `/sw-chinese-series-practice`, `/sw-sitcom-comedy`, `/chekhov-dramaturgy`, `/ozu-screenplay-style`, `/succession-series-writing` | `output/<slug>/story-bible.md` |
| **1.5. Chốt Gói Mở Đầu (Title + Thumbnail + Hook)** | `/fk-scriptwriter` (§G2) + `/fk-thumbnail-guide` + `/sw-industry-business` | 3 Tiêu đề + 4 phương án Thumbnail + Câu mở đầu 5s + Lời hứa 30s (User duyệt trước khi viết kịch bản) |
| **2. Viết Kịch bản Phân cảnh (`Script`)** | `/sw-scene-craft` + `/sw-dialogue` + `/sw-format-adaptation` + `/fk-scriptwriter` + `/fk-camera-guide` + `/fk-action-choreography` + `/fk-cinematic-transitions` + `/fk-sound-design` + [`references/voice-bible.md`](references/voice-bible.md) | `output/<slug>/script.md` (hoặc `script_act*.md`) |
| **2.5. Dựng trên giấy (`Paper Edit`)** | `/fk-paper-edit` (`python tools/paper_edit.py`) | `output/<slug>/paper_edit.md` (Kiểm tra tổng thời lượng, số từ Rule 49, lời hứa 30s, móc giữ chân $\le 90\text{s}$) |
| **3. Thiết kế Nhân vật & Sinh vật (`Character & Creature Design`)** | `/fk-character-design` (Rule 58, Rule 72) + `/fk-character-bible` + `/fk-add-material` + [`references/character-bible.md`](references/character-bible.md) | Prompt & Ảnh Turnaround Sheet 16:9 35mm Live-Action / Practical SFX cho mọi Nhân vật (`<Tên>`, `<Tên> Body`) & Sinh vật chủ chốt |
| **4. Thiết kế Phân cảnh & Storyboard 2×2** | `/fk-storyboard` (Rule 69) + `/fk-camera-guide` + `/fk-action-choreography` + [`references/shots-and-realism.md`](references/shots-and-realism.md) | `output/<slug>/storyboards_act*.json` (Bảng phân cảnh 4 panel theo thời gian cho mọi cảnh chuyển) |
| **5. Chuyển thể Structured Prompt JSON & Kiểm toán** | `/fk-script-to-prompts` + `/fk-prompt-lock` + `/fk-review-prompt` + `python tools/lint_prompt.py` + [`references/prompt-lock.md`](references/prompt-lock.md) + [`references/production-lessons.md`](references/production-lessons.md) | `output/<slug>/prompts_act*.json` (`errors=0` trên `lint_prompt.py`) |
| **6. Khởi tạo Dự án & Sinh Ảnh Reference** | `/fk-create-project` + `/fk-switch-project` + `/fk-gen-refs` + `/fk-upload-ref` + `/fk-upload-image` + `/fk-remove-watermark` + `/fk-fix-uuids` + `/fk-review-board` | Project DB + Toàn bộ Entity có UUID ảnh sạch logo (`*_clean.jpg`) được User duyệt |
| **6.5. Sinh Ảnh Storyboard 2×2 & Visual Audit** | `/fk-storyboard` + `/fk-gen-images` + `/fk-remove-watermark` + `/fk-upload-image` + `/fk-review-prompt` + `/fk-review-board` | `output/<slug>/images/<CLIP>_storyboard_clean.jpg` + Cập nhật `video_prompt` khớp 100% thể ảnh thực tế |
| **7–9. Sinh Video R2V, Review 24 Frames + Whisper, Upscale 1080p** | `/fk-gen-videos` + `/fk-monitor` + `/fk-status` + `/fk-doctor` + `/fk-review-video` (Rule 73: 24 frames `tile=6x4` + Rule 67: `tools/review_dialogue.py` Whisper) + `/fk-remove-watermark` | Video 720p được duyệt $\to$ `output/<slug>/1080/<CLIP>_1080p_clean.mp4` |
| **10–12. Dựng Hậu kỳ, Xuất bản & Analytics** | `/video-editing` (Rule 66) + `/fk-capcut-edit` + `/fk-sound-design` + `/fk-gen-music` + `/fk-brand-logo` + `/fk-concat` + `/fk-youtube-seo` + `/fk-thumbnail` + `/fk-youtube-upload` + `/fk-youtube-analytics` | Bản phim Master `−14 LUFS`, Shorts 9:16, Bộ Thumbnail & SEO YouTube |

---

## Quy Trình 12 Bước Thực Thi Chi Tiết (Có Cổng Duyệt Ở Mỗi Bước Sinh Media — Rule 29)

### Bước 0 — Nghiên cứu & Xác thực (`/fk-research`)
- Đọc [`references/era-research.md`](references/era-research.md).
- Nếu phim dựa trên lịch sử, sự kiện hoặc địa danh có thật: bắt buộc chạy `/fk-research` và lưu kết quả vào `.omc/research/`. Nếu có nhân vật lấy nguyên mẫu từ người thật nổi tiếng, áp dụng **Rule 15 (Real-people bypass)**.

### Bước 1 — Xây dựng `story-bible.md` (BẮT BUỘC điều phối qua bộ `sw-*`)
- Đọc và kích hoạt `/sw-workflow`:
  1. **`/sw-premise-theme`**: Xác lập Premise, Controlling Idea (*Value + Cause*) và xung đột cốt lõi.
  2. **`/sw-genre-anatomy`**: Xác định hệ thống Genre Beats và triết lý thể loại (Phiêu lưu sinh tồn, Sử thi lịch sử, Kinh dị quái thú, Giả tưởng, v.v.).
  3. **`/sw-story-structure` & `/sw-truby-anatomy`**: Thiết kế 22 bước cấu trúc hữu cơ của Truby (Ghost, Need vs. Desire, Opponent's Plan, Drive, Reveal, Moral Decision) kết hợp bản đồ nhịp 3 Hồi.
  4. **`/sw-character-conflict`**: Xây dựng nhân vật 3 chiều (Physiology, Sociology, Psychology), ma trận đối kháng 4 góc (*Four-Corner Opposition*), `CHARACTER_LOCK` và `VOICE_LOCK` (theo [`references/character-bible.md`](references/character-bible.md) và [`references/voice-bible.md`](references/voice-bible.md)).
  5. *(Nếu làm Series nhiều tập)*: Kích hoạt thêm `/sw-series-engine-bible`, `/sw-series-structure`, và `/sw-writers-room`.
- Lưu toàn bộ vào `output/<slug>/story-bible.md`.

### Bước 1.5 — Chốt Gói Mở Đầu: Tiêu đề + Thumbnail + Lời hứa 30s (`/fk-scriptwriter` §G2, `/fk-thumbnail-guide`)
- Trước khi viết kịch bản chi tiết, trình User duyệt:
  1. **3 phương án Tiêu đề** (High-Stakes / Kịch tính cao).
  2. **4 phương án Thumbnail** (Bố cục, biểu cảm nhân vật, mối nguy trực diện, text 2–4 từ).
  3. **Câu mở đầu 5 giây đầu tiên + Lời hứa trong 30 giây đầu**.
- **DỪNG chờ User chọn phương án.**

### Bước 2 — Viết Kịch bản Phân cảnh `script.md` (BẮT BUỘC `/sw-scene-craft` + `/sw-dialogue` + `/fk-scriptwriter`)
- Mỗi cảnh trong `script.md` (hoặc `script_act1.md`..`script_act3.md`) phải được xây dựng bằng:
  - **`/sw-scene-craft`**: Xác định rõ Mục tiêu nhân vật (*Objective*), Rào cản (*Obstacle*), Bước ngoặt giá trị (*Value Turn*: `+ to -`, `- to +`), Đạo cụ mấu chốt (*Prop & Detail*), vào cảnh muộn – ra cảnh sớm (*Enter late, leave early*).
  - **`/sw-dialogue` & [`references/voice-bible.md`](references/voice-bible.md)**: Thoại là hành động (*Dialogue as Action*), giàu ẩn ý (*Subtext*), qua bài kiểm tra che tên (*Cover-the-Names Test*). Số từ tiếng Anh trong mỗi cảnh **khớp cứng thời lượng clip theo Rule 49** (`4s: 0 hoặc 6–8 từ`; `6s: 12–15 từ`; `8s: 18–22 từ`; `10s: 24–28 từ`). Mỗi nhân vật có thoại được gán một Voice ID Pinhole riêng biệt.
  - **`/fk-camera-guide`, `/fk-action-choreography`, `/fk-cinematic-transitions`, `/fk-sound-design`**: Thiết kế góc máy điện ảnh 35mm, vũ đạo hành động 3 pha an toàn vật lý, điểm nối cảnh và âm thanh hiện trường.

### Bước 2.5 — Dựng trên giấy & Kiểm toán nhịp giữ chân (`/fk-paper-edit`)
- Chạy `python tools/paper_edit.py` trên `script.md` để xuất `output/<slug>/paper_edit.md`.
- Kiểm tra: tổng thời lượng từng hồi, mật độ thoại từng cảnh theo Rule 49, lời hứa 30s đầu, các móc giữ chân khán giả mỗi $\le 90\text{s}$, và đề xuất cắt gọt những cảnh không làm dịch chuyển giá trị kịch tính.
- **DỪNG trình User duyệt Kịch bản & Paper Edit.**

### Bước 3 — Thiết kế Nhân vật, Trang phục & Sinh vật Tham chiếu (BẮT BUỘC `/fk-character-design` — Rule 58, Rule 72)
- Đọc [`references/character-bible.md`](references/character-bible.md) và kích hoạt `/fk-character-design`:
  1. **Nhân vật (`<Tên>` & `<Tên> Body`):** Bắt buộc tạo Character Turnaround Sheet 16:9 chuẩn 4 góc (Front, 3/4, Side Profile, Portrait Close-up) hoặc `<Tên>` (mặt) + `<Tên> Body` (3 góc đã mặc hoàn chỉnh trang phục thời kỳ theo Rule 46). Phải là **ảnh chụp người thật trên phim trường 35mm (`Live-Action Casting Photo`)**.
  2. **Sinh vật / Quái thú chủ chốt:** Bắt buộc tạo Creature Turnaround Sheet 16:9 chuẩn 3 panel (3/4 trái, 3/4 phải, cận cảnh đầu/sọ nhìn từ phía có dấu sẹo/sừng gãy bất đối xứng). Phải là **mô hình practical animatronic / SFX vật lý trên phim trường 35mm**.
  3. **Bối cảnh & Đạo cụ vô tri (Rule 34):** Ảnh 16:9 đơn nhất, bắt buộc khóa `strictly NO humans, NO people, NO scale figures, NO split screen`.
  4. **CẤM TUYỆT ĐỂ từ khóa 2D/phác thảo (Rule 72):** Không bao giờ dùng các từ `study`, `character study`, `comparative study`, `sketch`, `sketchbook`, `concept art`, `drawing`, `illustration`, `line art`, `anime`, `cartoon`, `CGI render`.

### Bước 4 — Thiết kế Storyboard 2×2 Cho Mọi Cảnh Chuyển (BẮT BUỘC `/fk-storyboard` — Rule 65, Rule 69, Rule 74)
- Đọc [`references/shots-and-realism.md`](references/shots-and-realism.md) và kích hoạt `/fk-storyboard`:
  - **Phân loại cảnh (Rule 65):**
    - **Loại 2 (Cảnh mở đầu / Chuyển cảnh / Đổi góc máy):** Bắt buộc thiết kế tấm **Storyboard 2×2** (`start_frame.type = "STORYBOARD"`), gồm 4 panel 16:9 theo tiến trình thời gian của clip (`4s: 0/1/3/4`, `6s: 0/2/4/6`, `8s: 0/3/6/8`, `10s: 0/3/7/10`).
    - **Loại 1 (Cảnh nối tiếp trực tiếp cùng góc máy):** Dùng khung cuối của cảnh trước (`start_frame.type = "PREV_LAST_FRAME"`).
  - **Các quy tắc vàng khi thiết kế 4 Panel Storyboard 2×2 (Rule 74):**
    1. **Quy tắc 30°–90° giữa các Panel cắt cảnh (Rule 74 (5)):** Hai panel liên tiếp dùng để cắt cảnh phải thay đổi góc máy hoặc cỡ cảnh **tối thiểu `45°–90°`**. Cấm đặt 2 panel trùng góc nhìn dọc cùng một dãy lan can/tường chắn (gây lỗi cắt nửa khung hình và nhân đôi 2 lan can).
    2. **Chống đảo trục 180° gây đứng ngoài biển (Rule 74 (3)):** Không gộp 2 panel ngược trục Trái/Phải vào chung một Shot; luôn khóa rõ bên nào là sàn gỗ bên trong tàu (`INSIDE`) và bên nào là mặt biển bên ngoài (`OUTSIDE`).
    3. **Ngữ pháp "Chỉ tay ngắn ➔ Cắt cảnh mới lộ mục tiêu" & Cấm ôm mặt (Rule 74 (6)):** Khi nhân vật trên cao chỉ tay phát hiện thuyền/sinh vật/đảo ở xa, Panel chỉ tay (`0-2s`/`0-3s`) **CHỈ quay người chỉ tay trên boong tàu chỉ ra ngoài khung hình (`off-screen target`)**, tuyệt đối không nhồi cả chiếc thuyền/ông lão vào chung panel chỉ tay. Sang Panel tiếp theo (sau cú Hard Cut) mới lộ diện chiếc thuyền/ông lão. Nhân vật sợ hãi phải giữ **khuôn mặt lộ rõ 100% (`unobstructed face`)**, hai tay bám mạn thuyền, cấm lấy hai tay ôm mặt/má kịch cỡm.
    4. **Khóa đồng bộ kích thước & trọng lượng Sinh vật/Đạo cụ (Rule 74 (4)):** Đính kèm ref sinh vật/đạo cụ (như `Omen Fish`) và khóa kích thước tuyệt đối (`1.7m–1.9m, 80 kg`) đồng nhất giữa mọi tấm Storyboard.

### Bước 5 — Chuyển thể Structured Prompt JSON & Kiểm toán Tự động (BẮT BUỘC `/fk-script-to-prompts` + `/fk-prompt-lock` + `/fk-review-prompt`)
- Đọc [`references/prompt-lock.md`](references/prompt-lock.md) và [`references/production-lessons.md`](references/production-lessons.md).
- Kích hoạt `/fk-script-to-prompts` để chuyển thể từng cảnh sang cấu trúc JSON chuẩn của phim (bao gồm đầy đủ `clip_id`, `scene_name`, `duration`, `aspect_ratio`, `refs`, `start_frame`, `storyboard`, `camera`, `style`, `setting`, `characters`, `timeline_action`, `speech`, `post_vo`, `dramatic_craft`, `props_lock`, `audio`, `negative_constraints`).
- Chạy `/fk-review-prompt` để rà soát toàn bộ 15 mục trong **Checklist B** của `prompt-lock.md` và chạy công cụ kiểm toán bắt buộc:
  ```bash
  python tools/lint_prompt.py output/<slug>/prompts_act1.json
  ```
- Bắt buộc đạt **`errors=0`** trước khi lưu DB hoặc trình User duyệt.

### Bước 6 — Khởi tạo Dự án FlowKit & Sinh Ảnh Reference (Cổng Duyệt 1)
- Đọc [`references/flowkit-pipeline.md`](references/flowkit-pipeline.md).
- Chạy pre-flight kiểm tra `/health`, xóa các request `PENDING` cũ (Rule 21), tạo Project & Scenes trên FlowKit.
- Sinh ảnh Reference (`/fk-gen-refs`) gửi luôn, không cần chờ User đồng ý trước (sinh ảnh không tốn credit — Rule 29, user 24/10/2026); báo danh sách entity đã gửi và trình kết quả ở Cổng Duyệt 1.
- Ngay khi mỗi ảnh Reference sinh xong, thực hiện **4 bước Clean-Before-Video-Gen (Rule 28)**:
  1. Tải ảnh về `output/<slug>/images/<name>.jpg`.
  2. Chạy `python tools/remove_watermark_from_image.py` tạo `<name>_clean.jpg` và **xóa ngay ảnh gốc còn logo**.
  3. Upload `<name>_clean.jpg` qua `/api/flow/upload-image` lấy UUID sạch.
  4. Cập nhật UUID sạch vào Entity và mở Review Board (`/fk-review-board`) trình User duyệt.

### Bước 6.5 — Sinh Ảnh Storyboard 2×2 & Thực Hiện Visual Audit (Cổng Duyệt 2 — Rule 25, Rule 69 (7))
- Với các cảnh chuyển (Rule 65 Loại 2), báo User trước khi gửi sinh ảnh Storyboard 2×2 (bắt buộc truyền `source_media_id` từ ảnh ref nhân vật/bối cảnh có sẵn theo Rule 69 (8)).
- Khi ảnh Storyboard 2×2 sinh xong:
  1. Tải về `output/<slug>/images/<CLIP>_storyboard.jpg` $\to$ chạy `remove_watermark_from_image.py` $\to$ xóa file gốc còn logo $\to$ upload `<CLIP>_storyboard_clean.jpg` lấy UUID sạch $\to$ gán vào entity `<CLIP> Storyboard`.
  2. **Thực hiện Visual Audit bắt buộc (Rule 69 (7)):** Mở xem trực tiếp ảnh `<CLIP>_storyboard_clean.jpg`, đối chiếu từng panel (tay trái/phải, hướng nhìn, vị trí lan can, nhân vật có mặt trong từng panel) và **chỉnh lại `video_prompt`** (resolve toàn bộ `{{ref:...}}` thành chip `{{media:<uuid>|<name>}}`) cho khớp 100% với thể ảnh thực tế. Chạy lại `python tools/lint_prompt.py` đạt `errors=0`.
  3. **DỪNG — Trình ảnh Storyboard 2×2 sạch và bản cập nhật Visual Audit cho User duyệt trước khi sinh video.**

### Bước 7 — Sinh Video R2V (`GENERATE_VIDEO_REFS` — Omni Flash Pure References)
- Chỉ sau khi User duyệt ảnh Storyboard 2×2 của cảnh, gửi lệnh `GENERATE_VIDEO_REFS` (server tự điều tiết khoảng cách 45–60s giữa mọi request theo Rule 10).
- Khi video 720p sinh xong, tải ngay về `output/<slug>/scenes/`. **TUYỆT ĐỐI CHƯA XÓA LOGO Ở BƯỚC NÀY (Rule 18).**

### Bước 8 & 9 — Kiểm Toán Video Bằng 24-Frame Contact Sheet + Whisper & Cổng Duyệt Video (Rule 18, 32, 67, 73)
- Ngay khi tải video 720p thô về máy, **BẮT BUỘC** thực hiện:
  1. **Trích xuất chính xác 24 frames bằng `ffmpeg` và ghép Contact Sheet 6×4 (`tile=6x4` — Rule 73):**
     ```bash
     ffmpeg -y -i <clip>.mp4 -vf "fps=24/<duration>" -q:v 2 <dir>/frame_%02d.jpg
     ffmpeg -y -i "<dir>/frame_%02d.jpg" -vf "tile=6x4" -q:v 2 <dir>/contact_sheet_24frames.jpg
     ```
  2. **Kiểm toán âm thanh & thoại bằng Whisper (`tools/review_dialogue.py` — Rule 67):**
     - Đảm bảo khớp câu thoại trong `script.md`, không bị cắt chữ cuối, không phát sinh tiếng nói lạ (`EXTRA SPEECH`).
  3. **Chấm bảng AI Review Scorecard 6 tiêu chí (`/fk-review-video`):**
     - Đối chiếu từng cụm frame trong 24 frames với 4 panel của Storyboard 2×2 và Checklist B của `prompt-lock.md`.
  4. **DỪNG — Trình bảng Scorecard, Contact Sheet 24 frames và mở Review Board (`http://localhost:8200`) cho User duyệt từng cảnh.**
     - Nếu cảnh chưa đạt hoặc User yêu cầu sửa: cập nhật prompt / Storyboard và hỏi User trước khi gửi sinh lại ở 720p.
     - **Chỉ những cảnh đã được User duyệt thông qua:** Gửi `UPSCALE_VIDEO` lên 1080p (`p0UkFb`) $\to$ tải về `output/<slug>/1080/<CLIP>_1080p.mp4` $\to$ chạy `remove_watermark_video` trực tiếp trên bản 1080p tạo `<CLIP>_1080p_clean.mp4`.

### Bước 10, 11 & 12 — Dựng Hậu Kỳ Điện Ảnh, Đóng Gói YouTube & Chẩn Đoán Sau Đăng
- Đọc [`references/post-and-publish.md`](references/post-and-publish.md).
- Phối hợp bắt buộc:
  - **`/video-editing` (Rule 66) + `/fk-capcut-edit` + `/fk-cinematic-transitions`**: Cắt bỏ dead air, nối J-cut/L-cut, dựng Intro Trailer Montage 30s, xuất thêm 3–4 Shorts 9:16.
  - **`/fk-sound-design` + `/fk-gen-music` + `/fk-concat` + `/fk-brand-logo`**: Phối nhạc nền cổ điển/giao hưởng, foley, color grade 35mm film grain và master âm thanh chuẩn **−14 LUFS**.
  - **`/fk-youtube-seo` + `/fk-thumbnail` + `/fk-youtube-upload` + `/fk-youtube-analytics`**: Xuất metadata đồng nhất ngôn ngữ kịch bản (Rule 20), tạo 4 biến thể Thumbnail, đăng tải và theo dõi CTR / Retention 30s / AVD sau 48h & 7 ngày.

---

## Danh Mục Tài Liệu Tham Chiếu Tinh Gọn Trong `skills/fk-film/references/`

| File | Nội dung cốt lõi |
| :--- | :--- |
| [`references/era-research.md`](references/era-research.md) | Nghiên cứu lịch sử, niên đại, phục trang và quy tắc `PERIOD LOCK` (Bước 0–1) |
| [`references/character-bible.md`](references/character-bible.md) | `CHARACTER_LOCK`, `VOICE_LOCK`, bộ Reference Mặt + Body đã mặc đồ và `/fk-character-design` 16:9 (Bước 1, 3) |
| [`references/voice-bible.md`](references/voice-bible.md) | Bảng 30 giọng Pinhole / Gemini-TTS, phân vai đa nhân vật và chuẩn số từ Rule 49 (Bước 2, 5) |
| [`references/shots-and-realism.md`](references/shots-and-realism.md) | Ngôn ngữ ống kính Panavision Anamorphic 35mm, bảng phân cảnh Storyboard & Vật lý (Bước 4) |
| [`references/cinematic-toolkit.md`](references/cinematic-toolkit.md) | Vũ đạo hành động 3 pha, diễn xuất qua triệu chứng cơ thể, 5 công cụ gây hồi hộp và Wardrobe Ledger (Bước 2, 4, 5) |
| [`references/prompt-lock.md`](references/prompt-lock.md) | Khung Structured JSON 13 trường của phim + Checklist 15 hạng mục bắt buộc trước khi lưu & sau khi sinh (Bước 5, 8) |
| [`references/production-lessons.md`](references/production-lessons.md) | 17 bài học thực chiến cốt lõi của phim điện ảnh ngôi thứ ba (Storyboard Hard Cuts, Anti-Cloning, Spatial Lock, Point-Then-Reveal, Turnaround Sheet 35mm, Scale Lock, v.v.) |
| [`references/flowkit-pipeline.md`](references/flowkit-pipeline.md) | Quy trình kỹ thuật vận hành FlowKit API, R2V Pure References, 24-Frame Review Gate & Upscale 1080p (Bước 6–9) |
| [`references/post-and-publish.md`](references/post-and-publish.md) | Dựng hậu kỳ `/video-editing` + `/fk-capcut-edit`, master `−14 LUFS`, đóng gói YouTube & Shorts (Bước 10–12) |
