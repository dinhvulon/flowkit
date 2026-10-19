# Lưu trữ luật POV / time-travel vlog — KHÔNG áp cho phim

> **Đọc trước:** file này chỉ để tham khảo. Skill `/fk-time-travel-vlog` đã đổi thành `/fk-film` (2026-10-19, user: "skill time-vlog giờ là làm phim rồi nên bỏ những cái liên quan đến vlog đi nhé"). Mọi luật, bài học và dòng checklist dưới đây chỉ đúng cho **POV / selfie vlog** (vlogger tự cầm máy, nói với ống kính, giọng Laomedeia). **Agent làm phim không được tự áp dụng nội dung file này.** Chỉ đọc khi user yêu cầu rõ một dự án POV / time-travel vlog, hoặc khi cần tra lại bằng chứng của một bài học cũ.
>
> Nội dung được chuyển **nguyên văn**. Số bài học giữ như cũ; ở chỗ cũ trong `production-lessons.md` và `prompt-lock.md` chỉ còn một dòng `→ chuyển sang vlog-archive.md`. Đường dẫn tương đối trong phần nguyên văn (ví dụ `references/…`, `../fk-script-to-prompts/SKILL.md`) tính từ thư mục skill cũ `skills/fk-time-travel-vlog/` (nay là `skills/fk-film/`), không tính từ file này. Các lệnh "BẮT BUỘC" trong phần nguyên văn là lệnh của dự án vlog cũ, không phải lệnh cho phim.

Mục lục:
1. Bản `SKILL.md` cũ của `/fk-time-travel-vlog` (nguyên văn, đến 2026-10-19)
2. Bảng §1 "LUẬT HIỆN HÀNH" cũ của `production-lessons.md` (bản vlog, 2026-10-12)
3. Bài học chỉ áp cho vlog (chuyển từ `production-lessons.md`)
4. Khung A cũ và các dòng checklist B chỉ áp cho vlog (chuyển từ `prompt-lock.md`)
5. Phần chỉ áp cho vlog còn nằm trong các reference khác
6. Luật CLAUDE.md chỉ áp cho POV vlog

---

## 1. Bản `SKILL.md` cũ của `/fk-time-travel-vlog` (nguyên văn)

Frontmatter cũ:

```yaml
name: fk-time-travel-vlog
description: Use when making a time-travel / POV survival vlog — a modern vlogger filming herself inside a historical or prehistoric era ("I Time Traveled to Ancient China in 211 BC", "A Day in Ancient Rome", "xuyên không vlog", "vlog cổ đại", "POV về quá khứ", "Hace 300.000 Años: Así Era La Vida…", "thoại tiếng Tây Ban Nha / Mỹ Latinh", "español latino") — writing its script, dialogue, storyboard or video_prompts, building or fixing its FlowKit project, or when the user shares a YouTube video of this kind and says "làm giống vậy".
```

Thân file cũ:

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

| Chủ đề              | Luật                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Chi tiết                                               |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| Hư cấu              | Phim giải trí, không phải tài liệu: sự kiện, phong tục, mẹo sinh tồn đều bịa được. Vlogger **không dạy lịch sử** (không niên đại, "scientists say"). Chỉ giữ: trông đúng thời kỳ + không biếm họa dân tộc/tôn giáo. `/fk-research` tùy chọn                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `era-research.md`                                      |
| Sinh video          | **Chỉ R2V Ingredients** (`GENERATE_VIDEO_REFS`, `abra_r2v_<N>s`, `MZZa6b`). Không sinh start frame rồi i2v cho clip có vlogger                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `flowkit-pipeline.md`                                  |
| Bộ ref vlogger      | `<V>` (mặt+tóc) + `<V> Body` (body 3 góc **đã mặc outfit**, EDIT từ Body trần gốc theo công thức outfit lock). **Cảnh POV có bàn tay tương tác**: tay + cẳng tay lấy từ `<V> Body` (đính Body, không đính `<V> Hand` — Bài học 95, user 15/10/2026), độ dài tay áo đúng như Body. Không entity `<V> Outfit`. Tối đa 7 ref/clip (giới hạn Omni Flash; luật 3 ref đã bỏ, user 2026-10-14). Body & Hand phải được user duyệt trước khi sinh video | `character-bible.md` §5–6, `production-lessons.md` #95 |
| Khóa trang phục     | **Khóa trang phục thuần ref**: TUYỆT ĐỐI KHÔNG mô tả lại trang phục bằng lời trong prompt. Chỉ trỏ thẳng: `wears the exact historical outfit shown in the <V> Body reference sheet (NO shearling collar, NO extra fur, NO hood, NO outfit variations)`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `production-lessons.md` #63                            |
| Khóa hình thể       | **Chống teo tóp body**: Góc máy ngang ngực/bụng trên (Waist-Up Medium Shot) hơi hất nhẹ lên, nhân vật đứng thẳng; cụm đối kháng cực mạnh: `tall statuesque 178 cm, voluptuous hourglass, large heavy bust, tiny waist, wide hips, NOT flat-chested, NOT skinny`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `production-lessons.md` #63                            |
| Giọng               | Chỉ vlogger có `voice_description` (Laomedeia). 1 giọng/clip                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `character-bible.md` §3                                |
| Nhân vật phụ        | Được nói, bằng ngôn ngữ không hiểu được, ở sub-clip riêng, giọng tả bằng chữ; vlogger phản ứng với giọng điệu, **không dịch**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `character-bible.md` §4                                |
| Độ dài clip         | **Không cố định & Phân định Chuỗi 4s vs Chuyển cảnh** (user lock 2026-10-12). **Dễ lỗi liền mạch (KHÔNG chuyển cảnh)** (chuyển động nhanh, tương tác thú, ngã/rơi máy, sinh vật lớn đi ngang, VFX chớp sáng/mưa kính, vật vỡ/đứt) → **chuỗi 4s liên tiếp (`a → b → c`)**: Mỗi clip 1 hành động, **CẤM TUYỆT ĐỐI CHUYỂN CẢNH / ĐỔI GÓC MÁY trong chuỗi** (giữ nguyên 100% vị trí máy, cỡ cảnh, góc quay, câu `Setting`, ánh sáng, bộ ref (tối đa 7)), clip sau mở đúng tư thế clip trước kết thúc (Rule 44), hỏng chỉ sinh lại đúng mắt xích đó. **Cảnh phức tạp CÓ CHUYỂN CẢNH / ĐỔI GÓC**: **CẤM gom vào chuỗi `a/b/c`**, tách Scene ID riêng biệt (4s/6s) nối bằng kỹ thuật dựng phim. **Dễ, không chuyển cảnh** (selfie nói chuyện, fixed cam, lia chậm, phong cảnh) → **8s**; long take / master take / cảnh cuối im lặng → **10s**; lưng chừng → **6s**. Ghi cột `Dur` trong storyboard, PATCH `duration` từng scene | CLAUDE.md Rule 49 (0), `production-lessons.md` #71     |
| Thoại               | **Theo độ dài clip** (Rule 49 bảng (0)): **4s** 0 từ (hành động) hoặc 6–8 từ, `0-2s / 2-4s` · **6s** 12–15 từ, `0-2s / 2-4s / 4-6s` · **8s** 18–22 từ, `0-3s` 6–7 / `3-6s` 7–8 / `6-8s` 5–7 · **10s** 24–28 từ, `0-3s / 3-7s / 7-10s`. Thiếu → dead air; thừa → cụt âm. **Ngoại lệ Sonic Isolation**: Cảnh rình mồi, phục kích thì 0 từ trên hình (miệng khóa chặt, thoại dẫn chuyển thành voiceover hậu kỳ). Viết/sửa qua `/fk-gen-narrator`. Thoại tiếng Tây Ban Nha Mỹ Latinh: cùng dải số từ, thêm câu khóa accent, cấm từ Tây Ban Nha (vosotros, vale, coger…)                                                                                                                                                                                                                                                                                                                                              | `voice-bible.md` §2, CLAUDE.md Rule 49, `dialogue-es-latam.md` |
| Thiết bị & Material | **Cấm 100% từ khóa thiết bị**: Không viết `phone`, `smartphone`, `phone_vlog`, `camera` (đạo cụ), `selfie stick`, `device`, `screen`, `gimbal` — kể cả câu phủ định và trong project material. Ràng buộc quang học: `The camera lens and viewpoint are completely outside the visible frame and never seen; both hands are empty`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `prompt-lock.md` #16, #28, `production-lessons.md` #63 |
| Góc máy & Động học  | **Phối hợp Góc máy Vlog Chân thực (Bỏ selfie 1 tay vươn dài)**: Linh hoạt phối hợp 3 góc máy: (1) _Lúc cần có Nora (Self-Vlog / Tự quay)_: Cầm máy tự nhiên ngang ngực/cổ quay mặt mình, nhìn thẳng camera dẫn dắt; (2) _Lúc thao tác 2 tay & Cảnh rộng (In-Frame Host Experience)_: Máy đặt cố định trên đá/cây (Medium/Wide shot), Nora xuất hiện rõ trong khung hình dùng 2 tay trải nghiệm sinh tồn, vừa làm vừa nhìn camera giới thiệu; (3) _Cận cảnh chi tiết (POV Close-Up)_: Soi cận cảnh đồ vật/hiện tượng                                                                                                                                                                                                                                                                                                                                                                                               | `production-lessons.md` #62                            |
| Nội dung sinh tồn   | **Cấm 100% đánh đấm / vật lộn cận chiến với thú lớn** (tử huyệt làm vỡ hình AI). Tập trung 100% vào **Cơ chế sinh tồn kỳ thú & giao lưu văn hóa** (đẽo đá Mousterian, may đo chỉ gân hươu, đun nước đá nung, bột xúc tác MnO2, dấu bàn tay đất son đỏ) theo phong cách documentary trải nghiệm triệu view (như Medieval Sisters)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `production-lessons.md` #62                            |
| Bối cảnh thời kỳ    | **Khóa bối cảnh chuẩn xác (Strictly No Snow)**: Tôn trọng đúng khí hậu thời kỳ (MIS 3 Neanderthal Dordogne là rừng thông ôn đới, đất mùn rêu xanh, tuyệt đối không tự ý chèn tuyết/bão mùa đông)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `production-lessons.md` #62                            |
| Chuyển cảnh         | Cắt thẳng tại khung che. Selfie → swing/whip pan; POV → foreground wipe; cùng tư thế → match on action. Không crossfade, không title card                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | `transitions.md`                                       |
| Chữ trên hình       | Chỉ năm, mission card, countdown `HOUR X — Y HOURS REMAINING`, chèn hậu kỳ, không viết vào prompt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `story-engine.md` §9                                   |
| Cổng duyệt          | Hỏi trước **mỗi** bước sinh; dừng sau mỗi bước cho user duyệt; lỗi thì đề xuất, không tự sinh lại                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | CLAUDE.md Rule 29                                      |
| Nhịp request        | Server giãn mọi call Flow 45–60s; video: 1 cái một lúc, xong mới gửi tiếp; dừng khi `UNUSUAL_ACTIVITY` / `QUOTA`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `prompt-lock.md` #18                                   |
| Cấm khói thở & hơi nước | **Khóa Tuyệt Đối Chống Khói Thở (Zero Smoke / Zero Breath Vapor)**: Khí hậu ấm/cận nhiệt đới/tiền sử/Hell Creek: CẤM TUYỆT ĐỐI `hot condensed breath vapor`, `vapor mist`, `snorting steam`, `smoke plumes`. BẮT BUỘC: `strictly NO smoke, strictly NO breath vapor, strictly NO steam; clean dry nostrils breathing transparent clean air`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | CLAUDE.md Rule 62 (1), `prompt-lock.md` #37           |
| Da thú sống & Triệt tiêu CGI | **Chất Liệu Sinh Học Da Thú Sống (Pachyderm Living Biology vs Anti-Plastic Sheen)**: Khủng long/voi/quái thú: CẤM vảy bóng nhờn (specular sheen), tia nắng ảo (`sunlight streaming`, `volumetric god rays`), đèn studio. BẮT BUỘC: `rough non-reflective pachyderm hide (black rhino / African elephant skin)`, `flat natural overcast diffuse daylight`, `strictly NOT a 3D digital render, NOT a plastic toy model`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | CLAUDE.md Rule 57, 61, 62 (2), `prompt-lock.md` #33, #37 |
| Deep Focus f/8      | **Deep Focus f/8 Chống Xóa Phông Bokeh (Anti-Bokeh / Anti-Shallow DoF)**: Cảnh trung & selfie vlog: CẤM shallow depth of field, xóa phông mù mịt bokeh f/1.8 làm mất môi trường. BẮT BUỘC: `deep focus, deep depth of field (f/8 aperture), entire frame sharp from foreground to distant horizon, strictly NO shallow depth of field, strictly NO bokeh`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | CLAUDE.md Rule 62 (3), `prompt-lock.md` #37           |
| Khóa mặt Start Frame 1:1 | **Khóa Ngũ Quan DNA, Lệnh 1:1 & BẮT BUỘC Truyền `source_media_id` Cho Cảnh Có Người**: Ngăn face drift giữa các Start Frame 2D: (1) BẮT BUỘC truyền `source_media_id` = UUID ảnh ref nhân vật (`uploads/nora_main_clean.jpg`) vào request tạo Start Frame để Flow neo thẻ ảnh ref vào canvas (`BASE_IMAGE`), (2) Lệnh ép 1:1 `[Name]'s face is an exact 1:1 identical match to reference` + đặc tả ngũ quan DNA (mặt trái xoan mềm, cằm thon tròn, má bầu bĩnh, mũi nhỏ thẳng, bờ môi dày mọng hình trái tim, tóc vàng cột cao mái bay). Phủ định: `strictly NO square jaw, NO thin lips, NO freckles, NO face drift` | CLAUDE.md Rule 60, 62 (4), 63, `prompt-lock.md` #36, #37, #38 |
| Start Frame (Liên tục vs Chuyển cảnh) | **Quy tắc bất di bất dịch: Cảnh liên tục cắt Last Frame — cấm sinh ảnh mới; chỉ chuyển cảnh mới sinh ảnh**: (1) _Cảnh liên tục (Chain Action / Motion sequence / cùng góc nhìn tiếp nối)_: CẤM TUYỆT ĐỐI sinh Start Frame mới từ văn bản (`GENERATE_IMAGE`). BẮT BUỘC trích xuất Last Frame clip trước bằng `ffmpeg -sseof -0.08`, tẩy watermark, upload làm Start Frame sạch (`PREV_LAST_FRAME`), (2) _Chuyển cảnh (Đổi góc, đổi bối cảnh, cutaway, establishing)_: Mới sinh ảnh tĩnh Frame 0 bằng `GENERATE_IMAGE` (truyền `source_media_id`), tẩy watermark, duyệt qua Review Board | CLAUDE.md Rule 65, `production-lessons.md` #79 |

## Quy trình

Mỗi bước: đọc reference ghi kèm **trước khi** làm. Bước có ⛔ là cổng — dừng chờ user.

| #   | Bước                                                                                                                                                                                                                                                                                                                                                                                       | Đọc                                                                                                                                                                     | Ra                                        |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| 0   | **Đầu vào** — tối đa 1 lượt hỏi, còn lại dùng mặc định (bảng dưới) và ghi rõ giả định                                                                                                                                                                                                                                                                                                      | —                                                                                                                                                                       | 3–5 dòng giả định                         |
| 1   | **Ý tưởng thế giới** (tùy chọn): `/fk-research` hoặc tự bịa, chọn 10–15 beat                                                                                                                                                                                                                                                                                                               | `era-research.md`                                                                                                                                                       | bảng beat                                 |
| 1.5 | **Gói trước khi viết** (package first): 3 tiêu đề theo 3 Option High-Stakes của `/fk-youtube-seo` Step 3 + 3 ý tưởng thumbnail theo `fk-thumbnail-guide.md`, mỗi cặp kèm 1 câu lời hứa; tiêu đề và chữ trên thumbnail theo ngôn ngữ thoại (Rule 20) ⛔ user chọn 1 → ghi `- **Package:** <tiêu đề> · <thumbnail> · <lời hứa>` vào khối thông tin đầu `script.md`. Outline (bước 3) phải trả lời hứa trong 30s đầu | `skills/fk-youtube-seo.md` Step 3, `skills/fk-thumbnail-guide.md`, `post-and-publish.md` §2 | dòng `Package` |
| 2   | **Character & Creature Bible**: Bắt buộc dùng `/fk-character-design` khóa 5 tầng DNA anchors, `CHARACTER_LOCK` + Laomedeia + `VOICE_LOCK` + kế hoạch bộ ref đa góc (Rule 58) | `skills/fk-character-design/SKILL.md`, `character-bible.md`, `voice-bible.md` §0–1, `prompt-templates.md`, `cinematic-toolkit.md` §4 | khối lock trong `script.md`               |
| 3   | **Outline**: chuỗi nhân quả sinh tồn → cold open (cắt từ master 10s) → 5 Act mỗi Act 1 câu hỏi → payoff → cảnh cuối không thoại. **Bắt buộc dùng subagent**: `fk-action-choreography` (động lực học), `fk-camera-guide` (chọn góc máy theo hành động), `fk-cinematic-transitions` (chuyển hồi)                                                                                             | `story-engine.md` (**nguồn cấu trúc duy nhất**), `structure-7-acts.md` (kho ý tưởng cảnh/beat, không phải cấu trúc), `reference-analysis.md`, `cinematic-toolkit.md` §3 | outline + thời lượng                      |
| 4   | **Storyboard + bảng vật lý** từng clip, có cột `Dur` (4/6/8/10 theo độ khó; cảnh dễ lỗi tách thành chuỗi 4s `a/b/c`) (máy ở đâu, có gì ở giây 0, hướng + tốc độ vật di chuyển, ai rời khung bằng cách nào). **Bắt buộc dùng subagent**: `fk-camera-guide` (bảng vật lý & quang học), `fk-cinematic-transitions` (khớp điểm nối) ⛔ user duyệt bảng vật lý                                  | `shots-and-realism.md`, `transitions.md`                                                                                                                                | bảng storyboard + bảng vật lý             |
| 4.5 | **Dựng trên giấy** (`/fk-paper-edit`): bấm giờ, số từ Rule 49, lời hứa trong 30s đầu, đặt `RH · <lý do>` ở cột Beat sao cho 2 móc liền nhau cách ≤ 90s, đề xuất cắt trước khi viết prompt ⛔ user duyệt đề xuất cắt | `skills/fk-paper-edit.md` | `paper_edit.md` + `script.md` đã sửa |
| 5   | **Clip JSON + `video_prompt`** theo khung 9 khối, qua checklist B. **Bắt buộc phối hợp 5 subagent**: `fk-action-choreography` (3 pha hành động), `fk-add-material` (visual profile), `fk-cinematic-transitions` (chuyển cảnh), `fk-gen-narrator` (số từ + mốc theo `duration`, Rule 49), `fk-camera-guide` (5 tầng quang học). Long-form xuất từng Act, ⛔ hỏi user trước khi sang Act sau | `prompt-lock.md`, `production-lessons.md`, `prompt-templates.md`, `voice-bible.md` §2–6, `cinematic-toolkit.md` §1–2                                                    | `output/<slug>/script.md`                 |
| 5.5 | **Cổng QC — review & viết lại prompt** (bắt buộc, chạy trên 100% prompt trước khi lưu): soi từng prompt qua 4 bộ kiểm của repo `character-scene-design-skills-main`, **sửa trực tiếp câu chữ** rồi mới `python tools/lint_prompt.py`. Xem §QC dưới                                                                                                                                         | `character-bible.md` §7, §QC dưới                                                                                                                                       | prompt đã viết lại + sổ liên tục bối cảnh |
| 6   | **Dựng dự án FlowKit** (pre-flight, flush PENDING, project, video, scenes, PATCH `duration` + `narrator_text`)                                                                                                                                                                                                                                                                             | `flowkit-pipeline.md` §2–3; tập tiếp theo của series: `cinematic-toolkit.md` §5                                                                                         | project/video/scene ids                   |
| 7   | **Refs**: mặt, Body đã mặc outfit (công thức outfit lock), sinh vật chủ chốt/bối cảnh — BẮT BUỘC dùng /fk-character-design tạo Turnaround Sheet 16:9 (Rule 58), xóa logo, upload lại ⛔ hỏi trước khi sinh, ⛔ user duyệt ảnh                                                                                                                                                                                                                                              | `flowkit-pipeline.md` §4, `character-bible.md` §6                                                                                                                       | entity có UUID media_id                   |
| 7.5 | **Start Frame từng Scene** (`GENERATE_IMAGE` với `image_prompt` đặc tả chất liệu vi mô & anti-CGI) ➔ tải ảnh, xóa logo sạch (Rule 28) ➔ gán vào scene ➔ mở Image Review Board (`review_images.html`) ⛔ **CỔNG DUYỆT BẮT BUỘC (Rule 22, 25, 27)**: dừng chờ user duyệt Start Frame Frame 0 trước khi sinh video!                                                                     | `flowkit-pipeline.md` §4.5, `CLAUDE.md` Rule 22, 25, 27                                                                                                                  | start_image_media_id sạch                 |
| 8   | **Video R2V**: kết hợp Start Frame đã duyệt (Frame 0 anchor) + Ingredients tham chiếu (mặt, Body mặc outfit, bối cảnh), clip khó nhất trước, rồi clip mốc, rồi cả loạt ⛔ hỏi trước mỗi lượt                                                                                                                                                                                            | `flowkit-pipeline.md` §5                                                                                                                                                | clip 720p                                 |
| 9   | **Review 720p** (`/fk-review-video` + Review Board :8200) ⛔ user duyệt từng clip. Clip rớt → **quay lại cổng 5.5**: chẩn đoán lỗi theo bảng §QC, viết lại prompt, lint, rồi mới đề xuất regen → upscale 1080p → xóa logo → concat                                                                                                                                                         | `flowkit-pipeline.md` §6                                                                                                                                                | bản 1080p clean                           |
| 10  | **Hậu kỳ**: cắt tại khung che + J-cut, nhạc duck dưới thoại, card chữ, bíp, master −14 LUFS                                                                                                                                                                                                                                                                                                | `post-and-publish.md` §1, `cinematic-toolkit.md` §6–7                                                                                                                   | video final                               |
| 11  | **Đóng gói YouTube** (tinh chỉnh từ gói bước 1.5) + chiến lược kênh → sau đăng 48h và 7 ngày: `/fk-youtube-analytics`                                                                                                                                                                                                                                                                                                                                                     | `post-and-publish.md` §2–4, `skills/fk-youtube-analytics.md`                                                                                                                                              | tiêu đề, mô tả, thumbnail                 |

Long-form → ghi `output/<slug>/script.md` (cập nhật dần theo Act); Shorts → trả thẳng trong chat. Chỉ dựng dự án FlowKit (bước 6) sau khi user duyệt kịch bản.

### §QC — Cổng review & viết lại prompt (bước 5.5)

Kho phương pháp: `skills/character-scene-design-skills-main/` (repo tham chiếu — **đọc, không copy về**). Luật của skill này luôn thắng khi mâu thuẫn; repo chỉ cung cấp **cách soi và cách viết lại**.

Chạy **4 bộ kiểm theo đúng thứ tự** này, mỗi bộ là một lượt quét qua toàn bộ prompt của Act:

| #   | Bộ kiểm                           | Đọc                                                                                                                           | Soi cái gì                                                                                                                                                                            | Viết lại thế nào                                                                                                                                                                                                                                                                                                                                                          |
| --- | --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Q1  | **Proportion lock**               | `skills/character-design/SKILL.md` → _Production Asset Pipeline_ b1 + b4 (_W0 turnaround contract_)                           | Chạy **một lần trước khi sinh `<V> Body`**, không phải mỗi clip. 3 panel của sheet có giống "một người xoay" không: net height, head ratio, width-to-height, leg ratio, foot baseline | Chốt 5 con số đó **thành câu chữ** trong prompt ảnh Body. Mạnh hơn nhồi thêm tính từ vào `BODY LOCK`                                                                                                                                                                                                                                                                      |
| Q2  | **Permanent prop geometry**       | cùng file → b3                                                                                                                | Mọi đạo cụ cố định (gùi, túi, dao, bầu nước) trong prompt **ảnh ref**. Có bị tả chung chung → trôi thành vật generic giữa 40 clip không                                               | Tả bằng **hình học + bên đeo + cách gắn + chất liệu + mặt trước/sau**, và nêu rõ **nó KHÔNG phải cái gì** (`not a round ball, not a bottle, not a pouch`). Chỉ trong prompt ảnh — `video_prompt` vẫn chỉ trỏ ref (Rule 52 §2). Đạo cụ xuất hiện ở ≥2 clip (kể cả clip nhặt / chế tác trước khi đeo): **một câu tả chuẩn** dùng nguyên văn ở mọi clip + đính ref chứa nó (Bài học 94)                                                                                                                                             |
| Q3  | **Bone And Face Structure Layer** | cùng file                                                                                                                     | Bảng nhân vật phụ: có ≥2 người dễ bị trộn mặt không                                                                                                                                   | Mỗi nhân vật phụ đổi ít nhất **2 trong**: face envelope, cheek/jaw, eye geometry, hairline, skin texture, posture. Ghi vào cột dấu nhận diện                                                                                                                                                                                                                              |
| Q4  | **Scene continuity ledger**       | `.agents/skills/scene-design/SKILL.md` → đoạn _base location vs scene state_ + danh sách trường của _scene continuity ledger_ | Mỗi địa điểm xuất hiện ≥5 clip: trạng thái có chạy **một chiều** không; dấu vết (vết kéo, vật vỡ, bùn trên da) có bị "reset sạch" giữa các clip không                                 | Lập sổ 2 tầng ngay trong `script.md`: **base scene** (bản đồ cố định, mốc được bảo vệ, hướng trục máy) + **bậc trạng thái** S0→Sn ghi clip nào dùng bậc nào, kèm dấu vết, ánh sáng, vùng đứng của nhân vật, thứ được phép đổi. Trạng thái kế thừa của clip trước là **đầu vào bắt buộc** của khối 3 `Everything is already in place from the very first frame` ở clip sau |

Sau 4 bộ kiểm → chạy checklist B (`prompt-lock.md`) → `python tools/lint_prompt.py` → phải 0 lỗi Critical/High mới được lưu.

**Bỏ qua** trong repo đó: short-drama / casting dọc 9:16, `references/full-manual.md`, `SECTIONS/`, `scene-illustration-workflow/` (bộ sinh prompt tiếng Trung cho Jimeng — khác công cụ, khác `scene-design` ở `.agents/`), và mọi đường dẫn `/Users/baimengke/...` (không tồn tại trên máy này).

### Mặc định đầu vào (bước 0)

| Thông số                 | Mặc định                                                                                                                                                                                                                                                     |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Thời kỳ + địa điểm + năm | **bắt buộc, chính xác tới năm** (`Rome, 79 AD`, `Xianyang, Qin dynasty China, 211 BC`) — từ chung chung làm AI trộn thời kỳ                                                                                                                                  |
| Độ dài                   | Long-form ~10 phút ≈ 38–42 beat × ~15s; Shorts 45–60s ≈ 4–8 clip. Mỗi beat ghép từ clip 4/6/8/10s tùy độ khó (beat hành động ≈ 3–4 clip 4s; beat trò chuyện ≈ 2 clip 8s hoặc 8s + 6s). Tính runtime theo thời lượng dùng được: 4s→3.5s, 6s→5s, 8s→7s, 10s→9s |
| Ngôn ngữ thoại           | English; dân bản địa nói ngôn ngữ không hiểu được. User chọn **tiếng Tây Ban Nha Mỹ Latinh** (`es-419`, video mẫu kiểu "Hace N Años…") → đọc `references/dialogue-es-latam.md` (luật chung) + `references/dialogue-es-mx-ca.md` (Mexico/Trung Mỹ: giọng, kho từ, câu khóa giọng) trước khi viết thoại: prompt vẫn tiếng Anh, chỉ thoại trong ngoặc kép là tiếng Tây Ban Nha + câu khóa accent |
| Nhân vật                 | Vlogger nữ ngoại quốc ngoại hình nổi bật, mặc trang phục thời kỳ ngay từ clip đầu                                                                                                                                                                            |
| Tỉ lệ khung              | HORIZONTAL 16:9 (long-form) hoặc VERTICAL 9:16 (Shorts); mọi ảnh ref đều 16:9                                                                                                                                                                                |
| Material                 | `prehistoric_vlog` (hoặc `<era>_vlog`), `documentary_footage` hoặc `realistic`; **TUYỆT ĐỐI CẤM material chứa chữ phone (như `phone_vlog`)**                                                                                                                 |

Chỉ học format; không sao chép tên, ngoại hình hay lời thoại nhân vật của kênh gốc user đưa làm ví dụ.

## Kiến Trúc Tiền Kỳ 3 Tầng: Từ Ý Tưởng ➔ story-bible.md ➔ script.md ➔ prompts.json

Mọi dự án kịch bản FlowKit bắt buộc trải qua đúng 3 tầng tài liệu với sự phân công skill minh bạch:

```
[Ý Tưởng / Concept]
       │
       ▼
[TẦNG 1: story-bible.md] ◄── Tạo bởi /sw-workflow điều phối:
       │                      • /sw-premise-theme: Premise, Theme, Misbelief ("I'm just here to watch")
       │                      • /sw-story-structure: Khung 起承转合 (Khởi 19% - Thừa 51% - Chuyển 19% - Hợp 11%), 12 mốc giờ
       │                      • /sw-character-conflict: Nora Want vs Need, Đàn Triceratops là "bộ tộc"
       ▼
[TẦNG 2: script.md + outfit.json + ref_prompts.json] ◄── Phối hợp các Subagents điện ảnh & material:
       │                      • §1–§8: Triết lý, Character Bible, Material (/fk-add-material), Khung thời lượng
       │                      • output/<slug>/outfit.json: Prompt may đo trang phục thời kỳ lên Nora Body
       │                      • output/<slug>/ref_prompts.json: Toàn bộ prompt ảnh Ref bối cảnh, sinh vật, đạo cụ
       │                      • §9 Storyboard: Toàn bộ clip (Shot, Ref, Visual, Thoại Nora chuẩn Rule 49, Việc)
       │                      • §10 Bảng vật lý (/fk-action-choreography): Vị trí máy, Frame 0, Vector chuyển động, Chuỗi 4s
       ▼
[TẦNG 2.5: paper_edit.md] ◄── /fk-paper-edit (python tools/paper_edit.py):
       │                      • Bấm giờ, số từ Rule 49, lời hứa của gói trong 30s đầu
       │                      • Bản đồ móc giữ chân RH (≤ 90s), đề xuất cắt ⛔ user duyệt
       ▼
[TẦNG 3: prompts_actX.json + vn.json] ◄── Tạo bởi /fk-script-to-prompts (Rule 56):
                              • Chuyển thể 100% kịch bản sang Structured JSON Prompt phân cấp
                              • Tự động chạy tools/lint_prompt.py kiểm toán và self-repair đạt 0 lỗi
                              • Xuất file hoàn chỉnh cho User review trước khi gửi batch sinh video!
```

## Định dạng output (theo đúng thứ tự)

1. **Giả định** (3–5 dòng).
2. **Character Bible & Outfit JSON** — `CHARACTER_LOCK` + `voice_description` + xuất file `output/<slug>/outfit.json` (prompt mặc đồ thời kỳ lên `<V> Body`).
3. **Bảng beat** (thật hoặc bịa) + Nghiên cứu chất liệu (`/fk-add-material`, `/fk-research`).
4. **Bảng chuỗi nhân quả sinh tồn** + **outline** cold open / 5 Act + thời lượng.
5. **Storyboard toàn bộ clip** + **bảng vật lý** ⛔ user duyệt (`script.md`).
5.2. **Báo cáo dựng trên giấy** — `output/<slug>/paper_edit.md` từ `/fk-paper-edit` (bấm giờ, lời hứa 30s, móc giữ chân, đề xuất cắt) ⛔ user duyệt đề xuất cắt.
5.5. **Bảng Prompt Ảnh Reference** — Xuất file `output/<slug>/ref_prompts.json` gồm tất cả prompt ảnh bối cảnh, sinh vật, đạo cụ chuẩn 16:9 ⛔ user duyệt trước khi sinh media.
6. **Clip JSON từng clip** — BẮT BUỘC dùng [`/fk-script-to-prompts`](../fk-script-to-prompts/SKILL.md) để chuyển thể từ kịch bản phân cảnh sang prompt JSON, tự động chạy linter `lint_prompt.py` self-repair, và xuất file `prompts_actX.json` + `vn.json` (long-form theo từng Act, user duyệt trước khi sang Act sau).
7. **Ghi chú hậu kỳ + gói YouTube.**

## ⚠️ KHÓA BẮT BUỘC 5 SUBAGENT VIẾT KỊCH BẢN & CÁC SKILL ĐIỆN ẢNH (RULE 50 — LOCK CỨNG PHẢI DÙNG)

Mọi dự án POV / Time-Travel Vlog (`/fk-time-travel-vlog`, `/fk-vlog-guide`, `/fk-vlog-japan`) **BẮT BUỘC** phải vận hành 5 skill dưới đây làm **SUBAGENT CHUYÊN TRÁCH** để lấy output chuẩn trước khi viết Kịch bản, Storyboard và Video Prompt (Bước 3, 4, 5). **AI AGENT TUYỆT ĐỐI KHÔNG ĐƯỢC PHÉP BỎ QUA HOẶC TỰ BỊA KỊCH BẢN MÀ KHÔNG DÙNG OUTPUT CỦA 5 SUBAGENT NÀY**:

### 1. Bộ 5 Subagent Bắt Buộc Để Lấy Output Viết Kịch Bản

| Subagent Chuyên Trách          | Vai Trò & Output Cung Cấp Cho Kịch Bản (Lock Cứng)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **`fk-action-choreography`**   | **Subagent Vũ Đạo Hành Động & Cơ Học Vật Lý**: <br>• _Nhiệm vụ_: Rà soát và loại bỏ 100% bẫy biến dạng (CẤM 360°, CẤM đâm xuyên thịt/máu me, CẤM cận chiến vật lộn giáp lá cà người vs thú lớn theo Lesson 62). <br>• _Quy tắc 3 pha_: Mọi pha hành động/sinh tồn đi theo 3 pha: Chuẩn bị/Hạ trọng tâm $\to$ Một vector hành động dứt khoát $\to$ Thu thế & chấn động tiêu tán. Hành động dễ lỗi: **mỗi pha = 1 clip 4s** nối liền cùng bối cảnh (Rule 49 (0)); hành động dễ: 3 pha trong 1 clip 8s (`0-3s / 3-6s / 6-8s`). <br>• _Output cung cấp_: Khối mô tả hành động 3 pha và tương tác cơ học vật lý an toàn đưa trực tiếp vào `video_prompt`.                                                                                                                                                                                                                                                         |
| **`fk-add-material`**          | **Subagent Chất Liệu Hình Ảnh & Visual Profile**: <br>• _Nhiệm vụ_: Xác định và cấu hình Image Material chuẩn cho project (`prehistoric_vlog`, `documentary_footage`, `realistic`). **Tuyệt đối CẤM** dùng material chứa token `phone` (`phone_vlog` - Lesson 63) khiến AI tự vẽ điện thoại 3D ngoài đời thực. <br>• _Output cung cấp_: Thiết lập `style_instruction`, `scene_prefix` và `lighting` chuẩn áp dụng đồng bộ cho toàn bộ entity và scene của video.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **`fk-cinematic-transitions`** | **Subagent Kỹ Thuật Nối Cảnh & Chuyển Màn**: <br>• _Nhiệm vụ_: Thiết kế logic chuyển cảnh chuẩn vlog chân thực: Match-on-action (khớp tư thế cuối clip trước theo Rule 44), Foreground wipe (vật lướt qua che ống kính cho POV), Swing/Whip-pan (lia máy nhòe chuyển động cho Selfie), J-cut âm thanh (tiếng clip sau vào sớm 0.5s). **CẤM TUYỆT ĐỐI** bumper, dip-to-black, crossfade làm mất tính vlog thật. <br>• _Output cung cấp_: Thiết kế liên kết chuỗi cảnh và `transition_prompt` đưa vào Storyboard và `clips.json`.                                                                                                                                                                                                                                                                                                                                                                              |
| **`fk-gen-narrator`**          | **Subagent Biên Kịch Thoại & Khẩu Hình Bản Địa**: <br>• _Nhiệm vụ_: Chuẩn hóa số từ tiếng Anh của Vlogger theo **Rule 49 bảng (0)**: 4s 0 hoặc 6–8 từ / 6s 12–15 / 8s 18–22 (chia `0-3s` 6–7 / `3-6s` 7–8 / `6-8s` 5–7) / 10s 24–28, bắt đầu nói ngay từ 0.0s (Lesson 65). Áp dụng **Sonic Isolation (Im lặng tuyệt đối 0 từ)** khi rình mồi / rình săn / tập trung cao độ. Dân bản địa không nói tiếng Anh, chỉ dùng cử chỉ hoặc âm gằn ngực tự nhiên. <br>• _Output cung cấp_: Cặp trường `narrator_text` và lời thoại nhúng trong `video_prompt` khớp từng giây.                                                                                                                                                                                                                                                                                                                                          |
| **`fk-camera-guide`**          | **Subagent Đạo Diễn Hình Ảnh & Quang Học Camera**: <br>• _Nhiệm vụ_: Thiết lập quang học Smartphone Vlog tự nhiên (0.5x ultra-wide, horizontal 16:9, vertical bounce nảy dọc theo bước chân, rotational lag khi xoay người, cấm góc nhìn gimbal/flycam bay lơ lửng). Kiến trúc prompt 5 tầng (Layer 1: Chủ thể $\to$ Layer 2: Lực tiếp xúc $\to$ Layer 3: Quán tính thứ cấp $\to$ Layer 4: Phản ứng môi trường $\to$ Layer 5: Động học camera). **Chọn góc máy theo hành động, KHÔNG theo tỷ lệ phần trăm** (Rule 42 (3), user lock 2026-10-12 — đã bỏ "Golden Camera Ratio"): hành động/di chuyển/rình săn ➔ POV; thao tác 2 tay ➔ Fixed/Ground Cam; tâm sự/hook/kết ➔ Selfie; đồng hành ➔ OTS. Ràng buộc: cấm 100% selfie, cấm 3 clip selfie liên tiếp, cấm 2 clip liền nhau cùng cỡ cảnh + cùng góc máy. <br>• _Output cung cấp_: Cỡ cảnh, vị trí đặt máy, quang học camera và bảng vật lý cho từng cảnh. |

### 2. Các Skill Điện Ảnh Bổ Trợ & Đóng Gói

| Skill                                       | Vai Trò                                                                                                                                                                   |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`/fk-character-bible`**                   | **Khóa trang phục thời kỳ (`OUTFIT LOCK`)**: Quản lý trạng thái trang phục, dùng `<V> Body` đã mặc hoàn chỉnh. Cấm tuyệt đối đồ tập gym, áo ba lỗ hiện đại.               |
| **`/fk-sound-design`**                      | **Hậu kỳ âm thanh**: Ducking nhạc nền tự động dưới thoại/foley; master chuẩn YouTube -14 LUFS / -1 dBTP; chạy `scripts/sfx_layering.py` bổ sung tiếng bước chân, gió bão. |
| **`/fk-capcut-edit`**                       | **Dựng Intro Trailer Hook**: Dùng `scripts/trailer_cuts.py` dựng trailer 30s/45s trước khi ghép master.                                                                   |
| **`/fk-research`**                          | Tùy chọn, gom ý tưởng hình ảnh và bối cảnh lịch sử.                                                                                                                       |
| **`/fk-review-video` / `/fk-review-board`** | Duyệt video 720p thô trước khi upscale 1080p và xóa watermark.                                                                                                            |
| **`/fk-youtube-seo` / `/fk-thumbnail`**     | Đóng gói metadata và thumbnail YouTube chuẩn SEO.                                                                                                                         |
| **`/fk-paper-edit`** | Bước 4.5: dựng trên giấy — bấm giờ, lời hứa 30s, bản đồ móc giữ chân `RH`, đề xuất cắt trước khi tốn credit. |
| **`/fk-youtube-analytics`** | Sau đăng 48h / 7 ngày: chẩn đoán CTR, giữ chân 30s, AVD; đổi 1 biến (thumbnail hoặc tiêu đề); end screen, playlist, Shorts mồi. |
| **`/fk-doctor`**                            | Chẩn đoán và sửa lỗi toàn bộ pipeline.                                                                                                                                    |

Không dùng: `/fk-gen-chain-videos` (unsupported), `/fk-gen-text-overlays` và `/fk-concat-fit-narrator` với text overlay/crossfade. Mọi clip (kể cả có vlogger) BẮT BUỘC phải sinh ảnh Start Frame và qua cổng duyệt ảnh bước 7.5 (Rule 22, 25, 27) trước khi sinh video.

## Lỗi hay gặp

| Lỗi                                                                   | Sửa                                                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Thiết bị quay hiện ra trong hình                                      | Xóa mọi từ chỉ thiết bị, kể cả "no phone"; chỉ tả góc nhìn + tay trống (Bài học 9, 33)        |
| Vật tự hiện ra / biến mất giữa clip                                   | Khối "already in place from the very first frame" liệt kê mọi người/vật ở giây 0 (Bài học 48) |
| Người bản địa mấp máy miệng theo giọng vlogger                        | Khóa miệng hoặc cho họ sub-clip nói riêng; test 1 clip trước (Bài học 49)                     |
| Clip ra 10s thay vì độ dài đã chọn                                    | PATCH `duration` sau khi POST scene (Bài học 12)                                              |
| Clip hành động dài bị méo người / thú trôi / vật hiện-biến giữa chừng | Tách thành chuỗi 4s cùng bối cảnh, mỗi clip 1 hành động, khớp tư thế đầu-cuối (Bài học 71)    |
| Outfit trôi / lộ da Body trần                                         | Dùng `<V> Body` đã mặc outfit + ID-LOCK; không gửi Body trần (Bài học 60)                     |
| Thoại bị cắt hoặc có khoảng lặng chết                                 | Đếm lại số từ theo `duration` của clip và theo sub-clip (Rule 49 bảng (0))                    |
| Khủng long/thú thở ra khói trắng như đầu máy xe lửa                   | CẤM `breath vapor`, `vapor mist`, `snorting steam`. BẮT BUỘC dùng `clean dry nostrils breathing transparent clean air, strictly NO smoke, strictly NO steam` (Rule 62) |
| Khủng long nhìn bóng như nhựa 3D CGI, ánh sáng studio giả            | CẤM `sunlight streaming`, `god rays`, `shiny scales`. Dùng da thú sần sùi không phản quang `rough non-reflective pachyderm hide (black rhino / African elephant skin)`, ánh sáng tự nhiên `flat natural overcast diffuse daylight` (Rule 57, 62) |
| Phông nền mờ tịt (bokeh), nhân vật sắc nét                            | CẤM shallow DoF / bokeh f/1.8. BẮT BUỘC: `deep focus, deep depth of field (f/8 aperture), entire frame sharp from foreground to distant horizon, strictly NO bokeh` (Rule 62) |
| Mặt nhân vật khác nhau giữa các cảnh Start Frame                     | Phân tán attention do Turnaround sheet. BẮT BUỘC lệnh ép 1:1 `exact 1:1 identical match to reference` + khóa ngũ quan DNA chi tiết (môi dày mọng trái tim, má bầu, cằm thon, mũi thẳng, tóc cột cao) (Rule 60, 62) |
| Đạo cụ chính khác nhau giữa 2 clip chuyển cảnh (mai rùa A1-06 ≠ A1-07) | Một câu tả chuẩn cho đạo cụ, không tính từ trái ref, đính `<V> Body` khi đạo cụ nằm trên sheet; clip chuyển trạng thái tự ghi trạng thái (Bài học 94). Nếu clip sau nối tiếp trực tiếp (cùng địa điểm, khoảnh khắc, góc máy, cỡ cảnh) thì không phải chuyển cảnh: dùng `PREV_LAST_FRAME` (Rule 65 (2)) là hết lệch |
| Clip nối tiếp trực tiếp nhưng không có hậu tố `a/b/c` vẫn sinh Start Frame mới ➔ lệch trang phục/đạo cụ giữa 2 clip | Rule 65 (2), mở rộng 16/10/2026: áp cho MỌI clip nối tiếp, không chỉ chuỗi `a/b/c`. Phép thử 4 yếu tố (địa điểm, khoảnh khắc, góc máy, cỡ cảnh) giống hệt ➔ `PREV_LAST_FRAME`; đổi 1 yếu tố ➔ `GENERATE_IMAGE`. Ghi lý do vào `start_frame.note` (Bài 79) |
| Thêm lỗi mới khi review                                               | Ghi bài học mới vào `production-lessons.md` **và** thêm dòng checklist B ở `prompt-lock.md`   |

---

## 2. Bảng §1 "LUẬT HIỆN HÀNH" cũ của `production-lessons.md` (bản vlog, nguyên văn)

Bảng thay thế cho phim nằm ở `production-lessons.md` §1.

## §1. LUẬT HIỆN HÀNH — đọc mục này là đủ để viết prompt

> Bảng tra nhanh (cập nhật 2026-10-12). File dưới §2 là **kho lịch sử 71 bài học**; khi nghi ngờ, bảng này thắng. Mỗi khi chốt luật mới, sửa bảng này **trước**, rồi mới ghi bài học mới vào §2.

| Chủ đề | Luật hiện hành | Nguồn | Đã thay luật nào |
|---|---|---|---|
| **Độ dài clip** | **Không cố định.** Dễ lỗi → chuỗi 4s cùng bối cảnh (1 hành động/clip, khớp tư thế đầu-cuối). Dễ, không chuyển cảnh → 8s; long take / master / cảnh cuối → 10s; lưng chừng → 6s | Rule 49 (0) + Bài 71 | ~~mọi clip 8s~~ |
| **Số từ thoại theo độ dài** | **4s** 0 hoặc 6–8 (`0-2s / 2-4s`) · **6s** 12–15 (`0-2s / 2-4s / 4-6s`) · **8s** 18–22, chia `0-3s` 6–7 / `3-6s` 7–8 / `6-8s` 5–7 · **10s** 24–28 (`0-3s / 3-7s / 7-10s`). Thiếu → dead air; thừa → cụt âm. Nói **ngay từ giây 0.0** | CLAUDE.md Rule 49 + Bài 65, 71 | ~~23–25 từ~~ (Bài 62), ~~20–25 từ~~ |
| **Tỷ lệ góc máy** | **KHÔNG có tỷ lệ % nào.** Chọn theo hành động: POV (hành động/di chuyển/rình săn/quan sát) · OTS (đồng hành, thao tác qua vai) · FIXED (thao tác 2 tay) · SELFIE (hook, tâm sự, phản ứng, kết). Cấm 100% selfie · cấm 3 selfie liên tiếp · cấm 2 clip liền nhau trùng cỡ cảnh + góc máy | Rule 42 (3) | ~~60–70% POV~~ (Bài 61), ~~POV 35/OTS 35/FIXED 15/SELFIE 15~~ (Bài 66) |
| **Im lặng khi rình săn** | Cảnh áp sát thú/phục kích/ẩn nấp: **0 từ trên hình**, miệng khóa chặt (`Sonic Isolation`). Thoại dẫn → voiceover hậu kỳ | Rule 49 (4) + Bài 61 | — |
| **Bộ ref vlogger** | `<V>` (mặt+tóc) + `<V> Body` (3 góc, **đã mặc outfit**, EDIT 1 lần từ Body trần gốc). **Không** có entity `<V> Outfit`. Tối đa 3 ref/clip. Cảnh OTS cần thêm `<V> Back` (sau gáy) | Rule 46 + Bài 60, 66 | ~~entity Outfit riêng~~ |
| **Khóa trang phục** | **Thuần ref** — cấm mô tả lại quần áo bằng lời. Chỉ trỏ: `wears the exact historical outfit shown in the <V> Body reference sheet (NO shearling collar, NO extra fur, NO hood, NO outfit variations)` | Rule 52 (2) + Bài 63 | ~~tả outfit bằng chữ trong prompt~~ |
| **Khóa hình thể** | Waist-Up Medium Shot hơi hất lên, đứng thẳng + cụm `BODY LOCK` đối kháng. Cấm góc xa/toàn khi cúi gập người | Rule 52 (3) + Bài 63 | — |
| **Từ cấm (ghost device)** | Cấm 100% `phone`, `smartphone`, `phone_vlog`, `device`, `screen`, `selfie stick`, `gimbal`, `camera` (đạo cụ) — **kể cả trong câu phủ định và trong project material**. Thay bằng: `The camera lens and viewpoint are completely outside the visible frame and never seen; both hands are empty` | Rule 52 (1) + Bài 9, 33, 63 | — |
| **Bàn tay trong POV** | Nếu POV có thao tác tay (nhặt đồ, vốc nước, chạm dấu chân): BẮT BUỘC cấp ref `<V> Hand` (sheet 16:9 cẳng tay/bàn tay chuẩn giải phẫu nữ, xắn áo kaki khớp outfit) + gán `characters: ["<V> Hand"]`. Cấm để rỗng nhân vật khiến AI vẽ tay đàn ông lông lá. Nếu không có ref tay → chuyển sang **OTS hoặc FIXED** | Bài 66, 67, 72 | ~~cấm tuyệt đối tay trong POV~~ |
| **Vật ở giây 0** | Mọi người/sinh vật/đạo cụ phải nằm trong khối `Everything is already in place from the very first frame`, ghi vị trí + khoảng cách + số lượng + tay nào cầm | Bài 48, 69 | — |
| **Chất liệu / bột** | Phải có sẵn trên bề mặt từ Frame 0; quệt ngón tay trực tiếp vào đá. Cấm hứng bụi/bột rơi giữa không trung | Rule 53 + Bài 64 | — |
| **Đạo cụ** | Bảo toàn xuyên suốt clip; cấm buông/đặt xuống đất giữa chừng; cấm xoay người 180° khi vác đồ nặng. Đạo cụ đơn nhất, không nhân bản | Bài 68, 69 | — |
| **Cận chiến** | **Cấm 100%** đánh đấm/vật lộn cận chiến người vs thú lớn. Thay bằng cơ chế sinh tồn & giao lưu văn hóa | Rule 51 (1) + Bài 62 | — |
| **Miệng nhân vật phụ** | Không thoại → khóa miệng. Có thoại → sub-clip riêng, ngôn ngữ không hiểu được, giọng tả bằng chữ, vlogger im lặng khi họ nói | Bài 49 | ~~người bản địa câm hoàn toàn~~ |
| **Duration** | **PATCH `duration`** sau khi POST scene, nếu không clip tự thành 10s | Bài 12 | — |
| **Bối cảnh** | Ảnh ref bối cảnh 16:9 dùng chung cho mọi clip cùng địa điểm; duyệt start frame bối cảnh trước khi sinh R2V | Bài 69 | — |
| **Xác phân hủy sinh học** | Xác thú lớn lún bùn 30cm, thịt rữa đỏ thẫm + gân nhờn bám sườn ố vàng, vết cắn T. rex dập tủy, ruồi nhặng. CẤM xương thạch cao trắng khô như tượng sáp / mô hình bảo tàng | Rule 59 (1) + Bài 75 | ~~xương trắng khô trên sỏi~~ |
| **Đường mòn tiền sử (Anti-Tire)** | Lối mòn thú giẫm đạp hỗn loạn, hố chân tròn lún bùn, dương xỉ dập nát. CẤM 100% vệt lốp xe ô tô 4x4, thân gỗ xẻ, đường lâm nghiệp hiện đại | Rule 59 (2) + Bài 75 | ~~từ khóa trail gây lốp xe~~ |
| **Ánh sáng tự nhiên (Anti-God Rays)** | Ánh sáng ban mai tán xạ dịu, sương ẩm mép sông, mai rùa nửa chìm bùn sỏi. CẤM 100% tia nắng thần thoại volumetric god rays kiểu hoạt hình / diorama hồ cá | Rule 59 (3) + Bài 75 | ~~god rays diorama~~ |
| **Khóa khuôn mặt (Anti-Text Drift)** | Prompt BẮT BUỘC khóa 1:1 theo ảnh ref face (tóc vàng mật ong, mái thưa, da trắng mịn không tàn nhang). CẤM tả lệch màu tóc/kiểu tóc/da đè lên ref | Rule 59 (4) + Bài 75 | ~~prompt ghi đè tóc đỏ/tàn nhang~~ |
| **Khóa ngũ quan & Lệnh ép 1:1 (Ironclad Face Lock)** | Dùng đúng ảnh ref hiện có. BẮT BUỘC lệnh ép: exact 1:1 identical match to attached reference + đặc tả ngũ quan (mặt trái xoan mềm, môi mọng Cupid's bow, cằm thon, mũi thẳng). CẤM mặt vuông già, cấm môi mỏng | Rule 60 + Bài 76 | ~~tả chung chung gây mặt vuông/môi mỏng~~ |
| **Ánh sáng tự nhiên & Chống Glamour CGI** | 100% ánh sáng tự nhiên (overcast / dappled canopy), micro-shadows. CẤM 100% beauty glow, smooth creamy skin, studio lighting, cấm cánh tay selfie vươn dài (camera off-screen, both hands natural/empty). Khủng long vảy sần cặn bùn thật | Rule 61 + Bài 77 | ~~tả da mịn làm dính beauty filter / selfie vươn tay~~ |
| **Start Frame: Liên tục vs Chuyển cảnh** | **Cảnh liên tục cắt Last Frame (`ffmpeg -sseof -0.08`), CẤM sinh ảnh mới. Chỉ chuyển cảnh/cắt góc mới sinh Start Frame tĩnh** (truyền `source_media_id` cho cảnh có người, tẩy watermark, user duyệt) | Rule 65 + Bài 79 | ~~sinh ảnh start frame cho mọi cảnh~~ |

---

## 3. Bài học chỉ áp cho vlog (chuyển từ `production-lessons.md`, nguyên văn)

Số bài học giữ như cũ. File bài học có hai loạt số 71–79; "bản 2" là loạt thứ hai (sau Bài 101). Bài 42 chỉ chuyển mục 3, các mục 1, 2, 4, 5 vẫn ở `production-lessons.md`.

### Bài 9

9. **Điện thoại là máy quay, nhưng KHÔNG viết chữ `phone` trong prompt (bài 33):** chỉ tả góc nhìn (`The lens sits at the end of her outstretched arm…` / `The view is her own eyes`) và tay trống (`her free hand is empty`). Không viết `she holds the phone up`, `the phone is the camera` hay `no phone`; nhắc tới đồ vật, kể cả câu phủ định, đều làm model vẽ nó ra. Với POV, cho tay nhân vật bận việc khác (bám mép thuyền, cầm đồ vật).

### Bài 10

10. **Shot selfie không dùng vật lướt qua ống kính** (xà gỗ, ngựa…): ở góc selfie, vật phải chen vào khoảng khoảng 60 cm giữa gậy selfie và mặt nên trông như "bay" đến, và model hay xóa luôn nhân vật (user duyệt: không thực tế). Selfie chuyển cảnh bằng **swing/whip pan** (nhân vật xoay gậy lia máy nhanh sang cảnh mới, nhòe chuyển động nửa giây cuối; clip sau mở giữa cú lia rồi dừng lại trên nhân vật ở chỗ mới) hoặc **jump cut**. Foreground wipe chỉ dùng cho shot POV.

### Bài 22

22. **[ĐÃ THAY bởi bài học 60 / Rule 46 — trang phục mặc lên `<Vlogger> Body`, không tách entity Outfit]** **Trang phục khóa bằng panel toàn thân trong ảnh sheet nhân vật** (góp ý của user, 2026-10-01; thay bài học S31 Atlantis): ảnh ref vlogger là một sheet 16:9 có mặt rõ, góc 3/4 và toàn thân mặc trang phục (xem mục 2). Chỉ tách entity `<Vlogger> Outfit` riêng khi trang phục vẫn bị đổi giữa các clip.

### Bài 23

23. **Tuyệt đối CẤM từ khóa `selfie-stick` và mô tả cầm điện thoại (bài học S11, S17, S20 Atlantis):**
    - Từ khóa `selfie-stick` hay `smartphone selfie` làm AI vẽ thêm 1 chiếc gậy selfie trong tay, hoặc vẽ 1 chiếc điện thoại/màn hình điện thoại bay lơ lửng trước ống kính (hiện tượng quay màn hình điện thoại).
    - **Chuẩn thay thế:** Dùng `Handheld front-camera vlog footage, ultra-wide 0.5x lens, slight wide-angle barrel distortion`. Tả cánh tay: `Mia holds the camera at arm's length with her right arm extended toward the bottom-right corner of the frame.`
    - **Khóa câu khẳng định bắt buộc:** `The lens sits at the end of Mia's outstretched right arm, looking back at her; her right hand is beyond the frame edge and her other hand is empty, so the frame contains only Mia and the scene behind her.` (không nhắc tới thiết bị, xem bài 33)

### Bài 24

24. **100% First-Person POV không vẽ thiết bị hay thao tác sai vật lý (bài học S12, S16, S34 Atlantis):**
    - Khi quay POV (nhúng tay thử nước, bước qua cầu, nhìn xuống mặt nước): Người xem nhìn thẳng qua mắt vlogger. Vlogger đứng hoàn toàn sau camera, hai tay giữ máy ở tầm ngực.
    - Chỉ có **1 bàn tay không** (trống trơn, không cầm gì) vươn vào mép dưới khung hình để tương tác (chạm nước, nhặt đá, chỉ tay).
    - CẤM mô tả "cầm gậy rồi thả ra rồi cầm điện thoại" hoặc vẽ bàn tay cầm điện thoại khác; cấm để điện thoại nổi lơ lửng trên mặt nước. Khóa câu: `The view is Mia's own eyes; Mia's face and body never appear, and only her bare empty hand enters the lower frame.` (không nhắc tới thiết bị, xem bài 33)

### Bài 25

25. **Vật lý cầm máy khi chạy tháo chạy và nhảy — Running & Action Leap Physics (bài học S27, S30 Atlantis):**
    - **Khi chạy trốn (S27):** Vlogger vlogging cuộc tháo chạy của mình thì **PHẢI LUÔN NẮM CHẶT CAMERA QUAY MẶT MÌNH**. Cấm để AI cho nhân vật buông tay, vứt điện thoại hay chạy xa khỏi camera. Tả: `Mia clutches the camera firmly in her right hand at arm's length pointed continuously at her face; she NEVER drops, releases, or lets go of the camera. The camera shakes violently with her sprint.`
    - **Khi nhảy (S30):** Vlogger một tay nắm chặt máy nhảy xuống thuyền; camera trải qua một cú giật nảy giật dọc cực kỳ thực tế khi tiếp đất trên sàn thuyền gỗ. Cấm buông máy/gậy trước khi nhảy.

### Bài 33

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

### Bài 34

34. **[LEGACY & BÀI HỌC GỐC] BỘ REF CHO VLOGGER: Mặt + Body (bài học H1/H2 Ice Age 16,000 BC; từ 05/10/2026 cập nhật theo Rule 46 & Bài học 60):**
    - **Root-cause #1 (lỗi nặng nhất): `character_names` phải là TÊN entity, không phải UUID.** Server so khớp theo `name`/`slug` (`_char_matches` trong `agent/sdk/services/operations.py`). Nếu lưu UUID thì không khớp entity nào → server rơi vào nhánh dự phòng và chỉ gửi **1 ref duy nhất** (entity đầu tiên của project). Mọi lock outfit/body đều vô hiệu. Luôn PATCH `character_names: ["Nora", "Nora Body", ...]` (bài học 60) và đọc lại scene để kiểm tra.
    - **Root-cause #2: giới hạn ref r2v.** `_R2V_MAX_REFS` đã nâng từ 3 lên 7 (giới hạn Omni Flash). Thứ tự ưu tiên: `visual_asset` trước, rồi `character`; entity `location` KHÔNG được gửi làm ref (chỉ mô tả bằng prompt). Một scene có tối đa 7 ref visual_asset + character.
    - **Root-cause #3: không có entity body/outfit riêng** → model tự suy diễn quần áo theo bối cảnh (tuyết → áo parka nâu) và tự đổi dáng người.
    - **Bộ 2 entity chuẩn cho vlogger (Rule 46 & Bài học 60 — TUYỆT ĐỐI KHÔNG TẠO ENTITY OUTFIT RIÊNG):**
      | Entity | Nguồn ảnh | Chứa gì |
      |---|---|---|
      | `<Vlogger>` | Ảnh mặt user cung cấp (Ice Age: `uploads/nora_main.jpg`) — upload thẳng, KHÔNG gen lại | Chỉ khuôn mặt, tóc, khuyên tai |
      | `<Vlogger> Body` | **`EDIT_CHARACTER_IMAGE` từ ảnh body trần nguồn (`source_media_id` = media_id của Body trần chuẩn)** để "mặc trang phục" lên body: giữ nguyên 3 panel (chính diện, 3/4, sau lưng), tư thế, tỉ lệ giải phẫu (ngực đầy, eo thon, hông nở, chân dài), khung cắt vai/dưới cằm không lộ mặt, và nền studio. **Đây chính là Body đã mặc hoàn chỉnh trang phục, đóng vai trò là `<Vlogger> Body` duy nhất.** | Body đã mặc outfit: dáng người + trang phục |
    - **Vì sao body KHÔNG có mặt:** nếu ảnh body có mặt, model nhận 2 khuôn mặt khác nhau (ảnh mặt + ảnh body) và trộn lẫn → mặt trôi. Body sheet chỉ được mang thông tin dáng người và trang phục.
    - **Quy trình khi setup project (Rule 46 & Bài học 60):**
      1. Xóa logo ảnh mặt → upload → PATCH `media_id` của `<Vlogger>`.
      2. Lấy ảnh Body trần của user (ví dụ `uploads/nora_body_v3_clean.jpg`) làm nguồn (`source_media_id`), chạy `EDIT_CHARACTER_IMAGE` với prompt mô tả trang phục vừa vặn form-fitting để "mặc đồ" lên body. Tải về, kiểm tra không lộ mặt, giữ đúng dáng ngực/eo/hông/chân, xóa logo SynthID, upload lại lấy UUID sạch và gán trực tiếp làm `media_id` cho entity `<Vlogger> Body`.
      3. **Duyệt Body đã mặc đồ**: Xuất ảnh `<Vlogger> Body` sạch logo cho user duyệt trước khi gen video.
      4. Trong `clips.json` / scene: mọi clip có `<Vlogger>` chỉ gắn **2 ref nhân vật** `["<Vlogger>", "<Vlogger> Body", ...]`. **TUYỆT ĐỐI KHÔNG tạo entity Outfit riêng và KHÔNG gửi ảnh Body trần/gym vào video** (Rule 46 & 47).
      5. `common.identity` nêu rõ vai trò từng ảnh: *"her face and hair from the Nora face sheet, and her build and clothing from the Nora Body sheet."*
    - **LUẬT CỨNG cho shot POV (`pov`, `pov_hand`, `wide`): KHÔNG gắn `<Vlogger>`, `<Vlogger> Body` vào `refs`/`character_names`.** Bằng chứng: H2 hỏng 3 lần liên tiếp theo cùng một kiểu. Prompt nói Nora ở sau camera, nhưng ảnh ref chứa mặt Nora. Model ưu tiên ảnh hơn chữ nên vẽ Nora vào khung. Vì prompt POV không có khối identity/outfit, model tự chọn áo parka sẫm, rồi diễn giải "holding it firmly" thành cầm điện thoại thấy rõ màn hình. POV chỉ gắn ref của thứ cần thấy trong khung (động vật, đồ vật, người địa phương). Với `pov_hand`, tả tay áo bằng chữ trong lock (*"her bare empty hand… coming out of a cream suede sleeve with a thick white fox-fur cuff"*).
    - **Outfit lock trong `common.identity`:** Cập nhật `common.identity` trong `clips.json` để mô tả chi tiết màu sắc, chất liệu, phụ kiện của trang phục. Phải nêu rõ "NOT dark, NOT brown, NOT a parka" để ngăn model suy diễn.
    - **Outfit lock trong `video_prompt`:** Thêm `OUTFIT LOCK (CRITICAL)` vào mỗi `video_prompt` của cảnh có vlogger, nêu rõ màu chủ đạo (ví dụ: "WHITE/CREAM reindeer suede dress, NOT dark/brown coat").
    - **Lưu ý mannequin:** KHÔNG gen outfit trên mannequin (phom người thon thẳng, không có tay chân thật → các góc mâu thuẫn, mất tay áo/legging; Neanderthal ep 2 v1/v2 hỏng). Trang phục luôn EDIT trực tiếp lên Body sheet của user (Rule 46 & Bài học 60).
    - **[LEGACY — chỉ project Ice Age cũ] Lệnh crop Nora Outfit ref** (project mới dùng bài học 60):
      ```bash
      ffmpeg -y -i "output/<slug>/refs/nora_clean.jpg" \
        -vf "crop=iw*2/3:ih:iw/3:0" \
        "output/<slug>/refs/nora_outfit_crop.jpg"
      # Kết quả: panel 3/4 + full-body từ nora_clean.jpg, không có face close-up
      # Upload rồi dùng làm media_id của entity "Nora Outfit"
      ```

    **[ICE AGE PROJECT — LEGACY, project mới theo bài học 60] Nora — bộ 3 ref đã khóa:**
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

### Bài 35

35. **CHẠY MÀ KHUNG HÌNH KHÔNG RUNG (bài học H1 Ice Age 16,000 BC bản v4 — người chạy hết sức nhưng mặt Nora và đường chân trời đứng yên như quay bằng gimbal):**
    - **Root-cause:** prompt chỉ ghi chung chung "the view bounces vertically with each footfall" một lần ở phần style. Model video mặc định ổn định hình (stabilize), nên một câu trừu tượng như vậy bị lờ đi. Chỉ chân và tay chuyển động, còn khung hình thì không.
    - **Fix: tả hiệu ứng rung NHÌN THẤY ĐƯỢC trên khung hình, có biên độ cụ thể, và nhắc lại trong TỪNG đoạn thời gian:**
      - Style `run` (bản đã sửa theo bài 36): *"Raw unstabilized footage: because the lens is in Nora's own outstretched right hand, every stride she takes jolts the whole frame — her face jumps up and down by about a tenth of the frame height and the horizon behind her tilts a few degrees left and right, with a brief motion blur on each footfall, while her face always stays in the frame."*
      - Mỗi segment `0-3s / 3-6s / 6-8s` của shot chạy phải có một cụm rung riêng, **gắn vào tay vlogger**, ví dụ *"her outstretched arm jolting the frame hard on every stride"*, *"the horizon swinging left and right with each footfall"*.
      - Không dùng các từ làm model ổn định hình: `smooth`, `steady`, `stable`, `cinematic tracking`.
    - **Mức rung theo hành động** (rung phải khớp nhịp chân): đi bộ → nảy nhẹ, chân trời nghiêng ≤2°. Chạy bộ → mặt nhảy ~5% chiều cao khung. Chạy thục mạng hoặc vấp → mặt nhảy ~10%, chân trời nghiêng 3–5°, nhòe chuyển động mỗi bước. Trượt, ngã → khung xoay mạnh. Với shot selfie, mặt vlogger luôn nằm trong khung; không tả "khung trôi khỏi mặt rồi giật về" (xem bài 36).
    - **Review:** khi xem contact sheet, so vị trí mặt và đường chân trời giữa các khung liền nhau. Nếu gần như không đổi trong lúc nhân vật đang chạy thì trừ điểm Motion Quality và sửa prompt theo mẫu trên.

### Bài 36

36. **TẢ RUNG NHƯ MỘT CAMERA ĐỘC LẬP LÀM MẤT GÓC SELFIE (bài học H1 Ice Age v5 — v4 giữ selfie đủ 8 giây, v5 thành người ngoài chạy giật lùi quay theo, cả hai tay Nora đều đánh):**
    - **Root-cause:** thay đổi duy nhất giữa v4 và v5 là câu rung *"the framing drifts off her face and snaps back"* cùng cụm *"the framing lurching and snapping back"* trong từng segment. Câu này mô tả khung hình có chuyển động riêng, tách khỏi cơ thể Nora, nên model hiểu là có một người quay riêng và dựng thành tracking shot. (Mới có một mẫu so sánh, nhưng đây là thay đổi duy nhất.)
    - **Fix:** mọi mô tả rung trong shot selfie/run phải nêu **nguyên nhân là tay của chính vlogger**: *"because the lens is in Nora's own outstretched right hand, every stride she takes jolts the whole frame … while her face always stays in the frame"*. Segment dùng *"her outstretched arm jolting the frame"*, không dùng "the framing lurches / drifts / snaps back".
    - **Kiểm tra trước khi gen:** grep prompt shot `run`/`selfie`; không được có `framing (drifts|lurch|snaps)`.

### Bài 37

37. **SHOT POV TẢ HÀNH ĐỘNG CỦA NGƯỜI QUAY → MODEL VẼ NGƯỜI ĐÓ TỪ BÊN NGOÀI (bài học H2 Ice Age v5 — cuối clip thấy một người mặc đồ sẫm lăn xuống dốc ở góc người thứ ba):**
    - **Root-cause:** segment ghi *"the camera pitches down sharply as Nora slides over the lip"*. "Nora slides" là hành động cơ thể có chủ ngữ là người, nên model dựng hình người đó trượt. Prompt POV không gắn ref Nora, nên model tự bịa ra một người mặc đồ sẫm.
    - **Fix:** trong shot `pov`/`wide`, chủ ngữ chỉ được là **góc nhìn hoặc khung hình** ("the view tips forward and drops over the lip, sliding fast down the snowy slope, snow spraying across the frame"), không bao giờ là "Nora …". Riêng `pov_hand` được tả bàn tay ("Nora's bare hand lifts…") vì tay có trong khung.
    - **Không dùng phủ định để chặn người** ("no person is seen", "no face, no body"): phủ định vẫn gọi tên đối tượng (cùng cơ chế với bài 33). Viết câu khẳng định: *"only snow, sky and the slope fill the frame"*, *"only the world in front of her fills the frame"*.
    - Đã sửa cùng lỗi ở S30 (cũng "Nora slides over the lip") và S49 ("whips back down toward Nora" trong shot wide → "toward the firelit camp").
    - **Kiểm tra trước khi gen:** với clip `pov`/`wide`, grep segment; không được có `\bNora\b` ngoài "Nora says".

### Bài 38

38. **SHOT POV BỊ NGƯỜI LẠ CHIẾM KHUNG — "OVER THE SHOULDER" VÀ "FROM BEHIND THE CAMERA" (bài học H2 Ice Age v6 — 2.5 giây đầu quay qua vai một phụ nữ lạ tóc nâu tết, áo parka sẫm, không phải Nora):**
    - **Root-cause:** trường `shot` ghi *"first looking back over the shoulder"*. Với model video, "over the shoulder" là thuật ngữ góc máy chuẩn: quay qua vai một người đang đứng trong khung. Model dựng đúng nghĩa đen. Vì cảnh POV không gắn ref vlogger, model bịa ra một người lạ. Thêm nữa, lời thoại gắn dạng *"Nora says from behind the camera"* ngầm báo có một người quay đứng sau máy, càng kéo model vẽ người. Đoạn cuối *"sliding fast down the slope"* là hành động của cơ thể, nên vẫn ra một người lăn.
    - **Fix:**
      - Không dùng thuật ngữ góc máy có người trong đó (`over the shoulder`, `OTS`, `two-shot`, `behind her`) cho shot POV. Viết theo chuyển động của góc nhìn: *"the view swings round to face backward toward the mammoth, then swings forward to the riverbank edge"*.
      - Lời thoại POV/wide gắn dạng **`Nora's off-screen voice says, …:`**, không dùng "from behind the camera".
      - Rơi hoặc trượt trong POV thì tả mặt đất lao về phía ống kính: *"the view tips forward over the lip and the snowy slope rushes up toward the lens, snow spraying across the frame until it turns white"*. Không dùng "sliding", "tumbling", "falling" (động từ của cơ thể).
    - **Kiểm tra trước khi gen:** clip `pov`/`wide` không được có `over the shoulder|from behind the camera|\b(sliding|tumbling|falling)\b` trong `shot` và segment.
    - **Trạng thái:** fix đã áp vào `clips.json` nhưng chưa gen kiểm chứng (hết credit ngày 2026-10-02). Gen xong phải ghi kết quả vào đây.

### Bài 39

39. **NHẢY HOẶC TIẾP ĐẤT TRONG SHOT SELFIE DỄ BỊ BUÔNG MÁY → CHUYỂN GÓC THỨ BA (bài học H2 Ice Age 16,000 BC bản v7):**
    - **Root-cause:** Khi mô tả nhân vật nhảy hoặc trượt qua gờ dốc ("Nora reaches the edge and leaps, sliding feet-first..."), model video AI (Omni Flash / Veo) ưu tiên mô tả hành động cơ thể tiếp đất tự nhiên (người nhảy phải vung hai tay giữ thăng bằng), dẫn đến việc model "buông điện thoại", lùi camera ra ngoài thành góc người thứ 3 (third-person spectator wide shot) hoặc vẽ Nora chạy ra xa máy.
    - **Fix:**
      - **Khóa cứng cánh tay và máy quay (Permanent Arm & Camera Lock):** Trong shot selfie có động tác nhảy/rơi/trượt, bắt buộc tả rõ cánh tay vlogger luôn duỗi thẳng và nắm chặt máy hướng về mặt mình: *"Nora plunges downward over the icy lip, her right arm remaining permanently extended gripping the camera tightly aimed directly back at her screaming face; she NEVER drops, releases, or lets go of the camera, and the view NEVER switches to third-person or spectator angle."*
      - **Tả chuyển động khung hình và tuyết thay vì tả chuyển động toàn thân:** Khung hình rung giật dọc theo quán tính cú rơi (`view jerks violently downward with the sudden drop`), tuyết bắn mù mịt xung quanh bờ vực, nhưng khuôn mặt vlogger luôn neo chặt ở trung tâm khung hình selfie.
    - **Kiểm tra trước khi gen:** Trong shot selfie có hành động nhảy/rơi/trượt (`leap`, `slide`, `jump`, `fall`): Bắt buộc phải có mệnh đề khẳng định: `her [right/left] arm remains extended pointing the camera at her face, NEVER drops or lets go of the camera, view never switches to third-person`.
    - **Bằng chứng thực nghiệm:** H2 bản v8 (media `665ccebc-ec01-406a-88cd-55aaefc9643b`) giữ góc selfie 100% từ 0s đến 6s, Nora vừa trượt dốc tuyết vừa la hét trực tiếp vào ống kính, cánh tay vươn dài giữ chắc máy, hoàn toàn không chuyển góc thứ 3.

### Bài 40

40. **BODY DRIFT KHI DÙNG VÁY MANNEQUIN VÀ THỨ TỰ TRUYỀN REF TRONG R2V INGREDIENTS (bài học H1/H2 Ice Age 16,000 BC bản v7):**
    - **Root-cause:**
      1. Ảnh Outfit tạo trên manocanh (mannequin display) có phom người thon gọn, thẳng đuột tiêu chuẩn. Khi đưa vào R2V ingredients cùng với ảnh Body đồng hồ cát, model video AI có xu hướng bị phom dáng mảnh khảnh của manocanh làm lấn át (body drift), khiến nhân vật trong video bị phẳng ngực và mất đường cong eo-hông dù prompt có ghi "hourglass build".
      2. Thứ tự ref gửi lên server: Nếu entity Outfit được gửi trước entity Body, model sẽ dựng phom áo trước khi gán tỉ lệ cơ thể.
    - **Fix (từ 05/10/2026 thay bằng Rule 46 & bài học 60: outfit EDIT trực tiếp lên Body, <Vlogger> Body chính là Body đã mặc trang phục, video chỉ nhận `["<Vlogger>", "<Vlogger> Body"]` → không còn mannequin và không có entity Outfit riêng lẻ; các ý dưới chỉ là tài liệu tham khảo cho project cũ):**
      - **Bảo toàn thứ tự truyền Ref theo chuỗi nhận diện:** Server (`agent/sdk/services/operations.py`) bảo toàn thứ tự entities trong `character_names`: `[Face] -> [Body]` (ví dụ: `["Nora", "Nora Body"]`). Model cố định nhận diện khuôn mặt trước, sau đó áp vóc dáng và trang phục từ Body sheet.
      - **Manocanh không đầu (Headless Mannequin):** Ảnh trang phục manocanh BẮT BUỘC là manocanh không đầu trên nền studio trung tính, chụp 3 góc (chính diện, 3/4, sau lưng); tuyệt đối không có tóc giả hay mặt người giả để tránh xung đột nhận diện khuôn mặt.
      - **Khóa tương phản giải phẫu cơ thể (Negative Contrast Constraints) trong Prompt:** Trong `common.identity` và `video_prompt`, phải có cụm từ tương phản đối kháng mạnh mẽ ép model tuân thủ ảnh Body: *"BODY LOCK (CRITICAL): Nora has a voluptuous hourglass figure with a large full heavy natural bust, tiny narrow waist, and wide curvaceous hips matching Nora Body reference; she is NOT skinny, NOT slender, NOT petite, NOT flat-chested, and her deep neckline proudly showcases her cleavage."*
    - **Bằng chứng thực nghiệm:** H1 (media `81b3bf5f`) và H2 (media `665ccebc`) bản v8 thể hiện chuẩn xác vóc dáng đồng hồ cát nóng bỏng với vòng 1 đầy đặn và váy slip dress lụa trắng xẻ ngực sâu trùng khớp hoàn toàn với ảnh `thumbnail_v2_2k_clean.jpg` và `nora_body_v3_clean.jpg`.

### Bài 41

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

### Bài 42 — mục 3

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

### Bài 43

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

### Bài 44

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

### Bài 47

47. **OUTFIT DRIFT, SAI KIỂU TÓC & CÔNG THỨC KHÓA NHẬN DIỆN VỚI ẢNH MANNEQUIN TRONG R2V (Omni Flash / Veo 3 — Bài học Scene 00 H1 Ice Age 16,000 BC bản Test 1-4):**
    
    #### 1. Hiện tượng lỗi thực tế qua các vòng Test
    - **Test 1**: Mô tả sơ sài/thiếu chuẩn xác khiến vlogger biến thành mặc váy ngắn hiện đại (mini dress) lộ đùi trần giữa bão tuyết, kèm theo chiếc máy ảnh DSLR trên gimbal xuất hiện góc phải khung hình.
    - **Test 2**: Dù đã loại sạch từ khoá camera để hết máy ảnh ma, nhưng do **xoá trắng mô tả trang phục và tóc trong prompt** (chỉ để câu logic trơ trọi `"wearing the exact outfit from reference image"`), kết hợp việc gửi kèm ref `Nora Body` (ảnh mặc đồ gym: áo tank top sát nách và quần đùi đen lộ da thịt trần). Kết quả: Vlogger biến thành người tiền sử cởi trần mặc áo da thú thô màu nâu rách rưới, tóc nâu bù xù xoã tự do, mất sạch kiểu tóc đuôi ngựa vàng và mất đầm trắng may đo!
    - **Test 3**: Đổi sang dùng ảnh crop nhân vật `nora_outfit_crop_clean.jpg`. Đã khóa được màu trắng và tóc đuôi ngựa, nhưng thiếu mất cổ áo mũ trùm lông cáo tuyết dày bản lớn và đai răng xương đặc trưng của trang phục ma-nơ-canh `nora_outfit_clean.jpg`.
    - **Test 4 (Chuẩn xác 100%)**: Dùng đúng ảnh ma-nơ-canh 3 góc `nora_outfit_clean.jpg`, loại bỏ hoàn toàn `Nora Body`, và viết khối `IDENTITY & OUTFIT LOCK` neo chính xác từng chi tiết (mũ trùm lông cổ vai to bản, dây đan ngực chéo, thắt lưng nẹp răng xương, bo viền lông cổ tay, tóc đuôi ngựa vàng cột cao có mái bay). ➔ Kết quả: Đạt chuẩn 100% cả tóc lẫn outfit.

    #### 2. Root Cause (Nguyên nhân gốc rễ)
    1. **Nhiễm da thịt trần từ ảnh Body gym (`Body Latent Contamination`):**
       - Khi đưa entity `<Vlogger> Body` (vốn mặc đồ tập gym ngắn áo tank top + quần đùi lộ da tay chân) vào cùng danh sách `character_names` với `<Vlogger> Outfit` trong bối cảnh mùa đông/tiền sử, model R2V bị nhiễm latent tay chân trần từ ảnh body. Khi kết hợp với bối cảnh "Ice Age 16,000 BC", AI tự động biến thành áo da thú cộc tay cởi trần kiểu người tiền sử generic!
    2. **Cái bẫy "Xoá sạch mô tả outfit" (`The Empty Prompt Trap`):**
       - Diffusion model hoạt động bằng cơ chế liên kết chéo (Cross-Attention) giữa text embeddings và image latents. Nó KHÔNG hiểu câu lệnh trỏ logic thuần tuý: `"wearing the exact outfit from reference image"`.
       - Nếu trong prompt không có các từ neo thị giác (`honey-blonde hair tied in a high wavy ponytail with curtain bangs`, `cream-white reindeer suede dress`, `fluffy white fur hood and collar`, `criss-cross leather ties`), thì các từ khoá bối cảnh thời kỳ (`Ice Age 16,000 BC mammoth steppe`) sẽ chiếm 100% trọng số attention, ép nhân vật ra kiểu tóc bù xù xoã ngang vai và áo da thú cởi trần nguyên thủy.
    3. **Hiện tượng loãng trọng số Ma-nơ-canh (`Mannequin Attention Dilution`):**
       - Ảnh ma-nơ-canh không đầu trên nền trung tính rất tốt để AI học cấu trúc 3D của trang phục, NHƯNG nếu có quá nhiều ref (ví dụ 5 ref gồm cả Body, Location, Creature) hoặc thiếu text anchor, model sẽ bỏ qua ma-nơ-canh vì nó không phải là con người.
       - Khi tinh gọn ref còn đúng 3 ref cốt lõi `[<Vlogger>, <Vlogger> Outfit, Creature]` và có text anchor mạnh mẽ, model ánh xạ chính xác 100% bộ đầm từ ma-nơ-canh lên thân hình vlogger!

    #### 3. Quy tắc Vàng: Công thức Khóa Nhận diện Tóc & Outfit chuẩn 100%
    1. **Bộ Reference tối ưu (Tối đa 3 Ref cho cảnh Vlogger — [ĐÃ THAY bởi Bài học 88: tối đa 7 ref]):**
       - Khóa chuẩn: `[<Vlogger>, <Vlogger> Outfit, <Creature/Asset>]`.
       - **BẮT BUỘC LOẠI BỎ `<Vlogger> Body`** đối với mọi cảnh nhân vật mặc trang phục mùa đông/may đo dài tay kín đáo. Từ 05/10/2026 (bài học 60): **Body trần/gym** không bao giờ gửi vào video; trang phục nào cũng được mặc lên Body bằng EDIT và chính ảnh đã mặc đó là `<Vlogger> Body` gửi vào video.
       - **[ĐÃ THAY bởi bài học 60]** Entity `<Vlogger> Outfit` chỉ còn ở project Ice Age cũ. Project mới: ảnh 3 góc đã mặc outfit (EDIT từ Body, xóa watermark) gán thẳng làm `<Vlogger> Body`, không có entity Outfit.
    2. **Khối cấu trúc Prompt `IDENTITY & OUTFIT LOCK` bắt buộc (Đưa lên vị trí SỚM ngay sau `Shot:` trước `0-3s`):**
       ```text
       IDENTITY & OUTFIT LOCK (CRITICAL -- match reference images exactly):
       [Character] has [hair color] hair tied in a [exact hairstyle, e.g. high wavy ponytail with curtain bangs framing her face], [eye color] eyes, and fair skin with natural pink flush. Her high blonde ponytail bounces energetically with each running stride.
       [Character] wears the exact outfit from the [Character] Outfit reference ([outfit_ref_name]): a tailored cream-white reindeer suede dress with a large fluffy white arctic-fox fur hood and collar framing a plunging laced V-neckline, long sleeves with thick white fur cuffs, a wide tan belt sewn with vertical bone teeth at her waist, thick white fur trim at the mid-thigh hem, cream hide leggings, and knee-high boots with white fur cuff trim.
       This outfit is WHITE/CREAM throughout -- NOT dark, NOT brown, NOT a caveman fur pelt, NOT sleeveless, NOT bare legs, NOT loose unkempt hair, NOT modern clothing.
       ```
    3. **Gia cố chi tiết trong từng phân đoạn hành động (Action Sub-clips):**
       - Phân đoạn `0-3s`: Nhắc lại chuyển động tóc và tay áo (`her blonde high ponytail bouncing with her desperate survival momentum; her cream suede sleeves with thick white fur cuffs pump powerfully in rhythm; her wide tooth-studded belt and fur collar flutter in the freezing wind`).
       - Phân đoạn `3-6s`: Nhắc lại tà váy và bo lông (`her white fur-trimmed dress and fur cuffs flutter in the freezing wind`).
    4. **Duy trì không vết tích thiết bị quay (No Ghost Devices):**
       - Tuân thủ Bài học 40, 42: hoàn toàn không xuất hiện từ `phone`, `smartphone`, `screen`, `device`, `gimbal`, `selfie stick`. Dùng góc nhìn `Handheld front-facing running vlog POV footage, ultra-wide 0.5x view, natural wide-angle perspective`.
    5. **Bằng chứng thực nghiệm:**
       - Scene 00 H1 Ice Age 16,000 BC bản Test 4 (`bfb7ba56-a131-45ae-8612-d2c5fa4528c1`) thể hiện chuẩn xác 100% bộ đầm may đo da tuần lộc trắng kem với cổ áo mũ trùm lông cáo tuyết dày to bản, đan dây ngực chéo, đai răng xương, bo lông gấu áo, kiểu tóc đuôi ngựa vàng cột cao có mái bay, động tác chạy nổ tuyết chân thực, không có thiết bị ma.

### Bài 50

50. **HÀNH ĐỘNG HAI TAY KHI ĐANG CẦM MÁY & ĐƯỜNG ĐI CỦA GÓC NHÌN QUA CỬA (Two-Hand Action While Filming — Bài học Scene 09, 11 Ice Age 16,000 BC Part 2, user review 03/10/2026):**
    - **Hiện tượng:** Scene 11 Nora vén tấm da cửa bằng **cả hai tay** trong khi góc nhìn đã nằm sẵn bên trong lều nhìn ra — không thể vừa tự quay vừa có máy ở trong trước. Cuối clip `swings her outstretched arm` sinh ra bàn tay vung về phía ống kính. Scene 09 tấm da cửa tự vén lên cứng đờ "do gió" trong khi tóc và cỏ đứng yên.
    - **Root cause:** Prompt không phân vai hai tay (tay nào giữ góc quay, tay nào làm việc) và không mô tả góc nhìn đi qua cửa thế nào. Vật nặng (tấm da cửa) được giao cho "gió" thay vì cho một bàn tay.
    - **Quy tắc:**
      1. Mọi shot selfie ghi rõ: `"her right arm stays extended toward the lens for the entire clip ... Only her left hand is free."` Mọi thao tác (vén cửa, cầm cốc, kéo mũ) tả là `"using only her free left hand"`.
      2. Đi qua cửa trong selfie: cánh tay giữ máy dẫn trước → `"the viewpoint passes through the doorway first, facing back at Nora, and she follows it inside"`.
      3. Vật nặng chỉ chuyển động khi có lực: `"It is thick and weighted; it stays completely still unless a hand moves it."` Không dùng "sways in the wind / lifts slightly" cho tấm da cửa.
      4. Chuyển cảnh swing dùng **cả góc nhìn lia** (`"the whole view whips quickly to the left in a heavy motion blur; no hand comes into the frame"`), không dùng "swings her arm".

### Bài 61

61. **PHÂN BIỆT RẠCH RÒI SELFIE VLOGGER VS POV ĐI SĂN / HÀNH ĐỘNG CẬN CHIẾN (Bài học Neanderthal 51ka, Scene 20–36, user review 08/10/2026):** *(phần tỷ lệ % góc máy đã bị BỎ — xem Rule 42 (3), user lock 2026-10-12)*
    - **Hiện tượng & Root Cause:** 
      1. Hiểu nhầm luật "phone is the camera" và bài học 25/39/50 (cánh tay vươn dài giữ máy) thành việc ép 100% mọi cảnh vlogger phải giơ tay selfie quay mặt mình. Kết quả: vlogger vừa đi săn vừa giơ tay quay mặt mình nói chuyện, biểu cảm đơ cứng, không thể di chuyển tự nhiên, biến cuộc đi săn thành buổi livestream lố bịch, phản sinh tồn.
      2. Áp dụng máy móc Rule 49 (thoại 18–22 từ) vào lúc áp sát con thú lớn, khiến nhân vật lải nhải khi đang cách bò mộng 3 mét.
    - **Quy tắc:**
      1. **Chọn góc máy theo hành động, KHÔNG theo tỷ lệ phần trăm (Rule 42 (3)):**
         - **First-Person POV (Cam sau):** hành động rình rập, săn bắn, di chuyển, quan sát đồng đội và cảnh quan.
         - **Front-Camera Selfie & Over-the-Shoulder (Cam trước 0.5x):** lúc an toàn, mở đầu/kết thúc tập, tâm sự với khán giả, phản ứng sốc/hú vía sau khi vượt hiểm nguy; OTS cho cảnh đồng hành cùng người bản địa.
         - **Ground / Fixed Cam:** camera tựa đá/mặt đất khi cần 2 tay rảnh hoàn toàn (chế tác, nấu nướng, khiêng vác).
         - **CẤM TUYỆT ĐỐI 3 cảnh selfie liên tiếp; cấm 100% video là selfie; cấm 2 clip liền nhau cùng cỡ cảnh + cùng góc máy.**
      2. **Khóa Im Lặng Khi Rình Mồi / Cận Chiến (Sonic Isolation — Rule 49 & 50):** 
         - Khi áp sát mục tiêu, phục kích, hoặc giao chiến sinh tử: BẮT BUỘC dùng First-Person POV và áp dụng **Sonic Isolation** (`Strictly NO spoken dialogue. Her mouth stays firmly closed in dead silence`). 
         - Âm thanh là Foley cơ học: tiếng thở nén qua mũi, tiếng tim đập, tiếng cành cây gãy, tiếng dã thú thở phì phò. Lời dẫn/suy nghĩ nội tâm nếu có chỉ đưa vào voiceover/subtitles hậu kỳ, miệng nhân vật KHÔNG được mấp máy.
      3. **Cánh tay khóa máy chỉ áp dụng cho shot Selfie:** Các bài học 25, 39, 50 về cánh tay duỗi thẳng giữ máy chỉ kích hoạt khi shot đó ĐÃ ĐƯỢC CHỌN là góc Selfie. Khi là shot First-Person POV, hai tay vlogger tự do tham gia hành động (cầm giáo, bò trườn, bám đá).

### Bài 66

66. **CẤM TẢ BÀN TAY VLOGGER TRONG GÓC POV; CHUYỂN THAO TÁC TAY SANG OTS/FIXED & BẮT BUỘC ẢNH REF SAU GÁY VLOGGER (POV Hand Glitch, OTS Transition & Back/Nape Reference Lock — Bài học Neanderthal 51ka, User review 09/10/2026):**
    - **Hiện tượng & Root Cause:**
      1. **Lỗi tay lơ lửng & biến dạng trong POV (POV Hand Glitch):** Khi đặt góc POV (Point of View) mà prompt lại mô tả bàn tay của Vlogger thò vào khung hình (`Nora's hands reach in...`, `holding meat`, `pressing palm against stone`, `holding herbal root`), AI Diffusion (Veo 3 / Omni Flash R2V) chỉ nhận ảnh mặt trước (`<Vlogger>`) và ảnh body không đầu (`<Vlogger> Body`), hoàn toàn không có dữ liệu hình ảnh về bàn tay của Vlogger. Hậu quả: AI tự "bịa" ra bàn tay lơ lửng không gắn liền cơ thể, dẫn đến bàn tay bị biến dạng 6 ngón, sai màu da, hoặc biến thành bàn tay lông lá, thô ráp của đàn ông Neanderthal / thổ dân.
      2. **Lỗi tụt tóc & mất nhận diện khi quay sau lưng / qua vai (OTS Nape/Hair Drift):** Khi camera quay góc OTS (Over-The-Shoulder / nhìn qua vai từ sau tới), AI nhìn vào sau gáy và tóc của Vlogger. Do ảnh `<Vlogger> Body` bị crop ngang vai (không có đầu/tóc/gáy) và `<Vlogger>` chỉ chụp mặt trước, AI không có ảnh tham chiếu góc nhìn sau gáy. Hậu quả: AI tự ý vẽ kiểu tóc sau gáy, gây bung tóc xõa, mất đuôi ngựa cột cao đặc trưng, hoặc dáng gáy biến dạng.
      3. **Mất cân đối tỷ lệ góc máy Vlog (Vlog Camera Imbalance):** Tỷ lệ POV quá cao (50%) trong khi Selfie quá thấp (1.4% = 1 cảnh) làm mất hoàn toàn tính chất kết nối cảm xúc của Travel Vlog. Khán giả cần thấy biểu cảm khuôn mặt, sự hoảng loạn, kinh ngạc và nụ cười của Vlogger để giữ chân (Retention).
    - **Quy tắc giải pháp:**
      1. **POV Thuần túy (Pure POV Lock — CẤM 100% tả tay Vlogger):**
         - Trong các shot POV, **TUYỆT ĐỐI CẤM 100%** mô tả bàn tay, cánh tay hay ngón tay của Vlogger xuất hiện trong khung hình (`strictly NO hands of the vlogger enter the frame`).
         - Góc nhìn POV 100% hướng ra ngoài cảnh vật, đường đi, thiên nhiên, hoặc **đối phương thao tác** (Thủ Lĩnh cạo đá, Người Phụ Nữ bản địa đào rễ cây).
      2. **Chuyển toàn bộ cảnh thao tác tay của Vlogger sang OTS hoặc FIXED:**
         - Bất kỳ cảnh nào Vlogger cần thao tác tay (cầm đuốc, mài bột đất son, cầm thịt nướng, đặt tay lên vách in tranh, nhặt đồ vật): BẮT BUỘC chuyển từ POV sang **OTS (Over-The-Shoulder / Nhìn qua vai từ sau tới)** hoặc **FIXED (Kê máy tĩnh)**.
         - Khi nhìn từ sau vai hoặc kê máy tĩnh, cả cánh tay và bàn tay của Vlogger được neo vững chắc vào cơ thể và trang phục từ ảnh Body Reference, khử sạch hoàn toàn lỗi tay lơ lửng.
      3. **Bắt buộc tạo Ảnh Reference Sau Gáy / Sau Đầu của Vlogger (`<Vlogger> Back`):**
         - Mọi dự án có góc quay OTS / Follow Shot sau lưng BẮT BUỘC phải có ảnh reference chuyên biệt cho góc nhìn sau gáy (`<Vlogger> Back` hoặc Turnaround Sheet có góc sau đầu rõ nét).
         - Ảnh thể hiện rõ: Mái tóc đuôi ngựa cột cao đặc trưng (`high ponytail`), những lọn tóc mai buông nhẹ hai bên, bờ gáy thon gọn, cổ áo và bờ vai áo da nhìn từ sau lưng để gán vào Slot tham chiếu của các cảnh OTS.
      4. **~~Tái cân bằng Tỷ lệ Góc máy Vàng~~ — ĐÃ BỎ (user lock 2026-10-12):** Không còn hạn ngạch phần trăm nào cho POV / OTS / FIXED / SELFIE. Góc máy chọn theo **bản chất hành động** của từng clip (Rule 42 (3)): hành động/di chuyển/rình săn ➔ POV; đồng hành & thao tác qua vai ➔ OTS; chế tác 2 tay & nhịp nghỉ ➔ FIXED; hook mở đầu, chia sẻ cảm xúc, thì thầm hoảng loạn, kết nối người xem ➔ SELFIE. Chỉ giữ ràng buộc định tính: cấm 100% selfie, cấm 3 clip selfie liên tiếp, cấm 2 clip liền nhau cùng cỡ cảnh + cùng góc máy.

### Bài 67

67. **QUY TẮC ĐỒNG NHẤT ĐIỂM NHÌN POV VLOG — CẤM GÓC POV TỰ THÂN KHI QUAY NGƯỜI KHÁC; CHUYỂN TOÀN BỘ THAO TÁC CỦA ĐỐI PHƯƠNG SANG OTS HOẶC OBSERVER CLOSE-UP (Observer POV vs Self-POV Identity Conflict — Bài học Scene 28 & 32 Neanderthal 51ka, User review 09/10/2026):**
    - **Hiện tượng & Root Cause (Nghịch lý đồng nhất điểm nhìn):**
      1. Trong Travel Vlog, điểm nhìn camera là **đôi mắt của Vlogger (Nora)**.
      2. Khi đặt góc quay *"First-person POV nhìn xuống mặt đất/tấm da"* mà có 2 cánh tay thò từ dưới camera lên làm việc (như ghè đá, phết keo):
         - Tâm lý khán giả mặc định 100%: **Đó là 2 cánh tay của người đang cầm máy quay (Vlogger Nora)**!
         - Nhưng thực tế trong hình, 2 cánh tay đó lại là tay đàn ông vạm vỡ, lông lá, sạm khói bếp của thổ dân Neanderthal, trong khi giọng thuyết minh của Nora lại nói ở ngôi thứ ba: *"One sharp glancing blow from HIS hammerstone..." (Một nhát gõ từ hòn búa của ÔNG ẤY...)*.
         - **Hậu quả**: Khán giả bị rối loạn nhân dạng nghiêm trọng — không biết Vlogger là ai, tại sao người đàn ông lại có camera mọc trên ngực trong khi giọng nói là con gái bên ngoài.
    - **Quy tắc giải pháp:**
      1. **CẤM TUYỆT ĐỐI góc POV "nhìn xuống tay mình" khi chủ thể hành động là người khác:** Không bao giờ để camera đặt ở góc nhìn thứ nhất của nhân vật phụ nhìn xuống chính tay họ.
      2. **Chuyển toàn bộ cảnh đối phương thao tác sang OTS (Over-The-Shoulder qua bờ vai Vlogger):**
         - Đặt camera sau vai/gáy Vlogger (thấy vai áo và tóc đuôi ngựa của Vlogger ở góc khung hình), nhìn thẳng sang đối phương đang ngồi đối diện thao tác (Thủ Lĩnh ghè đá, thợ săn bôi keo).
         - Khán giả thấy rõ ràng: **Vlogger đang đứng cạnh quan sát và quay lại cảnh đối phương làm việc**.
      3. **Hoặc dùng Observer Close-Up (Góc quay cận cảnh người quan sát):**
         - Camera hướng từ đối diện/chếch bên hông nhìn vào cả khuôn mặt, thân trên và đôi tay đang thao tác của nhân vật phụ, không có bất kỳ cánh tay nào mọc ra từ mép dưới camera.

### Bài 87

87. **MÁY DỰNG CỐ ĐỊNH TRONG CẢNH RƯỢT ĐUỔI LÀ PHI LÝ VỚI VLOG CẦM TAY (user 11/10/2026):**
    - **Hiện tượng:** cảnh D quay rượt đuổi bằng máy đặt cố định trên tảng đá nhìn ngang. User: "khung cố định bỏ đi nhé, nó không hợp lý, chất liệu phone vlog mà" — giữa lúc bị bạo chúa đuổi không ai đặt được máy, khung tĩnh làm mất cảm giác người thật đang tự quay.
    - **Quy tắc:** cảnh hành động/nguy hiểm quay POV cầm tay; muốn thấy kẻ đuổi thì cho nó chạy chéo/song song ở cạnh khung POV, hoặc tách sang một clip selfie khi đã an toàn. Máy dựng chỉ khi vlogger tự đặt máy lúc yên ổn. Checklist B dòng 55 (sửa) và 60. Rule 51 (CLAUDE.md) hiểu theo luật này.

### Bài 72 (bản 2, khóa tay POV `<Vlogger> Hand`)

72. **KHÓA BÀN TAY POV BẰNG ẢNH REF `<VLOGGER> HAND` & CẤM ĐỂ RỖNG CHARACTER TRONG SHOT TƯƠNG TÁC (POV Hand Reference Lock, Dedicated Forearm Sheet & Anti-Male Hand Glitch — Bài học Scene 7 Hell Creek 66 Ma, User review 12/10/2026):**
    - **Hiện tượng & Root Cause:**
      1. **Tay biến hình / thành tay đàn ông / dị tật ngón trong cảnh POV:** Khi thực hiện cảnh quay góc nhìn thứ nhất (First-person POV nhìn xuống nhặt đồ vật, vốc nước, gạt cành dương xỉ, chạm vào dấu chân bùn, cầm mai rùa...), nếu prompt chỉ gán bối cảnh (`refs: ["Hell Creek Bank"]`, `characters: []`) mà không có nhân vật, hoặc chỉ gắn `<Vlogger>` (chỉ có khuôn mặt):
         - AI video diffusion model (Omni Flash / Veo) **hoàn toàn không có dữ liệu về bàn tay của nhân vật chính**.
         - Kết quả: AI tự tưởng tượng ra một bàn tay ngẫu nhiên — thường biến thành **bàn tay đàn ông thô ráp, đốt ngón tay đầy lông lá, sạm đen**, hoặc xuất hiện móng tay dài sơn móng lòe loẹt, móng vuốt kỳ quái, cổ tay áo hiện đại, đồng hồ thông minh, hoặc dị tật ngón (6 ngón, ngón tay tan chảy).
         - Nếu cố tình nhét `<Vlogger>` (ảnh mặt), AI lại cố gắng ép khuôn mặt lọt vào góc nhìn POV, gây vỡ bố cục máy quay.
    - **Quy tắc giải pháp:**
      1. **Bổ sung Entity `<Vlogger> Hand` vào Bộ Reference Chuẩn của Dự Án POV:**
         - Đối với bất kỳ dự án POV Vlog nào có phân cảnh nhân vật chính dùng tay tương tác với môi trường hoặc đạo cụ, BẮT BUỘC tạo thêm 1 entity reference: `<Vlogger> Hand` (hoặc `POV Hand Sheet`).
         - **Chuẩn Turnaround Sheet 16:9 của `<Vlogger> Hand`:**
           - Thể hiện cận cảnh 4 góc cẳng tay & bàn tay của nữ vlogger: mu bàn tay, lòng bàn tay, ngón tay duỗi và ngón tay cầm nắm đồ vật.
           - Đặc điểm giải phẫu: Cánh tay thon gọn, thanh mảnh nhưng săn chắc khỏe khoắn; làn da tự nhiên có vết rám nắng nhẹ dã ngoại; móng tay cắt ngắn sạch sẽ, **tuyệt đối không sơn móng**.
           - Trang phục tay áo: Ống tay áo sơ mi xám tro/kaki xắn ngang cẳng tay (khớp 100% với trang phục trên `<Vlogger> Body`), cổ tay để trần hoặc có vòng dây da thô mộc thời kỳ.
         - Tẩy sạch watermark logo & SynthID (Rule 28) rồi upload lên Flow lấy UUID Media ID sạch.
      2. **Khóa Nhân vật trong Scene POV Tương tác:**
         - Mọi scene POV có xuất hiện bàn tay (`reaches down`, `picks up`, `scoops`, `holds`, `parts foliage`), `character_names` và `refs` BẮT BUỘC phải đính kèm: `["<Vlogger> Hand", "<Bối Cảnh / Đạo Cụ>"]`.
         - Trong khối `characters` của Structured JSON:
           `{"name": "<Vlogger> Hand", "visual_lock": "Slender athletic female forearms and hands matching <Vlogger> Hand reference, rolled sleeves matching outfit, natural unpainted fingernails; NO male hands, NO hairy knuckles, NO modern jewelry/smartwatch."}`
         - Trong `negative_constraints`:
           `"NO male hands, NO hairy arms, NO modern wristwatch or bracelet, NO painted fingernails, NO extra or deformed fingers; strictly matching <Vlogger> Hand reference."`

### Bài 17

17. **[ĐÃ THAY bởi Rule 46 / bài học 60]** Vlogger mặc đồ hiện đại theo ảnh ref là chấp nhận được. Hiện tại: vlogger mặc trang phục thời kỳ ngay từ clip đầu qua `<Vlogger> Body` đã mặc outfit; đồ hiện đại chỉ khi user yêu cầu phong cách "lạc loài".

### Bài 18

18. User có thể yêu cầu **cảnh mở đầu FPV điện ảnh** (từ không gian lao xuống toàn cảnh thành phố, không có vlogger), là ngoại lệ của luật "mọi shot quay bằng điện thoại". Clip đó dùng ảnh ref toàn cảnh, giữ yên 2–3 giây cuối, và clip sau mở bằng vật lướt qua ống kính để che cú cắt.

---

## 4. Khung A cũ và các dòng checklist B chỉ áp cho vlog (chuyển từ `prompt-lock.md`, nguyên văn)

### Đầu file và khung A cũ của `prompt-lock.md` (bản vlog, nguyên văn)

# 🔒 PROMPT LOCK — khung `video_prompt` + checklist trước khi lưu

Đọc ở **Bước 5** của `SKILL.md`, chạy lại ở Bước 8 khi review. Thay mục 10b cũ.

> User yêu cầu: các bài học ở `production-lessons.md` (mục 11 cũ) phải được **khóa vào lúc viết prompt**, không chỉ nằm trong danh sách bài học. Mọi `video_prompt` (POST hoặc PATCH) phải dựng theo khung dưới đây và **qua đủ checklist** trước khi lưu. Clip nào không qua checklist thì sửa prompt trước, không gửi sinh.

**A. Thứ tự khối trong `video_prompt` (không đảo, không bỏ khối):**

1. **Style + góc máy** — chọn đúng 1 trong 3 loại **theo bản chất hành động của clip** (Rule 42 (3) — KHÔNG có tỷ lệ phần trăm cứng): hành động / di chuyển / rình săn / quan sát ➔ POV; thao tác cần 2 tay ➔ Máy dựng cố định; tâm sự / hook / kết / phản ứng cảm xúc ➔ Selfie & OTS. Ràng buộc: cấm 100% video là selfie dí sát mặt; cấm 3 clip selfie liên tiếp; cấm 2 clip liền nhau cùng cỡ cảnh + cùng góc máy:
   - *Selfie:* `"The lens sits at the end of <V>'s outstretched right arm, completely outside the visible frame and never seen; her right arm stays extended toward the lens for the entire clip, and she never reaches toward, touches, covers, taps, or points at the lens. Only her left hand is free."`
   - *POV:* `"The view is <V>'s own eyes; all recording gear is completely outside the visible frame, and her hands stay out of frame for the whole clip."` (chỉ viết "her hands enter the frame" khi sub-clip **thật sự** có thao tác tay — Bài học 50).
   - *Máy dựng cố định:* `"Static footage from a fixed viewpoint resting on <vật cụ thể>; the frame does not move; nobody touches the viewpoint. Both of <V>'s hands are free."` — dùng khi hành động cần **hai tay** (Bài học 50).
2. **`Setting:`** — địa điểm + năm + **mặt đất/thời tiết** (tuyết, băng) + **giờ & ánh sáng khớp clip trước và sau** + vật liệu thời kỳ. Nội thất luôn có câu khóa bếp: `"an open fire in a shallow sunken hearth ringed with stones in the earth floor; no fireplace, no chimney, no brick or built wall, no grate, no metal objects."` (Bài học 53, Scene 15/27/28/53).
3. **`Everything is already in place from the very first frame:`** — liệt kê **mọi người, sinh vật, đạo cụ** sẽ xuất hiện trong clip, vị trí và khoảng cách của từng thứ ở giây 0, kèm `"stays in that same spot; never appears suddenly, never vanishes"`. Ghi **số lượng** (`"exactly one spear / one cup"`) và **tay nào cầm**. (Bài học 48)
4. **`Shot:`** — bố cục khung (ai ở 1/3 nào, thấy tới đâu trên người).
5. **`[ID-LOCK]`** theo Rule 46 / Bài học 60 (mặt + tóc từ `<V>`, dáng + quần áo từ `<V> Body` đã mặc outfit, kèm `BODY LOCK` & `OUTFIT LOCK`; mẫu ở `character-bible.md` mục 5) + câu khóa mũ (Bài học 52 điểm 2b) + câu `"From the very first frame to the last, <V> is fully dressed in the complete outfit: ... No part of the outfit appears, disappears or changes."`
6. **Miệng nhân vật phụ** khi họ hiện mặt: không có thoại → khóa miệng `"<Local>'s lips stay closed for the entire clip; ... The only moving mouth in the frame is <V>'s."` (Bài học 49). Có thoại ngôn ngữ không hiểu được → ghi rõ sub-clip họ nói, giọng (`deep, gravelly male voice — guttural non-English sounds, no recognizable words`) và `<V> stays silent while he speaks` (`character-bible.md` mục 4).
7. **Sub-clip theo `duration`** (4s `0-2s / 2-4s`; 6s `0-2s / 2-4s / 4-6s`; 8s `0-3s / 3-6s / 6-8s`; 10s `0-3s / 3-7s / 7-10s`) — mỗi đoạn: hành động có **nguyên nhân vật lý** + nhắc lại 1 chi tiết outfit (cổ lông / cổ V đan dây / thắt lưng) + thoại.
8. **Câu kết:** `"Pure front-facing selfie view; the shot never switches to a third-person view. Only <V> speaks English; nobody speaks over anyone else. No subtitles or text appear in the frame. Real amateur footage, not a 3D render."` (Thoại tiếng Tây Ban Nha Mỹ Latinh → `Only <V> speaks, and only in Latin American Spanish` + câu khóa accent, `non-Spanish` cho nhân vật phụ — `dialogue-es-latam.md` §2.) + với POV/cảnh rộng: `"The image is clean footage only: no on-screen interface, no recording indicator, no battery icon, no zoom label, no names, no text or symbols."`
9. **`Audio:`** cuối cùng.

### Các dòng checklist B chỉ áp cho vlog (nguyên văn)

| # | Kiểm tra | Bài học |
|---|---|---|
| 1 | Chỉ 1 loại góc máy, **chọn theo hành động** (không theo tỷ lệ %); không phải clip selfie thứ 3 liên tiếp; không trùng cỡ cảnh + góc máy với clip liền trước; nếu là selfie thì cánh tay phải giữ máy suốt clip, mọi thao tác chỉ bằng **tay trái** | 41, 42, 50, 61 |
| 2 | Hành động cần **2 tay** (trượt, chống tay, kẹp tay vào nách, ôm vật nặng) → đã chuyển sang POV hoặc máy dựng cố định | 50, Scene 27/45 |
| 7 | Người bản địa hiện mặt + vlogger có thoại → selfie qua vai; người bản địa không thoại thì khóa miệng, có thoại thì ở sub-clip riêng, ngôn ngữ không hiểu được, giọng ghi rõ; cảnh săn bắn/áp sát thú thì BẮT BUỘC dùng Sonic Isolation (im lặng tuyệt đối, miệng ngậm chặt) | 49, character-bible §4, Scene 13/53, 61 |
| 16 | Không có từ `phone`, `smartphone`, `camera` (đạo cụ), `selfie stick`, `device`, `screen`, `gimbal`; không dùng dòng `Negative:`. Thoại tiếng Tây Ban Nha: cả `celular`, `teléfono`, `móvil`, `pantalla`, `dispositivo`, `palo de selfie`, `cámara` | 40, memory, `dialogue-es-latam.md` §8 |
| 17 | Không còn câu mẫu thừa bị lặp (`only her bare empty hand enters...`, `Wearing the exact outfit from reference image`) ở clip không dùng tay | 50, Scene 67 |
| 24 | **KHÓA SĂN BẮN & HÀNH ĐỘNG (Rule 50):** Đi săn, giao chiến, chạy trốn, dùng 2 tay BẮT BUỘC dùng First-Person POV qua mắt vlogger hoặc camera nấp sau vật cản; **CẤM TUYỆT ĐỐI vừa đi săn vừa giơ tay selfie quay mặt mình nói chuyện**. Cắt thoại trong lúc rình săn (Sonic isolation) | Rule 50, `cinematic-toolkit.md` §1 |
| 25 | **ĐỔI CỠ CẢNH LIÊN TỤC (Rule 50):** **CẤM TUYỆT ĐỐI 2 cảnh liền nhau cùng 1 góc máy/cỡ cảnh**. Phải xoay vòng: POV rộng → POV chi tiết tay → POV quay lén từ chỗ nấp → Selfie qua vai → Máy dựng cố định | Rule 50, `cinematic-toolkit.md` §2–3 |
| 27 | **CHỐNG TEO TÓP BODY DO GÓC QUAY (Bài học 63):** Không dùng góc xa/toàn khi nhân vật cúi gập người; bắt buộc góc ngang ngực/bụng trên (Waist-Up Medium Shot) hơi hất nhẹ lên, nhân vật đứng thẳng + cụm đối kháng cực mạnh tôn dáng đồng hồ cát (`tall statuesque 178 cm, voluptuous hourglass, large heavy bust, tiny waist, wide hips, NOT flat-chested, NOT skinny`) | Bài học 63, Scene 23 |
| 28 | **CẤM TỪ KHÓA PHONE_VLOG TRONG MATERIAL & PROMPT (Bài học 63):** Tuyệt đối không dùng `phone_vlog` trong project material hay prompt để tránh lỗi vật thể hóa điện thoại 3D trong bối cảnh cổ đại; dùng `prehistoric_vlog` hoặc `realistic` / `documentary_footage` | Bài học 63, Scene 24 |

### Schema JSON cũ của `skills/fk-script-to-prompts/SKILL.md` (bản vlog, nguyên văn)

```json
{
  "clip_id": "Mã clip duy nhất khớp script.md (ví dụ: A1-02, A1-12a)",
  "scene_name": "Tên cảnh mô tả hành động",
  "duration": 8,
  "aspect_ratio": "16:9",
  "refs": ["Nora", "Nora Body", "Hell Creek Bank"],
  "camera": {
    "viewpoint": "mô tả góc nhìn quang học (ngang ngực/bụng trên, hơi hất nhẹ lên)",
    "shot_size": "cỡ cảnh (extreme close-up | close-up | medium close-up | medium shot | wide shot | extreme wide shot)",
    "description": "khóa điểm mù quang học: 'The camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Both hands are empty unless handling specified prop.'"
  },
  "style": "phong cách tài liệu thực địa tự nhiên (raw 35mm wildlife forensic documentary realism), không CGI, không bộ lọc màu công nghiệp",
  "setting": "mô tả bối cảnh và mốc ánh sáng L1-L7 khớp script.md §3: flat natural overcast diffuse daylight, soft organic environmental shadows",
  "characters": [
    {
      "name": "Nora",
      "visual_lock": "khóa nhận diện khuôn mặt 1:1 và body reference: exact 1:1 match to reference, soft heart-shaped face, full plump pillowy lips with Cupid's bow, delicate chin, straight petite nose, honey-blonde ponytail with curtain bangs",
      "state": "trạng thái thể chất lúc mở màn (giây 0)"
    }
  ],
  "in_place": "mọi vật thể, bối cảnh, dã thú đã hiện diện đầy đủ từ khung hình 0 (Already In Place), clean dry nostrils breathing transparent clean air",
  "timeline_action": {
    "0-3s": "hành động 1 + tương tác vật lý + nhân vật bắt đầu nói ngay từ 0.0s",
    "3-6s": "hành động 2 + biến dạng vật liệu",
    "6-8s": "thu thế & neo đất + kết thúc hành động"
  },
  "speech": {
    "speaker": "Nora",
    "language": "(chỉ khi thoại không phải English) vd. es-419 Latin American Spanish, neutral Mexican accent — xem fk-film/references/dialogue-es-latam.md",
    "delivery": "chỉ dẫn ngữ điệu Laomedeia, subtext, trạng thái thở dốc/adrenaline",
    "dialogue": [
      {"t": "0-3s", "speaker": "Nora", "line": "câu thoại 1 khớp script.md"},
      {"t": "3-6s", "speaker": "Nora", "line": "câu thoại 2 khớp script.md"},
      {"t": "6-8s", "speaker": "Nora", "line": "câu thoại 3 khớp script.md"}
    ]
  },
  "dramatic_craft": {
    "beat": "nhịp kịch tính: mục tiêu hành động & phản ứng đối kháng",
    "value_turn": "chuyển biến giá trị (+/-)",
    "subtext": "tầng nghĩa ngầm / ý đồ tâm lý của nhân vật",
    "prop_and_detail": "chức năng đạo cụ kịch tính & chi tiết đắt giá (Lu Jun)"
  },
  "audio": "thiết kế âm thanh 3 lớp (thoại + foley + ambient/sonic isolation)",
  "physics": "vận tốc, gia tốc, trọng lực, tương tác tiếp xúc cơ học, phản lực đất, p=m*v quán tính dã thú",
  "negative_constraints": [
    "The camera lens itself and her right gripping hand are completely outside the visible frame and never seen.",
    "NO phone, NO smartphone, NO screen, NO device, NO selfie stick.",
    "NO modern technology, NO artificial gadgets.",
    "Word count strictly N words matching script.md exactly.",
    "BODY LOCK: matches Nora Body reference, voluptuous hourglass figure, NOT flat-chested, NOT slender.",
    "FACE LOCK: exact 1:1 match to attached face reference; soft heart-shaped face, full plump pillowy lips with Cupid's bow, delicate rounded chin, petite straight nose; strictly NO square jaw, NO thin lips, NO freckles, NO face drift.",
    "ANTI-SMOKE LOCK: strictly NO smoke, strictly NO breath vapor, strictly NO steam, strictly NO white plumes; clean dry nostrils breathing transparent clean air.",
    "ANTI-CGI LOCK: rough non-reflective pachyderm hide, strictly NOT a 3D digital render, NOT a plastic toy model, NOT a museum resin statue, strictly NO artificial god rays, strictly NO sunlight streaming, strictly NO studio rim light.",
    "DEEP FOCUS: deep depth of field (f/8 aperture), entire frame sharp from foreground to distant horizon, strictly NO shallow depth of field, strictly NO bokeh."
  ]
}
```

---

## 5. Phần chỉ áp cho vlog còn nằm trong các reference khác

Các file dưới đây vẫn ở chỗ cũ vì phần lớn nội dung dùng được cho phim. Mỗi file có khung *"Phim vs vlog"* ngay dưới tiêu đề, ghi rõ mục nào chỉ áp cho vlog:

| File | Phần chỉ áp cho vlog |
|---|---|
| `character-bible.md` | giọng Laomedeia trong mẫu `CHARACTER_LOCK`, §3, §4, đoạn "chống teo tóp body" cuối §5 |
| `cinematic-toolkit.md` | bảng "Cách chuyển một template gốc sang vlog", chế độ selfie khi tháo chạy, "vlogger là người cầm máy" |
| `story-engine.md` | vlogger nói với ống kính, countdown / mission card (§9), nhân vật phụ nói tiếng không hiểu được (§13) |
| `structure-7-acts.md`, `reference-analysis.md` | cả file (kho beat và phân tích video vlog mẫu) |
| `transitions.md` | foreground wipe "cho POV", swing "cho selfie", back-of-head, selfie → POV, hand-over-lens, selfie flip, phone glitch |
| `voice-bible.md` | Laomedeia mặc định (§0), persona vlogger (§1), khuôn beat sinh tồn (§4), mẫu §5 |
| `shots-and-realism.md` | tỉ lệ loại shot, "mọi thứ quay bằng máy của cô", material `phone_vlog` |
| `prompt-templates.md` | mẫu Clip JSON selfie / POV / máy dựng (trừ mẫu mắt xích chuỗi 4s) |
| `flowkit-pipeline.md` | swing / foreground wipe ở §1, `phone_vlog` + Laomedeia trong ví dụ §3 |
| `post-and-publish.md` | "footage của một máy", SFX lướt qua ống kính |
| `dialogue-es-latam.md`, `dialogue-es-mx-ca.md` | Laomedeia, persona và kho từ của vlogger |
| `skills/fk-vlog-guide.md` | cả file (hub vlog cũ, đã đánh dấu ngừng dùng) |

## 6. Luật CLAUDE.md chỉ áp cho POV vlog

Các luật này vẫn ở CLAUDE.md, có tiền tố *"(Chỉ áp cho POV vlog — phim dùng /fk-film)"*:

- **Rule 14** — ngoại lệ "hư cấu được phép, research tùy chọn" chỉ cho time-travel / POV vlog.
- **Rule 24** — giọng Laomedeia.
- **Rule 30** — bài học sản xuất vlog (giờ: `production-lessons.md` cho phim + file này cho vlog).
- **Rule 42** — đơn góc nhìn selfie / POV, chọn góc máy vlog. Ý "cấm 2 clip liền nhau cùng cỡ cảnh + cùng góc máy" ở (4) vẫn áp cho phim.
- **Rule 45 (1)** — cấm tay vươn chạm ống kính. Mục (2)–(3) (động tác mặc/đeo đạo cụ) áp cho phim.
- **Rule 49 (3)** — khóa liên kết skill viết thoại vlog. Bảng (0), số từ, Sonic Isolation áp cho phim.
- **Rule 50** — khóa 8 skill vào time-travel vlog. Phim dùng bảng skill trong `SKILL.md` của `/fk-film`.
- **Rule 51 (2)–(5)** — phối hợp góc máy vlog, thoại Laomedeia, bối cảnh Dordogne. Mục (1) (cấm giáp lá cà với thú lớn) áp cho phim.
- **Rule 52 (1)** — cấm từ `phone / smartphone / device / screen`, material `phone_vlog`. Mục (2) (khóa trang phục thuần ref) áp cho phim; mục (3) (cụm BODY LOCK vòng 1) đã bị memory 2026-10-14 "Body lock = normal figure" thay.
- **Rule 61 (3)** — cấm cánh tay selfie vươn dài. Mục (1), (2), (4) áp cho phim.
