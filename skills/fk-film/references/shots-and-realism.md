# Storyboard, Cỡ Cảnh Điện Ảnh & Chuẩn Chân Thực 35mm (Narrative Film)

> **Quy chuẩn điện ảnh ngôi thứ ba (`fk-film`):** Toàn bộ hình ảnh được ghi nhận qua lăng kính điện ảnh 35mm Panavision Anamorphic khách quan. Người xem là nhân chứng vô hình; máy quay không bao giờ hiện diện trong câu chuyện. Không sử dụng góc quay selfie hay thiết bị di động.

Đọc ở **Bước 4** của quy trình `fk-film`.

---

## 1. Ethnicity Lock & Period Lock (Khóa Dân Tộc & Thời Kỳ Lịch Sử)

- **Nhân vật & Quần chúng:** Mọi người xuất hiện trong khung hình (thủy thủ, lính canh, người dân, thương nhân) phải mang đúng đặc điểm nhân trắc học và phục trang lịch sử chuẩn xác của thời kỳ/bối cảnh.
- **PERIOD LOCK:** Cấm tuyệt đối các chi tiết lệch niên đại (đồng hồ, vải tổng hợp hiện đại, đinh ốc kim loại công nghiệp, khóa kéo). Ánh sáng bối cảnh chỉ sử dụng nguồn sáng tự nhiên: ánh mặt trời, ánh trăng, đuốc lửa, đèn dầu.
- **Tôn trọng văn hóa:** Không làm méo mó hoặc biếm họa tôn giáo, tín ngưỡng. Cảnh chiến đấu thể hiện qua xung lực, chấn động môi trường và tàn tích, tránh bạo lực máu me phản cảm để không vi phạm bộ lọc AI (`UNSAFE_GENERATION`).

---

## 2. Bảng Phân Cảnh Storyboard & Bảng Vật Lý

### 2.1. Bảng Storyboard Toàn Video
Bắt buộc hoàn thành trước khi chuyển thể sang Structured Prompt JSON:

| # | Hồi (Act) | Beat kịch tính | Cỡ cảnh & Ống kính | Hành động (3 pha) | Thoại (Nhân vật & Số từ) | Điểm chuyển vào | Điểm chuyển ra |
|---|---|---|---|---|---|---|---|

### 2.2. Bảng Vật Lý Từng Clip (Rule 41, 51)
Kiểm soát tính chân thực cơ học trước khi gửi lệnh sinh video:

| Cảnh | Vị trí máy & Góc nhìn | Thực thể có mặt ở giây 0 | Hướng chuyển động & Gia tốc | Tác động môi trường (Khói, nước, đá vôi) | Điểm thoát khung |
|---|---|---|---|---|---|

---

## 3. Ngôn Ngữ Góc Máy & Cỡ Cảnh Điện Ảnh (Cinematic Composition)

Tỷ lệ và cỡ cảnh trong phim điện ảnh được phân bổ linh hoạt theo nhịp kịch tính:

| Cỡ cảnh | Tên thuật ngữ | Ống kính | Chức năng kịch tính |
| :--- | :--- | :--- | :--- |
| **Toàn cảnh cực rộng** | `Extreme Wide Shot (EWS)` | Anamorphic 24mm | Thiết lập không gian vĩ đại (đại dương bão táp, vách đá Clashing Rocks, Điện Thờ Cây Vàng). Nhân vật là chấm nhỏ giữa thiên nhiên. |
| **Toàn cảnh** | `Wide Shot (WS)` / `Full Shot` | 35mm | Bao quát chuyển động tập thể, bố cục dàn trận, tương tác giữa tàu và sóng biển. |
| **Trung cảnh** | `Medium Shot (MS)` | 50mm | Đối thoại tương tác 2 người (Two-shot), đấu kiếm, kéo dây buồm. |
| **Cận cảnh trung bình** | `Medium Close-up (MCU)` | 65mm / 85mm | Tập trung biểu cảm khuôn mặt từ ngực trở lên, khóa vóc dáng và thần thái chỉ huy của Nora. |
| **Cận cảnh & Đặc tả** | `Close-up (CU)` / `Macro (ECU)` | 100mm Macro | Biểu cảm ánh mắt căng thẳng, rạch bụng cá, ký tự vàng kim hiện hình trên da cừu, giọt mồ hôi rơi trên cán kiếm. |

*Chuyển động máy quay:* Kết hợp mượt mà giữa **Slow Push-in Dolly** (kéo cảm xúc), **Crane / High-angle tilt** (mở rộng tầm nhìn), **Steadicam Tracking** (bám sát nhân vật chạy), và **Handheld Drama** (rung lắc tự nhiên có chủ đích trong cảnh hỗn chiến). Tuyệt đối không để 2 cảnh liền nhau trùng cỡ cảnh và góc máy.

---

## 4. Chuẩn Chân Thực Hình Ảnh 35mm — Chống CGI & Bóng Nhựa

Mọi clip phim phải tuân thủ nghiêm ngặt phong cách hình ảnh điện ảnh:

- **Style string chuẩn điện ảnh:**
  `35mm film, cinematic documentary realism, Panavision anamorphic lens, natural organic lighting, subtle film grain, deep focus, photorealistic, tactile textures`
- **Kết cấu vật liệu thực tế:** Gỗ sồi vỏ tàu nứt nẻ đóng muối mặn, da thuộc mòn xước sần sùi, kim loại đồng cổ oxy hóa ánh xanh, đá vôi thô ráp bám bụi trắng.
- **Ràng buộc đối kháng (Negative Constraints):**
  `Strictly NO CGI, NO plastic skin, NO 3D render sheen, NO floating devices, NO modern objects, NO text overlays, NO artificial lens flares.`
