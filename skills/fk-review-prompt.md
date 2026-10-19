---
description: Use after writing or editing any FlowKit video_prompt (prompt*.json file, POST/PATCH /api/scenes with video_prompt) and before asking the user to approve generation — or when the prompt-review hook says so, or when the user asks to review a prompt.
---

# fk-review-prompt — Tự đánh giá video_prompt trước khi duyệt / sinh

Chạy sau **mỗi lần** viết hoặc sửa `video_prompt`, trước khi hỏi user duyệt sinh. Hook `tools/hooks/prompt_review_hook.py` tự nhắc chạy skill này sau khi ghi file prompt hoặc PATCH scene. Đây là mục D của `skills/fk-film/references/prompt-lock.md` (Bài học 86) dưới dạng một bước có báo cáo.

Usage: `/fk-review-prompt <prompt.json | scene_id> [...]`

## Bước 1 — Linter

```bash
python tools/lint_prompt.py --file <prompt.json>     # hoặc --scene <scene_id>
```

0 CRITICAL / 0 HIGH. Mỗi MEDIUM: sửa, hoặc ghi lý do giữ vào báo cáo.

## Bước 2 — Đọc lại toàn bộ prompt, gom theo thuộc tính

Đọc từ đầu tới cuối (không chỉ đoạn vừa sửa). Lập bảng, mỗi chủ thể (từng nhân vật, từng con vật, khung hình) một dòng; mỗi cột gom **mọi câu** trong `camera`, `setting`, `characters`, `timeline_action`, `motion_choreography`, `physical_realism`, `speech`, `audio`, `negative_constraints` nói về thuộc tính đó:

| Chủ thể | Tốc độ / dáng đi | Hướng | Vị trí trên màn hình theo mốc | Tay / miệng | Trạng thái cuối |
|---|---|---|---|---|---|

Khung hình: cố định hay cầm tay; có rung không; góc nhìn có đổi không.
Mọi ô phải nói cùng một điều. Hai câu ngược nhau = mâu thuẫn → sửa cho khớp, rồi tìm (grep) mọi chỗ khác dùng từ cũ.

## Bước 3 — Checklist B

Chạy hết checklist B trong `skills/fk-film/references/prompt-lock.md` (checklist của phim; các dòng chỉ áp cho POV vlog đã chuyển sang `vlog-archive.md` §4 — chỉ chạy chúng khi dự án là POV vlog). Ghi dòng nào áp dụng và Đạt / Không đạt.

Kiểm thêm ngoài prompt:
- Mọi sinh vật trong khung có entity `creature` với `media_id` UUID và ảnh ref đã duyệt (dòng 57, CLAUDE.md Rule 5).
- `character_names` của scene ≤ 7 ref (giới hạn Omni Flash, Bài học 88); là TÊN entity, không phải UUID.
- `duration` của scene khớp các mốc (10s: `0-3s / 3-7s / 7-10s`).

## Bước 4 — Báo cáo tự đánh giá (bắt buộc, gửi kèm prompt)

```markdown
### Báo cáo tự đánh giá — <scene / file>
- Linter: <0 CRITICAL / 0 HIGH / n MEDIUM — xử lý thế nào>
- Mâu thuẫn tìm thấy: <câu A ↔ câu B → đã sửa thành ...> (hoặc "không có")
- Checklist B áp dụng: <#3 Đạt, #42 Đạt, #58 Không đạt → đã sửa ...>
- Ref / entity: <đủ / thiếu gì>
- Rủi ro còn lại: <điều model hay làm sai dù prompt đúng>
- Kết luận: Sẵn sàng hỏi duyệt sinh | Cần sửa tiếp
```

Có mục "Cần sửa tiếp" → sửa, rồi chạy lại từ Bước 1. Prompt user đã duyệt mà review muốn đổi nội dung → đưa thành danh sách lựa chọn cho user, không tự ghi đè.

## Không làm

- Không gửi lệnh sinh (Rule 29) — skill này chỉ review.
- Không coi "linter qua" là review xong: linter chỉ bắt chuỗi cấm và hai kiểu mâu thuẫn (`SPEED_CONTRADICTION`, `CAMERA_CONTRADICTION`).
