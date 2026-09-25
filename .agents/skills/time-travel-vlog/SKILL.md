---
name: time-travel-vlog
description: >-
  Viết kịch bản + storyboard từng clip 8 giây + kế hoạch chuyển cảnh cho video "Time Travel Vlog" bằng AI (kiểu "I Time Traveled to Ancient China in 211 BC", "A Day in Ancient Rome", "POV you woke up in 1890 London") — vlogger hiện đại cầm điện thoại selfie, du hành về một thời kỳ lịch sử, nói chuyện với camera và dân bản địa. Tạo character bible khóa nhân vật, gói nghiên cứu lịch sử, cấu trúc kịch bản giữ chân người xem, prompt JSON cho Veo 3.1 / Google Flow (ảnh khung đầu cho Grok/Imagen nếu cần), thiết kế chuyển cảnh in-camera (whip pan, che ống kính, xuyên cửa, lật camera, match cut, time-skip) và hướng dẫn ráp CapCut + đóng gói YouTube. LUÔN dùng skill này khi user muốn làm video du hành thời gian, vlog lịch sử, POV về quá khứ, "time travel vlog", "vlog cổ đại", "xuyên không vlog", clone video kiểu trên YouTube/TikTok, hoặc hỏi cách viết kịch bản / cách chuyển cảnh cho video vlog lịch sử bằng AI — kể cả khi user chỉ đưa một link YouTube kiểu này và nói "làm giống vậy".
---

# Time Travel Vlog — Kịch bản & Chuyển cảnh

Format này ăn view vì 3 thứ: **góc nhìn người thật** (mọi thứ "quay bằng điện thoại của nhân vật" → người xem thấy mình đang ở đó), **thế giới xa lạ nhưng có thật** (sự thật lịch sử bật ra qua quan sát), và **đường cong cảm xúc** đi từ đời thường → quyền lực/nguy hiểm → di sản mà người xem hiện đại đã biết tên. Cảnh nào không phục vụ 3 thứ đó thì cắt.

Video mẫu gốc đã được phân tích khung-hình ở `.agents/skills/time-travel-vlog/references/reference-analysis.md` — **đọc file này trước khi viết**, nó là chuẩn tham chiếu về nhịp, góc máy và chuyển cảnh.

## Bước 0 — Đầu vào

Tối đa 1 lượt hỏi, còn lại dùng mặc định và ghi rõ giả định:

| Thông số | Mặc định |
|---|---|
| Thời kỳ + địa điểm + năm cụ thể | bắt buộc |
| Độ dài | long-form ~10 phút ≈ 38–42 beat × ~15s; Shorts 45–60s ≈ 4–6 beat |
| Công cụ | Veo 3.1 / Google Flow. Một beat 15s = clip 8s + Extend ~7s, hoặc 2 clip 8s nối liền (khung cuối clip 1 = khung đầu clip 2) |
| Ngôn ngữ thoại | English; dân bản địa nói tiếng địa phương/cổ |
| Nhân vật | vlogger nữ ngoại quốc có ngoại hình nổi bật, **mặc trang phục đúng thời kỳ** |
| Tỉ lệ khung | 16:9 (YouTube), 9:16 (Shorts) |

Chỉ học format; không sao chép tên, ngoại hình hay lời thoại nhân vật của kênh gốc.

## Bước 1 — Character Bible

Một khối mô tả cố định, **dán nguyên văn vào mọi prompt**, kèm ảnh tham chiếu mặt (Ingredients trong Flow). Video mẫu giữ mặt nhân vật giống hệt suốt 10 phút — đây là điều kiện sống còn.

Điểm then chốt: nhân vật **mặc đồ của thời kỳ** để "trà trộn", còn yếu tố gây tò mò là ngoại hình khác biệt (tóc màu nổi, người ngoại quốc) + gậy selfie/điện thoại. Cách này cho phép cô đi khắp nơi mà không bị lộ ngay, và để dành căng thẳng cho cao trào. Chỉ dùng đồ hiện đại nếu user muốn phong cách hài "lạc loài".

Gồm: mặt (tuổi, dáng mặt, mắt, tàn nhang/nốt ruồi), tóc (màu, kiểu búi, trâm), trang phục thời kỳ (kiểu áo, màu, cổ áo, thắt lưng), thiết bị (gậy selfie ngắn + điện thoại góc 0.5x), giọng (tông, tốc độ, thì thầm khi sợ). Mẫu ở `.agents/skills/time-travel-vlog/references/prompt-templates.md`.

## Bước 2 — Research pack

Điền checklist `.agents/skills/time-travel-vlog/references/era-research.md`, chọn 10–15 beat thật. Ưu tiên:
- Chi tiết thị giác **trái với hình dung phổ biến** (vd: tượng binh mã từng được sơn màu rực rỡ) — đây là khoảnh khắc "wow" người xem đem đi bình luận/chia sẻ.
- Chi tiết cho POV xúc giác: cầm, nếm, sờ, đong (hạt kê, thẻ tre, giáp, kiếm).
- Sự kiện/công trình người xem đã biết tên để làm điểm đến cuối.

Không chắc → cho nhân vật nói "I think…", "historians say…".

## Bước 3 — Cấu trúc kịch bản (theo video mẫu)

Mở `.agents/skills/time-travel-vlog/references/reference-analysis.md` (mục "Dòng thời gian" + "Cấu trúc rút ra") **trước khi viết outline**. Video mẫu có đúng **23 beat chuẩn** chia vào **7 hồi** theo đường cong cảm xúc tăng tiến. Khi viết cho thời kỳ mới, đặt kịch bản cạnh từng beat của video mẫu dưới đây và thay bằng sự thật của thời kỳ mình — **giữ vai trò, vị trí và kỹ thuật camera, chỉ đổi nội dung sự kiện**.

Không mở bằng cảnh du hành. **Vào thẳng thế giới từ giây 0**, khung đầu tiên là chuyển động mạnh sát ống kính (bánh xe bò, thân ngựa, súc gỗ) rồi mở ra nhân vật giữa đám đông.

### 1. Bảng 7 Hồi & 3 Cú Reveal Lớn (The 3 Grand Reveals)

| % thời lượng | Hồi | Nội dung & Vai trò | Điểm nhấn camera & Reveal | Mốc video mẫu (211 BC) |
|---|---|---|---|---|
| **0–5%** | **Hồi 1: Hook** | Giữa chợ/đường lớn, câu đầu nói rõ đang ở đâu, năm nào, lời hứa video | Foreground wipe sát ống kính ở giây 0 | 0:00 bánh xe bò sát ống kính → chợ Hàm Dương |
| **5–40%** | **Hồi 2: Đời thường** | Đời sống thường nhật: hành chính, ẩm thực, nghề nghiệp, đo lường (mỗi beat 1 sự thật mới) | Ít nhất 1 beat **máy dựng trên bàn** khi ăn + 2 beat **POV xúc giác** (cầm/đong/sờ) | 0:30–4:15 đường lớn, thẻ tre, cháo kê (dựng bàn), đong hạt, xưởng nhuộm |
| **40–55%** | **Hồi 3: Quyền lực** | Quân đội, công trường, lực lượng cai trị — nâng quy mô và tạo áp lực | **Reveal #1**: Quay gáy (Look-away) reveal lực lượng quân sự/quy mô lớn | 5:05 quay gáy → đại quân tập trận, chuồng ngựa |
| **55–70%** | **Hồi 4: Cao trào nguy hiểm** | **Một** sự kiện quyền lực lớn duy nhất → bị phát hiện/để ý → rượt đuổi nghẹt thở qua ngõ → thoát hiểm | Máy rung lắc, thở dốc, chạy trốn, phóng ngựa ra cổng | 6:05–7:05 đoàn xe hoàng đế đi qua, dân quỳ rạp, lính tiến lại, chạy qua ngõ, phi ngựa thoát |
| **70–75%** | **Hồi 5: Hạ nhịp** | **Khoảng đệm hạ nhiệt**: đi nhờ xe, trò chuyện với dân quê thân thiện, cảnh đồng quê | Camera tĩnh hơn, nhịp thở chậm, J-cut ambient bình yên | 7:25 đi nhờ xe bò với bà nông dân thân thiện |
| **75–95%** | **Hồi 6: Di sản** | Kỳ quan/di sản người xem **đã biết tên** — reveal theo 4 bậc: nhìn từ xa → xưởng làm → chạm tay → toàn cảnh khổng lồ | **Reveal #2**: Nhìn công trình từ xa (7:50)<br>**Reveal #3**: Toàn cảnh kỳ quan từ trên cao (9:25) + POV chạm tay (9:05) + chi tiết "Wow" sơn màu (8:50) | 7:50–10:05 lăng mộ từ xa → lò nung đầu tượng → tượng sơn màu rực rỡ → chạm kiếm đồng → hố tượng khổng lồ |
| **95–100%** | **Hồi 7: Kết** | Ngồi tĩnh lúc hoàng hôn, chia sẻ suy nghĩ cá nhân, mồi tập sau. Không có cảnh "quay về" | **Máy dựng cố định** dưới gốc cây/bờ tường hoàng hôn | 10:22 ngồi dưới gốc cây hoàng hôn |

---

### 2. Bảng ánh xạ 23 Beat chi tiết từ Video Mẫu (Khung xương đối chiếu)

Khi lập Storyboard dài (~10 phút ≈ 38–42 clip 8s), dùng bảng 23 beat này làm mốc ánh xạ trực tiếp:

| Beat | Mốc mẫu | Loại cảnh | Ý đồ & Kỹ thuật máy quay | Thay thế cho thời kỳ mới |
|---|---|---|---|---|
| **1** | 0:00 | **Hook vào thẳng** | Bánh xe/vật thể lướt sát ống kính (Foreground wipe) → lộ nhân vật giữa phố | Vật đặc trưng thời kỳ lướt qua che khung → phố xá đông đúc |
| **2** | 0:30 | **Định hướng** | Selfie vừa đi vừa nhìn quanh, giải thích bối cảnh và năm | Nói rõ năm, sự kiện lớn sắp tới (dramatic irony) |
| **3** | 0:45 | **Quy mô công trình** | Selfie lia nhẹ sang công trường/lao dịch, thấy sự khắc nghiệt | Công trình xây dựng lớn của thời kỳ |
| **4** | 1:00 | **Nguy hiểm nhẹ** | Súc gỗ khiêng ngang che khung (Wipe) → lính tuần tra đi qua | Chuyển cảnh bằng vật cản lướt qua → lính canh thời đại |
| **5** | 1:15 | **Đời sống dân sinh** | POV nhìn mặt đường, phương tiện đi lại, người dân địa phương | Đời sống bình dân, đường phố lầy lội/đá cuội |
| **6** | 1:40 | **Sự thật hành chính** | POV mắt nhân vật nhìn giấy tờ/chữ viết/thẻ tre/con dấu | Văn thư, luật pháp hoặc chữ viết cổ thời đó |
| **7** | 2:05 | **Chợ phiên & đời thường** | Selfie đi giữa hàng quán, tương tác hài hước với động vật/rau củ | Chợ phiên thời kỳ, con vật nuôi, rau quả đặc trưng |
| **8** | 2:35 | **Ẩm thực (Máy dựng bàn)** | **Điện thoại dựng cố định trên bàn**, cô ngồi ăn món địa phương | Món ăn dân dã thời đó, cách ăn bằng tay/thìa/đũa cổ |
| **9** | 3:05 | **Chuyển tiếp vận tải** | Xe chở lương thực / hàng hóa lướt qua chuyển bối cảnh | Phương tiện vận chuyển hàng hóa thời kỳ |
| **10** | 3:25 | **POV xúc giác: Đo lường** | Tay nhân vật cầm/đong nông sản hoặc sờ tiền tệ tiêu chuẩn | Sự thật về tiền xu, cân đo đong đếm |
| **11** | 4:15 | **Nghề thủ công** | Xưởng nhuộm, rèn, dệt vải — màu sắc và khói bụi thực tế | Nghề thủ công nổi tiếng của thời kỳ |
| **12** | 5:05 | **Reveal #1: Quyền lực** | **Quay gáy (Look-away)**: nhân vật quay đi → lộ ra đại quân duyệt binh | Quay gáy reveal lực lượng quân đội hoặc lính gác hoàng gia |
| **13** | 5:37 | **Chuẩn bị căng thẳng** | Chuồng ngựa, chuẩn bị vũ khí, dân bắt đầu dạt ra hai bên | Không khí căng thẳng, lính chỉnh đốn hàng ngũ |
| **14** | 6:05 | **Cao trào: Sự kiện lớn** | Đoàn xe vua/lãnh tụ đi qua, dân quỳ rạp, nhân vật nấp sau cột | Nhân vật quyền lực tối cao xuất hiện, vlogger bị nhìn chằm chằm |
| **15** | 6:42 | **Rượt đuổi** | Lính tiến lại → nhân vật quay lưng chạy thục mạng qua ngõ nhỏ | Bị nghi ngờ là gián điệp/kẻ lạ → chạy trốn qua ngõ |
| **16** | 7:05 | **Thoát hiểm** | Nhảy lên ngựa/xe phóng vụt ra khỏi cổng thành | Thoát khỏi vùng nguy hiểm ra ngoại ô |
| **17** | 7:25 | **Hạ nhịp (Decompression)** | **Đi nhờ xe bò** với nông dân thân thiện, nhịp thở chậm lại | Đi nhờ xe rơm/thuyền tam bản, trò chuyện với dân quê |
| **18** | 7:50 | **Reveal #2: Di sản từ xa** | Từ trên xe nhìn ra xa: thấy bóng dáng công trình kỳ quan | Thấy kỳ quan/di sản nổi tiếng từ đằng xa |
| **19** | 7:55 | **Quy trình chế tác** | Đến xưởng chế tác/lò gốm/nơi đẽo đá tạo nên kỳ quan | Hậu trường xây dựng kỳ quan (xưởng đá, lò nung) |
| **20** | 8:50 | **Chi tiết "Wow" trái ngược** | Điểm nhấn lịch sử ít ai biết (vd: tượng từng sơn màu rực rỡ) | Chi tiết thật gây sửng sốt trái với phim ảnh |
| **21** | 9:05 | **POV xúc giác: Di sản** | Tay nhân vật chạm vào hiện vật (giáp đồng, thanh kiếm, mặt đá) | Tay chạm trực tiếp vào hiện vật bảo vật thời đó |
| **22** | 9:25 | **Reveal #3: Đỉnh toàn cảnh** | Đứng trên gờ cao nhìn xuống toàn bộ kỳ quan khổng lồ | Toàn cảnh kỳ quan tráng lệ (vẫn từ góc nhìn cô đứng) |
| **23** | 10:22 | **Kết trầm** | **Máy dựng cố định** lúc hoàng hôn, ngồi tĩnh suy ngẫm, mồi tập sau | Ngồi tĩnh dưới bóng hoàng hôn suy ngẫm, hẹn tập sau |

---

### 3. Quy tắc cốt lõi khi thiết kế Outline

1. **Thứ tự là cố định**: Đời thường → Quyền lực → Cao trào nguy hiểm → Hạ nhịp → Di sản → Kết. Điểm đến nổi tiếng nhất **bắt buộc nằm sau cao trào nguy hiểm** — dồn sự kinh ngạc lớn nhất vào 25% cuối để giữ chân người xem đến giây cuối.
2. **Quy tắc 3 cú Reveal lớn (Reveal Triad)**:
   - *Reveal #1 (~45%)*: Sức mạnh/quân đội, thực hiện bằng cú quay gáy (Look-away).
   - *Reveal #2 (~75%)*: Di sản từ xa, nhìn thấy khi đang ngồi trên xe đi nhờ.
   - *Reveal #3 (~90%)*: Toàn cảnh di sản đỉnh cao, đứng trên cao nhìn xuống + chạm tay xúc giác.
3. **Hai cảnh máy dựng cố định (Phone Prop-up)**:
   - Beat ăn uống (~25%): Điện thoại dựng trên bàn ăn.
   - Beat kết (~98%): Điện thoại dựng đối diện nhân vật lúc hoàng hôn.
4. **Khoảng hạ nhiệt sau thoát hiểm (70–75%)**: Tuyệt đối không nhảy thẳng từ rượt đuổi sang kỳ quan. Phải có cảnh đi nhờ xe, trò chuyện với dân bản địa hiền hòa để nhịp phim lắng xuống.

**Shorts (4–6 beat × 8s)** — nén cùng đường cong, không đảo thứ tự:

| Beat (6 beat) | Hồi | Bắt buộc | Nếu chỉ 4 beat |
|---|---|---|---|
| 1 | Hook | Chuyển động sát ống kính ở giây 0, câu nói rõ nơi + năm | 1 |
| 2 | Đời thường | POV xúc giác, 1 sự thật trái hình dung | 2 |
| 3 | Quyền lực / quy mô | Công trình hoặc lực lượng lớn, reveal bằng quay gáy/lia | gộp vào 2 hoặc bỏ |
| 4 | Cao trào nguy hiểm | Sự kiện lớn → bị để ý → thoát (chỉ 1 người nói) | 3 (gộp nguy hiểm + thoát) |
| 5 | Di sản | Công trình người xem đã biết tên, selfie flip / reveal toàn cảnh | gộp vào 4 |
| 6 | Kết | Máy dựng cố định, hoàng hôn, câu dramatic irony hoặc mồi tập sau | 4 |

**Tự kiểm tra outline trước khi sang Bước 4** (so với `.agents/skills/time-travel-vlog/references/reference-analysis.md`):
- [ ] Giây 0 là vật thể chuyển động sát ống kính (Wipe), không có cảnh cỗ máy thời gian hay du hành.
- [ ] Đúng **một** cao trào nguy hiểm, nằm ở ~55–70% (Shorts: beat 4 / 6), có rượt đuổi thoát hiểm.
- [ ] Có khoảng đệm **hạ nhịp** đi nhờ xe / trò chuyện nhẹ nhàng (~70–75%) ngay sau khi thoát hiểm.
- [ ] Đủ **3 cú Reveal lớn**: #1 Quân sự/Quy mô (quay gáy), #2 Di sản từ xa, #3 Toàn cảnh di sản đỉnh cao.
- [ ] Có ít nhất 1 beat máy dựng cố định trên bàn ăn uống (~25%) và 1 beat kết máy dựng cố định lúc hoàng hôn.
- [ ] Có ít nhất 1 beat POV xúc giác (tay sờ/đong/nếm) và 1 chi tiết "wow" trái hình dung phổ biến.
- [ ] Công trình nổi tiếng nhất nằm **sau** cao trào; di sản reveal theo 4 bậc (xa → xưởng → chạm → toàn cảnh).
- [ ] Mỗi beat có một thứ mới (nơi mới, người mới, thông tin mới hoặc nguy hiểm mới).

**Quy tắc thoại** (kinh nghiệm thực chiến tối ưu cho Veo / AI Video):
- Beat 15s ≈ 25–35 từ tiếng Anh; chia theo clip 8s ≈ **12–18 từ**. Để 1–2s không thoại ở đầu/cuối mỗi clip cho chuyển cảnh.
- Một người nói/clip. Dân bản địa nói → nhân vật im lặng phản ứng (mắt mở to, môi mím).
- Giọng vlog thật: câu ngắn, cảm thán, thì thầm, gọi người xem ("you guys...", "okay don't freak out..."). Sự thật lịch sử nói qua quan sát, không giảng bài sách vở.

## Bước 4 — Storyboard

Bảng tóm tắt toàn video: `# | Hồi | Beat | Loại shot | Hành động | Thoại (ai nói) | Chuyển cảnh vào | Chuyển cảnh ra | Khung cuối`

Tỉ lệ loại shot theo video mẫu (giữ gần đúng, vì chính tỉ lệ này tạo cảm giác "máy của cô"):
- ~65% selfie góc siêu rộng, cánh tay/gậy lọt khung, vừa đi vừa nói.
- ~15% POV mắt nhân vật, thấy tay cô tương tác với đồ vật/người.
- ~10% sau gáy / qua vai — chủ yếu để làm chuyển cảnh.
- ~5% máy dựng cố định (ăn uống, kết).
- ~5% toàn cảnh hoành tráng nhưng **vẫn từ vị trí cô đứng**, không drone, không b-roll điện ảnh tách rời.

Sau đó xuất prompt JSON từng clip (template `.agents/skills/time-travel-vlog/references/prompt-templates.md`). Mỗi clip bắt buộc có `transition_in` và `transition_out` viết thành câu prompt cụ thể (không chỉ ghi tên kỹ thuật), và mỗi mối nối ghi rõ cách nối trong Flow (Extend / Frames to Video / tạo riêng rồi cắt) — vì hai clip chỉ khớp nhau khi cả hai prompt cùng mô tả khung che.

## Bước 5 — Chuyển cảnh

Đọc `.agents/skills/time-travel-vlog/references/transitions.md` (gồm 3 cách nối trong Flow, luật giấu mối nối, prompt mẫu A/B cho từng kỹ thuật). Nguyên tắc từ video mẫu: **cắt thẳng, che mối nối bằng chuyển động có sẵn trong khung** — vật thể tiền cảnh lướt sát ống kính, nhân vật quay gáy đi, camera lia theo thứ chạy qua. Không dùng hiệu ứng CapCut, không title card. Jump cut khi đang đi bộ là chấp nhận được.

## Bước 6 — Ráp CapCut & đóng gói
- Cắt thẳng theo khung che; nhạc nền + ambient trải liên tục suốt video (video mẫu gần như không có khoảng lặng), hạ nhạc ở cảnh nguy hiểm và cảnh kết.
- SFX nhẹ khi vật thể lướt qua ống kính; J-cut ambient cảnh sau vào sớm ~0.5s.
- Phụ đề tùy chọn (video mẫu không có chữ trên màn hình).
- Grade ấm, hoàng hôn ở cuối; thêm grain nhẹ để đồng nhất các clip.
- YouTube: 3 tiêu đề dạng "I Time Traveled to ___ in ___! (Vlog)", thumbnail (mặt nhân vật sốc + công trình/sự kiện nổi tiếng nhất của thời kỳ), mô tả có timestamp theo beat, bật nhãn "Altered or synthetic content".

## Định dạng output
1. Giả định (3–5 dòng)
2. Character Bible
3. Research pack (bảng beat)
4. Outline theo 7 hồi + thời lượng
5. Bảng storyboard toàn bộ beat
6. Prompt JSON từng clip — long-form xuất theo từng hồi, hỏi user trước khi sang hồi tiếp
7. Ghi chú CapCut + gói YouTube

Long-form → ghi file `.md`; Shorts → trả trực tiếp trong chat.
