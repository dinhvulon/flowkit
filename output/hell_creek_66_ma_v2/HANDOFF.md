# Handoff — Hell Creek 66 Ma v2 (cập nhật 14/10/2026 ~19:45, tài khoản Google mới)

## Trạng thái

- Kịch bản v2.1 đã duyệt: `story-bible.md`, `script.md`, `outfit.json`, `ref_prompts.json`.
- Đã đổi tài khoản Google. Project cũ (`6cb771f6…`) và toàn bộ media_id cũ không dùng được nữa. Thông tin cũ lưu trong `project_state_old_account.json`.
- Project mới — `project_state.json`:
  - project_id `34396f76-de18-4bb7-8596-d8c78db2c563` (đã đặt làm active project)
  - video_id `bdedcb6c-2fba-4ab5-9c91-4c8cee4d79e1`
  - material `cretaceous_documentary` (đã tạo lại trong DB), omni_flash, allow_voice, Nora = Laomedeia
  - `image_prompt` của mọi entity = prompt trong `ref_prompts.json` (kèm negative); NB = `outfit.json` edit_prompt
- Upload: mặt Nora `3a3b6dbc-a1e5-4045-9713-b878b4bec006` (đã gán vào N), Body trần `b513a211-a468-4ee4-bdb0-8bfd2b7d0d69`.
- Đã sinh đủ 14 ref (1 EDIT + 13 GENERATE), không lỗi. Mọi ảnh đã tải về `refs/`, xóa logo, upload bản sạch và PATCH media_id sạch.
  - Raw/clean id: `ref_clean_log.json`. Request id: `ref_gen_log.json`.
  - NB sạch được copy sang `uploads/nora_body_cretaceous_dressed_clean.jpg`.
- Review board: `python tools/review_server.py 8200` → http://localhost:8200/review_refs

## Kết quả review ảnh ref — 3 vòng (14/10)

Ảnh đang dùng: `refs/<CODE>_clean.jpg`. Các bản cũ lưu trong `refs/r1`, `refs/r2`, `refs/r3`. Media_id lấy theo `ref_clean_log.json`; lịch sử các vòng xem `ref_clean_log_history.json`.

| Mã | Bản dùng | Ghi chú |
|---|---|---|
| N | upload | — |
| NB | vòng 2 | Áo ôm hơn, hông rõ; ngực vẫn nhỏ hơn Body trần (giới hạn của EDIT). Vòng 3 bị loại vì bình mai rùa sang hông phải. Lộ cằm ở panel 1–2. |
| NH | vòng 1 | Tay hơi già, vệt bùn hơi xanh (lỗi nhỏ) |
| BD | vòng 3 | Sừng gãy và sẹo đúng bên trái ở cả 3 panel. Bố cục 2 panel xếp chồng + 1 cận đầu 3/4. Đã tẩy cục bộ 2 chữ số "2" do model tự chèn. Diềm có vài đốm cam nhạt. |
| CG | vòng 2 | Đạt; lưng võng chưa rõ, sừng hơi dài |
| CN | vòng 3 | Đạt; da hơi giống render |
| TR | vòng 3 | Đạt (miệng khép kín, sẹo bên trái) |
| AR | vòng 2 | Đạt |
| ED | vòng 3 | Mỏ vịt đúng; đuôi bị cắt ở mép panel (cả 3 vòng đều vậy) |
| BS | vòng 1 | Đạt |
| IN | vòng 3 | Giới hạn: cánh gấp vẫn vẽ thành tấm tam giác (cả 3 vòng). Chỉ dùng cho cảnh xa. |
| CA | vòng 2 | Đạt; da hơi bóng như cao su, đầu có mào thịt |
| LB / LC / LW | vòng 1 | Đạt; LB và LW có dải cỏ nhỏ |

Lỗi chung: ảnh đã xóa logo còn một vết nhòe nhỏ ở góc dưới bên phải.
Bài học rút ra đã ghi vào skill: production-lessons #93 và prompt-lock B dòng 39.

## Prompt 112 clip (14/10, ~20:10) — đã xong, chờ user duyệt

- `prompts_act1.json` (18) · `prompts_act2.json` (25) · `prompts_act3.json` (32) · `prompts_act4.json` (28) · `prompts_act5.json` (9) = 112 clip; `vn.json` = bản tiếng Việt (hình, beat, thoại EN/VI, số từ).
- Mỗi clip có thêm `start_frame` (EDIT_IMAGE + mặt Nora / GENERATE_IMAGE / PREV_LAST_FRAME), kèm `image_prompt`. Khi gửi `video_prompt` lên Flow thì bỏ khối `start_frame`.
- `lint_prompt.py`: 5/5 file đạt. Đã quét thêm: không có từ thiết bị (kể cả trong negative_constraints), không có trail/grass/red clay, không mô tả ngực. Thoại khớp nguyên văn và đúng số từ §9.
- BODY LOCK mới: hình thể bình thường, ảnh Nora Body là tham chiếu (user 14/10). Script §2.2 đã sửa.
- Bộ build: `scratchpad/hc2/prompts/` gồm `common.py`, `act1..5.py`, `build.py`. Sửa dữ liệu ở đó rồi chạy lại `python build.py`.

## Việc tiếp theo

1. User duyệt prompt (đọc `vn.json` hoặc file JSON).
2. Tạo 112 scene (POST /api/scenes) → PATCH `duration` + `narrator_text` (không tốn credit).
3. Start Frame → cổng duyệt ảnh → video. Chạy clip khó nhất trước (A1-12), mỗi bước đều hỏi trước (Rule 29).

## File

- Script tạm (phiên này): `C:/Users/Admin/AppData/Local/Temp/claude/c--flowkit/7fe7b637-29ac-43f7-8647-8f5f298985c5/scratchpad/hc2/`
  - `setup_project.py`: đã chạy
  - `prompts/`: bộ build prompt 112 clip
  - `revise_r2.py` / `revise_r3.py`: chỉnh prompt cho từng vòng (prompt cũ giữ lại trong `prompt_r1` / `prompt_r2` của `ref_prompts.json` và `edit_prompt_r1` / `_r2` của `outfit.json`)
  - `gen_refs.py`: gửi batch + theo dõi; dừng khi gặp QUOTA/UNUSUAL_ACTIVITY
  - `post_refs.py`: tải ảnh → xóa logo → upload ảnh sạch → PATCH → tạo `review_refs.html`
