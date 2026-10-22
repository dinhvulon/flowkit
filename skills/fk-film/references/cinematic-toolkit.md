# Cinematic Toolkit & Upstream Subagents Cho Phim Điện Ảnh (Narrative Film)

> **Quy chuẩn điện ảnh ngôi thứ ba (`fk-film`):** Tài liệu này hướng dẫn cách kết hợp bộ subagent điện ảnh chuyên nghiệp để xây dựng kịch bản, thiết kế reference và đạo diễn hình ảnh cho phim điện ảnh kể chuyện. Mọi góc máy đều là góc nhìn điện ảnh khách quan (Third-person cinematic camera, người xem vô hình).

---

## 0. Bảng Ánh Xạ Subagent Viết Kịch Bản & Thiết Kế Điện Ảnh

| Subagent | Chuyên Môn | Output Cung Cấp Cho Kịch Bản / Reference |
| :--- | :--- | :--- |
| **`/fk-character-design`** | Thiết kế Nhân vật & Sinh vật Chủ Chốt (Rule 58) | Chuẩn Turnaround Sheet 16:9 đa góc (4 góc nhân vật, 3 panel sinh vật), khóa 5 tầng DNA anchors (tỷ lệ, xương sọ, biểu bì Rule 57, đạo cụ, cấm khói thở trắng) |
| **`/fk-action-choreography`** | Vũ đạo hành động & an toàn cơ học AI | 3 pha động học điện ảnh (chuẩn bị, ra đòn, thu thế), từ vựng né/săn an toàn chống méo giải phẫu |
| **`/fk-add-material`** | Image Material & Visual Style | Style instruction, lighting 35mm anamorphic, chống bóng nhựa CGI |
| **`/fk-cinematic-transitions`** | Kỹ thuật nối cảnh & nhịp chuyển màn | Match-on-action, foreground wipe, whip pan, J-cut / L-cut |
| **`/fk-camera-guide`** | Đạo diễn hình ảnh & ngôn ngữ ống kính | 5 tầng prompt, cỡ cảnh (Wide/Medium/Close-up/Macro), chuyển động máy (Dolly, Crane, Tracking, Dutch Angle) |
| **`/fk-sound-design`** | Thiết kế âm thanh & Mastering | Foley hiện trường, tiếng động ma thuật/sinh vật, master chuẩn −14 LUFS / −1 dBTP |

---

## 1. Vũ Đạo Hành Động Điện Ảnh — 3 Pha Động Học (`/fk-action-choreography`)

Hành động trong phim luôn tuân thủ cấu trúc 3 pha để đảm bảo mô hình video AI diễn hoạt mượt mà, không bị vỡ giải phẫu:

* **Pha 1 (`0-3s`): Chuẩn bị (Anticipation / Stance)**  
  Hạ trọng tâm, siết chặt chuôi kiếm/vũ khí, khóa ánh mắt vào mục tiêu. Mọi thực thể và đạo cụ đã hiện diện ổn định trong khung hình từ giây 0 (`already in place`).
* **Pha 2 (`3-6s`): Ra đòn (Execution / Impact)**  
  Một đòn duy nhất theo một quỹ đạo rõ ràng: vung kiếm, phóng lao, nhảy né, trượt đất. Mô tả tác động lên môi trường xung quanh (đất đá tung bay, rêu bụi văng, mặt nước sủi bọt), tuyệt đối không tả cảnh đâm xuyên thịt máu me để tránh bị chặn kiểm duyệt (`UNSAFE_GENERATION`).
* **Pha 3 (`6-8s`): Thu thế & Neo giữ (Recovery / Anchorage)**  
  Chân ghì chặt đất, ổn định lại trọng tâm, ngực phập phồng lấy lại nhịp thở; bụi đá lắng xuống, khung hình ổn định.

### Bảng Từ Vựng An Toàn Chống Méo Hình:

| Hành động | ❌ Dễ méo / Bị bộ lọc chặn | ✅ Viết chuẩn điện ảnh |
| :--- | :--- | :--- |
| Đâm vũ khí vào quái thú | `sword pierces the beast's heart, blood sprays` | `thrusts the bronze blade forward in one clean straight line toward the carapace; sparks and chitin dust burst out as the creature recoils` |
| Bắn tên / Phóng lao | `shoots five arrows in two seconds` | `draws the heavy recurve bow to her cheek, releasing one single arrow that streaks diagonally across the frame` |
| Quái thú lao tới | `monster jumps straight into the lens` | `the beast charges diagonally from screen-left toward the stone pillar, massive claws churning limestone debris` |
| Nhảy né đòn | `she does an acrobatic backflip` | `she drops low and slides behind the granite outcrop as the claw sweeps past above her head` |
| Va chạm vật lý | `wrestles the creature directly on the ground` | Giữ khoảng cách một sải tay; thể hiện xung lực qua mặt đất nứt, đá sạt lở và hơi thở dồn dập |

---

## 2. Diễn Xuất Cảm Xúc Qua Triệu Chứng Cơ Thể (`/fk-scriptwriter`)

Mô hình AI không hiểu các tính từ cảm xúc trừu tượng (*"she feels scared"*). Trong các cảnh cận (Close-up) và trung cận (Medium Close-up), bắt buộc mô tả bằng **triệu chứng cơ thể hữu hình**:

| Cảm xúc | Triệu chứng cơ thể thể hiện trong Prompt |
| :--- | :--- |
| **Sợ hãi / Căng thẳng** | `rapid shallow chest breathing, jaw clenched tight, knuckles whitening around the leather hilt, gaze fixed` |
| **Quyết tâm / Lãnh đạo** | `jaw set firmly, eyes narrowing with cold resolve, a single sharp decisive nod to the crew` |
| **Kinh ngạc / Choáng ngợp** | `sudden complete stillness, lips parting without a sound, breath catching in throat, dilated pupils` |
| **Kiệt sức** | `shoulders sagging with heavy fatigue, labored breathing, leaning shoulder against the damp stone wall` |
| **Nghi ngờ / Cảnh giác** | `head tilting subtly, eyes narrowing, posture shifting weight back onto the rear leg, hand hovering near sword` |

*Vòng biến chuyển cảm xúc (Emotional Arc):* Mỗi cảnh 8s nên có sự chuyển dịch: `0-3s` cảnh giác $\to$ `3-6s` biến cố bất ngờ $\to$ `6-8s` phản ứng quyết liệt hoặc chấp nhận tình thế.

---

## 3. Bộ Công Cụ Hồi Hộp Điện Ảnh (Cinematic Suspense Toolkit)

1. **Ticking Clock (Áp lực thời gian tự nhiên):**  
   Thủy triều đang dâng ngập bãi đá cạn, mặt trời sắp khuất sau rặng núi để lại bóng đêm cho quái thú săn mồi, ngọn đuốc dầu sắp lụi tàn.
2. **Blind Spot (Góc khuất kịch tính):**  
   Nhân vật đứng ở tiền cảnh bên trái; 2/3 hậu cảnh bên phải là vòm hang tăm tối. Mối đe dọa (đôi mắt phát quang hoặc vảy quái thú) đã ẩn hiện từ giây 0 nhưng chỉ lộ diện hoàn toàn khi ánh chớp lóe lên.
3. **Delayed Reveal (Trì hoãn tiết lộ):**  
   Shot A: Cận cảnh khuôn mặt nhân vật biến sắc khi nhìn về phía trước. Cắt sang Shot B: Góc nhìn toàn cảnh hé lộ thực thể khổng lồ đang sừng sững trước mặt họ.
4. **Sonic Isolation (Im lặng kịch tính):**  
   Khoảnh khắc áp sát nguy hiểm: Hoàn toàn không có thoại (`Strictly NO spoken dialogue`), tắt hẳn nhạc nền, chỉ còn tiếng gió lùa qua khe đá, tiếng thở nén và tiếng tim đập dồn dập.
5. **Time Dilation (Giãn nở thời gian):**  
   Kéo dài một khoảnh khắc sinh tử thành trọn vẹn 1 clip 4s: Giọt nước biển rơi chạm vào mặt da cừu làm bừng sáng ký tự vàng kim, hoặc mũi tên trúng vào sợi dây thừng bẫy đá.

---

## 4. Quản Lý Trạng Thái Trang Phục Nhân Vật (Wardrobe Continuity Ledger)

Khi nhân vật trải qua các thử thách khốc liệt làm thay đổi trang phục (ướt sũng sau khi đắm tàu, dính bùn đất khi luồn qua mê cung):
* Mỗi trạng thái là một ảnh reference riêng: `<Tên> Body`, `<Tên> Body Wet`, `<Tên> Body Battle Damaged`.
* Được tạo bằng lệnh `EDIT_CHARACTER_IMAGE` từ Body trần gốc (Rule 46), không xâu chuỗi từ ảnh trạng thái trước đó.
* Trong `video_prompt`, chỉ định đúng entity tương ứng: `character_names: ["Nora", "Nora Body Wet", ...]`.

---

## 5. Thiết Kế Âm Thanh & Hòa Âm Điện Ảnh (`/fk-sound-design`)

* **Hòa âm đa tầng:** Tách bạch rõ 3 tầng âm thanh: (1) Thoại nhân vật dứt khoát, rõ khẩu hình; (2) Tiếng động môi trường (tiếng sóng, tiếng gió rít qua hẻm đá, tiếng đá vôi lở); (3) Nhạc nền giao hưởng kịch tính.
* **Tiêu chuẩn phát sóng:** Master âm thanh đạt chuẩn quốc tế **−14 LUFS** và giới hạn đỉnh **−1 dBTP** để đảm bảo chất lượng âm thanh điện ảnh đồng nhất trên YouTube và màn ảnh lớn.
