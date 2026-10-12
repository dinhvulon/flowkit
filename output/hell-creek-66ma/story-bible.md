# I Time Travelled to the Last 12 Hours of the Dinosaurs — story bible

## Thông tin dự án
- Thể loại / định dạng: POV time-travel vlog (hư cấu, Rule 14 ngoại lệ), long-form, thời lượng thật **≈ 10:08** (608s), 16:9, thoại tiếng Anh, giọng Laomedeia
- Đường vào: **có bản nháp** → điền ngược giai đoạn 1–3 từ script, mục thiếu ghi **THIẾU** → thành danh sách sửa ở giai đoạn 6. Khung cấu trúc: **起承转合 (khởi–thừa–chuyển–hợp) + 结尾八法 (tám kiểu kết)** thay cho BS2
- Khán giả: YouTube, người xem documentary/khủng long; chi phí: **117 lượt sinh** Omni Flash R2V = 50×4s (11 chuỗi = 30 mắt xích + 20 clip lẻ) · 16×6s · 46×8s · 5×10s
- Thể loại theo Snyder: **Dude with a Problem** (survival/disaster)
- File liên quan:
  - `script.md` — bản 3 (2026-10-12): §1–§12, storyboard §9 có cột `Dur`, 117 lượt sinh, ~10:08
  - Repo QC vendored: `skills/character-scene-design-skills-main/` (cổng 5.5, Q1–Q4)

## Giai đoạn hiện tại
- Giai đoạn: **6 (sửa) xong vòng 2** — F1–F13 đã làm; thời lượng nâng lên 10:08 bằng 6 tình tiết mới thay vì kéo giãn clip; 4 mặc định mở giữ nguyên
- Bước tiếp: user duyệt storyboard bản 3 (cổng ⛔ §12) → giai đoạn 5: viết `video_prompt` JSON (Rule 55) + `python tools/lint_prompt.py`

## Quyết định đã chốt (chỉ ghi kết luận; đổi phải ghi nhật ký)
- Nhân vật: Nora, một mình, không vũ khí, không cận chiến (Rule 51)
- Địa điểm: Hell Creek, Montana, cách tâm Chicxulub ≈ 3.000 km
- Kết: Nora ở lại chứng kiến; cảnh cuối 0 từ; cắt thẳng sang đen
- Trục giờ: **12 giờ** (HOUR 0 ≈ 06:00 → va chạm HOUR 12 ≈ 18:00)
- Đàn Triceratops là "bộ tộc"; không đánh nhau
- **Độ dài clip không cố định** (user): cảnh dễ lỗi → chuỗi 4s cùng bối cảnh; cảnh dễ, không chuyển cảnh → 8s/10s; 6s cho beat ngắn có thoại. Số từ theo Rule 49 (0)
- **Kéo thời lượng lên 10:00 (đo thật 10:08)**: không kéo giãn clip mà thêm 6 tình tiết mới thay đổi tình thế của Nora, dồn thời lượng vào phần 承 (Thừa)

## 1 Premise và chủ đề
- Ý tưởng gốc: đứng giữa ngày cuối của một thế giới, biết trước điều sắp đến mà không đổi được gì
- Chủ đề một câu: biết trước không cứu được ai; biết lắng nghe thì sống
- **Premise** (Egri): *Lắng nghe thay vì cậy biết trước dẫn đến sống sót* (mặc định, chờ xác nhận)
- **Controlling idea** (McKee, **mỉa mai**): Nora sống sót vì học ngôn ngữ của đàn chứ không nhờ biết trước, nhưng đó là ngôn ngữ của một thế giới đang tắt (mặc định, chờ xác nhận)
- Tuyến thứ ba (Cron):
  - **Want**: tận mắt chứng kiến ngày cuối
  - **Misbelief**: "biết trước = được làm khán giả đứng ngoài, an toàn" — **nói ra ở A1-05** *"I'm just here to watch"* (0:38) + củng cố sai lầm ở **A1-S1** *"they're vegetarians, they'll ignore me"* → HỎNG 1 là hậu quả trực tiếp
  - **Origin scene**: không flashback (vlog); câu A1-05 gánh thay — ĐẠT theo thể loại
  - Cảnh chuyển: A1-S1 (chủ quan) → A1-12 chuỗi (Bò Đực xông) → A2-R3 (Acheroraptor rình: ở mép là làm mồi) → A2-14 "Their silence is my alarm now" → A3-D3 (nghe đất khi thú không có diềm) → A3-W3 (uống theo lượt) → A3-Q1 (Con Non ngủ tựa Nora) → A3-17 "Almost forgot what today is" (yên ổn giả)
  - Misbelief bị đánh bại: **A4-04** *"I knew the hour, the place, the distance. / I thought knowing meant I'd be watching. / I'm not watching."* — ĐẠT
- **戏核**: đàn đứng sững = có thứ đang tới
- **戏胆**: mai rùa (nước) + bùn đỏ và lá cọ (khiên) + hốc dưới bờ lạch
- **戏眼**: bóng thứ hai mọc ngược hướng (A4-03 chuỗi); T. rex xé khói chạy trốn (A4-T1 chuỗi); bàn chân Con Non đặt cạnh mặt Nora (MASTER)
- 5 câu Hicks: Nora · đối thủ là chính ngày hôm đó (đàn là người gác cổng) · cần đàn chỉ đường tới nước và chỗ trú · khán giả → thành viên → kẻ cuối cùng còn lại · chính cô chọn ngày này
- **Logline** (chờ xác nhận): Một vlogger du hành thời gian cố tình đến Hell Creek đúng 12 giờ trước khi thiên thạch rơi, tưởng mình chỉ đến để xem. Bị đàn Triceratops xua đuổi và cạn nước, cô phải học đọc sự im lặng của chúng, vì khi bầu trời bốc cháy, biết trước không cứu được cô; chỉ con non biết chỗ trốn.
- Luật thế giới (lộ trong phút đầu): chớp sáng → sóng địa chấn (~10 phút) → mưa thủy tinh (~30 phút) → trời cháy (~1 giờ); nước chỉ có ở lạch cá sấu và hố nước; không vũ khí

## 2 Cấu trúc (起承转合, đo từ cột "Dựng" §9 = **10:08 / 608 s**)

| Phần | Clip | Thời gian | Tỷ lệ | Chuẩn | Đánh giá |
|---|---|---|---|---|---|
| 起 Khởi | CO + EST-01 + Act 1 (17 lượt) | 0:00–1:57 | 19% | ngắn, vào việc nhanh | ĐẠT (+7s từ A1-S1) |
| 承 Thừa | Act 2 + EST-02 + Act 3 + EST-03 (63 lượt) | 1:57–7:09 | 51% | dài nhất (~2/3 phim) | ĐẠT (+81s từ Vòng tròn đàn, Đàn mỏ vịt, Cá sấu hố nước, Giờ thứ 11) |
| 转 Chuyển | Act 4 + MASTER (28 lượt) | 7:09–9:05 | 19% | cao trào | ĐẠT (+14s từ Cây cọ cháy + T. rex chạy trốn) |
| 合 Hợp | Act 5 (9 lượt) | 9:05–10:08 | 11% | ngắn nhất, dư vị | ĐẠT (giữ nguyên 1:03) |

- Mở: cold open (MASTER 0–8s) → A1-01 cá sấu áp sát
- Inciting incident: A1-01/02 (lạch cá sấu); A1-05 đồng hồ 12h + misbelief (0:38)
- Sai lầm trực tiếp: A1-S1 "they're vegetarians, they'll ignore me" → HỎNG 1 A1-12a/b/c
- Câu hỏi 13 (đáp án đúng có ở Act 1 và bị từ chối): A1-06 hốc khô dưới bờ lạch, Nora gạt đi vì cá sấu → payoff A4-16 — ĐẠT
- Plot point I: A1-14 "And I wait" — Nora **tự quyết**
- Vòng tròn đàn: A2-R1→R5 (Acheroraptor rình ở mép đàn, Nora lách vào khe, hiểu "đứng ở mép là làm mồi")
- Midpoint: A2-15 "furniture now" (dời sang ~4:10, 41-45%) — chiến thắng giả có nền tảng vững chắc từ bài học A2-R
- HỎNG 2: chuỗi A3-06 vỡ mai rùa → A3-08 Nora **tự đọc dấu chân** tìm lại đàn
- Đàn mỏ vịt: A3-D1→D3 (Edmontosaurus không có diềm, chạy loạn; học nghe tiếng rung của đất)
- Cá sấu ở hố nước: A3-W1→W3 (uống theo lượt; con canh ngẩng đầu)
- Bò Đực: A3-14 Nora qua mặt nó bằng luật Act 2 → payoff A5-05 sừng gãy trong tro
- Giờ thứ 11: A3-Q1→Q2 Con Non ngủ dựa Nora, thằn lằn bay về phía nam
- Plot point II: chuỗi A4-03 bóng thứ hai
- All is lost: A4-12 "Where do I go?" — đối nghịch midpoint
- Cọ cháy & T. rex chạy loạn: A4-P1, A4-T1/T2, A4-P2 (chúa tể cũng tháo chạy, không săn, không đánh)
- Khủng hoảng tĩnh: **A4-14** đàn lên rừng phía bắc vs Con Non xuống lạch cá sấu → "Follow the kid." — ĐẠT
- Cao trào: A4-15 → MASTER bùn + lá cọ, chui hốc, bàn chân Con Non — Nora tự làm bằng kỹ năng Act 2
- Kết: A5-09 (10s, 0 từ) — Con Non đi vào màn tro, Nora nhổm dậy rồi ngồi lại, cắt đen. Lời cuối ở A5-07
- Kiểu kết: **延伸式** + **呼应式** (cold open ↔ MASTER; bờ lạch đầu ↔ cuối)

## 3 Nhân vật và xung đột

| Nhân vật | Sinh lý | Xã hội | Tâm lý / premise riêng | Loại cụ thể | Thái độ với chủ đề | Quan hệ với Nora |
|---|---|---|---|---|---|---|
| Nora | 178 cm, khỏe, không vũ khí | Vlogger hiện đại, kẻ ngoài | Tò mò, dry humor; tin vào biết trước | Khán giả tự tin | biết → lắng nghe | — |
| Con Cái Già | Diềm ửng đỏ khi cảnh giác | "Radar" của đàn | Cảnh giác tuyệt đối | Trí giả (Jung) | Lắng nghe là sống | Thầy không lời |
| Bò Đực | Sừng trái gãy | Người gác ngưỡng | Lãnh thổ | Người gác cổng | — | Thử thách đầu (A1-12) → bị vượt bằng luật (A3-14) → sừng gãy trong tro (A5-05) |
| Con Non | Lăn bùn đỏ | Con non của đàn | Tò mò, bản năng | Đối tượng tình cảm + người dẫn đường | Bản năng > kiến thức | Bạn → người cứu |
| T. rex | Ruồi quanh mõm | Kẻ săn | — | Cái bóng (Jung) | — | Mối đe dọa (chuỗi A2-12) → đồng nạn nhân tháo chạy (A4-T1/T2). Không đụng độ, không săn cô |
| Acheroraptor ×2 | Dài 2.5 m, lông nâu xám, móng liềm | Kẻ ăn thừa bám vệt T. rex | Cơ hội, rình mò mép ngoài | Kẻ thử thách ngưỡng (Act 2) | Kẻ yếu ở mép là mồi | Buộc Nora phải tìm cách vào trong vòng tròn đàn (A2-R1→R5) |
| Edmontosaurus Herd | Mỏ vịt, mặt trơn, không sừng diềm | Đàn ăn thực vật khác | Hoảng hốt, phản ứng theo đất | Lực cản / bài học mới | Không nghe đất thì chết | Dạy Nora luật 4: nghe rung chấn mặt đất (A3-D1→D3) |
| Borealosuchus | Hai dải lưng | — | Kiên nhẫn | Chướng ngại | — | Canh giữ nước và hốc (A1-01, A3-W2) |
| Vụ va chạm | Chớp, sóng, thủy tinh, tro | — | Vô tri | Đối thủ tuyệt đối | — | Thứ cô đến để xem |

- Vật ràng buộc: thung lũng và nước; chỉ khi ảo tưởng "khán giả" chết (A4-04) mới thoát
- Dao của đối thủ: đàn đi nhanh hơn cô chạy; nước cạn; cấm đánh T. rex; lạch đầy cá sấu; raptor rình mép; cây đổ cháy
- Xiềng xích của Nora: không vũ khí; không cận chiến; không biết ngôn ngữ thú; biết trước nhưng không đổi được gì
- "Đối thủ mạnh nhất là chính mình": misbelief khán giả (A1-S1, A3-17 yên ổn giả)
- Thang trưởng thành: du khách tự tin (A1-S1) → bị từ chối (A1-12) → học vòng tròn đàn (A2-R) → được dung thứ (A2-15) → tự đọc dấu (A3-08) → học nghe đất (A3-D) → học uống theo lượt (A3-W) → vượt Bò Đực (A3-14) → thấy chúa tể chạy loạn (A4-T) → chọn theo Con Non (A4-14) → sống sót → nhân chứng
- Hệ hình ảnh: bóng (một → hai), nước (mai rùa → hố nước → lạch xám), đỏ (diềm → bùn → trời), tro phủ dần

## 4 Danh sách cảnh
- Storyboard: `script.md` §9 — **118 dòng / 117 lượt sinh** (CO cắt từ MASTER)
- 11 chuỗi 4s: A1-12a/b/c · A2-12a/b/c · A2-R2a/b/c · A3-06a/b/c · A3-12a/b · A3-D2a/b/c · A3-W2a/b · A4-03a/b/c · A4-07a/b/c · A4-T1/T2 (mỗi chuỗi tính là 1 shot cho luật góc máy)
- Clip mới bổ sung ở bản 3:
  - Act 1: A1-S1 (bước ra tự tin vì tin thú ăn cỏ vô hại, 8s)
  - Act 2: A2-R1, A2-R2a/b/c, A2-R3, A2-R4 (vòng tròn đàn chống Acheroraptor, 6 clip)
  - Act 3: A3-D1, A3-D2a/b/c, A3-D3 (đàn Edmontosaurus mỏ vịt, nghe đất, 5 clip)
  - Act 3: A3-W1, A3-W2a/b, A3-W3 (cá sấu hố nước & uống theo lượt, 4 clip)
  - Act 3: A3-Q1, A3-Q2 (giờ thứ 11, Con Non ngủ tựa chân, thằn lằn bay tránh bão, 2 clip)
  - Act 4: A4-P1 (cọ cháy đổ), A4-T1/T2 (T. rex xé khói chạy loạn), A4-P2 (chúa tể cũng chạy, 4 clip)
- Thứ tự sinh: §12 — chuỗi khó nhất trước (A1-12 → A2-12 → A2-R2 → A4-07 → A4-T1/T2 → MASTER → A4-03 → A3-06)

## 5 Tiến độ bản nháp
- 2026-10-12: bản 1 §1–§12 (80 lượt, 8:07)
- 2026-10-12: bản 2 — F1–F12 áp dụng, độ dài clip biến thiên, 91 lượt, 8:17
- 2026-10-12: bản 3 — F13 áp dụng, nâng thời lượng lên 10:08 (608s), 117 lượt sinh, thêm 6 cụm tình tiết mới có chuyển biến kịch tính, hoàn thiện 起承转合 51% Thừa

## 6 Sửa (thứ tự thực hiện)

| # | Mục tiêu | Nguồn | Trạng thái |
|---|---|---|---|
| F1 | Đồng bộ trục 12h: thẻ C1–C8 HOUR 0/1/4/6/8/10/11/12; header Act | Sổ liên tục | xong |
| F2 | Thẻ trỏ đúng clip: C3 → A2-10; C5 → A3-06b; C6 → A3-W1; C7 → A3-Q1; C8 → A4-03a | Sổ liên tục | xong |
| F3 | Header thời lượng/số clip theo số đo thật (10:08 / 117) | Format | xong |
| F4 | Act 5 rút 12 → 9; dồn lượt sinh sang 承 | Structure Q10 | xong |
| F5 | Khủng hoảng tĩnh A4-14 | McKee crisis | xong |
| F6 | Gieo hốc ở A1-06 | Structure Q13 | xong |
| F7 | Misbelief nói ra A1-05, củng cố sai ở A1-S1, bị đánh bại A4-04 | Cron | xong |
| F8 | HỎNG 2 dạy kỹ năng dùng lại: A3-08 tự đọc dấu | "mỗi thất bại dạy một điều" | xong |
| F9 | Payoff Bò Đực: A3-14 + A5-05 | Character Q9 | xong |
| F10 | Bỏ giọng giảng giải A1-03, A4-04 | memory: không bài học lịch sử | xong |
| F11 | A5-09: nhổm dậy rồi ngồi lại | Structure Q8 | xong |
| F12 | Chạy 5 bảng chẩn đoán vòng 1 (bản 2) | sw-workflow giai đoạn 6 | xong |
| F13 | Mở rộng 10 phút: thêm 6 tình tiết mới (+26 lượt sinh, 117 lượt, 10:08), chia lại 起承转合, chạy lại chẩn đoán vòng 2 | sw-workflow + sw-story-structure | xong |

### Kết quả F12 & F13 (bản 3 - 10:08)
- **sw-scene-craft 13**: 118 clip/mắt xích, mỗi clip có một hành động và một chuyển giá trị rõ ràng (+/-); 11 chuỗi 4s nối bằng tư thế cuối (`chain.opens_on`); không cặp clip liền kề nào trùng cả góc máy và cỡ cảnh (trừ mắt xích nội bộ chuỗi). ĐẠT
- **sw-dialogue 14**: chỉ Nora nói; số từ thoại khớp chuẩn Rule 49 (0) theo từng độ dài clip `Dur`; các phân đoạn xuất hiện dã thú (T. rex, Acheroraptor, Borealosuchus, Edmontosaurus) đều tuân thủ triệt để Sonic Isolation (0 từ thoại); không có thoại giải thích bài học lịch sử. ĐẠT
- **sw-genre-anatomy 12** (Dude with a Problem): người thường + thảm họa tuyệt đối + thời hạn đếm ngược 12h. Nora tự chọn vấn đề (tưởng mình là khán giả) làm nổi bật tính châm biếm sâu sắc của controlling idea. ĐẠT
- **Snyder 9 câu & Rule 51**: nhân vật chủ động giải quyết bài toán sinh tồn; không có cảnh chiến đấu/cận chiến; T. rex xuất hiện lần 2 ở Act 4 cũng là nạn nhân tháo chạy kinh hoàng trước sóng nhiệt. ĐẠT
- **sw-format-adaptation A12**: kiểm toán từ cấm đạt 0 lỗi (không có `phone`, `smartphone`, `screen`, `device`, `selfie-stick`); tỷ lệ selfie hợp lý, không có 3 selfie liền kề; định dạng storyboard cột `Dur` đầy đủ. ĐẠT

## 7 Phát hành
- Logline: xem §1
- Tiêu đề: "I Time Travelled to the Last 12 Hours of the Dinosaurs"; thoại tiếng Anh → SEO tiếng Anh (Rule 20)
- Không timestamp, không chapter cho vlog POV

## Câu hỏi mở (đã áp mặc định, chờ user xác nhận)
1. Thời lượng: nâng lên ~10 phút (10:08 / 117 lượt sinh, 6 cụm tình tiết mới) → **đã áp**
2. Premise / controlling idea ở §1 → **giữ nguyên**
3. "So I'll just stay" là một lựa chọn thật → **đã áp**
4. A5-09: Nora nhổm dậy rồi ngồi lại → **đã áp**

## Nhật ký quyết định
- 2026-10-12: Lập bible theo sw-workflow, đường vào "có bản nháp", khung 起承转合 + 结尾八法 ← user chọn
- 2026-10-12: Chốt trục giờ 12h, bỏ 18h ← thoại A1-05/A5-08 và hình học bóng A4-03 chỉ khớp với 12h
- 2026-10-12: Thời lượng thật bản 1 là 8:07 (đo cột "Dựng" §9), không phải 9:45
- 2026-10-12: **Độ dài clip biến thiên + chuỗi 4s** cho cảnh dễ lỗi; 8s/10s cho cảnh dễ không chuyển cảnh ← user. Skill + CLAUDE.md đã cập nhật
- 2026-10-12: Áp 4 mặc định cho câu hỏi mở để viết bản 2 (91 lượt sinh, 8:17)
- 2026-10-12: **Nâng thời lượng lên ~10:00 (đo thật 10:08, 117 lượt sinh)** theo `sw-workflow` và `sw-story-structure`: từ chối giải pháp kéo giãn clip (tránh khoảng lặng vô nghĩa), chọn giải pháp thêm 6 cụm tình tiết mới thay đổi tình thế của Nora (A1-S1, A2-R vòng tròn đàn, A3-D đàn mỏ vịt, A3-W cá sấu hố nước, A3-Q giờ thứ 11, A4-P/T T. rex chạy loạn). Phân bổ lại 起承转合: Thừa chiếm 51%, Hợp 11%. Chạy lại 5 bảng chẩn đoán đạt chuẩn.

Bước tiếp: user duyệt storyboard bản 3 (§9 trong script.md) và các cập nhật trong story-bible.md → giai đoạn 5 viết video_prompt JSON + lint → cổng Rule 29 (hỏi trước khi sinh bất cứ thứ gì).
