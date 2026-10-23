# Bài Học Sản Xuất Phim Điện Ảnh Ngôi Thứ Ba (Narrative Film Production Lessons)

> **Quy chuẩn `/fk-film`:** Toàn bộ bài học dưới đây được đúc kết từ thực chiến sản xuất phim điện ảnh ngôi thứ ba trên Google Flow / Omni Flash R2V. Tuyệt đối không dùng góc máy selfie hay quy tắc vlog. Mọi bài học phải được khóa trực tiếp vào lúc viết `story-bible.md`, `script.md`, `storyboards.json`, và `prompts.json` (kiểm tra qua `prompt-lock.md` và `tools/lint_prompt.py`).

---

## 1. Kiến Trúc Storyboard 2×2 & Đạo Diễn Hình Ảnh R2V (Rule 69, Rule 74)

### Bài học 1 — Cấm sinh Start Frame đơn lẻ; bắt buộc Storyboard 2×2 cho mọi cảnh chuyển (Rule 69)
- Mọi cảnh mở đầu hoặc chuyển cảnh / đổi góc máy (Rule 65 Loại 2) **BẮT BUỘC** sinh 1 tấm **Storyboard 2×2** (`16:9`, chia 4 panel 16:9 theo thời gian: Panel 1 Top-Left, Panel 2 Top-Right, Panel 3 Bottom-Left, Panel 4 Bottom-Right) theo `/fk-storyboard`.
- **Truyền `source_media_id` từ ảnh ref có sẵn:** Khi sinh ảnh Storyboard 2×2 có nhân vật hoặc sinh vật, bắt buộc truyền `source_media_id` = UUID của ảnh ref nhân vật chính / Body / sinh vật có sẵn và nhắc chip `{{ref:...}}` trong `image_prompt` để khóa nhận diện 1:1. Cấm sinh text-to-image chay từ con số 0.
- **Bỏ cắt Panel 1 (`<CLIP> P1`):** Omni Flash R2V (`GENERATE_VIDEO_REFS`) vận hành theo cơ chế Pure References. Tấm Storyboard 2×2 đã tẩy watermark là bản thiết kế thời gian cho cả clip.
- **Cảnh nối tiếp trực tiếp (Rule 65 Loại 1 — Chain):** Cấm sinh ảnh mới; cắt khung cuối của clip trước đã duyệt (`PREV_LAST_FRAME`), tẩy logo và upload lấy UUID sạch.

### Bài học 2 — Visual Audit: Đọc thể ảnh Storyboard thực tế trước khi sinh video (Rule 69 (7))
- Sau khi sinh ảnh Storyboard 2×2, tải về, chạy `tools/remove_watermark_from_image.py`, xóa file gốc còn logo, upload bản `_clean.jpg` lấy UUID mới.
- **BẮT BUỘC đọc trực quan 4 panel thực tế** trên ảnh vừa sinh (cỡ cảnh, hướng nhìn, tay trái/phải, vị trí lan can/vật cản, biểu cảm) để **điều chỉnh lại `video_prompt`** (`camera.shot_size`, `camera.description`, `timeline_action`, `negative_constraints`) khớp 100% với ảnh thực tế trước khi gửi sinh video.

### Bài học 3 — Crisp Hard Cuts theo Storyboard & Cấm gộp một cú máy dolly liên tục (Rule 74 (1))
- Khi 4 panel của tấm Storyboard 2×2 thể hiện các góc máy, cỡ cảnh hoặc nhân vật khác nhau (ví dụ Panel 1: EWS tàu ngoài biển ➔ Panel 2: MS Nora ở mũi tàu ➔ Panel 3: MCU Castor ở boong giữa):
  - `camera.description` và `timeline_action` **BẮT BUỘC** chỉ định rõ các cú cắt gắt (**crisp hard cuts**) tại đúng mốc giây (`At second 3.0, a crisp hard cut matching Panel 2... At second 7.0, a crisp hard cut matching Panel 3...`).
  - **CẤM TUYỆT ĐỐI** viết một cú máy liên tục (`slow tracking dolly shot`) bao trùm từ đầu đến cuối clip khi các panel là các cú máy độc lập.

### Bài học 4 — Cô lập nhân vật trong từng Shot & Chống phân thân / nhân đôi (Rule 74 (2))
- Khi danh sách `refs` / `character_names` có nhiều nhân vật (ví dụ cả Nora và Castor), nhưng một cú máy trong clip chỉ quay **MỘT** nhân vật:
  - Trong `timeline_action`: Ghi rõ `Strictly [Character A] alone in this shot; [Character B] is completely off-screen and never seen`.
  - Trong `negative_constraints`: Bắt buộc khóa `strictly NO duplicate characters, strictly NO multiple [Name], strictly [Character A] alone in shot X, [Character B] never appears in shot X, no ghost figures, no cloning; crisp hard cuts at second X.0, no camera blending, no crossfades`.

### Bài học 5 — Chống trộn trục 180° giữa 2 Panel & Khóa không gian Trong/Ngoài lan can (Rule 74 (3))
- **CẤM viết gộp `matching Panel 3 and Panel 4` trong cùng một Shot** khi 2 panel đó có góc máy đảo chiều hoặc ngược trục Trái/Phải (ví dụ Panel 3 sàn tàu bên trái, biển bên phải; Panel 4 biển bên trái, sàn tàu bên phải). Việc gộp 2 panel ngược trục khiến AI ghép nhân vật của Panel 3 vào nền nước biển của Panel 4 (nhân vật đứng lơ lửng ngoài mặt biển).
- Mỗi Shot chỉ được neo bố cục không gian theo **MỘT Panel duy nhất** (hoặc phải có `crisp hard cut` rõ ràng).
- Mọi cảnh trên boong tàu, mạn thuyền, gờ vực bắt buộc có `SPATIAL LOCK`: chỉ rõ bên nào (`LEFT` hay `RIGHT`) là sàn gỗ bên trong, bên nào là mặt biển bên ngoài (`All characters stand firmly INSIDE the vessel on the solid wooden deck planks, NEVER on the exterior ocean side of the railing`).

### Bài học 6 — Quy tắc 30°–90° khi Hard Cut & Chống cắt nửa khung hình / nhân đôi 2 lan can (Rule 74 (5))
- Khi 2 panel liên tiếp trên Storyboard có **cùng một góc máy và phông nền (`< 30°` thay đổi góc nhìn — Jump Cut)** nhưng vị trí lan can/tường chắn dịch ngang, bộ giải mã R2V sẽ giữ nguyên nửa khung hình của Panel 1 (Lan can số 1) và dán đè nửa khung hình của Panel 2 (Lan can số 2) vào giữa màn hình ➔ tạo ra **2 dãy lan can song song xẻ đôi con tàu**.
- **Quy tắc bắt buộc:**
  1. Mọi cú `Hard Cut` giữa các panel phải thay đổi góc máy hoặc cỡ cảnh **tối thiểu `45°–90°`** (ví dụ: trên boong tàu nhìn ngang ➔ cắt góc 90° từ trên cao nhìn thẳng xuống lòng thuyền nhỏ).
  2. Không bao giờ cắt giữa 2 panel trùng góc máy dọc cùng một mạn tàu; kèm câu khóa `SINGLE BARRIER LOCK: Strictly ONE single continuous wooden railing; NEVER two parallel railings, NEVER a split railing down the middle of the frame, NEVER a half-frame cut`.

### Bài học 7 — Ngữ pháp "Chỉ tay ngắn ➔ Cắt cảnh mới lộ mục tiêu" & Cấm ôm mặt kịch cỡm (Rule 74 (6))
- **Tách riêng cú máy chỉ tay (`Point Shot`, ngắn 2–3s) và cú máy lộ mục tiêu (`Reveal Shot`)**: Khi nhân vật trên boong tàu/vách đá chỉ tay phát hiện mục tiêu ở xa/dưới thấp (thuyền nhỏ, sinh vật, hòn đảo), **TUYỆT ĐỐI KHÔNG nhồi cả người chỉ tay trên boong tàu lẫn chiếc thuyền/ông lão dưới biển vào chung một khung hình** (làm sai tỷ lệ phối cảnh và khiến tay chỉ lệch lên trời). Cú máy chỉ tay chỉ quay nhân vật trên boong chỉ tay dứt khoát về phía màn sương ngoài khung hình (`off-screen target`), sau đó **Hard Cut** sang cú máy tiếp theo mới lộ diện chiếc thuyền và ông lão.
- **Cấm tư thế ôm mặt / bưng má kịch cỡm (`NO HANDS ON FACE/CHEEKS`)**: Khi mô tả nhân vật sợ hãi hoặc kinh hoàng, **CẤM** viết `"hands pressed against his face/cheeks"` (khiến AI vẽ nhân vật ôm má há hốc mồm giả tạo và che khuất mặt). **BẮT BUỘC** giữ khuôn mặt lộ rõ 100% (`unobstructed face clearly visible`), diễn tả nỗi sợ qua ánh mắt và cơ mặt điện ảnh (`wide bloodshot eyes frozen in dread, jaw trembling`), hai tay bám chặt vào mạn thuyền hoặc đạo cụ (`hands gripping the wooden gunwale planks at his sides`).

---

## 2. Thiết Kế Nhân Vật, Sinh Vật & Đạo Cụ Tham Chiếu (Rule 46, 58, 60, 64, 72, 74 (4))

### Bài học 8 — Chuẩn Turnaround Sheet 16:9 chụp người thật 35mm / Practical SFX qua `/fk-character-design` (Rule 58, Rule 72)
- Mọi ảnh reference cho nhân vật chính/phụ và sinh vật chủ chốt **BẮT BUỘC 100%** tạo bằng skill `/fk-character-design`:
  - **Nhân vật:** Character Sheet 16:9 chuẩn 4 góc (Full-body Front, Full-body 3/4, Full-body Side Profile, Portrait Close-up) hoặc `<Tên>` (chân dung mặt) + `<Tên> Body` (3 góc đã mặc hoàn chỉnh trang phục thời kỳ theo Rule 46). Phải là **ảnh chụp người thật 35mm (Live-Action Casting Photo)**.
  - **Sinh vật / Quái thú:** Creature Turnaround Sheet 16:9 chuẩn 3 panel (3/4 trái, 3/4 phải, cận cảnh đầu/sọ nhìn từ phía có dấu sẹo/sừng gãy bất đối xứng). Phải là **mô hình practical animatronic / SFX vật lý trên phim trường 35mm**.
- **CẤM TUYỆT ĐỐI** các từ khóa kích hoạt tranh vẽ 2D/phác thảo: `study`, `character study`, `comparative study`, `sketch`, `sketchbook`, `concept art`, `drawing`, `illustration`, `line art`, `anime`, `cartoon`, `CGI render`, `3D model`, `wax statue`.

### Bài học 9 — Khóa nhận diện khuôn mặt 1:1, khóa trang phục thuần ảnh Ref & Chip `{{media:...}}` (Rule 60, 64)
- Mọi ảnh ref đính kèm trong `refs` phải được nhắc trực tiếp trong `video_prompt` bằng chip `{{ref:<Tên Entity>}}` (được resolve thành `{{media:<uuid>|<filename>}}` khi lưu DB).
- Không tả lại màu sắc hay chi tiết quần áo bằng văn bản dài dòng trong `video_prompt` (tránh AI tự vẽ biến thể trang phục); chỉ khóa: `"[Name]'s face and hair are an exact 1:1 match to {{ref:<Name>}}, and his/her body proportions and wardrobe match {{ref:<Name> Body}} with zero outfit variations."`

### Bài học 10 — Khóa đồng bộ kích thước & trọng lượng Sinh vật / Đạo cụ xuyên suốt các cảnh (`CREATURE & PROP SCALE/MASS LOCK` — Rule 74 (4))
- Khi một sinh vật hoặc đạo cụ chủ chốt có ảnh ref (ví dụ `Omen Fish`), bắt buộc:
  1. Đưa tên entity đó vào `refs` / `character_names` của **MỌI cảnh** có mặt thực thể đó.
  2. Khóa cứng thông số vật lý tuyệt đối kèm thước đo so sánh trực quan trong cả `image_prompt` của Storyboard lẫn `video_prompt`: ví dụ `strictly 1.7 to 1.9 meters (1.8m) long and 80 kg heavy—as long as an adult human with a thick 45cm body girth, spanning the entire length of the wooden skiff floorboards or end-to-end across the full 2-meter oak dissection table; strictly NEVER a small 50cm-100cm fish, NEVER a handheld parcel`.
  3. Không mô tả vật thể nằm bên trong bụng sinh vật (`"cylindrical shape bulging beneath the scales"`) ở các cảnh chưa mổ bụng vì AI sẽ vẽ một ống kim loại dán lộ thiên bên ngoài vảy.

### Bài học 11 — Một đạo cụ liền mạch & Cấm tự sinh/biến mất giữa clip
- **Có mặt từ giây 0 (`already in place`):** Mọi người, sinh vật và đạo cụ xuất hiện trong clip phải được khai báo vị trí cụ thể từ giây 0 (hoặc ngay tại đầu Shot sau cú Hard Cut).
- **Một tay — Một đạo cụ:** Đạo cụ cầm tay (dao găm, cuộn da cừu, đèn bão) giữ cố định ở một tay, tối đa 2 trạng thái/clip; kèm `props_lock` đếm số lượng chính xác (`exactly ONE bronze dagger in her right hand, never duplicates, never vanishes`).
- **Một sợi dây liền khi hai người cùng cầm:** Ghi rõ `exactly ONE single continuous unbroken rope/strap`, chỉ định rõ ai cầm đầu nào, cấm đứt hoặc tách đôi.

---

## 3. Cơ Học Vật Lý, Chất Liệu Sinh Học & Chống CGI (Rule 57, 59, 62)

### Bài học 12 — Động lượng vật lý $p = m \cdot v$, truyền lực qua vật cản & Cấm phanh ABS
- Sinh vật khổng lồ hoặc tàu thuyền nặng hàng chục tấn phải tuân theo quán tính $p = m \cdot v$: lao chéo 3/4, trượt cày bùn/nước có độ trễ thứ cấp (bờm, vây, dây buồm văng trễ nhịp), cấm dừng khựng tức thì như phanh ABS, cấm xoay 360°.
- Truyền lực qua cấu trúc vững chắc (`force -> hull/timber barrier -> ocean/ground`), không để cơ thể người đỡ trực tiếp lực va chạm hàng tấn.

### Bài học 13 — Chất liệu sinh học sần sùi, cấm khói thở trắng & Deep Focus `f/8` (Rule 57, 62)
- Da sinh vật/quái thú phải là biểu bì sinh học thô ráp không bóng nhựa (`non-reflective pachyderm/chitinous hide, mud-caked skin folds, chipped keratin, battle scars`).
- **CẤM TUYỆT ĐỐI khói thở trắng / sương khói từ mũi miệng (`strictly NO breath smoke, NO white steam plumes, NO nostril vapor`)** và cấm tia nắng giả tạo (`strictly NO volumetric god rays, NO studio rim lighting`).
- Khóa khẩu độ `deep focus f/8` để hậu cảnh và tiền cảnh đều rõ nét thực tế, chống xóa phông bokeh giả tạo.

---

## 4. Đối Thoại Điện Ảnh, Nhịp Độ & Kiểm Toán Âm Thanh (Rule 49, 54, 67)

### Bài học 14 — Đa giọng nói Pinhole, nói từ giây 0 & Khóa miệng người nghe (Rule 49, 54)
- Mỗi nhân vật có thoại dùng một Voice ID riêng trong `speech.voices` (`voice-bible.md` §0).
- Số từ tiếng Anh khớp cứng thời lượng clip: **4s = 0 hoặc 6–8 từ**; **6s = 12–15 từ**; **8s = 18–22 từ**; **10s = 24–28 từ**.
- Mặt người nói phải lộ rõ trong khung hình ngay lúc mở lời; người không nói phải khóa chặt môi (`mouth stays firmly closed`).
- **Không nhắc tên vật thể/mối nguy chưa xuất hiện trong câu thoại** nếu không muốn AI vẽ ngay vật thể đó vào khung hình.
- **Tránh từ khóa mua bán/tiền bạc (`pay`, `buy`, `dollars`, `gold coins`)** khi có nhân vật trẻ để không kích hoạt bộ lọc chặn ngầm (ghost op) của Flow.
- **Lời qua bộ đàm / tiếng vọng ngoài hình:** Để ở `post_vo` (ghép khi dựng hậu kỳ), không viết vào thoại trên hình của clip im lặng.

### Bài học 15 — Ngữ điệu thoại trong vùng nguy hiểm và khi tranh cãi
- Trong cảnh bão tố, cháy nổ, chiến đấu hoặc tranh cãi căng thẳng, không được để giọng đọc bình thản (`natural pace`). Bắt buộc ghi rõ trong `speech.delivery` và nhịp timeline: `"shouted fast, loud and sharp over the roar, urgent, clipped, forceful, no pauses, never calm, never a normal talking voice"`, kết hợp trạng thái cơ thể căng thẳng.

---

## 5. Vận Hành Pipeline FlowKit, 24-Frame Review & Hậu Kỳ (Rule 10, 18, 28, 67, 73)

### Bài học 16 — Nhịp gửi request 45–60s & Xử lý Ghost Op
- Mọi request gửi tới Google Flow cách nhau ngẫu nhiên **45–60 giây** (server tự điều tiết qua `/api/requests/batch`). Dừng ngay khi gặp `PUBLIC_ERROR_UNUSUAL_ACTIVITY` hoặc `QUOTA` và chạy `/fk-doctor`.
- Nếu một cảnh bị "ghost op" (poll báo xong ngay nhưng không trả về media) 2 lần liên tiếp: kiểm tra và làm sạch từ khóa nhạy cảm trong thoại/hành động trước khi gửi lại.

### Bài học 17 — Quy trình bất khả xâm phạm: 720p Raw ➔ 24-Frame Contact Sheet + Whisper Review ➔ User Duyệt ➔ Upscale 1080p ➔ Tẩy Logo (Rule 18, 32, 67, 73)
1. Khi video 720p sinh xong, tải ngay về `${OUTDIR}/scenes/`. **TUYỆT ĐỐI CHƯA XÓA LOGO Ở BƯỚC NÀY.**
2. Dùng `ffmpeg` trích xuất **đúng 24 frames** phân bổ đều theo thời lượng (`fps=24/<duration>`, ví dụ 10s: `fps=2.4`, 8s: `fps=3.0`) và ghép thành **Contact Sheet 6×4 (`tile=6x4`)** (Rule 73).
3. Chạy `python tools/review_dialogue.py` (Whisper, Rule 67) kiểm tra khớp thoại 100% và chấm bảng AI Review Scorecard 6 tiêu chí trên 24 frames.
4. **DỪNG chờ User duyệt từng cảnh.** Cảnh nào đạt và được User duyệt mới gửi lệnh `UPSCALE_VIDEO` lên 1080p, tải về `${OUTDIR}/1080/`, rồi chạy `remove_watermark_video` trực tiếp trên bản 1080p trước khi đưa vào dựng hậu kỳ (`/video-editing`, `/fk-capcut-edit`, `/fk-sound-design`).
