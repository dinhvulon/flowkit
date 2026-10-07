# HANDOFF — Neanderthal 51ka (Tập 2: "I Survived 24 Hours with Neanderthals")

**Người nhận:** agent tiếp nhận dự án (Claude Code / Antigravity).
**Cập nhật:** 2026-10-06 tối, sau khi đổi sang tài khoản Google mới.
**Đọc trước:** [CLAUDE.md](../../CLAUDE.md) (Rule 10, 27, 28, 29, 31, 46), [skills/fk-time-travel-vlog.md](../../skills/fk-time-travel-vlog.md), [clips.json](clips.json) (nguồn prompt chuẩn), [prompts_review.md](prompts_review.md) (bản đọc của 60 prompt).

---

## 0. Việc cần làm tiếp (theo thứ tự)

1. **Chờ user chọn bảng xung đột X1–X13** (mục 4). Chỉ áp các mục user chọn, lấy nội dung từ [clips_review_fixes.json](clips_review_fixes.json), patch `clips.json` + DB project mới. **Không tự áp mục nào.**
2. **Chờ user duyệt 37 prompt Act 3–5** (scene 24–60). Bản tiếng Việt đã gửi trong hội thoại 2026-10-06. Nếu user giữ X1/X3 như bản chiều (Neanderthal "may chỉ gân", không khóa trang sức) thì đổi khóa tương ứng trong 37 clip cho đồng bộ. Nếu user giữ MASTER bản chiều (Nora quỳ một mình, mục X13) thì sửa A4-11/A4-12 (scene 51–52) bỏ các thợ săn đứng chắn.
3. **Trước khi gen:** user ghim và reload tab `flow.google.com` (tài khoản mới), reload extension, vì lần gửi MASTER đầu tiên dính `NO_INJECTION_RESULT`. Pre-flight `GET /health`.
4. **Gen video scene 8 → 60 (53 clip)**, mỗi lần một clip, theo nhịp user chốt: gửi 1 `GENERATE_VIDEO_REFS`, chờ COMPLETED/FAILED, nghỉ `random(45,60)s + 120s`, rồi mới gửi clip tiếp. Dừng hẳn khi gặp `UNUSUAL_ACTIVITY` / `QUOTA` / `CAPTCHA`; lỗi khác chỉ ghi lại, không tự retry (Rule 29). Mỗi clip xong tải ngay bản 720p về `scenes/scene_{idx:02d}_{sid8}.mp4`. Tiến độ ghi ở `gen_state.json` (tạo khi chạy). Ước tính 6–7 giờ.
   - Không gen scene 1–7 (user: đã có). Scene 1 (MASTER-FIRE) chỉ gen khi user muốn có payoff Act 4.
   - Script runner của phiên 2026-10-06 nằm trong scratchpad (`gen_runner.py`), không nằm trong repo (Rule 43); viết lại theo mô tả trên nếu cần.
5. **Sau khi gen:** chạy `/fk-review-video` (light) cho từng clip, đưa scorecard lên Review Board `:8200`. User duyệt từng clip thì mới upscale 1080p (`UPSCALE_VIDEO`), rồi xóa logo trên bản 1080p (Rule 18/32).
6. **Dựng:** FOREST-SPRINT làm cold open và phát lại sau A4-05; payoff = MASTER giây 6–10; A5-02 đã cắt; countdown 7 mốc (H0, H3, H8, H10, H12, H20, H24) chèn ở hậu kỳ.

---

## 1. Quy tắc bắt buộc (cập nhật 2026-10-07)

1. **TUYỆT ĐỐI CẤM TRẺ CON (Zero Children Rule - User Rule cứng):** Không bao giờ có trẻ con Neanderthal trong video. Tất cả các cảnh bộ tộc, bên bếp lửa và nghi lễ 100% chỉ có người trưởng thành (Thủ Lĩnh, Người Mạnh Nhất, Người Phụ Nữ Lớn Tuổi, Nữ Thợ Săn Trưởng Thành).
2. **BỎ ẨM THỰC LẶP LẠI (User Rule 2026-10-07):** Bỏ hoàn toàn các cảnh ăn tủy xương, nướng thịt vì đã có ở tập trước. Không biến video thành review đồ ăn.
3. **CHỈ ÁP DỤNG 2 TRỤ CỘT VĂN HÓA CỐT LÕI (User Rule 2026-10-07):**
   - **Nghệ thuật & Tâm linh (Symbolic Culture):** Nghi thức đất son đỏ (*Red Ochre*), dấu bàn tay in vách đá (*Hand Stencils*), vòng cổ móng vuốt đại bàng (*Eagle Talon Necklace*).
   - **Đời sống gia đình bên bếp lửa (Adult Hearth Life - CHỈ NGƯỜI LỚN):** Người phụ nữ lớn tuổi làm da thú bằng dao nạo đá Mousterian, xỏ gân hươu, nước sôi bằng đá nung, góc ngủ lót cành thông và da gấu ấm áp.
4. **ĐÃ PHÂN TÍCH & KHÓA CHÍNH XÁC VIDEO 01-07 (1080P CLEAN):** Toàn bộ phân tích chi tiết, góc máy, bối cảnh, hành động và lời thoại thực tế của 7 video có sẵn trong `1080/` đã được lưu tại [SCENES_01_TO_07_ANALYSIS.md](SCENES_01_TO_07_ANALYSIS.md).
5. **KỊCH BẢN MASTER 10 PHÚT (75 CẢNH):** Kịch bản chuẩn 10 phút nối tiếp hoàn hảo từ Cảnh 07 đã được lập tại [SCRIPT_10MIN_75SCENES.md](SCRIPT_10MIN_75SCENES.md).
   - Cảnh 08: Người Mạnh Nhất đưa ngọn giáo gỗ chắn nhẹ nhàng, bình tĩnh, KHÔNG bạo lực.
   - Cảnh 09: POV Nora bị cấm cửa ngoài thềm đá lạnh buốt, CẮT BỎ HOÀN TOÀN NGƯỜI BỊ THƯƠNG.
   - Cảnh 10: Thử thách đánh lửa (Thủ Lĩnh ném hai viên quặng pyrite + đá lửa flint biface).
6. **Prompt của user là chuẩn.** Bản `clips.json` user sửa là nguồn đúng. Review chỉ được đưa ra bảng xung đột để user chọn, không tự đổi góc máy, hành động hay khóa.
7. **Rule 41 đã bỏ** (user 2026-10-06): shot bám theo từ sau lưng vlogger là hợp lệ (A1-06).
8. **Rule 29:** không gửi lệnh tốn credit khi user chưa đồng ý; sau mỗi bước gen phải dừng cho user duyệt.
9. **Rule 28:** ảnh AI phải tải về, chạy `python tools/remove_watermark_from_image.py`, upload lại lấy UUID sạch rồi mới gán.
10. **Nhịp request:** mọi request Flow cách nhau 45–60s (server tự giãn); khi chạy gen dài thì nghỉ thêm 2 phút sau mỗi request.
11. **Rule 46:** video chỉ nhận `["Nora", "Nora Body", ...]`; không có entity outfit riêng.
12. **Ảnh bối cảnh phải sinh mới trên Flow từ prompt**, không cắt frame từ video.
13. **Project id = Flow project id**: khi upload ảnh phải truyền `project_id` của project.
14. Entity `location` **có** được gửi vào R2V (lọc theo `character_names`, tối đa 7 ref).

---

## 2. Project hiện tại (tài khoản mới)

| | ID |
|---|---|
| Project (= Flow project) | `52fe8660-3617-4e4b-8055-23cf987ac4a2` · material `prehistoric_vlog`, `allow_voice: true` |
| Video HORIZONTAL | `b5e0894c-3341-4cd9-a209-9bc39f63a58b` |
| Scenes | 60 (display_order 1–60); prompt, ref và duration khớp 100% `clips.json`. ID từng scene ở [new_project.json](new_project.json) |

### Entity (đều đã có ảnh sạch, không logo)

| Entity | Loại | Entity ID | Media ID | File / dùng ở |
|---|---|---|---|---|
| Nora | character | `bfecefea-7114-451c-a5eb-50f38ccbd537` | `7bf53e09-e902-49bb-8e1d-72b888bad0fd` | `output/ice_age_16_000_bc_survival_vlog/refs/nora_main_clean.jpg` · voice `Laomedeia — …` |
| Nora Body (v8) | character | `a08a76ac-7806-4ecd-a026-20ef40ad751f` | `34e03061-a276-4ca3-9957-0c66f9230146` | `refs/nora_body_v8_clean.jpg` |
| Leader | character | `20d2e841-248b-4d47-869e-f3c3e9e7ac38` | `6d99f576-e136-4d71-af73-5f80ec5aaaaa` | `refs/leader_clean.jpg` |
| Old Woman | character | `5e9044f9-f378-4d78-bae6-af787cb00696` | `3bb8e824-d32a-4997-8d96-3821a609d4ab` | `refs/old_woman_clean.jpg` |
| Strongest | character | `3bcc2f1f-6c7a-4e1a-864b-d5efbd824012` | `e70d0eaa-11bc-4f16-aef3-9982ad6c05ad` | `refs/strongest_clean.jpg` |
| Strongest Spear | visual_asset | `3dbaf548-44c9-4f8f-992c-9dc5113a9279` | `6a9c5dfe-2371-413a-9031-3a91bc51e108` | `refs/strongest_spear_clean.jpg` |
| Cave Hyena | creature | `e0a6ed6d-0e04-4953-b264-e1ef51d24382` | `602b4bf9-a555-407e-a5c2-e1234e07a78f` | `refs/cave_hyena_clean.jpg` |
| Ember Bundle | visual_asset | `cdfb5607-e169-4ba9-ae02-b1f19cbdd942` | `7a9de394-b63e-4dcd-a0c8-8a723f7b69ae` | `refs/ember_bundle_clean.jpg` |
| Pech Valley | location | `3602e1b6-e1fb-451d-b12c-af125f2fe88a` | `ea699e1e-9814-4201-bb13-dad8147e00da` | `refs/pech_valley_clean.jpg` · A1-01/02, Act 3 thung lũng, EST-02/03 |
| Cave Mouth (cũ, nhìn từ trong ra) | location | `f8e4f524-6752-41fe-a404-4eeea4b0b766` | `3b629fb5-dd93-42d4-bff5-8e2c866deb0d` | `refs/cave_mouth_clean.jpg` · không còn clip nào dùng |
| **Cave Exterior** | location | `3bcbc969-6184-47c5-9e0f-741d359d16ac` | `4064de72-abcb-4efb-b26b-dc86cfc9d83a` | `refs/cave_exterior_clean.jpg` · scene 8–21, A5-04/06/07 |
| **Cave Interior** | location | `a4c4b28e-b6f1-4342-b080-85533d385f79` | `ad597b2b-f93d-40c6-9e7e-9f8bf16e44fd` | `refs/cave_interior_clean.jpg` · scene 22–23 và các cảnh trong hang Act 3–5 |
| **Meat Cache** | location | `abb4e925-3bac-44ca-bdbf-23ffce5b8da9` | `1f296118-bccf-4938-afe4-5f0dc9378391` | `refs/meat_cache_clean.jpg` · MASTER, A3-09 → A4-15 |
| **Valley Woodland** | location | `1d041530-52ee-42cb-9233-0d8bcea3825f` | `d092f5aa-ed98-472d-ab53-94b41c8e6d4b` | `refs/valley_woodland_clean.jpg` · A1-03/04/05, A3-07/08, A4-05/05b/16 |

### Trạng thái 60 clip

| Scene | Clip | Trạng thái |
|---|---|---|
| — | FOREST-SPRINT (cold open, 10s) | ✅ `1080/scene_01_8ae57638_1080p_clean.mp4`; prompt gốc ở [shipped_prompts_scene01_02.json](shipped_prompts_scene01_02.json) |
| 1 | MASTER-FIRE (10s) | ⏳ chưa gen (lần gửi đầu user đã hủy); chỉ dùng 4s cuối làm payoff |
| 2 | EST-01 (6s) | ✅ dùng bản bay FPV đã duyệt `1080/scene_02_3fc899f4_1080p_clean.mp4` |
| 3–7 | A1-01 → A1-05 | ✅ 1080p clean trong `1080/` |
| 8–13 | A1-06 → A2-01 | ⏳ cần gen lại (file cũ user đã xóa; bản cũ vẫn còn trong commit `7a9c284`) |
| 14–23 | A2-02 → A2-11 | ⏳ chưa gen |
| 24–60 | Act 3–5 (37 clip, gồm A4-05b mới; A5-02 đã cắt) | ⏳ prompt mới, **chờ user duyệt** |

---

## 3. File trong thư mục

| File | Nội dung |
|---|---|
| `clips.json` | **Nguồn prompt chuẩn** cho 60 clip (scene 1–23 = bản chiều của user + ref bối cảnh; 24–60 = Act 3–5 mới) |
| `clips_review_fixes.json` | Bản có các sửa sau review (X1–X13), lấy ra khi user chọn |
| `prompts_review.md` | Toàn bộ 60 prompt tiếng Anh, dạng để đọc |
| `new_project.json` | ID project, video, entity, scene của tài khoản mới |
| `shipped_prompts_scene01_02.json` | Prompt thật của 2 clip đã duyệt (FOREST-SPRINT, EST-01 FPV) |
| `script-v5.md`, `outline-v5.md` | Kịch bản và storyboard. Storyboard Act 3–5 chưa cập nhật theo review; `clips.json` mới là bản đúng |

---

## 4. Bảng xung đột chờ user chọn (scene 1–23)

| # | Clip | Bản chiều (đang dùng) | Đề xuất sau review |
|---|---|---|---|
| X1 | 8–23 | Neanderthal "đồ may chỉ gân, nhiều lớp, cấm để trần ngực" | Da thô buộc dây, không đường may (A1-05 dựa trên chi tiết họ chưa từng thấy đường may; clip 3–7 cũng là da thô) |
| X2 | 8–11, 14–21 | "Inside, an open fire…"; 12–14 "hang tối lạnh" | Một câu chung: ánh cam ở sâu khoảng 5 m trong hang, ngoài hang không có lửa |
| X3 | 8–11, 15–23 | Thiếu khóa trang sức | Thêm khóa trang sức + dây đan không khoen kim loại (A1-10 cũ bị ra dây chuyền) |
| X4 | 9 | Giáo đang nằm ngang mà dộng cán xuống đá | Dựng giáo thẳng lên rồi mới dộng |
| X5 | 13 | Vừa đánh đá vừa thổi, tia lửa như mưa, than còn cháy ở cuối | Lửa 2–3 cm rồi tự cháy hết thành nhúm đen nguội; rêu rắc bột sẵn (gieo cho A2-06) |
| X6 | 14 | Không có nhúm rêu cháy; còn chữ "camera" | Có nhúm rêu cháy đen; bỏ chữ camera |
| X7 | 16 | Nhét tay trái vào nách khi tay phải đang cầm máy | Chụm tay hà hơi |
| X8 | 17 | Gió thổi lên dốc nhưng rêu bay xuống dốc | Gió đổ xuống dốc |
| X9 | 18 | Bà mở túi ngay | Gõ tay vào bột trên nhúm rêu cũ trước (cần X5) |
| X10 | 19 | "small flame / small fire" | Lửa rêu 2–3 cm, lửa que cỡ lòng bàn tay |
| X11 | 21 | 3 que vẫn cháy sau quãng nhảy thời gian | Bó que đã dùng một nửa |
| X12 | 10, 11 | Thiếu ref giáo | Thêm `Strongest Spear` |
| X13 | 1 | Nora quỳ một mình | 3 thợ săn quay lưng đứng chắn trước linh cẩu (khớp A4-11/12), thêm khóa loài, lửa 2–3 cm |

---

## 5. Công Thức & Quy Trình Tạo Body Mặc Trang Phục (Tái Sử Dụng Cho Mọi Dự Án Tương Lai)

Để tạo ảnh `<Vlogger> Body` đã mặc trang phục mà không bị méo người hay mất form:
1. **Ảnh nguồn:** Bắt buộc dùng ảnh body chuẩn không mặt của user: [uploads/nora_body_v3_clean.jpg](file:///c:/flowkit/uploads/nora_body_v3_clean.jpg) (UUID: `3ea9f8fb-6119-49c8-8466-0bb0ddb2669b`).
2. **Cấu trúc Prompt:** Tham khảo trực tiếp [uploads/nora_base_body_prompt.json](file:///c:/flowkit/uploads/nora_base_body_prompt.json) và [uploads/nora_body_outfit_prompt.json](file:///c:/flowkit/uploads/nora_body_outfit_prompt.json).
   - Đưa mô tả giải phẫu cơ thể lên đầu: Chiều cao `178 cm`, vóc dáng đồng hồ cát rõ nét, ngực lớn đầy đặn nhô cao ở góc nghiêng (`large full heavy natural bust projecting well forward in profile`), eo con kiến nhỏ sắc nét (`very small, narrow, sharply defined waist`), bụng phẳng, hông nở, đùi thon săn chắc và có khoảng hở giữa 2 đùi (`clear gap between the thighs`).
   - Giữ nguyên 3 panel cắt ngang vai ở gốc cổ không lộ mặt: Chính diện, 3/4 và Sau lưng.
   - Thay thế trang phục: mô tả trang phục ôm sát (`form-fitting skin-tight tailored tunic`), thắt eo làm bật đường cong, quần legging bó sát đùi, cấm áo khoác xòe chữ A hay áo parka rộng giấu eo.
3. **Quy tắc khóa trang phục v8 chuẩn (Bắt buộc đồng bộ 100% cho mọi prompt video downstream):**
   - **Dây đan chéo chữ X ở ngực:** `CHEST LACING LOCK (CRITICAL): The deep plunging V-neckline MUST be visibly laced with distinct criss-crossing dark-brown leather thongs forming a prominent X-pattern bridge across her full cleavage (matching the Nora Body ref exactly); strictly NOT plain open skin, NOT unlaced, NOT gaping empty.`
   - **Đai da bò nâu chocolate đậm (10–12 cm):** `CORSET BELT LOCK (CRITICAL): Tightly cinched at her tiny waist with a wide 10-12 cm dark-chocolate brown leather belt... strictly plain prehistoric dark-brown hide tied with a thong, strictly NO modern metal buckle, NO brass ring, creating sharp dark-against-golden contrast matching the Nora Body reference exactly.`
   - **Cổ tay áo trơn sạch tuyệt đối cấm tua rua:** `SLEEVE CUFF LOCK (CRITICAL): Long fitted sleeves ending cleanly and neatly at the wrists with smooth stitched cuffs; strictly NO fringe, NO tassels, NO hanging leather strips, NO fur trim, NO fur cuffs.`
4. **Thực thi:** Gọi `EDIT_CHARACTER_IMAGE` với `source_media_id` là UUID của ảnh body nguồn. Tải về, xóa logo SynthID, upload lại lấy UUID sạch và gán trực tiếp làm `media_id` cho entity `<Vlogger> Body`.

---

## 6. Lưu trữ: trạng thái tài khoản cũ (project 4cc4b500-…, không còn gen được)

Tài khoản cũ bị PUBLIC_ERROR_UNUSUAL_ACTIVITY cho mọi lệnh sinh từ 16:28 ngày 2026-10-05. DB project cũ đã patch prompt đồng bộ với clips.json để tham khảo, nhưng không dùng để gen nữa.

### A. Project tài khoản cũ

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

### B. Tiến độ clip trên tài khoản cũ

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

    - **Clip 11 (`A1-09 v2`, 8s) — Nora Đánh Lửa Sai Cách (Cạo Đá Kiểu Ferro Rod)**: ✅ **ĐÃ HOÀN TẤT 1080P CLEAN 100% (READY FOR EDIT)**
      - Operation Video 720p: `6acaa9bf-eaf7-40f2-b496-f6bd8076542e`
      - Operation Upscale 1080p: `bab49e9b-14c8-4c5a-9c1b-2dbb9efbfbd5_upsampled`
      - Flow Media ID: `bab49e9b-14c8-4c5a-9c1b-2dbb9efbfbd5`
      - File video 720p thô: `output/neanderthal-51ka/scenes/scene_11_v2_bab49e9b.mp4` (3.40 MB, 1280x720, 8.0s, 192 frames)
      - File video 1080p thô: `output/neanderthal-51ka/1080/scene_11_bab49e9b_1080p.mp4` (8.17 MB)
      - **File video 1080p SẠCH HOÀN TOÀN LOGO (READY FOR EDIT)**: `output/neanderthal-51ka/1080/scene_11_bab49e9b_1080p_clean.mp4` (6.96 MB, 1920x1080, 8.0s, 192 frames)
      - Preview frames 720p: `output/neanderthal-51ka/review/scene_11_v2_frames/` (8 frames)
      - Preview frames 1080p clean: `output/neanderthal-51ka/review/scene_11_1080p_clean_frames/` (8 frames)
      - **Đánh giá chất lượng thực tế (Điểm Scorecard: 9.95/10 - User Đã Duyệt)**:
        - ✅ **Khắc phục 100% lỗi dây đan ngực (`CHEST LACING LOCK`)**: Dây da màu nâu đen đan chéo chữ X rõ nét, dày dặn bắc ngang qua rãnh ngực sâu và đầy đặn, khớp 100% với ảnh reference `nora_body_v8_clean.jpg`. Tuyệt đối không còn khoảng hở ngực trần thiếu dây.
        - ✅ **Khắc phục 100% màu đai & loại bỏ khóa kim loại (`CORSET BELT LOCK`)**: Bản đai da bò màu nâu chocolate đậm (10–12 cm) siết chặt vòng eo con kiến, buộc dây thừng da tiền sử mộc mạc, tuyệt đối không có mặt khóa kim loại (`metal buckle`), tạo độ tương phản cực kỳ sắc nét trên nền áo da lộn vàng.
        - ✅ **Khắc phục 100% cổ tay áo trơn sạch (`SLEEVE CUFF LOCK`)**: Ống tay áo da lộn ôm sát dài chấm cổ tay, viền may chỉ sinew phẳng phiu, sạch bóng 100% không còn dải tua rua (`fringes / tassels`) hay viền lông nào.
        - ✅ **Diễn xuất & Động tác cạo đá sinh tồn**: Nora quỳ gối trên sỏi đá, hai tay cầm flint biface và pyrite cạo dọc tạo tia lửa nhưng trượt; ngước mắt nhìn lên nói: *"Like a ferro rod. Right?"*; 4 thợ săn Neanderthal quay lưng đi vào hang bỏ mặc cô quỳ co ro trong gió buốt.
      - **Clip 12 (`A1-10 v2`, 8s) — Người Già Đặt 4 Nhúm Rêu Lên Vỏ Cây (SẠCH HOÀN TOÀN LỬA NGOÀI HANG)**: ✅ **ĐÃ HOÀN TẤT 1080P CLEAN 100% (USER ĐÃ DUYỆT)**
      - Operation Video 720p: `fc638e55-290e-4d59-98a3-87a98e7f30af`
      - Operation Upscale 1080p: `9b25a81c-2674-4abd-ac27-902b514455d1_upsampled`
      - Flow Media ID: `9b25a81c-2674-4abd-ac27-902b514455d1`
      - File video 720p thô: `output/neanderthal-51ka/scenes/scene_12_v2_9b25a81c.mp4` (6.49 MB, 1280x720, 8.0s, 192 frames)
      - File video 1080p thô: `output/neanderthal-51ka/1080/scene_12_9b25a81c_1080p.mp4` (10.19 MB)
      - **File video 1080p SẠCH HOÀN TOÀN LOGO (READY FOR EDIT)**: `output/neanderthal-51ka/1080/scene_12_9b25a81c_1080p_clean.mp4` (9.86 MB, 1920x1080, 8.0s, 192 frames)
      - Preview frames 720p: `output/neanderthal-51ka/review/scene_12_v2_frames/` (8 frames)
      - **Đánh giá chất lượng thực tế (Điểm AI Scorecard: 10/10 - User Đã Duyệt)**:
        - ✅ **Khắc phục 100% lỗi đống lửa ngoài hang (`STRICTLY NO FIRE OUTSIDE`)**: Khoảng đất sỏi giữa hai chân Bà Lão và khu vực ngoài hang hoàn toàn đóng băng lạnh ngắt, không còn bất kỳ đốm than, ngọn lửa hay vòng đá nào; miệng hang phía sau tối xám lạnh lẽo, thể hiện chính xác 100% logic Nora bị cô lập ngoài trời băng giá không có lửa.
        - ✅ **Hành động & Đạo cụ chuẩn xác (4 Nhúm Rêu Khô)**: Người Già từ trong hang bước ra, ngồi xổm đặt đúng 4 nhúm rêu khô thành hàng thẳng tắp lên miếng vỏ cây trước mặt Nora trên nền sỏi trần, rồi đứng dậy quay bước vào hang.
        - ✅ **Diễn xuất & Thoại Native của Nora**: Nora quan sát 4 nhúm rêu trên miếng vỏ cây, ngoái nhìn theo Người Già rồi xoay ánh mắt về phía camera, khẩu hình mở thì thào *"Okay."* với vẻ mặt cảm kích xen lẫn lạnh buốt; hơi thở phả khói tan nhanh.
        - ✅ **Khóa trang phục chuẩn v8 (100% Locked)**: Dây da đan chéo chữ X dày dặn, sắc nét bắc ngang qua rãnh ngực sâu và đầy đặn; đai da bò màu nâu chocolate đậm siết chặt eo không mặt khóa kim loại; ống tay áo da lộn may trơn sạch, cấm tuyệt đối tua rua.
      - **Review Server**: Đang chạy tại `http://localhost:8200`.

    - **Clip 13 (`A2-01 v6`, 8s) — Người Già Đánh Lửa Mẫu (LỬA MỒI LI TI 2-3CM, TÀN TỰ NHIÊN & KHÓI BỐC NGHI NGÚT)**: ✅ **ĐÃ HOÀN TẤT 1080P CLEAN 100% (USER ĐÃ DUYỆT)**
      - Operation Video 720p: `a0c650f1-a77a-4875-86e4-25c734535354`
      - Operation Upscale 1080p: `a9e321d4-1dce-4f2d-8abd-ee4ec4c03b82_upsampled`
      - Flow Media ID: `a9e321d4-1dce-4f2d-8abd-ee4ec4c03b82`
      - File video 720p thô: `output/neanderthal-51ka/scenes/scene_13_v6_a9e321d4.mp4` (7.02 MB, 1280x720, 8.0s, 192 frames)
      - File video 1080p thô: `output/neanderthal-51ka/1080/scene_13_a9e321d4_1080p.mp4` (11.01 MB)
      - **File video 1080p SẠCH HOÀN TOÀN LOGO (READY FOR EDIT)**: `output/neanderthal-51ka/1080/scene_13_a9e321d4_1080p_clean.mp4` (10.22 MB, 1920x1080, 8.0s, 192 frames)
      - Preview frames 720p: `output/neanderthal-51ka/review/scene_13_v6_frames/` (8 frames)
      - **Đánh giá chất lượng thực tế (Điểm AI Scorecard: 10/10 - User Đã Duyệt)**:
        - ✅ **Khắc phục 100% lỗi lửa quá to (`TINY CANDLE-SIZED FLAME 2–3 cm`)**: Rêu bùi nhùi mồi lửa chỉ bốc ngọn lửa mồi li ti cực nhỏ như ngọn nến le lói, tâm rêu ửng than đỏ hồng tự nhiên, phản chiếu ấm áp lên ngón tay bà lão (khắc phục triệt để lỗi lửa bùng to như bếp ga).
        - ✅ **Khắc phục 100% lỗi lửa tắt ngúm phi lý (`GRADUAL NATURAL DECAY`)**: Không dùng đất hay đá đè dập lửa bạo lực làm tắt ngúm trong 1 frame; ngọn lửa mồi li ti tự nhiên lụi tàn dần từ từ qua 2–3 giây thành đốm than đỏ cam cháy âm ỉ bên dưới.
        - ✅ **Khói bốc nghi ngút cực kỳ chân thực (`SMOKE EMISSION`)**: Làn khói trắng xám dày đặc cuộn sóng uốn lượn bốc lên liên tục từ đốm than đang âm ỉ bay vào không khí giá buốt.
        - ✅ **Khóa bối cảnh & Đạo cụ từ frame 0**: Sạch 100% đống lửa hậu cảnh (cửa hang tối và lạnh buốt phía sau); hai viên đá cầm chắc trên tay từ giây 0.0s.
        - ✅ **Khóa nhận diện trang phục v8 của Nora**: Đai da bò màu nâu chocolate đậm siết eo, đan dây ngực X dày dặn, cổ tay trơn sạch, sạch tuyệt đối dây chuyền trang sức; Nora kinh ngạc thì thào qua hàm răng run: *"Three strikes. She does it in three."*
      - **Review Server**: Đang chạy tại `http://localhost:8200`.

3. **Tổng kết tiến độ & Công việc tiếp theo (Rule 29):**
   - **Tiến độ:** 13/13 clips đầu tiên (Clip 01 đến Clip 13) đều đã hoàn tất **1080p Clean 100%** (Sẵn sàng đưa vào Timeline dựng phim).
   - **Bước tiếp theo:**
     - Prompt của **Scene 14 (`A2-02`, 8s) — Nora Tự Đánh Lửa Nhát 1: Hỏng** đã được chuẩn hóa 100% theo các bài học Story Engine mới (STRICTLY NO FIRE OUTSIDE, cầm đá từ frame 0, outfit v8, 4 nhúm rêu -> 3 nhúm rêu).
     - Xin xác nhận từ User theo Rule 29 để gửi lệnh tạo video 720p thô cho Scene 14.
