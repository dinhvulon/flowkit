# fk-vlog-japan — Japanese Historical & Time-Travel POV Vlog Orchestrator (Kyoto Heian, Kamakura, Edo)

Tạo kịch bản và dự án video vlog **DU HÀNH LỊCH SỬ / POV VLOG NHẬT BẢN** (Kyoto Heian 1000, Kamakura 1274, Edo 1650...) với phong cách vlogger hiện đại tự quay camera trước điện thoại (smartphone selfie), chuẩn quang học Pan-Focus (nét sâu toàn khung), và **thoại tiếng Nhật đàm thoại tự nhiên** (`dialog-japan`: 話し言葉 / タメ口, đếm nhịp mora chuẩn 8 giây).

---

## 🎭 VAI TRÒ & MỤC TIÊU

Skill này kết hợp 2 hệ thống chuyên biệt:
1. **`kich-ban-vlog`**: Bộ khung 12 beat kịch bản du hành lịch sử, 3 kiểu clip (nói / đi bộ chạm tay / flycam toàn cảnh), quang học Pan-Focus f/8–f/11, khóa dân tộc (Strict Ethnicity Lock) và khóa thời kỳ (Period Lock) chống AI lai Tây.
2. **`dialog-japan`**: Quy tắc viết lời thoại tiếng Nhật đàm thoại tự nhiên của giới trẻ Nhật (casual, đếm mora 48–58 mora ≈ 6.5–7.5s, phiên âm hiragana cho chữ Hán dễ đọc sai, câu nói mang tính suy đoán tránh áp đặt lịch sử).

Kết quả đầu ra tương thích 100% với pipeline của FlowKit:
- **Project API**: `POST /api/projects` (với `material: "realistic"`, entities nhân vật + bối cảnh + đạo cụ)
- **Video API**: `POST /api/videos`
- **Scene API**: `POST /api/scenes` (tách biệt **Prompt Frame 0** cho ảnh tĩnh và **Video Prompt 8s** chia sub-clip `0-3s`, `3-6s`, `6-8s` kèm thoại tiếng Nhật và hiệu ứng âm thanh)
- **TTS Engine**: Tạo giọng đọc tiếng Nhật tự nhiên qua OmniVoice (`POST /api/videos/{vid}/narrate`)

---

## 📐 NGUYÊN TẮC CỐT LÕI (BẮT BUỘC TUÂN THỦ)

### 1. Khung "Time Capsule" — Phải chính xác tới năm
- **CẤM** dùng từ chung chung như "Nhật Bản cổ đại" hay "thời phong kiến" — AI sẽ trộn lẫn thời Heian + Edo + Kimono du lịch hiện đại + anime.
- **BẮT BUỘC** chỉ định rõ: `Heian-kyō, Kyoto, Japan, 1000 AD` / `Kamakura, Japan, 1274 AD` / `Edo, Japan, 1657 AD`.

### 2. Chuẩn Quang Học Smartphone Pan-Focus (f/8–f/11)
- Vlogger cầm điện thoại tự quay bằng camera trước 28mm wide-angle ở cự ly cánh tay (tight waist-up selfie framing, minimal headroom).
- **Infinite Depth of Field (Nét sâu từ trước ra sau)**: Mặt nhân vật phía trước và toàn bộ bối cảnh người dân, sạp chợ, nhà cửa phía sau đều **100% TACK-SHARP**.
- **STRICTLY ZERO BACKGROUND BLUR / ZERO BOKEH**: Tuyệt đối cấm xóa phông, cấm hiệu ứng chân dung (portrait mode). Xóa phông làm mất đi giá trị tư liệu của bối cảnh lịch sử.
- **Vị trí bàn tay ở Frame 0**: Bàn tay rảnh rỗi (không cầm máy) phải được neo chính xác ngay từ ảnh tĩnh frame 0 (đang chỉ trỏ, đang chạm tay vào sạp hàng, đang cầm lược hay đang khép nép).

### 3. Khóa Sắc Tộc & Khóa Thời Kỳ Nghiêm Ngặt
- **STRICT ETHNICITY LOCK**: Mọi người xuất hiện trong khung hình (kể cả người đi đường, người bán hàng, phu khuân vác, quý tộc) phải là **100% native East Asian Japanese** thời kỳ tương ứng. Tuyệt đối **KHÔNG CÓ** người da trắng (Caucasian), người phương Tây, mắt xanh, tóc vàng hoặc nâu sáng.
- **PERIOD LOCK**:
  - *Heian (năm 1000)*: Gỗ tuyết tùng mộc không sơn, đường đất lầy lội có vết bánh xe, mái tranh hoặc ván gỗ, vải gai thô không nhuộm. CẤM nhà phố machiya, CẤM đường lát đá, CẤM đèn lồng đỏ du lịch, CẤM guốc geta, CẤM kimono thời Edo, CẤM sơn đỏ tươi kiểu đền Heian Jingu hiện đại.
  - *Kamakura (1274)*: Trang phục chiến tranh, lính canh samurai, nhà gỗ mộc, vải chàm dệt tay thô, dép rơm waraji.
  - *Edo (thời Mạc phủ)*: Nhà machiya, bảng hiệu chữ Hán cổ, đường lát đá sỏi, trang phục kimono có obi rõ ràng.

### 4. Ba Kiểu Clip & Cấu Trúc Nhịp 8 Giây
Mỗi clip dài đúng **8 giây** (phù hợp hoàn hảo với mô hình Veo 3 / Omni Flash của Google Flow):

| Kiểu clip | Vai trò & Tần suất | Cách quay & Start Frame | Thoại tiếng Nhật |
| :--- | :--- | :--- | :--- |
| **Clip Nói** | Chiếm đa số (~6 clip): Biểu cảm khuôn mặt, phản ứng trực tiếp với camera. | Camera trước selfie ngang ngực, mắt nhìn thẳng vào ống kính. | Có thoại đàm thoại trực tiếp vào lens. |
| **Đi Bộ + Chạm Tay** | 1–2 clip: Khám phá xúc giác (sờ vải, chạm cột gỗ, nếm đồ ăn). | Camera trước hơi nghiêng, thấy tay nhân vật tương tác với vật thể thật. | Có thoại ngắn kết hợp hành động. |
| **Flycam Toàn Cảnh** | Đúng **2 slot cố định**: Clip 2 (ngay sau Hook mở đầu) và Clip cuối (Coda kết thúc). | Góc nhìn flycam từ mái nhà lướt bay lên cao toàn cảnh, **không có vlogger**. | **Hoàn toàn KHÔNG thoại (`""`)**, chỉ có âm thanh môi trường + nhạc cụ koto/sáo truyền thống. |

### 5. Cầu Nối Đổi Trang Phục (Costume Bridge)
- **Clip 1**: Vlogger mặc trang phục **hiện đại** (áo thun, hoodie, sneaker) vừa rơi xuống quá khứ, ngơ ngác sốc văn hóa.
- **Clip 2 (Flycam)**: Đóng vai trò "dấu ba chấm thời gian" lướt toàn cảnh kinh thành.
- **Clip 3**: Vlogger đã mặc trang phục thời kỳ (vải gai thô thường dân), mở đầu bằng câu tự giễu tự nhiên: `「はい、着替えました。」` (*Rồi, thay đồ xong rồi nè*). Không cần quay cảnh thay đồ phức tạp.

---

## 🗣️ NGUYÊN TẮC THOẠI TIẾNG NHẬT (`dialog-japan`)

1. **Văn phong đàm thoại (話し言葉 / タメ口)**:
   - Nói tự nhiên như đang gọi video call cho bạn thân. Tuyệt đối không dùng giọng đọc tin tức truyền hình, không dùng kính ngữ `敬語` (Desu/Masu) cứng nhắc kiểu thuyết minh du lịch.
2. **Đo độ dài bằng MORA (Phách âm)**:
   - Một clip 8 giây chỉ chứa được **6.5 – 7.5 giây phát âm thật**.
   - Cần khống chế từ **48 đến 58 mora** (khoảng 35–45 ký tự tiếng Nhật). Nếu câu quá dài, AI TTS sẽ đọc dồn dập hoặc bị cắt cụt đuôi câu.
3. **Phiên âm Hiragana cho chữ dễ đọc sai**:
   - Các chữ Hán cổ hoặc từ vựng lịch sử dễ bị TTS đọc sai âm Onyomi/Kunyomi thì viết thẳng bằng Hiragana trong kịch bản:
     - `牛車` → viết `ぎっしゃ` (gissha - xe bò quý tộc, tránh đọc nhầm thành gyuusha)
     - `大極殿` → viết `だいごくでん` (daigokuden)
     - `櫛` → viết `くし` (kushi - lược gỗ)
     - `醤油` → viết `しょうゆ` (shoyu)
     - `弔ってる` → viết `とむらってる` (tomuratteru - tưởng niệm)
4. **Hạ mức độ khẳng định lịch sử thành suy đoán (Hedging)**:
   - Khán giả Nhật rất nhạy cảm với việc khẳng định sai kiến thức lịch sử. Vì vậy, các thông tin lịch sử cần được nói dưới dạng "nghe nói", "mình nghĩ":
     - Dùng `〜んだって` (*nghe nói là...*) thay vì khẳng định tuyệt đối.
     - Dùng `〜のかな` (*không biết có phải là...*).
     - Dùng `〜と思う` (*mình nghĩ là...*).
5. **Chỉ dẫn cảm xúc đặt ngay trước ngoặc thoại**:
   - Ví dụ: `戸惑いながらも明るい声で、少し早口: 「えっ、ちょっと待って。においが…においがすごい。」`

---

## 📋 KỊCH BẢN MẪU HOÀN CHỈNH: `Heian-kyō 1000` (Kyoto thời Heian)

### Thông Tin Tổng Quan Dự Án
- **Tên dự án**: `Heian-kyo 1000 - Kyoto Time Travel Vlog`
- **Thời lượng**: 10 clips × 8s = 80s
- **Material**: `realistic`
- **Giọng TTS**: Giọng nữ trẻ Nhật Bản (21–23 tuổi, casual, biểu cảm sinh động)
- **Thực thể (Entities)**:
  1. `Vlogger` (`character`): Nữ vlogger Nhật Bản trẻ 22 tuổi, tóc đen tự nhiên buộc lỏng, nét mặt Á Đông, trang điểm nhẹ nhàng tự nhiên.
  2. `Modern Outfit` (`visual_asset`): Áo phông trắng oversize, quần jean xắn gấu, giày sneaker.
  3. `Heian Commoner Kosode` (`visual_asset`): Áo choàng kosode vải gai thô không nhuộm màu be nhạt, dây thắt lưng chàm thô, tạp dề vải gai nâu đất, dép rơm waraji.
  4. `East Market Higashinoichi` (`location`): Chợ Đông Heian, sạp gỗ cedar thô thấp, mái tranh, đường đất lầy lội, chiếu cói bày vải gai và bao gạo.
  5. `Suzaku Avenue and Palace` (`location`): Đại lộ Suzaku rộng 80m đất trống, rãnh nước hai bên, cổng Suzaku cột son đỏ bạc màu và Đại điện Daigokuden ngói xám xa xa.
  6. `Kamo Riverbank` (`location`): Bãi sỏi sông Kamo hoang sơ, cỏ lau khô susuki, dòng nước trong nông nhiều nhánh, vài tấm bia mộ gỗ cắm nghiêng bên mép nước.
  7. `Boxwood Comb` (`visual_asset`): Chiếc lược gỗ hoàng dương nhỏ chạm khắc mộc mạc thời Heian.

---

### Danh Sách 10 Phân Cảnh (Scene Breakdown)

#### Scene 1 (ROOT) — Beat 1: Hook, Vừa Rơi Xuống Chợ Đông (Đồ Hiện Đại)
- **Character Names**: `["Vlogger", "East Market Higashinoichi"]`
- **Prompt (Frame 0)**:
  ```
  Authentic smartphone selfie photograph, vertical 9:16, 28mm wide-angle front camera held at arm's length. TIGHT WAIST-UP SELFIE FRAMING, looking directly into lens with stunned expression. PAN-FOCUS (f/8-f/11) - DEEP DEPTH OF FIELD, face and background simultaneously 100% tack-sharp, STRICTLY ZERO BOKEH, ZERO PORTRAIT BLUR. Cool morning daylight 6000K, thin cooking smoke. Vlogger wearing modern white t-shirt. Standing in Higashi-no-ichi market lane of Heian-kyo 1000 AD, packed-earth muddy ground, rough cedar stalls with thatch roofs, porters in undyed hemp cloth. Free hand raised in open-palm helpless gesture. STRICT ETHNICITY LOCK: 100% East Asian Japanese. NO phone visible.
  ```
- **Video Prompt (8s)**:
  ```
  0-3s: Handheld front camera with natural micro-shake. Still in modern clothes, she turns slightly, nose wrinkling at the pungent smell of wet earth, smoke, and dried fish, eyes widening in disbelief. Market porters carrying rice sacks move behind her.
  3-6s: She looks straight into the lens, lifting her free hand helplessly toward the market stalls behind her.
  6-8s: She speaks in natural casual Japanese, bewildered yet lively: "えっ、ちょっと待って。においが…においがすごい。道は土だし、車の音もゼロ。しかも、なんか寒い。ここ、どこ？"
  Audio: ambient street noise, chatter of market traders, wooden carts on dirt. No background music. Keep natural sound effects.
  ```
- **Narrator Text**: `えっ、ちょっと待って。においが…においがすごい。道は土だし、車の音もゼロ。しかも、なんか寒い。ここ、どこ？`

---

#### Scene 2 (ROOT) — Establishing: Flycam Toàn Cảnh Chợ Đông & Kinh Thành
- **Character Names**: `["East Market Higashinoichi"]`
- **Prompt (Frame 0)**:
  ```
  Authentic photorealistic establishing aerial drone photograph (flycam), 4K, 28mm wide-angle, vertical 9:16. PAN-FOCUS f/8-f/11 - entire depth tack-sharp, ZERO BOKEH. Cool morning light 6000K. Low angle skimming just above the dark thatch roofs of Higashi-no-ichi market in Heian-kyo 1000 AD. Beyond, the straight earthen street grid stretches to the distant faded red palace gate and wooded Higashiyama hills. NO vlogger in frame, nobody looking at camera. STRICT ETHNICITY LOCK: 100% native Japanese.
  ```
- **Video Prompt (8s)**:
  ```
  0-3s: Smooth continuous aerial drone glide soaring slowly above dark thatch roofs and cloth drying racks of the market lane.
  3-8s: Buttery-smooth acceleration rising steadily upward into a panoramic view of the wide earthen avenues, low wooden roofs, and distant northern palace gates under an overcast sky.
  Audio: Gentle, sparse traditional koto and bamboo flute melody with natural morning wind. NO dialogue, NO voiceover.
  ```
- **Narrator Text**: ` ` *(Để trống — Flycam câm)*

---

#### Scene 3 (ROOT) — Beat 2: Định Vị & Tuyên Bố Nhiệm Vụ (Đồ Thời Kỳ)
- **Character Names**: `["Vlogger", "East Market Higashinoichi"]`
- **Prompt (Frame 0)**:
  ```
  Authentic smartphone selfie photograph, vertical 9:16, 28mm front camera at arm's length. TIGHT WAIST-UP SELFIE FRAMING. PAN-FOCUS f/8-f/11, DEEP DEPTH OF FIELD, ZERO BOKEH. Cool daylight 6000K. Vlogger now wearing authentic Heian commoner hemp kosode robe. Her free hand is lightly tugging her own coarse hemp sleeve at the elbow with a wry smile. Standing in packed-earth market lane, traders bargaining animatedly behind her. STRICT ETHNICITY LOCK: 100% native Japanese.
  ```
- **Video Prompt (8s)**:
  ```
  0-3s: Handheld smartphone front camera micro-shake. She tugs her coarse hemp sleeve with a self-deprecating grin, glancing down at her clothes before looking back up into the lens.
  3-6s: She pans the phone slightly to show the lively cedar market stalls and moving shoppers in undyed hemp.
  6-8s: Speaking casually into the lens with a calm, amused tone: "はい、着替えました。ここは平安京、西暦千年です。貴族じゃなくて、庶民の暮らしを見に行きます。"
  Audio: Ambient market bustle, footsteps on dirt, gentle chatter. No background music. Keep natural sound effects.
  ```
- **Narrator Text**: `はい、着替えました。ここは平安京、西暦千年です。貴族じゃなくて、庶民の暮らしを見に行きます。`

---

#### Scene 4 (CONTINUATION) — Beat 5: Chợ & Kinh Tế: Đổi Vải Lấy Gạo (Đi Bộ + Chạm Tay)
- **Character Names**: `["Vlogger", "East Market Higashinoichi", "Boxwood Comb"]`
- **Prompt (Frame 0)**:
  ```
  Authentic smartphone selfie photograph, vertical 9:16, 28mm front camera. TIGHT WAIST-UP SELFIE FRAMING. PAN-FOCUS f/8-f/11, ZERO BOKEH. Standing close to an open cloth stall. On the reed mat beside her lie rolls of coarse hemp cloth and a row of small boxwood combs. Her free hand rests on the mat with fingertips touching one boxwood comb. Mid-ground: a kneeling trader pushes hemp cloth across to a farmer putting down a straw rice sack. STRICT ETHNICITY LOCK: 100% native Japanese.
  ```
- **Video Prompt (8s)**:
  ```
  0-3s: Her free hand slides fingertips slowly across a small boxwood comb on the mat with a longing look, then points toward the merchant and customer. The merchant vigorously pushes cloth forward while taking a straw bale of rice.
  3-6s: She turns back to the camera, eyes wide with genuine excitement, gesturing with her open hand toward the barter exchange.
  6-8s: Speaking with rapid, excited casual inflection: "見て、今の。布と米、そのまま交換してる。銭より、米や布で払うことも多いんだって。顔見て決めてる。"
  Audio: Rustle of straw sacks, merchant laughing and bargaining. No background music. Keep natural sound effects.
  ```
- **Narrator Text**: `見て、今の。布と米、そのまま交換してる。銭より、米や布で払うことも多いんだって。顔見て決めてる。`

---

#### Scene 5 (CONTINUATION) — Beat 6: Ăn Thử Cơm Phơi Khô
- **Character Names**: `["Vlogger", "East Market Higashinoichi"]`
- **Prompt (Frame 0)**:
  ```
  Authentic smartphone selfie photograph, vertical 9:16, 28mm front camera. TIGHT WAIST-UP SELFIE FRAMING. PAN-FOCUS f/8-f/11, ZERO BOKEH. Cool morning light. Vlogger in hemp kosode. Her free hand holds a small woven straw packet of dried rice (hoshi-ii) at chest height. In front of a rustic food stall with unglazed clay dishes. Behind her, a food vendor grins while wiping his hands on his apron. STRICT ETHNICITY LOCK: 100% native Japanese.
  ```
- **Video Prompt (8s)**:
  ```
  0-3s: She brings the dried rice packet closer to inspect it, takes a small crunchy bite, chewing thoughtfully with eyebrows raised at the hard, salty texture.
  3-6s: She nods with honest surprise, showing the small straw packet to the camera lens.
  6-8s: Speaking with cheerful curiosity: "これ、乾かしたごはん。めちゃくちゃ硬いけど、かめば甘い。しょうゆはあるけど、今のとは別物なんだって。"
  Audio: Crunchy chewing sound effect, cheerful market laughter nearby. No background music. Keep natural sound effects.
  ```
- **Narrator Text**: `これ、乾かしたごはん。めちゃくちゃ硬いけど、かめば甘い。しょうゆはあるけど、今のとは別物なんだって。`

---

#### Scene 6 (CONTINUATION) — Beat 9: Quyền Lực: Xe Bò Quý Tộc Đi Qua Đại Lộ Suzaku
- **Character Names**: `["Vlogger", "Suzaku Avenue and Palace"]`
- **Prompt (Frame 0)**:
  ```
  Authentic smartphone selfie photograph, vertical 9:16, 28mm front camera. TIGHT WAIST-UP SELFIE FRAMING. PAN-FOCUS f/8-f/11, ZERO BOKEH. Standing by roadside willow trees on the vast 80-meter-wide packed-earth Suzaku avenue. A black lacquered ox carriage with lowered bamboo blinds rolls past in the mid-ground. Townspeople nearby have stopped and bowed their heads. Her free hand is raised low in a cautious wait gesture. STRICT ETHNICITY LOCK: 100% native Japanese.
  ```
- **Video Prompt (8s)**:
  ```
  0-3s: Wide outdoor perspective. A black ox slowly pulls the heavy lacquered carriage across the avenue, wooden wheels creaking. Vlogger quickly steps back toward the willow tree, glancing sideways with caution and bowing slightly.
  3-6s: She brings the camera close to her face, keeping her head low and eyes cautious.
  6-8s: Whispering in hushed, tense tones straight into the lens: "ぎっしゃが来た。牛車。みんな、道を空けて下向いてる。……誰も中を見ようとしない。"
  Audio: Heavy slow clopping of ox hooves, low creaking of wooden wheels, silence of the crowd. No background music.
  ```
- **Narrator Text**: `ぎっしゃが来た。牛車。みんな、道を空けて下向いてる。……誰も中を見ようとしない。`

---

#### Scene 7 (CONTINUATION) — Beat 10: Beat Lắng Bên Bờ Sông Kamo
- **Character Names**: `["Vlogger", "Kamo Riverbank"]`
- **Prompt (Frame 0)**:
  ```
  Authentic smartphone selfie photograph, vertical 9:16, 28mm front camera. TIGHT WAIST-UP SELFIE FRAMING. PAN-FOCUS f/8-f/11, ZERO BOKEH. Soft grey late-afternoon daylight 5800K. Standing on the wide gravel bed of Kamo river. Shallow clear braided water, wild susuki grass. Off to one side, simple weathered wooden grave tablets lean unevenly in the grass. An old woman places a bundle of reeds in silence. Her free hand hangs still at her side. STRICT ETHNICITY LOCK: 100% native Japanese.
  ```
- **Video Prompt (8s)**:
  ```
  0-3s: River breeze blowing wild susuki pampas grass. She turns slowly to glance at the weathered wooden tablets standing by the gravel bank, eyes softened with quiet contemplation.
  3-6s: She turns back to the camera, speaking slowly with a gentle, subdued, reflective voice.
  6-8s: Speaking with heartfelt sincerity: "川のそばに、木の札が立ってる。誰かを、とむらってるのかな。名前を呼ぶ人がいる限り、その人は消えないんだと思う。"
  Audio: Soft flowing water, rustling dry grass in the river wind. No background music. Keep natural sound effects.
  ```
- **Narrator Text**: `川のそばに、木の札が立ってる。誰かを、とむらってるのかな。名前を呼ぶ人がいる限り、その人は消えないんだと思う。`

---

#### Scene 8 (CONTINUATION) — Beat 11: Kỳ Quan: Cột Son Cổng Suzaku & Đại Điện
- **Character Names**: `["Vlogger", "Suzaku Avenue and Palace"]`
- **Prompt (Frame 0)**:
  ```
  Authentic smartphone selfie photograph, vertical 9:16, 28mm front camera. TIGHT WAIST-UP SELFIE FRAMING. PAN-FOCUS f/8-f/11, ZERO BOKEH. Cool daylight. Standing inside Daidairi palace enclosure beside a massive round timber pillar coated in weathered, faded red-ochre lacquer. Across the open court stands the great Daigokuden audience hall on a raised earthen-stone foundation with broad timber steps. Her free hand is laid flat against the aged red pillar. STRICT ETHNICITY LOCK: 100% native Japanese.
  ```
- **Video Prompt (8s)**:
  ```
  0-3s: Her palm slides gently across the weathered chalky red lacquer of the giant pillar, feeling the wood grain beneath her fingers. She gazes up at the vast dark grey ceramic roof of Daigokuden.
  3-6s: She turns to the lens, face filled with solemn historical reverence.
  6-8s: Speaking in a low, reverent voice: "この朱色、本物。だいごくでん、まだ建ってる。……百七十七年後に焼けて、その後は再建されないんだ。"
  Audio: Open courtyard breeze, distant deep bell tone, muffled footsteps of distant courtiers. No background music.
  ```
- **Narrator Text**: `この朱色、本物。だいごくでん、まだ建ってる。……百七十七年後に焼けて、その後は再建されないんだ。`

---

#### Scene 9 (CONTINUATION) — Beat 12: Kết: Chiếc Lược Kỷ Niệm Lúc Hoàng Hôn
- **Character Names**: `["Vlogger", "Kamo Riverbank", "Boxwood Comb"]`
- **Prompt (Frame 0)**:
  ```
  Authentic smartphone selfie photograph, vertical 9:16, 28mm front camera. TIGHT WAIST-UP SELFIE FRAMING. PAN-FOCUS f/8-f/11, ZERO BOKEH. Low warm sunset amber light 4600K across Kamo river gravel. Higashiyama hills turning deep blue. Vlogger smiling warmly. In her raised free hand she holds up the small pale boxwood comb from Scene 4, turned to catch the evening light. Behind her, villagers walk home across the shallows. STRICT ETHNICITY LOCK: 100% native Japanese.
  ```
- **Video Prompt (8s)**:
  ```
  0-3s: Low golden sunset light glinting across the Kamo river. She raises the boxwood comb into the light, smiling fondly at it before tucking it safely into her kosode sash.
  3-6s: She looks warmly into the camera lens, giving a slight, grateful nod to the viewers.
  6-8s: Speaking warmly and tenderly with a peaceful smile: "あのくし、ヘアゴムと交換してもらえた。千年後の世界に、これだけ持って帰ります。平安京、いい街でした。"
  Audio: Gentle evening water flow, distant cicadas or crickets, peaceful river breeze. No background music.
  ```
- **Narrator Text**: `あのくし、ヘアゴムと交換してもらえた。千年後の世界に、これだけ持って帰ります。平安京、いい街でした。`

---

#### Scene 10 (ROOT) — Coda: Flycam Hoàng Hôn Sông Kamo (Câm)
- **Character Names**: `["Kamo Riverbank"]`
- **Prompt (Frame 0)**:
  ```
  Authentic photorealistic establishing aerial drone photograph (flycam), 4K, 28mm wide-angle, vertical 9:16. PAN-FOCUS f/8-f/11, ZERO BOKEH. Low sunset light 4600K skimming just above dry susuki grass and pale gravel bars of Kamo river. The shallow braided channels reflect amber light. Behind, the grid of Heian-kyo stretches west toward the dark silhouette of the mountains. NO vlogger in frame. STRICT ETHNICITY LOCK: 100% native Japanese.
  ```
- **Video Prompt (8s)**:
  ```
  0-3s: Smooth fluid aerial glide soaring low over the glowing water channels and golden susuki plumes of Kamo river.
  3-8s: Stepping into a high, majestic climb as the capital slips into dusk, hearth smoke rising from small wooden houses under the glowing evening sky.
  Audio: Solitary, gentle koto melody fading slowly into quiet evening river wind. NO dialogue, NO voiceover.
  ```
- **Narrator Text**: ` ` *(Để trống — Flycam câm)*

---

## 🛠️ CÁCH TRIỂN KHAI TRONG FLOWKIT

### Bước 1: Tạo dự án Heian 1000 qua script tự động
Chạy script tự động có sẵn để nạp toàn bộ kịch bản này vào FlowKit API:
```bash
python scripts/create_kyoto_heian_1000.py
```

### Bước 2: Sinh tài nguyên theo pipeline của FlowKit
Sau khi project được tạo:
```bash
# 1. Sinh ảnh mẫu cho các thực thể nhân vật, bối cảnh, đạo cụ
/fk-gen-refs <project_id>

# 2. Sinh ảnh Frame 0 cho toàn bộ 10 phân cảnh
/fk-gen-images <project_id> <video_id>

# 3. Sinh 10 đoạn video ngắn 8s
/fk-gen-videos <project_id> <video_id>

# 4. Review chất lượng video bằng AI Vision
/fk-review-video <video_id>

# 5. Sinh giọng đọc tiếng Nhật tự nhiên
/fk-gen-narrator <video_id>

# 6. Ghép hoàn chỉnh và đồng bộ độ dài video theo giọng đọc
/fk-concat-fit-narrator <video_id>
```
