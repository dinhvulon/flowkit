# Công thức thao tác (pro recipes)

Bảng dựng gọi công thức bằng **tên trong ngoặc vuông**, ví dụ `3.0 [Zoom-CO] 112%`. User tự làm theo công thức, không cần dẫn từng click. Phím ghi theo **mặc định CapCut Desktop** (user đã chốt, không đổi keymap). Tên menu đổi theo phiên bản; không thấy thì hỏi user đang thấy gì.

Nguồn: Quạ HD (quy trình dựng), Hướng Edit (10 mẹo CapCut), cùng các nguồn ở mục "Pro YouTuber" cuối file.

## Mục lục
1. Dựng thô chính xác
2. Zoom & chuyển động
3. Hình & lớp
4. Âm thanh
5. Xuất & kiểm duyệt
6. Chỉ dùng cho video tự quay
7. Không dùng (đã chốt)
8. Pro YouTuber: điều có nguồn

## 1. Dựng thô chính xác

| Tên | Làm gì | Khi nào |
|---|---|---|
| `[Frame]` | `Ctrl` + lăn chuột phóng timeline tối đa, `←` / `→` đi từng khung, đặt điểm cắt đúng khung | Mọi điểm cắt ở phút đầu và cao trào. Không để dính 1–2 khung thừa (nháy hình) |
| `[Nam châm]` | Bật Magnet / Snapping trên thanh công cụ timeline | Luôn bật. Clip tự hít sát, không có khe đen 1 khung |
| `[Split AI]` | Chuột phải clip dài → **Split scenes** | Chỉ còn 1 file dài (vd. bản ghép full) mà cần tách lại từng cảnh để cắt intro |

Thư mục dự án đánh số để tìm nhanh: `01_Footage` (hoặc trỏ thẳng `1080/`), `02_Audio`, `03_Graphics`, `04_Render`. Chọn Ratio (16:9 / 9:16) **trước** khi dựng.

## 2. Zoom & chuyển động

| Tên | Công thức | Khi nào |
|---|---|---|
| `[Punch]` | Split tại mốc → đoạn sau Scale 110–115%, chỉnh Position | Đổi hình tức thì giữa câu nói / hành động (mặc định của Bảng dựng) |
| `[Zoom-CO]` | Keyframe 1 ở Scale 100% → `Shift`+`→` 2 lần (~20 khung) → Scale 110–120% → chuột phải keyframe 2 → đường cong **Cubic Out** | Zoom mượt có gia tốc: phát hiện, câu chốt, "nhìn kìa" |
| `[Zoom-out-CO]` | Như trên nhưng từ Scale đang zoom về 100%, Cubic Out | Trả khung sau một `[Zoom-CO]`, hoặc "lùi lại để thấy toàn cảnh" |
| `[Push]` | Keyframe Scale 100% ở đầu clip → 105–108% ở cuối (tuyến tính) | Căng thẳng tăng dần, lời thú nhận |
| `[Gióng mắt]` | Bật **Show ruler** / guides của Player → kéo 1 đường ngang ở tầm mắt nhân vật trước khi zoom → chỉnh Position để mắt ở đoạn sau nằm trên đúng đường đó | Mọi `[Punch]` / jump cut trên mặt người: mắt người xem không phải nhảy, cú cắt "vô hình" |
| `[Ramp]` | Clip → Speed → **Curve** (hoặc Custom) → kéo đoạn giữa lên 2–4× | Chỉ **tăng tốc**: đi đường, làm việc tay chân, montage chuẩn bị. Không làm chậm clip AI có mặt/tay (CapCut phải nội suy khung, mặt và ngón tay méo). Cần slow-mo thì chỉ ≤ 1s, cảnh không người |
| `[Blur chuyển động]` | Clip có keyframe Position/Scale nhanh → bật Motion blur (Effects hoặc mục Motion blur của clip), cường độ thấp | `[Zoom-CO]` nhanh, whip-pan giả. Không dùng trên clip AI đã nhiều chuyển động sẵn |

Trần Scale ~120% trên nguồn 1080p (hình mềm, lộ lỗi AI). Không zoom cắt mất mặt, tay đang cầm vật, hay mối nguy.

## 3. Hình & lớp

| Tên | Công thức | Khi nào |
|---|---|---|
| `[Darken]` | Nhân đôi clip chính → lớp trên: sticker/khối đen, Opacity ~50%, Mask ngang phía có chữ, Fade in → nếu muốn chủ thể nổi trên lớp tối: lớp trên cùng dùng **Remove background** | Video không phải vlog: chữ/icon nhấn mạnh cần đọc rõ. Vlog FlowKit không cần (card đã có viền đen) |
| `[Bóng đổ]` | Nhân đôi logo/vật → lớp dưới Scale 105%, Adjust → Curves kéo đen hết, tăng Feather, lệch Position vài px | Logo, sticker, ảnh cắt nền trên video không phải vlog |
| `[Mask mềm]` | Mask (hình khối hoặc Pen) → tăng **Feather** để mép mềm | Ghép 2 lớp, che lỗi AI một góc khung (vd. tay méo ở rìa) bằng lớp clip khác |
| `[Màu chung]` | Adjustment → Custom adjustment phủ cả đoạn → Temp/Contrast; clip lệch chỉnh riêng ở Adjust | Đầu mỗi dự án (SKILL.md §6) |

## 4. Âm thanh

Đọc trên đồng hồ mức của CapCut (dB, đỉnh):

| Lớp | Mức | Ghi chú |
|---|---|---|
| Thoại | đỉnh −6 đến −12 dB | Không chạm vàng/đỏ. Bật Normalize loudness rồi chỉnh tay câu nào vẫn lệch |
| Nhạc nền | −15 đến −30 dB | Dưới thoại: −20 đến −24. Đoạn không thoại (intro, montage) được lên −15 đến −18 |
| SFX | nhỏ hơn thoại | Hit/boom ở CUT ĐEN là lúc duy nhất SFX được nổi |

| Tên | Công thức | Khi nào |
|---|---|---|
| `[Fade]` | Kéo chấm tròn đầu/cuối clip audio (hoặc Fade in/out 0.5–1s) | Nhạc vào/ra. **Ngoại lệ**: cú câm ở CUT ĐEN cắt cụt có chủ ý |
| `[Duck]` | 4 keyframe Volume trên nhạc: bình thường → hạ 4–6 dB → giữ → trả lại, quanh câu thoại | Câu thoại quan trọng |
| `[J-cut]` | Separate audio → kéo âm clip sau sớm ~0.5s | Nối cảnh mượt (SKILL.md §5) |
| `[Beat]` | Chọn nhạc → **Auto beat / Match beats** (Beat 1 thưa, Beat 2 dày) → dùng các chấm vàng làm điểm cắt | Intro trailer, montage, Shorts. Không dùng cho đoạn kể chuyện có thoại (cắt theo câu nói, không theo nhạc) |
| `[Giọng]` | Voice effects: Cave / Echo / Deep / Mic | Video không phải vlog: điểm nhấn hài. Vlog FlowKit: không dùng, tiếng Veo đã có vang không gian |

Sau khi xuất vẫn chạy `loudnorm` −14 LUFS (SKILL.md §5). Đồng hồ dB lo từng câu; LUFS lo cả video.

## 5. Xuất & kiểm duyệt

| Tên | Công thức |
|---|---|
| `[Xuất đoạn]` | `I` đặt điểm đầu, `O` điểm cuối → Export chỉ vùng đó. Dùng để xuất thử intro / 1 Act xem trên điện thoại trước khi xuất cả video |
| `[Loop]` | Khung cuối Short nối được về khung đầu: cùng hướng chuyển động, cùng màu, hoặc câu cuối là câu hỏi mà giây đầu trả lời → cắt cụt, không fade | Shorts. Từ 31/3/2025 YouTube đếm view cả lượt xem lại |
| `[Preset chữ]` | Làm 1 card chuẩn → **Save preset** → các card sau chọn preset (giữ đúng font, viền, vị trí) |
| Xuất | MP4, H.264, 1080p, **fps = nguồn** |

Về fps: bài Quạ HD khuyên 30 fps; với clip FlowKit **24 fps thì xuất 24**. Đổi 24 → 30 phải lặp khung, chuyển động bị giật nhịp. Xuất 30 chỉ khi footage gốc là 30. Shorts cũng chỉ cần 1080p, không cần 4K.

## 6. Chỉ dùng cho video tự quay

Clip AI không cần (mặt đã được khóa bằng ref; filter làm đẹp làm trôi khuôn mặt).

- **Làm đẹp da**: Retouch → chọn **Multiple faces** (không dùng Single face, filter sẽ nháy/mất khi người di chuyển nhanh) → Smooth 10–20% (nam), cao hơn với nữ; Even ~50%; Dark circles tùy.
- **Dáng người**: Body → chỉnh tay vùng chân, Strength vừa phải. Kiểm tra nền sau lưng không bị cong.

## 7. Không dùng (đã chốt)

- Auto captions **burn vào hình**: user chốt không burn, cả video dài lẫn Shorts. Captions vẫn tạo được để xuất `.srt` rời (`references/capcut-desktop-howto.md` §8), nhưng ẩn track trước khi Export.
- Chữ nhảy từng từ (Single line caption) với vlog FlowKit; chữ bay; transition trong tab Transitions cho vlog.
- Đổi keymap: giữ mặc định CapCut.

## 8. Pro YouTuber: điều có nguồn

Lọc từ nghiên cứu 2026-10-08. Nhãn: **[P]** nguồn gốc / người làm thật · **[YT]** YouTube chính thức · **[TH]** người hành nghề, ý kiến · **[Yếu]** blog SEO chép nhau, chỉ là điểm xuất phát. Chỉ ghi điều SKILL.md dùng tới.

| Điều | Nguồn | Áp vào bảng dựng |
|---|---|---|
| Phút đầu phải xác nhận đúng tiêu đề + thumbnail, nếu không người xem thấy "bị lừa" | [P] memo MrBeast — alexanderjarvis.com/memo-how-to-succeed-in-mrbeast-production | Giây đầu intro = đúng thứ thumbnail hứa |
| Phút 1–3 "tiến triển điên cuồng": video sinh tồn 10 phút gói nhiều ngày trong 3 phút đầu | [P] memo MrBeast | Act 1 đi nhanh, để dành thời lượng cho set-piece |
| Re-engagement ~phút 3 và ~phút 6; phút 3–6 đổi cảnh nhanh, nội dung đơn giản kích thích | [P] memo MrBeast | Đặt cảnh mạnh ở 3:00 và 6:00 (SKILL.md §2) |
| Không báo hiệu sắp hết video; kết thúc đột ngột | [P] memo MrBeast; Casey Neistat (rosetta.to/u/casey/how-to-vlog) | Khớp CUT ĐEN là hết, không đoạn end screen |
| Intro trailer 40s **không nói chuyện gì đang xảy ra** chỉ giữ 18.5% | [TH] George Blackman, review retention (georgeblackman.substack.com) | Trailer phải có tiền đề + cái giá trong ~10s đầu |
| Lợi nhất là sửa intro: +10% giữ ở 0:30 có thể là khác biệt 100k và 1M view; viết 3–4 bản intro rồi chọn | [P] Paddy Galloway (X, podcast Creator Science) | Lập 2 bản intro cho user chọn khi có cả video |
| Studio → key moment "Intro" = % còn xem ở **0:30** | [YT] support.google.com/youtube/answer/9314415 | Số kiểm tra intro sau khi đăng |
| **Chậm lại** ở khoảnh khắc nhân vật làm retention tốt hơn | [P] Zach Levet, editor của Ryan Trahan (The Editing Podcast) | Đoạn chậm = nhịp nhân vật/cảm xúc, không phải giải thích |
| Thanh tiến độ nhìn thấy được (tiền ghim tường) | [TH] Blackman về Ryan Trahan | Vlog: countdown `HOUR X` đóng vai này, không thêm đồng hồ khác |
| Dip giữa video trùng đoạn giải thích hình tĩnh, cái giá thấp; sửa bằng cái giá của truyện, không phải thêm cut | [TH] Blackman | Đoạn trượt luật 15–20s → nâng cái giá trước, cắt nhanh sau |
| Chữ phải đọc kịp; không 2 chữ/đồ họa cùng lúc; tránh stock B-roll chung chung | [P] Galloway, ghi chú cho khách | Card ~2.5s, 1 dòng một lúc |
| Zoom phải phục vụ ý, không zoom bừa | [TH] firecut.ai | `[Punch]` / `[Zoom-CO]` chỉ ở mốc có lý do |
| Jump cut chỗ chết thật, không cắt khoảng giữa các từ | [TH] ProVideo Coalition | `[Frame]` cắt sau câu, không cắt hơi thở giữa câu |
| −14 LUFS, true peak ≤ −1 dBTP; YouTube chỉ hạ video to, không nâng video nhỏ | [TH] IRPR, nhiều nguồn khớp | Lệnh loudnorm SKILL.md §5. Kiểm: Stats for nerds → content loudness |
| Nhạc dưới thoại 15–20 dB | [TH] IRPR | Bảng dùng −20 đến −24 dB, hơi thận trọng hơn; đều hợp lý |
| SFX đỉnh −18 đến −12 dB; whoosh vào sớm 10–20 ms trước hình, dài 400–500 ms | [Yếu] | Điểm xuất phát, chỉnh tai |
| Shorts: giây đầu như thumbnail; theo dõi Viewed vs Swiped away | [P] Galloway | Shorts mở giữa hành động |
| Shorts tối đa 3 phút (từ 15/10/2024); YouTube nói không có độ dài ưu tiên | [YT] TechCrunch/PetaPixel | Giữ 15–45s mặc định; "15–30s là tốt nhất" chỉ là [Yếu] |
| Mỗi Short gắn được 1 Related video tới video dài | [YT] | Đã có ở SKILL.md §7 |

Không tìm được nguồn gốc cho: "intro MrBeast ≤ 25s, đổi cấu trúc mỗi 30s", "giữ ≥ 60% ở 0:30", "im 1.5–3s trước reveal", con số màu. Không đưa vào luật.
