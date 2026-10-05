# HANDOFF — Neanderthal 51ka (Tập 2: "I Survived 24 Hours with Neanderthals")

**Người nhận:** Agent tiếp nhận dự án (Antigravity IDE / Claude Code).  
**Ngày cập nhật:** 2026-10-05.  
**Tài liệu nền tảng bắt buộc đọc:**
- [CLAUDE.md](file:///c:/flowkit/CLAUDE.md) (Rule 10, 27, 28, 29, 31, 46, 47)
- [skills/fk-time-travel-vlog.md](file:///c:/flowkit/skills/fk-time-travel-vlog.md) (Bài học 34, 40, 47, 55–60)
- [output/neanderthal-51ka/script-v5.md](file:///c:/flowkit/output/neanderthal-51ka/script-v5.md) (Kịch bản chuẩn đã duyệt cấu trúc và danh sách ref `["Nora", "Nora Body", ...]`)
- [uploads/nora_base_body_prompt.json](file:///c:/flowkit/uploads/nora_base_body_prompt.json) & [uploads/nora_body_outfit_prompt.json](file:///c:/flowkit/uploads/nora_body_outfit_prompt.json) (Công thức prompt chuẩn giữ nguyên giải phẫu cơ thể)

---

## 1. Các Quy Tắc Cốt Lõi Bắt Buộc (CRITICAL RULES)

1. **Rule 46 & 47 (User Lock 2026-10-05):**
   - **`Nora Body` chính là ảnh Body đã mặc hoàn chỉnh trang phục**. TUYỆT ĐỐI KHÔNG tạo entity `Nora Outfit` riêng lẻ (entity này đã được xóa khỏi database).
   - Video downstream Omni Flash R2V chỉ nhận: `["Nora", "Nora Body", <NPC/Bối cảnh/Đạo cụ>]`.
   - **TUYỆT ĐỐI KHÔNG gửi ảnh body trần/gym** vào video để tránh nhiễm da thịt trần làm model AI vẽ trang phục generic mất áo.
2. **Rule 29 (Xác nhận trước khi sinh media):**
   - Không được gửi bất kỳ lệnh tạo ảnh/video tốn credit nào (`GENERATE_*`, `REGENERATE_*`) nếu user chưa nói "đồng ý" / "yes".
3. **Rule 28 (Tẩy sạch watermark SynthID trước khi đưa vào sinh video):**
   - Mọi ảnh AI do Google Flow sinh đều phải tải về, chạy `python tools/remove_watermark_from_image.py <path>`, upload lại qua `POST /api/flow/upload-image` để lấy UUID sạch 100%, rồi mới gán vào entity hoặc scene.
4. **Rule 10 (Pacing an toàn tránh Unusual Activity):**
   - Server tự động điều phối giãn cách 45–60s giữa các request gửi đến Flow. Luôn submit batch qua `/api/requests/batch`, không được tự ý spam API loop.
5. **Rule 4 & 43 (Scratch Directory Only):**
   - Mọi script tạm thời, test, debug bắt buộc lưu trong `<appDataDir>/brain/<conversation-id>/scratch/` hoặc chạy inline one-liner `python -c "..."`. Tuyệt đối không tạo file rác trong repo.

---

## 2. Thông Tin Dự Án & Database State (Hiện Tại)

| Thành phần | ID / Giá trị | Ghi chú |
|---|---|---|
| **Project ID** | `4cc4b500-6e3b-4379-96c3-dd18b7412c1a` | Material: `prehistoric_vlog`, `allow_voice: true` |
| **Video ID** | `15076345-ca4a-48cb-8afa-4a79c2a52028` | Orientation: `HORIZONTAL` (16:9) |
| **Scenes** | **Chưa tạo** | Sẽ tạo theo [script-v5.md](file:///c:/flowkit/output/neanderthal-51ka/script-v5.md) |
| **Entity thừa đã xóa** | `Child`, `Nora Outfit` | Đã xóa sạch khỏi DB, không còn xuất hiện trong project |

### Bảng Entity Chuẩn 100% Đã Có UUID Sạch Watermark trong Database:

| Entity Name | Entity ID | Clean Media ID (UUID trong DB) | Nguồn file local | Trạng thái |
|---|---|---|---|---|
| **Nora** (Mặt & tóc) | `f1e93b66-f83f-40d8-bf6e-d22ec444f57e` | `1454fb46-8510-4f14-99fe-8464720632b6` | `uploads/nora_main_clean.jpg` | ĐÃ DUYỆT ✅ |
| **Nora Body** (Body đã mặc outfit v6) | `c58ac1d3-14a9-4169-94a3-681790557d8e` | `ab34e369-d6ed-4c54-9e44-035e2439b704` | `refs/nora_body_v6_clean.jpg` | **USER ĐÃ DUYỆT** ✅ |
| **Leader** (Thủ lĩnh Neanderthal) | `288d06c2-2b2a-4016-9eab-c5d670df67e7` | `f4395dd6-9227-4b8d-8425-8bd71d8027ed` | `refs/leader_clean.jpg` | ĐÃ HOÀN TẤT ✅ |
| **Old Woman** (Bà lão giữ lửa) | `e8a607ed-e207-4be3-806d-f4df489f5a11` | `5a2b982a-5ae8-4124-ada7-dc98df9a59a8` | `refs/old_woman_clean.jpg` | ĐÃ HOÀN TẤT ✅ |
| **Strongest** (Thợ săn to lớn) | `4ae88e7c-997f-4e79-97ee-96a14b3b5d8c` | `10ab07ce-7600-4f73-8697-6cc1a3e09aca` | `refs/strongest_clean.jpg` | ĐÃ HOÀN TẤT ✅ |
| **Strongest Spear** (Ngọn giáo đá lửa) | `ee521059-d0c6-49c2-970b-59353fa87211` | `b508a82a-f410-421a-b6fd-38a1812d1abf` | `refs/strongest_spear_clean.jpg` | ĐÃ HOÀN TẤT ✅ |
| **Cave Hyena** (Linh cẩu hang động) | `680d64bf-c0c3-4cda-9074-d99cef97c12c` | `7559d40f-801e-4821-a685-2c7dded0b1f3` | `refs/cave_hyena_clean.jpg` | ĐÃ HOÀN TẤT ✅ |
| **Ember Bundle** (Bọc than hồng giữ lửa) | `5eed7279-5d4b-4144-904a-10c0a7805cbf` | `a91cc713-e831-4cc2-9f24-c32180a69653` | `refs/ember_bundle_clean.jpg` | ĐÃ HOÀN TẤT ✅ |
| **Pech Valley** (Thung lũng đá vôi) | `e02aec5c-df73-46a0-bc73-beaccb8c806f` | `6cd2b3d4-fb48-4015-8481-58b833808862` | `refs/pech_valley_clean.jpg` | ĐÃ HOÀN TẤT ✅ |
| **Cave Mouth** (Vòm cửa hang Pech de l'Azé) | `87dfde04-a15d-44a8-9172-78b4a3d55661` | `27348804-f91c-4a45-b395-50799417fd32` | `refs/cave_mouth_clean.jpg` | ĐÃ HOÀN TẤT ✅ |

---

## 3. Công Thức & Quy Trình Tạo Body Mặc Trang Phục (Tái Sử Dụng Cho Mọi Dự Án Tương Lai)

Để tạo ảnh `<Vlogger> Body` đã mặc trang phục mà không bị méo người hay mất form:
1. **Ảnh nguồn:** Bắt buộc dùng ảnh body chuẩn không mặt của user: [uploads/nora_body_v3_clean.jpg](file:///c:/flowkit/uploads/nora_body_v3_clean.jpg) (UUID: `3ea9f8fb-6119-49c8-8466-0bb0ddb2669b`).
2. **Cấu trúc Prompt:** Tham khảo trực tiếp [uploads/nora_base_body_prompt.json](file:///c:/flowkit/uploads/nora_base_body_prompt.json) và [uploads/nora_body_outfit_prompt.json](file:///c:/flowkit/uploads/nora_body_outfit_prompt.json).
   - Đưa mô tả giải phẫu cơ thể lên đầu: Chiều cao `178 cm`, vóc dáng đồng hồ cát rõ nét, ngực lớn đầy đặn nhô cao ở góc nghiêng (`large full heavy natural bust projecting well forward in profile`), eo con kiến nhỏ sắc nét (`very small, narrow, sharply defined waist`), bụng phẳng, hông nở, đùi thon săn chắc và có khoảng hở giữa 2 đùi (`clear gap between the thighs`).
   - Giữ nguyên 3 panel cắt ngang vai ở gốc cổ không lộ mặt: Chính diện, 3/4 và Sau lưng.
   - Thay thế trang phục: mô tả trang phục ôm sát (`form-fitting skin-tight tailored tunic`), thắt eo làm bật đường cong, quần legging bó sát đùi, cấm áo khoác xòe chữ A hay áo parka rộng giấu eo.
3. **Thực thi:** Gọi `EDIT_CHARACTER_IMAGE` với `source_media_id` là UUID của ảnh body nguồn. Tải về, xóa logo SynthID, upload lại lấy UUID sạch và gán trực tiếp làm `media_id` cho entity `<Vlogger> Body`.

---

## 4. Công Việc Tiếp Theo Cần Làm (Next Steps)

1. **Tạo Scenes cho Video (`15076345-ca4a-48cb-8afa-4a79c2a52028`):**
   - Đọc danh sách scene từ [output/neanderthal-51ka/script-v5.md](file:///c:/flowkit/output/neanderthal-51ka/script-v5.md) (từ `MASTER-FIRE` đến `A2-11`).
   - Gửi request tạo scenes qua `POST /api/scenes`:
     - Điền đầy đủ các placeholder: `[ID-LOCK]`, `[HAIR]`, `[SETTING-*]`, `[END-*]`.
     - `character_names` bắt buộc dùng tên entity: `["Nora", "Nora Body", ...]` (tối đa 7 entity/scene).
     - `duration`: `MASTER-FIRE` là 10s, `EST-01` là 6s, `EST-02/03` là 4s, các cảnh còn lại là 8s.
2. **Sinh Video R2V Omni Flash (`GENERATE_VIDEO_REFS`):**
   - Tuân thủ Rule 29: Trình bày danh sách scene và số lượt gen cho user duyệt ("đồng ý") trước khi gửi lệnh.
   - Bắt đầu với scene quan trọng nhất: `MASTER-FIRE` (clip gánh cả hook và payoff).
   - Tải về video 720p thô vào `output/neanderthal-51ka/scenes/scene_XX.mp4`.
3. **Review & Upscale (Rule 18 & 32):**
   - Trích xuất frame và review trên video 720p thô trước.
   - Đưa lên Review Board (`http://localhost:8200`) cho User duyệt.
   - Chỉ khi User duyệt mới gửi lệnh Upscale 1080p (`UPSCALE_VIDEO`) và xóa watermark trên video 1080p.
