---
name: fk-storyboard
description: "Storyboard-anchored film clips: sinh 1 ảnh storyboard 2×2 (4 khoảnh khắc theo thời gian, mỗi panel 16:9), cắt panel 1 làm khung mở đầu, rồi sinh video Omni r2v 4/6/8/10s đi đúng theo storyboard, kể cả đổi góc máy / cắt cảnh / dolly bên trong một clip. Dùng cho phim kể chuyện (/fk-film), ngôn ngữ điện ảnh (không phải vlog). BẮT BUỘC cho mọi clip phim có sinh ảnh (Rule 69, 22/10/2026) — không sinh start frame đơn lẻ cho phim. Dùng ngay khi user nói storyboard, panel, khung neo, 'video đi theo storyboard', clip 10s có chuyển cảnh hoặc đổi góc máy, hoặc khi một hành động khó (cứu người, vật nặng, ngã, đánh nhau, chạy trốn) đã sinh hỏng 2 lần trở lên dù prompt đúng."
---

# fk-storyboard — Clip phim neo bằng storyboard theo thời gian

Một clip 6–10s có nhiều nhịp hoặc nhiều góc máy thường hỏng vì model chỉ thấy **khung đầu** và phải tự đoán phần còn lại. Skill này đưa cho model **cả kế hoạch bằng hình**: một ảnh storyboard 2×2, bốn panel là bốn mốc thời gian của chính clip đó. Panel 1 cắt ra làm khung mở đầu; cả tấm storyboard đi kèm làm ref để model biết clip phải đi qua đâu và kết thúc ở đâu.

Đây là **ngôn ngữ phim**, không phải vlog: được cắt cảnh, đổi cỡ cảnh, dolly, đổi ống kính, slow-motion trong một clip.

**Chất liệu mặc định = cinematic (user 21/10/2026: "chất liệu cinematic, đang làm phim")**, không phải chất phim tài liệu. Khối `style` của cả ảnh storyboard lẫn video:

```text
cinematic feature-film look: shot on ARRI Alexa with Cooke S4 prime lenses, fine 35mm film grain, a rich amber-and-teal grade driven by the firelight, deep inky blacks, strong motivated chiaroscuro, thin atmospheric haze catching the light; real people and real materials, not CGI, not a video game
```

Giữ nét sâu (`deep focus, deep depth of field (f/8)`) ở mọi cỡ cảnh: Rule 62 cấm xóa phông và `tools/lint_prompt.py` báo HIGH (`BOKEH_VIOLATION`) nếu prompt có shallow depth of field / bokeh. Vẫn giữ các khóa vật liệu của `/fk-film` (lửa, da, gỗ, khói không thành CGI).

Skill chạy **bên trong** `/fk-film` (bước 5–8). Mọi luật của `/fk-film` và `CLAUDE.md` vẫn áp: hỏi trước mỗi lần sinh (Rule 29), prompt JSON + linter + `/fk-review-prompt` (Rule 55, 68), Whisper khi review (Rule 67), tẩy logo trước khi dùng ảnh (Rule 28).

## Khi nào dùng

- Clip cần **đổi góc máy hoặc cắt cảnh bên trong** (rộng → cận chân, OTS → phản ứng).
- Hành động **nhiều nhịp** mà khung đầu không mô tả được kết thúc (vật được nhấc rồi người thoát ra, ngã rồi đứng dậy).
- Một clip đã **hỏng ≥ 2 lần** vì model không đi tới trạng thái cuối.

**Bắt buộc trong phim (user lock 22/10/2026, CLAUDE.md Rule 69):** trong `/fk-film`, **mọi clip có sinh ảnh** (clip chuyển cảnh, Rule 65 Loại 2, kể cả clip một nhịp, một góc, 4s) đều làm bằng storyboard 2×2 theo skill này. Không sinh một ảnh start frame đơn lẻ (`GENERATE_IMAGE` 1 khung) cho clip phim nữa. Ngoại lệ duy nhất: clip liên tục (Rule 65 Loại 1) vẫn mở bằng khung cuối của clip trước đã duyệt, không sinh ảnh. Ba trường hợp trên vẫn là lý do quan trọng nhất; clip dễ dùng storyboard đơn giản (cùng một máy ở cả 4 panel).

## Điều đã biết (thử thật EMBERS BN-08b, 21/10/2026)

| Phát hiện | Hệ quả |
|---|---|
| Storyboard 2×2 làm ref trong r2v **không bị rò lưới** vào video (một khung liền, không vạch chia) khi prompt có câu khóa "storyboard theo thời gian" | Dùng được an toàn |
| Model **bám mốc thời gian** của panel (nhịp nhấc ở ~3s, co gối ở ~6s) tốt hơn hẳn chỉ có chữ | Mỗi panel = một mốc, ghi giây trong prompt |
| Model vẫn **không làm được động tác khó về hình học** (rút chân lùi qua dưới vật nằm ngang) dù panel vẽ đúng | Chọn hành động model làm được: vật **rơi / lăn / bị đẩy ra**, người **bước / ngã / quay** — không bắt chi luồn ngược dưới vật |
| Chữ **"hard cut"** trong prompt **i2v** bị ghost op 2/2 lần; cùng clip viết thành **dolly liền** thì chạy 75s | Cắt cảnh chỉ dùng với **r2v**; i2v thì dùng chuyển động máy liên tục |
| Panel nằm cạnh nhau 3 cột thì mỗi panel là **ảnh dọc**, không làm khung 16:9 được | Luôn dùng lưới **2×2**, mỗi panel tự là 16:9 |
| Model ảnh vẽ panel cuối dễ "quay về" trạng thái đầu | Panel 4 tả bằng vị trí cụ thể trong khung ("cả hai giày nằm trên rơm phía SAU xà") và nhắc lại trạng thái cuối trong prompt video |
| i2v Omni hay **nhảy zoom ~1s đầu** | Khi dựng cắt bỏ phần đó, hoặc dùng r2v với khung mở đầu là ref |

## Quy trình

### Bước 1 — Kế hoạch 4 panel (chưa tốn credit)

Chia clip theo bảng Rule 49 rồi đặt **4 panel ở các mốc biên**:

| `duration` | Mốc panel | Đoạn timeline |
|---|---|---|
| 4s | 0s · 1s · 3s · 4s | `0-2s / 2-4s` (user 22/10/2026) |
| 6s | 0s · 2s · 4s · 6s | `0-2s / 2-4s / 4-6s` |
| 8s | 0s · 3s · 6s · 8s | `0-3s / 3-6s / 6-8s` |
| 10s | 0s · 3s · 7s · 10s | `0-3s / 3-7s / 7-10s` |

Mỗi panel ghi: **cỡ cảnh + góc + ống kính** (theo `/fk-camera-guide`), ai ở đâu trong khung (trái / giữa / phải, trước / sau vật), trạng thái tay / chân / đạo cụ, ánh sáng. Giữa hai panel ghi **cách chuyển**: giữ máy, dolly, pan, cắt thẳng (chỉ r2v), cắt khớp động tác.

Kiểm trước khi viết prompt:
- Luật 180°: người A luôn một phía màn hình giữa các panel.
- Hướng màn hình của phim (ví dụ EMBERS: về chỗ an toàn = phải → trái).
- Mọi người / vật / đạo cụ dùng ở panel sau phải **có mặt ở panel 1** (Bài 48).
- Hành động thuộc loại model làm được (bảng trên). Nếu không, đổi hành động trước, đừng hy vọng prompt cứu.

Trình bảng 4 panel cho user duyệt.

### Bước 2 — Sinh ảnh storyboard (dùng ảnh ref có sẵn, bắt buộc truyền `source_media_id` — Rule 69 (8), User Lock 22/10/2026)

> **BẮT BUỘC TRUYỀN `source_media_id` TỪ ẢNH REF CÓ SẴN (CẤM SINH TEXT-TO-IMAGE TỪ SỐ 0):**
> Khi submit request sinh ảnh Storyboard cho bất kỳ cảnh nào có nhân vật, request (`GENERATE_IMAGE` hoặc `REGENERATE_IMAGE`) **BẮT BUỘC phải truyền `source_media_id` = UUID của ảnh ref nhân vật chính có sẵn** trong dự án (`<Character>` hoặc `<Character> Body` hoặc bối cảnh, ví dụ: `source_media_id: nora_media_id`):
> ```json
> {"type": "REGENERATE_IMAGE", "scene_id": sid, "source_media_id": nora_media_id, "project_id": pid, "video_id": vid, "orientation": "HORIZONTAL"}
> ```
> Tác dụng: Google Flow đưa `source_media_id` vào `base_media_id` / `target_asset`, gán trực tiếp thẻ ảnh ref của nhân vật vào khung vẽ (`BASE_IMAGE`), ép Imagen 3 phải bám chặt nhận diện ngũ quan, tóc, màu da, tỷ lệ cơ thể và trang phục gốc của nhân vật. **CẤM TUYỆT ĐỐI gửi request sinh ảnh storyboard mà không có `source_media_id`**, khiến AI tự vẽ nhân vật ngẫu nhiên làm biến dạng, vẽ sai mặt hoặc sai giới tính!


Mẫu prompt (thay phần `< >`; chip ref theo Rule 64):

```text
A film storyboard sheet, 16:9, made of FOUR photographic panels in a 2 by 2 grid, separated by thin straight black gutters; each panel is itself a 16:9 frame; no text, no numbers, no arrows, no captions anywhere. All four panels are cinematic feature-film stills (the style block above) of ONE continuous moment in <place>, the same people, clothes, light and scale in every panel: <location chip + light>; <character A>, wearing <...>, face exactly the face in <chip>; <character B> ...
TOP-LEFT PANEL, second 0: <shot size, angle, lens>. <exact positions and state>.
TOP-RIGHT PANEL, second <t2>: <camera, or "same camera">. <state>.
BOTTOM-LEFT PANEL, second <t3>: <camera>. <state>.
BOTTOM-RIGHT PANEL, second <t4>: <camera>. <final state in concrete frame positions>.
Not a 3D render, not CGI, no watermark, no logos.
```

- Đính ref: ảnh bối cảnh hoặc khung cuối clip trước (giữ đúng nơi và ánh sáng), mặt các nhân vật, ref đạo cụ dễ sai màu (balo, mũ). Không đính ref có sẵn thứ không muốn thấy (ví dụ sheet ngựa có dây khớp khi đầu ngựa phải trần).
- Ghi trang phục bằng động từ "wearing" (linter bắt lỗi `INDIRECT_PROP_DESCRIPTION`).
- Sinh qua một scene phụ (`REGENERATE_IMAGE` dùng `image_prompt` của scene) để không đè ảnh của scene chính.
- Chấm từng panel. Panel 1–3 đúng mà panel 4 sai vẫn dùng được nếu prompt video nhắc lại trạng thái cuối; panel 1 sai thì sinh lại.

### Bước 3 — Tẩy logo và upload tấm Storyboard (User Lock 22/10/2026: R2V là pure references, BỎ cắt Panel 1 / Start Frame)

> **BỎ YÊU CẦU CẮT PANEL 1 / START FRAME (User Lock 22/10/2026: "chỗ nào yêu cầu start frame thì bỏ đi"):**
> Chế độ sinh video `GENERATE_VIDEO_REFS` (RPC `MZZa6b` - Omni Flash `abra_r2v`) trong Google Flow hoàn toàn là chế độ **Tham chiếu (Pure References / Ingredients)**, không có tham số Start Frame (`start_image_media_id`). Tấm Storyboard 2x2 tự thân đã là bản thiết kế thời gian (Time Reference) cho cả clip. **TUYỆT ĐỐI BỎ bước cắt Panel 1**: không cần cắt P1 làm Start Frame, không cần entity `<CLIP> P1`.

```bash
python tools/remove_watermark_from_image.py "<sheet>.jpg"
rm "<sheet>.jpg"   # Rule 28: có bản _clean thì xóa ảnh gốc còn logo
```

Upload `<sheet>_clean.jpg` (`POST /api/flow/upload-image`), tạo entity `location`: `<CLIP> Storyboard`, link vào project.

### Bước 3.5 — Đọc thể ảnh Storyboard thực tế & tinh chỉnh Video Prompt (Visual Audit of Storyboard Sheet — BẮT BUỘC, User Lock 22/10/2026)

Sau khi có ảnh storyboard sạch, BẮT BUỘC mở ảnh lên để quan sát và phân tích thể ảnh thực tế của 4 panel:

1. **Panel 1 (Top-Left, mốc 0s)**: Kiểm tra cỡ cảnh thực tế AI đã vẽ (Close-up, Medium, Wide...), hướng nhìn của nhân vật, bố cục và ánh sáng. Đây là góc mở đầu video.
2. **Panel 2 (Top-Right, mốc t2), Panel 3 (Bottom-Left, mốc t3), Panel 4 (Bottom-Right, mốc t4)**: Đọc chính xác góc máy, bố cục và hành động thực tế mà AI đã vẽ ra ở các mốc thời gian (ví dụ: máy tĩnh, dolly tiến lại gần, lia sang phải, hay cắt góc sang cận cảnh).
3. **Điều chỉnh Video Prompt theo thể ảnh thực tế**:
   - Khớp `camera.shot_size` mở đầu với Top-Left Panel của Storyboard (`OPENING SHOT (second 0): matching the top-left panel of {{media:<uuid>|<CLIP> Storyboard.jpg}}: ...`).
   - Khớp `camera.movement` và nhịp chuyển cảnh trong `timeline_action`: Nếu thực tế giữa panel 1 và 2 là giữ nguyên góc chỉ đổi tư thế ➔ ghi `The camera holds still` hoặc `subtle slow drift`. Nếu panel 2 là góc nhìn khác hẳn ➔ ghi rõ cú cắt cảnh hoặc dolly/pan tương ứng.
   - Khớp `negative_constraints`: Ghi đúng số lần cắt và mốc giây dựa trên các panel thực tế.
   - Trạng thái cuối ở mốc kết thúc (giây cuối) phải mô tả đúng tư thế/vị trí xuất hiện ở Panel 4 (Bottom-Right).
4. **CẤM TUYỆT ĐỐI**: Không được lấy nguyên video prompt viết sẵn từ trước mà không đọc ảnh storyboard thực tế vừa sinh! Storyboard là bằng chứng thị giác trực quan, prompt video phải được tinh chỉnh để phục vụ và đồng bộ với bằng chứng đó.

### Bước 4 — Prompt video r2v (Nhắc ảnh Storyboard bằng chip inline và chỉ thị đọc đúng từng panel — Rule 69)

Theo khung JSON của `/fk-film` (`prompt-lock.md` khung A), thêm:

- `refs` (≤ 7): `<CLIP> Storyboard`, rồi mặt / Body / đạo cụ quan trọng nhất (không cần `<CLIP> P1`).
- BẮT BUỘC resolve mọi `{{ref:...}}` thành inline media chip `{{media:<uuid>|<file>.jpg}}` trước khi lưu DB và gửi Flow (Rule 64).
- `camera.shot_size` mở bằng `OPENING SHOT (second 0): matching the top-left panel of {{media:<uuid>|<CLIP> Storyboard.jpg}}: ...`, rồi tả chi tiết góc máy mở đầu theo Panel 1.
- `start_frame` ghi rõ: `{"type": "STORYBOARD", "note": "fk-storyboard (Rule 69): reference image {{media:<uuid>|<CLIP> Storyboard.jpg}} is the time reference for the 4 moments in time; pure r2v, no separate start frame."}`.
- Khối `storyboard` với câu khóa trỏ trực tiếp vào chip Storyboard:

```text
TIME STORYBOARD (CRITICAL): the reference image {{media:<uuid>|<CLIP> Storyboard.jpg}} is a STORYBOARD OF FOUR MOMENTS IN TIME from this one clip, NOT a single frame and NOT a layout to draw. Read it left to right, top to bottom: top-left = second 0 (Panel 1), top-right = second <t2> (Panel 2), bottom-left = second <t3> (Panel 3), bottom-right = second <t4> (Panel 4). Use it only as the plan for how the action and the camera unfold; the video is full-frame shots only, never a grid, never split into panels, never black gutters. <Nhắc lại trạng thái cuối bằng vị trí cụ thể khớp Panel 4.>
```

- `timeline_action` đúng các đoạn của bảng bước 1; mỗi đoạn bắt đầu bằng câu đối chiếu panel: `Matching Panel 1 to Panel 2 of {{media:<uuid>|<CLIP> Storyboard.jpg}}: The clip starts matching the top-left panel...`, tiếp theo là `Matching Panel 2 to Panel 3...`, `Matching Panel 3 to Panel 4...`.
- `negative_constraints` thêm: `The video is full-frame shots only: never a grid, never panels, never split screen, never black dividing lines.` Với mỗi lần cắt, ghi đúng số lần cắt và mốc giây.
- PATCH `duration` (thiếu thì ra 10s âm thầm), `character_names` = `refs`, `horizontal_image_media_id` = media của Storyboard.
- Linter 0 Critical/High → `/fk-review-prompt` → báo cáo → hỏi duyệt sinh.

### Bước 5 — Sinh và theo dõi

`GENERATE_VIDEO_REFS`. Nếu scene đã có video, `GENERATE_VIDEO_REFS` bị bỏ qua ("skipped: already completed", trả lại video cũ) — PATCH `horizontal_video_status` = `PENDING` trước rồi mới gửi; không dùng `REGENERATE_VIDEO` cho clip storyboard vì nó đi đường i2v, không phải r2v. Theo dõi theo memory "video ghost timeout":

- r2v chờ tối đa ~8 phút mỗi lần, i2v 5 phút; quá thì đánh FAILED **và đặt `retry_count = 99`** — nếu không, worker coi là "poll timeout", đưa về PENDING và poll tiếp, và `/api/requests/batch` sẽ trả lại chính request cũ thay vì tạo mới.
- Nếu batch trả về id của request cũ → dừng, không tính là một lần thử.
- Tối đa 2 lần ghost mỗi clip, rồi báo user (Bài 54).

### Bước 6 — Review

Trích ~8 khung (đúng các mốc panel + giữa các mốc), đặt **cạnh storyboard** để so từng panel; chạy `tools/review_dialogue.py` (Rule 67); chấm theo `/fk-review-video`. Ghi rõ panel nào đạt, panel nào không; nếu cả storyboard đúng mà video vẫn sai ở cùng một nhịp qua 2 lần → đổi hành động (bước 1), không sinh tiếp.

## Ghi chép

Lưu mọi file trong `output/<slug>/images/` (`<clip>_storyboard.jpg`, `_clean.jpg`, `<clip>_p1.jpg`). Sinh lại storyboard (`_v2`, `_v3`…) thì chuyển bản cũ vào `output/<slug>/images/rejects/` ngay khi có bản mới để so sánh, không xóa (user lock 22/10/2026); trong `images/` chỉ còn bản mới nhất của mỗi clip. Ghi các thông tin vào `scenes_v*.json` của dự án: media id của storyboard và P1, entity tạo ra, điểm từng panel, kết quả video. Lỗi mới → bài học trong `skills/fk-film/references/production-lessons.md` + một dòng checklist B trong `prompt-lock.md`.
