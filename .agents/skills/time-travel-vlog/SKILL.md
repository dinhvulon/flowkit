---
name: time-travel-vlog
description: >-
  Viết kịch bản + storyboard từng clip 8 giây + kế hoạch chuyển cảnh cho video "Time Travel Vlog" bằng AI (kiểu "I Time Traveled to Ancient China in 211 BC", "A Day in Ancient Rome", "POV you woke up in 1890 London") — vlogger hiện đại cầm điện thoại selfie, du hành về một thời kỳ lịch sử, nói chuyện với camera và dân bản địa. Tạo character bible khóa nhân vật, gói nghiên cứu lịch sử, cấu trúc kịch bản giữ chân người xem, prompt JSON cho Veo 3.1 / Google Flow (ảnh khung đầu cho Grok/Imagen nếu cần), thiết kế chuyển cảnh in-camera (whip pan, che ống kính, xuyên cửa, lật camera, match cut, time-skip) và hướng dẫn ráp CapCut + đóng gói YouTube. LUÔN dùng skill này khi user muốn làm video du hành thời gian, vlog lịch sử, POV về quá khứ, "time travel vlog", "vlog cổ đại", "xuyên không vlog", clone video kiểu trên YouTube/TikTok, hoặc hỏi cách viết kịch bản / cách chuyển cảnh cho video vlog lịch sử bằng AI — kể cả khi user chỉ đưa một link YouTube kiểu này và nói "làm giống vậy".
---

# Time Travel Vlog — Kịch bản & Chuyển cảnh

Format này ăn view vì 3 thứ: **góc nhìn người thật** (mọi thứ "quay bằng điện thoại của nhân vật" → người xem thấy mình đang ở đó), **thế giới xa lạ nhưng có thật** (sự thật lịch sử bật ra qua quan sát), và **đường cong cảm xúc** đi từ đời thường → quyền lực/nguy hiểm → di sản mà người xem hiện đại đã biết tên. Cảnh nào không phục vụ 3 thứ đó thì cắt.

Video mẫu gốc đã được phân tích khung-hình ở `references/reference-analysis.md` — **đọc file này trước khi viết**, nó là chuẩn tham chiếu về nhịp, góc máy và chuyển cảnh.

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

Gồm: mặt (tuổi, dáng mặt, mắt, tàn nhang/nốt ruồi), tóc (màu, kiểu búi, trâm), trang phục thời kỳ (kiểu áo, màu, cổ áo, thắt lưng), thiết bị (gậy selfie ngắn + điện thoại góc 0.5x), giọng (tông, tốc độ, thì thầm khi sợ). Mẫu ở `references/prompt-templates.md`.

## Bước 2 — Research pack

Điền checklist `references/era-research.md`, chọn 10–15 beat thật. Ưu tiên:
- Chi tiết thị giác **trái với hình dung phổ biến** (vd: tượng binh mã từng được sơn màu rực rỡ) — đây là khoảnh khắc "wow" người xem đem đi bình luận/chia sẻ.
- Chi tiết cho POV xúc giác: cầm, nếm, sờ, đong (hạt kê, thẻ tre, giáp, kiếm).
- Sự kiện/công trình người xem đã biết tên để làm điểm đến cuối.

Không chắc → cho nhân vật nói "I think…", "historians say…".

## Bước 3 — Cấu trúc kịch bản (theo video mẫu)

Không mở bằng cảnh du hành. **Vào thẳng thế giới từ giây 0**, khung đầu tiên là chuyển động mạnh sát ống kính (bánh xe, ngựa) rồi mở ra nhân vật giữa đám đông.

| % thời lượng | Hồi | Nội dung |
|---|---|---|
| 0–5% | Hook | Giữa chợ/đường lớn, câu đầu nói rõ đang ở đâu, năm nào, và lời hứa của video |
| 5–40% | Đời thường | Chợ, đồ ăn (có 1 cảnh ngồi ăn máy dựng trên bàn), nghề thủ công, hành chính — mỗi beat 1 sự thật |
| 40–55% | Quyền lực | Quân đội, công trường, lính — tăng quy mô và căng thẳng |
| 55–70% | Cao trào nguy hiểm | Một sự kiện lớn (vua đi qua, lễ, hành quyết được ám chỉ) → bị để ý → trốn/chạy/cưỡi ngựa thoát |
| 70–75% | Hạ nhịp | Đi nhờ xe, trò chuyện với người tốt bụng, cảnh đồng quê |
| 75–95% | Di sản | Điểm đến người xem đã biết tên, reveal dần: nhìn từ xa → xưởng làm → chạm tay → toàn cảnh khổng lồ |
| 95–100% | Kết | Máy dựng cố định, ngồi tĩnh lúc hoàng hôn, nói suy nghĩ; mồi tập sau |

Shorts: hook (1) → 2–3 beat đời thường/wow (2–4) → nguy hiểm hoặc reveal (5) → câu kết cliffhanger (6).

**Quy tắc thoại**
- Beat 15s ≈ 25–35 từ tiếng Anh; chia theo clip 8s ≈ 12–18 từ. Để 1–2s không thoại ở đầu/cuối mỗi clip cho chuyển cảnh.
- Một người nói/clip. Dân bản địa nói → nhân vật im lặng phản ứng.
- Giọng vlog thật: câu ngắn, cảm thán, thì thầm, gọi người xem. Sự thật lịch sử nói qua quan sát, không giảng bài.
- Cứ mỗi beat có một thứ mới: nơi mới, người mới, thông tin mới hoặc nguy hiểm mới.

## Bước 4 — Storyboard

Bảng tóm tắt toàn video: `# | Hồi | Beat | Loại shot | Hành động | Thoại (ai nói) | Chuyển cảnh vào | Chuyển cảnh ra | Khung cuối`

Tỉ lệ loại shot theo video mẫu (giữ gần đúng, vì chính tỉ lệ này tạo cảm giác "máy của cô"):
- ~65% selfie góc siêu rộng, cánh tay/gậy lọt khung, vừa đi vừa nói.
- ~15% POV mắt nhân vật, thấy tay cô tương tác với đồ vật/người.
- ~10% sau gáy / qua vai — chủ yếu để làm chuyển cảnh.
- ~5% máy dựng cố định (ăn uống, kết).
- ~5% toàn cảnh hoành tráng nhưng **vẫn từ vị trí cô đứng**, không drone, không b-roll điện ảnh tách rời.

Sau đó xuất prompt JSON từng clip (template `references/prompt-templates.md`). Mỗi clip bắt buộc có `transition_in` và `transition_out` viết thành câu prompt cụ thể (không chỉ ghi tên kỹ thuật), và mỗi mối nối ghi rõ cách nối trong Flow (Extend / Frames to Video / tạo riêng rồi cắt) — vì hai clip chỉ khớp nhau khi cả hai prompt cùng mô tả khung che.

## Bước 5 — Chuyển cảnh

Đọc `references/transitions.md` (gồm 3 cách nối trong Flow, luật giấu mối nối, prompt mẫu A/B cho từng kỹ thuật). Nguyên tắc từ video mẫu: **cắt thẳng, che mối nối bằng chuyển động có sẵn trong khung** — vật thể tiền cảnh lướt sát ống kính, nhân vật quay gáy đi, camera lia theo thứ chạy qua. Không dùng hiệu ứng CapCut, không title card. Jump cut khi đang đi bộ là chấp nhận được.

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
