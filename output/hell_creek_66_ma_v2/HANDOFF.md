# Handoff — Hell Creek 66 Ma v2

## Cập nhật 16/10/2026 (tài khoản mới — thay phần dưới nếu mâu thuẫn)

- project `946904bf-3e57-4ba2-97bb-9d545d037914` · video `32aa6e3a-02ef-4020-8ae2-7dda0164f18b` · `project_state.json` `scene_ids` = 94 clip (Act 2–5).
- **Act 1:** chốt, không sinh lại — `hell_creek_act1_1080p.mp4`. Đã xóa scene A1 tạm trên project mới.
- **Act 2:** 24/25 clip 720p xong, user đã duyệt. **A2-R3 BỎ HẲN** (timeout lặp lại ~5 lần; A2-R4 có Start Frame riêng nên vẫn liền mạch) → khi concat bỏ qua A2-R3.
- **A2-16:** sinh lại với ref Turtle Shell Flask + SHELL LOCK "mai kín, không thành bát" → `scenes/scene_024_A2-16_749d40ac.mp4` (đã duyệt). Bản cũ hình bát: `scene_041_A2-16_1fc2dfc8_old_bowl.mp4`.
- **Act 3–5:** đang sinh Start Frame (`gen_sf_waves.py act3 act4 act5`); duyệt trên Review Board rồi mới sinh video.
- Số file `scenes/scene_{order:03d}_…` theo thứ tự trong `scene_ids` của project mới (khác số của tài khoản cũ).
- **Sửa thẳng trong JSON, chưa đưa vào `_pipeline/prompts/*.py`** (không sửa .py khi job đang chạy): A2-16 (SHELL LOCK mai kín, `prompts_act2.json`), A3-W3 (`start_frame.image_prompt` bỏ câu "Self-filmed vlog framing", khóa ngồi + 2 tay trong lòng, `prompts_act3.json`). Chạy `build.py` sẽ ghi đè → phải chép sang `act2.py`/`act3.py` trước. Script tạm 5 ảnh/đợt: scratchpad `gen_sf_waves5.py` (WAVE=5, nhận request đang chạy).
- **Lỗi worker:** poll timeout → `processor.py` tự đặt lại PENDING và gửi lại lên Flow (kể cả request đã đặt FAILED tay). Cần sửa khi hàng đợi rảnh (sửa .py làm server khởi động lại).

## Trạng thái nhanh (14/10, tài khoản cũ)

| Hạng mục | Tình trạng |
|---|---|
| Kịch bản v2.1 + prompt JSON 112 clip | ✅ xong; thoại **tiếng Tây Ban Nha Mỹ Latinh (es-419, giọng Mexico City)**, 64/112 clip có thoại (~66% thời lượng) |
| 14 ảnh ref + mặt Nora (tài khoản Google mới) | ✅ xong (bảng review cuối file) |
| 112 scene trên FlowKit | ✅ đã tạo; đã PATCH `duration`, `narrator_text`, `video_prompt`, `image_prompt` |
| Start Frame Act 1 (16 ảnh) | ✅ xong, đã duyệt (`start_frame_approved.json`) |
| Start Frame Act 2–5 (79 ảnh) | ⏸ chưa sinh |
| **Video Act 1 (18 clip)** | 🟢 **17/18 xong (94.4%)** — Đã audit Vision tính liên tục đạt TB 9.18/10. Chỉ còn **A1-03** chờ xác nhận sinh lại. |
| Video Act 2–5 | ⏸ chưa sinh |
| Review video 720p / upscale / concat | 🟢 **Review Board Live**: `http://localhost:8200/` (`review_videos.html`). 17 clip đạt chuẩn, không cần regen clip nào. |

## Định danh

- project `34396f76-de18-4bb7-8596-d8c78db2c563` · video `bdedcb6c-2fba-4ab5-9c91-4c8cee4d79e1` (HORIZONTAL) · material `cretaceous_documentary` · omni_flash · giọng Laomedeia
- `project_state.json`: `scene_ids` (clip_id → scene_id), `character_ids`, uploads (mặt Nora `3a3b6dbc-…`, Body trần `b513a211-…`).
- Tài khoản cũ: `project_state_old_account.json` (không dùng được nữa).

## Video Act 1

| Xong — 720p thô trong `scenes/` (17 clip) | Chưa sinh / Cần chạy lại (1 clip) |
|---|---|
| EST-01, A1-01, A1-02, A1-04, A1-05, A1-06, A1-07, A1-08, A1-09, A1-10, A1-S1, A1-11, A1-12a, A1-12b, A1-12c, A1-13, A1-14 | **A1-03** (request bị timeout/dropped trên Google Flow >60m → đã unblock FAILED, chờ lệnh sinh lại riêng) |

Nhật ký: `video_log.json`. Review Board trực quan: `http://localhost:8200/`. Đã audit tính liên tục toàn diện: 17 clip đều đạt điểm cao (TB 9.18/10), không lỗi morphing, đạo cụ mai rùa và vết thương sinh vật nhất quán 100%. Chưa upscale, chưa xóa logo video (Rule 18).

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
- **Rule 65 — Cảnh liên tục vs Chuyển cảnh (User Lock 15/10/2026):** Cảnh liên tục (Chain/Action sequence/cùng góc nối tiếp): CẤM sinh Start Frame mới từ text (`GENERATE_IMAGE`), 100% cắt Last Frame clip trước bằng `ffmpeg -sseof -0.08`, tẩy watermark, upload làm Start Frame sạch (`PREV_LAST_FRAME`). Chỉ cảnh chuyển (đổi góc POV <-> Selfie, đổi bối cảnh, cutaway) mới sinh Start Frame tĩnh bằng `GENERATE_IMAGE` (có `source_media_id`), tẩy watermark, và chờ user duyệt qua `review_images.html`.

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
