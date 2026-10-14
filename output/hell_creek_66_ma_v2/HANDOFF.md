# Handoff — Hell Creek 66 Ma v2 (dừng 14/10/2026 ~17:15)

## Trạng thái

- Kịch bản v2.1 đã duyệt (10 flag): `story-bible.md`, `script.md`, `outfit.json`, `ref_prompts.json`.
- Project FlowKit đã tạo — `project_state.json`:
  - project_id `6cb771f6-3b2d-437a-a2cb-bd6106d43522`
  - video_id `51995d85-cb99-48fc-bbe2-dd532682a8cb`
  - material `cretaceous_documentary`, omni_flash, Nora voice = Laomedeia
- Nora (N) dùng ảnh mặt đã upload `41f6f329-21ac-4862-a899-59c73b664a0f`. Body trần upload `605d6efa-521a-468d-88a4-5847e5cc8f23`.
- Script sinh ref theo đợt và monitor 5 phút **đã dừng**. Đợt 5 (LC, LW) **chưa gửi**.

## Ảnh ref (14)

| Mã | Trạng thái | media_id Flow (ảnh thô, còn logo) |
|---|---|---|
| NB Nora Body (EDIT) | ✅ COMPLETED | 9362d971-1810-4214-8362-d6c7c85ab087 |
| BD | ✅ COMPLETED | beecccad-efe4-4ff8-930f-4933390ba757 |
| CG | ✅ COMPLETED | af75eb7a-3eba-4fe5-a484-3f094606ce7a |
| CN | ✅ COMPLETED | e2f8213e-da1e-4860-9dc6-6b4287514f70 |
| TR | ✅ COMPLETED | 2d79b7e0-c86d-49fe-994d-311dbb517ec0 |
| AR | ✅ COMPLETED | d738c1bd-02e4-4fbb-b612-2be3bef11d7d |
| NH v1 | ❌ UNSAFE_GENERATION (prompt cũ — đã thay bằng prompt sạch trong `ref_prompts.json`) | — |
| ED, BS | ❌ PER_MODEL_DAILY_QUOTA_REACHED | — |
| IN, CA, LB, NH v2 | ⚠️ Lúc dừng còn PROCESSING; worker đang retry vì lỗi QUOTA | — |
| LC, LW | ⏸ chưa gửi | — |

**Nguyên nhân dừng:** hết quota ảnh trong ngày của model (`PUBLIC_ERROR_PER_MODEL_DAILY_QUOTA_REACHED`).

## Tối làm tiếp — theo thứ tự

1. **Pre-flight:** chạy `GET /health` và `GET /api/flow/status`, đồng thời mở sẵn tab flow.google.com.
2. **Kiểm tra 4 request còn treo** (IN `bbf69d8e`, CA `5ee10dd3`, LB `b0e3c249`, NH v2 `566e60f7`) bằng `GET /api/requests/{id}`. Cái nào hết retry vì QUOTA thì để FAILED. Cái nào COMPLETED thì ghi vào `ref_gen_log.json`.
   - `ref_gen_log.json` hiện chỉ có NB…BS. `post_refs.py` chỉ xử lý mã có `status: COMPLETED` trong log, nên phải bổ sung log trước khi chạy.
3. **Xử lý 6 ref đã xong (không tốn credit):** chạy `scratchpad/hc2/post_refs.py`. Script sẽ tải ảnh → `remove_watermark_from_image.py` → upload ảnh sạch → PATCH `media_id` → tạo `review_refs.html`.
   - NB được copy thêm sang `uploads/nora_body_cretaceous_dressed_clean.jpg`.
   - Xem kết quả tại http://localhost:8200/review_refs (cần chạy `python tools/review_server.py 8200`).
4. **User duyệt 6 ref đó.**
5. **Hỏi user trước khi gửi lại** (Rule 29) các ref còn thiếu, tối đa 8 cái: ED, BS, LC, LW, cùng những cái trong IN/CA/LB/NH v2 bị fail.
   - Chỉ gửi khi quota đã reset. Nếu muốn đổi model ảnh thì dùng `/fk-change-model`.
   - Gửi mỗi đợt 3 request song song (user yêu cầu). Gặp QUOTA hoặc UNUSUAL_ACTIVITY thì dừng ngay.
   - Lưu ý: `gen_refs_waves.py` có dừng khi gặp UNUSUAL_ACTIVITY nhưng **chưa dừng khi gặp QUOTA**. Cần thêm `'quota' in err.lower()` vào điều kiện dừng trước khi chạy lại, và sửa `WAVES` chỉ còn các mã thiếu.
6. Sau khi đủ 14 ref:
   - Cập nhật dòng "Ref (14 ảnh)" trong `story-bible.md`.
   - Chạy `/fk-script-to-prompts` cho 112 clip + `lint_prompt.py`.
   - Tạo scenes → Start Frame → cổng duyệt ảnh → video. Mỗi bước đều chờ user đồng ý.

## File

- Script tạm: `C:/Users/ADMINI~1/AppData/Local/Temp/claude/c--flowkit/924dd737-fdc4-4102-9cbc-03a8660cba2c/scratchpad/hc2/`
  - `setup_project.py` (đã chạy)
  - `gen_refs_waves.py`
  - `post_refs.py`
  - `waves.log`
  - Thư mục scratchpad này có thể bị xóa khi sang phiên mới. Nếu mất thì viết lại theo mô tả ở bước 3 và bước 5.
- Log sinh ref: `output/hell_creek_66_ma_v2/ref_gen_log.json`
