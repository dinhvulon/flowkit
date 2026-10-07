# Hậu kỳ, đóng gói YouTube & chiến lược kênh

Đọc ở **Bước 10–11** của `SKILL.md`. Thay Bước 5–7 và mục 1b cũ.

## 1. Hậu kỳ — đồng nhất để trông như footage của một máy
- **Cắt thẳng theo khung che** (`transitions.md`); jump cut khi đi bộ để nguyên. Nhịp dựng theo `story-engine.md` mục 13b.
- **Nhạc + ambient liên tục** qua `/fk-gen-music` (nhạc cụ truyền thống của thời kỳ, không lời), mix dưới thoại; hạ nhạc ở cảnh nguy hiểm và cảnh kết, không tắt hẳn giữa scene.
- **SFX nhẹ** ("vút") khi vật thể lướt qua ống kính; **J-cut** ambient scene sau vào sớm ~0.5s.
- **Grade ấm, hoàng hôn ở cuối; thêm grain nhẹ** để đồng nhất các clip (clip AI sinh riêng lẻ thường lệch màu). Làm trong CapCut, hoặc ffmpeg trên file final, ví dụ:
  ```bash
  ffmpeg -i final.mp4 -vf "colorbalance=rs=0.03:bs=-0.03,noise=alls=5:allf=t" -c:a copy final_graded.mp4
  ```
  Thử trên một đoạn ngắn trước — grain quá tay làm mất cảm giác điện thoại.
- **Chữ trên màn hình** chỉ 3 loại: năm, mission card, countdown `HOUR X — Y HOURS REMAINING` (`story-engine.md` mục 9). Có thể render card bằng công thức ffmpeg của `/fk-cinematic-transitions` mục 2, nhưng **bỏ** fade/dip-to-black và drone bumper — card đè lên hình, cắt thẳng.
- **Mix & master âm thanh (`/fk-sound-design`):** thoại native của vlogger là lớp 1; ambient/nhạc duck −12 đến −15 dB khi có thoại; master cuối `loudnorm=I=-14:LRA=7:TP=-1.0` (−14 LUFS cho YouTube). `scripts/sfx_layering.py` tự thêm SFX theo từ khóa trong prompt — chỉ dùng khi clip thiếu tiếng va chạm, nghe lại trước khi giữ.
- Phụ đề tùy chọn, chỉ dạng `.srt` rời — **không** burn hardsub (`scripts/generate_subtitles.py --burn-subtitles` của luồng cinematic không áp dụng cho vlog).
- **Bíp chửi thề**: phủ tiếng bíp ~0.3s tại mỗi mốc `bleep_at` trong Clip JSON (xem lại clip trước khi bíp vì model có thể lệch mốc vài trăm mili-giây).

## 2. Đóng gói YouTube
- `/fk-youtube-seo` — **3 tiêu đề chuẩn High-Stakes / Sinh tồn nghẹt thở**:
  - *Option 1 (Nguy hiểm cận kề / Khuyên dùng)*: `I Time Travelled to [Year] — And Almost Got Trampled by a [Threat]`
  - *Option 2 (Câu hỏi sinh tồn)*: `Would [People] Let You Into Their [Cave/Camp]? ([Year])`
  - *Option 3 (Shock văn hóa & Nghịch lý)*: `What Happens When You Show a Lighter to [People]?`
  - Tiêu đề nào cũng phải có tên tộc người cụ thể (`Neanderthals`, không phải `Ancient People`) hoặc niên đại. **Không dùng `I Survived 24 Hours`** (user bỏ 2026-10-06) — mốc 24 giờ chỉ dùng trong truyện.
  - Ngôn ngữ SEO + thumbnail khớp ngôn ngữ thoại (CLAUDE.md Rule 20).
  - Mô tả có **timestamp theo beat/hồi**, bộ tag chuẩn SEO, tuyệt đối không dùng tiêu đề hiền/giáo khoa.
- `/fk-thumbnail` — Thumbnail High-Stakes: Mặt nhân vật hoảng loạn/adrenaline cực độ né mối nguy cận kề (chân voi ma mút giẫm, giáo chĩa, bão tuyết -40°C) + Text 2 dòng kích thích tò mò (Line 1: `ALMOST TRAMPLED!` / `-40°C SURVIVAL!` / `THEY SAW FIRE!`; Line 2: Địa điểm & Niên đại bằng tiếng Anh); 16:9 (long-form) hoặc 9:16 (Shorts).
- **Bật nhãn "Altered or synthetic content"** trong YouTube Studio khi upload — `/fk-youtube-upload` hiện không tự đặt nhãn này, phải bật tay.

## 3. Chiến lược "Mồi Thuật Toán" Sau Phát Hành (Algorithm Seeding)
Đừng chỉ đăng 1 video dài rồi ngồi đợi phép màu. Hãy áp dụng **Quy trình 3 bước "Mồi Thuật Toán"** để đưa kênh mới thoát mức vài trăm view:

1. **Vũ khí YouTube Shorts (Kéo traffic mồi qua "Related Video")**:
   - Cắt từ video dài ra **3 – 4 video Shorts (15–30s)** nhắm vào các cảnh giật gân nhất:
     - **Short 1 (Food Viral):** Cảnh đập xương voi/nếm món ăn kỳ lạ của thời kỳ (Ẩm thực luôn viral mạnh nhất).
     - **Short 2 (Adrenaline Chase):** Cảnh rượt đuổi nghẹt thở, voi ma mút/quái thú tấn công, chạy tháo thân trong bão tuyết.
     - **Short 3 (Prehistoric Lifehack):** Kỹ thuật sinh tồn kỳ lạ (đun sôi nước bằng đá nung đỏ, may áo ấm -40°C).
   - **Gắn tính năng "Related Video" trong YouTube Studio**: Để người xem Short bấm 1 chạm chuyển thẳng sang xem full video dài 7.5–10 phút. Shorts sẽ dễ dàng đạt vài nghìn đến vài chục nghìn view, từ đó "bơm" khán giả thật sang video dài.
2. **Kiểm tra 2 chỉ số sống còn sau 48h**:
   - **CTR (Click-Through Rate):** Phải $\ge 6\%$. Nếu dưới $4\%$, đổi ngay sang Title Option khác (Option 1/2/3) và bộ Thumbnail dự phòng đã chuẩn bị sẵn.
   - **AVD (Average View Duration):** Tỷ lệ giữ chân người xem 30 giây đầu phải $\ge 60\%$.
3. **Giữ nhịp phát hành 2 tuần/video**:
   - Đừng để kênh "ngủ đông" 1 tháng. Hãy duy trì đều đặn: **2 tuần = 1 video dài (7–10 phút) + 4 Shorts xen kẽ** (mỗi tuần 2 Shorts cắt từ video dài đó) để thuật toán YouTube ghi nhận kênh đang hoạt động tích cực.

## 4. Chọn chủ đề: săn trend đang lên (mục 1b cũ)

Để kéo kênh mới từ vài trăm view lên hàng chục nghìn đến hàng triệu view, bắt buộc phải chọn các chủ đề có sức hút tự nhiên cực mạnh (**High-Stakes & Tò mò tột độ**):

1. **Nhóm 1: Sự kiện thảm họa lịch sử có thật (CTR cao nhất)**:
   - Khán giả thế giới bị ám ảnh bởi việc "nhân vật cầm điện thoại livestream trực tiếp thảm họa":
   - **Đắm tàu Titanic (1912):** Thử cảnh báo thuyền trưởng về tảng băng trôi (video của Chloe đạt 4.3M view chính nhờ motif này).
   - **Núi lửa Vesuvius chôn vùi Pompeii (79 SCN):** Livestream lúc bầu trời chuyển sang màu đen và tro bụi nóng 500°C đổ ập xuống.
   - **Thảm họa hạt nhân Chernobyl (1986):** Vlogger vô tình bước vào Pripyat đúng lúc còi báo động phát nổ.
   - **Đại dịch Cái Chết Đen (Black Death - Châu Âu 1348):** Bác sĩ mỏ chim và sự hoang tàn nghẹt thở của thành phố.
   *(Khớp với Title Option 1: Nguy hiểm cận kề & Thumbnail V1: Immediate Peril / V4: Sprint for Life)*

2. **Nhóm 2: "Văn hóa hiện đại va chạm cổ đại" (Modern Shock / Bị coi là phù thủy)**:
   - Tạo xung đột kịch tính giữa công nghệ hiện đại và sự mê tín / tàn bạo thời xưa:
   - **Phiên tòa xử phù thủy Salem (Salem Witch Trials 1692):** Cầm iPhone chụp ảnh và bị cả làng vây bắt đòi thiêu sống.
   - **Ghé thăm Đấu trường La Mã (Rome 80 SCN):** Ngày khánh thành Colosseum, bị đẩy xuống đấu với giác đấu sĩ.
   - **Thời đại Viking (Scandinavia 870 SCN):** Lạc vào đại sảnh của các chiến binh Viking cuồng nộ.
   *(Khớp với Title Option 3: Shock văn hóa & Thumbnail V3: Culture Shock / Standoff)*

3. **Nhóm 3: Newsjacking & Ăn theo Hollywood (Bơm traffic tự nhiên cho kênh mới)**:
   - Đón đầu các dự án phim sắp chiếu hoặc sự kiện truyền thông: Khi phim tài liệu/bom tấn về La Mã, Ai Cập hay Chiến tranh ra rạp, lượng tìm kiếm tăng vọt hàng trăm lần. Bạn ra video cùng chủ đề ngay trước ngày công chiếu để đón đầu dòng người tìm kiếm.
   - *Ví dụ:* Phim *Gladiator 2* ➔ Video *Rome 80 AD (Colosseum)*; Phim về Napoleon ➔ Video *Waterloo 1815*; Khám phá mộ cổ Ai Cập ➔ Video *Giza 2400 BC*.
   *(Khớp với Title Option 2: Câu hỏi sinh tồn)*
