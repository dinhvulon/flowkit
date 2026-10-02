# fk-time-travel-vlog — Time Travel Vlog Orchestrator (Mọi Thời Kỳ, Mọi Địa Điểm)

Tạo kịch bản và dự án video vlog **DU HÀNH THỜI GIAN / POV VLOG LỊCH SỬ** kiểu *"I Time Traveled to Ancient China in 211 BC"*, *"A Day in Ancient Rome"*, *"POV You Woke Up in 1890 London"* — vlogger hiện đại cầm điện thoại/gậy selfie, rơi vào một thời kỳ lịch sử cụ thể, vừa đi vừa nói chuyện với camera và dân bản địa. Skill này dùng cho **mọi thời kỳ/địa điểm** (La Mã cổ đại, Trung Hoa Tần/Hán, London thời Victoria, Ai Cập cổ đại, Ba Tư, Viking, Nhật Bản Heian/Edo...).

Dùng skill này cả khi user chỉ đưa một link YouTube kiểu này và nói "làm giống vậy", hoặc hỏi cách viết kịch bản / cách chuyển cảnh cho vlog lịch sử, "xuyên không vlog", "vlog cổ đại", "POV về quá khứ".

Format này ăn view vì 3 thứ: **góc nhìn người thật** (mọi thứ "quay bằng điện thoại của nhân vật" → người xem thấy mình đang ở đó), **thế giới xa lạ nhưng có thật** (sự thật lịch sử bật ra qua quan sát, không giảng bài), và **đường cong cảm xúc** đi từ đời thường → quyền lực/nguy hiểm → di sản mà người xem hiện đại đã biết tên. Cảnh nào không phục vụ 3 thứ đó thì cắt.

---

## 📚 TÀI LIỆU THAM CHIẾU — BẮT BUỘC ĐỌC TRƯỚC KHI VIẾT

Mọi quy tắc trong skill này được rút ra từ 5 file ở `.agents/skills/time-travel-vlog/references/`. **Đọc cả 5 file trước khi viết bất kỳ dòng kịch bản/prompt nào** — chúng là nguồn chuẩn cho độ chân thực; skill này chỉ tóm tắt và ánh xạ sang FlowKit.

| File | Đọc ở bước | Dùng để |
|---|---|---|
| `reference-analysis.md` | Trước tiên, trước mọi bước | Chuẩn nhịp (~15s/beat), tỉ lệ góc máy, dòng thời gian beat, cách giấu mối nối quan sát được từ video mẫu thật |
| `era-research.md` | Mục 4 — Research Pack | Checklist nghiên cứu thời kỳ + bảng beat output |
| `prompt-templates.md` | Mục 2 + mục 10 | Mẫu `CHARACTER_LOCK`, Clip JSON, mẫu shot (dân bản địa nói, POV, máy dựng, toàn cảnh) |
| `transitions.md` | Mục 7 | 3 cách nối clip, luật giấu mối nối, prompt A/B cho từng kỹ thuật, bảng chọn nhanh |
| `voice-bible.md` | Mục 2 + mục 5 (trước khi viết bất kỳ dòng thoại nào) | `VOICE_LOCK` khóa tính cách (Nora: nhà khảo cổ, chuyên gia sinh tồn), mật độ thoại, chửi thề bị bíp, 3 khuôn beat truyền kiến thức, checklist chống giọng AI, mẹo sinh tồn sai cần tránh |

**Khi các nguồn mâu thuẫn**, ưu tiên theo thứ tự: `reference-analysis.md` (quan sát từ video thật) → skill này → phần "Kỹ thuật bổ sung" của `transitions.md`. Ví dụ: `transitions.md` gợi ý title "3 HOURS LATER" cho time-skip, nhưng video mẫu không có chữ trên màn hình → **không dùng title** (mục 8).

---

## 🎭 VAI TRÒ & MỤC TIÊU

Skill này kết hợp:
1. **Khung kịch bản 7 hồi du hành thời gian** — hook giữa chợ/đường lớn → đời thường → quyền lực → cao trào nguy hiểm → hạ nhịp → di sản → kết, với tỉ lệ % thời lượng cố định (mục 5).
2. **Character Bible khóa nhân vật** — khối `CHARACTER_LOCK` cố định dán vào mọi entity/scene để giữ mặt, tóc, trang phục nhân vật giống hệt suốt video (mục 2).
3. **Research Pack** — checklist sự thật lịch sử theo thời kỳ, tránh bịa sự kiện/vật dụng sai niên đại (mục 4).
4. **Storyboard + Clip JSON từng clip 8s** — mỗi clip có `transition_in`/`transition_out` viết thành câu prompt cụ thể và cách nối được ghi rõ (mục 6, 7, 10).
5. **Chuẩn chân thực "máy của nhân vật"** — ngôn ngữ hình ảnh điện thoại, ràng buộc viết thành câu khẳng định, hậu kỳ đồng nhất (mục 9, 11, Bước 5).

Skill này **gọi các skill FlowKit khác** để tự động fact-check và triển khai:
- `/fk-research` — bắt buộc chạy trước khi viết bất kỳ prompt nào, để khóa chính xác niên đại, địa danh, trang phục, ẩm thực.
- `/fk-add-material` — khóa chất liệu ảnh (`realistic` hoặc material điện thoại tùy chỉnh, mục 9).
- `/fk-camera-guide` — chuẩn góc máy selfie/POV cho Veo 3 / Omni Flash.
- `/fk-gen-music` — nhạc nền/ambient trải liên tục (mục 8).
- `/fk-upload-image` — đưa khung cuối clip A lên làm khung đầu clip B (nối F2V, mục 7).
- `/fk-create-project`, `/fk-switch-project`, `/fk-upload-ref`, `/fk-gen-refs`, `/fk-gen-images`, `/fk-review-board`, `/fk-pipeline`, `/fk-review-video`, `/fk-concat`, `/fk-youtube-seo`, `/fk-thumbnail` — triển khai và chạy pipeline (phần 🛠️).

Kết quả đầu ra tương thích 100% với pipeline của FlowKit:
- **Project API**: `POST /api/projects` (với `material`, entities nhân vật + bối cảnh + đạo cụ từ Character Bible)
- **Scene API**: `POST /api/scenes` — mỗi **beat** (~15s) = 2 scene FlowKit 8s (long-form) hoặc 1 scene (Shorts); `prompt` cho Frame 0 + `video_prompt` chia sub-clip `0-3s`, `3-6s`, `6-8s`
- **TTS Engine**: OmniVoice (`POST /api/videos/{vid}/narrate`) chỉ khi dùng lồng tiếng thay vì khẩu hình native — mặc định của format này là **thoại native trong video** (vlogger nói với camera)

---

## 📐 NGUYÊN TẮC CỐT LÕI (BẮT BUỘC TUÂN THỦ)

### 0. Đầu vào — tối đa 1 lượt hỏi, còn lại dùng mặc định và ghi rõ giả định

| Thông số | Mặc định |
|---|---|
| Thời kỳ + địa điểm + năm cụ thể | **bắt buộc** — cấm chung chung ("La Mã cổ đại"), phải ghi rõ ví dụ `Rome, 79 AD` / `Xianyang, Qin dynasty China, 211 BC` |
| Độ dài | Long-form ~10 phút ≈ **38–42 beat × ~15s** (mỗi beat = 2 scene 8s ≈ 76–84 scene); Shorts 45–60s ≈ **4–6 beat**, mỗi beat = 1 scene 8s |
| Công cụ | Veo 3.1 qua pipeline FlowKit (i2v từ ảnh Frame 0). Mối nối liền trong beat: F2V (khung cuối A = khung đầu B) hoặc Omni Flash first+last — mục 7 |
| Ngôn ngữ thoại | English mặc định; dân bản địa nói tiếng địa phương/cổ (phiên âm đơn giản) hoặc English có accent nếu muốn người xem hiểu |
| Nhân vật | Vlogger nữ ngoại quốc ngoại hình nổi bật, **mặc trang phục đúng thời kỳ ngay từ clip đầu tiên** — không có cảnh "vừa rơi xuống" mặc đồ hiện đại (mục 2) |
| Tỉ lệ khung | HORIZONTAL 16:9 (YouTube long-form) hoặc VERTICAL 9:16 (Shorts) |
| Material | `realistic` hoặc material điện thoại tùy chỉnh `phone_vlog` (khuyến nghị, mục 9) |

Chỉ học format; không sao chép tên, ngoại hình hay lời thoại nhân vật của kênh gốc mà user đưa làm ví dụ.

### 1. Khung "Time Capsule" — Phải chính xác tới năm
- **CẤM** dùng từ chung chung ("thời phong kiến", "cổ đại") — AI sẽ trộn lẫn nhiều thời kỳ/trang phục du lịch hiện đại.
- **BẮT BUỘC** chỉ định rõ thành phố + năm trong mọi `description`/`prompt`: `Rome, 79 AD` / `Xianyang, Qin dynasty China, 211 BC` / `London, 1890`.
- Chi tiết lịch sử phải qua `/fk-research` trước — vật dụng/món ăn xuất hiện sai niên đại (vd: ớt, ngô, khoai tây ở châu Á/châu Âu trước thế kỷ 16) là lỗi thường gặp nhất.

### 1b. Chiến Lược Săn "Trend Đang Lên" (Rising Trends) Cho Kênh Mới
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
   *(Khớp với Title Option 2: Format 24 Giờ Sinh Tồn)*

### 2. Character Bible — khóa nhân vật xuyên suốt
Một khối `CHARACTER_LOCK` cố định, **dán nguyên văn vào entity `description` và KHÔNG sửa giữa các clip**, kèm ảnh tham chiếu mặt (`/fk-upload-ref` nếu dùng mặt thật, hoặc `/fk-gen-refs` sinh ref AI rồi khóa lại). Video mẫu giữ mặt nhân vật giống hệt suốt 10 phút — đây là điều kiện sống còn của độ chân thực.

Gồm: mặt (tuổi, dáng mặt, mắt, tàn nhang/nốt ruồi), tóc (màu, kiểu búi, trâm/phụ kiện), trang phục thời kỳ (kiểu áo, màu, cổ áo, thắt lưng — **KHÔNG nhuộm màu/vải công nghiệp hiện đại**), thiết bị (gậy selfie ngắn + điện thoại góc siêu rộng 0.5x, cánh tay lọt mép khung), giọng (`voice_description`: tông, tốc độ, thì thầm khi sợ).

#### Quy tắc Cốt Lõi Về Voice, Omni Flash Ingredients R2V (BẮT BUỘC):
1. **CHỈ DÙNG OMNI FLASH INGREDIENTS (`reference_to_video` / `abra_r2v`) — KHÔNG DÙNG START FRAME I2V**:
   - Khi tạo video nhân vật/vlog, **TUYỆT ĐỐI KHÔNG sinh ảnh Start Frame (`GENERATE_IMAGE`) để chạy Image-to-Video (`i2v`)**. Cách làm cũ bằng Start Frame làm chuyển động bị cứng, dễ giật, méo người và biến dạng khuôn mặt khi di chuyển.
   - **BẮT BUỘC chỉ sử dụng Omni Flash Ingredients (`GENERATE_VIDEO_REFS` / `omni_flash_models.reference_to_video` / `abra_r2v_<duration>s` qua RPC `MZZa6b`)**:
     - Đính kèm trực tiếp các thành phần tham chiếu (Ingredients): Nhân vật (`Mia`), Trang phục (`Mia Outfit`), và Bối cảnh/Địa điểm (`reference_media_ids` / `imageInputs`).
     - Model `abra_r2v` tự động tổng hợp chuyển động video mượt mà trực tiếp từ các thành phần tham chiếu và `video_prompt`, tích hợp khẩu hình native với voice profile **Laomedeia** (Slot 7).
     - Không chạy quy trình `GENERATE_IMAGE` cho từng cảnh; sau khi các entity có `media_id`, gửi thẳng yêu cầu `GENERATE_VIDEO_REFS`.
2. **Voice Laomedeia**: Với nhân vật vlogger nữ, khai báo `voice_description` theo chuẩn **Laomedeia** (Google Gemini-TTS: *"Laomedeia — upbeat, mid-high pitched, energetic expressive conversational female voice, fast confident vlog delivery with dry humor, rises into real cracking screams when in danger, drops to a fast whisper when hiding"*). Đính thoại dạng `Mia says: "..."` trong sub-clips `0-3s / 3-6s / 6-10s` để `abra_r2v` tự sinh khẩu hình và giọng nói bản địa tự nhiên.
2b. **Kỹ Thuật Vlog Phiên Dịch (Translator POV — Tương Tác Bản Địa Chuẩn)**:
   - **Rào cản AI & Lịch sử:** Model AI chỉ nhận 1 giọng nói (Slot 7 Laomedeia). Nếu gán thoại tiếng Anh cho nhân vật phụ (thợ săn, nông dân, thương nhân), AI sẽ lấy giọng Laomedeia phát ra từ miệng họ gây méo tiếng và vỡ khẩu hình. Hơn nữa, việc người tiền sử/cổ đại nói tiếng Anh lưu loát là phản khoa học và mất chất tài liệu.
   - **Quy tắc bắt buộc:**
     - Người bản địa giao tiếp bằng **cử chỉ tay, biểu cảm sống động, hiệu lệnh săn bắn hoặc cổ ngữ tự nhiên** trong prompt hành động. TUYỆT ĐỐI KHÔNG ghi thoại tiếng Anh cho nhân vật phụ.
     - Vlogger thuật lại trực tiếp cho người xem bằng giọng Vlogger (`Nora says: "He just warned me that...", "She says this is..."`).
     - Triển khai chuẩn (Single-Perspective Vlog Purity): Hoặc **100% Selfie Qua Vai (Over-the-Shoulder)** (Vlogger chiếm 1/3 tiền cảnh, bản địa ở 2/3 hậu cảnh, tương tác qua ánh mắt và quay đầu, KHÔNG xoay máy; xem Bài học 44 & Rule 42). Hoặc **Cặp Shot Kép** (Shot A: 100% POV Cam sau ➔ Cut sang Shot B: 100% Selfie Cam trước). TUYỆT ĐỐI CẤM cú lia máy 180° giữa cam trước và cam sau trong 1 shot liên tục.
3. **Review 720p trước ➔ User duyệt ➔ Upscale 1080p & Xóa Logo sau**: Tải từng clip 720p về `${OUTDIR}/scenes/scene_{idx}_{sid}.mp4`. **Chưa cần xóa logo ở bước này** để tránh lãng phí thời gian encode. Trích xuất frames từ video 720p, chạy AI Review Scorecard và đưa lên Review Board (`http://localhost:8200`) cho người dùng review từng clip. **CHỈ KHI NGƯỜI DÙNG DUYỆT THÔNG QUA**: Gửi lệnh Upscale 1080p (`p0UkFb` / `veo_3_1_upsampler_1080p`), tải bản 1080p về folder riêng `${OUTDIR}/1080/scene_{idx}_{sid}_1080p.mp4`, rồi mới chạy `remove_watermark_video` trực tiếp trên bản 1080p (`${OUTDIR}/1080/scene_{idx}_{sid}_1080p_clean.mp4`) để đưa vào Concat cuối cùng.

Mẫu (từ `prompt-templates.md` — thay giá trị, tên nhân vật do bạn đặt, rồi đóng băng):
```
CHARACTER_LOCK:
Nora, a 26-year-old Western woman with a heart-shaped face, hazel-green eyes, dense freckles across nose and cheeks,
bright copper-red hair in a high bun held by a dark wooden hairpin, a few loose strands at the temples,
wearing an era-appropriate [dark indigo cross-collar hemp robe with a white inner collar and a plain dark sash],
holding a short black selfie stick with a smartphone on ultra-wide 0.5x lens, her arm visible at the frame edge.
Voice: Laomedeia — upbeat, mid-high pitched, energetic expressive conversational female voice, fast confident vlog delivery with dry humor, rises into real cracking screams when in danger, drops to a fast whisper when hiding.
```
Tên trong `CHARACTER_LOCK`, tên entity và tên người nói trong `video_prompt` phải **trùng nhau tuyệt đối** (mẫu gốc có chỗ lệch Nora/Mia — đừng lặp lại lỗi đó).

**`VOICE_LOCK` — khóa tính cách đi kèm `CHARACTER_LOCK` (góp ý của user, 2026-10-01):** `CHARACTER_LOCK` chỉ khóa ngoại hình và chất giọng; cách nói (vlogger là ai, nói nhanh hay chậm, đùa kiểu gì, sợ gì, không bao giờ nói gì) khóa bằng khối `VOICE_LOCK` theo `voice-bible.md` mục 1. Ghi `VOICE_LOCK` vào `script.md` ngay dưới `CHARACTER_LOCK` và không sửa giữa các clip. `VOICE_LOCK` **không** dán vào entity `description` hay `video_prompt`; nó là luật để viết thoại, còn thứ đi vào prompt là câu thoại và tag cách diễn đạt.

**Trang phục theo ảnh ref — mặc định gộp vào ảnh nhân vật (góp ý của user, 2026-10-01; thay bài học S31):** với R2V, quần áo của vlogger **lấy từ ảnh ref**, không lấy từ chữ trong `CHARACTER_LOCK`. Mặc định dùng **một ảnh sheet 16:9 duy nhất** cho vlogger: mặt chính diện rõ nét | góc 3/4 | bên phải là toàn thân đang mặc đủ trang phục của thời kỳ. Một ảnh vừa khóa mặt vừa khóa trang phục, và tiết kiệm 1 slot ref (mỗi clip tối đa 3).
- Chỉ khi trang phục vẫn bị trôi giữa các clip mới tách thêm entity `<Vlogger> Outfit` (`visual_asset`, ảnh toàn thân trang phục sạch nền) và đính vào `character_names` của các clip bị lỗi.

### 3. Strict Ethnicity Lock & Period Lock
- Mọi người xuất hiện trong khung (người đi đường, người bán hàng, lính canh, quý tộc) phải **đúng chủng tộc bản địa của thời kỳ/địa điểm đó** — nghiên cứu qua `/fk-research` trước khi viết `description`.
- **PERIOD LOCK**: cấm rập khuôn điện ảnh sai (vd: mũ sừng Viking), cấm vật liệu/kiến trúc/trang phục lệch niên đại. Ánh sáng dùng mặt trời/đuốc/đèn dầu, tránh nguồn sáng không đúng thời đại.
- Không làm nhục/biếm họa dân tộc, tôn giáo. Hình phạt/chiến tranh chỉ ám chỉ, không mô tả máu me — vừa đúng lịch sử vừa tránh bị Veo từ chối (`UNSAFE_GENERATION`) và YouTube hạn chế quảng cáo. Xem bảng từ ngữ an toàn trong `fk-create-project.md`.

### 4. Research Pack — điền đủ checklist `era-research.md` trước khi viết scene
Chạy `/fk-research`, rồi điền **toàn bộ** checklist ở `era-research.md` (bối cảnh, thị giác, đời sống, cấm kỵ), đánh dấu độ chắc chắn ✅ chắc chắn · ⚠️ tranh cãi/phỏng đoán. Chọn ra **10–15 beat sự thật thật**. Ưu tiên:
- Chi tiết thị giác **trái với hình dung phổ biến** (vd: tượng binh mã từng được sơn màu rực rỡ) — khoảnh khắc "wow" người xem đem đi bình luận/chia sẻ.
- Chi tiết cho POV xúc giác: cầm, nếm, sờ, đong (hạt kê, thẻ tre, giáp, kiếm, tiền xu).
- **Dramatic irony**: sự kiện lớn đang/sắp xảy ra mà vlogger biết còn dân chưa biết — gia vị cho lời thoại thì thầm với người xem.
- Chợ & tiền tệ, đo lường, đồ ăn thường ngày, luật lệ & hình phạt (beat căng nhất), giấy tờ đi đường/giờ giới nghiêm, nghề nghiệp/lao dịch, tín ngưỡng, vệ sinh/nước uống (beat hài hiệu quả), phép tắc với người trên, vị trí phụ nữ trong xã hội (tạo xung đột nếu vlogger là nữ).
- Sự kiện/công trình người xem đã biết tên để làm điểm đến cuối (Colosseum, Vạn Lý Trường Thành, Big Ben...).

Output bắt buộc là bảng beat:

| # | Beat | Sự thật | Độ chắc | Cơ hội hình ảnh | Cơ hội xung đột/hài |
|---|---|---|---|---|---|

Beat ⚠️ → cho nhân vật nói dạng suy đoán: "I think...", "historians say...", "apparently...".

### 5. Cấu trúc kịch bản 7 hồi theo % thời lượng & 23 Beat Ánh Xạ

**Không mở bằng cảnh du hành.** Vào thẳng thế giới từ giây 0 — khung đầu là chuyển động mạnh sát ống kính (bánh xe, ngựa, súc gỗ) rồi mở ra nhân vật giữa đám đông.

#### 5a. Bảng 7 Hồi & 3 Cú Reveal Lớn (The 3 Grand Reveals)

| % thời lượng | Hồi | Nội dung & Vai trò | Điểm nhấn camera & Reveal | Mốc video mẫu (211 BC) |
|---|---|---|---|---|
| **0–5%** | **Hồi 1: Hook** | Giữa chợ/đường lớn, câu đầu nói rõ đang ở đâu, năm nào, lời hứa video | Foreground wipe sát ống kính ở giây 0 | 0:00 bánh xe bò sát ống kính → chợ Hàm Dương |
| **5–40%** | **Hồi 2: Đời thường** | Đời sống thường nhật: hành chính, ẩm thực, nghề nghiệp, đo lường (mỗi beat 1 sự thật mới) | Ít nhất 1 beat **máy dựng trên bàn** khi ăn + 2 beat **POV xúc giác** (cầm/đong/sờ) | 0:30–4:15 đường lớn, thẻ tre, cháo kê (dựng bàn), đong hạt, xưởng nhuộm |
| **40–55%** | **Hồi 3: Quyền lực** | Quân đội, công trường, lực lượng cai trị — nâng quy mô và tạo áp lực | **Reveal #1**: Quay gáy (Look-away) reveal lực lượng quân sự/quy mô lớn | 5:05 quay gáy → đại quân tập trận, chuồng ngựa |
| **55–70%** | **Hồi 4: Cao trào nguy hiểm** | **Một** sự kiện quyền lực lớn duy nhất → bị phát hiện/để ý → rượt đuổi nghẹt thở qua ngõ → thoát hiểm | Máy rung lắc, thở dốc, chạy trốn, phóng ngựa ra cổng | 6:05–7:05 đoàn xe hoàng đế đi qua, dân quỳ rạp, lính tiến lại, chạy qua ngõ, phi ngựa thoát |
| **70–75%** | **Hồi 5: Hạ nhịp** | **Khoảng đệm hạ nhiệt**: đi nhờ xe, trò chuyện với dân quê thân thiện, cảnh đồng quê | Camera tĩnh hơn, nhịp thở chậm, J-cut ambient bình yên | 7:25 đi nhờ xe bò với bà nông dân thân thiện |
| **75–95%** | **Hồi 6: Di sản** | Kỳ quan/di sản người xem **đã biết tên** — reveal theo 4 bậc: nhìn từ xa → xưởng làm → chạm tay → toàn cảnh khổng lồ | **Reveal #2**: Nhìn công trình từ xa (7:50)<br>**Reveal #3**: Toàn cảnh kỳ quan từ trên cao (9:25) + POV chạm tay (9:05) + chi tiết "Wow" sơn màu (8:50) | 7:50–10:05 lăng mộ từ xa → lò nung đầu tượng → tượng sơn màu rực rỡ → chạm kiếm đồng → hố tượng khổng lồ |
| **95–100%** | **Hồi 7: Kết** | Ngồi tĩnh lúc hoàng hôn, chia sẻ suy nghĩ cá nhân, mồi tập sau. Không có cảnh "quay về" | **Máy dựng cố định** dưới gốc cây/bờ tường hoàng hôn | 10:22 ngồi dưới gốc cây hoàng hôn |

#### 5b. Bảng ánh xạ 23 Beat chi tiết từ Video Mẫu

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

Shorts: hook (1) → 2–3 beat đời thường/wow (2–4) → nguy hiểm hoặc reveal (5) → câu kết cliffhanger (6).

**Quy tắc thoại** (chi tiết và ví dụ ở `voice-bible.md`)
- **Mật độ từ (user chốt 2026-10-01: nói nhanh để giữ nhịp, không gây buồn ngủ)**: clip 10s = **22–28 từ**; 8s = 18–22; 6s = 13–16; 4s = 8–10.
- Chỉ chừa **~0.5s không thoại ở đầu và cuối mỗi clip** cho chuyển cảnh — không bao giờ cắt ngang câu.
- **Một người nói/clip.** Dân bản địa nói → vlogger im lặng phản ứng (mắt mở to, môi mím).
- Thoại viết theo `VOICE_LOCK`, kèm tag cách diễn đạt: `Nora says (fast, teeth chattering, half-laughing): "..."`. Sự thật lịch sử nói qua trải nghiệm của vlogger, không giảng bài.
- **Chạy checklist chống giọng AI (`voice-bible.md` mục 6) trên từng dòng thoại** trước khi đưa vào `video_prompt`. Cấm câu chốt khẩu hiệu, mô tả lại thứ đang hiện trên hình, giọng giảng ("Survival rule number one"), số liệu vlogger không thể biết.
- Chửi thề nhẹ chỉ viết dạng cắt dở (`"sh—"`, `"what the f—"`) và bíp ở hậu kỳ; tối đa 1 lần / 3 clip, không chửi trong hook hay beat kết (`voice-bible.md` mục 3).
- Mỗi beat có một thứ mới: nơi mới, người mới, thông tin mới hoặc nguy hiểm mới.

#### 5c. Survival Preset — "I Survived 24 Hours in…" (thời tiền sử, thiên tai, tương lai khắc nghiệt)

Dùng khi bối cảnh tự nó có thể giết người (Kỷ Băng Hà, khủng long, hậu tận thế, Sao Hỏa). **Giữ nguyên 7 hồi và 3 cú reveal của mục 5a**, chỉ đổi xương sống sang **đồng hồ 24 giờ + cơ thể vlogger xuống dốc dần**:

| Hồi (mục 5a) | Giờ trong 24h | Áp lực cơ thể | Beat sinh tồn |
|---|---|---|---|
| 1 Hook | Giờ 0–1 | Sốc lạnh / sốc môi trường | Câu đầu nói rõ ở đâu, năm nào, thử thách 24h |
| 2 Đời thường | Giờ 1–8 | Tê tay → run → đói | Chỗ trú, lửa và nước, ăn, quần áo — **mỗi beat là một phương pháp sinh tồn có giải thích + bằng chứng khảo cổ** (khuôn A/B/C ở `voice-bible.md` mục 4) |
| 3 Quyền lực | Giờ 8–12 | Mệt, mất cảm giác ngón chân | Reveal #1: đàn thú / bộ lạc chuẩn bị đi săn |
| 4 Cao trào | Giờ 12–15 | Adrenaline, thở dốc | Cuộc săn / thú lớn tấn công / bão — đúng **một** cao trào |
| 5 Hạ nhịp | Giờ 15–17 | Run sau cơn sợ, cười được | Chia thịt, được bộ lạc coi là người trong nhóm |
| 6 Di sản | Giờ 17–22 | Kiệt sức, lạnh về đêm | Nghệ thuật, nghi lễ, bầu trời đêm — áp lực lạnh vẫn còn |
| 7 Kết | Giờ 23–24 | Tĩnh, kiệt | Máy dựng cố định, nói thật lòng, không có câu đạo lý |

- **Mốc giờ nói bằng lời**, không bằng chữ trên màn hình (mục 8): `"Hour six."` mở đầu khoảng mỗi 3 beat, không phải mỗi clip.
- **Vlogger là chuyên gia (user chốt 2026-10-01): nhà khảo cổ có kỹ năng sinh tồn thượng thừa.** Người xem ở lại vì học được phương pháp dùng được + lý do + lịch sử thật đằng sau. Mỗi beat kiến thức theo 1 trong 3 khuôn ở `voice-bible.md` mục 4: **Làm → Vì sao → Bằng chứng**, **Lý thuyết vs Thực tế** (hiện vật cô từng đào được giờ thấy được dùng), **Người bản địa dạy mẹo địa phương → Nora giải thích** (Translator POV). Mẹo nói dạng mệnh lệnh của người thật ("Don't eat snow. Ever."), không dùng nhãn khuôn mẫu ("Survival rule number one:", "Here's the trick:").
- **Mọi mẹo sinh tồn phải có nguồn trong bảng beat (mục 4)**, đánh dấu ✅/⚠️. Danh sách câu nghe hay nhưng sai (phổi đóng băng, hoại tử 10 phút, "8,000 calo") ở `voice-bible.md` mục 7.
- Tiêu đề: dùng động từ **"Survived"** thay cho "Spent" (`I Survived 24 Hours in/with …`); chi tiết SEO ở `/fk-youtube-seo`.

### 6. Storyboard & tỉ lệ loại shot

**Bảng storyboard toàn video (bắt buộc, trước khi viết Clip JSON):**

| # | Hồi | Beat | Loại shot | Hành động | Thoại (ai nói) | Chuyển cảnh vào | Chuyển cảnh ra | Khung cuối |
|---|---|---|---|---|---|---|---|---|

Cột "Khung cuối" mô tả chính xác khung hình cuối clip (vd: "súc gỗ che 90% khung, đi trái→phải") — clip kế tiếp mở từ đúng khung này.

**Tỉ lệ loại shot** — giữ gần đúng, vì chính tỉ lệ này tạo cảm giác "máy của nhân vật":

| Tỉ lệ | Loại | Mẫu `shot` (từ `prompt-templates.md`) |
|---|---|---|
| ~65% | Selfie góc siêu rộng (front camera 0.5x), cánh tay/gậy lọt khung, vừa đi vừa nói | `ultra-wide selfie at arm's length, her extended arm visible at the right edge, face on the left third, deep [street] behind her` |
| ~15% | POV mắt nhân vật, thấy tay cô tương tác với đồ vật/người — không thấy mặt, dùng cho beat xúc giác | `first-person POV from her eye level, her own hands visible in the lower frame [scooping millet / touching bronze armor]` |
| ~10% | Sau gáy / qua vai — chủ yếu để làm chuyển cảnh | `camera behind her head, she turns away to look at [X], the back of her hair bun fills the frame` |
| ~5% | Máy dựng cố định (ăn uống, kết) | `smartphone propped on the table facing her, static frame, she sits and eats, vendors moving behind` |
| ~5% | Toàn cảnh hoành tráng nhưng **vẫn từ vị trí nhân vật đứng** | `view from where she stands on a high earthen ridge, slow handheld pan over [thousands of soldiers / the pits]; the view is her own eyes, and she never appears in the frame` |

**Không drone, không flycam, không b-roll điện ảnh tách rời** — video mẫu gần như không có shot nào không "quay bằng máy của cô". Chỉ dùng drone khi user yêu cầu rõ.

**Clip dân bản địa nói**: người nói là dân bản địa (`<Name> says in [ancient language]: "..."`), thêm vào hành động `"<Vlogger> listens silently, reacting with wide eyes, lips closed"`.

### 7. Chuyển cảnh — giấu mối nối bằng chuyển động có sẵn trong khung

Nguyên tắc từ video mẫu: **cắt thẳng, che mối nối bằng chuyển động trong khung** — vật thể tiền cảnh lướt sát ống kính, nhân vật quay gáy đi, camera lia theo thứ chạy qua. **Không dùng hiệu ứng dựng (crossfade, glitch, zoom), không title card.** Jump cut khi đang đi bộ là chấp nhận được. Mỗi chuyển cảnh = 2 clip được prompt khớp nhau: clip A kết bằng một khung "che", clip B mở từ đúng khung che đó — hai clip chỉ khớp khi **cả hai prompt cùng mô tả khung che**.

#### 7a. Ba cách nối trong FlowKit (ghi rõ cho từng mối nối trong storyboard)

`transitions.md` mô tả 3 cách nối trong Google Flow; ánh xạ sang FlowKit như sau:

| Cách (Flow gốc) | Trong FlowKit | Dùng khi |
|---|---|---|
| **Tạo riêng rồi cắt** | 2 scene độc lập (ROOT, hoặc CONTINUATION để ảnh Frame 0 kế thừa bối cảnh qua EDIT_IMAGE). `video_prompt` A kết bằng khung che; `prompt` (Frame 0) + đầu `video_prompt` của B mô tả khung che đang rời đi. Cắt thẳng tại khung che kín nhất lúc concat | **Mặc định** cho mối nối giữa các beat. Nhanh, chạy song song được |
| **Frames to Video** (khung cuối A = khung đầu B) | Sinh video A trước → trích khung cuối `ffmpeg -sseof -0.1 -i A.mp4 -frames:v 1 A_last.png` → `/fk-upload-image` → PATCH `${ori}_image_media_id` của scene B → sinh video B | Hai nửa của **cùng một beat 15s** cần liền mạch tuyệt đối (thay cho Extend). Phải chạy tuần tự A → B |
| **Extend** | FlowKit không có Extend. Thay bằng F2V ở trên, hoặc Omni Flash first+last: `POST /api/flow/generate-video` với `model_family: "omni_flash"` + `start_image_media_id` + `end_image_media_id` (hỗ trợ 4/6/8/10s, xem `docs/OMNI_FLASH.md`) | Clip cầu nối cần cả khung đầu và khung cuối cố định |

⚠️ **Không dùng `/fk-gen-chain-videos` (Veo start+end frame)** — trên transport hiện tại nó fail với `UNSUPPORTED_ON_BATCH_API`. `FLOW_ALLOW_DEGRADED=1` chỉ biến nó thành i2v thường, mối nối **không** liền — khi đó phải dựa hoàn toàn vào khung che.

#### 7b. Luật giấu mối nối (áp dụng cho mọi kỹ thuật)
- 1–2 giây cuối clip A và đầu clip B **không có thoại**.
- Giữ nguyên ánh sáng/giờ trong ngày giữa A và B; muốn đổi giờ thì dùng time-skip công khai.
- Hướng chuyển động ở A và B phải cùng chiều (trái→phải thì B cũng rời khung sang phải).
- Đầu clip B giữ vật che thêm ~3–5 khung hình trước khi mở ra — mắt đọc thành một chuyển động liên tục.
- J-cut: âm thanh môi trường của B vào sớm ~0.5s trước điểm cắt; SFX "vút" nhẹ khi vật lướt qua (Bước 5).

#### 7c. Kỹ thuật ưu tiên (~80% mối nối — theo video mẫu)
Viết `transition_in`/`transition_out` thành **câu prompt cụ thể**, không chỉ ghi tên kỹ thuật:

| Kỹ thuật | Cuối clip A (`transition_out`) | Đầu clip B (`transition_in`) |
|---|---|---|
| **A. Foreground wipe** ⭐ dùng nhiều nhất — **chỉ cho shot POV** (máy nhìn ra phía trước, không có mặt vlogger) | `in the last 1.5 seconds two laborers carry a large wooden log right across the lens from left to right, almost filling the frame` | `opens with a wooden log sliding out of frame to the right very close to the lens, revealing [new place]` |
| **B. Look-away / back-of-head** (video mẫu dùng để reveal đại quân) | `she turns her head away from the camera to look behind her, the back of her hair bun fills the frame` | `opens on the back of her head, she turns around to face the camera revealing [new place] behind her` |
| **C. Swing — lia theo chuyển động** ⭐ **mặc định cho shot selfie** | `a horse gallops past very close, the camera whips right following it, heavy motion blur fills the frame` | `begins mid whip pan with heavy motion blur moving right, settling on [new place]` |
| **D. Selfie → POV** (beat xúc giác) | `she leans toward the camera, whispers 'look at this', and points past the lens` | `first-person POV from her eye level, her own hands visible in the lower frame reaching for [object]` |
| **E. Jump cut khi đi bộ** | cùng nhân vật, cùng góc selfie, cùng hướng đi | bối cảnh đã tiến lên — cắt thẳng, không xử lý gì thêm |

Vật che có thể là: súc gỗ phu khuân, tấm ván, bánh xe bò, thân ngựa, người đi ngang, cột gỗ.

#### 7d. Kỹ thuật bổ sung (dùng tiết chế)
| Kỹ thuật | Khi nào | Ghi chú |
|---|---|---|
| **Hand-over-lens** | Chuyển chỗ gần trong cùng thành phố | A: `in the final second she raises her palm toward the lens until it fully covers the camera, frame goes dark` · B: `opens with a palm covering the lens, the hand pulls away to reveal [new place]` |
| **Walk-through** (cửa/màn vải/đám đông) | Vào trong nhà, cung điện, quán | A: bước qua màn vải/cổng tối, khung ngập tối · B: từ bóng tối bước ra nội thất. Biến thể: crowd wipe, xe ngựa chạy qua |
| **Selfie flip (lật camera)** — "chữ ký" của format | Reveal cảnh hoành tráng ở hồi Di sản | A: selfie, `"you guys… look at this"`, bắt đầu xoay điện thoại · B: POV camera sau, cảnh lớn, tay hơi lọt khung. Cắt giữa cú xoay |
| **Whip pan** | Đổi chủ thể nhanh, đoạn năng lượng cao | Hướng quăng A và B phải khớp; cắt ở khung nhòe nhất |
| **Match cut** | Nhảy thời gian/địa điểm có ý nghĩa | Vật cùng vị trí + kích thước trong khung (đồng tiền → mặt trời; khói bát cháo → khói lò rèn) |
| **Time-skip** | Nhảy giờ | Cùng góc/địa điểm, ánh sáng đổi (trưa → hoàng hôn → đuốc), nhân vật đổi trạng thái (mệt, lấm bụi). **Không title card** |
| **Dust / smoke wipe** | Công trường, lò gốm, chiến trường | A: bụi/khói phủ kín khung · B: bụi tan ra |
| **Light wipe + phone glitch** | **Chỉ** biến thể "cú du hành" khi user yêu cầu | Mặc định không có cảnh du hành; glitch là hiệu ứng dựng, trái nguyên tắc "không hiệu ứng" |

**Bảng chọn nhanh:** đi sang chỗ gần → foreground wipe / hand-over-lens / walk-through · reveal hoành tráng → look-away hoặc selfie flip · đoạn năng lượng cao → swing / whip pan · nhảy giờ → time-skip · trong một đoạn nói chuyện → jump cut.

### 8. Không chữ trên màn hình, nhạc/ambient trải liên tục
Video mẫu **không có bất kỳ chữ nào trên màn hình** — không title card chương, không "3 HOURS LATER", không phụ đề cứng. Mọi thông tin (địa điểm, thời gian, chuyển cảnh) truyền qua lời thoại + hình ảnh. Phụ đề chỉ là tùy chọn dạng file `.srt` rời, không burn vào hình. Vì vậy **không dùng `/fk-gen-text-overlays`**, và không dùng `/fk-concat-fit-narrator` với text overlay/crossfade.

Âm thanh (nhạc nền + ambient) **trải liên tục suốt video, gần như không có khoảng lặng** — hạ nhạc nhỏ dưới thoại thay vì tắt hẳn giữa các scene; hạ thêm ở cảnh nguy hiểm và cảnh kết (Bước 5).

### 9. Chuẩn chân thực — "mọi thứ quay bằng điện thoại của cô"
Độ chân thật của format đến từ việc **người xem tin đây là footage điện thoại thật**. Mọi clip phải giữ đủ các yếu tố sau:

- **Style string cố định** (đầu mọi `video_prompt`, từ `prompt-templates.md`):
  `handheld front-camera vlog footage, arm extended holding camera, natural daylight, zero lens distortion, straight natural perspective, subtle hand shake, photorealistic, documentary realism`
- **Dấu vết máy quay chân thực**: góc nhìn tự nhiên, không méo viền (zero lens distortion, straight lines), rung tay nhẹ theo nhịp bước, cánh tay lọt mép khung ở shot selfie, auto-exposure theo nguồn sáng tự nhiên. Không dolly/crane/gimbal mượt kiểu điện ảnh.
- **Người nền phản ứng**: dân bản địa dừng lại nhìn chằm chằm, tò mò hoặc nghi ngờ — nhưng **không ai nói** trừ người nói duy nhất của clip.
- **Audio môi trường đúng thời kỳ**: tiếng chợ bằng ngôn ngữ cổ/địa phương, bánh xe gỗ lạch cạch, chuông đồng xa — ghi ở dòng `Audio:` cuối prompt.
- **Ràng buộc viết thành câu khẳng định trong thân prompt — KHÔNG dùng dòng `Negative:` liệt kê từ khóa** (góp ý của user: liệt kê từ khóa không có tác dụng, điện thoại vẫn hiện ra). Câu chuẩn, đặt trước dòng `Audio:`:
  `The view comes from her own outstretched arm or her own eyes, and her free hand is empty. Mia stays in frame for the whole clip and never disappears. The locals wear [period clothing]; everything around is [era], with no modern buildings or vehicles. Only Mia speaks. No subtitles or text appear on screen. This looks like real footage, not a movie or a 3D render.`
- **Material**: `realistic` mặc định áp *Canon EOS R5, 35mm* — kiểu ảnh máy ảnh, lệch với footage điện thoại. Khuyến nghị tạo material tùy chỉnh (giữ ảnh ref chân thực, chỉ đổi scene sang chất điện thoại):
  ```bash
  curl -X POST http://127.0.0.1:8100/api/materials -H "Content-Type: application/json" -d '{
    "id": "phone_vlog",
    "name": "Smartphone Vlog (Photoreal)",
    "style_instruction": "Photorealistic RAW photograph, natural available light, real skin texture, documentary realism.",
    "negative_prompt": "NOT 3D render, NOT anime, NOT illustration, NOT cinematic color grade, NOT studio lighting, NOT lens distortion.",
    "scene_prefix": "Handheld vlog frame, natural daylight, zero lens distortion, straight natural perspective, documentary realism.",
    "lighting": "Natural available light"
  }'
  ```
  Rồi tạo project với `"material": "phone_vlog"`. Nếu user không muốn thêm material → dùng `realistic` và dựa vào style string trong `video_prompt`.

### 10. Clip JSON từng clip → ánh xạ sang scene FlowKit
Sau bảng storyboard, viết **Clip JSON cho từng clip 8s** theo mẫu `prompt-templates.md` — đây là bản thiết kế đọc được, lưu trong file kịch bản. Mỗi clip **bắt buộc** có `transition_in`, `transition_out` (câu prompt cụ thể) và `join` (cách nối, mục 7a).

```json
{
  "clip_id": "CH2-05",
  "duration": "8s",
  "aspect_ratio": "16:9",
  "style": "handheld smartphone selfie-stick vlog footage, ultra-wide 0.5x front camera, natural daylight, slight lens distortion, subtle hand shake, photorealistic, documentary realism",
  "character": "<dán CHARACTER_LOCK nguyên văn>",
  "setting": "Xianyang market street, Qin dynasty China, 211 BC: rammed-earth walls, dark timber stalls with grey tile roofs, dirt road, merchants in plain hemp robes, soldiers in lamellar armor at the far end",
  "shot": "ultra-wide selfie at arm's length, her extended arm visible at the right edge, face on the left third, deep market street behind her",
  "action": "0-2s she walks backward glancing over her shoulder; 2-6s leans toward the camera and speaks in a hushed voice; 6-8s two laborers carry a large wooden log right across the lens from left to right, almost filling the frame",
  "dialogue": {"speaker": "Nora", "line": "Okay, don't freak out, but everyone here is staring at my hair.", "delivery": "hushed, nervous half-laugh"},
  "background_people": "merchants pause and stare at her with suspicion, no one speaks",
  "audio": "market chatter in ancient Chinese, clattering wooden carts, distant bronze bell",
  "transition_in": "opens with a cart wheel sliding out of frame very close to the lens",
  "transition_out": "foreground wipe: log fills the frame in the final second",
  "join": "CUT — cắt tại khung súc gỗ che kín nhất; CH2-06 mở bằng súc gỗ rời khung sang phải",
  "physics": "camera: selfie at arm's length facing her, walking forward at walking pace; frame 0: Nora mid-market, stalls both sides; moving: laborers walk left to right at walking pace behind the lens line; Nora never leaves frame except by camera movement",
  "constraints": "The view comes from her own outstretched arm or her own eyes, and her free hand is empty. Nora stays in frame for the whole clip and never disappears. Only Nora speaks. No subtitles or text appear on screen. This looks like real footage, not a movie or a 3D render."
}
```

| Trường Clip JSON | Vào trường FlowKit |
|---|---|
| `character` | entity `description` (CHARACTER_LOCK) + `character_names` của scene |
| `setting` | entity `location` + câu bối cảnh trong `prompt` và `video_prompt` (luôn kèm thành phố + năm) |
| `shot` + khung đầu của `transition_in` | `prompt` (ảnh Frame 0 — mô tả tư thế ở giây 0, kể cả vật che đang rời khung) |
| `style` + `shot` + `action` + `dialogue` + `background_people` + `transition_out` | `video_prompt` dạng văn xuôi, chia `0-3s / 3-6s / 6-8s`; thoại theo format `Nora says: "..." (no subtitles)` |
| `audio` | dòng `Audio:` / `SFX:` cuối `video_prompt` |
| `constraints` | các câu khẳng định ngay trước dòng `Audio:` trong `video_prompt` (không dùng `Negative:`) |
| `join` | `chain_type` + `parent_scene_id` (CONTINUATION nếu cùng bối cảnh) và ghi chú cho bước F2V/concat |
| `transition_prompt` | để trống — chỉ dùng khi scene có `end_scene_media_id`, mà Veo start+end đang unsupported |
| `bleep_at` (tùy chọn) | không vào FlowKit — ghi chú hậu kỳ: mốc giây cần phủ tiếng bíp lên từ chửi cắt dở (`voice-bible.md` mục 3) |

---

### 11. Bài Học Từ Sản Xuất Thực Tế — Góp Ý Của User (BẮT BUỘC, ưu tiên hơn mọi chỗ khác trong skill)

Rút ra từ dự án `output/atlantis-9600bc/` (2026-09-27). Khi mâu thuẫn với phần khác của skill, **mục này thắng**.

**Quy trình**
1. **Xác nhận trước mỗi bước sinh** (ảnh ref, video, clip thử, sinh lại): nói rõ sinh gì, bao nhiêu, rồi chờ user đồng ý. Xong mỗi bước thì **dừng và đưa kết quả cho user xem** (kèm link file, bảng ghép ảnh hoặc khung hình). Không tự sinh lại khi lỗi.
2. **Chạy thử clip khó nhất trước, 1 clip**, rồi **1 clip bình thường làm mốc**, trước khi gửi cả loạt. Lỗi thường có hệ thống; sửa ở vài clip đầu rẻ hơn nhiều so với sửa cả loạt.
3. **Ảnh ref phải được user xem trước khi dùng.** Ghép bảng ảnh và đưa đường dẫn file để user tự xem.

**Ảnh ref (R2V)**
4. Mỗi clip **tối đa 3 ref**; worker chỉ lấy entity `character` và `visual_asset`. Công trình hay bối cảnh cần giữ nhất quán (thành phố, tường thành, đền) phải khai báo là `visual_asset`.
5. **Clip nào có thành phố hay bối cảnh lớn thì phải kèm ảnh ref của chính bối cảnh đó** (ví dụ ảnh toàn cảnh thành phố). Chỉ tả bằng chữ thì model tự vẽ một thành phố khác.
6. **Mọi ảnh ref đều sinh ngang 16:9** (góp ý của user, 2026-10-01), kể cả nhân vật (sheet các góc đặt cạnh nhau). FlowKit đã sinh 16:9 cho mọi loại entity. Entity `location` **không** được worker đưa vào R2V, nên mọi bối cảnh cần giữ nhất quán phải khai báo `visual_asset`. Worker lấy `visual_asset` trước `character`, nên tổng `character_names` của mỗi clip phải ≤3 và luôn có vlogger, nếu không vlogger bị loại khỏi ref.
7. Ảnh ref không được có người, tay, đồ vật hay trang phục hiện đại lọt vào (găng tay, ủng, người mặc áo thun), không có kiến trúc lệch thời kỳ (mái vòm, tháp nhọn, lâu đài trung cổ), và không có dải màu trơn quanh ảnh.

**Viết `video_prompt`**
8. **Ràng buộc là câu khẳng định**, không dùng dòng `Negative:` (xem mục 9).
9. **Điện thoại là máy quay, nhưng KHÔNG viết chữ `phone` trong prompt (bài 33):** chỉ tả góc nhìn (`The lens sits at the end of her outstretched arm…` / `The view is her own eyes`) và tay trống (`her free hand is empty`). Không viết `she holds the phone up`, `the phone is the camera` hay `no phone`; nhắc tới đồ vật, kể cả câu phủ định, đều làm model vẽ nó ra. Với POV, cho tay nhân vật bận việc khác (bám mép thuyền, cầm đồ vật).
10. **Shot selfie không dùng vật lướt qua ống kính** (xà gỗ, ngựa…): ở góc selfie, vật phải chen vào khoảng khoảng 60 cm giữa gậy selfie và mặt nên trông như "bay" đến, và model hay xóa luôn nhân vật (user duyệt: không thực tế). Selfie chuyển cảnh bằng **swing/whip pan** (nhân vật xoay gậy lia máy nhanh sang cảnh mới, nhòe chuyển động nửa giây cuối; clip sau mở giữa cú lia rồi dừng lại trên nhân vật ở chỗ mới) hoặc **jump cut**. Foreground wipe chỉ dùng cho shot POV.
11. **Chống hình kiểu 3D ở cảnh thần thoại hoặc thảm họa** (model chỉ biết những cảnh này qua phim và game):
    - mở prompt bằng khối "footage thật": `raw unedited amateur video, looks like real footage posted online, not a movie`, rung tay, auto-exposure, nhiễu nén, giọt nước trên ống kính, ánh sáng bệt;
    - tả bằng vật liệu có thật (ví dụ "tường ốp tấm đồng đỏ cũ, xỉn màu" thay vì "orichalcum phát sáng"); tên thần thoại chỉ để trong lời thoại;
    - giảm độ hoành tráng: cảnh ở xa, bị mưa hoặc sương che, khung lệch;
    - nhưng **vẫn phải kèm ảnh ref bối cảnh** (quy tắc 5), nếu không sẽ mất nhận diện (ví dụ Atlantis thành làng chài Anh).

**Kỹ thuật FlowKit**
12. `POST /api/scenes` không nhận `duration`; phải `PATCH {"duration": 8}` (thiếu thì âm thầm ra clip 10s).
13. Mỗi clip chỉ có 1 giọng, lấy từ entity **đầu tiên theo thứ tự DB** có `voice_description`. **Chỉ nhân vật chính khai báo voice**; khai báo cho nhân vật phụ thì giọng họ sẽ đè lên thoại của nhân vật chính.
14. Sinh lại một scene R2V đã COMPLETED: PATCH `horizontal_video_status: PENDING` rồi gửi `GENERATE_VIDEO_REFS` (không có `REGENERATE_VIDEO_REFS`).
15. Ảnh do Flow sinh luôn có logo ✦ ở góc dưới phải (tâm khoảng `(W-98, H-97)`). Xóa bằng `tools/remove_watermark_from_image.py` (đã sửa ngưỡng ngày 2026-09-27), rồi **mở ảnh ra kiểm tra**. Ảnh không phải do Flow sinh (ví dụ bảng ảnh ghép của user) thì tool có thể đoán sai vị trí.
16. Google chặn sinh tự động (`UNUSUAL_ACTIVITY`) → làm theo Bước 4.9. Đổi tài khoản Google thì phải tạo project mới (project và media thuộc tài khoản đã tạo ra chúng).

19. **Không có gì tự hiện ra giữa clip:** thứ được "reveal" (thành phố, tường thành, tượng…) phải **có mặt từ khung hình đầu**, chỉ lộ ra nhờ nhân vật dịch sang bên hoặc máy xoay tới, và đứng yên một chỗ. Viết rõ vị trí của nó ở giây 0 (ví dụ `to the right of her head, far across the water, the city is already visible on the horizon`) và thêm câu `nothing pops into view`. Nếu tả nó ở mốc thời gian sau, model sẽ cho nó xuất hiện ở mốc đó (lỗi S31 Atlantis).

20. **Ghi rõ hướng và tốc độ của mọi thứ đang di chuyển** (thuyền, xe, ngựa, người chạy): đi về đâu, nhanh cỡ nào, và hệ quả trong khung hình (ví dụ `the boat moves only at slow rowing speed and away from the city, so the city stays the same size or slowly shrinks and never gets closer`). Tả cả chuyển động vật lý thật (thuyền nhấp nhô và lắc theo sóng, không lướt đi; người chèo ngồi quay mặt về phía đuôi thuyền). Bỏ trống thì model chọn kiểu kịch tính và sai vật lý (lỗi S31 Atlantis: thuyền chèo lao về phía thành phố như thuyền máy).

21. **Bảng vật lý phải được user duyệt trước khi viết Clip JSON** (mục Định dạng output, bước 5b): mỗi clip ghi máy đặt ở đâu và nhìn về đâu, có gì trong khung ở giây 0, mọi vật di chuyển (hướng, tốc độ, hệ quả trong khung), chuyển động vật lý thật, và ai hoặc cái gì rời khung bằng cách nào. Nội dung bảng được viết thành câu trong `video_prompt` (quy tắc 19, 20). Đây là chỗ bắt lỗi vật lý rẻ nhất: sửa trên giấy, không tốn credit.

22. **Trang phục khóa bằng panel toàn thân trong ảnh sheet nhân vật** (góp ý của user, 2026-10-01; thay bài học S31 Atlantis): ảnh ref vlogger là một sheet 16:9 có mặt rõ, góc 3/4 và toàn thân mặc trang phục (xem mục 2). Chỉ tách entity `<Vlogger> Outfit` riêng khi trang phục vẫn bị đổi giữa các clip.

23. **Tuyệt đối CẤM từ khóa `selfie-stick` và mô tả cầm điện thoại (bài học S11, S17, S20 Atlantis):**
    - Từ khóa `selfie-stick` hay `smartphone selfie` làm AI vẽ thêm 1 chiếc gậy selfie trong tay, hoặc vẽ 1 chiếc điện thoại/màn hình điện thoại bay lơ lửng trước ống kính (hiện tượng quay màn hình điện thoại).
    - **Chuẩn thay thế:** Dùng `Handheld front-camera vlog footage, ultra-wide 0.5x lens, slight wide-angle barrel distortion`. Tả cánh tay: `Mia holds the camera at arm's length with her right arm extended toward the bottom-right corner of the frame.`
    - **Khóa câu khẳng định bắt buộc:** `The lens sits at the end of Mia's outstretched right arm, looking back at her; her right hand is beyond the frame edge and her other hand is empty, so the frame contains only Mia and the scene behind her.` (không nhắc tới thiết bị, xem bài 33)

24. **100% First-Person POV không vẽ thiết bị hay thao tác sai vật lý (bài học S12, S16, S34 Atlantis):**
    - Khi quay POV (nhúng tay thử nước, bước qua cầu, nhìn xuống mặt nước): Người xem nhìn thẳng qua mắt vlogger. Vlogger đứng hoàn toàn sau camera, hai tay giữ máy ở tầm ngực.
    - Chỉ có **1 bàn tay không** (trống trơn, không cầm gì) vươn vào mép dưới khung hình để tương tác (chạm nước, nhặt đá, chỉ tay).
    - CẤM mô tả "cầm gậy rồi thả ra rồi cầm điện thoại" hoặc vẽ bàn tay cầm điện thoại khác; cấm để điện thoại nổi lơ lửng trên mặt nước. Khóa câu: `The view is Mia's own eyes; Mia's face and body never appear, and only her bare empty hand enters the lower frame.` (không nhắc tới thiết bị, xem bài 33)

25. **Vật lý cầm máy khi chạy tháo chạy và nhảy — Running & Action Leap Physics (bài học S27, S30 Atlantis):**
    - **Khi chạy trốn (S27):** Vlogger vlogging cuộc tháo chạy của mình thì **PHẢI LUÔN NẮM CHẶT CAMERA QUAY MẶT MÌNH**. Cấm để AI cho nhân vật buông tay, vứt điện thoại hay chạy xa khỏi camera. Tả: `Mia clutches the camera firmly in her right hand at arm's length pointed continuously at her face; she NEVER drops, releases, or lets go of the camera. The camera shakes violently with her sprint.`
    - **Khi nhảy (S30):** Vlogger một tay nắm chặt máy nhảy xuống thuyền; camera trải qua một cú giật nảy giật dọc cực kỳ thực tế khi tiếp đất trên sàn thuyền gỗ. Cấm buông máy/gậy trước khi nhảy.

26. **Khóa cố định nền đất cho cảnh trên cạn (bài học S11 Atlantis):**
    - Với các cảnh đứng trên bờ đá, suối khoáng, thềm gạch: Bắt buộc ghi rõ `Mia stands firmly on a solid stone terrace/ground; zero vehicle or boat motion; background structures remain completely static`. Tránh mô tả chung chung về nước chảy khiến AI làm nền trôi bồng bềnh như đang trên thuyền hay cầu di chuyển theo thuyền.

27. **Cơ học truyền lực & Điểm neo vững chắc (Force Transmission & Structural Ground Anchoring) (bài học S28–S30 Ice Age 20,000 BC):**
    - **CẤM để cơ thể người (chân, tay, vai) làm điểm tì chống chịu lực trực tiếp** từ động vật khổng lồ hoặc vật cản nặng hàng tấn (`human boot → spear → mammoth`). Động lượng $p = m \times v$ sẽ nghiền nát hoặc hất văng người.
    - **Đường truyền lực đúng:** `Incoming force → Weapon/Object → Timber barrier/Brace → Frozen Ground/Boulders`. Giáo cắm vào rãnh ngang của dầm gỗ chắn nặng (`heavy timber brace`), tựa vào súc gỗ ngang neo giữa các tảng đá đóng băng.
    - **Chiến thuật thực tế:** Người tiền sử không "chặn đứng" con voi bằng sức người; họ dùng **khe hẹp + mặt băng trơn + chướng ngại vật kiên cố** để ép động vật mất bám, trượt ngang và bẻ hướng tháo lui (`deflection, not direct stop`).

28. **Động lực học Megafauna & Quán tính chuyển động thứ cấp (Megafauna Biomechanics & Heavy Inertia) (bài học S20, S22, S25, S27, S29 Ice Age):**
    - Động vật lớn (voi ma mút, tê giác lông mượt, khủng long) có **quán tính thân hình cực lớn (`heavy body inertia`)**: chân nén tuyết/đất trước khi thân chuyển động; tai, vòi, lông dài có độ trễ chuyển động thứ cấp (`delayed secondary motion`).
    - **CẤM phanh khựng lại cách mũi giáo vài bước như ô tô có ABS** (`skidding to a halt just feet away`). Trên mặt băng/bùn: chân trước mất bám (`loses traction on glazed surface`), thân hình lảo đảo chao đảo cố lấy lại thăng bằng (`lurching sideways to regain balance`), trượt ngang và bẻ hướng.
    - **Không tả thú "vung ngà như kiếm" (`brandishing tusks`)**, mà là hất đầu tự vệ (`tossing its head defensively, tusks naturally sweeping through snow/brush`). Khi kiếm ăn, ngà chỉ thi thoảng ủi tuyết cạn (`occasionally pushing through shallow snow`).
    - **Phân tầng giải phẫu lông:** Lớp lông ngoài cứng dài (`long coarse guard hairs in uneven strands`) phủ trên lớp lông tơ ngắn dày cách nhiệt (`dense shorter woolly undercoat`).

29. **Vật lý chất liệu, Biến dạng & Nhiệt động học (Material Deformation & Thermodynamic Realism) (bài học S6, S8, S11, S14, S15, S38, S39, S41 Ice Age):**
    - **Nhiệt truyền dần, không tức thì:** Thả đá nung đỏ vào túi nước không làm nước sôi bùng nổ tức thì (`instant violent boil`), mà gây sủi bọt cục bộ quanh viên đá (`rapid localized bubbling around the submerged stone`) và hơi nước bốc lên tăng dần theo đối lưu nhiệt.
    - **Biến dạng vật liệu:** Da thú cong nhẹ dưới áp lực mũi kim khâu (`hide flexes slightly around needle`); đập xương tạo các vết nứt lan tỏa từ điểm va chạm (`cracks radiate from impact point`) rồi mảng yếu mới vỡ toác bốc khói; màng da trống rung nảy rõ rệt theo từng nhịp gõ (`drum membrane visibly flexes with each strike`).
    - **Vân đá tự nhiên:** Lưỡi dao/giáo đá lửa có vân gãy hình vỏ sò tự nhiên (`conchoidal fracture patterns`), tránh tả "như thủy tinh" làm AI vẽ thành kính. Tượng ngà có độ bóng satin mờ với vết ghè đá lửa và bề mặt hơi gồ ghề (`subtle satin sheen, microscopic tool marks and uneven surface`).
    - **Khí động học:** Hơi thở trong −35°C tan biến nhanh trong không khí lạnh (`dense short-lived breath vapor that dissipates rapidly`), không đọng thành khói; khói bốc theo đối lưu nhiệt và bị gió lạnh làm xáo trộn; tàn lửa bay theo luồng khí nóng rồi nguội dần và tắt.

30. **Cử động nhân vật & Quang học Smartphone chân thực (Character Action & Dynamic Smartphone Optics) (bài học S18, S26, S27, S33, S37, toàn bộ 45 cảnh):**
    - **Di chuyển trong tuyết sâu:** Người chạy trong tuyết ngập đầu gối không thể lướt nhanh, mà sải bước nặng nhọc với bước chân rút ngắn (`struggles through knee-deep powder with shortened, heavy strides, boots sinking deep`). Dấu chân nén tuyết sâu với gờ tuyết đùn cao xung quanh mép (`raised rim of displaced snow`).
    - **Không chạy lùi khi tháo chạy:** Vừa chạy tới vừa xoay người ngoái nhìn (`runs forward while twisting upper body and looking back over shoulder`), tránh chạy lùi trên địa hình nguy hiểm.
    - **Quang học Smartphone:** Bỏ câu lệnh cứng nhắc "zero lens distortion", chuyển sang `natural wide-angle handheld perspective, no exaggerated fisheye distortion` (không dùng chữ `smartphone`, xem bài 33).
    - **Động học camera chuyển động:** Khi nhân vật chạy hoặc vận động mạnh, bắt buộc tả: `handheld smartphone footage with natural vertical bounce synchronized to each footfall, slight rotational lag when turning, and realistic motion blur`.
    - **Cân bằng sáng:** Cực quang hay ánh trăng không chiếu sáng rực như đèn neon, mà chỉ tạo ánh xanh nhạt tinh tế trên tuyết và chóp mái, lửa trại/đuốc vẫn là nguồn sáng chính.

31. **Mô hình Prompt 5 Tầng (5-Layer Physical Prompt Architecture):**
    - Mọi cảnh hành động đều tuân thủ 5 tầng:
      - **Layer 1 (Primary Motion):** Hành động chính của chủ thể.
      - **Layer 2 (Force & Traction):** Lực tiếp xúc, ma sát và độ nén bề mặt.
      - **Layer 3 (Secondary Motion & Inertia):** Quán tính thân hình, độ trễ chuyển động của tóc, lông thú, quần áo, tai/vòi.
      - **Layer 4 (Environment/Material Response):** Biến dạng vật liệu, gãy vỡ, đối lưu khói lửa, mảnh vỡ văng tung tóe.
      - **Layer 5 (Camera Dynamic Response):** Độ nảy dọc theo bước chân, độ trễ xoay góc, nhòe chuyển động tự nhiên.

32. **Tính liên tục của Đạo cụ & Vật lý giữa các cảnh (Physical & Prop Continuity):**
    - Khi các cảnh nối tiếp nhau (ví dụ: gắp đá nung S10 → đun nước S11 → uống nước ấm S12), kích thước viên đá, màu sắc than hồng, túi nước và nhiệt độ phải đồng nhất xuyên suốt chuỗi cảnh.

33. **ĐIỆN THOẠI HIỆN RA LẶP ĐI LẶP LẠI — KHÔNG ĐƯỢC NHẮC TỚI THIẾT BỊ TRONG PROMPT (bài học H1/H2 Ice Age 16,000 BC, sau 4 lượt gen hỏng liên tiếp):**
    - **Root-cause:** model video **không hiểu phủ định**. Câu "no phone, no phone screen, no device…" thực chất là gọi tên đồ vật nhiều lần, nên model càng vẽ ra nó. Bản lock `PHONE INVISIBILITY RULE (CRITICAL)` từng ghi ở đây là **SAI**: prompt H1 khi đó chứa `phone` 8 lần, `screen` 4, `device` 3, `smartphone` 3, và kết quả vẫn có điện thoại. Ngoài ra, mọi `style.*` cũ đều mở đầu bằng "Handheld smartphone footage… natural smartphone perspective".
    - **Luật bắt buộc:** trong `style`, `lock`, `general`, `physics`, `bg`, `shot`, `frame0` TUYỆT ĐỐI KHÔNG có các từ `phone`, `smartphone`, `device`, `screen` (theo nghĩa thiết bị), `gadget`, `selfie stick`, `tripod` (đồ vật). Chỉ tả **góc nhìn** và **tay đang trống**:
      - `selfie`/`run`: *"The lens sits at the end of Nora's outstretched right arm, about 60 cm in front of her face, looking back at her; her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there, so her right hand is never in view."* + *"Her left hand is empty, and nothing is held up in front of her or near her face."*
      - `pov`: *"The view is Nora's own eyes, and only the world in front of her fills the frame; the view simply moves as she moves."* (câu khẳng định; không viết "no face, no body, no person" vì phủ định vẫn gọi tên đối tượng, xem bài 37)
      - `tripod`: *"Static locked-off footage from a fixed viewpoint resting on a ledge… nothing that holds or supports the view is visible."*
      - thay "natural smartphone perspective" bằng **"natural wide-angle handheld perspective"**.
    - **Kiểm tra trước khi gen:** sau khi render, grep prompt; phải ra 0 kết quả cho `\b(phone|smartphone|device|gadget|selfie stick)\b`.
    - **Tay giữ camera không được đánh khi chạy (lỗi H1, góc selfie bị gãy ở giây 2.5):** nếu prompt vừa nói "right arm extended toward the lens" vừa nói "arms swinging hard" thì model buộc phải chọn một. Nó cho cả 2 tay đánh, và góc quay biến thành camera người ngoài quay theo. Với shot `run`, luôn viết **"her left arm pumps hard while her right arm stays extended toward the lens for the entire clip"**, không bao giờ viết "arms swing" (số nhiều).
    - **Tốc độ chạy trong tuyết sâu:** để cảnh trông KHẨN CẤP và NHANH, tả `legs pumping as fast as physically possible, her left arm pumping hard, the view bouncing violently with each stride, face locked in wide-eyed terror`. Tránh "short heavy strides" vì model sẽ gen thành đi bộ.
    - **Kẻ đuổi không được bắt kịp:** ghi rõ khoảng cách cố định, ví dụ *"The mammoth stays about twenty metres behind Nora for the whole clip; she never draws level with Nora."* Nếu chỉ ghi "never catches up" thì khung cuối mammoth vẫn chạy ngang hàng.
    - **Biểu cảm:** Với cảnh trốn chạy, phải khóa cứng `wide-eyed terror, mouth open in a gasp or scream, no smile whatsoever, brow furrowed hard` — nếu chỉ tả "terrified" mà không chi tiết, model hay gen mặt cười kiểu excited.

34. **BỘ 3 REF CỐ ĐỊNH CHO VLOGGER: Mặt + Body + Outfit (bài học H1/H2 Ice Age 16,000 BC — outfit trôi, dáng người trôi):**
    - **Root-cause #1 (lỗi nặng nhất): `character_names` phải là TÊN entity, không phải UUID.** Server so khớp theo `name`/`slug` (`_char_matches` trong `agent/sdk/services/operations.py`). Nếu lưu UUID thì không khớp entity nào → server rơi vào nhánh dự phòng và chỉ gửi **1 ref duy nhất** (entity đầu tiên của project). Mọi lock outfit/body đều vô hiệu. Luôn PATCH `character_names: ["Nora", "Nora Body", "Nora Outfit", ...]` và đọc lại scene để kiểm tra.
    - **Root-cause #2: giới hạn ref r2v.** `_R2V_MAX_REFS` đã nâng từ 3 lên 7 (giới hạn Omni Flash). Thứ tự ưu tiên: `visual_asset` trước, rồi `character`; entity `location` KHÔNG được gửi làm ref (chỉ mô tả bằng prompt). Một scene có tối đa 7 ref visual_asset + character.
    - **Root-cause #3: không có entity outfit/body riêng** → model tự suy diễn quần áo theo bối cảnh (tuyết → áo parka nâu) và tự đổi dáng người.
    - **Bộ 3 entity bắt buộc cho vlogger (tất cả `entity_type: character`, ảnh 16:9, đã xóa logo trước khi upload theo rule 28):**
      | Entity | Nguồn ảnh | Chứa gì |
      |---|---|---|
      | `<Vlogger>` | Ảnh mặt user cung cấp (Ice Age: `uploads/nora_main.jpg`) — upload thẳng, KHÔNG gen lại | Chỉ khuôn mặt, tóc, khuyên tai |
      | `<Vlogger> Body` | `EDIT_CHARACTER_IMAGE` với `source_media_id` = media_id ảnh mặt, prompt từ `uploads/nora_base_body_prompt.json` đã sửa: **bỏ panel face close-up, mọi panel cắt ngang VAI (cắt ngang cằm vẫn lộ môi) → không thấy mặt; quần áo phải ÔM SÁT (skin-tight) nếu không model vẽ áo buông thẳng và mất eo**, 3 panel trước / 3/4 / sau, áo tank xám + quần bike đen, chân trần | Chỉ dáng người, tỉ lệ, màu da |
      | `<Vlogger> Outfit` | Crop panel 3/4 + toàn thân từ character sheet đang mặc outfit (`ffmpeg -vf "crop=iw*2/3:ih:iw/3:0"`) | Chỉ trang phục |
    - **Vì sao body KHÔNG có mặt:** nếu ảnh body có mặt, model nhận 2 khuôn mặt khác nhau (ảnh mặt + ảnh body) và trộn lẫn → mặt trôi. Body sheet chỉ được mang thông tin dáng người.
    - **Quy trình khi setup project:**
      1. Xóa logo ảnh mặt → upload → PATCH `media_id` của `<Vlogger>`.
      2. Tạo entity `<Vlogger> Body` với prompt body-không-mặt → link vào project → batch `EDIT_CHARACTER_IMAGE` (`character_id`, `source_media_id` = media_id mặt). Tải về, mở ra kiểm tra không lộ mặt, xóa logo, upload lại, PATCH `media_id`.
      3. Crop outfit → xóa logo nếu có → upload → PATCH `media_id` của `<Vlogger> Outfit`.
      4. Trong `clips.json`: mọi clip có `<Vlogger>` trong `refs` phải có đủ `["<Vlogger>", "<Vlogger> Body", "<Vlogger> Outfit", ...]`.
      5. `common.identity` nêu rõ vai trò từng ảnh: *"her face from the Nora face sheet, her tall curvy hourglass build from the Nora Body sheet, and her clothing from the Nora Outfit sheet."*
    - **LUẬT CỨNG cho shot POV (`pov`, `pov_hand`, `wide`): KHÔNG gắn `<Vlogger>`, `<Vlogger> Body`, `<Vlogger> Outfit` vào `refs`/`character_names`.** Bằng chứng: H2 hỏng 3 lần liên tiếp theo cùng một kiểu. Prompt nói Nora ở sau camera, nhưng ảnh ref chứa mặt Nora. Model ưu tiên ảnh hơn chữ nên vẽ Nora vào khung. Vì prompt POV không có khối identity/outfit, model tự chọn áo parka sẫm, rồi diễn giải "holding it firmly" thành cầm điện thoại thấy rõ màn hình. Ảnh outfit cũng có mặt Nora (crop từ sheet nhân vật) nên vẫn kéo Nora vào khung. POV chỉ gắn ref của thứ cần thấy trong khung (động vật, đồ vật, người địa phương). Với `pov_hand`, tả tay áo bằng chữ trong lock (*"her bare empty hand… coming out of a cream suede sleeve with a thick white fox-fur cuff"*).
    - **Outfit lock trong `common.identity`:** Cập nhật `common.identity` trong `clips.json` để mô tả chi tiết màu sắc, chất liệu, phụ kiện của trang phục. Phải nêu rõ "NOT dark, NOT brown, NOT a parka" để ngăn model suy diễn.
    - **Outfit lock trong `video_prompt`:** Thêm `OUTFIT LOCK (CRITICAL)` vào mỗi `video_prompt` của cảnh có vlogger, nêu rõ màu chủ đạo (ví dụ: "WHITE/CREAM reindeer suede dress, NOT dark/brown coat").
    - **Lưu ý mannequin:** Nếu gen ảnh outfit mới bằng AI (mannequin display), ảnh sẽ KHÔNG khớp chính xác với outfit trong character ref vì AI tự diễn giải từ text. Phải luôn dùng crop từ character ref sheet thay vì gen mới.
    - **Lệnh crop chuẩn cho Nora Outfit ref** (chạy 1 lần khi setup project):
      ```bash
      ffmpeg -y -i "output/<slug>/refs/nora_clean.jpg" \
        -vf "crop=iw*2/3:ih:iw/3:0" \
        "output/<slug>/refs/nora_outfit_crop.jpg"
      # Kết quả: panel 3/4 + full-body từ nora_clean.jpg, không có face close-up
      # Upload rồi dùng làm media_id của entity "Nora Outfit"
      ```

    **[ICE AGE PROJECT] Nora — bộ 3 ref đã khóa:**
    - `Nora` ← `uploads/nora_main.jpg` (sheet mặt 4 góc, đã xóa logo → `refs/nora_main_clean.jpg`). Đây là ảnh nhân vật chính thức; KHÔNG dùng `nora_clean.jpg` làm ảnh mặt nữa.
    - `Nora Body` ← `refs/nora_body_v3_clean.jpg` (EDIT_CHARACTER_IMAGE từ nora_main + `uploads/nora_base_body_prompt.json` v3: khung cắt ngang vai, áo tank + quần bike ôm sát để thấy eo nhỏ, chân thon, ngực đầy; không có mặt).
    - `Nora Outfit` ← `refs/nora_outfit_crop.jpg` (crop từ `nora_clean.jpg`).
    - `refs` của mọi clip có Nora: `["Nora", "Nora Body", "Nora Outfit", ...]`.
    - **common.identity lock (dùng trong tất cả cảnh Nora xuất hiện):**
      ```
      Nora looks exactly like her three reference images: her face from the Nora face sheet
      (honey-blonde high ponytail with curtain bangs, grey-green eyes), her tall curvy hourglass build
      from the Nora Body sheet, and her clothing from the Nora Outfit sheet.
      OUTFIT LOCK (CRITICAL -- match the Nora Outfit reference image exactly):
      she wears a fitted WHITE/CREAM reindeer suede jacket-dress (mid-thigh length),
      deep plunging V neckline laced with thin leather ties and ivory beads along the edges,
      large white arctic-fox fur collar/hood framing the neckline,
      long sleeves with thick white fur cuffs,
      wide tan leather belt at waist sewn with rows of drilled ivory/bone teeth,
      the body of the dress is CREAM/OFF-WHITE suede -- NOT dark, NOT brown, NOT a parka.
      Light beige-white hide leggings (NOT dark/black).
      Knee-high suede cream boots with white fur cuff trim at the top.
      Small white fur mittens on a braided cord hanging at her sides.
      Every scene featuring Nora must show this exact costume.
      ```
    - **Inline OUTFIT LOCK cho video_prompt (thêm sau "No one else in the shot."):**
      ```
      OUTFIT LOCK (CRITICAL -- match Nora Outfit reference exactly):
      Nora wears a fitted WHITE/CREAM reindeer suede jacket-dress (mid-thigh length),
      deep V neckline laced with leather ties and ivory beads, large white arctic-fox fur collar,
      long sleeves with thick white fur cuffs, wide tan leather belt with bone teeth at waist,
      light beige-white hide leggings (NOT dark/black leggings),
      knee-high cream suede boots with white fur cuff trim,
      small white fur mittens on braided cord.
      This outfit is WHITE/CREAM throughout -- NOT a dark coat, NOT a brown parka, NOT modern clothing.
      ```

35. **CHẠY MÀ KHUNG HÌNH KHÔNG RUNG (bài học H1 Ice Age 16,000 BC bản v4 — người chạy hết sức nhưng mặt Nora và đường chân trời đứng yên như quay bằng gimbal):**
    - **Root-cause:** prompt chỉ ghi chung chung "the view bounces vertically with each footfall" một lần ở phần style. Model video mặc định ổn định hình (stabilize), nên một câu trừu tượng như vậy bị lờ đi. Chỉ chân và tay chuyển động, còn khung hình thì không.
    - **Fix: tả hiệu ứng rung NHÌN THẤY ĐƯỢC trên khung hình, có biên độ cụ thể, và nhắc lại trong TỪNG đoạn thời gian:**
      - Style `run` (bản đã sửa theo bài 36): *"Raw unstabilized footage: because the lens is in Nora's own outstretched right hand, every stride she takes jolts the whole frame — her face jumps up and down by about a tenth of the frame height and the horizon behind her tilts a few degrees left and right, with a brief motion blur on each footfall, while her face always stays in the frame."*
      - Mỗi segment `0-3s / 3-6s / 6-8s` của shot chạy phải có một cụm rung riêng, **gắn vào tay vlogger**, ví dụ *"her outstretched arm jolting the frame hard on every stride"*, *"the horizon swinging left and right with each footfall"*.
      - Không dùng các từ làm model ổn định hình: `smooth`, `steady`, `stable`, `cinematic tracking`.
    - **Mức rung theo hành động** (rung phải khớp nhịp chân): đi bộ → nảy nhẹ, chân trời nghiêng ≤2°. Chạy bộ → mặt nhảy ~5% chiều cao khung. Chạy thục mạng hoặc vấp → mặt nhảy ~10%, chân trời nghiêng 3–5°, nhòe chuyển động mỗi bước. Trượt, ngã → khung xoay mạnh. Với shot selfie, mặt vlogger luôn nằm trong khung; không tả "khung trôi khỏi mặt rồi giật về" (xem bài 36).
    - **Review:** khi xem contact sheet, so vị trí mặt và đường chân trời giữa các khung liền nhau. Nếu gần như không đổi trong lúc nhân vật đang chạy thì trừ điểm Motion Quality và sửa prompt theo mẫu trên.

36. **TẢ RUNG NHƯ MỘT CAMERA ĐỘC LẬP LÀM MẤT GÓC SELFIE (bài học H1 Ice Age v5 — v4 giữ selfie đủ 8 giây, v5 thành người ngoài chạy giật lùi quay theo, cả hai tay Nora đều đánh):**
    - **Root-cause:** thay đổi duy nhất giữa v4 và v5 là câu rung *"the framing drifts off her face and snaps back"* cùng cụm *"the framing lurching and snapping back"* trong từng segment. Câu này mô tả khung hình có chuyển động riêng, tách khỏi cơ thể Nora, nên model hiểu là có một người quay riêng và dựng thành tracking shot. (Mới có một mẫu so sánh, nhưng đây là thay đổi duy nhất.)
    - **Fix:** mọi mô tả rung trong shot selfie/run phải nêu **nguyên nhân là tay của chính vlogger**: *"because the lens is in Nora's own outstretched right hand, every stride she takes jolts the whole frame … while her face always stays in the frame"*. Segment dùng *"her outstretched arm jolting the frame"*, không dùng "the framing lurches / drifts / snaps back".
    - **Kiểm tra trước khi gen:** grep prompt shot `run`/`selfie`; không được có `framing (drifts|lurch|snaps)`.

37. **SHOT POV TẢ HÀNH ĐỘNG CỦA NGƯỜI QUAY → MODEL VẼ NGƯỜI ĐÓ TỪ BÊN NGOÀI (bài học H2 Ice Age v5 — cuối clip thấy một người mặc đồ sẫm lăn xuống dốc ở góc người thứ ba):**
    - **Root-cause:** segment ghi *"the camera pitches down sharply as Nora slides over the lip"*. "Nora slides" là hành động cơ thể có chủ ngữ là người, nên model dựng hình người đó trượt. Prompt POV không gắn ref Nora, nên model tự bịa ra một người mặc đồ sẫm.
    - **Fix:** trong shot `pov`/`wide`, chủ ngữ chỉ được là **góc nhìn hoặc khung hình** ("the view tips forward and drops over the lip, sliding fast down the snowy slope, snow spraying across the frame"), không bao giờ là "Nora …". Riêng `pov_hand` được tả bàn tay ("Nora's bare hand lifts…") vì tay có trong khung.
    - **Không dùng phủ định để chặn người** ("no person is seen", "no face, no body"): phủ định vẫn gọi tên đối tượng (cùng cơ chế với bài 33). Viết câu khẳng định: *"only snow, sky and the slope fill the frame"*, *"only the world in front of her fills the frame"*.
    - Đã sửa cùng lỗi ở S30 (cũng "Nora slides over the lip") và S49 ("whips back down toward Nora" trong shot wide → "toward the firelit camp").
    - **Kiểm tra trước khi gen:** với clip `pov`/`wide`, grep segment; không được có `\bNora\b` ngoài "Nora says".

38. **SHOT POV BỊ NGƯỜI LẠ CHIẾM KHUNG — "OVER THE SHOULDER" VÀ "FROM BEHIND THE CAMERA" (bài học H2 Ice Age v6 — 2.5 giây đầu quay qua vai một phụ nữ lạ tóc nâu tết, áo parka sẫm, không phải Nora):**
    - **Root-cause:** trường `shot` ghi *"first looking back over the shoulder"*. Với model video, "over the shoulder" là thuật ngữ góc máy chuẩn: quay qua vai một người đang đứng trong khung. Model dựng đúng nghĩa đen. Vì cảnh POV không gắn ref vlogger, model bịa ra một người lạ. Thêm nữa, lời thoại gắn dạng *"Nora says from behind the camera"* ngầm báo có một người quay đứng sau máy, càng kéo model vẽ người. Đoạn cuối *"sliding fast down the slope"* là hành động của cơ thể, nên vẫn ra một người lăn.
    - **Fix:**
      - Không dùng thuật ngữ góc máy có người trong đó (`over the shoulder`, `OTS`, `two-shot`, `behind her`) cho shot POV. Viết theo chuyển động của góc nhìn: *"the view swings round to face backward toward the mammoth, then swings forward to the riverbank edge"*.
      - Lời thoại POV/wide gắn dạng **`Nora's off-screen voice says, …:`**, không dùng "from behind the camera".
      - Rơi hoặc trượt trong POV thì tả mặt đất lao về phía ống kính: *"the view tips forward over the lip and the snowy slope rushes up toward the lens, snow spraying across the frame until it turns white"*. Không dùng "sliding", "tumbling", "falling" (động từ của cơ thể).
    - **Kiểm tra trước khi gen:** clip `pov`/`wide` không được có `over the shoulder|from behind the camera|\b(sliding|tumbling|falling)\b` trong `shot` và segment.
    - **Trạng thái:** fix đã áp vào `clips.json` nhưng chưa gen kiểm chứng (hết credit ngày 2026-10-02). Gen xong phải ghi kết quả vào đây.

39. **NHẢY HOẶC TIẾP ĐẤT TRONG SHOT SELFIE DỄ BỊ BUÔNG MÁY → CHUYỂN GÓC THỨ BA (bài học H2 Ice Age 16,000 BC bản v7):**
    - **Root-cause:** Khi mô tả nhân vật nhảy hoặc trượt qua gờ dốc ("Nora reaches the edge and leaps, sliding feet-first..."), model video AI (Omni Flash / Veo) ưu tiên mô tả hành động cơ thể tiếp đất tự nhiên (người nhảy phải vung hai tay giữ thăng bằng), dẫn đến việc model "buông điện thoại", lùi camera ra ngoài thành góc người thứ 3 (third-person spectator wide shot) hoặc vẽ Nora chạy ra xa máy.
    - **Fix:**
      - **Khóa cứng cánh tay và máy quay (Permanent Arm & Camera Lock):** Trong shot selfie có động tác nhảy/rơi/trượt, bắt buộc tả rõ cánh tay vlogger luôn duỗi thẳng và nắm chặt máy hướng về mặt mình: *"Nora plunges downward over the icy lip, her right arm remaining permanently extended gripping the camera tightly aimed directly back at her screaming face; she NEVER drops, releases, or lets go of the camera, and the view NEVER switches to third-person or spectator angle."*
      - **Tả chuyển động khung hình và tuyết thay vì tả chuyển động toàn thân:** Khung hình rung giật dọc theo quán tính cú rơi (`view jerks violently downward with the sudden drop`), tuyết bắn mù mịt xung quanh bờ vực, nhưng khuôn mặt vlogger luôn neo chặt ở trung tâm khung hình selfie.
    - **Kiểm tra trước khi gen:** Trong shot selfie có hành động nhảy/rơi/trượt (`leap`, `slide`, `jump`, `fall`): Bắt buộc phải có mệnh đề khẳng định: `her [right/left] arm remains extended pointing the camera at her face, NEVER drops or lets go of the camera, view never switches to third-person`.
    - **Bằng chứng thực nghiệm:** H2 bản v8 (media `665ccebc-ec01-406a-88cd-55aaefc9643b`) giữ góc selfie 100% từ 0s đến 6s, Nora vừa trượt dốc tuyết vừa la hét trực tiếp vào ống kính, cánh tay vươn dài giữ chắc máy, hoàn toàn không chuyển góc thứ 3.

40. **BODY DRIFT KHI DÙNG VÁY MANNEQUIN VÀ THỨ TỰ TRUYỀN REF TRONG R2V INGREDIENTS (bài học H1/H2 Ice Age 16,000 BC bản v7):**
    - **Root-cause:**
      1. Ảnh Outfit tạo trên manocanh (mannequin display) có phom người thon gọn, thẳng đuột tiêu chuẩn. Khi đưa vào R2V ingredients cùng với ảnh Body đồng hồ cát, model video AI có xu hướng bị phom dáng mảnh khảnh của manocanh làm lấn át (body drift), khiến nhân vật trong video bị phẳng ngực và mất đường cong eo-hông dù prompt có ghi "hourglass build".
      2. Thứ tự ref gửi lên server: Nếu entity Outfit được gửi trước entity Body, model sẽ dựng phom áo trước khi gán tỉ lệ cơ thể.
    - **Fix:**
      - **Bảo toàn thứ tự truyền Ref theo chuỗi nhận diện:** Server (`agent/sdk/services/operations.py`) bắt buộc bảo toàn thứ tự entities khai báo trong `character_names`: `[Face] -> [Body] -> [Outfit]` (ví dụ: `["Nora", "Nora Body", "Nora Outfit"]`). Nhờ đó, model cố định tỉ lệ giải phẫu cơ thể trước, sau đó mới khoác lớp trang phục lên.
      - **Manocanh không đầu (Headless Mannequin):** Ảnh trang phục manocanh BẮT BUỘC là manocanh không đầu trên nền studio trung tính, chụp 3 góc (chính diện, 3/4, sau lưng); tuyệt đối không có tóc giả hay mặt người giả để tránh xung đột nhận diện khuôn mặt.
      - **Khóa tương phản giải phẫu cơ thể (Negative Contrast Constraints) trong Prompt:** Trong `common.identity` và `video_prompt`, phải có cụm từ tương phản đối kháng mạnh mẽ ép model tuân thủ ảnh Body: *"BODY LOCK (CRITICAL): Nora has a voluptuous hourglass figure with a large full heavy natural bust, tiny narrow waist, and wide curvaceous hips matching Nora Body reference; she is NOT skinny, NOT slender, NOT petite, NOT flat-chested, and her deep neckline proudly showcases her cleavage."*
    - **Bằng chứng thực nghiệm:** H1 (media `81b3bf5f`) và H2 (media `665ccebc`) bản v8 thể hiện chuẩn xác vóc dáng đồng hồ cát nóng bỏng với vòng 1 đầy đặn và váy slip dress lụa trắng xẻ ngực sâu trùng khớp hoàn toàn với ảnh `thumbnail_v2_2k_clean.jpg` và `nora_body_v3_clean.jpg`.

41. **LOCK BODY, TÔN DÁNG VÒNG 1 (PUSH-UP CLEAVAGE), CHÂN DÀI SIÊU MẪU & QUY TẮC VIẾT PROMPT (bài học H1/H2 Ice Age 16,000 BC bản v9):**
    - **Hiện tượng & Root-causes khiến vòng 1 trông nhỏ và chân bị ngắn trong video:**
      1. *Ảnh Body Ref bị nén thể thao:* Người mẫu trong ảnh Body thường mặc áo tank top thể thao bó sát (compression tank), khiến mô ngực bị nén phẳng chặt vào lồng ngực (cỡ C-cup thể thao tự nhiên) và tỉ lệ thân/chân 1:1, không có gọng đẩy ngực (push-up) hay khe ngực sâu như trong ảnh thumbnail.
      2. *Động tác chạy mở rộng lồng ngực:* Khi vlogger chạy thục mạng một tay vươn cầm máy và một tay vung ra sau, lồng ngực mở rộng kéo dạt hai bầu ngực sang hai bên nách, không thể chụm lại tạo khe ngực sâu như lúc đứng yên khoanh tay (trong ảnh thumbnail).
      3. *Hiệu ứng co ngắn phối cảnh góc rộng (Foreshortening) của ống kính 0.5x:* Khi cầm máy ngang mặt chúc xuống, phần đầu/mặt ở gần ống kính nhất sẽ bị phóng to (magnified), trong khi phần hông/đùi/chân ở xa trục camera sẽ bị hút nhỏ và co ngắn lại (foreshortening). Người chạy chúi thân trên về phía trước càng làm chân bị lùi sâu vào hậu cảnh.
      4. *Vị trí khối BODY LOCK bị chôn vùi cuối prompt (Attention Decay):* Trong prompt dài 5.000–6.000 ký tự, nếu để khối BODY LOCK ở vị trí thứ 8 sau 3.500 ký tự (sau style, setting, timed segments, physics...), model AI bị phân tán sự chú ý và ưu tiên mô phỏng chuyển động trước khi áp hình thể nhân vật.
    - **Bộ giải pháp chuẩn khi viết Prompt (BẮT BUỘC ÁP DỤNG MỌI CẢNH):**
      - **1. Kiến trúc Prompt đưa Body Lock lên SỚM (Early Conditioning):**
        Đưa khối `Identity & Body Lock` lên vị trí **ngay sau `Shot:`**, TRƯỚC các phân đoạn hành động `0-3s`, `3-6s`. Cấu trúc chuẩn: `[Style] -> [Setting & Light] -> [Shot] -> [Identity & Body Lock (Face + Body + Outfit)] -> [Timed Segments] -> [Background] -> [Physics] -> [Lock] -> [General] -> [Audio]`. Model AI sẽ định hình lưới giải phẫu và trang phục trước khi render động tác.
      - **2. Cụm từ khóa đấm lực vòng 1 (Push-up Cleavage Punch):**
        TUYỆT ĐỐI CẤM các từ gây xệ hoặc phẳng ngực (`low-hanging bust`, `natural bust compression`). BẮT BUỘC dùng cụm khẳng định đối kháng cực mạnh:
        *"BODY LOCK (CRITICAL): [Character] has an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage), a dramatically tiny narrow cinched waist, and wide curvaceous hips; she is distinctly voluptuous, curvy, and busty -- NOT flat-chested, NOT small-busted, NOT skinny, NOT slender."*
      - **3. Cụm từ khóa chân dài & chiều cao siêu mẫu (Statuesque Legs Punch):**
        CẤM dùng "thick thighs" đơn độc làm chân trông ngắn và mập. Bổ sung thông số chuẩn:
        *"STATURE & LEGS: [Character] is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an elongated tall athletic silhouette -- NOT short, NOT stubby, NOT stocky."*
      - **4. Quang học góc máy tôn dáng (Optical Angle — Low-Angle Chest Level):**
        Trong `style.run` và `style.selfie`, điều chỉnh vị trí đặt máy:
        *"The lens sits at the end of [Character]'s outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at [Character]; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height."*
        Góc máy từ ngực/bụng hất nhẹ lên loại bỏ hiện tượng to đầu - ngắn chân, khoe trọn khe ngực và kéo dài đôi chân.
      - **5. Nhúng đặc điểm thể hình trực tiếp vào chuyển động (Action-Segment Reinforcement):**
        Trong từng phân đoạn `0-3s`, `3-6s`, lặp lại trực tiếp:
        *"...her tall statuesque frame and long slender legs pumping powerfully through the snow; her exceptionally large, voluptuous full bust bounces with dramatic push-up cleavage prominently spilling out of the deep plunging neckline of her snug white silk slip dress; her tiny cinched waist and wide curvy hips accentuated..."*
    - **Bằng chứng thực nghiệm:** H1 (`2f001786`) và H2 (`287f5bf5`) bản v9: góc máy hất nhẹ lên khoe trọn đôi chân dài miên man đang sải bước trong tuyết, khe ngực sâu push-up căng đầy bốc lửa trong chiếc váy lụa trắng xẻ sâu, điểm số AI Review Scorecard đạt 95.5 và 97.0 / 100.

42. **BỘ TỨ NGUYÊN LÝ VẬT LÝ SINH TỒN & ĐIỂM MÙ QUANG HỌC POV VLOG (bài học H2 Ice Age 16,000 BC bản v10):**
    
    #### 1. Nguyên lý Động lượng & Quán tính cơ học ($p = m \cdot v$)
    - **Lỗi AI thường gặp ("Nhìn giả như AI"):**
      - Khi prompt mô tả: *"Nora lao mình nhảy xuống bờ sông trong khi tay vẫn giơ máy quay"*, AI sẽ hiểu theo kiểu phim hoạt hình hoặc video game: nhân vật bay lơ lửng giữa không trung (anti-gravity), cơ thể đơ cứng, không có trọng lực.
    - **Vật lý con người thực tế:**
      - Nora có khối lượng $m \approx 55\text{ kg}$, đang chạy nước rút với vận tốc $v \approx 6\text{ m/s}$ ➔ Động lượng $p = m \cdot v$ cực lớn.
      - Khi gót giày vấp phải rãnh băng (hệ số ma sát $\mu \to 0$): Chân dừng/trượt đột ngột, nhưng phần thân trên mang toàn bộ quán tính lao về phía trước.
      - Trọng tâm cơ thể (Center of Mass) vượt khỏi chân đế. Con người không thể bay, mà bắt buộc phải trải qua chuỗi phản xạ sinh học:
        1. *Loạng choạng quán tính:* Chân bước vội 1–2 bước ngắn trong tuyệt vọng để cứu thăng bằng.
        2. *Mất mômen xoắn:* Cánh tay tự do quơ loạn xạ trong không khí để tìm thăng bằng.
        3. *Sụp đổ trọng lực:* Lực hấp dẫn $F_g = mg$ kéo sụp cơ thể, ngã đập mạnh hông và đầu gối xuống mặt băng tuyết với xung lực nén lún rõ rệt.

    #### 2. Nguyên lý Tương phản Trọng tải trên Sườn dốc ($m_{\text{voi}} \gg m_{\text{người}}$)
    - **Tại sao ngã trên mặt đất bằng phẳng là sai logic vật lý & sinh tồn?**
      - Nếu ngã trên thảo nguyên bằng phẳng ngay trước mũi voi ma mút: Con voi 6 tấn với đà chạy khủng khiếp sẽ giẫm bẹp vlogger trong 0.5 giây! Cảnh quay trở nên hoàn toàn vô lý.
    - **Vật lý địa hình sườn dốc bờ sông băng ($\theta \approx 45^\circ - 60^\circ$):**
      - Bờ dốc sông băng là một mặt phẳng nghiêng có tuyết dày. Thành phần trọng lực dọc theo sườn dốc $F = mg\sin\theta$ thắng lực ma sát trượt của tuyết $F_{\text{friction}} = \mu mg\cos\theta$, biến cú ngã thành cú trượt cày dốc tuyết (Kinetic Slope Slide).
    - **Sự tương phản trọng lượng quyết định sinh tử:**
      - *Nora (55 kg):* Nhẹ, trượt cày trên lớp tuyết xốp dày xuống đáy thung lũng sông băng an toàn giống như vận động viên trượt tuyết (lớp tuyết đóng vai trò đệm giảm chấn hấp thụ động năng).
      - *Voi ma mút (6.000 kg — gấp hơn 100 lần):* Khối lượng quá khủng khiếp khiến nó không thể lao xuống sườn dốc băng tuyết trơn trượt vì sẽ gây sạt lở tuyết, gãy chân hoặc lăn đè bẹp chính nó!
      - ➔ **Chính định luật vật lý về trọng tải đã giải thích tại sao Nora sống sót và tại sao con voi ma mút bắt buộc phải phanh khựng lại trên đỉnh mép dốc!**

    #### 3. Nguyên lý Động học Camera & Điểm mù Quang học (Optical Viewpoint)
    - **Hiện tượng "Điện thoại ma" (Ghost Phone) dưới góc nhìn vật lý AI:**
      - Khi trong prompt xuất hiện từ `phone`, `smartphone`, `screen`, `device`, `selfie stick` (ngay cả trong câu cấm *"she never drops the phone"*), model AI hiểu rằng có một vật thể vật lý 3D mang tên "chiếc điện thoại" cần xuất hiện trong khung hình. Thế là nó vẽ chiếc iPhone trên tay Nora và tự động đặt một camera thứ ba lùi ra xa để quay cảnh đó!
    - **Vật lý quang học chân thực của POV Vlog:**
      - Bản thân người xem đang nhìn **XUYÊN QUA ỐNG KÍNH MÁY QUAY**.
      - Cánh tay phải giơ ra giữ ống kính, nghĩa là **thân máy và bàn tay cầm máy nằm ở PHÍA SAU MẶT PHẲNG TIÊU CỰ (Behind the focal plane / Off-screen)**, quang học tự nhiên không thể nào chụp được chính cái máy đang quay nó!
      - **Đặc tả đúng kỹ thuật:**
        `Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective. The lens sits at the end of [Character]'s outstretched right arm, held at chest level angled slightly upward; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen; her free left hand is completely empty and flails naturally for balance.`
      - **TUYỆT ĐỐI CẤM 100% các từ:** `phone`, `smartphone`, `screen`, `device`, `selfie stick` trong toàn bộ prompt.
    - **Động học chấn động (Kinematic Shockwave):**
      - Khi thân người đập xuống tuyết và trượt dốc, cánh tay có khớp vai và cơ bắp chịu chấn động gián tiếp: khung hình phải rung giật cực mạnh chúc xuống mặt tuyết (`rotational jolt & downward shockwave`), tuyết bột bắn tung tóe dính vào mặt kính thấu kính (`powder snow coats the lens glass`) làm mờ nhòe tự nhiên (whiteout transition).

    #### 4. Nguyên lý Biến dạng Vật liệu & Triệt tiêu Động năng (Energy Dissipation)
    - **Tuyết Kỷ Băng Hà không phải là mặt sàn bê tông cứng:**
      - *Nứt nén bề mặt (Crust Fracture):* Khi gót chân vấp và thân người đập xuống, lớp váng băng mỏng trên bề mặt nứt vỡ rạn chân chim.
      - *Bụi tuyết khí dung (Aerosolized Powder Snow):* Lực va chạm nén không khí, hất tung lớp tuyết bột xốp bên dưới thành đám mây bụi trắng xóa quanh người.
      - *Rãnh ma sát (Frictional Furrow):* Cơ thể cày một vệt lõm sâu trên sườn dốc, ma sát tuyết triệt tiêu dần toàn bộ động năng $\frac{1}{2}mv^2 \to Q$ cho đến khi người dừng hẳn lại ở bãi tuyết chân dốc.

    #### 5. Quy trình BẮT BUỘC: Prompt Self-Linter (Tự kiểm tra prompt sau khi viết xong)
    - Sau khi soạn thảo bất kỳ prompt nào (trước khi lưu DB, `clips.json` hoặc gửi API gen media), Agent BẮT BUỘC phải chạy công cụ kiểm tra tự động (`python tools/lint_prompt.py`):
      1. Quét regex cấm `\b(phone|smartphone|screen|device|selfie[- ]?stick)\b`. Nếu có, lập tức loại bỏ.
      2. Kiểm tra câu điểm mù quang học (`off-screen`, `outside the visible frame`).
      3. Kiểm tra vị trí `BODY LOCK` (phải đặt SỚM ngay sau `Shot:` trước `0-3s`).
    - **Bằng chứng thực nghiệm:** H2 Ice Age 16,000 BC bản v10 loại bỏ 100% từ "phone", camera giữ góc POV selfie hoàn hảo, tuyết phủ mặt kính chuyển cảnh mượt mà, không còn bất kỳ chiếc điện thoại ma nào xuất hiện trong khung hình.

43. **LỖI "VẬT THỂ HÓA MÁY ẢNH" & XUNG ĐỘT GÓC NHÌN NGƯỜI THỨ BA (Camera Prop Glitch & Third-Person POV Conflict — Bài học Scene 04 Ice Age 16,000 BC):**
    
    #### 1. Hiện tượng lỗi thực tế
    - Trong Scene 04 của Ice Age 16,000 BC, ở giây thứ 1, AI vẽ Nora đứng quay lưng lại, trên tay cầm một chiếc **máy ảnh compact kỹ thuật số có màn hình LCD** chĩa vào thợ săn Torak. Đến giây thứ 5 khi cô xoay tay lại để selfie, chiếc máy ảnh biến dạng thành một **ống kính máy ảnh rời (DSLR Lens)** to đùng trên tay Nora giơ ra trước mặt khán giả.
    
    #### 2. Root Cause (Nguyên nhân gốc rễ)
    - **Xung đột góc nhìn chết người (Third-Person vs POV):**
      - Prompt mô tả: *"Handheld vlog footage that starts from Nora's raised hand just behind her head and then turns around to face her... Shot: From just behind Nora's head, then turning around to a selfie."*
      - Khi camera đặt ở phía sau đầu / sau lưng vlogger nhìn tới (`from just behind Nora's head`), đây là **GÓC NHÌN NGƯỜI THỨ BA (Third-person spectator)**. Khán giả đứng ngoài nhìn thấy toàn bộ lưng và cánh tay của Nora.
      - AI model lập luận logic: *"Người xem đang đứng sau lưng quay cảnh Nora và Torak, vậy vật thể mà tay Nora đang giơ lên là cái gì?"* ➔ AI bắt buộc phải vật thể hóa thành một **chiếc máy ảnh kỹ thuật số (Compact Camera / LCD screen)** trong tay nhân vật!
    - **Lỗi ngữ nghĩa từ "Camera" như một Đạo cụ (Prop):**
      - Mặc dù đã cấm `phone/smartphone`, prompt lại dùng từ `camera` tới 5 lần như tân ngữ của hành động: *"starts from Nora's raised hand... Nora slowly brings the camera around... she never lets go of the camera..."*.
      - Trong góc nhìn người thứ ba, AI hiểu "the camera" là một **đạo cụ vật lý (prop)** cầm tay chứ không phải ống kính của chính người xem. Khi Nora xoay tay lại, AI tiếp tục giữ góc nhìn người xem ở ngoài và vẽ một **ống kính máy ảnh rời (DSLR Lens)** trong tay Nora!
    - **AI Video không thể tự "chui vào mắt" vlogger:**
      - AI diffusion model không thể chuyển đổi mượt mà giữa camera thứ 3 (sau lưng) và camera thứ 1 (POV cầm tay) trong cùng một chuỗi khung hình liên tục mà không sinh ra thiết bị quay thứ hai.

    #### 3. Quy tắc & Giải pháp Khắc phục Triệt để
    - **1. TUYỆT ĐỐI CẤM các shot quay từ sau đầu / sau lưng vlogger rồi xoay ra trước mặt:**
      - CẤM: `from just behind her head`, `from behind her back`, `over her shoulder from behind then turning`.
    - **2. Kỹ thuật Đơn góc nhìn thuần khiết (Single-Perspective Vlog Purity — THAY THẾ Whip Pan 180°):**
      - *Lưu ý quan trọng (Đã lỗi thời):* Cú lia máy Whip Pan 180° trong 1 clip trước đây từng được thử nghiệm để loại bỏ đạo cụ máy ảnh ma, nhưng đã bị bãi bỏ vì gây cảm giác phi lý (quay cam trước lật cam sau thì mù màn hình, camera bay như có người thứ ba; xem chi tiết Bài học 44).
      - **Giải pháp chuẩn:** Khi vlogger muốn tương tác với đối tượng phía sau hoặc cảnh vật:
        - **Bản đề xuất 100% Selfie Tự Nhiên (Over-the-Shoulder Selfie Interaction):** Toàn bộ shot 8s–10s giữ 100% cam trước Selfie 0.5x. Vlogger ở 1/3 tiền cảnh, đối tượng ở 2/3 hậu cảnh. Tương tác qua ánh mắt và quay đầu, camera luôn cố định vào vlogger, loại bỏ hoàn toàn cảm giác xoay lật giả tạo.
        - **Hoặc Cặp Shot Kép (Two Separate Shots):** Shot 1 (100% POV Cam sau) nhìn qua mắt vlogger ➔ Cắt cảnh (Cut) sang Shot 2 (100% Selfie Cam trước) vlogger nói chuyện. Không xoay 180° trong cùng 1 clip.
    - **3. Không bao giờ mô tả nhân vật "cầm/xoay the camera" như một vật thể:**
      - Thay câu *"she brings the camera around"* bằng *"she pivots her extended arm back toward herself"*.
      - Điểm nhìn người xem chính là thấu kính (`The viewer looks directly through the camera lens`).
    - **4. Tự động kiểm tra qua Prompt Self-Linter:**
      - Linter BẮT BUỘC quét và chặn các cụm từ: `behind (her|his|their) head`, `behind (her|his|their) back`, và cảnh báo hành động cầm nắm `camera` làm đạo cụ.

44. **LỖI LẬT XOAY CAMERA 180° GIỮA CAM TRƯỚC & CAM SAU TRONG CÙNG MỘT SHOT (The 180° Camera Flip Fallacy & Single-Perspective Vlog Purity — Bài học Scene 04 Ice Age 16,000 BC bản v2):**
    
    #### 1. Hiện tượng lỗi thực tế
    - Dù đã loại bỏ được chiếc máy ảnh/ống kính ma bằng kỹ thuật Whip Pan 180° (Two-Phase POV), nhưng khi xem video thực tế, người xem lập tức cảm thấy **vô lý, giả tạo và phi logic** khi camera đang quay góc nhìn thứ nhất (cam sau nhìn Torak ở 0-3s) rồi đột ngột xoay lật 180° chuyển sang góc selfie (cam trước ở 4-10s) trong cùng một shot 10 giây.
    
    #### 2. Root Cause (Nguyên nhân gốc rễ)
    - **Nghịch lý công thái học điện thoại (Smartphone Ergonomics Fallacy):**
      - Trong thực tế, khi cầm điện thoại quay vlog:
        - Nếu bạn đang quay cam sau (quay người khác/cảnh vật), rồi lật ngược điện thoại 180° lại để tự quay mình, thì màn hình điện thoại sẽ quay ra phía trước! Người quay bị hoàn toàn mù màn hình, không thể nhìn thấy khung hình, biểu cảm hay kiểm tra người đứng sau lưng.
        - Nếu dùng tính năng chuyển cam trên màn hình (flip camera button), ứng dụng luôn tạo ra một cú **CẮT CẢNH (Cut shot)**, chứ không bao giờ lia xoay vật lý 180° trong không gian.
    - **Nghịch lý động học không gian (Spatial Kinematics & Fake Cameraman Feel):**
      - Ở 3 giây đầu, điểm nhìn camera nằm ở ngang tầm mắt người quay (cam sau). Đến giây thứ 5, camera bỗng nhiên nằm ở trước mặt vlogger cách 60cm nhìn ngược lại.
      - Cú xoay này đòi hỏi camera phải tự bay một vòng quỹ đạo bán kính lớn trong không khí, tạo cảm giác như **có một người quay phim thứ ba (cameraman cầm gimbal/flycam)** chạy vòng quanh vlogger, phá hủy hoàn toàn cảm giác "vlogger đơn độc tự cầm máy sinh tồn".
    - **Gãy mạch thị giác (Visual Continuity Breakdown):**
      - Scene 03 là góc Selfie cam trước. Scene 05 là góc Selfie cam trước. Việc Scene 04 bị chèn một đoạn cam sau rồi xoay lật làm vỡ nhịp điệu thị giác và tính nhất quán của chuỗi vlog.
    
    #### 3. Quy tắc Vàng: Đơn góc nhìn thuần khiết & Selfie qua vai (Single-Perspective Vlog Purity & Over-the-Shoulder Vlog Composition)
    - **Quy tắc tuyệt đối: 1 SHOT = 1 GÓC NHÌN DUY NHẤT (Single Perspective per Shot):**
      - Mỗi shot 8s–10s chỉ được chọn MỘT trong hai góc nhìn:
        - Hoặc là **100% Selfie (Cam trước 0.5x)** từ đầu đến cuối clip.
        - Hoặc là **100% First-Person POV (Cam sau)** từ đầu đến cuối clip.
      - **TUYỆT ĐỐI CẤM** xoay lật 180° giữa cam trước và cam sau trong cùng một shot (`whip pan 180-degree ... turning to face`, `pivoting the viewpoint back`).
    - **Kỹ thuật Vlog Selfie qua vai (Over-the-Shoulder Selfie Interaction):**
      - Khi vlogger muốn giao tiếp hoặc phản ứng với một nhân vật phụ / sinh vật xuất hiện:
        1. **Bố cục 1/3 tiền cảnh (Vlogger in Foreground 1/3):** Vlogger cầm máy ở góc selfie 0.5x (bên trái hoặc bên phải), chiếm 1/3 khung hình. Tay cầm máy nằm ngoài điểm mù (`outside the visible frame`).
        2. **Nhân vật phụ ở 2/3 hậu cảnh (Subject in Background 2/3):** Nhân vật phụ (như Torak, thổ dân, quái thú) xuất hiện ở 2/3 khung hình còn lại, nhìn thấy rõ hành động bước tới, cử chỉ hoặc hiệu lệnh săn bắn ngay phía sau vai vlogger.
        3. **Tương tác đa chiều bằng ánh mắt & quay đầu (Gaze & Head Turns, NOT Camera Flips):**
           - Vlogger nói trực tiếp với khán giả qua ống kính: *"Okay, that's Torak. My name for him."*
           - Vlogger khẽ quay đầu hoặc liếc mắt ra sau kiểm tra đối tượng khi đối tượng hành động (giơ tay dừng, giơ giáo): *"Hand flat, palm down, probably means stay. I stay."*
           - Vlogger quay lại nhìn thẳng vào camera thể hiện cảm xúc chân thật (lo lắng, cười gượng, thì thầm): *"A stranger walking into a winter camp? I'd spear me too."*
        ➔ Camera luôn neo cố định vào vlogger, chuyển động chỉ là rung lắc bước chân tự nhiên (`subtle hand shake / footfall bounce`), tạo cảm giác chân thực 100% như vlog YouTube/TikTok đời thực!
    
45. **LỖI GÃY MẠCH TƯ THẾ ĐẦU KHI CẮT NỐI HAI SHOT & KỸ THUẬT KHỚP ĐỘNG TÁC (The Inter-Scene Posture Snap & Head-Turn Match Continuity — Bài học Scene 03 -> Scene 04 Ice Age 16,000 BC):**
    
    #### 1. Hiện tượng lỗi thực tế
    - Scene 03 kết thúc ở 5-6s: Nora quay ngoắt đầu sang phải nhìn lều xương voi Mezhyrich (`At 5s she turns her head to look back at the camp, so the back of her head and ponytail fill half the frame`).
    - Nhưng Scene 04 mở đầu ở 0-3s: Prompt lại mô tả ngay Nora cầm máy nhìn thẳng vào ống kính camera thì thầm (`Nora holds the camera firmly in front-facing selfie at arm's length; she glances directly into the lens whispering nervously`).
    - **Hậu quả**: Khi nối Scene 03 và Scene 04, đầu của Nora bị giật 90 độ ngay lập tức từ quay gáy sang nhìn chính diện (Spatial Snap / Disorienting Jump Cut). Khán giả cảm thấy video bị sượng, đứt gãy mạch chuyển động và mất tính liên tục.
    
    #### 2. Root Cause (Nguyên nhân gốc rễ)
    - Do mỗi clip AI diffusion sinh độc lập, AI không có bộ nhớ tư thế khung hình cuối của clip trước. Nếu prompt của clip B không neo rõ tư thế mở đầu khớp với tư thế kết thúc của clip A, AI sẽ tự động sinh nhân vật ở tư thế cơ bản (đứng thẳng nhìn vào camera).
    - Cắt giữa 2 shot cùng cự ly (Medium Close-Up Selfie) mà tư thế đầu bị nhảy đột ngột là vi phạm quy tắc 30 độ trong dựng phim.
    
    #### 3. Quy tắc Vàng: Khớp Động Tác Liền Mạch (Match on Action / Head-Turn Continuity)
    - **Quy tắc bắt buộc khi nối 2 shot liền kề:**
      1. **Neo tư thế mở đầu ở 0-1s / 0-2s**: Clip B BẮT BUỘC phải mở đầu ở đúng tư thế kết thúc của Clip A (`0-2s: Matching the previous scene's ending, the clip opens with [Character]'s head turned looking back over her shoulder toward [Object]...`).
      2. **Thực hiện động tác chuyển đổi in-camera**: Trong chính 1-2 giây đầu của Clip B, mô tả nhân vật phát hiện đối tượng hoặc nghe thấy tiếng động, sau đó mới xoay mặt lại nhìn vào ống kính camera (`Seeing him emerge, her eyes widen and she smoothly turns her head back around to face directly into the camera lens`).
      3. **Tác dụng kỳ diệu**: Mối nối giữa Clip A và Clip B trở thành một cú cắt **Match on Action**. Khán giả nhìn thấy động tác quay đầu diễn ra mượt mà và tự nhiên, hoàn toàn triệt tiêu cảm giác giật hình (jump cut) của AI!
    
    > **Quy ước:** mỗi lỗi gen lặp lại được ghi thành MỘT bài học đánh số riêng ở đây, gồm root-cause, câu prompt sửa cụ thể và bằng chứng (clip nào, bản nào), để lần sau rút kinh nghiệm thay vì sửa lại từ đầu.

**Nội dung**
17. Vlogger mặc đồ hiện đại theo ảnh ref là chấp nhận được (mục 2).
18. User có thể yêu cầu **cảnh mở đầu FPV điện ảnh** (từ không gian lao xuống toàn cảnh thành phố, không có vlogger), là ngoại lệ của luật "mọi shot quay bằng điện thoại". Clip đó dùng ảnh ref toàn cảnh, giữ yên 2–3 giây cuối, và clip sau mở bằng vật lướt qua ống kính để che cú cắt.

---

## 📊 BẰNG CHỨNG THỰC NGHIỆM (Reference Video Analysis)

Khung kịch bản và tỉ lệ shot ở trên không phải suy đoán — được rút ra từ phân tích khung-hình thật của video *"I Time Traveled to Ancient China in 211 BC! (Vlog)"* (10:40, ~38 shot). Toàn bộ chi tiết nằm ở `.agents/skills/time-travel-vlog/references/reference-analysis.md`.

**Số liệu chính:**
- ~38 shot / 10:40 → trung bình ~17s, trung vị ~15s. Rất nhiều mối nối cách nhau đúng ~15s → mỗi beat ≈ 1 clip 8s + Extend, hoặc 2 clip 8s nối liền mạch (trong FlowKit: 2 scene nối F2V, mục 7a).
- 1 cao trào nguy hiểm duy nhất ở ~60% video (đoàn xe hoàng đế đi qua → bị lính để ý → chạy trốn), sau đó hạ nhịp rồi dồn vào reveal.
- Không có cảnh "du hành" mở đầu — vào thẳng thế giới từ giây 0 bằng một vật chuyển động mạnh sát ống kính (bánh xe bò).
- Âm thanh gần như không có khoảng lặng; không có chữ trên màn hình.
- Kết bằng khoảnh khắc tĩnh, phản tư (ngồi dưới gốc cây lúc hoàng hôn) — không có cảnh "quay về".

**Dòng thời gian rút gọn (minh họa tỉ lệ, không sao chép nguyên văn):**

| % video | Beat | Loại |
|---|---|---|
| 0% | Bánh xe bò sát ống kính → giữa chợ, trẻ con, lính cầm giáo | Hook vào thẳng |
| 4–9% | Đường lớn, công trường cung điện, súc gỗ khiêng ngang (wipe) | Định hướng + quy mô |
| 12–29% | POV đường bùn, quan lại viết thẻ tre, chợ rau, ăn cháo, đong hạt bằng đấu chuẩn, xưởng nhuộm | Đời thường (mỗi beat 1 sự thật) |
| ~47% | Quay gáy → đại quân đang tập trận (Reveal lớn #1) | Quyền lực |
| ~57–68% | Đoàn xe hoàng đế đi qua, dân quỳ rạp → nấp sau cột → chạy trốn qua ngõ → cưỡi ngựa thoát ra cổng thành | Cao trào nguy hiểm |
| ~70% | Đi nhờ xe bò với bà nông dân thân thiện | Hạ nhịp |
| ~74–92% | Công trường lăng mộ xa xa, xưởng gốm, tượng binh mã sơn màu rực rỡ (chi tiết ít người biết), chạm giáp/kiếm đồng, hố tượng nhìn từ trên cao | Di sản (reveal dần) |
| ~94–100% | Đi dọc hàng tượng, ngồi dưới gốc cây lúc hoàng hôn nói suy nghĩ | Đỉnh cảm xúc → Kết trầm |

Chỉ học tỉ lệ/nhịp; không sao chép tên, ngoại hình hay lời thoại nhân vật của video gốc.

---

## 📤 ĐỊNH DẠNG OUTPUT (theo đúng thứ tự)

1. **Giả định** (3–5 dòng) — thời kỳ/năm, độ dài, số beat/scene, tỉ lệ khung, material.
2. **Character Bible** — khối `CHARACTER_LOCK` + `voice_description` + `VOICE_LOCK` (`voice-bible.md` mục 1). Bối cảnh sinh tồn → ghi rõ đang dùng Survival Preset (mục 5c).
3. **Research pack** — bảng beat (mục 4), kèm độ chắc ✅/⚠️.
4. **Outline theo 7 hồi** + thời lượng từng hồi.
5. **Bảng storyboard toàn bộ beat** (mục 6).
5b. **Bảng vật lý từng clip — BẮT BUỘC HỎI USER DUYỆT** (góp ý của user, mục 11 quy tắc 21) trước khi viết Clip JSON. Dùng `AskUserQuestion` hoặc hỏi thẳng trong chat, và chỉ viết Clip JSON / sinh video sau khi user đồng ý hoặc sửa bảng:

   | # | Máy đặt ở đâu, nhìn về đâu | Có gì trong khung ở giây 0 | Vật di chuyển: hướng + tốc độ + hệ quả trong khung | Chuyển động vật lý thật | Ai hoặc cái gì rời khung, bằng cách nào |
   |---|---|---|---|---|---|
   | S31 | Trên thuyền chèo, nhìn về sau qua đuôi thuyền | Sau gáy Mia bên trái, thành phố ở chân trời bên phải | Thuyền chèo tay đi chậm, rời xa thành phố → thành phố giữ nguyên hoặc nhỏ dần | Thuyền nhấp nhô và lắc theo sóng; người chèo quay mặt về đuôi thuyền | Mia dịch sang bên; sóng tạt kín ống kính ở giây cuối |

6. **Clip JSON từng clip** (mục 10) — long-form xuất **theo từng hồi, hỏi user xác nhận trước khi sang hồi tiếp**; Shorts xuất hết một lần.
7. **Ghi chú hậu kỳ + gói YouTube** (Bước 5–6 bên dưới).

Long-form → ghi file `output/<slug>/script.md` (cập nhật dần theo từng hồi); Shorts → trả trực tiếp trong chat. Chỉ dựng project FlowKit (phần 🛠️) sau khi user duyệt kịch bản.

---

## 🛠️ CÁCH TRIỂN KHAI TRONG FLOWKIT

### Bước 0: Kiểm Tra Kết Nối & Pre-Flight (Bắt Buộc)
```bash
curl -s http://127.0.0.1:8100/health
# Bắt buộc trả về: {"extension_connected": true}
curl -s http://127.0.0.1:8100/api/flow/status
# Bắt buộc: {"transport": "batch", "flow_project_id": "<uuid>", ...}
```
Project mới → flush request PENDING cũ trước (theo `CLAUDE.md`). Gặp lỗi pipeline bất kỳ → `/fk-doctor` trước khi đoán cách sửa.

---

### Bước 1: Nghiên cứu Dữ Kiện & Khóa Mỹ Thuật
1. **Đọc 4 file references** (phần 📚) nếu chưa đọc.
2. **Fact-check lịch sử qua `/fk-research`** (bắt buộc, trước khi viết bất kỳ prompt nào), rồi điền checklist `era-research.md`:
   ```bash
   /fk-research "Ancient Rome 79 AD daily life market food dress Pompeii"
   # hoặc: /fk-research "Qin dynasty China 211 BC Xianyang market commoners soldiers"
   # hoặc: /fk-research "Victorian London 1890 daily life market fog gaslight"
   ```
3. **Khóa chất liệu qua [`/fk-add-material`](file:///c:/flowkit/skills/fk-add-material.md)** — `phone_vlog` (mục 9) hoặc `realistic`.
4. **Quy chuẩn góc máy qua [`/fk-camera-guide`](file:///c:/flowkit/skills/fk-camera-guide.md)** — camera selfie trước góc siêu rộng, nhịp walking gait nhấp nhô, tỉ lệ shot ở mục 6.

---

### Bước 2: Dựng Dự Án Trong FlowKit (Character Bible + Clip JSON → API)
Skill này không có script cố định vì mỗi thời kỳ/địa điểm khác nhau — dùng thẳng `/fk-create-project` với Character Bible và Clip JSON đã duyệt:

```bash
curl -X POST http://127.0.0.1:8100/api/projects \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Rome 79 AD - Time Travel Vlog",
    "story": "<tóm tắt 7 hồi từ storyboard>",
    "material": "phone_vlog",
    "characters": [
      {"name": "Nora", "entity_type": "character", "description": "<CHARACTER_LOCK nguyên văn>", "voice_description": "<tông giọng>"},
      {"name": "Forum Market", "entity_type": "location", "description": "<bối cảnh từ research pack, kèm thành phố + năm>"},
      {"name": "Selfie Stick", "entity_type": "visual_asset", "description": "short black selfie stick with a smartphone on ultra-wide 0.5x lens"}
    ]
  }'
```
Sau đó tạo video (`POST /api/videos`) và từng scene (`POST /api/scenes`) theo đúng thứ tự storyboard, chuyển mỗi Clip JSON thành scene theo bảng ánh xạ ở mục 10. Beat mới/đổi địa điểm → `ROOT`; nửa sau của cùng beat hoặc cùng bối cảnh → `CONTINUATION` + `parent_scene_id`. Ghi lại danh sách các cặp scene nối **F2V** để xử lý tuần tự ở Phase B. Chi tiết định dạng `prompt`/`video_prompt`/`character_names` xem [`/fk-create-project`](file:///c:/flowkit/skills/fk-create-project.md).

---

### Bước 2.5: Xác Định & Đặt Dự Án Hoạt Động (Set Active Project)
```bash
curl -s http://127.0.0.1:8100/api/active-project
/fk-switch-project <PROJECT_ID>
```

---

### Bước 3: Tải Ảnh Chân Dung Thật (Tùy Chọn)
Nếu muốn dùng khuôn mặt thật làm Vlogger thay vì mặt AI:
```bash
/fk-upload-ref "C:/photos/my_face.jpg" --entity "Nora"
```

---

### Bước 4: Sinh Ảnh Scene → Review → Sinh Video

> [!IMPORTANT]
> **Xác nhận trước mỗi bước sinh.** Trước bất kỳ bước nào khiến Flow sinh media (ảnh ref, video, clip chạy thử, thử lại, sinh lại), nói rõ sẽ sinh gì, bao nhiêu cái, rồi chờ user đồng ý. Xong mỗi bước sinh thì DỪNG, đưa kết quả cho user duyệt, chỉ sang bước sau khi được đồng ý. Clip lỗi hoặc điểm review thấp thì báo cáo kèm đề xuất sửa, không tự sinh lại. Quy tắc này ưu tiên hơn mọi chỗ ghi "tự động chạy tiếp" trong skill (xem CLAUDE.md, AGENTS.md rule 29).


Pipeline chia **2 phase** với cửa review bắt buộc ở giữa. Không bao giờ sinh video trực tiếp từ prompt chưa được kiểm tra ảnh — ảnh xấu thì video chắc chắn xấu theo.

#### Phase A — Sinh Refs + Ảnh Scene
```bash
/fk-gen-refs    # Sinh ảnh nhân vật/bối cảnh/đạo cụ còn thiếu media_id
/fk-gen-images  # Sinh ảnh frame-0 cho toàn bộ scene (VERTICAL hoặc HORIZONTAL)
```
Khi tất cả scene có `${ori}_image_status = COMPLETED`, dừng lại và **bắt buộc review trước khi sang Phase B**.

#### Bước 4.5: Review Ảnh Scene (Bắt Buộc Trước Khi Sinh Video)
```bash
/fk-review-board   # Mở bảng review trực quan tất cả ảnh scene trong browser
```

| Tiêu chí | Pass | Fail → Hành động |
|---|---|---|
| Khuôn mặt nhân vật giống ảnh ref, rõ, đúng góc | ✅ | REGENERATE_IMAGE với prompt rõ hơn về góc máy |
| Trang phục của vlogger khớp ảnh ref (đồ hiện đại theo ảnh ref là chấp nhận được); dân bản địa mặc đồ đúng thời kỳ | ✅ | Thêm câu: `The locals wear [period clothing].` |
| Bối cảnh + người nền đúng niên đại và đúng chủng tộc bản địa | ✅ | REGENERATE_IMAGE, siết thêm thành phố + năm vào `prompt` |
| Trông như **khung hình điện thoại** (góc siêu rộng, méo nhẹ), không phải ảnh điện ảnh/studio | ✅ | Patch `prompt` thêm `"ultra-wide 0.5x smartphone frame, slight lens distortion"` |
| Selfie: tay/gậy selfie lọt mép khung | ✅ | Patch `prompt` nhấn mạnh `"her extended arm and the Selfie Stick visible at the frame edge"` |
| Ánh sáng nhất quán với giờ trong ngày của beat (và giữa hai clip của một mối nối) | ✅ | REGENERATE_IMAGE với chú thích ánh sáng |
| Frame 0 của scene có `transition_in` thể hiện đúng vật che đang rời khung, đúng hướng | ✅ | Patch `prompt` mô tả rõ vật che + hướng |
| Không chữ/logo/watermark trên ảnh | ✅ | Thêm `"no text, no watermark, no subtitles"` |
| Scene CONTINUATION: bối cảnh liên tục với parent | ✅ | REGENERATE_IMAGE; nếu vẫn fail → đổi `chain_type: ROOT` |

Chỉ khi **tất cả scene pass**, mới chạy Phase B.

#### Phase B — Sinh Video + Nối F2V + Review
1. **Lượt 1 — Videos**: sinh video cho mọi scene **trừ** nửa sau (B) của các cặp F2V, bằng một lượt `POST /api/requests/batch` với `GENERATE_VIDEO` chỉ gồm các scene đó (format ở `/fk-gen-videos` Step 3). Không chạy `/fk-gen-videos` cho toàn bộ — nó sẽ sinh luôn scene B từ ảnh Frame 0 cũ, tốn credit vô ích.
2. **Nối F2V** (cho từng cặp A → B đã đánh dấu ở Bước 2): tải video A, trích khung cuối, upload và gán làm Frame 0 của B:
   ```bash
   ffmpeg -sseof -0.1 -i A.mp4 -frames:v 1 A_last.png
   /fk-upload-image A_last.png --project <PID>   # → media_id (UUID)
   # PATCH /api/scenes/<B_ID>  {"${ori}_image_media_id": "<MEDIA_ID>"}
   ```
   Rồi **Lượt 2**: gom toàn bộ scene B vào một lượt `POST /api/requests/batch` — không viết script lặp gọi API.
3. **Review video bắt buộc**: `/fk-review-video` — kiểm tra khuôn mặt không trôi, thoại không bị cắt, khung che ở cuối A và đầu B khớp nhau; REGENERATE scene fail.
4. **Concat thẳng**: `/fk-concat` (cắt thẳng, **không** crossfade, không text overlay). Nếu clip dư phần khung che, trim tại khung che kín nhất.
5. Chỉ thêm `--tts` nếu user chọn lồng tiếng thay vì thoại native.

---

### Bước 4.9: Phương Án Dự Phòng Khi Google Chặn Sinh Tự Động → Xuất File Kịch Bản Để Import Thủ Công

**Khi nào đề xuất:** lệnh sinh qua FlowKit bị `PUBLIC_ERROR_UNUSUAL_ACTIVITY` (không có `[HIJACK]`) **từ 2 lần chạy thử 1 request trở lên**, dù extension đúng bản, đã xóa cookie, và bấm tay trên giao diện Flow vẫn sinh được. Khi đó dừng gửi request và **đề xuất với user** xuất kịch bản ra JSON để import vào công cụ tạo thủ công, không tiếp tục thử lại.

```bash
python tools/export_flow_import.py <PROJECT_ID> --main <Vlogger>   --upload "<Vlogger>=C:/path/face_clean.jpg"   --refs-dir output/<slug>/refs --script output/<slug>/script.md   --out output/<slug> --time-capsule "<Địa điểm>, <năm> — <vibe>"
# → output/<slug>/kich-ban-vlog/<project-slug>/<project-slug>.json + base-ref/*.jpg
```

- **Template chuẩn:** `.agents/skills/time-travel-vlog/references/flow-import-template.json` (các loại node `upload` / `image` / `video`, `promptParts` gồm `text` + `image_ref`, `refImageIds`, `sources`, `voiceId`, `dialog`, `edges`).
- **Ánh xạ R2V:** không có start frame, nên mỗi node video tham chiếu thẳng các ảnh ref (`image_ref` + `refImageIds`), `sources: []`, `model: abra_r2v_<duration>s`.
- **Entity có ảnh local** (`--upload` hoặc `<slug>_clean.jpg` / `<slug>.jpg` trong `--refs-dir`) thành node `upload`, ảnh được copy vào `base-ref/`. Entity chưa có ảnh thành node `image` với prompt lấy từ `description`.
- **Thoại:** lấy chính xác từ Clip JSON trong `script.md`. Clip của vlogger có `voiceId` + `voiceCharId: "char-main"`; clip của dân bản địa có `speaker` riêng.
- Ảnh trong `base-ref/` phải là **bản đã xóa logo**. Chạy lại lệnh sau khi làm sạch ảnh.
- Copy cả thư mục `kich-ban-vlog/` vào thư mục gốc của công cụ import (đường dẫn `file` trong JSON có dạng `kich-ban-vlog/<slug>/base-ref/...`).

### Bước 5: Hậu Kỳ — Đồng Nhất Để Trông Như Một Chiếc Điện Thoại
- **Cắt thẳng theo khung che** (mục 7); jump cut khi đi bộ để nguyên.
- **Nhạc + ambient liên tục** qua `/fk-gen-music` (nhạc cụ truyền thống của thời kỳ, không lời), mix dưới thoại; hạ nhạc ở cảnh nguy hiểm và cảnh kết, không tắt hẳn giữa scene.
- **SFX nhẹ** ("vút") khi vật thể lướt qua ống kính; **J-cut** ambient scene sau vào sớm ~0.5s.
- **Grade ấm, hoàng hôn ở cuối; thêm grain nhẹ** để đồng nhất các clip (clip AI sinh riêng lẻ thường lệch màu). Làm trong CapCut, hoặc ffmpeg trên file final, ví dụ:
  ```bash
  ffmpeg -i final.mp4 -vf "colorbalance=rs=0.03:bs=-0.03,noise=alls=5:allf=t" -c:a copy final_graded.mp4
  ```
  Thử trên một đoạn ngắn trước — grain quá tay làm mất cảm giác điện thoại.
- Phụ đề tùy chọn, chỉ dạng `.srt` rời.
- **Bíp chửi thề**: phủ tiếng bíp ~0.3s tại mỗi mốc `bleep_at` trong Clip JSON (xem lại clip trước khi bíp vì model có thể lệch mốc vài trăm mili-giây).

---

### Bước 6: Đóng Gói YouTube
- `/fk-youtube-seo` — **3 tiêu đề chuẩn High-Stakes / Sinh tồn nghẹt thở**:
  - *Option 1 (Nguy hiểm cận kề / Khuyên dùng)*: `I Time Travelled to [Year] — And Almost Got Trampled by a [Threat]`
  - *Option 2 (Format 24 Giờ Sinh Tồn)*: `I Spent 24 Hours in [Location/Era] ([Extreme Condition]) with [Ancient People]`
  - *Option 3 (Shock văn hóa & Nghịch lý)*: `What Happens When You Show Modern Fire to [Ancient People]?`
  - Mô tả có **timestamp theo beat/hồi**, bộ tag chuẩn SEO, tuyệt đối không dùng tiêu đề hiền/giáo khoa.
- `/fk-thumbnail` — Thumbnail High-Stakes: Mặt nhân vật hoảng loạn/adrenaline cực độ né mối nguy cận kề (chân voi ma mút giẫm, giáo chĩa, bão tuyết -40°C) + Text 2 dòng kích thích tò mò (Line 1: `ALMOST TRAMPLED!` / `-40°C SURVIVAL!` / `THEY SAW FIRE!`; Line 2: Địa điểm & Niên đại bằng tiếng Anh); 16:9 (long-form) hoặc 9:16 (Shorts).
- **Bật nhãn "Altered or synthetic content"** trong YouTube Studio khi upload — `/fk-youtube-upload` hiện không tự đặt nhãn này, phải bật tay.

---

### Bước 7: Chiến Lược "Mồi Thuật Toán" Sau Phát Hành (Algorithm Seeding)
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
