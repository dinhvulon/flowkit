---
description: Use after writing or editing any FlowKit video_prompt or Storyboard 2x2 image_prompt (prompt*.json, storyboards*.json, POST/PATCH /api/scenes) and before asking the user to approve generation. Checks the prompt against /fk-film, /fk-storyboard, /fk-camera-guide, /fk-action-choreography, /fk-cinematic-transitions, and the sw-* screenwriting & dialogue rules (Rule 49/54/67/69/72/74).
---

# fk-review-prompt — Kiểm Toán & Tự Đánh Giá Prompt Phim Điện Ảnh Trước Khi Duyệt / Sinh

Chạy bắt buộc sau **mỗi lần** viết hoặc sửa `video_prompt` hoặc `image_prompt` của Storyboard 2×2 / Turnaround Sheet, trước khi hỏi User duyệt sinh (Rule 29, Rule 68). Thực thi đầy đủ Mục B và Mục D của [`skills/fk-film/references/prompt-lock.md`](fk-film/references/prompt-lock.md).

Usage: `/fk-review-prompt <prompts_actX.json | scene_id>`

---

## Bước 1 — Chạy Công Cụ Kiểm Toán Tự Động (`tools/lint_prompt.py`)

```bash
python tools/lint_prompt.py output/<slug>/prompts_act1.json
# Hoặc kiểm tra trực tiếp 1 scene trong DB:
python tools/lint_prompt.py --scene <scene_id>
```
Bắt buộc đạt **`0 CRITICAL / 0 HIGH` (`errors=0`)**.

---

## Bước 2 — Đọc Lại Toàn Bộ Prompt & Kiểm Tra Chéo Không Tự Mâu Thuẫn

Đọc toàn bộ đối tượng JSON của cảnh từ đầu đến cuối (không chỉ đọc dòng vừa sửa). Gom các câu theo từng chủ thể để kiểm tra không có hai câu nào nói ngược nhau:

| Chủ thể | Vị trí & Không gian (Trong/Ngoài lan can) | Góc máy & Cú cắt (Hard Cut ở giây nào) | Tay trái / Tay phải & Đạo cụ | Khuôn mặt & Khẩu hình |
|---|---|---|---|---|

- Kiểm tra liên tục vật lý với cảnh liền trước và liền sau: hướng nhìn, tư thế, trang phục, đạo cụ, nguồn sáng, kích thước/trọng lượng sinh vật (`CREATURE & PROP SCALE/MASS LOCK`).

---

## Bước 3 — Kiểm Toán 15 Hạng Mục Trong Checklist B (`skills/fk-film/references/prompt-lock.md`)

1. **Máy quay điện ảnh ngôi thứ ba:** `"third-person cinematic camera; the camera itself is never seen"`, ống kính Anamorphic 35mm, khẩu độ `deep focus f/8` (không bokeh, không góc selfie/vlog).
2. **Đủ 13 trường JSON & Nhắc đủ chip `{{ref:...}}` / `{{media:...}}`:** Tối đa 7 refs/cảnh; mọi entity trong `refs` đều có chip inline trong prompt.
3. **Khóa khuôn mặt 1:1 & Trang phục thuần ảnh Ref (Rule 52, 60, 64):** Chỉ trỏ chip `{{ref:<Tên>}}` và `{{ref:<Tên> Body}}`; không tả lại ngũ quan hay quần áo bằng chữ dài dòng.
4. **Chuẩn Turnaround Sheet 16:9 Live-Action / Practical SFX (`/fk-character-design`, Rule 58, 72):** Không có từ khóa 2D (`study`, `sketch`, `concept art`, `drawing`, `illustration`, `CGI render`).
5. **Storyboard 2×2 & `source_media_id` (`/fk-storyboard`, Rule 65, 69):**
   - Cảnh chuyển (Rule 65 Loại 2) dùng `STORYBOARD` 2×2 có `source_media_id` từ ảnh ref có sẵn; cảnh nối tiếp cùng góc máy dùng `PREV_LAST_FRAME`.
   - Prompt video R2V mở đầu `camera.shot_size` bằng `OPENING SHOT (second 0): matching the top-left panel (Panel 1) of {{media:<uuid>|<CLIP> Storyboard.jpg}}` (không cắt `<CLIP> P1` riêng lẻ).
6. **Visual Audit 4 Panel thực tế (Rule 69 (7)):** Khi đã sinh ảnh Storyboard 2×2 sạch, đã đọc trực tiếp 4 panel trên ảnh để chỉnh lại `camera` và `timeline_action` (tay trái/phải, hướng nhìn, bố cục) khớp 100% với ảnh thực tế.
7. **Crisp Hard Cuts & Quy tắc 30°–90° (Rule 74 (1), (5)):**
   - Các panel khác góc máy được chuyển bằng `crisp hard cut` tại đúng mốc giây.
   - Góc máy giữa 2 panel cắt cảnh phải lệch nhau `> 45°–90°`; cấm cắt giữa 2 panel trùng góc nhìn dọc cùng một lan can gây lỗi cắt nửa khung hình / nhân đôi 2 lan can (`SINGLE BARRIER LOCK`).
8. **Cô lập nhân vật & Chống phân thân (`Anti-Cloning Lock` — Rule 74 (2)):**
   - Khi một Shot chỉ quay 1 nhân vật, ghi rõ `Strictly [Character A] alone in this shot; [Character B] is completely off-screen and never seen` và khóa `NO duplicate characters, NO cloning` trong `negative_constraints`.
9. **Chống trộn trục 180° & Khóa không gian Trong/Ngoài lan can (`SPATIAL LOCK` — Rule 74 (3)):**
   - Mỗi Shot chỉ neo theo 1 Panel duy nhất (không gộp `matching Panel 3 and Panel 4` nếu ngược trục); ghi rõ bên nào là sàn tàu/mặt đất bên trong và bên nào là mặt biển/vực bên ngoài.
10. **Ngữ pháp "Chỉ tay ngắn ➔ Cắt cảnh mới lộ mục tiêu" & Cấm ôm mặt (Rule 74 (6)):**
    - Cú máy chỉ tay (`0-2s`/`0-3s`) chỉ quay nhân vật trên boong tàu chỉ ra ngoài khung hình (`off-screen target`), sau đó **Hard Cut** mới lộ chiếc thuyền/ông lão/sinh vật.
    - Nhân vật sợ hãi giữ khuôn mặt lộ rõ 100% (`unobstructed face clearly visible, NO hands on face or cheeks`), hai tay bám chặt mạn thuyền hoặc đạo cụ.
11. **Khóa đồng bộ kích thước & trọng lượng Sinh vật/Đạo cụ (`SCALE & MASS LOCK` — Rule 74 (4)):**
    - Đính ref sinh vật/đạo cụ (như `Omen Fish`) vào `refs` ở mọi cảnh có mặt và khóa kích thước tuyệt đối (`1.7m–1.9m, 80 kg`).
12. **Vật lý 3 pha, Chống CGI & Cấm khói thở trắng (`/fk-action-choreography`, Rule 57, 62):**
    - Có mặt từ giây 0 (`already in place`), một đạo cụ liền mạch (`props_lock`), cấm khói thở trắng (`NO breath smoke`), cấm `god rays`.
13. **Thoại chuẩn `/sw-dialogue` & Rule 49 / 54 / 67:**
    - Khớp nguyên văn `script.md`; đúng dải số từ theo `duration` (4s: 0/6-8; 6s: 12-15; 8s: 18-22; 10s: 24-28); mỗi người nói 1 Voice ID riêng trong `speech.voices`; nói lớn/gắt khi đối đầu hoặc nguy hiểm; không có từ khóa mua bán/tiền bạc.
14. **Đầy đủ `dramatic_craft` từ bộ `sw-*` (`/sw-scene-craft`, Rule 56):**
    - Có đủ `beat`, `value_turn`, `subtext`, `prop_and_detail`.

---

## Bước 4 — Mẫu Báo Cáo Tự Đánh Giá (Gửi Kèm Trước Khi Hỏi User Duyệt Sinh)

```markdown
### Báo cáo tự đánh giá Prompt — <Scene ID / File>
- **Linter (`tools/lint_prompt.py`):** 0 CRITICAL / 0 HIGH (errors=0)
- **Visual Audit & Storyboard 2×2 (Rule 69, Rule 74):** <Khớp 4 panel thực tế, góc cắt >45°-90°, khóa không gian Trong/Ngoài lan can, cô lập nhân vật chống phân thân>
- **Kỹ nghệ Kịch bản & Thoại (`sw-*`, Rule 49):** <Số từ / dải chuẩn, Voice ID, dramatic_craft>
- **Khóa Thực thể & Đạo cụ (`refs`, Scale Lock):** <≤ 7 refs, đủ chip {{media:...}}, đồng bộ kích thước>
- **Kết luận:** Sẵn sàng trình User duyệt sinh | Cần sửa tiếp
```
