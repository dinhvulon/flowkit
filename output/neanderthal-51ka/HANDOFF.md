# HANDOFF — Neanderthal 51ka (Tập 2 "I Survived 24 Hours")

Người nhận: agent Antigravity làm tiếp dự án. Viết ngày 2026-10-05.
Đọc trước: `CLAUDE.md` (đặc biệt Rule 10, 27, 28, 29, 31, 46), `skills/fk-time-travel-vlog.md` (bài học 34, 47, 55–60), `output/neanderthal-51ka/script-v5.md`.

---

## 1. Luật bắt buộc khi làm tiếp

- **Rule 29:** KHÔNG gửi bất kỳ lệnh sinh nào (`GENERATE_*`, `REGENERATE_*`, `EDIT_CHARACTER_IMAGE`, video) khi user chưa nói "yes". Trước mỗi lần sinh, nói rõ sinh cái gì và bao nhiêu lượt. Sinh xong thì DỪNG và cho user xem. Lỗi thì báo cáo, không tự retry.
- **Rule 31:** gặp lỗi pipeline thì chạy `/fk-doctor` trước.
- **Rule 46 (user lock 2026-10-05):** Body đã mặc trang phục đóng vai trò là `Nora Body` luôn (xóa bỏ entity `Nora Outfit` riêng). Video chỉ nhận `["Nora", "Nora Body", ...]`.
- Không dùng "Copy as cURL" khi capture, vì nó chứa cookie đăng nhập. Chỉ copy `f.req`.

## 2. Trạng thái server

| Mục | Giá trị |
|---|---|
| Project | `4cc4b500-6e3b-4379-96c3-dd18b7412c1a` (material `prehistoric_vlog`, `allow_voice: true`) |
| Video | `15076345-ca4a-48cb-8afa-4a79c2a52028` (HORIZONTAL) |
| Scenes | **chưa tạo** |

| Entity | ID | media_id hiện tại |
|---|---|---|
| Nora (mặt) | `f1e93b66-f83f-40d8-bf6e-d22ec444f57e` | `1454fb46-8510-4f14-99fe-8464720632b6` (sạch, từ `nora_main_clean.jpg`) ✅ |
| Nora Body | `c58ac1d3-14a9-4169-94a3-681790557d8e` | `76efe0b4-6c92-428c-8cce-4bbfd8c9a7e1` (sạch, từ `nora_outfit_v4_clean.jpg` — Body đã mặc outfit da hươu ôm sát) ✅ |
| Leader | `288d06c2-2b2a-4016-9eab-c5d670df67e7` | chưa có |
| Old Woman | `e8a607ed-e207-4be3-806d-f4df489f5a11` | chưa có |
| Strongest | `4ae88e7c-997f-4e79-97ee-96a14b3b5d8c` | chưa có |
| Strongest Spear | `ee521059-d0c6-49c2-970b-59353fa87211` | chưa có |
| Cave Hyena | `680d64bf-c0c3-4cda-9074-d99cef97c12c` | chưa có |
| Ember Bundle | `5eed7279-5d4b-4144-904a-10c0a7805cbf` | chưa có |
| Pech Valley | `e02aec5c-df73-46a0-bc73-beaccb8c806f` | chưa có |
| Cave Mouth | `87dfde04-a15d-44a8-9172-78b4a3d55661` | chưa có |
| Child | `72cef9e2-1ebb-41ac-8950-27c823dbf8cc` | **đã xóa khỏi DB** ✅ |
| Nora Outfit | `14753a8e-7c58-4513-8ea6-8079e4096fd4` | **đã xóa khỏi DB** (Body đã mặc outfit trực tiếp, video chỉ nhận `["Nora", "Nora Body"]`) ✅ |

## 3. VIỆC ĐÃ XONG: Outfit v4 hợp nhất Nora Body + Outfit đã hoàn tất
- Đã dùng đúng ảnh body của user: `uploads/nora_body_v3_clean.jpg` (`108813da-76b2-4d7b-8ecb-207db760c45e`).
- Đã chạy 1 lệnh `EDIT_CHARACTER_IMAGE` tạo `refs/nora_outfit_v4.jpg`.
- Đã xóa sạch watermark SynthID bằng `python tools/remove_watermark_from_image.py` -> `refs/nora_outfit_v4_clean.jpg`.
- Đã PATCH `media_id` sạch vào entity `Nora Body` (`c58ac1d3-14a9-4169-94a3-681790557d8e`), đồng thời xóa bỏ entity thừa `Nora Outfit` khỏi database.
- Đã cập nhật `[ID-LOCK]` trong `script-v5.md` phản ánh đúng `Nora Body` là Body đã mặc outfit (khóa ngực đầy nhô cao, eo thon, hông nở, chân dài, áo tunic ôm sát).

**Đã xem ảnh và so sánh:**
- `refs/nora_outfit_v3.jpg` (EDIT từ `Nora Body` = `uploads/nora_body_v3_clean.jpg`):
  - ngực bị ép phẳng, mất eo;
  - áo dáng chữ A xòe che mất hông;
  - legging rộng, chân trông gầy.
- **Có thể đã dùng nhầm body:** body chuẩn dùng lại của user là `uploads/nora_base_body_clean.jpg` (memory `project_nora_base_ref`: "reusable base for ALL future projects"). Ảnh này đầy đặn hơn hẳn: ngực đầy, eo, hông và đùi tròn. Còn `nora_body_v3_clean.jpg` (của Ice Age) là một dáng khác, mảnh hơn, chân dài thon. Project này đang gắn nhầm ảnh thứ hai làm `Nora Body`.

**Nguyên nhân trong prompt v3** (file `outfit_prompt_v3.json` nằm trong scratchpad của phiên Claude cũ; nội dung gồm prompt EDIT "keep the exact same three panels… Only change the clothing…"):
1. Phần bố cục đặt trước phần mô tả body. Memory `project_nora_base_ref` đã cảnh báo: "Put the BODY description before layout in the prompt or the bust gets toned down."
2. Dùng chữ "parka" và "flaring over the wide hips", nên model vẽ áo khoác dày, xòe chữ A, che mất đường cong.
3. Không có câu BODY LOCK đối kháng (NOT slimmer, NOT flat-chested…).

**Đã chuẩn bị (không tốn lượt sinh):** `output/neanderthal-51ka/refs/nora_base_body_noface.jpg`.
- Cách làm: crop từ `uploads/nora_base_body_clean.jpg`, bỏ panel mặt, cắt ngang vai, pad 16:9.
- Lệnh: `crop=918:620:458:148,pad=1102:620:92:0:color=0xE6E6E8`.
- Kết quả: 2 panel (3/4 và chính diện), không lộ mặt, giữ đúng form của user. Màu nền pad hơi lệch nền gốc, có thể chỉnh lại.
- **Chưa upload, chưa cho user xem.**

**Đề xuất cho bước tiếp theo** (phải hỏi user, nhất là câu 1):
1. Hỏi user đúng body của họ là `uploads/nora_base_body_clean.jpg` phải không. Cho user xem cả hai ảnh body và ảnh v3.
2. Nếu đúng:
   - upload `nora_base_body_noface.jpg` (`POST /api/flow/upload-image` `{file_path, project_id}`);
   - PATCH `media_id` của `Nora Body` (`c58ac1d3-…`).

   Bước này không tốn lượt sinh.
3. Viết prompt EDIT v4 và PATCH vào `image_prompt` của Nora Outfit. Prompt phải:
   - mở đầu bằng mô tả BODY: giữ đúng dáng, ngực, eo, hông, đùi như ảnh nguồn;
   - sau đó mới tới bố cục: "keep the same two panels, same poses, same framing at the shoulders, same background";
   - outfit **ôm sát**: "fitted tunic-dress" thay cho "parka"; may theo đường cong, thắt eo; vạt thẳng dài tới giữa đùi, không xòe; legging da ôm sát như quần bike;
   - thêm câu đối kháng: "the body is exactly as full and curvy as in the source image: NOT slimmer, NOT flat-chested, NOT a loose A-line or boxy coat".

   Giữ nguyên các chi tiết outfit đã duyệt: da hươu vàng nâu xông khói, đường chỉ gân, mũ viền lông sói xám bẻ ra sau, cổ chữ V buộc dây da, cổ tay lông sói, đai da nâu sẫm, bốt moccasin cao gối quấn dây.
4. **Hỏi yes**, rồi chạy 1 lượt `EDIT_CHARACTER_IMAGE`:
   - `character_id` = `14753a8e-…`;
   - `source_media_id` = media_id Body mới;
   - EDIT một lần từ Body gốc, không EDIT tiếp từ v3.
5. Tải ảnh về `refs/nora_outfit_v4.jpg`, đặt cạnh ảnh body cho user so form. Chỉ khi user duyệt mới xóa logo, upload lại, PATCH `media_id`.
6. Cập nhật script-v5:
   - §1, dòng "Ref đã upload": Body mới;
   - §2: tiêu đề Outfit và CHARACTER_LOCK;
   - §7, khối `[ID-LOCK]`: đổi "knee-length parka" cho khớp ảnh đã duyệt, thêm BODY LOCK.
7. Cập nhật skill bài học 60, phần bằng chứng: v3 hỏng form vì đặt bố cục trước body và vì áo parka xòe; ghi lại công thức v4 nếu đạt.

## 4. Sau khi Outfit được duyệt

- **Bước 3:** sinh 8 ref còn lại: Leader, Old Woman, Strongest, Strongest Spear, Cave Hyena, Ember Bundle, Pech Valley, Cave Mouth. Tổng 8 lượt, cần user nói yes. Đều là 16:9 (Rule 5); xóa logo từng ảnh.
- **Tạo scenes:** tạo theo storyboard §5 và prompt §7 (hiện đã có prompt từ MASTER-FIRE đến A2-11).
  - Placeholder (`[ID-LOCK]`, `[WET]`, `[HAIR]`, `[SETTING-*]`, `[END-*]`) phải thay bằng văn bản đầy đủ.
  - PATCH `duration`: MASTER-FIRE 10, EST-01 6, EST-02/03 4, còn lại 8.
  - `character_names` dùng TÊN entity, không dùng UUID; tối đa 7 ref.
- **Prompt Act 3–5:** chưa viết; viết sau khi user duyệt Act 2.
- **Clip đầu tiên:** MASTER-FIRE (clip khó nhất). Kèm 1 clip POV để thử khóa mặt.

## 5. Những gì đã xong trong phiên này

- Bỏ Child khỏi kịch bản:
  - A2-10: C (râu rậm) gặm xương;
  - A3-08: Người Mạnh Nhất chỉ giọt máu;
  - A5-06: Người Già trao pyrite của chính bà;
  - số người: ngoài hang 5, đi săn 7 + Nora, trong hang 9 + Nora.
- Lock Rule 46 vào:
  - `CLAUDE.md`, `AGENTS.md`, `setup.py` (`_CRITICAL_RULES`);
  - `skills/fk-time-travel-vlog.md` (bài học 60; sửa bài học 34, 40, 47 và mục outfit ở đầu file);
  - `.agents/skills/fk-time-travel-vlog/SKILL.md`, tạo lại từ skills/;
  - memory `feedback_outfit_on_body.md`.
- script-v5 đã đổi refs `N3` → `N2` (Nora + Nora Outfit) và bỏ `Nora Body` khỏi mọi danh sách ref.
- Chưa commit.
