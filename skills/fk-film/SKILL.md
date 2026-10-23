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
| Khung neo / Storyboard | Clip nối tiếp trực tiếp (cùng địa điểm, khoảnh khắc, góc máy, cỡ cảnh) → `PREV_LAST_FRAME`; chuyển cảnh → **storyboard 2×2 bắt buộc** theo `/fk-storyboard` (Rule 69, bắt buộc từ 22/10/2026). BỎ cắt Panel 1 / Start Frame (Omni R2V là pure references, storyboard là Time Reference), tẩy logo, visual audit đọc thể ảnh trước khi chốt prompt video | Rule 28, 65, 69 |
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
| 3 | **Nhân vật & sinh vật**: bảng nhân vật (tuổi ≥19, dấu nhận diện, trạng thái trang phục theo cảnh, voice id), thiết kế Turnaround Sheet bằng `/fk-character-design` (Rule 72 — 35mm Live-Action Casting / Practical SFX; CẤM prompt ad-hoc, CẤM từ khóa 2D/sketch), `CHARACTER_LOCK` cho từng người | `skills/fk-character-design/SKILL.md`, `character-bible.md` §1, §5–7, `voice-bible.md` §0–0b, `cinematic-toolkit.md` §0, §4 | bảng nhân vật trong `script.md` |
| 4 | **Kịch bản + storyboard + bảng vật lý**: `/sw-scene-craft`, `/sw-dialogue`, `/fk-scriptwriter`, `/fk-camera-guide`, `/fk-action-choreography`, `/fk-cinematic-transitions`. Cột `Dur` (4/6/8/10), cột `SF` (start frame), sổ liên tục bối cảnh ⛔ user duyệt | `shots-and-realism.md` (phần phim), `transitions.md` (phần phim), `cinematic-toolkit.md` §1–3 | `script.md` |
| 4.5 | **Dựng trên giấy** (`/fk-paper-edit`): bấm giờ, số từ Rule 49, lời hứa trong 30s, móc giữ chân ≤ 90s, đề xuất cắt ⛔ | `skills/fk-paper-edit.md` | `paper_edit.md` |
| 5 | **Prompt JSON** qua `/fk-script-to-prompts` theo khung A + checklist B của `prompt-lock.md`; long-form xuất từng Act, ⛔ hỏi trước khi sang Act sau | `prompt-lock.md`, `production-lessons.md` §1 | `prompts_<act>.json` + `vn_<act>.json` |
| 5.5 | **Cổng QC** (bắt buộc, 100% prompt): 4 bộ kiểm §QC dưới → checklist B → `python tools/lint_prompt.py --file …` → `/fk-review-prompt` (đọc lại toàn bộ, mục D) | §QC dưới, `prompt-lock.md` mục D | prompt đã viết lại + báo cáo tự kiểm |
| 6 | **Dựng dự án FlowKit**: pre-flight, flush PENDING (Rule 21), project + material + entities, video, scenes, PATCH `duration` + `narrator_text` | `flowkit-pipeline.md` §2–3 | project / video / scene ids |
| 7 | **Refs**: mặt, Body đã mặc đồ cho từng trạng thái trang phục, sinh vật, bối cảnh — Turnaround Sheet 16:9 bắt buộc qua `/fk-character-design` (Rule 58, Rule 72), 35mm film still chụp người thật / quái animatronic, xóa logo, upload lại ⛔ hỏi trước khi sinh, ⛔ user duyệt ảnh | `flowkit-pipeline.md` §4, `character-bible.md` §6 | entity có UUID media_id |
| 7.5 | **Storyboard 2×2 / Khung neo** theo Rule 65 & 69: chuyển cảnh → **storyboard 2×2 bắt buộc** (Rule 69; BỎ cắt Panel 1 / Start Frame — pure R2V references) → tẩy logo → **bước 3.5 Visual Audit đọc thể ảnh thực tế để chỉnh Video Prompt** ⛔; nối tiếp → `PREV_LAST_FRAME` → tẩy logo ⛔ | CLAUDE.md Rule 28, 65, 69 | entity Storyboard sạch |
| 8 | **Video R2V**: clip khó nhất trước, rồi clip mốc, rồi cả loạt ⛔ hỏi trước mỗi lượt | `flowkit-pipeline.md` §5 | clip 720p |
| 9 | **Review 720p**: trích xuất đúng 24 frames bằng ffmpeg (`fps=24/<duration>`, contact sheet `tile=6x4`, Rule 73) + `/fk-review-video` + `tools/review_dialogue.py` (Whisper, Rule 67) + Review Board :8200 ⛔ user duyệt từng clip. Clip rớt → quay lại 5.5, sửa đúng khối gây lỗi, lint, đề xuất regen → upscale 1080p → xóa logo | `flowkit-pipeline.md` §6, Rule 32, 67, 73 | bản 1080p clean |
| 10 | **Hậu kỳ**: `/video-editing` (Rule 66 — tự động điều phối `/fk-capcut-edit` & MCP `capcut` để lập Bảng dựng và dựng trực tiếp vào timeline draft CapCut) + `/fk-cinematic-transitions` + `/fk-sound-design` (−14 LUFS / −1 dBTP); `post_vo` và phụ đề thêm ở đây | `post-and-publish.md` §1, `cinematic-toolkit.md` §6–7 | `${OUTDIR}/edit/edit_vN` |
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
[TẦNG 1: story-bible.md] ◄── /sw-workflow điều phối toàn diện:
   │                          • /sw-premise-theme: Premise, controlling idea, moral argument, logline
   │                          • /sw-genre-anatomy: Hệ thống 12 thể loại Truby, luật thể loại, genre-mixing
   │                          • /sw-story-structure: Khung 3 hồi / 4 phần, inciting incident, plot points, midpoint, climax
   │                          • /sw-truby-anatomy: 22 bước organic plot spine, four-corner opposition, moral argument chain
   │                          • /sw-character-conflict: Want vs. Need, 3D orchestration, unity of opposites, antagonism
   │                          • (Nếu là series/phim bộ): /sw-series-engine-bible, /sw-series-structure
   ▼
[TẦNG 2: script.md + ref_prompts.json] ◄── kịch bản + storyboard + ngôn ngữ điện ảnh:
   │                          • /sw-scene-craft: Beat design, value turns +/-, subtext, sensory details, objective-obstacle-tactic
   │                          • /sw-dialogue: Dialogue as action, trialogues, subtext, zero on-the-nose exposition, speech duration calibration
   │                          • /sw-format-adaptation: Spec screenplay standards, Fountain contract, active visual action lines
   │                          • /fk-scriptwriter: Nhịp kịch tính, triệu chứng cơ thể, công cụ hồi hộp (blind spots, sonic isolation)
   │                          • /fk-camera-guide: Ngôn ngữ máy điện ảnh, cỡ cảnh, ống kính, 5 tầng vật lý
   │                          • /fk-action-choreography: Bảng vật lý (physics ledger), hành động 3 pha, chuỗi 4s an toàn
   │                          • /fk-cinematic-transitions: Mối nối giữa các clip, match on action, J/L-cut
   │                          • bảng nhân vật, material, mốc ánh sáng
   │                          • storyboard từng clip (Clip | Dur | Shot | Ref | SF | Sáng | Hình | Thoại | Từ | Việc | Beat | Dựng)
   │                          • sổ liên tục bối cảnh (scene continuity ledger: S0 → Sn)
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

## Hệ Thống Từ Vựng Kỹ Thuật Video Điện Ảnh Chuẩn Hóa (Standardized Cinematic Video Taxonomy)

Mọi khâu từ tiền kỳ, thiết kế, dàn dựng bối cảnh, chọn góc máy, viết kịch bản đến prompt JSON BẮT BUỘC sử dụng chuẩn từ vựng kỹ thuật điện ảnh tiếng Anh chuẩn hóa dưới đây:

### 1. Thiết Kế Nhân Vật & Sinh Vật (Character & Creature Design)
- **16:9 Turnaround Sheet**: Bảng tạo hình đa góc 16:9 bắt buộc theo `/fk-character-design` và Rule 58 (Nhân vật: 4 panels gồm Toàn thân chính diện, Toàn thân 3/4, Toàn thân nghiêng/sau, Cận cảnh chân dung mặt/cổ; Sinh vật: 3/4 trái, 3/4 phải, Cận cảnh đầu sọ).
- **Proportion Lock**: Khóa tỷ lệ cơ thể bất biến gồm Net Height (chiều cao tịnh), Head-to-Body Ratio (tỷ lệ đầu/thân, ví dụ 1:7.5), Inseam/Leg Ratio (tỷ lệ chân), Foot Baseline.
- **Bone & Cranial Architecture**: Cấu trúc xương sọ, hốc mắt, xương gò má/quai hàm (`facial bone envelope`), diềm cổ, gai nón sừng, bất đối xứng giải phẫu nhận diện.
- **Biological Micro-Texture Layer (Rule 57)**: Chi tiết biểu bì vi mô gồm vảy đa giác dạng lát gạch (`polygonal basement scales`), gai nón sừng (`conical keratin tubercles`), rãnh máu phong hóa (`weathered hairline fissures`), nếp gấp da động học (`dewlap biological skin folds`), Subsurface Scattering (SSS) tự nhiên.
- **Wardrobe State Ladder**: Thang bậc trạng thái trang phục theo tiến trình câu chuyện (`Pristine` → `Worn/Dusted` → `Scorched/Torn` → `Mud-Caked`), khóa cứng theo từng entity `<Character> Body <State>`.
- **Permanent Prop Geometry**: Hình học đạo cụ cố định (vị trí đeo, cách móc gắn, vật liệu cứng cáp, mặt trước/sau; tả bằng hình học và nêu rõ nó KHÔNG phải cái gì).
- **Anti-Wax / Zero Plastic Sheen**: Triệt tiêu triệt để lớp bóng nhờn nhựa 3D CGI (`rough non-reflective pachyderm hide`, `matte dried alluvial clay`, không bóng nhờn studio).

### 2. Dựng Cảnh & Bối Cảnh (Mise-en-Scène & Setting)
- **Base Location vs. Scene State Ledger**: Quản lý bối cảnh 2 tầng (địa điểm gốc + bậc trạng thái S0 → Sn). Trạng thái môi trường suy thoái một chiều (tro tàn, vệt cháy, bùn đất bám tăng dần), cấm reset sạch giữa các clip.
- **Spatial Blocking & Depth Staging**: Bố trí không gian diễn xuất 3 lớp sâu gồm Tiền cảnh (Foreground - FG), Trung cảnh (Midground - MG), Hậu cảnh (Background - BG); duy trì trục hành động 180 độ (`180-Degree Axis of Action`) và tương quan đường nhìn (`Eyeline Match`).
- **Motivated Practical Lighting**: Nguồn sáng thực tế có động cơ trong khung hình (ánh lửa bập bùng, đèn bão, mặt trời xiên góc tán cây `natural dappled canopy sunlight`, ánh sáng ban ngày âm u `flat natural overcast diffuse daylight`). CẤM TUYỆT ĐỐI tia nắng đồ họa máy tính (`god rays`, `volumetric beams`) và đèn viền studio (`studio rim lighting`).

### 3. Góc Máy & Ngôn Ngữ Điện Ảnh (Cinematography & Camera)
- **Shot Scale / Framing (Cỡ cảnh)**:
  - `EWS` (Extreme Wide Shot): Đại toàn cảnh, thiết lập quy mô thiên nhiên và sự nhỏ bé của con người.
  - `WS` (Wide Shot / Establishing Shot): Toàn cảnh, xác lập không gian địa lý và vị trí các nhân vật.
  - `MS` (Medium Shot): Trung cảnh (ngang thắt lưng trở lên), cân bằng giữa hành động và biểu cảm.
  - `MCU` (Medium Close-Up): Trung cận (ngang ngực trở lên), cỡ cảnh chuẩn cho hội thoại và tương tác tâm lý.
  - `CU` (Close-Up): Cận cảnh gương mặt hoặc bàn tay, bắt trọn vi biểu cảm hoặc thao tác vật lý sống còn.
  - `ECU` (Extreme Close-Up): Đặc tả chi tiết vi mô (ánh mắt căng thẳng, mũi dao rạch, giọt mồ hôi).
  - `OTS` (Over-The-Shoulder): Góc quay qua vai người đối thoại, neo giữ chiều sâu quan hệ.
- **Camera Angle (Góc máy)**:
  - `Eye-Level`: Ngang tầm mắt, khách quan trung tính.
  - `Low-Angle`: Hất nhẹ từ dưới lên (ngang ngực), tôn dáng vóc, tạo cảm giác uy quyền hoặc áp lực sinh vật khổng lồ.
  - `High-Angle`: Chếch từ trên xuống, thể hiện sự tổn thương, cô lập, nguy nan.
  - `Dutch Angle / Canted`: Góc nghiêng trục lệch, báo hiệu tâm lý bất an, chấn động, sụp đổ trật tự.
  - `Top-Down / Bird's-Eye`: Góc nhìn thẳng từ trên đỉnh đầu nhìn xuống mặt đất, lập bản đồ di chuyển.
- **Camera Movement (Chuyển động máy)**:
  - `Static / Locked-Off`: Máy cố định trên chân máy, tăng độ căng thẳng ngột ngạt và tính quan sát tài liệu.
  - `Pan / Tilt`: Lia ngang (Pan) hoặc quét dọc (Tilt) theo hướng di chuyển của chủ thể.
  - `Dolly-In / Dolly-Out`: Đẩy máy tiến vào hoặc lùi ra theo trục sâu, kéo khán giả vào nội tâm nhân vật.
  - `Tracking / Trucking`: Máy trượt ngang song song bám theo nhân vật đang chạy hoặc chiến đấu.
  - `Steadicam / Handheld`: Cầm tay tài liệu hiện trường với độ rung lắc bước chân chân thực (`natural footfall vertical bounce and rotational lag`), cấm bay lượn trơn tuột như game 3D.
  - `Whip Pan`: Lia giật máy thần tốc tạo chuyển động mờ để cắt cảnh hoặc phản xạ đột ngột.
- **Optics & Texture (Quang học & Chất cảm)**:
  - Focal Length: 24mm/35mm (góc rộng điện ảnh, giữ chiều sâu bối cảnh), 50mm (thị giác mắt người tự nhiên), 85mm/135mm (nén hậu cảnh).
  - Depth of Field: `Deep Focus (f/8)` giữ rõ nét từ tiền cảnh đến chân trời (Rule 62); chỉ dùng `Cinematic Shallow DoF` khi cô lập cảm xúc nhân vật.
  - Texture: `35mm film grain`, `raw cinematic documentary realism`, 180-degree shutter motion blur.

### 4. Storyboard & Khung Neo (Storyboard & Visual Anchoring)
- **2×2 Time Storyboard Grid (Rule 69)**: Ảnh storyboard lưới 2×2 thể hiện 4 khoảnh khắc theo dòng thời gian (4 panels 16:9), bắt buộc cho mọi clip chuyển cảnh trong phim.
- **Panel 1 Frame 0 Anchor**: Panel trên-trái (Panel 1) của storyboard chính là neo xuất phát điểm tại giây 0 của video R2V.
- **Continuous Scene Chain (`PREV_LAST_FRAME`, Rule 65 Loại 1)**: Cắt khung hình cuối của clip trước làm Start Frame cho clip kế tiếp cùng bối cảnh/góc nhìn; cấm sinh ảnh mới.
- **Visual Audit of Storyboard Sheet (Rule 69 (7))**: Bắt buộc đọc và phân tích trực quan 4 panel storyboard thực tế trước khi chốt prompt video để khớp 100% cỡ cảnh, góc quay, nhịp cắt.

### 5. Prompt Kỹ Thuật Structured JSON (Structured Video Prompt Architecture)
Tuân thủ 5 tầng kiến trúc Structured JSON (`/fk-prompt-lock` và Rule 55):
- `camera`: Viewpoint (strictly third-person cinematic camera, invisible observer), shot scale, angle, lens, motion dynamics.
- `characters`: Inline media chip reference (`{{media:<uuid>|<file>}}`), Face Lock, Body Lock, physical and wardrobe state.
- `setting` & `style`: Macro/micro environment, practical lighting, atmospheric particles, material tags.
- `timeline_action`: Phân đoạn nhịp thời gian (`0-3s`, `3-6s`, `6-8s/6-10s`), cơ học quán tính ($p = m \cdot v$, truyền lực `force -> barrier -> ground`), biến dạng vật liệu, độ trễ thứ cấp.
- `speech` & `audio`: Thoại trực tiếp gắn nhãn nhân vật (`Character says "..."`), thông số giọng nói, âm thanh môi trường Foley, `post_vo` cho thoại ngoài hình.
- `negative_constraints`: Danh sách cấm tuyệt đối (zero CGI, zero plastic sheen, zero subtitles, zero split screen, camera never seen).

### 6. Kịch Bản & Hành Động Kịch (Screenplay & Dramatic Action)
- **Scene Sluglines**: Tiêu đề cảnh chuẩn (`INT.` / `EXT.` - `LOCATION` - `TIME OF DAY`).
- **Action Lines**: Dòng hành động hiện tại, chỉ tả những gì nhìn thấy và nghe thấy, không viết suy nghĩ trừu tượng vô hình.
- **Dialogue as Action**: Thoại là hành động công kích/phòng thủ, giàu subtext (lời nói dối, ẩn ý), tránh giải thích dông dài (*on-the-nose exposition*).
---

## Hướng Dẫn Chi Tiết Tạo Ảnh Storyboard 2×2 (Storyboard Generation Guide — Rule 69)

Trong quy trình làm phim `/fk-film`, việc tạo ảnh Storyboard 2×2 là **cột mốc bắt buộc** để định hình dòng thời gian thị giác (Visual Timeline) cho clip:

### 1. Nguyên Tắc Cốt Lõi
- **Bắt buộc cho mọi clip có sinh ảnh (Rule 69 (1))**: Mọi clip chuyển cảnh (Rule 65 Loại 2), đổi góc máy, clip mở đầu, clip hành động khó hoặc clip bị lỗi ≥ 2 lần BẮT BUỘC phải tạo ảnh Storyboard 2×2 (4 panel theo thời gian). CẤM sinh start frame 1 khung đơn lẻ.
- **BỎ cắt Panel 1 / Start Frame (User Lock 22/10/2026)**: Omni Flash R2V (`MZZa6b` - `GENERATE_VIDEO_REFS`) vận hành theo cơ chế **Pure References (Nguyên liệu tham chiếu)**. Tấm Storyboard 2×2 tự thân là bản thiết kế thời gian (Time Reference) cho cả clip. **TUYỆT ĐỐI BỎ bước cắt Panel 1 làm Start Frame**, không cần entity `<CLIP> P1`.

### 2. Quy Tắc Sống Còn Khi Submit Tạo Ảnh Storyboard (Rule 69 (8))
- **BẮT BUỘC TRUYỀN `source_media_id` TỪ ẢNH REF CÓ SẴN (CẤM SINH TEXT-TO-IMAGE TỪ CON SỐ 0)**:
  Khi submit request tạo ảnh Storyboard cho bất kỳ cảnh nào có nhân vật, request (`GENERATE_IMAGE` hoặc `REGENERATE_IMAGE`) **BẮT BUỘC phải truyền `source_media_id` = UUID của ảnh ref có sẵn** trong dự án (`<Character>`, `<Character> Body` hoặc bối cảnh):
  ```json
  {"type": "REGENERATE_IMAGE", "scene_id": sid, "source_media_id": character_media_id, "project_id": pid, "video_id": vid, "orientation": "HORIZONTAL"}
  ```
- **Tác dụng**: Google Flow đưa `source_media_id` vào `base_media_id` / `target_asset`, gán trực tiếp thẻ ảnh ref làm ảnh gốc (`BASE_IMAGE`), ép Imagen 3 phải bám chặt nhận diện ngũ quan, trang phục và tỷ lệ cơ thể gốc. CẤM TUYỆT ĐỐI gửi request tạo storyboard dạng text-to-image thuần túy không có `source_media_id` khiến AI tự vẽ nhân vật ngẫu nhiên làm biến dạng hoặc vẽ sai giới tính.

### 3. Phân Bổ 4 Panel Theo Thời Lượng (`duration`)
| `duration` | Mốc Panel | Phân đoạn Timeline |
|---|---|---|
| **4s** | 0s (Panel 1) · 1s (Panel 2) · 3s (Panel 3) · 4s (Panel 4) | `0-2s / 2-4s` |
| **6s** | 0s (Panel 1) · 2s (Panel 2) · 4s (Panel 3) · 6s (Panel 4) | `0-2s / 2-4s / 4-6s` |
| **8s** | 0s (Panel 1) · 3s (Panel 2) · 6s (Panel 3) · 8s (Panel 4) | `0-3s / 3-6s / 6-8s` |
| **10s** | 0s (Panel 1) · 3s (Panel 2) · 7s (Panel 3) · 10s (Panel 4) | `0-3s / 3-7s / 7-10s` |

### 4. Cấu Trúc Prompt Mẫu Ảnh Storyboard 2×2
Khung prompt mẫu bằng tiếng Anh chuẩn điện ảnh (thay thế phần `< >` và đính kèm chip ref `{{media:<uuid>|<file>}}` theo Rule 64):
```text
A film storyboard sheet, 16:9, made of FOUR photographic panels in a 2 by 2 grid, separated by thin straight black gutters; each panel is itself a 16:9 frame; no text, no numbers, no arrows, no captions anywhere. All four panels are cinematic feature-film stills of ONE continuous moment in <location chip + practical light>; <character A>, wearing <...>, face exactly the face in <face chip>; <character B> ...
TOP-LEFT PANEL, second 0: <shot scale, camera angle, lens>. <exact positioning of characters, hands, props>.
TOP-RIGHT PANEL, second <t2>: <camera, or "same camera">. <motion progression, physical interaction>.
BOTTOM-LEFT PANEL, second <t3>: <camera angle/movement>. <escalated action or reaction>.
BOTTOM-RIGHT PANEL, second <t4>: <camera>. <final concrete positions matching final frame>.
Cinematic feature-film look: 35mm film grain, deep focus (f/8), motivated practical lighting, not a 3D render, not CGI, zero watermark, zero logos.
```

### 5. Hậu Xử Lý Ảnh Storyboard
1. Tải ảnh gốc về: `${OUTDIR}/images/<clip>_storyboard.jpg`.
2. Chạy ngay script xóa watermark:
   ```bash
   python tools/remove_watermark_from_image.py "${OUTDIR}/images/<clip>_storyboard.jpg"
   rm "${OUTDIR}/images/<clip>_storyboard.jpg"
   ```
3. Upload ảnh sạch `${OUTDIR}/images/<clip>_storyboard_clean.jpg` lên Flowkit qua `POST /api/flow/upload-image` để nhận `media_id` UUID sạch.
4. Tạo entity `location`: `<CLIP> Storyboard` gán vào dự án.

### 6. BẮT BUỘC: Đọc Thể Ảnh Storyboard Thực Tế & Tinh Chỉnh Video Prompt (Rule 69 (7))
Sau khi có ảnh sạch, BẮT BUỘC mở file ảnh lên phân tích trực quan 4 panel thực tế:
- **Panel 1 (Top-Left, 0s)**: Kiểm tra cỡ cảnh thực tế (Close-up, Wide...), hướng mắt nhìn, bố cục ➔ ghi vào `camera.shot_size`: `OPENING SHOT (second 0): matching the top-left panel of {{media:<uuid>|<CLIP> Storyboard.jpg}}: ...`.
- **Panel 2, 3, 4**: Đọc chuyển động máy và hành động thực tế mà AI đã vẽ (máy tĩnh hay dolly/pan, có cú cắt thẳng hay không) ➔ điều chỉnh các mốc thời gian trong `timeline_action` và `camera.movement`.
- **Hard Cuts theo Storyboard (Rule 74 & Bài học 80)**: Nếu 4 panel thể hiện các góc máy, cỡ cảnh hoặc nhân vật khác nhau ➔ BẮT BUỘC ghi rõ cú cắt gắt (**crisp hard cuts**) tại đúng mốc giây trong `camera.description` và `timeline_action` (`At second 3.0, a crisp hard cut matching Panel 2... At second 7.0, a crisp hard cut matching Panel 3 & 4...`). CẤM dùng 1 cú tracking dolly liên tục khiến model không cắt cảnh.
- **Khóa cô lập nhân vật & Chống phân thân (Anti-Cloning Lock, Rule 74)**: Khi cú máy chỉ quay nhân vật B, BẮT BUỘC ghi `Strictly [Character B] alone in this shot; [Character A] is completely off-screen and never appears`. Bổ sung vào `negative_constraints`: `strictly NO duplicate characters, strictly NO multiple [Name], strictly [Other] alone in shot Y, no ghost figures, no cloning; crisp hard cuts at second X.0 and second Y.0, no camera blending, no crossfades` — triệt tiêu 100% lỗi xuất hiện 2 bản sao cùng lúc (như 2 Nora giây 9 SC-01).
- **Panel 4 (Bottom-Right, giây cuối)**: Khóa cứng tư thế và vị trí kết thúc của nhân vật/đạo cụ ở giây cuối khớp 100% với Panel 4.
- **CẤM TUYỆT ĐỐI**: Không gửi lệnh sinh video khi chưa đọc ảnh storyboard thực tế và chưa điều chỉnh video prompt cho ăn khớp!

---

## Bộ skill phối hợp

| Skill | Nhóm | Vai trò cụ thể trong sản xuất phim `/fk-film` |
| --- | --- | --- |
| `/sw-workflow` | Screenwriting | Điều phối quy trình tiền kỳ, quản lý trạng thái dự án, story bible xuyên suốt các giai đoạn |
| `/sw-premise-theme` | Screenwriting | Thiết lập tiền đề kịch bản, controlling idea (value + cause), xung đột chủ đề, logline thương mại |
| `/sw-genre-anatomy` | Screenwriting | Khảo sát hệ thống beat chuyên biệt của 12 thể loại Truby, phối trộn thể loại, triệt tiêu cliché |
| `/sw-story-structure` | Screenwriting | Kiến trúc 3 hồi / 4 phần Syd Field/Snyder, xác lập inciting incident, plot points, midpoint, all is lost, climax |
| `/sw-truby-anatomy` | Screenwriting | Bộ máy 22 bước phát triển hữu cơ, tứ giác đối kháng (four-corner opposition), chuỗi luận điểm đạo đức |
| `/sw-character-conflict` | Screenwriting | Thiết kế mâu thuẫn 3D nhân vật (want vs. need, misbelief), phối hợp dàn nhân vật đối kháng, cơ chế phòng vệ tâm lý |
| `/sw-scene-craft` | Screenwriting | Thủ pháp thiết kế cảnh: value turns (+/-), 5 bước phân tích cảnh McKee, text vs. subtext, chi tiết và đạo cụ đắt giá |
| `/sw-dialogue` | Screenwriting | Viết và gọt giũa lời thoại: thoại như hành động, tam giác đối thoại (trialogues), cắt bỏ thoại giải thích sáo rỗng |
| `/sw-format-adaptation` | Screenwriting | Định dạng kịch bản chuẩn spec, hợp đồng Fountain, viết action line trực quan, chuyển thể từ nguyên tác/sự kiện thật |
| `/sw-american-case-studies` | Screenwriting | Nghiên cứu tình huống cấu trúc kinh điển (Fargo, Thelma & Louise, Good Will Hunting, Hitchcock suspense) |
| `/sw-korean-french-screenwriting` | Screenwriting | Thủ pháp kịch tính căng thẳng hiện thực, nhân phẩm nhân vật, nhịp dựng cảm xúc phi tuyến tính |
| `/sw-series-engine-bible` | Screenwriting | Thiết kế động cơ series, ma trận quan hệ nhiều tập, cấu trúc pilot và master series bible (cho phim bộ) |
| `/sw-series-structure` | Screenwriting | Kiến trúc act ngầm streaming, đan xen tuyến truyện A/B/C/runner, kết thúc hồi mở (cliffhanger) (cho phim bộ) |
| `/fk-character-design` | Production / Art | Turnaround Sheet 16:9 cho nhân vật và sinh vật chủ chốt, khóa cứng 5 lớp DNA anchor (Rule 58) |
| `/fk-character-bible` | Production / Art | Ma trận trạng thái trang phục theo cảnh (`Wardrobe State Ladder`), series character manifest |
| `/fk-scriptwriter` | Directing | Nhịp cảnh điện ảnh, cảm xúc qua triệu chứng cơ thể, bộ công cụ hồi hộp (blind spot, sonic isolation) |
| `/fk-camera-guide` | Cinematography | Ngôn ngữ máy điện ảnh, cỡ cảnh, ống kính, quang học tài liệu thực tế, 5 tầng vật lý |
| `/fk-action-choreography` | Cinematography | Bảng vật lý hành động, chuyển động 3 pha, từ vựng an toàn chống méo giải phẫu, chuỗi 4s liên hoàn |
| `/fk-storyboard` | Cinematography | Storyboard lưới 2×2 theo thời gian (4 panels 16:9) làm neo trực quan, visual audit storyboard sheet (Rule 69) |
| `/fk-cinematic-transitions` | Editing | Mối nối cảnh quay điện ảnh: Match on action, J-cut, L-cut, in-camera transitions |
| `/fk-gen-narrator` | Audio | Đo đạc số từ thoại chuẩn xác theo thời lượng `duration` (Rule 49 bảng (0)) |
| `/fk-add-material` | Material | Khởi tạo Image Material chuyên biệt cho phim (realistic, documentary, anti-CGI) |
| `/fk-script-to-prompts` | Prompt Eng | Chuyển thể kịch bản sang Structured JSON Prompt, nhúng khối `dramatic_craft` (Rule 56) |
| `/fk-prompt-lock` | Prompt Eng | Khóa chuẩn kiến trúc prompt JSON, quy tắc tokens và checklist B kiểm soát rủi ro |
| `/fk-review-prompt` | QC Gate | Rà soát toàn bộ prompt video và storyboard trước khi sinh, lập bảng chủ thể theo giây (Rule 68) |
| `/fk-paper-edit` | Editing | Dựng kịch bản trên giấy: bấm giờ, kiểm tra lời hứa 30s và móc giữ chân 90s trước khi tốn credit |
| `/fk-review-video` | Review | Chấm điểm chất lượng clip 720p thô theo 6 tiêu chuẩn cốt lõi (Rule 32) |
| `tools/review_dialogue.py` | Review | Bắt buộc chạy Whisper phân tích âm thanh, độ khớp chữ và mốc thời gian thoại từng clip (Rule 67) |
| `/video-editing` | Post-Production | Skill tổng lực dựng hậu kỳ footage đã duyệt (Rule 66): trim, ghép, dead air, overlay, reframe Shorts; **tự động điều phối `/fk-capcut-edit` và MCP `capcut`** để lập Bảng dựng và ráp trực tiếp vào timeline draft CapCut |
| `/fk-capcut-edit` | Post-Production | Module chuyên sâu được gọi từ `/video-editing`: lập Bảng dựng CapCut theo giây, kịch bản trailer montage hook 30s/45s, điều phối các lệnh MCP `capcut` |
| `/fk-sound-design` | Audio | Mastering âm thanh điện ảnh chuẩn YouTube: ducking tự động, SFX layering, chuẩn −14 LUFS / −1 dBTP |
| `/fk-youtube-seo` + `/fk-thumbnail` | Packaging | Đóng gói siêu dữ liệu YouTube SEO chuẩn xác và thiết kế thumbnail giữ chân người xem |
| `/fk-youtube-analytics` | Analytics | Chẩn đoán video sau đăng 48h và 7 ngày (CTR, retention 30s, AVD) để tối ưu hóa dự án tiếp theo |
| `/fk-doctor` | Diagnostics | Chẩn đoán và xử lý mọi sự cố pipeline (Google Flow, worker, database, network) (Rule 31) |

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
| Hai nhân vật bị nhân đôi (2 Nora, clone) hoặc không cắt cảnh theo Storyboard | Bắt buộc chia mốc Hard Cut dứt khoát ('crisp hard cut at second X.0 matching Panel N'); chỉ định rõ nhân vật kia 'strictly off-screen and never seen'; cấm trong `negative_constraints` ('strictly NO duplicate characters, strictly NO multiple [Name], strictly [Other] alone in shot Y, no cloning, crisp hard cuts at second X.0') (Rule 74, Bài 80) |
| Thêm lỗi mới khi review | Ghi bài học mới vào `production-lessons.md` (số kế tiếp) **và** thêm 1 dòng checklist B ở `prompt-lock.md` |
