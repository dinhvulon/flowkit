# Kịch bản v6 — Thoại sinh tồn, cảnh 14–75 (Neanderthal 51ka)

**Trạng thái:** ĐÃ ÁP DỤNG vào DB và `clips.json` (2026-10-07, user duyệt S1–S5). `video_prompt` đầy đủ nằm trong DB và `clips.json`; file này chỉ là bản đọc thoại. Cảnh 63, 70, 71, 73 đã xóa khỏi DB (S3).
**Nguồn đã review:** `PROMPTS_TOAN_TIENG_VIET_14_TO_75.md`, `FULL_PROMPTS_SCENE_11_TO_75.md`, mảng `ACT2_EXPANDED` (cảnh 14–20).
**Chuẩn áp dụng:**
- 18–22 từ mỗi clip 8s, chia 3 mốc (skill mục 10, chốt 2026-10-07).
- `VOICE_LOCK` và checklist chống giọng AI (`voice-bible.md` §1, §4, §6).
- story-engine: chuỗi nhân quả, thất bại có hậu quả, cảnh cuối không thoại.

---

## A. Review bản hiện tại

### A1. Lỗi làm hỏng clip nếu gen (phải sửa)

| # | Lỗi | Cảnh |
|---|---|---|
| 1 | **Thoại lệch khỏi hành động của chính cảnh đó.** Lời của cảnh N lại tả cảnh N±1 (ví dụ cảnh 23 đang thử chiều gió nhưng thoại tả đàn bò; cảnh 33 đang xẻ thịt nhưng thoại tả nghi lễ tạ ơn) | 23, 24, 25, 31–36, 44–52, 54–56 |
| 2 | **Nora tự gọi tên mình ở ngôi thứ ba** ("Nora darts…", "onto Nora's cheek") | 48, 49, 53, 56, 57 |
| 3 | **Nora không có trong khung nhưng vẫn có thoại, trong khi mặt người bản địa lộ rõ** → giọng Laomedeia sẽ phát ra từ miệng họ (Bài học 49) | 16, 18, 26, 28–31, 33, 36, 39, 43, 45, 47, 48, 54, 55 |
| 4 | **Thiếu ref nhân vật đang diễn**: Old Woman / Leader / Strongest có hành động nhưng `refs` chỉ có Nora | 38, 60, 63, 64–67 |
| 5 | **Chưa có entity `Steppe Bison`** trong project, mà 9 cảnh săn cần nó (Rule 3) | 24–34 |
| 6 | **Vi phạm luật cấm cảnh ăn uống** (HANDOFF luật 2, chốt 2026-10-07): ăn tủy xương, tiệc nướng, miếng bít tết | 34, 51, 52 |
| 7 | Leader được gọi là "Torak" trong thoại. Nora không hiểu tiếng của họ thì không thể biết tên ông | 19, 24, 29, 33, 43, 67 |

### A2. Vì sao thoại nghe như phim tài liệu
- **Gần như mọi câu đều tả lại thứ đang có trên hình** ("She sets down a folded birch bark bowl…", "Torak points at empty hanging racks…"). Đây là giọng người dẫn phim tài liệu, không phải người đang cố sống.
- **Từ sách giáo khoa và số liệu:** hypothermia, convective, carnassial, "seventy-mile-an-hour", "two-meter", "100kg", "fifty millennia".
- **Câu chốt khẩu hiệu:** "humanity's oldest ceremonial jewelry", "unbreakable human spirit echoes forever", "They did not merely survive… they lived". Voice-bible cấm.
- **Nora chỉ đứng xem.** Hành động của cô trong bản cũ gần như toàn "tường thuật / thán phục / mô tả". Cô không thử, không hỏng, không sợ, không đùa. Không có cảnh nào vì lỗi của cô mà tình hình tệ hơn.
- **Act 5 quá dài và toàn tổng kết.** Từ khi bầy linh cẩu rút (cảnh 49) tới cảnh 75 là ~3,5 phút; riêng cảnh 70–74 là 5 câu khẩu hiệu liên tiếp.

---

## B. Đề xuất đổi cấu trúc (chờ bạn chọn: giữ hay đổi)

Thoại v6 bên dưới được viết theo bản **đã đổi**. Mục nào bạn không chọn thì báo, mình viết lại thoại các cảnh đó theo hành động cũ.

| # | Đề xuất | Cảnh | Lý do |
|---|---|---|---|
| **S1** | **Cú lao của con bò là lỗi của Nora.** Cảnh 26: Thủ Lĩnh bảo cô nấp sau đá. Cảnh 27: cô nhổm lên lấy góc quay đẹp, con bò phát hiện ra cô. Cảnh 31–32: cô nhận lỗi. Cảnh 48: cô chuộc lỗi bằng cách mồi lửa cho đuốc của Thủ Lĩnh | 26, 27, 31, 32, 48 | story-engine: cao trào phải do lỗi của vlogger gây ra. Persona trong `VOICE_LOCK`: "liều, đứng quá gần để lấy cảnh quay" |
| **S2** | **Bỏ 3 cảnh ăn, thay bằng mạch "Big Guy":** cảnh 34 anh quăng gói thịt cho Nora vác; cảnh 47 anh bị linh cẩu cào xước tay; cảnh 51–52 Nora sơ cứu, anh lần đầu nhìn cô | 34, 47, 51, 52 | Tuân luật cấm cảnh ăn uống. Khép mạch quan hệ đã gieo từ cảnh 18 ("chưa nhìn tôi lần nào") |
| **S3** | **Rút gọn Act 5:** cắt cảnh 63, 70, 71, 73 (thoại cho các cảnh này vẫn có sẵn nếu bạn giữ) | 63, 70, 71, 73 | story-engine §12: sau payoff 45–60s, không có câu chủ đề |
| **S4** | **Đổi góc máy chống lỗi miệng:** chuyển sang selfie qua vai (Nora 1/3 tiền cảnh), hoặc người bản địa quay lưng / chỉ thấy tay | xem lỗi A1-3 | Bài học 49 |
| **S5** | **Sửa ref:** thêm ref cho các nhân vật đang diễn; tạo entity `Steppe Bison`; thêm `Strongest Spear` ở các cảnh có giáo | xem A1-4, A1-5 | Rule 3, Rule 46 |

---

## C. Khóa liên tục (dán vào prompt từ cảnh ghi bên dưới)

| Đạo cụ / trạng thái | Từ cảnh | Tới cảnh |
|---|---|---|
| Tấm da gấu choàng vai Nora; ở cảnh 20 cô gấp lại đặt lên gờ đá | 14 | 20 (dùng lại ở 59) |
| Gói thịt bọc da trên vai trái Nora | 34 | 38 |
| Vết xước, sau đó là băng da, ở cẳng tay trái Strongest | 47 (băng từ 52) | 75 |
| Một vệt son đỏ ngang gò má phải Nora | 56 | 73 |
| Móng đại bàng đen dài ~6 cm đeo dây da trước ngực Nora | 58 | 74 |
| Viên pyrite trong tay trái Nora. Đây là viên cô dùng ở cảnh 10, do Bà Lão giữ lại | 65 | 72 |
| Bà Lão mặc đúng như ảnh ref; bỏ "áo choàng lông sói" ở cảnh 64 | 64 | 66 |

**Các mối nối cần khớp tư thế (Rule 44):**
- 19→20: Thủ Lĩnh nhìn ra cửa hang → bước ra cửa hang.
- 27→28: Nora đang thụp sau tảng đá.
- 47→48: tay Nora cầm cành thông cháy ngay từ frame 0.
- 49→50: Nora đang nhìn ra màn đêm.
- 56→57: tay Nora vẫn chạm má → Bà Lão nắm lấy tay đó.
- 68→69: "Don't look back" → cú ngoảnh lại.

---

## D. Biệt danh và giọng

- **Nora tự đặt biệt danh** cho người bản địa vì không biết tên họ: Leader = **"Chief"** (Sếp), Strongest = **"Big Guy"** (Anh To Con), Old Woman = **"Gran"** (Bà). Ba biệt danh ra mắt ở cảnh 17, 18 và 21, rồi được gọi lại ở cảnh 67 và 73.
- **Người bản địa** chỉ phát ra tiếng gằn, không thành từ, ở mốc riêng (cảnh 43, 45). Nora im trong lúc đó và không dịch lời họ.
- **Chửi thề bị bíp:** chỉ 2 lần, ở cảnh 27 và 41. Không chửi ở cảnh mở đầu và cảnh kết.
- **Nhịp im lặng 0–1s** ở cảnh 19 (Act 2), 25 (Act 3), 42 (Act 4). Act 5 kết bằng cảnh 74–75 không thoại.
- **Tag cách nói** trong ngoặc ngay sau `Nora says (...)`. Model phản ứng với tag này mạnh hơn với tính từ rải trong prompt (voice-bible §2).
- **Cảnh POV không có Nora** dùng `Nora's off-screen voice says`. Chỉ an toàn khi trong khung không có mặt người.

---

## E. Thoại từng cảnh

### Cảnh 14 · Tấm da gấu
`refs: Nora, Nora Body, Old Woman, Cave Interior` · **22 từ**

> Thay câu kết cũ vì trùng gần nguyên văn thoại cảnh 13.

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (teeth chattering, half-laughing): "Can't feel my fingers. At all. Okay." | Không cảm giác được ngón tay luôn. Ổn mà. |
| 3–6s | Nora says (cutting herself off, surprised): "No, wait— oh. Oh, that's a whole bear." | Khoan— ơ. Ơ, cả một con gấu luôn kìa. |
| 6–8s | Nora says (quiet, voice catching): "An hour ago, they shoved me out." | Một tiếng trước, họ còn đẩy tôi ra ngoài. |


### Cảnh 15 · Gắp đá nung (khuôn B)
`refs: Nora, Nora Body, Old Woman, Cave Interior` · **21 từ**

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (shivering, eyeing the bark bowl): "I'd put that right on the fire." | Tôi thì đặt thẳng cái đó lên lửa rồi. |
| 3–6s | Nora says (correcting herself): "—which burns it. Right. So she's cooking... rocks?" | —thì cháy mất. Ừ nhỉ. Vậy bà ấy đang nướng... đá? |
| 6–8s | Nora says (whispering, leaning in): "Oh, she's gonna drop that in." | Ơ, bà ấy định thả nó vào kìa. |


### Cảnh 16 · Đá rơi vào nước sôi
`refs: Old Woman, Cave Interior` · **20 từ**

> [SỬA KỸ THUẬT] Khung macro chỉ thấy tay Bà Lão + bát, KHÔNG thấy mặt bà (Bài 49). Thoại dạng `Nora's off-screen voice says`.

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora's off-screen voice says (hushed): "Okay, okay. Here it goes. Careful—" | Rồi, rồi. Thả nè. Cẩn thận— |
| 3–6s | Nora's off-screen voice says (yelping, then laughing): "Whoa—! Listen to that. It's boiling. Instantly!" | Uầy—! Nghe kìa. Sôi rồi. Ngay lập tức! |
| 6–8s | Nora's off-screen voice says (dry): "Ten seconds. My stove takes ten minutes." | Mười giây. Bếp nhà tôi mất mười phút. |


### Cảnh 17 · Uống trà thông (khuôn A)
`refs: Nora, Nora Body, Old Woman, Cave Interior` · **18 từ**

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (both hands around the bowl, blowing on it): "Hands around it first. Then sip." | Ôm bát bằng hai tay trước. Rồi nhấp từng ngụm. |
| 3–6s | Nora says (calmer): "Warms you from the inside. Shaking stops." | Ấm từ bên trong ra. Hết run. |
| 6–8s | Nora says (after a sip, surprised): "Christmas tree flavor. Thanks, Gran." | Vị cây thông Noel. Cảm ơn bà. |


### Cảnh 18 · Hơ giáo (gieo mâu thuẫn với Big Guy)
`refs: Nora, Nora Body, Strongest, Strongest Spear, Leader, Cave Interior` · **22 từ**

> [SỬA KỸ THUẬT] Bản cũ không gắn Nora mà vẫn có thoại, trong khi mặt Strongest/Leader ở trong khung → giọng Nora sẽ phát ra từ miệng họ. Chuyển selfie qua vai: Nora 1/3 tiền cảnh.

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (hushed, glancing over): "He's cooking the tip. Not burning it." | Anh ta đang hơ mũi giáo. Không phải đốt. |
| 3–6s | Nora says (explaining fast): "Dries it out. Dry wood holds a point." | Cho khô đi. Gỗ khô thì giữ mũi nhọn. |
| 6–8s | Nora says (dry, quieter): "Big Guy hasn't looked at me once." | Anh To Con chưa nhìn tôi lần nào. |


### Cảnh 19 · Kho thịt trống
`refs: Nora, Nora Body, Leader, Cave Interior` · **20 từ**

> Nhịp im lặng của Act 2: 0–1s không ai nói, chỉ tiếng gió.

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (hushed): "Wait. That's it? That's the food?" | Khoan. Hết rồi à? Đó là đồ ăn á? |
| 3–6s | Nora says (counting under her breath): "One bone. For all of them. Plus me." | Một khúc xương. Cho cả nhóm. Thêm tôi nữa. |
| 6–8s | Nora says (whispering to the lens, breath fogging): "Storm's coming. I'm the extra mouth." | Bão sắp tới. Tôi là cái miệng ăn thừa. |


### Cảnh 20 · Lệnh đi săn — Nora tự xin theo
`refs: Nora, Nora Body, Leader, Strongest, Strongest Spear, Cave Mouth` · **20 từ**

> Thêm ref `Strongest Spear`.

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (startled by the spear thud): "Whoa— that's not a dinner bell." | Uầy— đó không phải chuông gọi ăn cơm. |
| 3–6s | Nora says (dropping the bear pelt onto the ledge): "I eat their food, I hunt their food." | Tôi ăn đồ của họ thì tôi đi săn cùng họ. |
| 6–8s | Nora says (tightening her belt, following): "Nobody said no. So I'm going." | Không ai cản. Vậy tôi đi. |


### Cảnh 21 · Ra thung lũng
`refs: Nora, Nora Body, Leader, Strongest, Pech Valley` · **20 từ**

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (wind hits her, gasping): "Oh— that wind cuts right through." | Ôi— gió này xuyên thẳng qua người. |
| 3–6s | Nora says (dropping to a whisper as the Leader raises his hand): "Hand up means shut up. Got it, Chief." | Giơ tay nghĩa là im. Hiểu rồi, Sếp. |
| 6–8s | Nora says (whisper, dry): "Biggest thing I've hunted? A rabbit." | Con lớn nhất tôi từng săn? Một con thỏ. |


### Cảnh 22 · Dấu móng mới
`refs: Nora, Nora Body, Leader, Pech Valley` · **21 từ**

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (whisper): "That's a hoof. That's a huge hoof." | Đó là dấu móng. Móng to cỡ này. |
| 3–6s | Nora says (touching the edge): "Edges still sharp. Wind hasn't touched it." | Mép còn sắc. Gió chưa kịp làm lở. |
| 6–8s | Nora says (her hand inside the print, dry): "Three of my hands. Cool. Cool cool." | Bằng ba bàn tay tôi. Hay. Hay ghê. |


### Cảnh 23 · Thử chiều gió (khuôn C)
`refs: Nora, Nora Body, Strongest, Pech Valley` · **21 từ**

> Thoại cũ lệch cảnh (tả đàn bò của cảnh 24). [ĐỔI HÀNH ĐỘNG nhỏ] 6–8s: Nora tự bốc tuyết thả thử theo Strongest.

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (whisper): "No, wait— he's checking the wind." | Khoan— anh ta đang thử chiều gió. |
| 3–6s | Nora says (quick): "Blowing at us. So it can't smell us." | Gió thổi về phía mình. Nên nó không ngửi thấy mình. |
| 6–8s | Nora says (letting snow fall from her own hand): "Wind in your face. Stay in it." | Gió phả vào mặt. Cứ đứng trong gió. |


### Cảnh 24 · Lộ diện bò rừng
`refs: Steppe Bison, Pech Valley` · **19 từ**

> Thoại cũ lệch cảnh. POV không thấy mặt người → thoại `off-screen voice` an toàn. **Cần tạo entity `Steppe Bison` trước khi gen** (chưa có trong project).

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora's off-screen voice says (barely a whisper): "There. Right there. Through the trees." | Kia. Ngay kia. Sau mấy cái cây. |
| 3–6s | Nora's off-screen voice says (breath catching): "That's not a cow. That's a truck." | Đó không phải con bò. Đó là cái xe tải. |
| 6–8s | Nora's off-screen voice says (whisper): "And we're poking it with sticks." | Còn mình thì định chọc nó bằng que. |


### Cảnh 25 · Nín thở
`refs: Nora, Nora Body, Steppe Bison, Pech Valley` · **18 từ**

> Nhịp im lặng của Act 3: 0–1s không ai nói, chỉ tiếng thở và tiếng bò khịt mũi. Tiêu đề cũ ghi "4 giây" nhưng clip dài 8s, sửa lại tiêu đề.

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (after a held breath, lips barely moving): "Breathe slow. Through the nose. Quiet." | Thở chậm. Bằng mũi. Im lặng. |
| 3–6s | Nora says (whisper): "Don't move. Big animals see movement first." | Đừng cử động. Thú lớn thấy chuyển động trước tiên. |
| 6–8s | Nora says (whisper, shaky): "My heart's way too loud." | Tim tôi đập to quá. |


### Cảnh 26 · Chia gọng kìm — Nora bị bảo ở yên
`refs: Nora, Nora Body, Leader, Strongest, Strongest Spear, Pech Valley` · **20 từ**

> [SỬA KỸ THUẬT] Selfie qua vai, thêm ref Nora. [ĐỔI HÀNH ĐỘNG – S1] Thủ Lĩnh chỉ tay bảo Nora nấp sau tảng đá.

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (whisper): "He goes right. Chief goes left." | Anh ấy vòng phải. Sếp vòng trái. |
| 3–6s | Nora says (whisper): "And me? He points at the rock. Stay." | Còn tôi? Ông chỉ vào tảng đá. Ở yên. |
| 6–8s | Nora says (dry whisper): "Stay. Like a dog. Fair enough." | Ở yên. Như con cún. Cũng hợp lý. |


### Cảnh 27 · LỖI CỦA NORA — bò phát hiện cô
`refs: Nora, Nora Body, Steppe Bison, Pech Valley` · **19 từ**

> [ĐỔI HÀNH ĐỘNG – S1] Nora nhổm lên tảng đá để lấy góc quay đẹp hơn, con bò giật đầu nhìn thẳng vào cô, cô thụp xuống. Cú lao ở cảnh 28 là hậu quả từ lỗi của cô (story-engine: cao trào do lỗi của vlogger). `bleep_at` ≈ 5.8s.

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (whisper, inching up the rock): "Just a little higher. Better shot—" | Cao thêm chút nữa. Góc đẹp hơn— |
| 3–6s | Nora says (the bull's head snaps toward her; she freezes): "No no no. It's looking at me. Sh—" | Không không không. Nó đang nhìn tôi. Ch— |
| 6–8s | Nora says (voice cracking, ducking): "Down. Get down, get down—" | Xuống. Nằm xuống, nằm xuống— |


### Cảnh 28 · Bò lao vào Thủ Lĩnh
`refs: Nora, Nora Body, Leader, Steppe Bison, Pech Valley` · **18 từ**

> [SỬA KỸ THUẬT] Nora OTS thấp sau tảng đá, Thủ Lĩnh quay lưng về máy (không thấy miệng). Khớp tư thế đầu clip với cuối cảnh 27: Nora đang thụp sau đá (Rule 44).

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (screaming): "It's running! It's coming— Chief! Chief, move!" | Nó chạy! Nó lao tới— Sếp! Sếp, tránh ra! |
| 3–6s | Nora says (voice cracking): "He's not moving. Why isn't he moving?!" | Ông ấy không nhúc nhích. Sao không tránh?! |
| 6–8s | Nora says (raw scream): "Move! Please, please move!" | Tránh đi! Làm ơn, làm ơn tránh đi! |


### Cảnh 29 · Thủ Lĩnh lách người
`refs: Nora, Nora Body, Leader, Steppe Bison, Pech Valley` · **22 từ**

> [SỬA KỸ THUẬT] Như cảnh 28: Nora trong khung, Thủ Lĩnh quay lưng hoặc nghiêng.

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (screaming): "It's on him— it's right on him—" | Nó tới rồi— sát người ông ấy rồi— |
| 3–6s | Nora says (a shriek, then a gasp): "He stepped— he just stepped aside?! Oh my god!" | Ông ấy bước— ông ấy chỉ bước tránh sang?! Trời ơi! |
| 6–8s | Nora says (shaky laugh): "He waited for it. On purpose." | Ông ấy cố tình chờ nó. Có chủ đích. |


### Cảnh 30 · Big Guy đâm giáo
`refs: Nora, Nora Body, Strongest, Strongest Spear, Steppe Bison, Pech Valley` · **20 từ**

> [SỬA KỸ THUẬT] Selfie qua vai: Nora 1/3 tiền cảnh, cú đâm ở 2/3 hậu cảnh; thêm ref Nora.

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (yelling): "There's Big Guy— he's going in!" | Anh To Con kìa— anh ấy lao vào! |
| 3–6s | Nora says (yelling): "Right behind the shoulder! He's holding it there!" | Ngay sau bả vai! Anh ấy ghì chặt ở đó! |
| 6–8s | Nora says (breathless): "Don't let go. Don't let go!" | Đừng buông. Đừng buông! |


### Cảnh 31 · Con thú gục
`refs: Nora, Nora Body, Leader, Strongest, Strongest Spear, Steppe Bison, Pech Valley` · **19 từ**

> Thoại cũ lệch cảnh. [SỬA KỸ THUẬT] Nora trong khung (selfie qua vai).

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (breathless whisper): "It's going down. It's going down." | Nó gục rồi. Nó gục rồi. |
| 3–6s | Nora says (checking everyone, fast): "Is anyone hurt? Nobody's hurt. Okay, nobody's hurt." | Có ai bị thương không? Không ai cả. Ổn, không ai cả. |
| 6–8s | Nora says (shaky, quiet): "That charge was my fault." | Cú lao đó là lỗi của tôi. |


### Cảnh 32 · Tạ ơn con mồi
`refs: Nora, Nora Body, Leader, Strongest, Steppe Bison, Pech Valley` · **20 từ**

> Thoại cũ lệch cảnh. Bỏ câu "bài học đạo đức của tổ tiên" (voice-bible cấm câu chốt đạo lý). Thay bằng mặc cảm của chính Nora.

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (quietly): "No cheering. I was ready to cheer." | Không ai reo hò. Tôi thì đã định reo. |
| 3–6s | Nora says (whisper): "They're thanking it. I should thank him." | Họ đang cảm ơn nó. Tôi mới là người nên cảm ơn ông ấy. |
| 6–8s | Nora says (barely audible): "He nearly died for my shot." | Ông ấy suýt chết vì cảnh quay của tôi. |


### Cảnh 33 · Xẻ thịt bằng đá
`refs: Nora, Nora Body, Leader, Strongest, Steppe Bison, Pech Valley` · **20 từ**

> Thoại cũ lệch cảnh. [SỬA KỸ THUẬT] Selfie qua vai.

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (leaning in): "He's cutting hide with a rock." | Ông ấy rạch da bằng một hòn đá. |
| 3–6s | Nora says (impressed, dry): "Sharper than anything in my kitchen. Seriously." | Bén hơn mọi thứ trong bếp nhà tôi. Thật đấy. |
| 6–8s | Nora says (urgent): "Fast, before the cold locks it solid." | Phải nhanh, trước khi lạnh làm thịt đông cứng. |


### Cảnh 34 · Bị quăng gói thịt (THAY cảnh tủy xương)
`refs: Nora, Nora Body, Strongest, Steppe Bison, Pech Valley` · **19 từ**

> [ĐỔI HÀNH ĐỘNG – S2] Bỏ cảnh ăn tủy xương (HANDOFF luật 2: cấm cảnh ăn uống lặp). Thay bằng: Strongest buộc gói thịt bằng da rồi quăng cho Nora, cô loạng choạng đỡ và quàng lên vai. Nora vác gói này suốt cảnh 34–38.

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (catching it, winded): "Oof— so I'm carrying that. Apparently." | Hự— vậy là tôi vác cái này. Có vẻ thế. |
| 3–6s | Nora says (straining): "That's heavy. Like a soaked sleeping bag." | Nặng thật. Như cái túi ngủ ngấm nước. |
| 6–8s | Nora says (dry, shouldering it): "Fair. I earned the heavy one." | Công bằng. Tôi đáng vác gói nặng nhất. |


### Cảnh 35 · Mùi máu — tiếng cười trong rừng
`refs: Nora, Nora Body, Leader, Pech Valley` · **20 từ**

> Thoại cũ lệch cảnh (thoại cũ là của cảnh 36).

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (whisper): "Wait. He smells something. Everyone froze." | Khoan. Ông ấy ngửi thấy gì đó. Ai cũng đứng khựng. |
| 3–6s | Nora says (a distant whoop; her voice drops): "That's not wolves. Something's laughing out there." | Không phải sói. Có thứ gì đang cười ngoài kia. |
| 6–8s | Nora says (fast whisper to the lens): "We're carrying blood. We need to go." | Mình đang vác máu trên người. Phải đi ngay. |


### Cảnh 36 · Buộc đòn gánh
`refs: Nora, Nora Body, Leader, Strongest, Pech Valley` · **19 từ**

> Thoại cũ lệch cảnh. [SỬA KỸ THUẬT] Selfie qua vai, gói thịt vẫn trên vai Nora.

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (quick): "Pole across. Weight split between two." | Đòn gánh ngang vai. Chia sức nặng cho hai người. |
| 3–6s | Nora says (dry): "Knot pulled with his teeth. Whatever works." | Thắt nút bằng răng. Miễn được việc. |
| 6–8s | Nora says (urgent): "Move, move. That laughing's getting closer." | Đi, đi. Tiếng cười đó đang lại gần. |


### Cảnh 37 · Chạy về trước bão
`refs: Nora, Nora Body, Leader, Strongest, Pech Valley` · **19 từ**

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (panting hard, running): "Can't— feel— my legs. Keep going." | Không— còn cảm giác— chân. Đi tiếp. |
| 3–6s | Nora says (shouting over the wind): "They're carrying double and still beating me." | Họ vác gấp đôi mà vẫn bỏ xa tôi. |
| 6–8s | Nora says (gasping laugh): "Cave! I see the cave! Go!" | Hang! Thấy hang rồi! Đi! |


### Cảnh 38 · Về tới hang
`refs: Nora, Nora Body, Old Woman, Leader, Strongest, Cave Mouth` · **20 từ**

> Thêm ref Leader, Strongest (họ có hành động trong cảnh). Bỏ tên di chỉ "Pech de l'Azé" khỏi thoại.

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (stumbling inside, gasping): "We made it. We actually made it." | Về tới rồi. Về tới thật rồi. |
| 3–6s | Nora says (laughing): "She's smacking them. That's a hug, I think." | Bà ấy vỗ bôm bốp vào họ. Chắc ở đây thế là ôm. |
| 6–8s | Nora says (wiping snow off her brow): "And nobody got gored. Barely." | Và không ai bị húc. Suýt thôi. |


### Cảnh 39 · Cất thịt vào hốc đá
`refs: Nora, Nora Body, Strongest, Cave Interior` · **19 từ**

> [SỬA KỸ THUẬT] Strongest quay lưng/nghiêng về phía hốc đá, hoặc Nora selfie qua vai.

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (following him): "Back of the cave. Coldest rock." | Cuối hang. Chỗ đá lạnh nhất. |
| 3–6s | Nora says (explaining): "Cold keeps it. Stone keeps the noses out." | Lạnh giữ thịt. Đá chặn mấy cái mũi đánh hơi. |
| 6–8s | Nora says (uneasy): "Unless something bigger shows up." | Trừ khi có thứ gì to hơn mò tới. |


### Cảnh 40 · Bão phong tỏa
`refs: Nora, Nora Body, Cave Mouth` · **20 từ**

> Bỏ số liệu "seventy-mile-an-hour" (voice-bible cấm số liệu sách giáo khoa).

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (raising her voice over the wind): "That's the valley. Or it was." | Đó là thung lũng. Hay từng là. |
| 3–6s | Nora says (squinting into white): "Can't see the trees. Can't see anything." | Không thấy cây. Không thấy gì cả. |
| 6–8s | Nora says (pulling her collar tight): "Twenty minutes slower and we're out there." | Chậm hai mươi phút là mình kẹt ngoài đó. |


### Cảnh 41 · Tiếng cười linh cẩu
`refs: Nora, Nora Body, Cave Interior` · **19 từ**

> `bleep_at` ≈ 5.6s.

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (whisper): "Did you hear that? Tell me—" | Nghe thấy không? Nói tôi nghe đi— |
| 3–6s | Nora says (a whoop right outside; she flinches): "It's laughing. Right outside. Oh, sh—" | Nó đang cười. Ngay ngoài kia. Ôi, ch— |
| 6–8s | Nora says (fast whisper): "They followed the blood. All the way." | Chúng lần theo mùi máu. Tới tận đây. |


### Cảnh 42 · Bốn cặp mắt
`refs: Cave Hyena, Cave Mouth` · **20 từ**

> Nhịp im lặng của Act 4: 0–1s chỉ có tiếng bão. POV không thấy mặt người → `off-screen voice`. Bỏ số liệu "twice the size".

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora's off-screen voice says (barely breathing): "One, two, three... four. Four of them." | Một, hai, ba... bốn. Bốn con. |
| 3–6s | Nora's off-screen voice says (whisper): "Those aren't dogs. Way bigger than dogs." | Đó không phải chó. To hơn chó nhiều. |
| 6–8s | Nora's off-screen voice says (dry, terrified): "And we just filled the pantry." | Mà mình vừa chất đầy kho thịt. |


### Cảnh 43 · Dàn trận chặn cửa
`refs: Nora, Nora Body, Leader, Strongest, Strongest Spear, Cave Mouth` · **18 từ**

> [SỬA KỸ THUẬT] OTS từ sau lưng hai thợ săn (họ quay mặt ra ngoài), thêm ref Nora và Strongest Spear. Nora ở hàng sau, chưa làm được gì. Câu "Useless" gieo cho cảnh 46.

> 🔊 Người bản địa: `0–1s: The Leader barks one short command in a gravelly, low-pitched male voice — short guttural sounds, consonant-heavy, no recognizable words; Nora stays silent.`

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (after the bark, whisper): "Torch. Spear. Under ten seconds." | Đuốc. Giáo. Chưa tới mười giây. |
| 3–6s | Nora says (whisper): "They're blocking the whole entrance. Shoulder to shoulder." | Họ chắn kín cửa hang. Vai sát vai. |
| 6–8s | Nora says (whisper, frustrated): "And I'm behind them. Useless." | Còn tôi đứng sau. Vô dụng. |


### Cảnh 44 · Con đầu đàn thử phòng tuyến
`refs: Cave Hyena, Cave Mouth` · **20 từ**

> Thoại cũ lệch cảnh. Bỏ số liệu "100kg".

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora's off-screen voice says (whisper): "That's the big one. It's coming up." | Con to nhất kìa. Nó đang leo lên. |
| 3–6s | Nora's off-screen voice says (whisper): "Slow steps. It's testing us. Not scared." | Bước chậm. Nó đang thử mình. Không sợ. |
| 6–8s | Nora's off-screen voice says (whisper): "It's watching the torch. Not us." | Nó nhìn ngọn đuốc. Không nhìn mình. |


### Cảnh 45 · Hàng rào giáo & tiếng gầm
`refs: Nora, Nora Body, Leader, Strongest, Strongest Spear, Cave Hyena, Cave Mouth` · **19 từ**

> Thoại cũ lệch cảnh. [SỬA KỸ THUẬT] OTS sau lưng hai thợ săn.

> 🔊 Người bản địa: `3–4s: both hunters let out one wordless guttural roar together, no recognizable words; Nora stays silent.`

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (whisper, shaking): "Spears out. Banging the rock. Making noise." | Chĩa giáo. Dộng xuống đá. Làm ồn. |
| 4–6s | Nora says (right after the roar): "Bigger. Louder. Make yourself bigger." | To hơn. Ồn hơn. Làm mình to ra. |
| 6–8s | Nora says (amazed): "It stepped back. It actually stepped back!" | Nó lùi rồi. Nó lùi thật rồi! |


### Cảnh 46 · Nora lấy lửa (khuôn C)
`refs: Nora, Nora Body, Old Woman, Cave Interior` · **19 từ**

> Thoại cũ lệch cảnh. Bà Lão đưa cho Nora cành thông nhiều nhựa. Nora chuyển từ "vô dụng" sang hành động.

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (fast, hands busy): "Sappy pine. Lights fast, burns long." | Thông nhiều nhựa. Bắt lửa nhanh, cháy lâu. |
| 3–6s | Nora says (lifting the burning branch): "Their torches won't last. This one will." | Đuốc của họ sắp tàn. Cái này thì không. |
| 6–8s | Nora says (determined, to the lens): "Not standing in the back anymore." | Không đứng phía sau nữa. |


### Cảnh 47 · Con đầu đàn vồ — Big Guy bị thương
`refs: Nora, Nora Body, Strongest, Strongest Spear, Cave Hyena, Cave Mouth` · **19 từ**

> Thoại cũ lệch cảnh. [ĐỔI HÀNH ĐỘNG – S2] Răng linh cẩu sượt cẳng tay trái Strongest trước khi anh quét cán giáo (để có cảnh 51–52). [SỬA KỸ THUẬT] Nora OTS phía sau anh.

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (screaming): "It's jumping at him— look out!" | Nó nhảy vào anh ấy— coi chừng! |
| 3–6s | Nora says (crack of wood, a yelp): "He swung it like a bat— oh!" | Anh ấy vụt như cây gậy bóng chày— ôi! |
| 6–8s | Nora says (breathless): "His arm. He's bleeding. He's bleeding." | Tay anh ấy. Chảy máu. Chảy máu rồi. |


### Cảnh 48 · Nora tiếp lửa — bức tường lửa
`refs: Nora, Nora Body, Leader, Cave Hyena, Cave Mouth` · **19 từ**

> Thoại cũ lệch cảnh và Nora tự gọi tên mình ở ngôi thứ ba. [ĐỔI HÀNH ĐỘNG – S1] Ngay từ frame 0, tay Nora cầm cành thông cháy, mồi lửa cho đuốc của Thủ Lĩnh, rồi ông vung đuốc. Thêm ref Nora.

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (yelling): "Here! Take it— take the fire!" | Đây! Cầm lấy— cầm lửa đi! |
| 3–6s | Nora says (sparks flying): "Oh, they hate that. They hate that!" | Ồ, chúng ghét cái đó. Ghét lắm! |
| 6–8s | Nora says (screaming, half-laughing): "Go! Get out of here! Go!" | Cút! Cút khỏi đây! Đi! |


### Cảnh 49 · Bầy thú rút
`refs: Cave Hyena, Cave Mouth` · **19 từ**

> Thoại cũ lệch cảnh và dùng ngôi thứ ba. POV `off-screen voice`.

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora's off-screen voice says (panting): "They're backing off. They're actually leaving." | Chúng đang lùi. Chúng đi thật rồi. |
| 3–6s | Nora's off-screen voice says (tense whisper): "The big one's looking back. Don't you dare." | Con to nhất ngoái lại. Mày đừng có mà. |
| 6–8s | Nora's off-screen voice says (long exhale): "Gone. Okay. Okay. They're gone." | Đi rồi. Ổn. Ổn. Chúng đi rồi. |


### Cảnh 50 · Thở phào
`refs: Nora, Nora Body, Leader, Strongest, Cave Mouth` · **19 từ**

> Thoại cũ lệch cảnh. Đầu clip Nora đang nhìn ra màn đêm, khớp với POV cảnh 49 (Rule 44). Strongest có vết xước ở cẳng tay trái.

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (shaky, staring at her hands): "Hands won't stop. Look at them." | Tay không ngừng run. Nhìn này. |
| 3–6s | Nora says (surprised): "They're grinning at each other. They do grin." | Họ đang cười với nhau. Hóa ra họ biết cười. |
| 6–8s | Nora says (laughing, teary): "Never thought I'd see that." | Chưa từng nghĩ sẽ thấy cảnh đó. |


### Cảnh 51 · Đòi xem vết thương (THAY cảnh tiệc nướng)
`refs: Nora, Nora Body, Strongest, Cave Interior` · **21 từ**

> [ĐỔI HÀNH ĐỘNG – S2] Bỏ cảnh tiệc nướng (luật cấm ăn uống). Thay bằng: Nora thấy cẳng tay Strongest chảy máu, đòi xem, anh giật tay lại.

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (serious, fast): "Let me see that. Hey. Arm." | Để tôi xem. Này. Tay. |
| 3–6s | Nora says (he pulls it away): "He won't let me. Of course he won't." | Anh ấy không cho. Đương nhiên là không rồi. |
| 6–8s | Nora says (firm): "Clean it now or it rots. Arm." | Rửa ngay không thì nó thối. Đưa tay đây. |


### Cảnh 52 · Băng tay — lần đầu anh nhìn cô (THAY cảnh bít tết)
`refs: Nora, Nora Body, Strongest, Cave Interior` · **20 từ**

> [ĐỔI HÀNH ĐỘNG – S2] Nora rửa vết thương bằng nước tuyết ấm rồi quấn dải da. Strongest co duỗi ngón tay, rồi lần đầu nhìn thẳng vào cô (đáp lại cảnh 18). Từ cảnh này anh đeo băng da ở cẳng tay.

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (hands busy): "Snow water, then pressure. Then wrap it." | Nước tuyết, rồi ép chặt. Rồi quấn lại. |
| 3–6s | Nora says (checking his fingers): "Tight, not too tight. Fingers still pink." | Chặt, nhưng đừng quá. Ngón tay vẫn hồng. |
| 6–8s | Nora says (he looks at her; she freezes, then dry): "Oh. He's looking at me. Hi." | Ơ. Anh ấy đang nhìn tôi. Chào. |


### Cảnh 53 · Cú vỗ vai
`refs: Nora, Nora Body, Leader, Cave Interior` · **18 từ**

> Thoại cũ dùng ngôi thứ ba ("Nora's shoulder").

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (startled by the slap): "Ow— that's a big hand." | Á— bàn tay to thật. |
| 3–6s | Nora says (rubbing her shoulder, grinning): "I think that means I'm staying. Maybe." | Chắc vậy nghĩa là tôi được ở lại. Chắc thế. |
| 6–8s | Nora says (quiet, moved): "This morning I was outside. Freezing." | Sáng nay tôi còn ở ngoài kia. Chết cóng. |


### Cảnh 54 · Nghiền đất son
`refs: Nora, Nora Body, Old Woman, Cave Interior` · **20 từ**

> Thoại cũ lệch cảnh. [SỬA KỸ THUẬT] Selfie qua vai (mặt Bà Lão trong khung). Bỏ phần giảng "ý nghĩa văn hóa tâm linh".

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (curious whisper): "Red rock. Crushed to dust. For what?" | Đá đỏ. Nghiền thành bột. Để làm gì? |
| 3–6s | Nora says (watching her hands): "Fat goes in. Now it's paint. It sticks." | Cho mỡ vào. Giờ thành sơn. Bám chặt. |
| 6–8s | Nora says (hushed): "Everyone went quiet. This matters." | Mọi người im bặt. Chuyện này quan trọng. |


### Cảnh 55 · Dấu tay Thủ Lĩnh
`refs: Nora, Nora Body, Leader, Cave Interior` · **21 từ**

> Thoại cũ lệch cảnh. [SỬA KỸ THUẬT] Selfie qua vai. Bỏ câu "bản tuyên ngôn bất tử của nhân loại".

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (hushed): "His hand on the wall. Nobody talks." | Tay ông áp lên vách. Không ai nói gì. |
| 3–6s | Nora says (after the puff of red): "He blew it through a bone. Spray paint." | Ông thổi qua một ống xương. Như sơn xịt. |
| 6–8s | Nora says (whisper): "That's his hand. Right there. Forever." | Bàn tay ông đó. Ngay đó. Mãi mãi. |


### Cảnh 56 · Vệt son trên má
`refs: Nora, Nora Body, Leader, Cave Interior` · **20 từ**

> Thoại cũ lệch cảnh và sai giới tính ("She grinds" trong khi người vẽ là Thủ Lĩnh). **Khóa từ cảnh này: một vệt son đỏ ngang gò má phải của Nora.**

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (holding her breath): "He's coming over. Don't flinch. Don't flinch." | Ông đang tới. Đừng giật mình. Đừng giật mình. |
| 3–6s | Nora says (the cold ochre touches her cheek): "Oh— cold. That's on my face now." | Ôi— lạnh. Giờ nó ở trên mặt tôi rồi. |
| 6–8s | Nora says (teary, touching her cheek, dry): "I'm not crying. It's the smoke." | Tôi không khóc đâu. Tại khói. |


### Cảnh 57 · Dấu tay Nora
`refs: Nora, Nora Body, Old Woman, Cave Interior` · **20 từ**

> Thoại cũ dùng ngôi thứ ba.

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (as the Old Woman presses her hand to the wall): "Next to his. She wants mine there." | Cạnh tay ông ấy. Bà muốn tay tôi ở đó. |
| 3–6s | Nora says (red spray hits her fingers): "Don't move. Cold spray on my fingers." | Đừng động đậy. Bụi lạnh phủ lên ngón tay. |
| 6–8s | Nora says (lifting her hand, quiet): "My hand. Next to theirs. Wow." | Tay tôi. Cạnh tay họ. Trời. |


### Cảnh 58 · Móng đại bàng
`refs: Nora, Nora Body, Old Woman, Cave Interior` · **20 từ**

> Bỏ câu "humanity's oldest jewelry" (voice-bible cấm "humanity" và giảng lịch sử). **Khóa từ cảnh này: móng đại bàng đen dài ~6 cm đeo trước ngực Nora.**

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (eyes wide): "That's a claw. A bird claw. Huge." | Móng vuốt. Móng chim. To thật. |
| 3–6s | Nora says (the necklace goes over her head): "Over my head— heavier than it looks." | Qua đầu tôi— nặng hơn tôi tưởng. |
| 6–8s | Nora says (whisper, holding it to her chest): "I didn't earn this. Did I?" | Tôi đâu xứng với cái này. Đúng không? |


### Cảnh 59 · Ổ cành thông & da gấu (khuôn A)
`refs: Nora, Nora Body, Cave Interior` · **21 từ**

> Bỏ "Hour twenty" khỏi thoại vì countdown đã chèn ở hậu kỳ.

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (sleepy whisper): "Pine branches under me. Bear on top." | Cành thông bên dưới. Da gấu bên trên. |
| 3–6s | Nora says (sleepy): "Ground steals your heat. Branches keep it off." | Mặt đất hút hơi ấm. Cành thông chặn lại. |
| 6–8s | Nora says (yawning, half-laughing): "Best bed I've ever had. Honestly." | Cái giường ngon nhất đời tôi. Thật đấy. |


### Cảnh 60 · Big Guy gác đêm
`refs: Nora, Nora Body, Strongest, Cave Interior` · **21 từ**

> Bản cũ ghi "thợ săn già" nhưng không có ref → đổi thành Strongest (cẳng tay quấn băng), thêm ref.

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (whisper): "He's still up. Wrapped arm and all." | Anh ấy vẫn thức. Tay còn quấn băng. |
| 3–6s | Nora says (whisper): "Little bits of bark. All night long." | Bỏ từng mẩu vỏ cây. Suốt đêm. |
| 6–8s | Nora says (whisper, eyes closing): "If that fire dies, they come back." | Lửa mà tắt là chúng quay lại. |


### Cảnh 61 · Bình minh
`refs: Pech Valley` · **19 từ**

> POV phong cảnh → bỏ ref Nora (luật POV), thêm ref `Pech Valley`, thoại `off-screen voice`. Bỏ giọng văn tả cảnh kiểu thơ.

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora's off-screen voice says (raspy morning voice): "Morning. The storm's gone. Just gone." | Sáng rồi. Bão tan rồi. Tan hẳn. |
| 3–6s | Nora's off-screen voice says (surprised): "There's a river down there. Never saw it." | Dưới kia có con sông. Hôm qua không thấy. |
| 6–8s | Nora's off-screen voice says (quiet): "Yesterday this was all white." | Hôm qua chỗ này trắng xóa. |


### Cảnh 62 · Ra nắng
`refs: Nora, Nora Body, Cave Exterior` · **18 từ**

> Thêm ref `Cave Exterior`.

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (breathing in, squinting): "Sun. Actual sun on my face." | Nắng. Nắng thật trên mặt tôi. |
| 3–6s | Nora says (grinning): "Still freezing. Doesn't matter. Feels warm." | Vẫn lạnh cóng. Kệ. Thấy ấm lắm. |
| 6–8s | Nora says (to the lens): "Twenty-four hours. And I'm still here." | Hai mươi bốn giờ. Và tôi vẫn còn đây. |


### Cảnh 63 · Bộ tộc buổi sáng — ĐỀ XUẤT CẮT (S3)
`refs: Nora, Nora Body, Leader, Strongest, Old Woman, Cave Exterior` · **20 từ**

> Nếu giữ: thêm ref ba người, khóa số người trong khung (Bài học §2c).

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (looking around): "Everyone's up. Hides out drying already." | Ai cũng dậy rồi. Đã phơi da ra. |
| 3–6s | Nora says (noticing): "Spears get checked first. Before anything else." | Giáo được kiểm tra đầu tiên. Trước mọi thứ. |
| 6–8s | Nora says (smiling, a little sad): "Normal day for them. Not for me." | Ngày bình thường với họ. Với tôi thì không. |


### Cảnh 64 · Bà Lão bước tới
`refs: Nora, Nora Body, Old Woman, Cave Exterior` · **18 từ**

> **Bản cũ thiếu ref Old Woman → mặt bà sẽ bị vẽ ngẫu nhiên.** Bỏ "áo choàng lông sói" vì lệch với ảnh ref.

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (hearing footsteps, turning): "Footsteps behind me. Oh— good morning." | Có tiếng chân sau lưng. Ồ— chào buổi sáng. |
| 3–6s | Nora says (curious): "She's got something hidden in that fist." | Bà giấu gì đó trong nắm tay. |
| 6–8s | Nora says (smiling): "She never comes to me." | Bà chưa bao giờ tự đến chỗ tôi. |


### Cảnh 65 · Viên pyrite
`refs: Nora, Nora Body, Old Woman, Cave Exterior` · **21 từ**

> Thêm ref Old Woman. Đây chính là viên pyrite Nora dùng ở cảnh 10 (Bà Lão giữ lại). Câu cuối gọi lại câu "Three strikes" của cảnh 13.

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (as the palm opens): "No way. That's the stone. My stone." | Không thể nào. Hòn đá đó. Đá của tôi. |
| 3–6s | Nora says (voice wobbling): "The one from yesterday. My first spark." | Hòn đá hôm qua. Tia lửa đầu tiên của tôi. |
| 6–8s | Nora says (voice breaking into a laugh): "Three strikes. I still need way more." | Ba nhát. Tôi thì vẫn cần nhiều hơn thế. |


### Cảnh 66 · Chạm trán
`refs: Nora, Nora Body, Old Woman, Cave Exterior` · **21 từ**

> Thêm ref Old Woman.

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (soft, unsure): "Is a hug a thing here? Okay." | Ở đây có ôm không nhỉ? Thôi kệ. |
| 3–6s | Nora says (forehead to forehead, whispering): "Oh. Forehead. That's their hug. I'll take it." | Ồ. Chạm trán. Đó là cái ôm của họ. Tôi nhận. |
| 6–8s | Nora says (teary laugh): "Don't cry. Don't cry. Too late." | Đừng khóc. Đừng khóc. Muộn rồi. |


### Cảnh 67 · Chào bằng nắm đấm
`refs: Nora, Nora Body, Leader, Strongest, Strongest Spear, Cave Exterior` · **21 từ**

> Thêm ref Leader và Strongest (Strongest đeo băng tay). [ĐỔI HÀNH ĐỘNG nhỏ] Nora dùng tay trống vỗ ngực chào lại, không chạm vào ống kính (Rule 45). Bỏ tên "Torak": Nora không hiểu tiếng của họ thì không thể biết tên ông.

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (looking over her shoulder): "Up on the rock. Both of them." | Trên tảng đá kia. Cả hai người. |
| 3–6s | Nora says (as fists hit chests): "Fist to chest. Oh— is that for me?" | Đấm vào ngực. Ồ— là chào tôi à? |
| 6–8s | Nora says (thumping her own chest back, grinning): "Back at you, Chief. Big Guy." | Chào lại nè, Sếp. Anh To Con. |


### Cảnh 68 · Xuống dốc
`refs: Nora, Nora Body, Pech Valley` · **19 từ**

> Câu cuối mở đường cho cú ngoảnh lại ở cảnh 69 (Rule 44).

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (walking, breathing hard): "Downhill's easier. Only easy part today." | Xuống dốc thì dễ. Phần dễ duy nhất hôm nay. |
| 3–6s | Nora says (quieter): "Leaving feels wrong. Staying was never the plan." | Đi thì thấy sai sai. Mà ở lại chưa bao giờ là kế hoạch. |
| 6–8s | Nora says (to herself): "Okay. Don't look back. Don't—" | Rồi. Đừng ngoảnh lại. Đừng— |


### Cảnh 69 · Ngoảnh lại
`refs: Cave Exterior, Pech Valley` · **20 từ**

> POV, cửa hang ở xa, không có mặt người → `off-screen voice`; bỏ ref Nora.

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora's off-screen voice says (whisper): "I looked back. Of course I did." | Tôi ngoảnh lại rồi. Đương nhiên. |
| 3–6s | Nora's off-screen voice says (soft): "Smoke's still coming out. Someone fed the fire." | Khói vẫn bốc lên. Có người vừa thêm củi. |
| 6–8s | Nora's off-screen voice says (soft, smiling): "Good. Keep it going, guys." | Tốt. Giữ lửa nhé, mọi người. |


### Cảnh 70 · Selfie tổng kết 1 — ĐỀ XUẤT CẮT (S3)
`refs: Nora, Nora Body, Pech Valley` · **19 từ**

> Nếu giữ: thay hẳn câu "history books told me brutish beasts" (giảng bài + meta) bằng lời kể thất bại của chính Nora.

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (to the lens, tired grin): "Twenty-four hours. Wet, frozen, almost eaten." | Hai mươi bốn giờ. Ướt, cóng, suýt bị ăn thịt. |
| 3–6s | Nora says (wincing): "Charged by a bison. My fault, totally." | Bị bò rừng húc. Lỗi tôi, hoàn toàn. |
| 6–8s | Nora says (softer): "Painted. Given a claw. Kept alive." | Được vẽ mặt. Được tặng móng vuốt. Được cứu sống. |


### Cảnh 71 · Selfie tổng kết 2 — ĐỀ XUẤT CẮT (S3)
`refs: Nora, Nora Body, Pech Valley` · **19 từ**

> Nếu giữ: bỏ chuỗi liệt kê "family, fearless hunters, spiritual art…" (bộ ba tu từ + khẩu hiệu).

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (quiet): "And they let me in. Me." | Và họ cho tôi vào. Tôi đấy. |
| 3–6s | Nora says (shaking her head): "The stranger who almost got them killed." | Người lạ suýt khiến họ mất mạng. |
| 6–8s | Nora says (small smile): "They still gave me a bed." | Họ vẫn cho tôi chỗ ngủ. |


### Cảnh 72 · Hai kỷ vật
`refs: Nora, Nora Body, Pech Valley` · **19 từ**

> Pyrite cầm tay trái, móng đại bàng trên ngực. Bỏ "priceless prehistoric treasures".

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (holding up the pyrite): "This comes with me. Every trip." | Cái này đi cùng tôi. Mọi chuyến đi. |
| 3–6s | Nora says (turning it in her fingers): "First fire I ever made out here." | Ngọn lửa đầu tiên tôi nhóm ở đây. |
| 6–8s | Nora says (touching the talon): "And this one never comes off." | Còn cái này thì không bao giờ tháo. |


### Cảnh 73 · Lời cảm ơn — ĐỀ XUẤT CẮT (S3)
`refs: Nora, Nora Body, Pech Valley` · **19 từ**

> Nếu giữ: bỏ câu khẩu hiệu "They did not merely survive… they lived" (story-engine §12: sau payoff không có câu chủ đề).

| Mốc | Thoại EN (dán vào `video_prompt`) | Vietsub |
|---|---|---|
| 0–3s | Nora says (to the lens): "I came here to survive them." | Tôi đến đây để sống sót trước họ. |
| 3–6s | Nora says (small laugh): "Turns out I needed them to survive." | Hóa ra tôi cần họ mới sống sót được. |
| 6–8s | Nora says (quiet smile): "Thanks, Gran. Thanks, Chief. Big Guy." | Cảm ơn bà. Cảm ơn Sếp. Anh To Con. |


### Cảnh 74 · Drone kéo lùi
`refs: Pech Valley` · **0 từ**

> **Không thoại** (story-engine §12: cảnh cuối là hình ảnh, không thoại). Bỏ câu "unbreakable human spirit echoes forever". Chỉ có gió và nhạc.



### Cảnh 75 · Màn đen
`refs: —` · **0 từ**

> **Không thoại.** CUT BLACK.


