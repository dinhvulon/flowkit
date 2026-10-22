---
name: fk-film
description: "Narrative film / series orchestrator (third-person cinematic, structured JSON prompts, Omni Flash r2v) — dùng khi làm phim hoặc series kể chuyện ngôi thứ ba (ví dụ EMBERS, phim cháy rừng): story bible, kịch bản, storyboard, prompt JSON, dựng dự án FlowKit, refs, sinh và review clip, hậu kỳ."
---

# fk-film — Phim kể chuyện ngôi thứ ba (Narrative Film / Series Orchestrator)

Phim hoặc series kể chuyện bằng **máy điện ảnh ngôi thứ ba**: người xem vô hình, máy không bao giờ hiện ra, nhân vật không nói với ống kính. Kết quả: `story-bible.md` → `script.md` (storyboard + bảng vật lý) → `paper_edit.md` → prompt Structured JSON → dự án FlowKit chạy **Omni Flash R2V Ingredients**. Dự án đang chạy theo skill này: EMBERS (`output/embers/`, phim cháy rừng, nhân vật Nora, Ray, Eli).

Phim giữ người xem nhờ 3 thứ: **nhân vật có muốn và cần mâu thuẫn nhau** (xung đột thật, không giải thích bằng lời), **thế giới tin được** (chất liệu thật, lửa và khói đúng vật lý, không CGI), và **chuỗi nhân quả leo thang** tới payoff. Cảnh nào không phục vụ 3 thứ đó thì cắt.

**Quy chuẩn điện ảnh ngôi thứ ba:** Không dùng góc quay POV/selfie, không cầm máy điện thoại, không nhân vật nói với ống kính, không độc thoại kiểu YouTuber. Mọi góc máy đều là góc nhìn điện ảnh khách quan (Third-person cinematic camera).

## Thứ tự ưu tiên khi các nguồn mâu thuẫn

1. `CLAUDE.md` và memory của user.
2. Mục **Khóa cứng** bên dưới.
3. `references/production-lessons.md` — bảng §1 (phim) trước, rồi bài học số lớn / ngày mới thắng bài cũ.
4. `story-bible.md` / `script.md` của dự án (nguồn sự thật về truyện, thoại, nhân vật) và `references/prompt-lock.md` (câu chữ prompt).
5. Các reference còn lại trong thư mục `skills/fk-film/references/`.

Đường dẫn `references/…` tính từ thư mục skill này: `skills/fk-film/`.

## Khóa cứng (tóm tắt luật hiện hành — chi tiết ở reference ghi kèm)

| Chủ đề | Luật | Chi tiết |
| --- | --- | --- |
| Sự thật & hư cấu | Phim dựa trên sự kiện, nơi chốn, người thật → **`/fk-research` trước khi viết** (Rule 14); người nổi tiếng thật đổi thành bí danh vai trò (Rule 15). Phim hư cấu ghi rõ là hư cấu trong `story-bible.md`; vẫn phải trông đúng thời kỳ, không biếm họa dân tộc / tôn giáo | CLAUDE.md Rule 14, 15, `era-research.md` |
| Góc máy | Máy điện ảnh ngôi thứ ba: `camera.viewpoint` = `third-person cinematic camera; the camera itself is never seen`. Cỡ cảnh, ống kính, máy cố định hay di chuyển chọn theo nhịp kịch (`/fk-camera-guide`). Không 2 clip liền nhau trùng cỡ cảnh + góc máy | `prompt-lock.md` khung A, Rule 42 (4) |
| Prompt | Structured JSON (`camera`, `style`, `setting`, `characters`, `timeline_action`, `speech`, `post_vo`, `dramatic_craft`, `audio`, `negative_constraints`, `props_lock`), viết qua `/fk-script-to-prompts`, lint `tools/lint_prompt.py` đạt 0 Critical/High, rồi `/fk-review-prompt` | Rule 55, 56, `prompt-lock.md` |
| Sinh video | **R2V Ingredients** (`GENERATE_VIDEO_REFS`, `abra_r2v_<N>s`, `MZZa6b`); `N` lấy từ `duration` — luôn PATCH `duration` | `flowkit-pipeline.md` |
| Diễn viên | Chỉ người lớn (≥19 tuổi): Flow từ chối nhân vật vị thành niên | memory "No minor characters" |
| Bộ ref nhân vật | `<Tên>` (mặt) + `<Tên> Body <trạng thái trang phục>` (Body đã mặc đồ, EDIT 1 lần từ Body gốc; ví dụ `Nora Body Ranch`). Không entity Outfit riêng. Tối đa 7 ref/clip; ref cho mọi người / thú / bối cảnh cần nhất quán có trong khung; `character_names` là TÊN entity. Ref nhân vật và sinh vật là Turnaround Sheet 16:9 (`/fk-character-design`) | Rule 46, 58, `character-bible.md` §5–7, Bài 60, 88 |
| Khóa mặt & trang phục | Nhắc chip ref ngay trong câu khóa: `Nora's face is exactly the face in {{ref:Nora}}, kept 1:1 …`; không tả lại mặt, makeup, trang phục bằng chữ. Phần dễ trôi (tay áo, quần khi ngồi, gấu áo) chốt bằng câu khóa trỏ về ref | Rule 52 (2), 64, memory "Face lock = reference only", Bài 74, 78 |
| Giọng | Mỗi nhân vật có thoại một voice id riêng (30 giọng ở `voice-bible.md` §0), ghi `speech.voices`; Slot 7 mang nhiều giọng theo thứ tự nói | `voice-bible.md` §0–0b, prompt EMBERS |
| Thoại | Lấy nguyên văn từ `script.md`. Số từ theo `duration` (Rule 49 bảng (0)): 4s 0 hoặc 6–8 · 6s 12–15 · 8s 18–22 · 10s 24–28 (memory: 23–25 từ → 10s). Nói từ giây 0; mặt người nói phải thấy khi nói. Rình / ẩn nấp → Sonic Isolation, 0 từ | Rule 49, 54, `voice-bible.md` §2 |
| Thoại ngoài hình | Lời qua bộ đàm / điện thoại / lời dẫn → `post_vo`, thêm khi dựng; clip im lặng không để bộ đàm hiện trên hình | Bài 99 |
| Cảnh tranh cãi | To, gắt, cộc ở cả `speech.delivery` lẫn nhịp timeline; không `low / quiet / voice drops / flat` | Bài 101 |
| Thoại bị chặn | Không cho nhân vật nói chuyện trả tiền / mua bán (Flow chặn im lặng, ghost op); đưa ý đó vào `post_vo` / phụ đề | Bài 100 |
| Độ dài clip | Dễ lỗi liền mạch (chuyển động nhanh, tương tác thú, ngã, sinh vật lớn đi ngang, VFX, vật vỡ/đứt) → **chuỗi 4s `a → b → c`**, cùng vị trí máy, cỡ cảnh, `setting`, ánh sáng, bộ ref; clip sau mở đúng tư thế clip trước kết thúc. Có đổi góc / chuyển cảnh → tách Scene ID riêng. Dễ → 8s; long take / master / cảnh cuối → 10s; lưng chừng → 6s | Rule 44, 49 (0), Bài 71 |
| Vật lý & đạo cụ | Mọi người / vật có mặt từ giây 0; một tay — một đạo cụ suốt clip; đạo cụ xuất hiện ở ≥2 clip có một câu tả chuẩn; dây hai người cùng cầm là một sợi liền; ghi đường đi quanh vật cản; "suýt chạm" ghi khoảng cách bằng cm; không giáp lá cà với thú lớn | Bài 48, 70, 94, 96–98, Rule 51 (1) |
| Gọi tên là hiện ra | Model không hiểu phủ định: không gọi tên vật / thú / lửa / thiết bị mà mình không muốn thấy, kể cả trong thoại và audio | Bài 73, 77, 99 |
| Lửa, khói, chất liệu | `35mm film, cinematic documentary realism`; không CGI, không lửa hoạt hình, không khói thở / hơi nước trắng, không god rays; nguồn sáng ghi rõ chỗ; sinh vật da thật không bóng nhựa | Rule 57, 59, 61, 62, Bài 73, 75 |
| Ánh sáng & người | Ánh sáng tự nhiên, chống glamour (không beauty filter, không tạo dáng người mẫu); deep focus khi cần thấy bối cảnh | Rule 61 (1)(2), 62 (3) |
| Start Frame | Clip nối tiếp trực tiếp (cùng địa điểm, khoảnh khắc, góc máy, cỡ cảnh) → `PREV_LAST_FRAME`; chuyển cảnh → storyboard 2×2 theo `/fk-storyboard` (Rule 69, bắt buộc từ 22/10/2026), panel 1 làm khung mở đầu, tẩy logo, user duyệt. Không sinh start frame đơn lẻ | Rule 27, 28, 63, 65 |
| Chuyển cảnh | Cắt thẳng, match on action, J-cut / L-cut theo `/fk-cinematic-transitions`; không crossfade làm nhạt nhịp trừ khi kịch bản chủ đích | `transitions.md` (phần phim), Rule 44 |
| Chữ trên hình | Không viết vào prompt (`negative_constraints` cấm chữ); title / phụ đề chèn hậu kỳ | `post-and-publish.md` |
| Cổng duyệt | Hỏi trước **mỗi** bước sinh; dừng sau mỗi bước cho user duyệt; lỗi thì đề xuất, không tự sinh lại. Clip lỗi nhìn thấy được → sinh lại, không "cắt khi dựng" | Rule 29, memory "Regen, never trim" |
| Ngưỡng giữ clip | EMBERS v7: điểm AI ≥ 8 thì giữ cho user xem; dự án cũ ≥ 9; thấp hơn → sửa prompt + đề xuất regen | memory "Keep threshold" |
| Review thoại | Mọi lần review chạy `tools/review_dialogue.py` (Whisper) trước khi chấm điểm | Rule 67 |
| Nhịp request | Theo CLAUDE.md Rule 10 và memory về nhịp gửi; dừng ngay khi `UNUSUAL_ACTIVITY` / `QUOTA`; kiểm ghost tối đa 2 lần mỗi clip | Rule 10, Bài 54, 100 |

## Quy trình

Mỗi bước: đọc reference ghi kèm **trước khi** làm. Bước có ⛔ là cổng — dừng chờ user.

| # | Bước | Đọc | Ra |
| --- | --- | --- | --- |
| 0 | **Đầu vào** — tối đa 1 lượt hỏi, còn lại dùng mặc định (bảng dưới) và ghi rõ giả định | — | 3–5 dòng giả định |
| 1 | **Research** (bắt buộc nếu dựa trên sự kiện / nơi chốn thật): `/fk-research`, lưu `.omc/research/` | `era-research.md`, `skills/fk-research.md` | gói research |
| 1.5 | **Gói trước khi viết**: 3 tiêu đề + 3 ý tưởng thumbnail + 1 câu lời hứa cho mỗi cặp, theo ngôn ngữ thoại (Rule 20) ⛔ user chọn 1 → ghi `- **Package:** …` vào đầu `script.md` | `skills/fk-youtube-seo.md` Step 3, `skills/fk-thumbnail-guide.md`, `post-and-publish.md` §2 | dòng `Package` |
| 2 | **Story bible** qua `/sw-workflow` (`/sw-premise-theme`, `/sw-story-structure`, `/sw-character-conflict`; series: `/sw-series-engine-bible`, `/sw-series-structure`) ⛔ | `/sw-story-structure`, `/sw-premise-theme` | `output/<slug>/story-bible.md` |
| 3 | **Nhân vật & sinh vật**: bảng nhân vật (tuổi ≥19, dấu nhận diện, trạng thái trang phục theo cảnh, voice id), thiết kế Turnaround Sheet bằng `/fk-character-design`, `CHARACTER_LOCK` cho từng người | `skills/fk-character-design/SKILL.md`, `character-bible.md` §1, §5–7, `voice-bible.md` §0–0b, `cinematic-toolkit.md` §0, §4 | bảng nhân vật trong `script.md` |
| 4 | **Kịch bản + storyboard + bảng vật lý**: `/sw-scene-craft`, `/sw-dialogue`, `/fk-scriptwriter`, `/fk-camera-guide`, `/fk-action-choreography`, `/fk-cinematic-transitions`. Cột `Dur` (4/6/8/10), cột `SF` (start frame), sổ liên tục bối cảnh ⛔ user duyệt | `shots-and-realism.md` (phần phim), `transitions.md` (phần phim), `cinematic-toolkit.md` §1–3 | `script.md` |
| 4.5 | **Dựng trên giấy** (`/fk-paper-edit`): bấm giờ, số từ Rule 49, lời hứa trong 30s, móc giữ chân ≤ 90s, đề xuất cắt ⛔ | `skills/fk-paper-edit.md` | `paper_edit.md` |
| 5 | **Prompt JSON** qua `/fk-script-to-prompts` theo khung A + checklist B của `prompt-lock.md`; long-form xuất từng Act, ⛔ hỏi trước khi sang Act sau | `prompt-lock.md`, `production-lessons.md` §1 | `prompts_<act>.json` + `vn_<act>.json` |
| 5.5 | **Cổng QC** (bắt buộc, 100% prompt): 4 bộ kiểm §QC dưới → checklist B → `python tools/lint_prompt.py --file …` → `/fk-review-prompt` (đọc lại toàn bộ, mục D) | §QC dưới, `prompt-lock.md` mục D | prompt đã viết lại + báo cáo tự kiểm |
| 6 | **Dựng dự án FlowKit**: pre-flight, flush PENDING (Rule 21), project + material + entities, video, scenes, PATCH `duration` + `narrator_text` | `flowkit-pipeline.md` §2–3 | project / video / scene ids |
| 7 | **Refs**: mặt, Body đã mặc đồ cho từng trạng thái trang phục, sinh vật, bối cảnh — Turnaround Sheet 16:9 (Rule 58), xóa logo, upload lại ⛔ hỏi trước khi sinh, ⛔ user duyệt ảnh | `flowkit-pipeline.md` §4, `character-bible.md` §6 | entity có UUID media_id |
| 7.5 | **Start Frame** theo Rule 65: chuyển cảnh → **storyboard 2×2 bắt buộc** theo `/fk-storyboard` (Rule 69), panel 1 làm khung mở đầu; nối tiếp → `PREV_LAST_FRAME` → tẩy logo → Review Board ảnh ⛔ | CLAUDE.md Rule 22, 25, 27, 63, 65 | start frame sạch |
| 8 | **Video R2V**: clip khó nhất trước, rồi clip mốc, rồi cả loạt ⛔ hỏi trước mỗi lượt | `flowkit-pipeline.md` §5 | clip 720p |
| 9 | **Review 720p**: `/fk-review-video` + `tools/review_dialogue.py` (Whisper) + Review Board :8200 ⛔ user duyệt từng clip. Clip rớt → quay lại 5.5, sửa đúng khối gây lỗi, lint, đề xuất regen → upscale 1080p → xóa logo | `flowkit-pipeline.md` §6, Rule 32, 67 | bản 1080p clean |
| 10 | **Hậu kỳ**: `/video-editing` (Rule 66) + `/fk-capcut-edit` + `/fk-cinematic-transitions` + `/fk-sound-design` (−14 LUFS / −1 dBTP); `post_vo` và phụ đề thêm ở đây | `post-and-publish.md` §1, `cinematic-toolkit.md` §6–7 | `${OUTDIR}/edit/edit_vN` |
| 11 | **Đóng gói YouTube** (tinh chỉnh từ bước 1.5) → sau đăng 48h và 7 ngày: `/fk-youtube-analytics` | `post-and-publish.md` §2–4, `skills/fk-youtube-analytics.md` | tiêu đề, mô tả, thumbnail |

Long-form → ghi `output/<slug>/` (cập nhật dần theo Act); Shorts → trả thẳng trong chat. Chỉ dựng dự án FlowKit (bước 6) sau khi user duyệt kịch bản.

### §QC — Cổng review & viết lại prompt (bước 5.5)

Kho phương pháp: `skills/character-scene-design-skills-main/` (repo tham chiếu — **đọc, không copy về**). Luật của skill này luôn thắng khi mâu thuẫn; repo chỉ cung cấp **cách soi và cách viết lại**.

Chạy **4 bộ kiểm theo đúng thứ tự** này, mỗi bộ là một lượt quét qua toàn bộ prompt của Act:

| # | Bộ kiểm | Đọc | Soi cái gì | Viết lại thế nào |
| --- | --- | --- | --- | --- |
| Q1 | **Proportion lock** | `skills/character-design/SKILL.md` → _Production Asset Pipeline_ b1 + b4 (_W0 turnaround contract_) | Chạy **một lần trước khi sinh ảnh Body** của mỗi nhân vật chính, không phải mỗi clip. Các panel của sheet có giống "một người xoay" không: net height, head ratio, width-to-height, leg ratio, foot baseline | Chốt 5 con số đó **thành câu chữ** trong prompt ảnh Body |
| Q2 | **Permanent prop geometry** | cùng file → b3 | Mọi đạo cụ cố định (bộ đàm, mũ bảo hộ, dao, bình nước, dây dắt) trong prompt **ảnh ref**. Có bị tả chung chung → trôi thành vật generic giữa nhiều clip không | Tả bằng **hình học + bên đeo + cách gắn + chất liệu + mặt trước/sau**, nêu rõ **nó KHÔNG phải cái gì**. Chỉ trong prompt ảnh — `video_prompt` vẫn trỏ ref (Rule 52 (2)). Đạo cụ ở ≥2 clip: **một câu tả chuẩn** dùng nguyên văn ở mọi clip + đính ref chứa nó (Bài 94) |
| Q3 | **Bone And Face Structure Layer** | cùng file | Bảng nhân vật: có ≥2 người dễ bị trộn mặt không (cùng giới, cùng tuổi, cùng màu tóc) | Mỗi người khác ít nhất **2 trong**: face envelope, cheek/jaw, eye geometry, hairline, skin texture, posture. Ghi vào cột dấu nhận diện; người đứng sát nhau thêm câu "nobody is a copy of …" (Bài 76) |
| Q4 | **Scene continuity ledger** | `.agents/skills/scene-design/SKILL.md` → _base location vs scene state_ + trường của _scene continuity ledger_ | Mỗi địa điểm xuất hiện ≥5 clip: trạng thái có chạy **một chiều** không; dấu vết (tro, bỏng, bùn, vết cháy lan) có bị "reset sạch" giữa các clip không | Sổ 2 tầng trong `script.md`: **base scene** + **bậc trạng thái** S0→Sn, ghi clip nào dùng bậc nào. Trạng thái kế thừa của clip trước là đầu vào bắt buộc của `characters[].state` và `setting` ở clip sau |

Sau 4 bộ kiểm → checklist B (`prompt-lock.md`) → `python tools/lint_prompt.py` → phải 0 lỗi Critical/High mới được lưu.

**Bỏ qua** trong repo đó: short-drama / casting dọc 9:16, `references/full-manual.md`, `SECTIONS/`, `scene-illustration-workflow/`, và mọi đường dẫn `/Users/baimengke/...` (không tồn tại trên máy này).

### Mặc định đầu vào (bước 0)

| Thông số | Mặc định |
| --- | --- |
| Bối cảnh | **bắt buộc, cụ thể tới năm và nơi chốn** (`Northern California foothills, 2020s, fire season`) — từ chung chung làm model trộn thời kỳ |
| Độ dài | Theo `story-bible.md`. Tính runtime theo thời lượng dùng được: 4s→3.5s, 6s→5s, 8s→7s, 10s→9s |
| Ngôn ngữ thoại | English. Tiếng Tây Ban Nha Mỹ Latinh → `references/dialogue-es-latam.md` + `dialogue-es-mx-ca.md` (prompt vẫn tiếng Anh, chỉ thoại trong ngoặc kép là tiếng Tây Ban Nha) |
| Nhân vật | Người lớn ≥19 tuổi; mỗi nhân vật chính có ref mặt + Body theo từng trạng thái trang phục; mỗi người có thoại một voice id |
| Tỉ lệ khung | HORIZONTAL 16:9 (long-form) hoặc VERTICAL 9:16 (Shorts); mọi ảnh ref 16:9 (Rule 5) |
| Material | `realistic`, `documentary_footage` hoặc material riêng của phim tạo bằng `/fk-add-material` |

## Kiến trúc tiền kỳ 3 tầng

```
[Ý tưởng]
   │
   ▼
[TẦNG 1: story-bible.md] ◄── /sw-workflow điều phối:
   │                          • /sw-premise-theme: premise, theme, misbelief
   │                          • /sw-story-structure: khung hồi, plot point, midpoint
   │                          • /sw-character-conflict: want vs need, đối thủ, xung đột
   ▼
[TẦNG 2: script.md + ref_prompts.json] ◄── kịch bản + storyboard:
   │                          • bảng nhân vật, material, mốc ánh sáng
   │                          • storyboard từng clip (Clip | Dur | Shot | Ref | SF | Sáng | Hình | Thoại | Từ | Việc | Beat | Dựng)
   │                          • bảng vật lý (/fk-action-choreography) + sổ liên tục bối cảnh
   │                          • ref_prompts.json: prompt ảnh ref nhân vật, Body, sinh vật, bối cảnh
   ▼
[TẦNG 2.5: paper_edit.md] ◄── /fk-paper-edit: bấm giờ, Rule 49, lời hứa 30s, móc giữ chân, đề xuất cắt ⛔
   ▼
[TẦNG 3: prompts_<act>.json + vn_<act>.json] ◄── /fk-script-to-prompts (Rule 56):
                              • Structured JSON theo khung A của prompt-lock.md
                              • lint_prompt.py + /fk-review-prompt đạt 0 lỗi, user duyệt trước khi sinh
```

## Định dạng output (theo đúng thứ tự)

1. **Giả định** (3–5 dòng).
2. **Story bible** — `output/<slug>/story-bible.md` ⛔.
3. **Bảng nhân vật & sinh vật** + `CHARACTER_LOCK` từng người + kế hoạch ref (mặt, Body theo trạng thái trang phục, sinh vật, bối cảnh).
4. **Storyboard toàn bộ clip** + **bảng vật lý** + sổ liên tục ⛔ (`script.md`).
5. **Báo cáo dựng trên giấy** — `paper_edit.md` ⛔.
6. **Bảng prompt ảnh ref** — `ref_prompts.json` ⛔ user duyệt trước khi sinh media.
7. **Prompt JSON từng clip** — qua [`/fk-script-to-prompts`](../fk-script-to-prompts/SKILL.md), lint + review, xuất `prompts_<act>.json` + `vn_<act>.json` (theo từng Act).
8. **Ghi chú hậu kỳ** (`post_vo`, điểm cắt theo mốc Whisper, nhạc) + **gói YouTube**.

## Bộ skill phối hợp

| Skill | Vai trò trong phim |
| --- | --- |
| `/sw-workflow` + `sw-*` | Story bible, cấu trúc, nhân vật, cảnh, thoại (Tầng 1–2) |
| `/fk-character-design` | Turnaround Sheet 16:9 cho nhân vật và sinh vật chủ chốt, 5 lớp DNA anchor (Rule 58) |
| `/fk-character-bible` | Ma trận trạng thái trang phục theo cảnh, series manifest |
| `/fk-scriptwriter` | Nhịp cảnh, cảm xúc bằng triệu chứng cơ thể, bộ công cụ hồi hộp |
| `/fk-camera-guide` | Ngôn ngữ máy điện ảnh, cỡ cảnh, 5 tầng vật lý trong prompt |
| `/fk-action-choreography` | Hành động 3 pha, từ vựng an toàn chống méo người, chuỗi 4s |
| `/fk-storyboard` | **Bắt buộc cho mọi clip có sinh ảnh** (Rule 69, 22/10/2026): ảnh storyboard 2×2 theo thời gian làm ref + panel 1 làm khung mở đầu (r2v); không sinh start frame đơn lẻ. Bắt buộc đọc thể ảnh storyboard thực tế để điều chỉnh camera, góc quay, vắt cảnh trong prompt video trước khi sinh (Rule 69 (7)). Clip liên tục vẫn dùng khung cuối clip trước |
| `/fk-cinematic-transitions` | Match on action, J/L-cut, mối nối giữa các clip |
| `/fk-gen-narrator` | Đếm số từ thoại theo `duration`, `narrator_text` (chế độ phim) |
| `/fk-add-material` | Material của phim (style, lighting, chống CGI) |
| `/fk-script-to-prompts` + `/fk-prompt-lock` + `/fk-review-prompt` | Chuyển kịch bản sang prompt JSON, lint, đọc lại toàn bộ |
| `/fk-paper-edit` | Dựng trên giấy trước khi tốn credit |
| `/fk-review-video` + `/fk-review-board` | Review 720p (kèm Whisper, Rule 67) trước khi upscale |
| `/video-editing` + `/fk-capcut-edit` + `/fk-sound-design` | Dựng, trailer hook, mix và master −14 LUFS |
| `/fk-youtube-seo` + `/fk-thumbnail` + `/fk-youtube-analytics` | Đóng gói và chẩn đoán sau đăng |
| `/fk-doctor` | Mọi lỗi pipeline (Rule 31) |

Không dùng: `/fk-gen-chain-videos` (Veo start+end — `UNSUPPORTED_ON_BATCH_API`).

## Lỗi hay gặp

| Lỗi | Sửa |
| --- | --- |
| Vật / người tự hiện ra hoặc biến mất giữa clip | Liệt kê mọi người / vật ở giây 0 kèm vị trí (Bài 48); không gọi tên thứ mình không muốn thấy (Bài 73, 77) |
| Nhân vật không thoại mấp máy miệng theo giọng người khác | Khóa miệng người không thoại; người nói phải hiện mặt ở đúng nhịp mình nói (Bài 49) |
| Clip ra 10s thay vì độ dài đã chọn | PATCH `duration` sau khi POST scene (Bài 12) |
| Hành động dài bị méo người / thú trôi / vật hiện-biến | Tách chuỗi 4s cùng bối cảnh, mỗi clip 1 hành động, khớp tư thế đầu-cuối (Bài 71) |
| Trang phục trôi (mất tay áo, lộ đùi khi ngồi, tua rua lạ) | Trỏ ref Body đúng trạng thái trang phục + câu khóa phần dễ trôi (Bài 74, 78) |
| Thoại bị cắt hoặc có khoảng lặng chết | Đếm lại số từ theo `duration` và theo mốc (Rule 49 bảng (0)); chạy Whisper (Rule 67) |
| Clip im lặng bị lồng một câu thoại bịa (thường qua bộ đàm) | Bỏ bộ đàm khỏi hình, câu qua bộ đàm vào `post_vo` (Bài 99) |
| Request nhận rồi biến mất (ghost op), lặp lại ở cùng clip | Kiểm ghost tối đa 2 lần; soát thoại tìm ý trả tiền / mua bán và bỏ (Bài 100) |
| Cảnh cãi nhau đọc nhỏ nhẹ, đều đều | Khóa giọng to, gắt, cộc ở `speech.delivery` và timeline (Bài 101) |
| Dây hai người cùng cầm bị đứt / nhân đôi | `props_lock` một sợi liền; lần 2 vẫn hỏng → chỉ một người cầm dây (Bài 96) |
| Tay chạm hẳn khi kịch bản là "suýt chạm" | Ghi khoảng cách cm + câu cấm chạm, clip ≥ 6s (Bài 97) |
| Nhân vật đi xuyên rào / xe / cột | Ghi đường đi so với vật cản + câu cấm đi xuyên (Bài 98) |
| Lửa / khói trông như CGI, khói thở trắng, tia nắng có khối | Khóa anti-CGI + anti-smoke, nguồn sáng ghi rõ chỗ (Rule 57, 62; Bài 75) |
| Hai nhân vật bị trộn mặt | Câu khóa chip ref cho từng người + dấu nhận diện khác nhau + "nobody is a copy of …" (Bài 76, §QC Q3) |
| Đạo cụ chính khác nhau giữa 2 clip chuyển cảnh | Một câu tả chuẩn cho đạo cụ, đính ref chứa nó; clip nối tiếp trực tiếp thì dùng `PREV_LAST_FRAME` (Bài 94, Rule 65 (2)) |
| Thêm lỗi mới khi review | Ghi bài học mới vào `production-lessons.md` (số kế tiếp) **và** thêm 1 dòng checklist B ở `prompt-lock.md` |
