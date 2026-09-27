# fk-time-travel-vlog — Time Travel Vlog Orchestrator (Mọi Thời Kỳ, Mọi Địa Điểm)

Tạo kịch bản và dự án video vlog **DU HÀNH THỜI GIAN / POV VLOG LỊCH SỬ** kiểu *"I Time Traveled to Ancient China in 211 BC"*, *"A Day in Ancient Rome"*, *"POV You Woke Up in 1890 London"* — vlogger hiện đại cầm điện thoại/gậy selfie, rơi vào một thời kỳ lịch sử cụ thể, vừa đi vừa nói chuyện với camera và dân bản địa. Skill này dùng cho **mọi thời kỳ/địa điểm** (La Mã cổ đại, Trung Hoa Tần/Hán, London thời Victoria, Ai Cập cổ đại, Ba Tư, Viking, Nhật Bản Heian/Edo...).

Dùng skill này cả khi user chỉ đưa một link YouTube kiểu này và nói "làm giống vậy", hoặc hỏi cách viết kịch bản / cách chuyển cảnh cho vlog lịch sử, "xuyên không vlog", "vlog cổ đại", "POV về quá khứ".

Format này ăn view vì 3 thứ: **góc nhìn người thật** (mọi thứ "quay bằng điện thoại của nhân vật" → người xem thấy mình đang ở đó), **thế giới xa lạ nhưng có thật** (sự thật lịch sử bật ra qua quan sát, không giảng bài), và **đường cong cảm xúc** đi từ đời thường → quyền lực/nguy hiểm → di sản mà người xem hiện đại đã biết tên. Cảnh nào không phục vụ 3 thứ đó thì cắt.

---

## 📚 TÀI LIỆU THAM CHIẾU — BẮT BUỘC ĐỌC TRƯỚC KHI VIẾT

Mọi quy tắc trong skill này được rút ra từ 4 file ở `.agents/skills/time-travel-vlog/references/`. **Đọc cả 4 file trước khi viết bất kỳ dòng kịch bản/prompt nào** — chúng là nguồn chuẩn cho độ chân thực; skill này chỉ tóm tắt và ánh xạ sang FlowKit.

| File | Đọc ở bước | Dùng để |
|---|---|---|
| `reference-analysis.md` | Trước tiên, trước mọi bước | Chuẩn nhịp (~15s/beat), tỉ lệ góc máy, dòng thời gian beat, cách giấu mối nối quan sát được từ video mẫu thật |
| `era-research.md` | Mục 4 — Research Pack | Checklist nghiên cứu thời kỳ + bảng beat output |
| `prompt-templates.md` | Mục 2 + mục 10 | Mẫu `CHARACTER_LOCK`, Clip JSON, mẫu shot (dân bản địa nói, POV, máy dựng, toàn cảnh) |
| `transitions.md` | Mục 7 | 3 cách nối clip, luật giấu mối nối, prompt A/B cho từng kỹ thuật, bảng chọn nhanh |

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

### 2. Character Bible — khóa nhân vật xuyên suốt
Một khối `CHARACTER_LOCK` cố định, **dán nguyên văn vào entity `description` và KHÔNG sửa giữa các clip**, kèm ảnh tham chiếu mặt (`/fk-upload-ref` nếu dùng mặt thật, hoặc `/fk-gen-refs` sinh ref AI rồi khóa lại). Video mẫu giữ mặt nhân vật giống hệt suốt 10 phút — đây là điều kiện sống còn của độ chân thực.

Gồm: mặt (tuổi, dáng mặt, mắt, tàn nhang/nốt ruồi), tóc (màu, kiểu búi, trâm/phụ kiện), trang phục thời kỳ (kiểu áo, màu, cổ áo, thắt lưng — **KHÔNG nhuộm màu/vải công nghiệp hiện đại**), thiết bị (gậy selfie ngắn + điện thoại góc siêu rộng 0.5x, cánh tay lọt mép khung), giọng (`voice_description`: tông, tốc độ, thì thầm khi sợ).

#### Quy tắc Cốt Lõi Về Voice, Omni Flash Ingredients R2V (BẮT BUỘC):
1. **CHỈ DÙNG OMNI FLASH INGREDIENTS (`reference_to_video` / `abra_r2v`) — KHÔNG DÙNG START FRAME I2V**:
   - Khi tạo video nhân vật/vlog, **TUYỆT ĐỐI KHÔNG sinh ảnh Start Frame (`GENERATE_IMAGE`) để chạy Image-to-Video (`i2v`)**. Cách làm cũ bằng Start Frame làm chuyển động bị cứng, dễ giật, méo người và biến dạng khuôn mặt khi di chuyển.
   - **BẮT BUỘC chỉ sử dụng Omni Flash Ingredients (`GENERATE_VIDEO_REFS` / `omni_flash_models.reference_to_video` / `abra_r2v_<duration>s` qua RPC `MZZa6b`)**:
     - Đính kèm trực tiếp các thành phần tham chiếu (Ingredients): Nhân vật (`Mia`), Trang phục (`Mia Outfit`), và Bối cảnh/Địa điểm (`reference_media_ids` / `imageInputs`).
     - Model `abra_r2v` tự động tổng hợp chuyển động video mượt mà trực tiếp từ các thành phần tham chiếu và `video_prompt`, tích hợp khẩu hình native với voice profile **Achernar** (Slot 7).
     - Không chạy quy trình `GENERATE_IMAGE` cho từng cảnh; sau khi các entity có `media_id`, gửi thẳng yêu cầu `GENERATE_VIDEO_REFS`.
2. **Voice Achernar**: Với nhân vật vlogger nữ, khai báo `voice_description` theo chuẩn **Achernar** (Google Gemini-TTS: *"Achernar — soft, higher-pitched, natural expressive conversational female voice, casual vlog tone, breathy when amazed, hushed whisper when nervous"*). Đính thoại dạng `Mia says: "..."` trong sub-clips `0-3s / 3-6s / 6-10s` để `abra_r2v` tự sinh khẩu hình và giọng nói bản địa tự nhiên.
3. **Review 720p trước ➔ User duyệt ➔ Upscale 1080p & Xóa Logo sau**: Tải từng clip 720p về `${OUTDIR}/scenes/scene_{idx}_{sid}.mp4`. **Chưa cần xóa logo ở bước này** để tránh lãng phí thời gian encode. Trích xuất frames từ video 720p, chạy AI Review Scorecard và đưa lên Review Board (`http://localhost:8200`) cho người dùng review từng clip. **CHỈ KHI NGƯỜI DÙNG DUYỆT THÔNG QUA**: Gửi lệnh Upscale 1080p (`p0UkFb` / `veo_3_1_upsampler_1080p`), tải bản 1080p về folder riêng `${OUTDIR}/1080/scene_{idx}_{sid}_1080p.mp4`, rồi mới chạy `remove_watermark_video` trực tiếp trên bản 1080p (`${OUTDIR}/1080/scene_{idx}_{sid}_1080p_clean.mp4`) để đưa vào Concat cuối cùng.

Mẫu (từ `prompt-templates.md` — thay giá trị, tên nhân vật do bạn đặt, rồi đóng băng):
```
CHARACTER_LOCK:
Nora, a 26-year-old Western woman with a heart-shaped face, hazel-green eyes, dense freckles across nose and cheeks,
bright copper-red hair in a high bun held by a dark wooden hairpin, a few loose strands at the temples,
wearing an era-appropriate [dark indigo cross-collar hemp robe with a white inner collar and a plain dark sash],
holding a short black selfie stick with a smartphone on ultra-wide 0.5x lens, her arm visible at the frame edge.
Voice: Achernar — soft, higher-pitched, natural expressive conversational female voice, casual vlog tone, breathy when amazed, hushed whisper when nervous.
```
Tên trong `CHARACTER_LOCK`, tên entity và tên người nói trong `video_prompt` phải **trùng nhau tuyệt đối** (mẫu gốc có chỗ lệch Nora/Mia — đừng lặp lại lỗi đó).

**Trang phục theo ảnh ref (góp ý của user, đã kiểm chứng):** với R2V, quần áo của vlogger **lấy từ ảnh ref**, không lấy từ chữ trong `CHARACTER_LOCK`. Vlogger **mặc đồ hiện đại theo ảnh ref là chấp nhận được**, không bắt buộc đồ thời kỳ. Yếu tố "người lạ" nằm ở ngoại hình + gậy selfie + trang phục khác dân bản địa. Chỉ khi user yêu cầu đồ thời kỳ thì mới sinh thêm ảnh ref nhân vật mặc đồ thời kỳ (giống node `img-char-period` trong template import, Bước 4.9), và không thêm câu tả trang phục vào prompt để "ép" khi ảnh ref đang mặc đồ khác.

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

**Quy tắc thoại**
- **Mật độ từ**: beat 15s ≈ 25–35 từ tiếng Anh; mỗi clip 8s ≈ **12–18 từ**. Vượt ngưỡng → Veo nói nhanh bất thường hoặc cắt câu, mất chân thực.
- Để **1–2s không thoại ở đầu và cuối mỗi clip** cho chuyển cảnh — không bao giờ cắt ngang câu.
- **Một người nói/clip.** Dân bản địa nói → vlogger im lặng phản ứng (mắt mở to, môi mím).
- Giọng vlog thật: câu ngắn, cảm thán, thì thầm, gọi người xem ("you guys", "okay, don't freak out"). Sự thật lịch sử nói qua quan sát, không giảng bài.
- Mỗi beat có một thứ mới: nơi mới, người mới, thông tin mới hoặc nguy hiểm mới.

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
| ~5% | Toàn cảnh hoành tráng nhưng **vẫn từ vị trí nhân vật đứng** | `view from where she stands on a high earthen ridge, slow handheld pan over [thousands of soldiers / the pits]; the phone is the camera, so no phone appears anywhere in the frame` |

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
  `handheld smartphone selfie-stick vlog footage, ultra-wide 0.5x front camera, natural daylight, slight lens distortion, subtle hand shake, photorealistic, documentary realism`
- **Dấu vết điện thoại**: méo ống kính góc siêu rộng, rung tay nhẹ theo nhịp bước, cánh tay/gậy lọt mép khung ở shot selfie, auto-exposure theo nguồn sáng tự nhiên. Không dolly/crane/gimbal mượt kiểu điện ảnh.
- **Người nền phản ứng**: dân bản địa dừng lại nhìn chằm chằm, tò mò hoặc nghi ngờ — nhưng **không ai nói** trừ người nói duy nhất của clip.
- **Audio môi trường đúng thời kỳ**: tiếng chợ bằng ngôn ngữ cổ/địa phương, bánh xe gỗ lạch cạch, chuông đồng xa — ghi ở dòng `Audio:` cuối prompt.
- **Ràng buộc viết thành câu khẳng định trong thân prompt — KHÔNG dùng dòng `Negative:` liệt kê từ khóa** (góp ý của user: liệt kê từ khóa không có tác dụng, điện thoại vẫn hiện ra). Câu chuẩn, đặt trước dòng `Audio:`:
  `The phone is the camera, so no phone appears anywhere in the frame. Mia stays in frame for the whole clip and never disappears. The locals wear [period clothing]; everything around is [era], with no modern buildings or vehicles. Only Mia speaks. No subtitles or text appear on screen. This looks like real footage, not a movie or a 3D render.`
- **Material**: `realistic` mặc định áp *Canon EOS R5, 35mm* — kiểu ảnh máy ảnh, lệch với footage điện thoại. Khuyến nghị tạo material tùy chỉnh (giữ ảnh ref chân thực, chỉ đổi scene sang chất điện thoại):
  ```bash
  curl -X POST http://127.0.0.1:8100/api/materials -H "Content-Type: application/json" -d '{
    "id": "phone_vlog",
    "name": "Smartphone Vlog (Photoreal)",
    "style_instruction": "Photorealistic RAW photograph, natural available light, real skin texture, documentary realism.",
    "negative_prompt": "NOT 3D render, NOT anime, NOT illustration, NOT cinematic color grade, NOT studio lighting.",
    "scene_prefix": "Handheld smartphone vlog frame, ultra-wide 0.5x front camera, slight lens distortion, natural daylight, documentary realism.",
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
  "constraints": "The phone is the camera, so no phone appears anywhere in the frame. Nora stays in frame for the whole clip and never disappears. Only Nora speaks. No subtitles or text appear on screen. This looks like real footage, not a movie or a 3D render."
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
6. **Video 16:9 (long-form): ảnh ref cảnh rộng sinh ngang 16:9**, còn ảnh ref nhân vật và vật cao để dọc 9:16. FlowKit chỉ sinh ngang cho entity `location`, nên với `visual_asset` cảnh rộng: tạm PATCH `entity_type: location` → `REGENERATE_CHARACTER_IMAGE` → đổi lại `visual_asset`.
7. Ảnh ref không được có người, tay, đồ vật hay trang phục hiện đại lọt vào (găng tay, ủng, người mặc áo thun), không có kiến trúc lệch thời kỳ (mái vòm, tháp nhọn, lâu đài trung cổ), và không có dải màu trơn quanh ảnh.

**Viết `video_prompt`**
8. **Ràng buộc là câu khẳng định**, không dùng dòng `Negative:` (xem mục 9).
9. **Điện thoại là máy quay:** luôn có câu `The phone is the camera, so no phone appears anywhere in the frame.` Không viết `she holds the phone up` hay `the phone peeks out` (model sẽ vẽ luôn cái điện thoại). Với POV, cho tay nhân vật bận việc khác (bám mép thuyền, cầm đồ vật).
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
2. **Character Bible** — khối `CHARACTER_LOCK` + `voice_description`.
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

---

### Bước 6: Đóng Gói YouTube
- `/fk-youtube-seo` — **3 tiêu đề** dạng `"I Time Traveled to ___ in ___! (Vlog)"`, mô tả có **timestamp theo beat/hồi**, bộ tag.
- `/fk-thumbnail` — mặt nhân vật sốc + công trình/sự kiện nổi tiếng nhất của thời kỳ; 16:9 (long-form) hoặc 9:16 (Shorts).
- **Bật nhãn "Altered or synthetic content"** trong YouTube Studio khi upload — `/fk-youtube-upload` hiện không tự đặt nhãn này, phải bật tay.
