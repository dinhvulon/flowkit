# Character Bible — Khóa Nhân Vật, Giọng & Bộ Reference (Chuẩn Điện Ảnh Ngôi Thứ Ba)

> **Quy chuẩn điện ảnh ngôi thứ ba (`fk-film`):** Áp dụng §1 (`CHARACTER_LOCK` dán cố định vào entity, không sửa giữa các clip), §2 (`VOICE_LOCK` và phong cách thoại), §3 (mỗi nhân vật một voice id riêng theo `voice-bible.md` §0), §5–6 (mặt + Body đã mặc đồ theo Rule 46), §7 (thiết kế Turnaround Sheet 16:9 theo Rule 58). Không có vlogger, không có selfie, không góc nhìn điện thoại.

Đọc ở **Bước 3** của quy trình `fk-film`.

---

## 1. `CHARACTER_LOCK` — Khóa ngoại hình nhân vật

Một khối cố định, **dán nguyên văn vào entity `description` của nhân vật và KHÔNG sửa giữa các clip**. Điều này đảm bảo tính nhất quán khuôn mặt và nhận diện xuyên suốt toàn bộ bộ phim.

Bao gồm: khuôn mặt (tuổi ≥19, dáng mặt, mắt, đặc điểm da/tàn nhang), tóc (màu sắc, kiểu buộc, phụ kiện cố định), trang phục thời kỳ (chất liệu, màu sắc, phom dáng cổ điển — không dùng chất liệu công nghiệp hiện đại), và mô tả chất giọng (`voice_description`).

**Quy tắc góc máy điện ảnh:** Tuyệt đối không mô tả thiết bị ghi hình (camera, điện thoại, màn hình) trong `CHARACTER_LOCK` hay bất cứ đâu đi vào prompt. Góc máy chỉ được định nghĩa bằng các thuật ngữ điện ảnh chuẩn trong khối `camera` (`third-person cinematic camera; the camera itself is never seen`).

Mẫu chuẩn:
```text
CHARACTER_LOCK:
Nora, a 26-year-old Western woman with a heart-shaped face, hazel-green eyes, dense freckles across nose and cheeks,
bright copper-red hair in a high braided knot bound with weathered leather cords, a few loose strands at the temples,
wearing an era-appropriate maritime seafarer costume: dark navy linen tunic under a weathered oiled-leather corslet with dull brass buckles, cross-chest leather bandolier, fitted charcoal wool breeches, and tall calf-high seafaring boots.
Voice: kore — firm, resolute, mid-pitched commanding female seafarer voice.
```

*Lưu ý:* Tên trong `CHARACTER_LOCK`, tên entity và tên người nói trong `video_prompt` phải **trùng nhau tuyệt đối**.

---

## 2. `VOICE_LOCK` — Khóa tính cách & Ngữ điệu thoại

`CHARACTER_LOCK` khóa ngoại hình và chất giọng; tính cách và cách thoại (nhân vật là ai, nói nhanh hay điềm tĩnh, nhịp điệu dứt khoát hay trầm ngâm, sợ điều gì, không bao giờ nói điều gì) được khóa bằng `VOICE_LOCK`. 

Ghi `VOICE_LOCK` vào `script.md` ngay dưới bảng nhân vật, không sửa giữa các clip. `VOICE_LOCK` là kim chỉ nam để biên kịch viết thoại; nội dung đi vào prompt video là câu thoại cụ thể và tag chỉ dẫn cảm xúc trong ngoặc đơn (`speech.dialogue`).

---

## 3. Hệ thống Giọng Điện Ảnh (Multi-Character Voice System — Rule 35)

- **Mỗi nhân vật có thoại một voice id riêng** lấy từ danh sách 30 giọng chuẩn Pinhole / Gemini-TTS ở `voice-bible.md` §0.
- Thoại nhúng thẳng trong sub-clip theo `duration` (Rule 49):
  - 4s: 0 từ hoặc 6–8 từ
  - 6s: 12–15 từ
  - 8s: 18–22 từ
  - 10s: 24–28 từ
- Định dạng thoại trong timeline hành động: `Nora says (commanding, breathless): "Hold the helm! Don't let the swell take us!"` để mô hình video tự động đồng bộ khẩu hình diễn xuất tự nhiên.
- Mặt của người nói bắt buộc phải xuất hiện trong khung hình tại đúng khoảnh khắc nói. Khi nhân vật khác nói, nhân vật còn lại khép môi, lắng nghe hoặc phản ứng bằng ánh mắt.

---

## 4. Ngôn ngữ & Đối thoại trong Phim Điện Ảnh

- Trong phim điện ảnh, các nhân vật giao tiếp với nhau bằng đối thoại kịch tính (Dramatic Dialogue), phục vụ cốt truyện và xung đột trực tiếp.
- Tuyệt đối không có lời dẫn độc thoại giải thích cho khán giả, không có xưng hô với người xem.
- Đối thoại ngắn gọn, giàu tính hành động, mang ẩn ý (*subtext*).

---

## 5. Bộ Reference Nhân Vật: Mặt + Body đã mặc trang phục (Rule 46, 58)

- Mỗi nhân vật chính có đúng **2 reference entities**:
  1. `<Tên>`: Ảnh chân dung góc rộng / cận cảnh khuôn mặt và mái tóc.
  2. `<Tên> Body <Trạng thái trang phục>`: Sheet 3 góc (chính diện, 3/4, sau lưng) **đã mặc hoàn chỉnh trang phục của phân đoạn đó**, tạo từ Body trần gốc qua công thức EDIT. Không tạo entity Trang phục (`Outfit`) riêng lẻ.
- Trong mọi cảnh quay, `character_names` truyền vào video model theo danh sách: `["<Tên>", "<Tên> Body <Trạng thái>", <ref sinh vật / bối cảnh / đạo cụ xuất hiện trong khung>]` (tối đa 7 entities / clip theo giới hạn Omni Flash).
- **Khóa trang phục thuần ảnh tham chiếu (Pure Reference Lock — Rule 52):** Trong `video_prompt`, không tự tả lại chi tiết hoa văn trang phục bằng văn bản dài dòng. Chỉ trỏ thẳng vào reference sheet đã duyệt: `"[Character] wears the exact historical outfit shown in the [Character] Body reference sheet. From the first frame to the last, [Character] is fully dressed in the complete outfit without variations."`
- **Khóa tỷ lệ vóc dáng (Body Proportion Lock — Rule 52):** Đưa khối định nghĩa vóc dáng lên sớm ngay sau `SHOT:` để chống méo mó hoặc co rút hình thể do góc quay.

---

## 6. Công Thức Outfit Lock — Mặc trang phục lên Body trần gốc

1. Lấy `source_media_id` của Body trần gốc (3 panel cắt ngang vai, không lộ mặt).
2. Tạo prompt `EDIT_CHARACTER_IMAGE` miêu tả chi tiết trang phục may đo ôm sát vóc dáng gốc.
3. Chạy lệnh sinh ảnh -> Tải về -> Chạy `tools/remove_watermark_from_image.py` -> Upload lại lấy UUID sạch (Rule 28).
4. Đưa lên Review Board để User duyệt form dáng và chất liệu vải trước khi đưa vào sinh video.

---

## 7. Khóa Cứng Thiết Kế Nhân Vật & Sinh Vật — `/fk-character-design` (Rule 58 BẮT BUỘC)

BẮT BUỘC áp dụng runtime `/fk-character-design` để thiết kế reference sheet 16:9 cho toàn bộ Nhân vật và Sinh vật chủ chốt trước khi sinh video:

| Thực thể | Quy chuẩn thiết kế 16:9 | Chi tiết kỹ thuật |
| :--- | :--- | :--- |
| **Nhân vật chính (`<Tên> Body`)** | Turnaround Sheet 3 góc (Chính diện, 3/4, Sau lưng) | Khóa 5 chỉ số nhân trắc học: chiều cao, tỷ lệ đầu/thân, tỷ lệ chân, đường chân đế bằng phẳng. |
| **Sinh vật / Quái thú chủ chốt** | Creature Turnaround Sheet 16:9 (3 panel: 3/4 Trái, 3/4 Phải, Cận cảnh đầu/mắt) | CẤM ẢNH ĐƠN 1 GÓC. Khóa kết cấu vảy chitin gồ ghề, sẹo chiến tích bất đối xứng, rãnh sừng, lệnh cấm khói thở trắng đặc. |
| **Đạo cụ cố định (kiếm, la bàn, bản đồ)** | Permanent Prop Geometry | Tả bằng hình học cụ thể, chất liệu đồng/thép cổ, cách đeo nẹp bên hông, và nêu rõ nó KHÔNG phải cái gì. |
| **Nhân vật phụ trong đoàn** | Bone & Face Structure Layer | Đảm bảo các nhân vật nam/nữ trong cùng nhóm khác biệt rõ ràng về khung xương mặt, độ dày râu tóc, vóc dáng để không bị trộn lẫn khuôn mặt khi đứng cạnh nhau. |
