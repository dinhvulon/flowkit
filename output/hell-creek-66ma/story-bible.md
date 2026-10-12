# I Time Travelled to the Last 12 Hours of the Dinosaurs — story bible

## Thông tin dự án
- Thể loại / định dạng: POV time-travel vlog (hư cấu, Rule 14 ngoại lệ), long-form, thời lượng thật **≈ 8:17**, 16:9, thoại tiếng Anh, giọng Laomedeia
- Đường vào: **có bản nháp** → điền ngược giai đoạn 1–3 từ script, mục thiếu ghi **THIẾU** → thành danh sách sửa ở giai đoạn 6. Khung cấu trúc: **起承转合 (khởi–thừa–chuyển–hợp) + 结尾八法 (tám kiểu kết)** thay cho BS2
- Khán giả: YouTube, người xem documentary/khủng long; chi phí: **91 lượt sinh** Omni Flash R2V = 33×4s (6 chuỗi = 17 mắt xích + 16 clip lẻ) · 12×6s · 41×8s · 5×10s
- Thể loại theo Snyder: **Dude with a Problem** (survival/disaster)
- File liên quan:
  - `script.md` — bản 2 (2026-10-12): §1–§12, storyboard §9 có cột `Dur`
  - Repo QC vendored: `skills/character-scene-design-skills-main/` (cổng 5.5, Q1–Q4)

## Giai đoạn hiện tại
- Giai đoạn: **6 (sửa) xong vòng 1** — F1–F12 đã làm; 4 mặc định đang chờ user xác nhận (cuối file)
- Bước tiếp: user duyệt storyboard (cổng ⛔ §12) → giai đoạn 5: viết `video_prompt` JSON (Rule 55) + `python tools/lint_prompt.py`

## Quyết định đã chốt (chỉ ghi kết luận; đổi phải ghi nhật ký)
- Nhân vật: Nora, một mình, không vũ khí, không cận chiến (Rule 51)
- Địa điểm: Hell Creek, Montana, cách tâm Chicxulub ≈ 3.000 km
- Kết: Nora ở lại chứng kiến; cảnh cuối 0 từ; cắt thẳng sang đen
- Trục giờ: **12 giờ** (HOUR 0 ≈ 06:00 → va chạm HOUR 12 ≈ 18:00)
- Đàn Triceratops là "bộ tộc"; không đánh nhau
- **Độ dài clip không cố định** (user): cảnh dễ lỗi → chuỗi 4s cùng bối cảnh; cảnh dễ, không chuyển cảnh → 8s/10s; 6s cho beat ngắn có thoại. Số từ theo Rule 49 (0)

## 1 Premise và chủ đề
- Ý tưởng gốc: đứng giữa ngày cuối của một thế giới, biết trước điều sắp đến mà không đổi được gì
- Chủ đề một câu: biết trước không cứu được ai; biết lắng nghe thì sống
- **Premise** (Egri): *Lắng nghe thay vì cậy biết trước dẫn đến sống sót* (mặc định, chờ xác nhận)
- **Controlling idea** (McKee, **mỉa mai**): Nora sống sót vì học ngôn ngữ của đàn chứ không nhờ biết trước, nhưng đó là ngôn ngữ của một thế giới đang tắt (mặc định, chờ xác nhận)
- Tuyến thứ ba (Cron):
  - **Want**: tận mắt chứng kiến ngày cuối
  - **Misbelief**: "biết trước = được làm khán giả đứng ngoài, an toàn" — **nói ra ở A1-05** *"I'm just here to watch"* (0:38) — ĐẠT
  - **Origin scene**: không flashback (vlog); câu A1-05 gánh thay — ĐẠT theo thể loại
  - 3 cảnh chuyển: A1-12 chuỗi (Bò Đực xông → cô không vô hình) · A2-14 "Their silence is my alarm now" · A3-15 "Almost forgot what today is" (yên ổn giả)
  - Misbelief bị đánh bại: **A4-04** (5:53) *"I knew the hour, the place, the distance. / I thought knowing meant I'd be watching. / I'm not watching."* — ĐẠT
- **戏核**: đàn đứng sững = có thứ đang tới
- **戏胆**: mai rùa (nước) + bùn đỏ và lá cọ (khiên) + hốc dưới bờ lạch
- **戏眼**: bóng thứ hai mọc ngược hướng (A4-03 chuỗi); bàn chân Con Non đặt cạnh mặt Nora (MASTER)
- 5 câu Hicks: Nora · đối thủ là chính ngày hôm đó (đàn là người gác cổng) · cần đàn chỉ đường tới nước và chỗ trú · khán giả → thành viên → kẻ cuối cùng còn lại · chính cô chọn ngày này
- **Logline** (chờ xác nhận): Một vlogger du hành thời gian cố tình đến Hell Creek đúng 12 giờ trước khi thiên thạch rơi, tưởng mình chỉ đến để xem. Bị đàn Triceratops xua đuổi và cạn nước, cô phải học đọc sự im lặng của chúng, vì khi bầu trời bốc cháy, biết trước không cứu được cô; chỉ con non biết chỗ trốn.
- Luật thế giới (lộ trong phút đầu): chớp sáng → sóng địa chấn (~10 phút) → mưa thủy tinh (~30 phút) → trời cháy (~1 giờ); nước chỉ có ở lạch cá sấu và hố nước; không vũ khí

## 2 Cấu trúc (起承转合, đo từ cột "Dựng" §9 = **8:17 / 497 s**)

| Phần | Clip | Thời gian | Tỷ lệ | Chuẩn | Đánh giá |
|---|---|---|---|---|---|
| 起 Khởi | CO + EST-01 + Act 1 (16 lượt) | 0:00–1:50 | 22% | ngắn, vào việc nhanh | ĐẠT |
| 承 Thừa | Act 2 + EST-02 + Act 3 + EST-03 (41 lượt) | 1:50–5:32 | 45% | dài nhất | ĐẠT (trước 42% / 34 clip) |
| 转 Chuyển | Act 4 + MASTER (24 lượt) | 5:32–7:14 | 20% | cao trào | ĐẠT |
| 合 Hợp | Act 5 (9 lượt) | 7:14–8:17 | 13% | ngắn nhất, dư vị | ĐẠT (trước 17%, gần bằng 转) |

- Mở: cold open (MASTER 0–8s) → A1-01 cá sấu áp sát
- Inciting incident: A1-01/02 (lạch cá sấu); A1-05 đồng hồ 12h + misbelief (0:38)
- Câu hỏi 13 (đáp án đúng có ở Act 1 và bị từ chối): A1-06 (0:45) hốc khô dưới bờ lạch, Nora gạt đi vì cá sấu → payoff A4-16 (6:53) — ĐẠT
- Plot point I: A1-14 "And I wait" (1:41) — Nora **tự quyết**
- Midpoint: A2-15 "furniture now" (3:19, 40%) — chiến thắng giả. Sớm hơn mốc 50% của BS2; chấp nhận vì khung 起承转合 không dùng mốc này
- HỎNG 2: chuỗi A3-06 (3:59–4:12) vỡ mai rùa → A3-08 (4:16) Nora **tự đọc dấu chân** tìm lại đàn — ĐẠT
- Bò Đực: A3-14 (4:54) Nora qua mặt nó bằng luật Act 2 → payoff A5-05 (7:41) sừng gãy trong tro — ĐẠT
- Plot point II: chuỗi A4-03 bóng thứ hai (5:43, 69%)
- All is lost: A4-12 "Where do I go?" (6:32, 79%) — đối nghịch midpoint
- Khủng hoảng tĩnh: **A4-14** (6:43) đàn lên rừng phía bắc vs Con Non xuống lạch cá sấu → "Follow the kid." — ĐẠT
- Cao trào: A4-15 → MASTER (7:10) bùn + lá cọ, chui hốc, bàn chân Con Non — Nora tự làm bằng kỹ năng Act 2; không 祥云
- Kết: A5-09 (8:08, 10s, 0 từ) — Con Non đi vào màn tro, Nora nhổm dậy rồi ngồi lại (mặc định, chờ xác nhận), cắt đen. Lời cuối ở A5-07
- Kiểu kết: **延伸式** + **呼应式** (cold open ↔ MASTER; bờ lạch đầu ↔ cuối)
- Chuỗi thất bại → bài học: HỎNG 1 chuỗi A1-12 → đọc diềm và chân đàn · HỎNG 2 chuỗi A3-06 → đọc dấu chân (dùng lại A3-08)

## 3 Nhân vật và xung đột

| Nhân vật | Sinh lý | Xã hội | Tâm lý / premise riêng | Loại cụ thể | Thái độ với chủ đề | Quan hệ với Nora |
|---|---|---|---|---|---|---|
| Nora | 178 cm, khỏe, không vũ khí | Vlogger hiện đại, kẻ ngoài | Tò mò, dry humor; tin vào biết trước | Khán giả tự tin | biết → lắng nghe | — |
| Con Cái Già | Diềm ửng đỏ khi cảnh giác | "Radar" của đàn | Cảnh giác tuyệt đối | Trí giả (Jung) | Lắng nghe là sống | Thầy không lời |
| Bò Đực | Sừng trái gãy | Người gác ngưỡng | Lãnh thổ | Người gác cổng | — | Thử thách đầu (A1-12) → bị vượt bằng luật (A3-14) → sừng gãy trong tro (A5-05) |
| Con Non | Lăn bùn đỏ | Con non của đàn | Tò mò, bản năng | Đối tượng tình cảm + người dẫn đường | Bản năng > kiến thức | Bạn → người cứu |
| T. rex | Ruồi quanh mõm | Kẻ săn | — | Cái bóng (Jung) | — | Mối đe dọa, không đụng độ (chuỗi A2-12) |
| Borealosuchus | Hai dải lưng | — | Kiên nhẫn | Chướng ngại | — | Canh giữ nước và hốc |
| Vụ va chạm | Chớp, sóng, thủy tinh, tro | — | Vô tri | Đối thủ tuyệt đối | — | Thứ cô đến để xem |

- Vật ràng buộc: thung lũng và nước; chỉ khi ảo tưởng "khán giả" chết (A4-04) mới thoát
- Dao của đối thủ: đàn đi nhanh hơn cô chạy; nước cạn; cấm đánh T. rex; lạch đầy cá sấu
- Xiềng xích của Nora: không vũ khí; không cận chiến; không biết ngôn ngữ thú; biết trước nhưng không đổi được gì
- "Đối thủ mạnh nhất là chính mình": misbelief khán giả (A3-15 yên ổn giả)
- Thang trưởng thành: du khách → bị từ chối → quan sát → bắt chước → được dung thứ → phụ thuộc → bị tách → tự đọc dấu → vượt Bò Đực → đọc tín hiệu báo động → chọn theo Con Non → sống sót → nhân chứng
- Hệ hình ảnh: bóng (một → hai), nước (mai rùa → hố nước → lạch xám), đỏ (diềm → bùn → trời), tro phủ dần

## 4 Danh sách cảnh
- Storyboard: `script.md` §9 — **92 dòng / 91 lượt sinh** (CO cắt từ MASTER)
- 6 chuỗi 4s: A1-12a/b/c · A2-12a/b/c · A3-06a/b/c · A3-12a/b · A4-03a/b/c · A4-07a/b/c (mỗi chuỗi tính là 1 shot cho luật góc máy)
- Clip mới: A1-06 (gieo hốc) · A3-08 (tự đọc dấu, 6s) · A3-14 (vượt Bò Đực) · A4-14 (khủng hoảng tĩnh)
- Cảnh đã xóa: A5-04, A5-06, A5-09 cũ (lặp ý); Act 5 đánh số lại A5-01→A5-09
- Thứ tự sinh: §12 — 16 lượt khó nhất trước (A1-12 → A2-12 → A4-07 → MASTER → A4-03 → A3-06)

## 5 Tiến độ bản nháp
- 2026-10-12: bản 1 §1–§12 (80 lượt, 8:07)
- 2026-10-12: bản 2 — F1–F12 áp dụng, độ dài clip biến thiên, 91 lượt, 8:17. `video_prompt` JSON chưa viết; chưa có project FlowKit; chưa sinh gì

## 6 Sửa (thứ tự thực hiện)

| # | Mục tiêu | Nguồn | Trạng thái |
|---|---|---|---|
| F1 | Đồng bộ trục 12h: thẻ C1–C7 HOUR 0/1/4/6/8/11/12; header Act; "nắng lên gắt" | Sổ liên tục | xong |
| F2 | Thẻ trỏ đúng clip: C3 → A2-10; C5 → A3-06b "Vỡ mai rùa" | Sổ liên tục | xong |
| F3 | Header thời lượng/số clip theo số đo thật (8:17 / 91) | Format | xong |
| F4 | Act 5 rút 12 → 9; dồn lượt sinh sang 承 | Structure Q10 | xong (mặc định câu hỏi 1) |
| F5 | Khủng hoảng tĩnh A4-14 | McKee crisis | xong |
| F6 | Gieo hốc ở A1-06 | Structure Q13 | xong |
| F7 | Misbelief nói ra A1-05, bị đánh bại A4-04 | Cron | xong (mặc định câu hỏi 2) |
| F8 | HỎNG 2 dạy kỹ năng dùng lại: A3-08 tự đọc dấu | "mỗi thất bại dạy một điều" | xong |
| F9 | Payoff Bò Đực: A3-14 + A5-05 | Character Q9 | xong |
| F10 | Bỏ giọng giảng giải A1-03, A4-04 | memory: không bài học lịch sử | xong |
| F11 | A5-09: nhổm dậy rồi ngồi lại | Structure Q8 | xong (mặc định câu hỏi 3–4) |
| F12 | Chạy 5 bảng chẩn đoán (kết quả dưới) | sw-workflow giai đoạn 6 | xong — 2 mục để giai đoạn 5 |

### Kết quả F12 (bản 2)
- **sw-scene-craft 13**: mỗi clip/mắt xích có một hành động và một chuyển giá trị; chuỗi 4s nối bằng tư thế cuối (Rule 44); EST 0 từ là clip nhịp, không phải cảnh giải thích. Không cặp clip liền kề nào trùng góc + cỡ cảnh (trừ mắt xích trong cùng chuỗi). ĐẠT
- **sw-dialogue 14**: chỉ Nora nói (đàn câm, không cần test che tên); số từ khớp `Dur` ở 91/91 clip — ngoại lệ có chủ đích MASTER 22 từ trong 0–8s, 8–10s câm; không còn thoại giảng giải; 1 câu hỏi duy nhất ở all-is-lost A4-12 ("Where do I go?") — giữ, vì đây là điểm trũng. ĐẠT
- **sw-genre-anatomy 12** (Dude with a Problem): người thường + sự kiện sinh tử + thời hạn ĐẠT; lệch luật thể loại có chủ đích: Nora **tự chọn** vấn đề (cô đến để xem) — đây chính là chỗ mỉa mai của controlling idea. ĐẠT
- **Snyder 9 câu**: nhân vật chủ động, gần như không hỏi ✓ · không kể cốt truyện bằng lời ✓ · phản diện tối thượng (vụ va chạm) ✓ · bước ngoặt tăng tốc (Act 4 cắt bằng chuỗi 4s) ✓ · bánh xe cảm xúc: sợ, hài khô, kinh ngạc, trìu mến, mất mát ✓ · đặc điểm nhận dạng (sừng gãy, diềm đỏ, bùn đỏ, ruồi, hai dải lưng) ✓ · điểm xuất phát đủ xa (khán giả tự tin) ✓ · đủ nguyên thủy (sống sót, che chở con non) ✓
- **sw-format-adaptation A12**: cấu trúc storyboard, cột `Dur`, cờ cấm từ (phone/device/screen…: 0 lần), tỉ lệ selfie 15/92, không 3 selfie liền ĐẠT. **Chưa làm (giai đoạn 5)**: `video_prompt` JSON (Rule 55) và `lint_prompt.py`; PATCH `duration` từng scene khi tạo project

## 7 Phát hành
- Logline: xem §1
- Tiêu đề: "I Time Travelled to the Last 12 Hours of the Dinosaurs"; thoại tiếng Anh → SEO tiếng Anh (Rule 20)
- Không timestamp, không chapter cho vlog POV

## Câu hỏi mở (đã áp mặc định, chờ user xác nhận)
1. Thời lượng: giữ ~8 phút, chuyển clip từ Act 5 sang 承 → **đã áp** (8:17 / 91 lượt)
2. Premise / controlling idea ở §1 → **giữ nguyên**
3. "So I'll just stay" là một lựa chọn thật → **đã áp**
4. A5-09: Nora nhổm dậy rồi ngồi lại → **đã áp**

## Nhật ký quyết định
- 2026-10-12: Lập bible theo sw-workflow, đường vào "có bản nháp", khung 起承转合 + 结尾八法 ← user chọn
- 2026-10-12: Chốt trục giờ 12h, bỏ 18h ← thoại A1-05/A5-08 và hình học bóng A4-03 chỉ khớp với 12h
- 2026-10-12: Thời lượng thật bản 1 là 8:07 (đo cột "Dựng" §9), không phải 9:45
- 2026-10-12: **Độ dài clip biến thiên + chuỗi 4s** cho cảnh dễ lỗi; 8s/10s cho cảnh dễ không chuyển cảnh ← user. Skill + CLAUDE.md đã cập nhật
- 2026-10-12: Áp 4 mặc định cho câu hỏi mở để viết bản 2 ← user chưa trả lời; đổi được
- 2026-10-12: Bản 2 = 91 lượt sinh, 8:17

Bước tiếp: user duyệt storyboard §9 và 4 mặc định → giai đoạn 5 viết video_prompt JSON + lint → cổng Rule 29 (hỏi trước khi sinh bất cứ thứ gì).
