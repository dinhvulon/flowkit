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
| Giọng | Chỉ vlogger có `voice_description` (Laomedeia). 1 giọng/clip | `character-bible.md` §3 |
| Nhân vật phụ | Được nói, bằng ngôn ngữ không hiểu được, ở sub-clip riêng, giọng tả bằng chữ; vlogger phản ứng với giọng điệu, **không dịch** | `character-bible.md` §4 |
| Thoại | **18–22 từ / clip 8s** (6–7 / 7–8 / 5–7 theo `0-3s / 3-6s / 6-8s`), Rule 49. Chỉ cảnh cuối và establishing shot 4s không người được 0 từ. Viết/sửa qua `/fk-gen-narrator` | `voice-bible.md` §2 |
| Thiết bị | Không viết `phone`, `smartphone`, `camera` (đạo cụ), `selfie stick`, `device`, `screen`, `gimbal` — kể cả câu phủ định. Ràng buộc là câu khẳng định, không dòng `Negative:` | `prompt-lock.md` #16 |
| Góc máy | 1 shot = 1 góc (selfie **hoặc** POV **hoặc** máy dựng). Cấm lật 180° trong shot. Hành động hai tay → POV hoặc máy dựng | `prompt-lock.md` khối 1 |
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
| 3 | **Outline**: chuỗi nhân quả sinh tồn → cold open 8s → 5 Act mỗi Act 1 câu hỏi → payoff → cảnh cuối không thoại. Kho cảnh 7 hồi / 23 beat dùng để lấy ý | `story-engine.md` (bắt buộc), `structure-7-acts.md`, `reference-analysis.md`, `cinematic-toolkit.md` §3 (hồi hộp, đổi cỡ cảnh) | outline + thời lượng |
| 4 | **Storyboard + bảng vật lý** từng clip (máy ở đâu, có gì ở giây 0, hướng + tốc độ vật di chuyển, ai rời khung bằng cách nào) ⛔ user duyệt bảng vật lý | `shots-and-realism.md`, `transitions.md` | bảng storyboard + bảng vật lý |
| 5 | **Clip JSON + `video_prompt`** theo khung 9 khối, qua checklist B; thoại qua `/fk-gen-narrator`. Long-form xuất từng Act, ⛔ hỏi user trước khi sang Act sau | `prompt-lock.md`, `production-lessons.md`, `prompt-templates.md`, `voice-bible.md` §2–6, `cinematic-toolkit.md` §1–2 (hành động 3 pha, cảm xúc) | `output/<slug>/script.md` |
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
| Material | `phone_vlog` (tạo theo `shots-and-realism.md`) hoặc `realistic` |

Chỉ học format; không sao chép tên, ngoại hình hay lời thoại nhân vật của kênh gốc user đưa làm ví dụ.

## Định dạng output (theo đúng thứ tự)

1. **Giả định** (3–5 dòng).
2. **Character Bible** — `CHARACTER_LOCK` + `voice_description` + `VOICE_LOCK` + bảng nhân vật (cột `Voice` cho nhân vật phụ có thoại).
3. **Bảng beat** (thật hoặc bịa).
4. **Bảng chuỗi nhân quả sinh tồn** + **outline** cold open / 5 Act + thời lượng.
5. **Storyboard toàn bộ clip** + **bảng vật lý** ⛔ user duyệt.
6. **Clip JSON từng clip** (long-form theo từng Act, hỏi trước khi sang Act sau).
7. **Ghi chú hậu kỳ + gói YouTube.**

## Skill liên quan

| Dùng | Khi nào |
|---|---|
| `/fk-gen-narrator` | **Bắt buộc** khi viết/sửa thoại (Time-Travel Vlog Mode, 18–22 từ) |
| `/fk-research` | Tùy chọn, gom ý tưởng hình ảnh |
| `/fk-camera-guide` | Mục "5-Layer Physical Prompt" và quang học smartphone. **Bỏ qua** bảng ống kính điện ảnh / color grade (Anamorphic, Cooke…) — trái cảm giác footage tự quay |
| `/fk-action-choreography` | Đã chuyển thành `references/cinematic-toolkit.md` §1: hành động 3 pha khớp sub-clip thoại, góc máy của vlogger, từ vựng săn/né/thú lao tới chống méo người |
| `/fk-scriptwriter` | Phần dùng được đã chuyển vào `cinematic-toolkit.md` §2–3: cảm xúc bằng triệu chứng cơ thể, vòng A→B mỗi clip, 6 kỹ thuật hồi hộp, đổi cỡ cảnh. **Không** dùng lời dẫn TTS và luật 10–12 từ của nó |
| `/fk-character-bible` | `cinematic-toolkit.md` §4–5: mỗi trạng thái trang phục = một ảnh `<V> Body …` riêng; tập mới mang theo **mặt + Body trần gốc** (mặt qua `scripts/series_manifest.py bootstrap --only "<V>"`, Body trần qua `source_media_id`), rồi EDIT ra Body mặc outfit của tập theo công thức outfit lock (`character-bible.md` §6) |
| `/fk-sound-design` | `cinematic-toolkit.md` §6: duck nhạc theo track clip + master −14 LUFS (lệnh đã test), `scripts/sfx_layering.py` khi thiếu tiếng va chạm |
| `/fk-cinematic-transitions` | `cinematic-toolkit.md` §7: J-cut khi cắt thẳng và card chữ đè lên hình (lệnh đã test). **Không** bumper, dip-to-black, crossfade, hardsub |
| `/fk-upload-ref`, `/fk-gen-refs`, `/fk-remove-watermark`, `/fk-upload-image` | Bộ ref (bước 7) |
| `/fk-review-video`, `/fk-review-board`, `/fk-concat`, `/fk-gen-music` | Bước 9–10 |
| `/fk-youtube-seo`, `/fk-thumbnail`, `/fk-youtube-upload` | Bước 11 (bật nhãn "Altered or synthetic content" bằng tay) |
| `/fk-doctor` | Bất kỳ lỗi pipeline nào |

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
