---
description: Use after writing or editing any FlowKit video_prompt or start-frame / storyboard image_prompt (prompt*.json file, POST/PATCH /api/scenes with video_prompt or image_prompt) and before asking the user to approve generation — or when the prompt-review hook says so, or when the user asks to review a prompt. Checks the prompt against /fk-film, /fk-storyboard, /fk-camera-guide (shot choice per beat: /fk-scriptwriter §G, /fk-action-choreography, /fk-cinematic-transitions) and the dialogue rules (sw-dialogue, Rule 49/54/67).
---

# fk-review-prompt — Tự đánh giá prompt trước khi duyệt / sinh

Chạy sau **mỗi lần** viết hoặc sửa `video_prompt` **và** `image_prompt` của start frame / storyboard (kể cả sửa một câu, kể cả prompt EDIT ảnh), trước khi hỏi user duyệt sinh (CLAUDE.md Rule 68). Hook `tools/hooks/prompt_review_hook.py` tự nhắc chạy skill này sau khi ghi file prompt hoặc PATCH scene. Đây là mục D của `skills/fk-film/references/prompt-lock.md` (Bài học 86) dưới dạng một bước có báo cáo.

Usage: `/fk-review-prompt <prompt.json | scene_id> [...]`

Nguồn luật mà review đối chiếu (đọc lại bản hiện hành, không dựa vào trí nhớ):

| Nguồn | Phần kiểm | Bước |
|---|---|---|
| `tools/lint_prompt.py` | Chuỗi cấm, chip `{{ref:}}` / `{{media:}}`, hai kiểu mâu thuẫn | 1 |
| `skills/fk-film/SKILL.md` (bảng "Khóa cứng", "Lỗi hay gặp") + `references/prompt-lock.md` checklist B | Luật phim | 3 |
| `skills/fk-storyboard/SKILL.md` | Ảnh storyboard 2×2 và prompt video r2v đi theo storyboard | 4 |
| `skills/fk-camera-guide.md`, `fk-scriptwriter.md` §G (nhịp cỡ cảnh), `fk-action-choreography.md` (qua `cinematic-toolkit.md` §1), `fk-cinematic-transitions.md`, `fk-film/references/transitions.md`, `shots-and-realism.md` (bảng vật lý; bảng tỉ lệ selfie/POV ở đó chỉ cho vlog) | Chọn cảnh quay theo beat, máy, cỡ cảnh, hướng màn hình, hành động, chuyển cảnh | 5 |
| `/sw-dialogue`, `fk-film/references/voice-bible.md`, Rule 49 / 54 / 67, `script.md` của dự án | Thoại, giọng, số từ, thời điểm nói | 6 |

## Bước 1 — Linter

```bash
python tools/lint_prompt.py --file <prompt.json>     # hoặc --scene <scene_id>
```

0 CRITICAL / 0 HIGH. Mỗi MEDIUM: sửa, hoặc ghi lý do giữ vào báo cáo.

## Bước 2 — Đọc lại toàn bộ prompt, gom theo thuộc tính

Đọc từ đầu tới cuối (không chỉ đoạn vừa sửa). Lập bảng, mỗi chủ thể (từng nhân vật, từng con vật, khung hình) một dòng; mỗi cột gom **mọi câu** trong `camera`, `setting`, `characters`, `storyboard`, `timeline_action`, `motion_choreography`, `physical_realism`, `speech`, `audio`, `negative_constraints` nói về thuộc tính đó:

| Chủ thể | Tốc độ / dáng đi | Hướng | Vị trí trên màn hình theo mốc | Tay / miệng | Trạng thái cuối |
|---|---|---|---|---|---|

Khung hình: cố định hay cầm tay; có rung không; góc nhìn có đổi không; cắt ở giây nào.
Mọi ô phải nói cùng một điều. Hai câu ngược nhau = mâu thuẫn → sửa cho khớp, rồi tìm (grep) mọi chỗ khác dùng từ cũ.

Kiểm vật lý: lực, điểm tựa, trọng lực, hướng đi, vật dùng ở nhịp sau có mặt từ khung đầu (Bài 48), hành động thuộc loại model làm được (vật rơi / lăn / bị đẩy, người bước / ngã / quay — không bắt chi luồn ngược dưới vật nằm ngang). Liên tục với clip trước và sau: tư thế, hướng nhìn, đạo cụ trên người, ánh sáng (Rule 44).

## Bước 3 — Luật phim (`/fk-film`) và Checklist B

Chạy hết checklist B trong `skills/fk-film/references/prompt-lock.md` (checklist của phim; các dòng chỉ áp cho POV vlog đã chuyển sang `vlog-archive.md` §4 — chỉ chạy chúng khi dự án là POV vlog). Ghi dòng nào áp dụng và Đạt / Không đạt.

Kiểm thêm theo bảng "Khóa cứng" của `/fk-film`:
- Prompt là JSON đủ khối (`camera`, `style`, `setting`, `characters`, `timeline_action`, `speech`, `post_vo`, `dramatic_craft`, `audio`, `negative_constraints`, `props_lock`) (Rule 55).
- Máy ngôi thứ ba, máy không bao giờ hiện; không selfie, không ai nhìn vào ống kính.
- Mặt: đúng MỘT câu khóa trỏ vào chip `{{ref:<Tên>}}`, không tả ngũ quan / tóc / makeup bằng chữ, không câu cấm liệt kê bộ phận mặt (Rule 60, 64). Tuổi ≥ 19 và vai trò được ghi.
- Trang phục / đạo cụ trên người: trỏ vào ref Body theo trạng thái và ref đạo cụ (ví dụ EMBERS: "HALE Helmet Goggles"), viết bằng "wearing", không tả lại bằng lời (Rule 46, 52).
- Không gọi tên vật / thú / lửa / thiết bị không muốn thấy, kể cả trong câu phủ định, thoại và `audio` (Bài 73, 77, 99).
- Lời qua bộ đàm / điện thoại / lời dẫn nằm ở `post_vo`, không ở `speech`.

Kiểm thêm ngoài prompt:
- Mọi sinh vật trong khung có entity `creature` với `media_id` UUID và ảnh ref đã duyệt (dòng 57, CLAUDE.md Rule 5).
- `character_names` của scene ≤ 7 ref (giới hạn Omni Flash, Bài học 88); là TÊN entity, không phải UUID; mọi chip trong prompt nằm trong bộ ref này.
- `duration` của scene khớp các mốc (bảng Rule 49: 4s `0-2s / 2-4s`, 6s `0-2s / 2-4s / 4-6s`, 8s `0-3s / 3-6s / 6-8s`, 10s `0-3s / 3-7s / 7-10s`).
- Start frame đúng loại (Rule 65): clip liên tục (cùng nơi, cùng khoảnh khắc, cùng máy, cùng cỡ cảnh) mở bằng khung cuối clip trước đã duyệt, không có `image_prompt`; clip chuyển cảnh trong phim dùng storyboard 2×2 (Rule 69), không có start frame đơn lẻ.

## Bước 4 — Storyboard (`/fk-storyboard`)

Áp cho mọi clip phim có sinh ảnh (Rule 69).

**Prompt ảnh storyboard:**
- Mở bằng câu lưới: 2×2, mỗi panel 16:9, vạch đen mỏng, không chữ / số / mũi tên.
- Bốn panel đúng mốc giây theo `duration`: 4s 0/1/3/4 · 6s 0/2/4/6 · 8s 0/3/6/8 · 10s 0/3/7/10, ghi theo thứ tự đọc chữ Z: TOP-LEFT → TOP-RIGHT → BOTTOM-LEFT → BOTTOM-RIGHT.
- Mỗi panel có cỡ cảnh + góc + ống kính, vị trí từng người (trái / giữa / phải), trạng thái tay / chân / đạo cụ. Giữa hai panel: giữ máy, hay một lần cắt thẳng có chủ ý (cho phép trong storyboard, user 22/10/2026).
- Luật 180°: thứ tự trái → phải của người và vật giữ nguyên qua mọi panel; hướng màn hình của phim đúng (EMBERS: về chỗ an toàn = phải → trái). Dây / ánh nhìn / đầu con vật chỉ cùng hướng ở mọi panel.
- Trang phục, mũ, balo, mũ trùm giữ nguyên trạng thái ở cả 4 panel ("in every panel"); mọi thứ dùng ở panel sau có mặt ở panel 1.
- Đính ref: bối cảnh hoặc khung cuối clip trước, mặt, Body, đạo cụ dễ sai. Không đính ref có sẵn thứ không muốn thấy.

**Prompt video r2v đi theo storyboard:**
- `refs` mở bằng `<CLIP> P1`, `<CLIP> Storyboard`, rồi mặt / Body / đạo cụ (≤ 7). `horizontal_image_media_id` = media của P1. Request là `GENERATE_VIDEO_REFS` (r2v), không phải `REGENERATE_VIDEO` (i2v).
- `camera.shot_size` mở bằng `OPENING FRAME = {{ref:<CLIP> P1}}`.
- Khối `storyboard` có câu khóa "TIME STORYBOARD (CRITICAL): ... STORYBOARD OF FOUR MOMENTS IN TIME ... NOT a single frame" với đúng 4 mốc giây theo `duration`, và nhắc lại trạng thái cuối bằng vị trí cụ thể khớp panel BOTTOM-RIGHT.
- `timeline_action` đúng các đoạn Rule 49; mỗi đoạn mở bằng một câu máy riêng; nội dung từng đoạn khớp panel ở hai đầu đoạn.
- Cắt thẳng chỉ với r2v; `negative_constraints` ghi đúng số lần cắt + mốc giây và câu `The video is full-frame shots only: never a grid, never panels, never split screen, never black dividing lines.`

## Bước 5 — Máy quay (`/fk-camera-guide`)

- Cảnh quay hợp beat (`fk-scriptwriter` §G): mở khu vực mới / địa lý → toàn hoặc toàn rộng; hành động → trung bám theo; đối thoại → hai người → qua vai; cảm xúc / quyết định → cận, đẩy vào; vật quan trọng → cận chi tiết (insert); đe dọa → tele qua vật cản. Ghi beat của clip và vì sao chọn cỡ cảnh đó.
- Hành động nhiều pha theo `cinematic-toolkit.md` §1 (chuẩn bị → một đòn → thu thế); động tác chọn loại model làm được (Rule 69 (4)).
- Mối nối với clip trước / sau theo `fk-cinematic-transitions` + `transitions.md` (match on action, J/L-cut, wipe che khung).
- Mỗi đoạn timeline một hành vi máy (giữ / dolly / pan / tracking / cắt), không hai chuyển động ngược nhau trong một đoạn; tốc độ máy khớp nhịp kịch.
- Cỡ cảnh + ống kính + độ cao máy ghi rõ; deep focus f/8, không bokeh (Rule 62).
- Luật 180° và hướng màn hình giữ đúng trong clip và so với clip trước / sau.
- Không hai clip liền nhau cùng cỡ cảnh + cùng góc máy (Rule 42 (4)); so với clip đứng trước trong timeline.
- Cắt khớp động tác: clip mở đúng tư thế / hướng nhìn mà clip trước kết thúc (Rule 44).
- Người nói ở nhịp nào phải thấy mặt ở nhịp đó (Bài 49).

## Bước 6 — Thoại (`/sw-dialogue`, Rule 49 / 54 / 67)

- Thoại lấy 1:1 từ `script.md` (Rule 56); không tự thêm câu giải thích. Nếu prompt khác script → ghi rõ và hỏi user.
- Số từ đúng `duration`: 4s 0 hoặc 6–8 · 6s 12–15 · 8s 18–22 · 10s 24–28. Ngoại lệ: cảnh rình / ẩn nấp / sinh tử im lặng hoàn toàn (Rule 49 (4)) hoặc phong cách khẩn của dự án (EMBERS lửa: câu ngắn, hét, nhanh) — ghi lý do.
- Mỗi câu nằm trong đúng đoạn thời gian, chia đều các đoạn; câu cuối kết thúc trước giây cuối ~0.5s để không cụt. Nói từ giây 0 thì có câu "From the very first frame at second 0 ..." (Rule 54).
- `speech.voices`: mỗi người nói một voice id (`voice-bible.md` §0), thứ tự nói khớp Slot 7; cách nói (`delivery`) hợp cảnh.
- Chỉ miệng người đang nói cử động; người không thoại khóa miệng; không ai nói thêm ngoài các câu đã ghi; có `(no subtitles)` nếu dự án dùng.
- Thoại không gọi tên thứ không muốn thấy trên hình; không có ý mua bán / trả tiền (Bài 100).
- Nhắc trước: sau khi sinh, review bắt buộc chạy `tools/review_dialogue.py` (Rule 67).

## Bước 7 — Báo cáo tự đánh giá (bắt buộc, gửi kèm prompt)

```markdown
### Báo cáo tự đánh giá — <scene / file>
- Linter: <0 CRITICAL / 0 HIGH / n MEDIUM — xử lý thế nào>
- Mâu thuẫn / vật lý: <câu A ↔ câu B → đã sửa thành ...> (hoặc "không có")
- Luật phim + Checklist B: <#3 Đạt, #42 Đạt, #58 Không đạt → đã sửa ...>
- Storyboard: <mốc panel, thứ tự Z, 180°, trạng thái đồ qua 4 panel, câu khóa video — Đạt / sửa gì> (hoặc "không áp: clip liên tục")
- Máy: <hành vi máy từng đoạn, cỡ cảnh so với clip trước, hướng màn hình>
- Thoại: <số từ / dải chuẩn, khớp script, voice id, thời điểm từng câu>
- Ref / entity: <đủ / thiếu gì, ≤ 7, start frame đúng loại>
- Rủi ro còn lại: <điều model hay làm sai dù prompt đúng>
- Kết luận: Sẵn sàng hỏi duyệt sinh | Cần sửa tiếp
```

Có mục "Cần sửa tiếp" → sửa, rồi chạy lại từ Bước 1. Prompt user đã duyệt mà review muốn đổi nội dung → đưa thành danh sách lựa chọn cho user, không tự ghi đè.

## Không làm

- Không gửi lệnh sinh (Rule 29) — skill này chỉ review.
- Không coi "linter qua" là review xong: linter chỉ bắt chuỗi cấm và hai kiểu mâu thuẫn (`SPEED_CONTRADICTION`, `CAMERA_CONTRADICTION`).
