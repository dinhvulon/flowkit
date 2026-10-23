# 🔒 PROMPT LOCK — Khung `video_prompt` Phim Điện Ảnh & Checklist Trước Khi Lưu

> **Quy chuẩn `/fk-film`:** Đọc ở **Bước 5** của `SKILL.md` và chạy lại ở **Bước 9** khi review video. Mọi `video_prompt` (POST hoặc PATCH) bắt buộc tuân thủ kiến trúc Structured JSON của phim điện ảnh ngôi thứ ba, vượt qua `python tools/lint_prompt.py` với **0 lỗi**, và đạt 100% các mục trong **Checklist B** dưới đây trước khi lưu hoặc gửi sinh.

---

## A. Khung `video_prompt` của Phim — Structured JSON (Rule 55, Rule 56, Rule 64, Rule 69, Rule 74)

Thứ tự các trường bắt buộc trong mỗi đối tượng prompt JSON:

1. **`clip_id`, `scene_name`, `duration`, `aspect_ratio`, `refs`**
   - `duration`: `4`, `6`, `8`, hoặc `10` (giây).
   - `refs`: Danh sách tên entity tham chiếu (tối đa 7 theo giới hạn Omni Flash), bao gồm `<Tên>` (mặt), `<Tên> Body` (đã mặc trang phục), sinh vật/đạo cụ (`Omen Fish`, v.v.), bối cảnh, và `<CLIP> Storyboard` (tấm Storyboard 2×2 đã xóa logo).
2. **`start_frame` & `storyboard`**
   - Cảnh chuyển / mở đầu (Rule 65 Loại 2): `start_frame.type = "STORYBOARD"`, khối `storyboard` chứa câu khóa `"STORYBOARD OF FOUR MOMENTS IN TIME"` trỏ chip `{{media:<uuid>|<CLIP> Storyboard.jpg}}` và mô tả rõ 4 panel theo mốc giây (`4s: 0/1/3/4`, `6s: 0/2/4/6`, `8s: 0/3/6/8`, `10s: 0/3/7/10`).
   - Cảnh nối tiếp trực tiếp (Rule 65 Loại 1): `start_frame.type = "PREV_LAST_FRAME"`.
3. **`camera`**
   - `viewpoint`: `"third-person cinematic camera; the camera itself is never seen"`.
   - `shot_size`: Mở đầu bằng `OPENING SHOT (second 0): matching the top-left panel (Panel 1) of {{media:<uuid>|<CLIP> Storyboard.jpg}} — ...`.
   - `description`: Ống kính Anamorphic 35mm, khẩu độ `deep focus f/8`, chuyển động máy theo `/fk-camera-guide`, và chỉ định rõ các mốc **crisp hard cut** giữa các panel (`At second 3.0, a crisp hard cut matching Panel 2...`).
4. **`style`**
   - Chất phim điện ảnh 35mm (`35mm film, cinematic documentary realism, Panavision anamorphic lens, natural organic lighting, subtle film grain, deep focus f/8, photorealistic, tactile textures`), chống CGI.
5. **`setting`**
   - Địa điểm trỏ chip ref bối cảnh `{{ref:<Bối cảnh>}}`, thời tiết, giờ và nguồn sáng tự nhiên khớp cảnh liền trước/sau, kèm `SPATIAL LOCK (INSIDE vs. OUTSIDE)` chỉ rõ bên nào là sàn tàu/mặt đất bên trong và bên nào là mặt biển/vực bên ngoài.
6. **`characters[]`**
   - Mỗi nhân vật/sinh vật trong cảnh: `name`, `visual_lock` (trỏ thẳng chip `{{ref:<Tên>}}` và `{{ref:<Tên> Body}}` theo Rule 64, không tả lại trang phục bằng chữ), và `state` (trạng thái cơ thể ở giây 0: ướt mưa, căng cơ hàm, tay nắm chặt đạo cụ).
7. **`timeline_action`**
   - Chia đúng mốc theo `duration` (`4s: 0-2s / 2-4s`; `6s: 0-2s / 2-4s / 4-6s`; `8s: 0-3s / 3-6s / 6-8s`; `10s: 0-3s / 3-7s / 7-10s`).
   - Mỗi nhịp neo rõ vào đúng Panel của Storyboard (`Matching Panel 1 (Top-Left) of {{media:...}}: ...`), có nguyên nhân vật lý rõ ràng, ghi rõ nhân vật nào xuất hiện một mình (`Strictly [Name] alone in this shot; [Other] is completely off-screen`), và nhúng thoại trực tiếp tại mốc giây tương ứng.
8. **`speech`**
   - `speaker`, `voices` (map từng người nói sang Voice ID Pinhole riêng biệt), `delivery` (ngữ điệu cụ thể, gắt/khẩn trương khi nguy hiểm), `dialogue[]` (mốc giây, người nói, câu thoại nguyên văn từ `script.md`, tổng số từ tuân thủ Rule 49).
9. **`post_vo`**
   - Lời dẫn hoặc âm thanh bộ đàm/tiếng vọng ngoài hình chèn lúc dựng hậu kỳ (`null` nếu không có).
10. **`dramatic_craft`** (Rule 56 — kết tinh từ bộ `sw-*`)
    - `beat`: Hành động tác động / phản ứng bằng danh động từ (`gerunds`, theo `/sw-dialogue` & `/sw-scene-craft`).
    - `value_turn`: Bước ngoặt giá trị điện tích từ đầu cảnh đến cuối cảnh (ví dụ `+ to -`, `- to --`).
    - `subtext`: Ẩn ý thực sự dưới lời thoại hoặc sự im lặng.
    - `prop_and_detail`: Đạo cụ mấu chốt và chi tiết cơ học/sinh học neo cảm xúc.
11. **`props_lock`**
    - Khóa số lượng, kích thước vật lý tuyệt đối (`CREATURE & PROP SCALE/MASS LOCK`) và bàn tay cầm giữ của mọi đạo cụ/sinh vật quan trọng xuyên suốt clip.
12. **`audio`**
    - Hòa âm 3 tầng: thoại nổi rõ trên nền + foley hiện trường + ambient môi trường (theo `/fk-sound-design`).
13. **`negative_constraints`**
    - Viết thành câu hoàn chỉnh: cấm chữ/logo/watermark, cấm CGI/bóng nhựa/2D sketch, cấm khói thở trắng (`NO breath smoke`), cấm nhân đôi nhân vật (`NO duplicate characters, NO cloning`), khóa cắt cảnh dứt khoát (`crisp hard cuts at second X.0, no camera blending, no half-frame split-railing cut`), cấm ôm mặt kịch cỡm (`NO hands covering face or cheeks`).

---

## B. Checklist Kiểm Toán Trước Khi Lưu & Trước Khi Gửi Sinh (100% phải trả lời "ĐẠT")

| # | Hạng mục kiểm tra | Tham chiếu |
|---|---|---|
| 1 | **Góc máy ngôi thứ ba thuần túy:** `camera.viewpoint` là `"third-person cinematic camera; the camera itself is never seen"`; không trùng cả cỡ cảnh lẫn góc máy với cảnh liền trước | `/fk-camera-guide` |
| 2 | **Tối đa 7 refs & Nhắc đủ chip `{{ref:...}}` / `{{media:...}}`:** Mọi entity trong `refs` đều được nhắc bằng chip inline trong prompt; nhân vật có đủ `<Tên>` + `<Tên> Body`; `lint_prompt.py` báo 0 lỗi | Rule 46, Rule 64 |
| 3 | **Khóa khuôn mặt 1:1 & Trang phục thuần ảnh Ref:** Không tự tả lại hoa văn/biến thể trang phục bằng chữ; chỉ khóa khớp 1:1 với `{{ref:<Tên>}}` và `{{ref:<Tên> Body}}` | Rule 52, Rule 60 |
| 4 | **Chuẩn Turnaround Sheet 16:9 Live-Action / Practical SFX:** Mọi ảnh ref nhân vật và sinh vật chủ chốt đã được thiết kế qua `/fk-character-design` (không có từ khóa 2D `study`, `sketch`, `concept art`) và đã tẩy watermark + upload lại lấy UUID sạch | Rule 28, Rule 58, Rule 72 |
| 5 | **Storyboard 2×2 & `source_media_id`:** Cảnh chuyển (Rule 65 Loại 2) dùng `STORYBOARD` 2×2 sinh có `source_media_id` từ ảnh ref gốc, đã tẩy logo và upload lấy UUID sạch; cảnh nối tiếp dùng `PREV_LAST_FRAME` | Rule 65, Rule 69, `/fk-storyboard` |
| 6 | **Visual Audit 4 Panel thực tế:** Đã đọc trực tiếp ảnh Storyboard 2×2 sạch vừa sinh để chỉnh lại `camera`, `timeline_action` (tay trái/phải, hướng nhìn, bố cục) khớp 100% với hình ảnh thực tế trên 4 panel | Rule 69 (7) |
| 7 | **Crisp Hard Cuts & Quy tắc 30°–90°:** Các panel khác góc máy được chuyển bằng `crisp hard cut` tại đúng mốc giây; góc máy giữa 2 panel cắt cảnh chênh nhau `> 45°–90°` (không cắt giữa 2 panel trùng góc nhìn dọc cùng một lan can gây lỗi nhân đôi 2 lan can) | Rule 74 (1), (5) |
| 8 | **Cô lập nhân vật & Chống phân thân (`Anti-Cloning Lock`):** Khi một Shot chỉ quay 1 nhân vật, ghi rõ `Strictly [Name] alone in this shot; [Other] is completely off-screen` và khóa `NO duplicate characters, NO cloning` trong `negative_constraints` | Rule 74 (2) |
| 9 | **Chống trộn trục 180° & Khóa không gian Trong/Ngoài lan can (`SPATIAL LOCK`):** Mỗi Shot chỉ neo theo 1 Panel duy nhất (không gộp `matching Panel 3 and Panel 4` nếu ngược trục); ghi rõ bên nào là sàn gỗ bên trong tàu và bên nào là mặt biển bên ngoài | Rule 74 (3) |
| 10 | **Ngữ pháp "Chỉ tay ngắn ➔ Cắt cảnh mới lộ mục tiêu" & Cấm ôm mặt:** Cú máy chỉ tay (`0-2s`/`0-3s`) chỉ quay người chỉ tay trên boong về phía ngoài khung hình, sau đó Hard Cut mới lộ mục tiêu (thuyền/sinh vật/đảo); nhân vật sợ hãi giữ mặt lộ rõ 100% (`NO hands on face/cheeks`), hai tay bám mạn thuyền/đạo cụ | Rule 74 (6) |
| 11 | **Đồng bộ kích thước & trọng lượng Sinh vật / Đạo cụ (`SCALE & MASS LOCK`):** Sinh vật/đạo cụ có ảnh ref (như `Omen Fish`) được đính vào `refs` ở mọi cảnh có mặt và khóa cứng kích thước/trọng lượng tuyệt đối (`1.7m–1.9m, 80 kg`); không tả vật thể lồi bên ngoài vảy khi chưa mổ bụng | Rule 74 (4) |
| 12 | **Hiện diện từ giây 0 & Khóa đạo cụ liền mạch (`props_lock`):** Mọi thực thể trong Shot đã có mặt từ giây đầu của Shot; đạo cụ cầm tay hoặc sợi dây hai người giằng co được khóa `exactly ONE single continuous unbroken...` | Bài học 11 |
| 13 | **Vật lý thực tế, Chống CGI, Cấm khói thở & Deep Focus `f/8`:** Hành động chia 3 pha theo `/fk-action-choreography`, tuân thủ quán tính $p=m\cdot v$; biểu bì sinh học thô ráp; cấm khói thở trắng (`NO breath smoke`), cấm `god rays`; khóa `deep focus f/8` | Rule 57, Rule 62, `/fk-action-choreography` |
| 14 | **Thoại chuẩn Rule 49, Voice ID riêng & Ngữ điệu kịch tính:** Số từ khớp thời lượng clip (4s: 0/6-8; 6s: 12-15; 8s: 18-22; 10s: 24-28); mỗi người nói 1 Voice ID trong `speech.voices`; nói từ đầu nhịp khi mặt lộ rõ; người nghe khép môi; thoại trong vùng nguy hiểm/tranh cãi phải nhanh, lớn, gắt; không có từ khóa mua bán/tiền bạc gây ghost op | Rule 49, Rule 54, `/sw-dialogue` |
| 15 | **Đầy đủ `dramatic_craft` từ bộ `sw-*`:** Có đủ `beat`, `value_turn`, `subtext`, `prop_and_detail` phản ánh đúng kịch bản đã viết qua bộ skill `sw-*` | Rule 56, `/sw-scene-craft` |

---

## C. Kiểm Toán Sau Khi Sinh Video (24-Frame Contact Sheet + Whisper)

Khi video 720p sinh xong (trước khi upscale 1080p):
1. Dùng `ffmpeg` trích xuất **đúng 24 frames** (`fps=24/<duration>`) và ghép thành **Contact Sheet 6×4 (`tile=6x4`)** theo Rule 73.
2. Chạy `python tools/review_dialogue.py` (Whisper, Rule 67) kiểm tra khớp thoại.
3. Đối chiếu từng cụm frame trên Contact Sheet 24 frames với Checklist B và 4 panel của Storyboard 2×2. Nếu phát hiện lỗi mới, cập nhật ngay vào `production-lessons.md` và `prompt-lock.md`.

## D. Tự Đọc Lại Toàn Bộ Prompt Sau Mỗi Lần Sửa (`/fk-review-prompt`)

Sau mỗi lần chỉnh sửa bất kỳ trường nào trong prompt JSON:
1. Đọc lại **toàn bộ** đối tượng prompt của cảnh đó (không chỉ đọc dòng vừa sửa).
2. Kiểm tra chéo giữa `camera`, `storyboard`, `timeline_action`, `speech`, `props_lock`, và `negative_constraints` để đảm bảo không có hai câu nào tự mâu thuẫn (về tay trái/phải, vị trí trái/phải của lan can, số cú cắt cảnh, trạng thái đứng yên hay di chuyển của máy quay).
3. Chạy `python tools/lint_prompt.py` đạt `errors=0` trước khi trình User duyệt.
