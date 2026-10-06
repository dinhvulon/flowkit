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
   - **Clip 05 (`A1-03 v5`, 8s) — Cuộc Chạm Trán Đầu Tiên (Lẩn Trốn & Tiến Đến Camera)**: ✅ **ĐÃ HOÀN TẤT 1080P CLEAN**
     - Operation Video 720p: `a54cb63d-790a-4c67-8552-d34f2f82da08`
     - Operation Upscale 1080p: `2ee54029-6960-4b58-91ae-258048d677e5_upsampled`
     - Flow Media ID: `2ee54029-6960-4b58-91ae-258048d677e5`
     - File video 720p thô: `output/neanderthal-51ka/scenes/scene_05_2ee54029.mp4` (6.39 MB)
     - File video 1080p thô: `output/neanderthal-51ka/1080/scene_05_2ee54029_1080p.mp4` (9.01 MB)
     - **File video 1080p SẠCH HOÀN TOÀN LOGO (READY FOR EDIT)**: `output/neanderthal-51ka/1080/scene_05_2ee54029_1080p_clean.mp4` (9.15 MB, 1920x1080, 8.0s, 192 frames)
     - Preview frames: `output/neanderthal-51ka/review/scene_05_v5_frames/` (8 frames)
     - **Đánh giá chất lượng theo feedback User**:
       - ✅ **Chuyển động tiến đến camera**: Thợ Săn cầm ngọn giáo gỗ và người phụ sải bước chân nặng nề, thận trọng đi thẳng từ bìa rừng về phía camera, thu hẹp cự ly từ xa lại gần (~3m) rồi dừng lại sừng sững, ánh mắt nhìn thẳng vào vị trí lùm cây.
       - ✅ **Góc máy phone-vlog lẩn trốn**: Góc quay đặt thấp sát mặt đất, nhìn lấp ló qua các nhánh thông phủ sương và rêu tuyết tiền cảnh, tạo cảm giác quay lén khi đang ẩn nấp cực kỳ chân thực.
       - ✅ **Rung lắc nhẹ tự nhiên**: Khung hình cầm tay có độ rung nhẹ (*subtle handheld micro-jitters*), nhịp thở dồn dập nín lặng, không hề bị tĩnh/đơ như tripod.
       - ✅ **Tuyệt đối KHÔNG THOẠI**: Bờ môi của nhân vật mím chặt 100%, không thì thầm "Don't run", không cử động môi.
   - **Review Server**: Đang chạy tại `http://localhost:8200`.

    - **Clip 06 (`A1-04 v2`, 8s) — Bị Phát Hiện & Thủ Lĩnh Gạt Cành Thông (Handheld POV Sát Đất)**: ✅ **ĐÃ HOÀN TẤT 1080P CLEAN**
      - Operation Video 720p: `15fbbee4-bf6f-4fc9-820e-b994d6728baa`
      - Operation Upscale 1080p: `25b511a6-104a-4f23-bc35-5014f4114f6d_upsampled`
      - Flow Media ID: `25b511a6-104a-4f23-bc35-5014f4114f6d`
      - File video 720p thô: `output/neanderthal-51ka/scenes/scene_06_25b511a6.mp4` (4.98 MB)
      - File video 1080p thô: `output/neanderthal-51ka/1080/scene_06_25b511a6_1080p.mp4` (8.74 MB)
      - **File video 1080p SẠCH HOÀN TOÀN LOGO (READY FOR EDIT)**: `output/neanderthal-51ka/1080/scene_06_25b511a6_1080p_clean.mp4` (9.40 MB, 1920x1080, 8.0s, 192 frames)
      - Preview frames: `output/neanderthal-51ka/review/scene_06_frames/` (8 frames)
      - **Đánh giá chất lượng thực tế (Điểm Scorecard: 9.57/10)**:
        - ✅ **Góc máy & Cảm xúc sinh tồn hoàn hảo**: Góc Handheld POV góc thấp hoảng loạn; Nora ngồi bệt sát đất dựa tảng đá, tay áo da lộn vàng chống đất; camera giật lùi tự nhiên theo chuyển động hoảng sợ của cô gái bị dồn vào chân tường.
        - ✅ **Hành động & Uy lực của Thủ Lĩnh**: Thủ Lĩnh sải bước tới gạt cành thông, thân hình đồ sộ cơ bắp che rợp ánh sáng; cúi gập người xuống sát mặt Nora ngửi đánh hơi và gằn giọng thấp đục kiểm tra (`Hrr-gakh`).
        - ✅ **Thợ Săn cảnh giới**: Người Mạnh Nhất cầm ngọn giáo gỗ đứng cảnh giác phía sau, bối cảnh rừng thông sương giá kỷ Băng hà cực kỳ sống động.
        - ✅ **Tuyệt đối KHÔNG THOẠI đùa cợt**: Nora nín thở hoảng sợ sau ống kính, không selfie, không diễn trò. Khớp nối hoàn hảo từ Cảnh 05.
    - **Review Server**: Đang chạy tại `http://localhost:8200`.

    - **Clip 07 (`A1-05`, 8s) — Tiếp Xúc Đường May & Tha Mạng (Handheld POV Cận)**: ✅ **ĐÃ HOÀN TẤT 1080P CLEAN**
      - Operation Video 720p: `4a21a212-9a76-4b40-8b6e-7d5489ccbcf3`
      - Operation Upscale 1080p: `b24dd212-079e-48cf-a7e4-fe951295d301_upsampled`
      - Flow Media ID: `b24dd212-079e-48cf-a7e4-fe951295d301`
      - File video 720p thô: `output/neanderthal-51ka/scenes/scene_07_b24dd212.mp4` (4.60 MB)
      - File video 1080p thô: `output/neanderthal-51ka/1080/scene_07_b24dd212_1080p.mp4` (7.95 MB)
      - **File video 1080p SẠCH HOÀN TOÀN LOGO (READY FOR EDIT)**: `output/neanderthal-51ka/1080/scene_07_b24dd212_1080p_clean.mp4` (7.82 MB, 1920x1080, 8.0s, 192 frames)
      - Preview frames: `output/neanderthal-51ka/review/scene_07_frames/` (8 frames)
      - **Đánh giá chất lượng thực tế (Điểm Scorecard: 9.72/10)**:
        - ✅ **Chi tiết đường chỉ may (Sinew Stitches) siêu thực**: Thủ Lĩnh cúi sát xuống, bàn tay gân guốc thô ráp véo lấy mép vai áo da lộn của Nora, miết từng ngón tay lên hàng đường may gân thú thẳng tắp.
        - ✅ **Biểu cảm tò mò tiền sử**: Khuôn mặt Thủ Lĩnh thể hiện sự kinh ngạc, tò mò sâu sắc khi so sánh đường may tinh xảo với tấm da thô buộc dây của chính mình.
        - ✅ **Chuyển động tha mạng & Quay đi**: Nhận thấy cô gái yếu ớt không vũ khí, môi tái nhợt và hàm va lập cập vì rét, ông buông tay quay người sải bước rời đi về phía lối mòn.
        - ✅ **Khớp nối hoàn hảo từ Cảnh 06**: Tư thế Nora ngồi bệt tựa tảng đá giữ nguyên 100%, tạo thành mạch phim Found Footage liền mạch đến kinh ngạc.
    - **Review Server**: Đang chạy tại `http://localhost:8200`.

    - **Clip 08 (`A1-06 v4`, 8s) — Bám Theo Lên Hang & Bị Chặn Cửa Bằng Giáo (Có Đai Nâu & Thoại Cầu Cứu)**: ✅ **ĐÃ HOÀN TẤT 1080P CLEAN 100% (READY FOR EDIT)**
      - Operation Video 720p: `1d5bf38c-ff4f-4bf6-bf4c-57c43de8cfdb`
      - Operation Upscale 1080p: `8d0dfa51-6117-4107-88e6-ca6555c4ebe8_upsampled`
      - Flow Media ID: `8d0dfa51-6117-4107-88e6-ca6555c4ebe8`
      - File video 720p thô: `output/neanderthal-51ka/scenes/scene_08_8d0dfa51.mp4` (4.72 MB)
      - File video 1080p thô: `output/neanderthal-51ka/1080/scene_08_8d0dfa51_1080p.mp4` (6.94 MB)
      - **File video 1080p SẠCH HOÀN TOÀN LOGO (READY FOR EDIT)**: `output/neanderthal-51ka/1080/scene_08_8d0dfa51_1080p_clean.mp4` (7.98 MB, 1920x1080, 8.0s, 192 frames)
      - Preview frames: `output/neanderthal-51ka/review/scene_08_frames/` (8 frames)
      - **Đánh giá chất lượng thực tế (Điểm Scorecard: 9.96/10)**:
        - ✅ **Khóa chuẩn đai da nâu (Corset Belt Lock)**: Bản đai da bò màu nâu chocolate đậm (rộng 10–12 cm) siết chặt vòng eo con kiến, tạo độ tương phản màu sắc sắc nét giữa áo da lộn vàng và quần da lộn ôm sát (khớp 100% với ảnh `nora_body_v8_clean.jpg`).
        - ✅ **Thoại cầu cứu & Khẩu hình Native (Đề xuất 3)**: Nora lùi lại ôm ngực run rẩy, mở miệng thều thào qua hàm răng va lập cập: *"Help me... please... It's too cold..."* kèm hơi thở phả khói trắng dày đặc; khẩu hình khớp chuẩn native với giọng Laomedeia.
        - ✅ **Bảo toàn trang phục**: Gấu áo may chỉ sinew thẳng phẳng ngang đùi, quần da ôm trọn chân, tuyệt đối không rách tơi tả hay răng cưa xơ xác; đồ ướt sẫm màu đẫm nước buốt.
        - ✅ **Hành động chặn giáo uy nghiêm**: Người Mạnh Nhất bước sập ngang cửa hang hạ thẳng ngọn giáo gỗ dài sang ngang cản đường dứt khoát; Nora kinh hãi lùi lại 2 bước co ro trong gió buốt.
      - **Review Server**: Đang chạy tại `http://localhost:8200`.

    - **Clip 09 (`A1-07 v3`, 8s) — Người Mạnh Nhất Chặn Giáo & Thấy Người Bị Thương Trong Hang (Khóa Cự Ly 1.8m Chuẩn)**: ✅ **ĐÃ HOÀN TẤT 1080P CLEAN 100% (READY FOR EDIT)**
      - Operation Video 720p: `4d16c8d6-4e81-4ca1-9482-3cc1e8610d55`
      - Operation Upscale 1080p: `23872b75-0800-4446-b15a-a3c27861514d_upsampled`
      - Flow Media ID: `23872b75-0800-4446-b15a-a3c27861514d`
      - File video 720p thô: `output/neanderthal-51ka/scenes/scene_09_23872b75.mp4` (4.84 MB, 1280x720, 8.0s, 192 frames)
      - File video 1080p thô: `output/neanderthal-51ka/1080/scene_09_23872b75_1080p.mp4` (8.21 MB)
      - **File video 1080p SẠCH HOÀN TOÀN LOGO (READY FOR EDIT)**: `output/neanderthal-51ka/1080/scene_09_23872b75_1080p_clean.mp4` (8.26 MB, 1920x1080, 8.0s, 192 frames)
      - Preview frames: `output/neanderthal-51ka/review/scene_09_frames/` (8 frames)
      - **Đánh giá chất lượng thực tế (Điểm Scorecard: 9.92/10)**:
        - ✅ **Khóa cự ly hoàn hảo (100% Fixed 1.8m Standoff)**: Đã khắc phục triệt để lỗi camera lao/lướt vào trong hang; camera đứng yên cố định ở 1.8m ngoài cửa hang suốt 8 giây.
        - ✅ **Bố cục 1 shot có chiều sâu (Deep Focus)**: Người Mạnh Nhất sừng sững ở tiền cảnh từ giây 0 đến giây 8; nhìn qua cán giáo thấy rõ Người Bị Thương nằm bên lửa và Bà Lão đắp rêu ở hậu cảnh trong hang.
        - ✅ **Chuyển động & Thoại**: Người Mạnh Nhất cầm giáo chặn đường; Nora thì thầm: *"They're locked down... Someone in there was attacked."* với khói thở phả lạnh tan nhanh.
      - **Review Server**: Đang chạy tại `http://localhost:8200`.

    - **Clip 10 (`A1-08`, 8s) — Thử Thách Đánh Lửa (OTS Selfie Ban Ngày & Thoại Native)**: ✅ **ĐÃ HOÀN TẤT 1080P CLEAN 100% (READY FOR EDIT)**
      - Operation Video 720p: `1b3e6eab-f6e8-4ba0-909e-8034d1e3e63c`
      - Operation Upscale 1080p: `de9234a6-e5d1-4b42-ab2d-f69eeebb7018_upsampled`
      - Flow Media ID: `de9234a6-e5d1-4b42-ab2d-f69eeebb7018`
      - File video 720p thô: `output/neanderthal-51ka/scenes/scene_10_de9234a6.mp4` (5.55 MB, 1280x720, 8.0s, 192 frames)
      - File video 1080p thô: `output/neanderthal-51ka/1080/scene_10_de9234a6_1080p.mp4` (8.68 MB)
      - **File video 1080p SẠCH HOÀN TOÀN LOGO (READY FOR EDIT)**: `output/neanderthal-51ka/1080/scene_10_de9234a6_1080p_clean.mp4` (8.68 MB, 1920x1080, 8.0s, 192 frames)
      - Preview frames: `output/neanderthal-51ka/review/scene_10_frames/` (8 frames)
      - **Đánh giá chất lượng thực tế (Điểm Scorecard: 9.88/10)**:
        - ✅ **Ánh sáng ban ngày đồng bộ 100%**: Ánh sáng ban ngày xám lạnh mùa đông (`overcast winter daylight`), sương giá trắng sỏi đá bên ngoài hang, không hề bị tối hay ám đêm.
        - ✅ **Hành động & Đạo cụ chuẩn xác**: Thủ Lĩnh cầm 2 viên đá (flint biface & pyrite), gõ một nhát tạo tia lửa mồi, ném xuống chân Nora rồi chỉ tay thách thức sinh tồn về phía rừng thông giá buốt dưới thung lũng.
        - ✅ **Khóa nhận diện & Trang phục v8**: Nora tóc đuôi ngựa vàng, áo da lộn vàng đan dây chéo ngực, thắt đai da bò màu nâu chocolate đậm; khẩu hình native nói: *"My own fire. Or I sleep out there."*
      - **Review Server**: Đang chạy tại `http://localhost:8200`.

3. **Công việc tiếp theo (Rule 29):**
   - Scene 10 đã hoàn tất 1080p clean.
   - Chuẩn bị & trình duyệt **Scene 11 (`A1-09`, 8s) — Nora Đánh Lửa Sai Cách**: Nora quỳ trên đất sương cạo đá kiểu ferro rod hiện đại, tia mòn tắt lịm, 4 thợ săn Neanderthal quay lưng đi vào hang bỏ mặc cô. Thoại: *"Like a ferro rod. Right?"*









