# KỊCH BẢN PHÂN CẢNH ĐIỆN ẢNH: PIRATES OF THE GOLDEN TREE
## (HẢI TẶC CÂY VÀNG: BẢN ĐỒ BỤNG CÁ)

> **Dự án:** Golden Tree (Slug: `golden-tree`)  
> **Package:** *The Golden Trap: Voyage to the Forgotten Sanctuary*  
> **Lời hứa kịch tính:** Tấm bản đồ giấu trong bụng con cá dị dạng dẫn lối tới kho báu Cây Vàng, nhưng cái giá phải trả là mạng sống nếu không biết cơ chế mê cung.  
> **Ngôn ngữ thoại:** English (Cinematic Period Maritime English)  
> **Góc máy:** 100% Third-Person Cinematic Camera (Không selfie, không POV điện thoại, không xưng hô với khán giả).  
> **Âm thanh & Mix nhạc:** Chuẩn điện ảnh −14 LUFS / −1 dBTP.  

---

## 1. BẢNG NHÂN VẬT & MÃ GIỌNG ĐIỆN ẢNH (`VOICE_LOCK` & REFS)

| Tên Entity | Vai trò | Voice ID (`voice-bible.md`) | Mô tả âm sắc & Khẩu khí | Bộ References (`character_names`) |
| :--- | :--- | :--- | :--- | :--- |
| **Nora** | Nữ Thuyền trưởng (26 tuổi) | `kore` | Nữ, đanh thép, trầm ổn, dứt khoát; giọng chỉ huy phong trần giữa biển bão. | `["Nora", "Nora Body Seafarer"]` |
| **Theron** | Hoa tiêu sống sót (58 tuổi) | `sadaltager` | Nam, khản đặc, thở dốc vì đói khát nhưng sắc sảo và am tường địa tầng. | `["Theron"]` |
| **Castor** | Chiến binh mưu lược (29 tuổi) | `alnilam` | Nam, cộc cằn, sắc lạnh, giọng hoài nghi mang tính lý trí thực tế. | `["Castor"]` |
| **Heracles** | Chiến binh thể hình (35 tuổi) | `algenib` | Nam, trầm đục, gầm vang uy lực, ít lời nhưng nặng như đá tảng. | `["Heracles"]` |
| **Lão Ngư Dân**| Sứ giả khởi đầu (65 tuổi) | `enceladus` | Nam, run rẩy, hổn hển, kinh hoàng tột độ. | `["Old Fisherman"]` |
| **Sirens** | Quái nữ biển sâu | *Sound Design* | Tiếng ngân nga thì thầm ma mị chuyển sang tiếng thét rít xé màng nhĩ. | `["Abyssal Siren"]` |
| **Labyrinth Beast**| Quái vật Chitin 6 chân | *Sound Design* | Tiếng giáp xác nghiền đá, tiếng rít axit xì khói, tiếng đuôi quất rầm rộ. | `["Labyrinth Beast"]` |

---

## 2. BẢNG VẬT LÝ & LIÊN TỤC BỐI CẢNH (CONTINUITY LEDGER)

* **Sổ liên tục bối cảnh (Location States):**
  * `LOC-01 (Biển đêm mù sương)`: Boong tàu gỗ sồi ướt nước mặn, đèn lồng dầu đung đưa hắt ánh sáng vàng hổ phách, sương mù dày lơ lửng mặt nước.
  * `LOC-02 (Eo biển Clashing Rocks)`: Hai vách đá bazan xám đen cao 80m va đập sấm sét, bọt sóng trắng xóa tung cao 15m.
  * `LOC-03 (Hòn đảo Karst 15:18)`: Vực đá vôi xám xịt cằn cỗi, bụi vôi bám áo quần, khe nứt hẹp ngột ngạt không lối mòn.
  * `LOC-04 (Điện Thờ Cây Vàng)`: Giếng trời ngầm khổng lồ, giếng trăng rọi qua sương, hồ nước ngầm phản chiếu ánh kim, bụi sáng Golden Embers lơ lửng.
* **Quy chuẩn tương tác vật lý (Rule 41, 51):**
  * Đạo cụ tấm bản đồ da cừu: Khi khô là màu trắng tinh khiết; khi dính nước biển/ánh trăng lập tức phát quang đường viền mực vàng kim.
  * Truyền lực va chạm: Quái vật Labyrinth va vào vách đá làm đá vôi sạt lở trước khi rơi xuống đất; không có va chạm cơ thể người trực diện với quái thú 3.5 tấn.

---

## 3. PHÂN CẢNH CHI TIẾT TỪNG SHOT (SCENE-BY-SCENE STORYBOARD)

### HỒI 1: TẤM BẢN ĐỒ BỤNG CÁ (ACT 1: THE BIOLUMINESCENT OMEN)

#### Scene 01 | Biển Mù Sương & Bắt Giữ Thuyền Cá
* **Độ dài:** 8s | **Cỡ cảnh:** Extreme Wide Shot sang Medium Shot (Tracking).
* **Góc máy:** Máy điện ảnh từ mạn thuyền trôi chậm theo con tàu hải tặc lướt trong sương mù dày đặc; đèn lồng hắt sáng vàng lên mặt nước xanh thẫm.
* **Refs:** `["Nora", "Nora Body Seafarer", "Castor"]`
* **Hành động:**
  * `0-3s`: Con thuyền cá nhỏ tròng trành bị móc neo sắt của tàu hải tặc kéo giật vào mạn; sóng biển vỗ ầm ầm vào vỏ gỗ sồi.
  * `3-6s`: Castor nhảy xuống mũi thuyền cá, chĩa mũi nỏ vào lão ngư dân đang co rúm người ôm bọc lưới bốc khói lân tinh.
  * `6-8s`: Nora bước ra mạn tàu, ánh mắt kiên định nhìn xuống bọc lưới phát quang lục bảo.
* **Thoại:**
  * `3-6s`: Castor says (harsh, skeptical): *"Stand clear! He's hoarding something alive in the hold."* (10 words)
* **Audio/SFX:** Tiếng gỗ tàu kẽo kẹt, tiếng nước biển đập mạn, tiếng gió rít qua dây buồm.

---

#### Scene 02 | Mổ Bụng Con Cá Dị Dạng
* **Độ dài:** 8s | **Cỡ cảnh:** Medium Close-up to Macro Insert.
* **Góc máy:** Slow forward dolly push-in hướng vào mặt bàn gỗ mục cabin tàu; ánh đèn bão tạo bóng đổ Chiaroscuro gắt gao.
* **Refs:** `["Nora", "Nora Body Seafarer", "Omen Fish"]`
* **Hành động:**
  * `0-3s`: Con cá dị dạng nằm trên bàn gỗ, lớp vảy xà cừ đen nhấp nháy ánh lục bảo yếu ớt; hàm răng nhọn hoắt há hốc.
  * `3-6s`: Bàn tay Nora cầm đoản kiếm Hy Lạp rạch dứt khoát một đường dọc bụng cá; chất nhờn lấp lánh cát thạch anh tràn ra.
  * `6-8s`: Mũi dao tách mô thịt, để lộ cuộn da cừu trắng tinh khiết không dính máu.
* **Thoại:**
  * `0-3s`: Nora says (focused, steady): *"Look at the gills. This was bred in deep abyss."* (10 words)
* **Audio/SFX:** Tiếng dao cắt qua lớp vảy giáp tanh tách, tiếng chất nhờn ướt át trượt trên mặt gỗ.

---

#### Scene 03 | Bản Đồ Ma Thuật Khởi Động
* **Độ dài:** 8s | **Cỡ cảnh:** Close-up to Over-The-Shoulder Shot.
* **Góc máy:** Low-angle cố định ngang ngực Nora, hướng về cuộn da cừu mở rộng trên bàn.
* **Refs:** `["Nora", "Nora Body Seafarer", "Castor", "Heracles"]`
* **Hành động:**
  * `0-3s`: Castor nhìn tờ giấy trắng tinh, nhếch mép thất vọng; Heracles đứng khoanh tay sừng sững phía sau.
  * `3-6s`: Nora nhúng ngón tay vào bát nước biển mặn, nhỏ ba giọt nước lên mặt da cừu.
  * `6-8s`: Các đường gân mực vàng kim bừng sáng lan tỏa như mạch máu, vẽ nên hải trình ngoằn ngoèo dẫn tới biểu tượng Cây Vàng.
* **Thoại:**
  * `3-6s`: Nora says (commanding, inspired): *"Salt awakens the ink. The Golden Tree is not a myth."* (11 words)
* **Audio/SFX:** Tiếng rít nhẹ phát quang ma thuật (chimes ngân vang), tiếng trầm trồ của thủy thủ ngoài boong.

---

### HỒI 2A: THỬ THÁCH BIỂN SÂU (ACT 2A: THE OCEANIC ORDEALS)

#### Scene 04 | Vách Đá Nghiền Clashing Rocks
* **Độ dài:** 8s | **Cỡ cảnh:** Extreme Wide Low-Angle.
* **Góc máy:** Dynamic Tracking Shot bám sát mũi tàu lao giữa hai bức tường đá bazan dựng đứng đang chao đảo nghiền vào nhau.
* **Refs:** `["Nora", "Nora Body Seafarer", "Heracles"]`
* **Hành động:**
  * `0-3s`: Sóng biển cuộn trào bọt trắng xóa; vách đá bên phải sụp xuống hàng tấn mảnh đá dăm bay rào rào.
  * `3-6s`: Heracles dùng cả lồng ngực vạm vỡ gồng mình giữ chặt cần tời buồm; Nora ghì chặt bánh lái bẻ ngoặt 45 độ.
  * `6-8s`: Con tàu lách qua khe hẹp đúng một gang tay trước khi hai mảng đá khổng lồ đập sập vào nhau tạo tiếng nổ long trời.
* **Thoại:**
  * `0-3s`: Nora says (shouting over crashing waves): *"Brace the mast! Keep her straight into the spray!"* (10 words)
* **Audio/SFX:** Tiếng đá tảng va đập sấm sét, tiếng gỗ chịu lực gầm rú, tiếng sóng biển gầm vang.

---

#### Scene 05 | Tiếng Hát Sirens Vực Biển Sâu
* **Độ dài:** 8s | **Cỡ cảnh:** Medium Shot to Dutch Angle.
* **Góc máy:** Cận mặt nước xanh ngọc bích phát quang ma quái; sương mù bảng lảng.
* **Refs:** `["Nora", "Nora Body Seafarer", "Abyssal Siren"]`
* **Hành động:**
  * `0-3s`: Ba sinh vật Siren trồi lên mạn thuyền, da trắng như ngọc, cất tiếng ngâm nga ngân dài thôi miên thủy thủ đoàn.
  * `3-6s`: Một thủy thủ thả rơi mái chèo bước ra mạn; đôi mắt Siren lập tức hóa đen tuyền, hàm rách toạc để lộ 3 hàng răng cá mập chồm lên.
  * `6-8s`: Nora rút đoản kiếm chém đứt móng vuốt quái thú, túm cổ áo thủy thủ giật ngược lại sàn tàu an toàn.
* **Thoại:**
  * `3-6s`: Nora says (urgent, breathless): *"Cover your ears! Plug the wax and loose the fire-arrows!"* (11 words)
* **Audio/SFX:** Tiếng hát du dương biến thành tiếng thét rít quái thai xé toạc không gian.

---

### BƯỚC NGOẶT TRUNG TÂM (MIDPOINT 15:18): HÒN ĐẢO ĐÁ VÔI & GIẢI CỨU THERON

#### Scene 06 | Vách Đá Cụt & Cuộc Tranh Cãi Nảy Lửa
* **Độ dài:** 8s | **Cỡ cảnh:** Medium Two-Shot (Nora & Castor).
* **Góc máy:** Eye-level tĩnh đặt giữa khe hẻm núi đá vôi xám cằn cỗi; sương mù lạnh trôi là là mặt đất.
* **Refs:** `["Nora", "Nora Body Seafarer", "Castor"]`
* **Hành động:**
  * `0-3s`: Đoàn người dừng chân trước một vách đá vôi sừng sững bít kín hẻm núi; bụi đá trắng bay mù mịt.
  * `3-6s`: Castor ném mạnh mũi tên cắm phập vào vách đá, chỉ tay vào tấm bản đồ trên tay Nora với ánh mắt phẫn nộ.
  * `6-8s`: Nora giơ tấm bản đồ phát quang lên đối chiếu với rãnh đá, chân mày nhíu chặt căng thẳng.
* **Thoại:**
  * `3-6s`: Castor says (furious, cynical): *"It's a dead wall, Nora! Your glowing fish-skin led us into an open grave!"* (15 words)
* **Audio/SFX:** Tiếng gió hú qua khe đá hẹp, tiếng bước chân lạo xạo trên đá dăm khô khốc.

---

#### Scene 07 | Đúng 15:18 — Tiếng Kêu Cứu Trong Khe Nứt Sạt Lở
* **Độ dài:** 8s | **Cỡ cảnh:** Low-Angle Tilt-Up to Macro Crevice.
* **Góc máy:** Dutch Angle nhẹ (nghiêng 10 độ) tăng cảm giác bất an; lia máy từ chân vách đá vào một hốc nứt tối tăm.
* **Refs:** `["Nora", "Nora Body Seafarer", "Theron"]`
* **Hành động:**
  * `0-3s`: Nora giơ tay ra hiệu im lặng; giữa tiếng gió hú, vang lên tiếng cào cấu và tiếng thở hổn hển từ khe đá sập.
  * `3-6s`: Bên trong khe nứt hẹp, khuôn mặt Theron ló ra: râu tóc bạc phơ đóng bụi vôi, ánh mắt hoang dại vì đói khát, bàn tay gầy gò vươn ra cầu cứu.
  * `6-8s`: Bỏ qua lời phản đối của Castor, Nora lao tới quỳ xuống, chộp lấy bàn tay run rẩy của ông lão.
* **Thoại:**
  * `3-6s`: Theron speaks in a weathered, raspy knowledgeable male voice: *"Help me... the rocks slipped... before the hunter returns!"* (10 words)
* **Audio/SFX:** Tiếng đá dăm rơi rào rào, tiếng thở khò khè nghẹn ngào của Theron.

---

#### Scene 08 | Vạch Trần Cái Bẫy Của Bản Đồ Ma Thuật
* **Độ dài:** 8s | **Cỡ cảnh:** Over-The-Shoulder (Nora nhìn Theron).
* **Góc máy:** Cận cảnh trung bình; ánh sáng ban ngày xuyên qua kẽ nứt hắt bóng đổ gắt gao lên khuôn mặt hai người.
* **Refs:** `["Nora", "Nora Body Seafarer", "Theron"]`
* **Hành động:**
  * `0-3s`: Heracles bẩy tảng đá lớn ra; Nora đỡ Theron ngồi tựa vào vách đá, trao bầu nước da.
  * `3-6s`: Theron nhìn thấy tấm bản đồ da cừu phát quang trên tay Nora, bật cười khản đặc cay đắng.
  * `6-8s`: Theron giơ phiến đá cổ của mình lên, chỉ vào các rãnh bẫy ngầm mà bản đồ ma thuật đã cố tình che giấu.
* **Thoại:**
  * `3-6s`: Theron speaks in a weathered, raspy knowledgeable male voice: *"That paper doesn't show a passage. It shows the bait. The tree feeds on fools who follow it blindly."* (19 words)
* **Audio/SFX:** Tiếng nuốt nước ừng ực, tiếng phiến đá vôi gõ lách cách vào nhau.

---

### HỒI 2B: MÊ CUNG & BẪY QUÁI VẬT CHITIN (ACT 2B: THE LABYRINTH CLASH)

#### Scene 09 | Theron Dẫn Đường Trong Hẻm Ngầm
* **Độ dài:** 6s | **Cỡ cảnh:** Wide Tracking Shot.
* **Góc máy:** Camera lùi dần (Backwards Dolly) dẫn trước đoàn người đang luồn lách qua hẻm đá vôi dốc đứng u tối.
* **Refs:** `["Nora", "Nora Body Seafarer", "Theron", "Heracles"]`
* **Hành động:**
  * `0-3s`: Theron chống gậy đá đi trước, ra hiệu đoàn người cúi thấp người men theo gờ đá ẩm ướt.
  * `3-6s`: Từ trần hang phía sau, các mảnh đá vôi rung chuyển rơi xuống; tiếng chân giáp xác cào xé vách đá rền vang từ xa.
* **Thoại:**
  * `0-3s`: Theron speaks in a weathered, raspy knowledgeable male voice: *"Step where the moss clings. The stone beast listens to hollow footsteps."* (12 words)
* **Audio/SFX:** Tiếng bước chân nhẹ rón rén, tiếng đá rung chấn động từ sâu trong lòng núi.

---

#### Scene 10 | Quái Vật Chitin Xuất Kích
* **Độ dài:** 8s | **Cỡ cảnh:** Low-Angle Hero Shot sang Action Pan.
* **Góc máy:** Handheld Shaky bám sát chuyển động hỗn loạn; máy rung giật theo từng nhịp va chạm.
* **Refs:** `["Nora", "Nora Body Seafarer", "Labyrinth Beast", "Heracles"]`
* **Hành động:**
  * `0-3s`: Quái vật Chitin 6 mét từ trên vòm hang bổ nhào xuống; 6 chân móc cắm ngập vào vách đá làm vỡ vụn từng mảng đá lớn.
  * `3-6s`: Chiếc đuôi gai độc quét ngang một đường bạt mạng; Heracles giơ khiên đồng đỡ đòn, chấn lực đẩy trượt lùi 2 mét trên sỏi.
  * `6-8s`: Quái thú rít lên chói tai, đôi kìm đôi há to nhỏ giọt dịch axit bốc khói nghi ngút.
* **Thoại:** (Sonic Isolation — 0 từ; dồn toàn bộ kịch tính vào âm thanh chiến đấu).
* **Audio/SFX:** Tiếng kim loại va đập chát chúa, tiếng rít axit xèo xèo ăn mòn mặt đất, tiếng đất đá sạt lở dữ dội.

---

#### Scene 11 | Dùng Bản Đồ Làm Mồi & Kích Hoạt Bẫy Đá Sập
* **Độ dài:** 8s | **Cỡ cảnh:** Medium Action Shot to Wide Payoff.
* **Góc máy:** Chuyển từ góc cận Nora kéo nỏ sang góc toàn cảnh hẻm đá nơi bẫy sập được kích hoạt.
* **Refs:** `["Nora", "Nora Body Seafarer", "Labyrinth Beast", "Castor"]`
* **Hành động:**
  * `0-3s`: Nora quấn tấm bản đồ da cừu phát quang quanh mũi tên lửa, giương nỏ bắn cắm phập vào vòm hang bên kia hẻm.
  * `3-6s`: Quái thú bị ánh sáng lân tinh dụ dỗ chồm lên tảng đá treo; Castor chém đứt sợi dây chão neo giữ cọc gỗ.
  * `6-8s`: Tảng đá vôi hàng tấn sập xuống như trời giáng, đè bẹp thân quái thú trong bụi mù mịt mịt mùng.
* **Thoại:**
  * `0-3s`: Nora says (commanding, shouting): *"Castor, cut the lanyard now! Bring the arch down!"* (9 words)
* **Audio/SFX:** Tiếng dây chão đứt phựt, tiếng đá rơi ầm ầm long trời lở đất, tiếng gầm tắt nghẽn của quái vật.

---

### HỒI 3: ĐIỆN THỜ CÂY VÀNG & TỰ DO (ACT 3: THE GOLDEN SANCTUARY)

#### Scene 12 | Khám Phá Giếng Trời & Cây Vàng Rực Rỡ
* **Độ dài:** 10s | **Cỡ cảnh:** Extreme Wide Establishing Master Shot (Slow Push-In).
* **Góc máy:** Máy điện ảnh từ từ đẩy tới xuyên qua vòm hang tối, mở ra không gian giếng trời ngầm kỳ vĩ ngập ánh trăng.
* **Refs:** `["Nora", "Nora Body Seafarer", "Golden Tree", "Theron"]`
* **Hành động:**
  * `0-3s`: Cả đoàn người đứng sững sờ trên bờ đá; phản chiếu ánh vàng rực rỡ lên áo giáp phong trần của họ.
  * `3-7s`: Cây Vàng cổ đại sừng sững cao 20m ở trung tâm hồ pha lê, tán lá vàng óng rung rinh phát tán hàng ngàn đốm sáng Golden Embers lơ lửng.
  * `7-10s`: Dưới chân gốc cây, ánh đèn bộc lộ hàng chục bộ hài cốt mạ vàng bị đông cứng trong tư thế quằn quại vươn tay.
* **Thoại:**
  * `3-7s`: Theron speaks in a weathered, raspy knowledgeable male voice: *"Behold the golden curse. Everyone who reached for the boughs became part of the root."* (16 words)
* **Audio/SFX:** Dàn nhạc giao hưởng thánh thót, tiếng gió luồn qua khe đá tạo âm vang huyền bí, tiếng bụi sáng tanh tách như than hồng.

---

#### Scene 13 | Phép Thử Lòng Tham & Quyết Định Của Nora
* **Độ dài:** 8s | **Cỡ cảnh:** Medium Close-up Two-Shot.
* **Góc máy:** Low-Angle ngang ngực Nora và Castor bên bờ hồ nước ngầm trong vắt.
* **Refs:** `["Nora", "Nora Body Seafarer", "Castor"]`
* **Hành động:**
  * `0-3s`: Castor mê mẩn bước tới sát mặt nước, rút dao găm định vươn tay chặt một nhánh rễ vàng rực sáng.
  * `3-6s`: Nora đặt bàn tay thép ghì chặt cổ tay Castor lại, ánh mắt nghiêm nghị đầy quyền uy thức tỉnh anh.
  * `6-8s`: Nora cúi xuống mặt hồ, chỉ vớt lấy một chiếc lá vàng rụng trôi dạt bên mép đá làm chứng tích sống sót.
* **Thoại:**
  * `3-6s`: Nora says (firm, calm, resonant): *"Gold cannot steer a ship, Castor. We leave with our lives, or we become statues."* (16 words)
* **Audio/SFX:** Tiếng nước hồ sóng sánh gợn nhẹ, tiếng kim loại dao găm tra lại vào bao da dứt khoát.

---

#### Scene 14 | Hạ Màn — Giương Buồm Ra Khơi Biển Mênh Mông
* **Độ dài:** 10s | **Cỡ cảnh:** Wide Establishing Shot to Horizon Pan.
* **Góc máy:** Máy quay từ trên cao bay lượn (High-angle Crane/Dolly) theo cánh buồm con tàu hải tặc rẽ sóng ra khỏi vịnh đảo đá vôi; ánh bình minh rạng đông đỏ rực rọi sáng mặt biển bao la.
* **Refs:** `["Nora", "Nora Body Seafarer"]`
* **Hành động:**
  * `0-4s`: Con tàu giương toàn bộ cánh buồm no gió, lướt nhanh ra khỏi hẻm núi tăm tối hướng về biển lớn tự do.
  * `4-7s`: Nora đứng hiên ngang ở mũi tàu, một tay đặt trên chuôi đoản kiếm, bàn tay kia xòe ra chiếc lá vàng lấp lánh trong nắng sớm.
  * `7-10s`: Máy quay từ từ nâng cao lên bầu trời xanh biếc; con tàu trở thành biểu tượng kiêu hãnh giữa đại dương bao la.
* **Thoại:** (0 từ — Lắng đọng trọn vẹn bằng giai điệu điện ảnh hào hùng).
* **Audio/SFX:** Tiếng sóng vỗ mạn tàu mạnh mẽ, tiếng gió căng buồm, nhạc khúc khải hoàn hạ màn.

---

## 4. BƯỚC TIẾP THEO THEO QUY TRÌNH `fk-film`
1. Đã hoàn tất Tầng 1 (`story-bible.md`) và Tầng 2 (`script.md` + `creatures_and_characters_design.md`).
2. Sẵn sàng chuyển sang Tầng 2.5: **Dựng trên giấy (`paper_edit.md`)** kiểm toán thời lượng và số từ Rule 49.
3. Xuất Structured JSON Prompt cho từng phân cảnh (`prompts_act1.json`, `prompts_act2.json`, `prompts_act3.json`).
