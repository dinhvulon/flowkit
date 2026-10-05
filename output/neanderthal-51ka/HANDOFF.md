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
| **Nora Body** (Body đã mặc outfit v7 — đảo ngược từ video MASTER-FIRE) | `c58ac1d3-14a9-4169-94a3-681790557d8e` | `4cba3314-40ad-4ed1-a90a-a7d63870308c` | `refs/nora_body_v7_clean.jpg` | **USER ĐÃ DUYỆT** ✅ |
| **Leader** (Thủ lĩnh Neanderthal) | `288d06c2-2b2a-4016-9eab-c5d670df67e7` | `f4395dd6-9227-4b8d-8425-8bd71d8027ed` | `refs/leader_clean.jpg` | ĐÃ HOÀN TẤT ✅ |
| **Old Woman** (Bà lão giữ lửa) | `e8a607ed-e207-4be3-806d-f4df489f5a11` | `5a2b982a-5ae8-4124-ada7-dc98df9a59a8` | `refs/old_woman_clean.jpg` | ĐÃ HOÀN TẤT ✅ |
| **Strongest** (Thợ săn to lớn) | `4ae88e7c-997f-4e79-97ee-96a14b3b5d8c` | `10ab07ce-7600-4f73-8697-6cc1a3e09aca` | `refs/strongest_clean.jpg` | ĐÃ HOÀN TẤT ✅ |
| **Strongest Spear** (Ngọn giáo đá lửa) | `ee521059-d0c6-49c2-970b-59353fa87211` | `b508a82a-f410-421a-b6fd-38a1812d1abf` | `refs/strongest_spear_clean.jpg` | ĐÃ HOÀN TẤT ✅ |
| **Cave Hyena** (Linh cẩu hang động) | `680d64bf-c0c3-4cda-9074-d99cef97c12c` | `7559d40f-801e-4821-a685-2c7dded0b1f3` | `refs/cave_hyena_clean.jpg` | ĐÃ HOÀN TẤT ✅ |
| **Ember Bundle** (Bọc than hồng giữ lửa) | `5eed7279-5d4b-4144-904a-10c0a7805cbf` | `a91cc713-e831-4cc2-9f24-c32180a69653` | `refs/ember_bundle_clean.jpg` | ĐÃ HOÀN TẤT ✅ |
| **Pech Valley** (Thung lũng đá vôi) | `e02aec5c-df73-46a0-bc73-beaccb8c806f` | `6cd2b3d4-fb48-4015-8481-58b833808862` | `refs/pech_valley_clean.jpg` | ĐÃ HOÀN TẤT ✅ |
| **Cave Mouth** (Vòm cửa hang Pech de l'Azé) | `87dfde04-a15d-44a8-9172-78b4a3d55661` | `67e0005d-a440-4a45-b623-1d272b7a0676` | `refs/cave_mouth_clean.jpg` | ĐÃ HOÀN TẤT ✅ |

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

1. **Tạo Scenes cho Video (`15076345-ca4a-48cb-8afa-4a79c2a52028`):** ✅ **ĐÃ HOÀN TẤT 23 SCENES**
   - Đã tạo toàn bộ 23 scenes từ Cold Open đến Act 2 (`MASTER-FIRE` đến `A2-11`) trong database.
   - Đã bung đầy đủ tất cả placeholders (`[ID-LOCK]`, `[HAIR]`, `[WET]`, `[NEANDERTHAL]`, `[HYENA]`, `[SETTING-*]`, `[END-*]`).
   - Đã gán đúng duration (Scene 1 `MASTER-FIRE`: 10s, Scene 2 `EST-01`: 6s, các scene còn lại: 8s).
   - Đã khóa danh sách entity refs `["Nora", "Nora Body", ...]` theo đúng chuẩn Rule 46 & 38.

2. **Sinh Video R2V Omni Flash (`GENERATE_VIDEO_REFS`):**
   - **Clip 01 (`FOREST-SPRINT v6`, 10s) — Chạy Thục Mạng & Linh Cẩu Bám Đuổi Giữ Cự Ly**: ✅ **ĐÃ HOÀN TẤT 1080P CLEAN**
     - Request Video 720p: `7db2b639-fe83-44e8-96dd-0eb022e256eb`
     - Request Upscale 1080p: `7feb2c2e-f7a0-43fa-9ae8-ce234e888e1e`
     - Flow Media ID: `c05f7420-8252-48ab-ba7d-d7579dc6ab06`
     - File video 720p thô: `output/neanderthal-51ka/scenes/scene_01_8ae57638.mp4` (8.29 MB)
     - File video 1080p thô: `output/neanderthal-51ka/1080/scene_01_8ae57638_1080p.mp4` (12.77 MB)
     - **File video 1080p SẠCH HOÀN TOÀN LOGO (READY FOR EDIT)**: `output/neanderthal-51ka/1080/scene_01_8ae57638_1080p_clean.mp4` (14.60 MB, 1920x1080, 10.0s, 240 frames)
     - Preview frames: `output/neanderthal-51ka/review/scene_01_v6_frames/` (10 frames)
     - **Kết quả kiểm duyệt theo chỉ đạo User:**
       - ✅ **Hành vi linh cẩu:** 2 linh cẩu phi nước đại đuổi theo sau lưng giữ cự ly 4–6m trong bóng cây, tuyệt đối không nhảy đến cắn.
       - ✅ **Nhịp độ & Chuyển động:** Nora chạy thục mạng liên tục 10s (*non-stop full sprint*), camera selfie 0.5x rung lắc dữ dội theo bước chân, hơi thở phả khói lạnh.
       - ✅ **Khóa Trang phục (Outfit chuẩn v8):** Áo da lộn vàng mật ong có dây đan chéo chữ X ở ngực, cổ tay áo sạch lông trơn tru, không có dây chuyền kim loại.
       - ✅ **Bối cảnh:** Rừng thông đêm Dordogne 51k năm trước, cành khô lá mục phủ đất, không có tuyết.
   - **Clip 02 (`EST-01 v2`, 6s) — Cú Lướt FPV Tốc Độ Cao Lao Vào Hang Neanderthal**: ✅ **ĐÃ HOÀN TẤT 1080P CLEAN**
     - Request Video 720p: `260e150d-ff3d-4450-8f37-ad24c25ead6c`
     - Request Upscale 1080p: `569370ed-7167-4964-a939-db94e44d36d4`
     - Flow Media ID: `54682aa7-91cf-47a2-9de0-52c3acf3876c`
     - File video 720p thô: `output/neanderthal-51ka/scenes/scene_02_3fc899f4.mp4` (5.00 MB)
     - File video 1080p thô: `output/neanderthal-51ka/1080/scene_02_3fc899f4_1080p.mp4` (8.78 MB)
     - **File video 1080p SẠCH HOÀN TOÀN LOGO (READY FOR EDIT)**: `output/neanderthal-51ka/1080/scene_02_3fc899f4_1080p_clean.mp4` (9.33 MB, 1920x1080, 6.0s, 144 frames)
     - Preview frames: `output/neanderthal-51ka/review/scene_02_v2_frames/` (6 frames)
     - Đánh giá chất lượng: Đúng 100% yêu cầu user — camera lao nhanh với gia tốc lớn như đường chim bay từ thung lũng Pech Valley, lướt qua dòng suối và vách đá vôi rồi lao thẳng qua cửa hang vào tận trong lòng hang đá nơi có đống lửa sưởi và da thú.
   - **Review Server**: Đang chạy tại `http://localhost:8200`.

   - **Clip 03 (`A1-01`, 8s) — Nora Selfie Dọc Suối & Trượt Chân Ngã Nước**: ✅ **ĐÃ HOÀN TẤT 1080P CLEAN**
     - Request Video 720p: `8c466cf6-97bf-4f60-9533-3381fdf74a6c`
     - Request Upscale 1080p: `52dbb39f-7bde-4bee-aaf8-077bab0231f9`
     - Flow Media ID: `29178e1e-fba4-4732-81e6-e69cdbded862`
     - File video 720p thô: `output/neanderthal-51ka/scenes/scene_03_e7a2e9c3.mp4` (7.98 MB)
     - File video 1080p thô: `output/neanderthal-51ka/1080/scene_03_e7a2e9c3_1080p.mp4` (14.65 MB)
     - **File video 1080p SẠCH HOÀN TOÀN LOGO (READY FOR EDIT)**: `output/neanderthal-51ka/1080/scene_03_e7a2e9c3_1080p_clean.mp4` (14.50 MB, 1920x1080, 8.0s, 192 frames)
     - Preview frames: `output/neanderthal-51ka/review/scene_03_frames/` (8 frames)
     - Đánh giá chất lượng: Nhận diện khuôn mặt và outfit v8 chuẩn 100% (dây đan chéo chữ X, sạch lông cổ tay, không trang sức), cú trượt chân xuống suối băng tự nhiên, tay phải giữ camera giơ cao không rơi nước, tay trái bám rễ cây trèo lên, vết ướt nước trên áo da lộn rất thực tế.
   - **Review Server**: Đang chạy tại `http://localhost:8200`.

   - **Clip 04 (`A1-02 v2`, 8s) — Nora Quỳ Trên Đá Gạt Nước & Ôm Ngực Run Rẩy**: ✅ **ĐÃ HOÀN TẤT 1080P CLEAN**
     - Request Video 720p: `f11129d1-ac28-43b0-bce7-1b46cbdc7a68`
     - Request Upscale 1080p: `95484488-3cfe-4dd0-88f9-d3639633512a`
     - Flow Media ID: `7f579df4-0fca-4046-99c7-bdcccbd878d3`
     - File video 720p thô: `output/neanderthal-51ka/scenes/scene_04_1428bcf0.mp4` (3.77 MB)
     - File video 1080p thô: `output/neanderthal-51ka/1080/scene_04_1428bcf0_1080p.mp4` (9.90 MB)
     - **File video 1080p SẠCH HOÀN TOÀN LOGO (READY FOR EDIT)**: `output/neanderthal-51ka/1080/scene_04_1428bcf0_1080p_clean.mp4` (8.62 MB, 1920x1080, 8.0s, 192 frames)
     - Preview frames: `output/neanderthal-51ka/review/scene_04_v2_frames/` (8 frames)
     - Đánh giá chất lượng: Đã khắc phục 100% lỗi tua rua tay áo; tay áo da lộn trơn ôm sát chuẩn v8; động tác vuốt gạt nước tự nhiên; khoanh tay ôm ngực run rẩy vì sốc nhiệt; giơ bàn tay đỏ ửng tê dại lên nhìn rất điện ảnh.
   - **Clip 05 (`A1-03 v2`, 8s) — Cuộc Chạm Trán Đầu Tiên Với 5 Người Neanderthal**: ✅ **ĐÃ HOÀN TẤT 720P THÔ**
     - Request Video 720p: `221dc3a1-065b-4ba5-831a-2e2e89a080f3`
     - Flow Media ID: `ae013783-16cf-4ad9-bfd4-8b78019e1d10`
     - File video 720p thô: `output/neanderthal-51ka/scenes/scene_05_23a31226.mp4` (7.05 MB)
     - Preview frames: `output/neanderthal-51ka/review/scene_05_v2_frames/` (8 frames)
     - Đánh giá chất lượng: Khắc phục 100% lỗi người phụ cầm giáo bị biến mất và lỗi bước đều như rô bốt — chuyển sang bố cục bất đối xứng tự nhiên: thợ săn sừng sững găm giáo đá xuống đất xuyên suốt clip, bà lão quỳ nấp gốc bạch dương, người phụ nấp sau thân thông, Nora ngoái đầu sợ hãi rồi quay lại thì thào: *"Don't run."*
   - **Review Server**: Đang chạy tại `http://localhost:8200`.

3. **Công việc tiếp theo (Rule 29 - Chờ User duyệt để sinh):**
   - **Upscale Scene 05** hoặc tiếp tục sang:
   - **Scene 06 (`A1-04`, 8s)**: Thủ Lĩnh Neanderthal bước lên thăm dò, ra hiệu lệnh tay hoặc kiểm tra ngọn giáo. Refs: `["Nora", "Nora Body", "Leader", "Strongest", "Strongest Spear"]`. Model: `abra_r2v_8s`.









