# Handoff — Hell Creek 66 Ma v2 (dừng 14/10/2026 ~23:50)

## Trạng thái nhanh

| Hạng mục | Tình trạng |
|---|---|
| Kịch bản v2.1 + prompt JSON 112 clip | ✅ xong; thoại **tiếng Tây Ban Nha Mỹ Latinh (es-419, giọng Mexico City)**, 64/112 clip có thoại (~66% thời lượng) |
| 14 ảnh ref + mặt Nora (tài khoản Google mới) | ✅ xong (bảng review cuối file) |
| 112 scene trên FlowKit | ✅ đã tạo; đã PATCH `duration`, `narrator_text`, `video_prompt`, `image_prompt` |
| Start Frame Act 1 (16 ảnh) | ✅ xong, đã duyệt (`start_frame_approved.json`) |
| Start Frame Act 2–5 (79 ảnh) | ⏸ chưa sinh |
| **Video Act 1 (18 clip)** | 🟡 **9/18 xong** — bảng dưới |
| Video Act 2–5 | ⏸ chưa sinh |
| Review video 720p / upscale / concat | ⏸ chưa làm (user bảo chưa cần review lúc sinh) |

## Định danh

- project `34396f76-de18-4bb7-8596-d8c78db2c563` · video `bdedcb6c-2fba-4ab5-9c91-4c8cee4d79e1` (HORIZONTAL) · material `cretaceous_documentary` · omni_flash · giọng Laomedeia
- `project_state.json`: `scene_ids` (clip_id → scene_id), `character_ids`, uploads (mặt Nora `3a3b6dbc-…`, Body trần `b513a211-…`).
- Tài khoản cũ: `project_state_old_account.json` (không dùng được nữa).

## Video Act 1

| Xong — 720p thô trong `scenes/` | Chưa sinh |
|---|---|
| EST-01, A1-01, A1-02, A1-04, A1-05, A1-06, A1-12a, A1-12b, A1-12c | **A1-03** (request treo mồ côi: PROCESSING từ 23:03, worker báo 0 active → đã đánh FAILED), A1-07, A1-08, A1-09, A1-10, A1-S1, A1-11, A1-13, A1-14 |

Nhật ký: `video_log.json`. Chưa upscale, chưa xóa logo video (Rule 18). `scenes/` đã mở khỏi `.gitignore` để commit/push.

## Mai làm tiếp — theo thứ tự

1. **Khởi động server.** Server phiên này chạy nền từ Claude nên sẽ tắt khi đóng phiên:
   `cd C:\flowkit; venv\Scripts\python -m agent.main` → `GET /health` phải `extension_connected: true`; mở sẵn tab flow.google.com (đúng tài khoản Google mới).
2. `/fk-doctor` cho A1-03 (PROCESSING mồ côi) trước khi sinh lại (Rule 31).
3. **9 video Act 1 còn lại** (3 cái song song, user chốt 14/10):
   `cd C:\flowkit; python -u output\hell_creek_66_ma_v2\_pipeline\gen_videos.py A1-03 A1-07 A1-08 A1-09 A1-10 A1-S1 A1-11 A1-13 A1-14`
4. Tùy chọn: Start Frame **A1-13, A1-S1, A1-08** còn ánh sáng ngược nhẹ. Hỏi user trước khi sinh lại; nếu sinh lại ảnh thì phải sinh lại cả video tương ứng.
5. **Act 2:** `python -u output\hell_creek_66_ma_v2\_pipeline\gen_sf_waves.py act2` (đợt 3 ảnh) → user xem `http://localhost:8200/review_images` (`python tools\review_server.py 8200`) → thêm id vào `start_frame_approved.json` → `gen_videos.py <clip…>`. Chuỗi 4s `a/b/c` liệt kê theo thứ tự; script tự chờ mắt xích trước.
6. Lặp lại cho Act 3, 4, 5. Trước upscale: review 720p (Rule 32) + user duyệt → upscale 1080p → xóa logo → concat.

## Bộ script — `_pipeline/` (đã sao từ scratchpad để không mất)

| File | Việc |
|---|---|
| `_pipeline/prompts/` | Bộ build prompt: `common.py` (khóa chung, ánh sáng, chip ref, `image_refs`), `act1..5.py` (dữ liệu từng clip), `dialogue_es.py` + `added_lines.py` (thoại es-419), `vi_es.py` (dịch Việt). Sửa xong: `cd _pipeline\prompts; python build.py` → `prompts_act1..5.json` + `vn.json` → `python tools\lint_prompt.py --file …` → `push_prompts.py` |
| `_pipeline/push_prompts.py [clip…]` | `{{ref:Entity}}` → `{{media:uuid\|file}}`; gắn `opening_frame` cho Start Frame đã duyệt; PATCH prompt + narrator_text + duration |
| `_pipeline/gen_sf_waves.py [act1…] [--regen=ID,ID]` | Start Frame theo đợt 3; tự đổi bộ ref ảnh theo `start_frame.image_refs` rồi trả lại; tải → xóa logo → upload → gán; dừng khi QUOTA/UNUSUAL |
| `_pipeline/gen_videos.py clip… [--regen]` | Video R2V 3 cái song song; mắt xích P lấy khung cuối video trước; tiếp nhận request đang chạy (không gửi trùng); tải 720p về `scenes/` |
| `_pipeline/gen_refs.py`, `post_refs.py`, `create_scenes.py` | Đã dùng cho ref và scene; không cần chạy lại |

## Luật & quyết định mới của phiên này (đã ghi vào CLAUDE.md / skill / memory)

- **Rule 64 — chip ảnh ref trong prompt:** nhắc ảnh ref ngay tại câu khóa; gửi lên Flow thành đoạn `[null,[["uuid","file"]]]` (capture thật từ flow.google.com). Code: `agent/services/flow_batch.py` (`prompt_segments`, `mentioned_media_ids`), `agent/sdk/services/operations.py` (R2V tự đính ảnh được nhắc, xếp trước, ≤7). `tools/lint_prompt.py` kiểm định dạng + `start_frame.image_refs`.
- **Bỏ luật tối đa 3 ref** → tối đa 7 (Omni Flash).
- **Không tả lại mặt/makeup/trang phục**: chỉ "exactly as in {{ref}}" + `MAKEUP LOCK: keep her makeup exactly as in {{ref:Nora}}, unchanged`. Hình thể Nora bình thường.
- **Bộ ref khi sinh Start Frame:** có mặt Nora → [Nora, Nora Body, bối cảnh]; chỉ thấy tay → [Nora Hand, bối cảnh] + câu khẳng định "first-person view looking down at her own hands…" (không "female", không "no face"); chỉ thấy chân → tả bằng chữ, chỉ ref bối cảnh; flycam EST → không ref. Lý do: tổ hợp sheet Body không đầu + "no face" bị `UNSAFE_GENERATION` (A1-04/06/09).
- **Ánh sáng:** tự nhiên, không khí trong, không nắng ngược phát sáng/tia sáng (khóa L1–L5 đã sửa; giữ L0 sương bình minh, LG/LT/LD của va chạm).
- **3 video / 3 ảnh một lúc** (memory `request-pacing-45-60s`).
- **Video mở đầu bằng Start Frame đã duyệt:** builder R2V (MZZa6b) không có ô khung đầu → khối `opening_frame` nhắc ảnh Start Frame bằng chip.

## Thay đổi chưa commit

`agent/services/flow_batch.py`, `agent/sdk/services/operations.py`, `tools/lint_prompt.py`, `tests/unit/test_flow_batch.py`, `tests/unit/test_operations.py`, `CLAUDE.md`, `skills/fk-time-travel-vlog/` (SKILL.md, prompt-lock.md, production-lessons.md, flowkit-pipeline.md), `.gitignore`, toàn bộ `output/hell_creek_66_ma_v2/`.
Test: phần mới đạt. 4 test cũ fail từ trước, không do phiên này: `test_flow_client_batch` (r2v/upscale "unported" ×3), `test_operations::test_submits_references_through_the_client`.

## Phụ lục — review ảnh ref (3 vòng, 14/10)

Ảnh đang dùng: `refs/<CODE>_clean.jpg`; bản cũ ở `refs/r1`, `r2`, `r3`; media_id ở `ref_clean_log.json`.

| Mã | Bản dùng | Ghi chú |
|---|---|---|
| NB | vòng 2 | Đúng trang phục; ngực nhỏ hơn Body trần (user chấp nhận, hình thể bình thường) |
| NH | vòng 1 | Tay hơi già (lỗi nhỏ) |
| BD | vòng 3 | Sừng gãy + sẹo đúng bên trái; đã tẩy 2 chữ số "2" tự chèn |
| CG / CN / TR / AR / BS | đạt | — |
| ED | vòng 3 | Đuôi bị cắt ở mép panel |
| IN | vòng 3 | Cánh gấp vẽ thành tấm tam giác; chỉ dùng cảnh xa |
| CA | vòng 2 | Da hơi bóng như cao su |
| LB / LC / LW | vòng 1 | Đạt |
