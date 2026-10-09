---
name: fk-time-travel-vlog
description: Use when making a time-travel / POV survival vlog — a modern vlogger filming herself inside a historical or prehistoric era ("I Time Traveled to Ancient China in 211 BC", "A Day in Ancient Rome", "xuyên không vlog", "vlog cổ đại", "POV về quá khứ") — writing its script, dialogue, storyboard or video_prompts, building or fixing its FlowKit project, or when the user shares a YouTube video of this kind and says "làm giống vậy".
---

# fk-time-travel-vlog — Time Travel Vlog Orchestrator (Mọi Thời Kỳ, Mọi Địa Điểm)

Vlogger hiện đại rơi vào một thời kỳ cụ thể (La Mã, Tần/Hán, Victoria, Kỷ Băng Hà, Viking, Edo…), tự quay mình bằng góc selfie/POV, nói với người xem và sống sót giữa dân bản địa. Kết quả: kịch bản + storyboard + Clip JSON + dự án FlowKit chạy **Omni Flash R2V Ingredients**.

Format ăn view nhờ 3 thứ: **góc nhìn người thật** (mọi thứ như quay bằng máy của nhân vật), **thế giới xa lạ mà tin được** (trông đúng thời kỳ; chi tiết bịa thoải mái, không giảng), và **đường cong cảm xúc / sinh tồn** leo thang tới một payoff. Cảnh nào không phục vụ 3 thứ đó thì cắt.

## Thứ tự ưu tiên khi các nguồn mâu thuẫn

1. `CLAUDE.md` (Rule 27, 28, 29, 42–49…) và memory của user.
2. Mục **Khóa cứng** bên dưới.
3. `references/production-lessons.md` — bài học số lớn / ngày mới thắng bài cũ.
4. `references/story-engine.md` (cấu trúc truyện) và `references/prompt-lock.md` (câu chữ prompt).
5. Các reference còn lại. `reference-analysis.md` là quan sát video mẫu — dùng cho nhịp và góc máy, không ghi đè luật sản xuất.

Đường dẫn `references/…` tính từ thư mục skill này: `skills/fk-time-travel-vlog/`.

## Khóa cứng (tóm tắt luật mới nhất — chi tiết ở reference ghi kèm)

| Chủ đề | Luật | Chi tiết |
|---|---|---|
| Hư cấu | Phim giải trí, không phải tài liệu: sự kiện, phong tục, mẹo sinh tồn đều bịa được. Vlogger **không dạy lịch sử** (không niên đại, "scientists say"). Chỉ giữ: trông đúng thời kỳ + không biếm họa dân tộc/tôn giáo. `/fk-research` tùy chọn | `era-research.md` |
| Sinh video | **Chỉ R2V Ingredients** (`GENERATE_VIDEO_REFS`, `abra_r2v_<N>s`, `MZZa6b`). Không sinh start frame rồi i2v cho clip có vlogger | `flowkit-pipeline.md` |
| Bộ ref vlogger | `<V>` (mặt+tóc) + `<V> Body` (body 3 góc **đã mặc outfit**, EDIT từ Body trần gốc theo công thức outfit lock). Không entity `<V> Outfit`. Tối đa 3 ref/clip. Body phải được user duyệt trước khi sinh video | `character-bible.md` §5–6 |
| Khóa trang phục | **Khóa trang phục thuần ref**: TUYỆT ĐỐI KHÔNG mô tả lại trang phục bằng lời trong prompt. Chỉ trỏ thẳng: `wears the exact historical outfit shown in the <V> Body reference sheet (NO shearling collar, NO extra fur, NO hood, NO outfit variations)` | `production-lessons.md` #63 |
| Khóa hình thể | **Chống teo tóp body**: Góc máy ngang ngực/bụng trên (Waist-Up Medium Shot) hơi hất nhẹ lên, nhân vật đứng thẳng; cụm đối kháng cực mạnh: `tall statuesque 178 cm, voluptuous hourglass, large heavy bust, tiny waist, wide hips, NOT flat-chested, NOT skinny` | `production-lessons.md` #63 |
| Giọng | Chỉ vlogger có `voice_description` (Laomedeia). 1 giọng/clip | `character-bible.md` §3 |
| Nhân vật phụ | Được nói, bằng ngôn ngữ không hiểu được, ở sub-clip riêng, giọng tả bằng chữ; vlogger phản ứng với giọng điệu, **không dịch** | `character-bible.md` §4 |
| Thoại | **23–25 từ / clip 8s** (tốc độ nói nhanh, dồn dập, tự nhiên kiểu vlog Laomedeia; tối đa 26 từ chống cụt âm thanh). **Ngoại lệ Sonic Isolation**: Cảnh rình mồi, phục kích thì 0 từ trên hình (miệng khóa chặt, thoại dẫn chuyển thành voiceover hậu kỳ). Viết/sửa qua `/fk-gen-narrator` | `voice-bible.md` §2, `production-lessons.md` #62 |
| Thiết bị & Material | **Cấm 100% từ khóa thiết bị**: Không viết `phone`, `smartphone`, `phone_vlog`, `camera` (đạo cụ), `selfie stick`, `device`, `screen`, `gimbal` — kể cả câu phủ định và trong project material. Ràng buộc quang học: `The camera lens and viewpoint are completely outside the visible frame and never seen; both hands are empty` | `prompt-lock.md` #16, #28, `production-lessons.md` #63 |
| Góc máy & Động học | **Phối hợp Góc máy Vlog Chân thực (Bỏ selfie 1 tay vươn dài)**: Linh hoạt phối hợp 3 góc máy: (1) *Lúc cần có Nora (Self-Vlog / Tự quay)*: Cầm máy tự nhiên ngang ngực/cổ quay mặt mình, nhìn thẳng camera dẫn dắt; (2) *Lúc thao tác 2 tay & Cảnh rộng (In-Frame Host Experience)*: Máy đặt cố định trên đá/cây (Medium/Wide shot), Nora xuất hiện rõ trong khung hình dùng 2 tay trải nghiệm sinh tồn, vừa làm vừa nhìn camera giới thiệu; (3) *Cận cảnh chi tiết (POV Close-Up)*: Soi cận cảnh đồ vật/hiện tượng | `production-lessons.md` #62 |
| Nội dung sinh tồn | **Cấm 100% đánh đấm / vật lộn cận chiến với thú lớn** (tử huyệt làm vỡ hình AI). Tập trung 100% vào **Cơ chế sinh tồn kỳ thú & giao lưu văn hóa** (đẽo đá Mousterian, may đo chỉ gân hươu, đun nước đá nung, bột xúc tác MnO2, dấu bàn tay đất son đỏ) theo phong cách documentary trải nghiệm triệu view (như Medieval Sisters) | `production-lessons.md` #62 |
| Bối cảnh thời kỳ | **Khóa bối cảnh chuẩn xác (Strictly No Snow)**: Tôn trọng đúng khí hậu thời kỳ (MIS 3 Neanderthal Dordogne là rừng thông ôn đới, đất mùn rêu xanh, tuyệt đối không tự ý chèn tuyết/bão mùa đông) | `production-lessons.md` #62 |
| Chuyển cảnh | Cắt thẳng tại khung che. Selfie → swing/whip pan; POV → foreground wipe; cùng tư thế → match on action. Không crossfade, không title card | `transitions.md` |
| Chữ trên hình | Chỉ năm, mission card, countdown `HOUR X — Y HOURS REMAINING`, chèn hậu kỳ, không viết vào prompt | `story-engine.md` §9 |
| Cổng duyệt | Hỏi trước **mỗi** bước sinh; dừng sau mỗi bước cho user duyệt; lỗi thì đề xuất, không tự sinh lại | CLAUDE.md Rule 29 |
| Nhịp request | Server giãn mọi call Flow 45–60s; video: 1 cái một lúc, xong mới gửi tiếp; dừng khi `UNUSUAL_ACTIVITY` / `QUOTA` | `prompt-lock.md` #18 |

## Quy trình

Mỗi bước: đọc reference ghi kèm **trước khi** làm. Bước có ⛔ là cổng — dừng chờ user.

| # | Bước | Đọc | Ra |
|---|---|---|---|
| 0 | **Đầu vào** — tối đa 1 lượt hỏi, còn lại dùng mặc định (bảng dưới) và ghi rõ giả định | — | 3–5 dòng giả định |
| 1 | **Ý tưởng thế giới** (tùy chọn): `/fk-research` hoặc tự bịa, chọn 10–15 beat | `era-research.md` | bảng beat |
| 2 | **Character Bible**: `CHARACTER_LOCK` + Laomedeia + `VOICE_LOCK` + kế hoạch bộ ref | `character-bible.md`, `voice-bible.md` §0–1, `prompt-templates.md`, `cinematic-toolkit.md` §4 (trang phục đổi giữa tập) | khối lock trong `script.md` |
| 3 | **Outline**: chuỗi nhân quả sinh tồn → cold open 8s → 5 Act mỗi Act 1 câu hỏi → payoff → cảnh cuối không thoại. **Bắt buộc dùng subagent**: `fk-action-choreography` (động lực học), `fk-camera-guide` (tỷ lệ góc máy), `fk-cinematic-transitions` (chuyển hồi) | `story-engine.md` (bắt buộc), `structure-7-acts.md`, `reference-analysis.md`, `cinematic-toolkit.md` §3 | outline + thời lượng |
| 4 | **Storyboard + bảng vật lý** từng clip (máy ở đâu, có gì ở giây 0, hướng + tốc độ vật di chuyển, ai rời khung bằng cách nào). **Bắt buộc dùng subagent**: `fk-camera-guide` (bảng vật lý & quang học), `fk-cinematic-transitions` (khớp điểm nối) ⛔ user duyệt bảng vật lý | `shots-and-realism.md`, `transitions.md` | bảng storyboard + bảng vật lý |
| 5 | **Clip JSON + `video_prompt`** theo khung 9 khối, qua checklist B. **Bắt buộc phối hợp 5 subagent**: `fk-action-choreography` (3 pha hành động), `fk-add-material` (visual profile), `fk-cinematic-transitions` (chuyển cảnh), `fk-gen-narrator` (thoại 20–25 từ chia 3 mốc), `fk-camera-guide` (5 tầng quang học). Long-form xuất từng Act, ⛔ hỏi user trước khi sang Act sau | `prompt-lock.md`, `production-lessons.md`, `prompt-templates.md`, `voice-bible.md` §2–6, `cinematic-toolkit.md` §1–2 | `output/<slug>/script.md` |
| 6 | **Dựng dự án FlowKit** (pre-flight, flush PENDING, project, video, scenes, PATCH `duration` + `narrator_text`) | `flowkit-pipeline.md` §2–3; tập tiếp theo của series: `cinematic-toolkit.md` §5 | project/video/scene ids |
| 7 | **Refs**: mặt, Body đã mặc outfit (công thức outfit lock), bối cảnh — xóa logo, upload lại ⛔ hỏi trước khi sinh, ⛔ user duyệt ảnh | `flowkit-pipeline.md` §4, `character-bible.md` §6 | entity có UUID media_id |
| 8 | **Video R2V**: clip khó nhất trước, rồi clip mốc, rồi cả loạt ⛔ hỏi trước mỗi lượt | `flowkit-pipeline.md` §5 | clip 720p |
| 9 | **Review 720p** (`/fk-review-video` + Review Board :8200) ⛔ user duyệt từng clip → upscale 1080p → xóa logo → concat | `flowkit-pipeline.md` §6 | bản 1080p clean |
| 10 | **Hậu kỳ**: cắt tại khung che + J-cut, nhạc duck dưới thoại, card chữ, bíp, master −14 LUFS | `post-and-publish.md` §1, `cinematic-toolkit.md` §6–7 | video final |
| 11 | **Đóng gói YouTube** + chiến lược kênh | `post-and-publish.md` §2–4 | tiêu đề, mô tả, thumbnail |

Long-form → ghi `output/<slug>/script.md` (cập nhật dần theo Act); Shorts → trả thẳng trong chat. Chỉ dựng dự án FlowKit (bước 6) sau khi user duyệt kịch bản.

### Mặc định đầu vào (bước 0)

| Thông số | Mặc định |
|---|---|
| Thời kỳ + địa điểm + năm | **bắt buộc, chính xác tới năm** (`Rome, 79 AD`, `Xianyang, Qin dynasty China, 211 BC`) — từ chung chung làm AI trộn thời kỳ |
| Độ dài | Long-form ~10 phút ≈ 38–42 beat × ~15s (mỗi beat = 2 scene 8s); Shorts 45–60s ≈ 4–6 scene 8s |
| Ngôn ngữ thoại | English; dân bản địa nói ngôn ngữ không hiểu được |
| Nhân vật | Vlogger nữ ngoại quốc ngoại hình nổi bật, mặc trang phục thời kỳ ngay từ clip đầu |
| Tỉ lệ khung | HORIZONTAL 16:9 (long-form) hoặc VERTICAL 9:16 (Shorts); mọi ảnh ref đều 16:9 |
| Material | `prehistoric_vlog` (hoặc `<era>_vlog`), `documentary_footage` hoặc `realistic`; **TUYỆT ĐỐI CẤM material chứa chữ phone (như `phone_vlog`)** |

Chỉ học format; không sao chép tên, ngoại hình hay lời thoại nhân vật của kênh gốc user đưa làm ví dụ.

## Định dạng output (theo đúng thứ tự)

1. **Giả định** (3–5 dòng).
2. **Character Bible** — `CHARACTER_LOCK` + `voice_description` + `VOICE_LOCK` + bảng nhân vật (cột `Voice` cho nhân vật phụ có thoại).
3. **Bảng beat** (thật hoặc bịa).
4. **Bảng chuỗi nhân quả sinh tồn** + **outline** cold open / 5 Act + thời lượng.
5. **Storyboard toàn bộ clip** + **bảng vật lý** ⛔ user duyệt.
6. **Clip JSON từng clip** (long-form theo từng Act, hỏi trước khi sang Act sau).
7. **Ghi chú hậu kỳ + gói YouTube.**

## ⚠️ KHÓA BẮT BUỘC 5 SUBAGENT VIẾT KỊCH BẢN & CÁC SKILL ĐIỆN ẢNH (RULE 50 — LOCK CỨNG PHẢI DÙNG)

Mọi dự án POV / Time-Travel Vlog (`/fk-time-travel-vlog`, `/fk-vlog-guide`, `/fk-vlog-japan`) **BẮT BUỘC** phải vận hành 5 skill dưới đây làm **SUBAGENT CHUYÊN TRÁCH** để lấy output chuẩn trước khi viết Kịch bản, Storyboard và Video Prompt (Bước 3, 4, 5). **AI AGENT TUYỆT ĐỐI KHÔNG ĐƯỢC PHÉP BỎ QUA HOẶC TỰ BỊA KỊCH BẢN MÀ KHÔNG DÙNG OUTPUT CỦA 5 SUBAGENT NÀY**:

### 1. Bộ 5 Subagent Bắt Buộc Để Lấy Output Viết Kịch Bản

| Subagent Chuyên Trách | Vai Trò & Output Cung Cấp Cho Kịch Bản (Lock Cứng) |
|---|---|
| **`fk-action-choreography`** | **Subagent Vũ Đạo Hành Động & Cơ Học Vật Lý**: <br>• *Nhiệm vụ*: Rà soát và loại bỏ 100% bẫy biến dạng (CẤM 360°, CẤM đâm xuyên thịt/máu me, CẤM cận chiến vật lộn giáp lá cà người vs thú lớn theo Lesson 62). <br>• *Quy tắc 3 pha*: Mọi clip hành động/sinh tồn phải chia đúng 3 pha: `0-3s` Chuẩn bị/Hạ trọng tâm $\to$ `3-6s` Một vector hành động dứt khoát $\to$ `6-8s` Thu thế & chấn động tiêu tán. <br>• *Output cung cấp*: Khối mô tả hành động 3 pha và tương tác cơ học vật lý an toàn đưa trực tiếp vào `video_prompt`. |
| **`fk-add-material`** | **Subagent Chất Liệu Hình Ảnh & Visual Profile**: <br>• *Nhiệm vụ*: Xác định và cấu hình Image Material chuẩn cho project (`prehistoric_vlog`, `documentary_footage`, `realistic`). **Tuyệt đối CẤM** dùng material chứa token `phone` (`phone_vlog` - Lesson 63) khiến AI tự vẽ điện thoại 3D ngoài đời thực. <br>• *Output cung cấp*: Thiết lập `style_instruction`, `scene_prefix` và `lighting` chuẩn áp dụng đồng bộ cho toàn bộ entity và scene của video. |
| **`fk-cinematic-transitions`** | **Subagent Kỹ Thuật Nối Cảnh & Chuyển Màn**: <br>• *Nhiệm vụ*: Thiết kế logic chuyển cảnh chuẩn vlog chân thực: Match-on-action (khớp tư thế cuối clip trước theo Rule 44), Foreground wipe (vật lướt qua che ống kính cho POV), Swing/Whip-pan (lia máy nhòe chuyển động cho Selfie), J-cut âm thanh (tiếng clip sau vào sớm 0.5s). **CẤM TUYỆT ĐỐI** bumper, dip-to-black, crossfade làm mất tính vlog thật. <br>• *Output cung cấp*: Thiết kế liên kết chuỗi cảnh và `transition_prompt` đưa vào Storyboard và `clips.json`. |
| **`fk-gen-narrator`** | **Subagent Biên Kịch Thoại & Khẩu Hình Bản Địa**: <br>• *Nhiệm vụ*: Chuẩn hóa số từ tiếng Anh của Vlogger theo chuẩn Time-Travel Vlog Mode: **20–25 từ / clip 8s** (khớp chính xác 7.0–7.5s giọng Laomedeia, Lesson 62 & 65). BẮT BUỘC chia đều 3 mốc thời gian (`0-3s`, `3-6s`, `6-8s`) và bắt đầu nói ngay từ 0.0s (Lesson 65). Áp dụng **Sonic Isolation (Im lặng tuyệt đối 0 từ)** khi rình mồi / rình săn / tập trung cao độ. Dân bản địa không nói tiếng Anh, chỉ dùng cử chỉ hoặc âm gằn ngực tự nhiên. <br>• *Output cung cấp*: Cặp trường `narrator_text` và lời thoại nhúng trong `video_prompt` khớp từng giây. |
| **`fk-camera-guide`** | **Subagent Đạo Diễn Hình Ảnh & Quang Học Camera**: <br>• *Nhiệm vụ*: Thiết lập quang học Smartphone Vlog tự nhiên (0.5x ultra-wide, horizontal 16:9, vertical bounce nảy dọc theo bước chân, rotational lag khi xoay người, cấm góc nhìn gimbal/flycam bay lơ lửng). Kiến trúc prompt 5 tầng (Layer 1: Chủ thể $\to$ Layer 2: Lực tiếp xúc $\to$ Layer 3: Quán tính thứ cấp $\to$ Layer 4: Phản ứng môi trường $\to$ Layer 5: Động học camera). Phân bổ tỷ lệ góc máy vàng (Golden Camera Ratio theo Lesson 66: POV ~35%, OTS ~35%, FIXED ~15%, SELFIE ~15%). <br>• *Output cung cấp*: Cỡ cảnh, vị trí đặt máy, quang học camera và bảng vật lý cho từng cảnh. |

### 2. Các Skill Điện Ảnh Bổ Trợ & Đóng Gói

| Skill | Vai Trò |
|---|---|
| **`/fk-character-bible`** | **Khóa trang phục thời kỳ (`OUTFIT LOCK`)**: Quản lý trạng thái trang phục, dùng `<V> Body` đã mặc hoàn chỉnh. Cấm tuyệt đối đồ tập gym, áo ba lỗ hiện đại. |
| **`/fk-sound-design`** | **Hậu kỳ âm thanh**: Ducking nhạc nền tự động dưới thoại/foley; master chuẩn YouTube -14 LUFS / -1 dBTP; chạy `scripts/sfx_layering.py` bổ sung tiếng bước chân, gió bão. |
| **`/fk-capcut-edit`** | **Dựng Intro Trailer Hook**: Dùng `scripts/trailer_cuts.py` dựng trailer 30s/45s trước khi ghép master. |
| **`/fk-research`** | Tùy chọn, gom ý tưởng hình ảnh và bối cảnh lịch sử. |
| **`/fk-review-video` / `/fk-review-board`** | Duyệt video 720p thô trước khi upscale 1080p và xóa watermark. |
| **`/fk-youtube-seo` / `/fk-thumbnail`** | Đóng gói metadata và thumbnail YouTube chuẩn SEO. |
| **`/fk-doctor`** | Chẩn đoán và sửa lỗi toàn bộ pipeline. |

Không dùng: `/fk-gen-chain-videos` (unsupported), `/fk-gen-images` cho clip có vlogger (R2V không cần start frame), `/fk-gen-text-overlays` và `/fk-concat-fit-narrator` với text overlay/crossfade.

Không dùng: `/fk-gen-chain-videos` (unsupported), `/fk-gen-images` cho clip có vlogger (R2V không cần start frame), `/fk-gen-text-overlays` và `/fk-concat-fit-narrator` với text overlay/crossfade.

## Lỗi hay gặp

| Lỗi | Sửa |
|---|---|
| Thiết bị quay hiện ra trong hình | Xóa mọi từ chỉ thiết bị, kể cả "no phone"; chỉ tả góc nhìn + tay trống (Bài học 9, 33) |
| Vật tự hiện ra / biến mất giữa clip | Khối "already in place from the very first frame" liệt kê mọi người/vật ở giây 0 (Bài học 48) |
| Người bản địa mấp máy miệng theo giọng vlogger | Khóa miệng hoặc cho họ sub-clip nói riêng; test 1 clip trước (Bài học 49) |
| Clip ra 10s thay vì 8s | PATCH `duration` sau khi POST scene (Bài học 12) |
| Outfit trôi / lộ da Body trần | Dùng `<V> Body` đã mặc outfit + ID-LOCK; không gửi Body trần (Bài học 60) |
| Thoại bị cắt hoặc có khoảng lặng chết | Đếm lại 18–22 từ theo sub-clip (Rule 49) |
| Thêm lỗi mới khi review | Ghi bài học mới vào `production-lessons.md` **và** thêm dòng checklist B ở `prompt-lock.md` |

## Bản đồ mục cũ → file mới

Các bài học, memory và skill khác có thể còn trỏ "mục N" của bản skill một file cũ:

| Mục cũ | Giờ ở |
|---|---|
| Hư cấu được phép, Story Engine tóm tắt | Khóa cứng (trên) + `references/story-engine.md` |
| 0 Đầu vào, 1 Time Capsule | Mặc định đầu vào (trên) |
| 1b Trend đang lên | `references/post-and-publish.md` §4 |
| 2, 2b Character Bible, nhân vật phụ | `references/character-bible.md` |
| 3 Ethnicity & Period Lock | `references/shots-and-realism.md` |
| 4 Research Pack | `references/era-research.md` |
| 5, 5a, 5b, 5c 7 hồi / 23 beat / Survival Preset | `references/structure-7-acts.md` |
| 6 Storyboard, 8 chữ trên hình, 9 chân thực | `references/shots-and-realism.md` |
| 7 Chuyển cảnh (7a cách nối) | `references/transitions.md` (7a → `references/flowkit-pipeline.md` §1) |
| 10 Clip JSON | `references/prompt-templates.md` + `references/flowkit-pipeline.md` §2 |
| 10b Prompt Lock | `references/prompt-lock.md` |
| 11 Bài học sản xuất | `references/production-lessons.md` (giữ nguyên số bài) |
| Bằng chứng video mẫu | `references/structure-7-acts.md` §5 + `references/reference-analysis.md` |
| 🛠️ Bước 0–4.9 FlowKit | `references/flowkit-pipeline.md` |
| Bước 5–7 hậu kỳ, YouTube, mồi thuật toán | `references/post-and-publish.md` |
