# Cinematic Toolkit & 5 Subagents Cho Time-Travel Vlog

Đọc ở các bước ghi trong từng mục. File này điều phối **bộ 5 Subagent Bắt Buộc** dùng để lấy output viết Kịch bản và Prompt — `/fk-action-choreography`, `/fk-add-material`, `/fk-cinematic-transitions`, `/fk-gen-narrator`, `/fk-camera-guide` — cùng các kỹ thuật điện ảnh đã chỉnh theo luật vlog. Từ vựng chuyển động (Rule 57) và nhịp động học (Rule 58) nằm ngay trong file này ở §8–9, không cần skill riêng.

> **QUY TẮC BẮT BUỘC (LOCK CỨNG):** Khi xây dựng kịch bản và viết prompt, AI Agent **BẮT BUỘC** phải vận hành 5 subagent này để lấy output chuyên môn cấu thành kịch bản và prompt, tuyệt đối không tự bịa hoặc bỏ qua bất kỳ subagent nào!

### Bảng Ánh Xạ 5 Subagent Viết Kịch Bản & Prompt

| Subagent | Chuyên Môn | Output Cung Cấp Cho Kịch Bản & Prompt |
|---|---|---|
| **`/fk-action-choreography`** | Vũ đạo hành động & an toàn cơ học AI | 3 pha động học (`0-3s` / `3-6s` / `6-8s`), từ vựng né/săn an toàn |
| **`/fk-add-material`** | Image Material & Visual Style | Style instruction, lighting, cấm token phone |
| **`/fk-cinematic-transitions`** | Kỹ thuật nối cảnh & nhịp chuyển màn | Match-on-action, foreground wipe, swing pan, J-cut |
| **`/fk-gen-narrator`** | Biên kịch thoại & khẩu hình vlog | Thoại 23–25 từ / clip 10s chia 3 mốc, sonic isolation, nói từ giây 0 |
| **`/fk-camera-guide`** | Đạo diễn hình ảnh & quang học smartphone | 5 tầng prompt, tỷ lệ vàng POV/OTS/FIXED/SELFIE |

Cách chuyển một template gốc sang vlog:

| Template gốc có | Đổi thành |
|---|---|
| `Negative: ...` | Câu khẳng định trước dòng `Audio:` (`prompt-lock.md` khối 8) |
| "The camera tracks / dollies / orbits / pushes in" | Góc nhìn của vlogger: selfie, POV hoặc máy dựng (`prompt-lock.md` khối 1) + rung tay theo bước chân (Bài học 25, 35) |
| `narrator_text` lời dẫn | Thoại native của vlogger 23–25 từ / clip 10s trong `video_prompt` (Lesson 62, 65; user chốt 2026-10-09) |
| Nhân vật chính là chiến binh/tướng | Vlogger là người sống sót bị cuốn vào; người bản địa làm phần khó |
| Kiếm, khiên, kỵ binh | Vũ khí và mối nguy đúng thời kỳ: giáo, đá, đuốc, thú lớn, bão |

---

## 1. Hành động & cảnh săn — 3 pha (từ `/fk-action-choreography`) · Bước 5

Mỗi clip hành động 8s đúng 3 pha:
- `0-3s`: **Chuẩn bị** — hạ trọng tâm, siết tay cầm, khóa mắt vào mục tiêu (mọi người/thú/vật đã ở đúng chỗ từ giây 0, khối "already in place").
- `3-6s`: **Một đòn theo một hướng duy nhất** — đâm, ném, chạy, né (tả quỹ đạo và tác động lên môi trường, đất mùn tung, lá văng, không tả xuyên thịt).
- `6-8s`: **Thu thế & neo** — dừng trượt, giữ thế thủ, ngực phập phồng (bụi/tuyết lắng, rung nảy dần ổn định).

**Phân biệt 2 chế độ hành động cốt lõi:**

| Chế độ | Góc máy bắt buộc | Thoại / Âm thanh (Rule 49) | Ví dụ bối cảnh |
|---|---|---|---|
| **A. Rình mồi & Săn thú cận chiến** | **100% First-Person POV** qua mắt vlogger hoặc Camera nấp sau tảng đá/thân cây | **Sonic Isolation (Im lặng tuyệt đối):** Miệng ngậm chặt, 0 từ thoại trên hình (`Strictly NO spoken dialogue`). Kịch tính qua tiếng thở dồn, tim đập, foley lá gãy | Áp sát bò mộng, phục kích voi ma mút, rình bầy linh cẩu, leo trèo |
| **B. Tháo chạy & Thoát nạn sinh tử** | **Selfie góc rộng 0.5x** (cánh tay khóa cứng máy, không buông) | **18–22 từ thoại thở dốc / hét nghẹn:** `0-3s` (6-7 từ) $\to$ `3-6s` (7-8 từ) $\to$ `6-8s` (5-7 từ) | Động đất, tuyết lở, thú dữ bất ngờ quay đầu truy đuổi |

**Góc máy cho hành động** (vlogger là người cầm máy — tuân thủ Golden Camera Ratio ở Rule 42: 60-70% POV, 20-30% Selfie/OTS, 10% Fixed):
- Rình rập, bò trườn, đâm/ném giáo, hai tay làm việc: **100% First-Person POV hoặc máy dựng/tựa đá** (Bài học 50, 61) — vlogger không thể vừa giơ tay selfie vừa đi săn.
- Chạy trốn, né: selfie một tay, máy nảy theo từng bước, cánh tay không bao giờ buông máy (Bài học 25, 39).
- Người bản địa ra đòn chính: POV từ chỗ nấp (`/fk-camera-guide` mục 6 "quay lén") hoặc selfie qua vai (vlogger 1/3 tiền cảnh) ở những giây quan sát an toàn.

**Từ vựng an toàn chống méo người:**

| Hành động | ❌ Dễ méo / bị chặn | ✅ Viết thế này |
|---|---|---|
| Đâm giáo vào thú | `spear pierces the bison's chest, blood sprays` | `thrusts the spear forward in one straight line toward the bison's flank; dark loam and moss burst up where the beast stumbles` |
| Ném giáo | `throws three spears in two seconds` | `draws the spear back to her shoulder, then throws once; the spear streaks diagonally across the frame` |
| Thú lao tới | `the mammoth charges straight into the lens` | `the bison charges diagonally from the far left toward the right edge, dark loam churning under its hooves` |
| Né | `she backflips away` | `she drops low and sidesteps behind the boulder, the horn sweeping past above her` |
| Vật lộn với thú / người | `wrestles the wolf on the ground` | Giữ khoảng cách một sải tay; cho thấy hậu quả: đất tung, máy chúi, thở dốc |
| Đập đá, đánh lửa | `smashes rocks rapidly` | `strikes the flint once against the pyrite above the tinder; a single spark drops onto it` (`story-engine.md` mục 7d) |
| Quay người | `spins 360 degrees` | Tách 2 clip, cắt thẳng (Rule 42, 44) |

Thương tích, máu, cái chết: chỉ cho thấy **hậu quả** (vết cày trên đất, con thú nằm yên, nhóm thở dốc hồi sức), không cho thấy lúc xuyên/thương — vừa tránh `UNSAFE_GENERATION` vừa tránh model làm cong vũ khí.

**Mẫu 1: Khung clip săn rình mồi / cận chiến im lặng (Sonic Isolation — POV):**
```text
0-3s: Torak and Nora crouch low behind a mossy limestone boulder at the woodland edge, eyes locked on the bull bison twenty paces ahead. Nora holds her breath; strictly NO spoken dialogue, her mouth stays firmly closed in dead silence.
3-6s: Torak lunges forward in one explosive thrust, driving his heavy wooden spear with full body weight toward the bison's flank; dark loam and damp pine needles burst upward as the beast bellows gutturally and stumbles sideways.
6-8s: The bison crashes onto its front knees, churning the forest floor; Torak holds his low braced stance as the heavy animal collapses. Nora stays frozen behind the boulder, pulse racing; zero dialogue, only heavy nasal breathing and woodland wind.
```

**Mẫu 2: Khung clip tháo chạy có thoại (Voiced Evasion — Selfie 18–22 từ):**
```text
0-3s: Nora sprints past leaning pine trunks, her right arm permanently extended holding the camera locked on her face; behind her, timber cracks loudly. Nora gasps (voice cracking): "It turned around— it's right behind us!"
3-6s: Nora veers sharply right behind a granite outcrop as a massive dark shadow thunders past off-screen, showering dirt onto her shoulder. Nora pants (choked whisper): "Keep moving! Don't look back, just run!"
6-8s: Nora skids to a halt, pressing her back against the damp stone, chest heaving violently. Nora whispers (shaky exhale): "I think... I think we lost it."
```
(Thoại Mẫu 2 = 7 + 8 + 6 = 21 từ.)

---

## 2. Cảm xúc trên mặt vlogger (từ `/fk-scriptwriter` mục I, I2) · Bước 5

Model không hiểu tính từ trừu tượng ("she is terrified"). Ở shot selfie, mặt vlogger chiếm khung — tả **triệu chứng cơ thể**:

| Cảm xúc | Viết thế này |
|---|---|
| Sợ hãi | `rapid shallow breathing, eyes darting left and right, knuckles whitening around the spear shaft` |
| Quyết tâm | `jaw tightening, gaze narrowing to one point, one slow decisive nod` |
| Sốc | `sudden complete stillness, lips parting without a sound, breath held mid-inhale` |
| Kiệt sức | `shoulders sagging, slow heavy blink, leaning against the cave wall` |
| Nhẹ nhõm | `long slow exhale through parted lips, shoulders dropping, eyes closing for a beat` |
| Nghi ngờ | `head tilting slightly, eyes narrowing, weight shifting to the back foot` |
| Lạnh cóng | `teeth chattering, lips pale, breath fogging in short bursts, hands tucked under her arms` |

**Mỗi clip có một vòng cảm xúc A → B:** `0-3s` trạng thái A → `3-6s` chất xúc tác (âm thanh, cử chỉ của người bản địa, thú xuất hiện) → `6-8s` trạng thái B không quay lại được. Ví dụ hữu ích cho vlog: bình tĩnh → hoảng sợ; sợ → can đảm (nhắm mắt, hít một hơi, mở mắt nhìn thẳng); cảnh giác → nhẹ nhõm; cô lập → được chấp nhận (bắt gặp ánh mắt người bản địa, gật nhẹ).

---

## 3. Bộ công cụ hồi hộp (từ `/fk-scriptwriter` mục I4) · Bước 3

Dùng khi viết outline / Act — mỗi Act nên có ít nhất 1 kỹ thuật:

| Kỹ thuật | Bản cho vlog |
|---|---|
| **Ticking clock** | Mặt trời lặn dần / lửa sắp tắt / bão kéo tới — gắn với countdown `HOUR X — Y HOURS REMAINING` (`story-engine.md` mục 9). Chèn shot POV vật đếm giờ (than tàn, bóng đổ dài ra) |
| **Blind spot** | Selfie với vlogger 1/3 khung, **2/3 còn lại là bóng tối** phía sau (cửa hang, rừng). Thứ nguy hiểm đã có sẵn trong bóng tối từ giây 0, chỉ lộ dần (Bài học 48) |
| **Delayed reveal** | Clip A: selfie, mặt vlogger biến sắc nhìn qua vai máy (không quay máy). Cắt sang Clip B: POV thấy thứ cô thấy. Cấm lật 180° trong 1 shot (Rule 42) |
| **Sonic isolation** | Tuyệt đối im lặng khi rình mồi / áp sát cận chiến (Rule 49): trong prompt ghi `Strictly NO spoken dialogue. Her mouth stays firmly closed in dead silence`. Hậu kỳ tắt hẳn nhạc nền, chỉ còn tiếng thở dồn nén, tim đập và tiếng foley tự nhiên. Thoại dẫn chuyện chỉ chèn qua voiceover/subtitles nội tâm |
| **Deceptive calm** | Clip yên bình (hồ phẳng, đàn thú gặm cỏ) → vật rung nhẹ, chim bay tán loạn ở `6-8s` → cắt |
| **Time dilation** | Một khoảnh khắc 1 giây kéo thành cả clip 8s: bàn tay với tới mép đá, tia lửa rơi xuống bùi nhùi |

**Đổi cỡ cảnh liên tục** (mục G): không để 2 clip liền nhau cùng cỡ cảnh/góc. Xoay vòng selfie gần → POV rộng → POV chi tiết tay → selfie qua vai → máy dựng.

**Kiểu cảnh dùng được** (mục D, đã đổi sang góc của vlogger): establishing shot = 3 shot rộng 4s không thoại (`story-engine.md` mục 2b); insert/detail = POV xúc giác; reaction = selfie cận mặt + triệu chứng cơ thể; surveillance = POV quay lén từ chỗ nấp; silent moment = cảnh cuối. Không dùng: two-shot người thứ ba, montage nhiều góc trong 1 clip, crane/aerial (trừ khi user yêu cầu drone).

---

## 4. Trạng thái trang phục (từ `/fk-character-bible` mục 3) · Bước 2, 7

Khi trang phục **đổi giữa chừng tập** (ướt, rách, dính bùn, được khoác thêm da thú, bị thương băng bó):
- Mỗi trạng thái = một ảnh Body riêng: `<V> Body`, `<V> Body Wet`, `<V> Body Fur Cloak`… Vẫn **không** tạo entity Outfit (Rule 46).
- Mỗi ảnh trạng thái làm theo **công thức outfit lock** (`character-bible.md` §6): EDIT từ **Body trần gốc** (không chain từ ảnh trạng thái trước — Rule 46), câu `[OUTFIT]` tả đủ bộ đồ của trạng thái đó (vd thêm "soaked dark suede, clinging wet, mud-streaked leggings"); xóa logo → upload lại → user duyệt. Câu `[OUTFIT]` của trạng thái cũng là `OUTFIT LOCK` của các clip dùng trạng thái đó.
- Scene dùng đúng Body của trạng thái: `character_names: ["<V>", "<V> Body Wet", ...]`. Clip chuyển trạng thái (đang khoác áo vào) dùng Body của trạng thái **trước**, tả động tác mặc theo Bài học 46.
- Ghi bảng trong `script.md`:

  | Trạng thái | Từ clip | Đến clip | Entity Body | Khác biệt so với trạng thái trước |
  |---|---|---|---|---|

- Dấu nhận diện cố định (tàn nhang, nốt ruồi, kiểu tóc) nằm trong `CHARACTER_LOCK` và ảnh mặt, không đổi theo trạng thái.

---

## 5. Nhiều tập — mang mặt + Body trần gốc sang tập mới (từ `/fk-character-bible` mục 6) · Bước 6–7

Mỗi tập là thời kỳ mới, trang phục mới, bối cảnh mới. Mang sang tập mới **2 thứ cố định** của vlogger: ảnh mặt `<V>` và **Body trần gốc** (`uploads/<v>_body_v3_clean.jpg`). Body đã mặc outfit thì **tạo mới cho từng tập** bằng công thức outfit lock — không dùng lại Body mặc đồ của tập trước, không tạo entity Outfit.

1. **Mang mặt sang** bằng series manifest:
   ```bash
   python scripts/series_manifest.py sync --project-id <PID_TẬP_TRƯỚC>
   python scripts/series_manifest.py bootstrap --project-dir output/<slug-tập-trước>      --episode 2 --title "Rome 79 AD" --only "Nora"      --flow-project-id <FLOW_PROJECT_ID_TẬP_TRƯỚC>
   ```
   Dòng `Pre-linked entities: 1/1` = entity `Nora` của tập mới đã có `media_id` mặt cũ. `--flow-project-id` dùng lại Flow project cũ để media_id chắc chắn tham chiếu được; bỏ nó thì test 1 clip trước khi gen cả loạt.
2. **PATCH project** `{"allow_voice": true}` (`flowkit-pipeline.md` §3).
3. **Tạo entity `<V> Body`** cho tập mới: `POST /api/characters` `{"name": "Nora Body", "entity_type": "character", "description": "<body sheet 3 góc đã mặc outfit tập mới>"}` rồi gắn vào project bằng `POST /api/projects/<PID>/characters/<CID>`. Sau đó chạy **công thức outfit lock** ở `character-bible.md` §6 với `source_media_id` = Body trần gốc (cùng Flow project thì dùng lại UUID cũ; Flow project mới thì upload lại file) và `[OUTFIT]` = trang phục của tập mới.
4. ⛔ User duyệt ảnh Body đã mặc outfit → tiếp Bước 6 như bình thường. `CHARACTER_LOCK` (mặt, tóc, giọng) giữ nguyên; chỉ dòng `wearing …` đổi theo tập.

## 6. Âm thanh (từ `/fk-sound-design`) · Bước 10

Clip vlog có **thoại native lẫn ambient trong cùng một track** (không có TTS riêng), nên không duck riêng ambient được — chỉ duck **nhạc nền** theo track của clip.

```bash
# Nhạc tự hạ khi có tiếng trong clip, rồi master -14 LUFS / -1 dBTP cho YouTube (đã test: ra -13.8 LUFS)
ffmpeg -i final_cut.mp4 -i music.mp3 -filter_complex \
  "[0:a]asplit=2[dlg][sc];[1:a]volume=0.35[m];[m][sc]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400[md];[dlg][md]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:LRA=7:TP=-1.0[a]" \
  -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -ar 48000 final_mixed.mp4
```
- `volume=0.35` là mức nhạc khi không có tiếng; cảnh nguy hiểm và cảnh kết hạ tiếp (0.2) — cắt đoạn, chỉnh, rồi ghép.
- **SFX bổ sung** (`scripts/sfx_layering.py`): chỉ khi clip thiếu tiếng va chạm (Veo/Omni đã sinh foley native). Nó dò từ khóa trong prompt (`strike`, `thud`, `impact`, `flames`, `embers`, `heartbeat`, `gasping`…). Nghe lại trước khi giữ:
  ```bash
  python scripts/sfx_layering.py --input-video scenes/scene_012.mp4 \
    --prompt "3-6s: spear strike, heavy thud. 6-8s: gasping, heartbeat" --output scenes/scene_012_sfx.mp4 --volume 0.4
  ```
- Không dùng drone sub-bass của bumper. Nhịp im lặng = tắt nhạc, ambient vẫn chạy (`story-engine.md` mục 12).

---

## 7. Chuyển cảnh âm thanh & card chữ (từ `/fk-cinematic-transitions`) · Bước 10

**J-cut khi cắt thẳng** — tiếng của clip B vào sớm 0.5s, hình vẫn cắt thẳng tại khung che (đã test, hình–tiếng khớp):
```bash
ffmpeg -i A.mp4 -i B.mp4 -filter_complex \
  "[1:v]trim=start=0.5,setpts=PTS-STARTPTS[bv];[0:v][bv]concat=n=2:v=1:a=0[v];[0:a][1:a]acrossfade=d=0.5:c1=tri:c2=tri[a]" \
  -map "[v]" -map "[a]" -c:v libx264 -pix_fmt yuv420p -c:a aac AB.mp4
```
Hình B bị cắt 0.5s đầu đúng bằng phần tiếng B đã vào sớm. Chỉ dùng khi 0.5s đầu của B không có thoại (luật giấu mối nối). L-cut (tiếng A kéo dài sang B) làm tay trong CapCut. Cả timeline dài thì làm J/L-cut trong CapCut; lệnh trên để ghép thử từng cặp.

**Card chữ** — chỉ 3 loại: năm, mission card, countdown. Đè lên hình, không bumper nền đen, không fade (đã test):
```bash
ffmpeg -i clip.mp4 -vf "drawtext=fontfile='C\:/Windows/Fonts/arialbd.ttf':text='HOUR 3 — 21 HOURS REMAINING':fontcolor=white:fontsize=h/18:borderw=3:bordercolor=black@0.6:x=(w-tw)/2:y=h*0.08:enable='between(t,0.3,2.8)'" -c:a copy clip_card.mp4
```

**Không dùng từ skill này:** chapter bumper, dip-to-black/crossfade giữa clip, hardsub (`scripts/generate_subtitles.py --burn-subtitles`), `scripts/build_master_film.py` (dành cho phim nhiều chương có bumper). Dip/cut to black chỉ ở cảnh kết. Graphic match cut và whip pan đã có trong `transitions.md`. Rack focus dùng được trong POV (từ vật trong tay ra hậu cảnh).

---

## 8. Từ vựng chuyển động chuẩn · Rule 57 · Bước 5

Động từ mơ hồ ("moves quickly") để trống vector lực, model tự bịa ra trôi lướt, tua nhanh, méo tay chân. Mỗi chuyển động trong `timeline_action` và `physical_realism` viết bằng hành động vật lý cụ thể, rồi gắn thuật ngữ trong ngoặc. Không bao giờ chỉ viết thuật ngữ trơn.

| Hiện tượng thực tế | ❌ Từ ngữ mơ hồ (dễ méo/lướt trôi) | ✅ Thuật ngữ + câu prompt |
|---|---|---|
| **Lấy đà trước khi hành động** | `she prepares to jump`, `moves back` | **Anticipation**: `crouches low, lowering center of gravity to load leg muscles (anticipation)` |
| **Văng quá đà trước khi nén lại** | `stops suddenly`, `jerks stop` | **Overshoot & Settle**: `overshoots past the braking mark before settling back onto both heels` |
| **Chuyển động quán tính của tóc/tà áo** | `hair moves`, `clothes shake` | **Secondary Motion**: `secondary motion lag: ponytail snaps forward with inertia after body stops` |
| **Vật/người lộ ra** | `appears quickly`, `shows up`, `pops in` | **Reveal**: `the bison steps out from behind the boulder that has been in frame since second 0`. Không viết `pops into the frame` / `appears`: model sẽ cho vật mọc ra giữa clip (Bài học 48, 64) |
| **Hành động so le kế tiếp nhau** | `Torak does this, then Nora does that` | **Stagger**: `staggered reactions: Torak drops first, followed 0.5s later by Nora dropping behind the rock` |
| **Camera/tay kéo căng rồi nảy lại** | `camera jerks back and forth` | **Rubber-banding**: `reaches arm to maximum extension with slight rubber-banding elasticity` |
| **Độ trễ khi quay đầu** | `turns head slowly` | **Rotational Lag**: `head pivots quickly with rotational lag in camera tracking` |
| **Bước chạy nhấp nhô** | `camera bounces` | **Vertical Bounce**: `vertical bounce cadence matching rapid footfalls` |
| **Trượt dốc giảm tốc** | `slides down and stops` | **Slide & Dampen**: `frictional furrow dampens momentum gradually down the 45-degree slope` |
| **Tiếp đất / ngồi phịch xuống** | `falls down`, `sits` | **Impact & Compression**: `her knees bend deeply on landing, absorbing the impact, then she straightens` |
| **NPC đứng yên mà vẫn sống** | `stands there` | **Idle micro-motion**: `chest rises and falls, he blinks, shifts his weight to his left leg` |

**Cụm từ làm đơ hình** (model vẽ một tư thế rồi giữ nguyên — Bài học 81, checklist B dòng 50):

| ❌ Cấm | ✅ Thay bằng |
|---|---|
| `subtle smile` / `smiles` | `the corners of her mouth lift first, then her eyes crinkle; the smile settles after about a second` |
| `looks at the dinosaur` | `her eyes track the dinosaur from the ferns to the log, then flick back to the lens` |
| `reacts` | tên phản ứng cụ thể: `flinches`, `shifts her weight back`, `holds her breath`, `freezes mid-word` |
| `makes a gesture` | cử chỉ cụ thể + tay nào + mấy lần: `taps two fingers on the log twice` |
| `occasionally glances` | mốc cụ thể: `at 2s she glances left; at 4s her gaze returns to the lens` |
| `subtle movement`, `adds life`, `moves gracefully` | xóa; ghi bộ phận nào chuyển động, nhanh hay chậm, chạm vào đâu |

**Mẫu "never fully stops"** chỉ dùng cho cơ thể đứng yên của NPC và thú (dòng 51): `jaw keeps working, never fully stops chewing`, `flanks keep rising and falling, the tail never fully stills`. Không dùng cho tay đang neo (dòng 39, 52) hay đạo cụ phải đứng yên, vì nó sẽ làm chúng cử động.

Tên lỗi dùng khi review: **floating/gliding** (đi mà chân không đặt xuống), **foot sliding** (chân chạm đất vẫn trượt), **speed ramp** (đoạn tua nhanh), **linear robot motion** (khởi động và dừng đột ngột), **spawn/vanish**, **prop teleport**, **frozen NPC**, **gimbal float** (khung bay mượt mất cảm giác tay cầm).

---

## 9. Nhịp động học, điểm tựa & sửa lỗi chuyển động · Rule 58 · Bước 4, 5, 9, 10

### A. Khi viết storyboard & prompt (bước 4–5)

1. **Ngân sách thời gian:** mỗi mốc chỉ **1 beat chính**. Clip 8s: `0-3s / 3-6s / 6-8s`. Clip 10s (thoại 23–25 từ): `0-3s / 3-7s / 7-10s`. Nhồi 2–3 hành động vào một mốc ("cúi nhặt giáo, quay người, ném") làm model tua nhanh và méo hình. Beat thừa chuyển sang clip khác, báo user.
2. **Ba pha cho mọi động tác:** lấy đà (`anticipation`) → đỉnh vận tốc ở giữa mốc → hãm và hồi thăng bằng (`settle`). Không tả tốc độ đều từ đầu tới cuối. Vật nặng (thú lớn, tảng đá) tăng tốc chậm và cần nhiều bước để dừng.
3. **Quán tính thứ cấp:** tóc, lông viền, tà áo, dây trễ 0.2–0.3s so với thân; khi thân dừng thì chúng văng tiếp rồi mới `settle`. Chỉ gắn vào phần trang phục ref cho phép (Bài học 74).
4. **Điểm tựa cho mọi bộ phận chịu lực:** người ngồi, quỳ, ngả, dựa phải ghi rõ đặt lên đâu: mông trên gì, lưng tựa vào gì, chân đặt ở đâu, tay chống lên gì. Tư thế nghiêng mà không có vật đỡ thì model cho người lơ lửng. Tư thế giữ suốt clip thì viết một câu khóa ở đầu: `For the whole clip her back stays pressed against the rock wall and both boots stay flat on the cave floor.`
5. **Frame 0 là tư thế trước hành động đầu tiên:** muốn giây 2 nhân vật đứng dậy thì frame 0 phải đang ngồi; muốn giây 3 cầm đạo cụ lên thì frame 0 đạo cụ nằm trên bề mặt, tay ở đâu ghi rõ. Không tả frame 0 bằng trạng thái sau hành động.
6. **Chừa 0.5s cuối:** động tác chốt và chữ thoại cuối phải xong trước 0.5s cuối của clip (clip 10s: động tác xong trước ~9.5s, thoại xong trước ~9s). Model hay làm nhịp cuối trễ, dễ bị cắt.

Bảng chuyển động mỗi clip (đưa user duyệt cùng bảng vật lý ở bước 4):

| Mốc | Beat chính (1) | Lấy đà → đỉnh → hồi | Điểm tựa | Quán tính thứ cấp | NPC/thú (thở, chớp mắt, phản ứng so le) | Phản ứng của khung hình |
|---|---|---|---|---|---|---|

### B. Khi review 720p (bước 9)

Chạy cho mọi clip dưới 9/10 (ngưỡng giữ của user), mọi clip có Motion Quality hoặc Temporal Coherence < 7.5, và mọi clip có lỗi chuyển động nhìn thấy dù điểm cao.

1. **Soi lỗi** bằng frame của `/fk-review-video` (lỗi trượt chân và tua nhanh cần chế độ deep 8 fps): tốc độ bất thường, dừng như robot, trượt chân/trôi lướt, thiếu quán tính thứ cấp, đạo cụ mọc ra/biến mất/nhảy tay, NPC đơ, khung bay mượt như gimbal. Ghi giây + frame + tên lỗi (§8).
2. **Truy về prompt:** lỗi ở mốc nào, mốc đó thiếu gì (beat bị nhồi, thiếu điểm tựa, frame 0 sai tư thế, động từ mơ hồ, nhịp cuối sát 0.5s cuối).
3. **Motion Fix Plan** ghi vào `${OUTDIR}/motion-plans/scene_{idx}_{sid}.md`:
   - lỗi: giây, frame, tên lỗi, mức (CRITICAL = mọc/biến mất/biến dạng/thừa tay chân; HIGH = trôi, trượt chân, tua nhanh, dừng robot, gimbal float; MEDIUM = thiếu quán tính thứ cấp, NPC đơ);
   - khối prompt gây lỗi, trích nguyên văn;
   - khối mới, nguyên văn. **Chỉ đổi khối liên quan, phần còn lại giữ nguyên văn**, để mặt và bối cảnh không chạy. Sửa bằng cách tả thêm cho chính xác, không cắt bớt (Rule 56);
   - phần đụng vào prompt user đã duyệt → đưa thành lựa chọn cho user, không tự ghi đè.
4. `python tools/lint_prompt.py --file <prompt.json>` đạt 0 CRITICAL / 0 HIGH → PATCH scene → **hỏi user trước khi** `REGENERATE_VIDEO` (Rule 29).
5. Lỗi mới chưa có trong `production-lessons.md` → thêm bài học + dòng checklist B trong `prompt-lock.md`.

### C. Khi cắt nối (bước 10)

Kiểm hướng chuyển động giữa 2 clip liền nhau: rời khung bên phải ở clip A thì vào từ bên trái ở clip B, tốc độ tương đương; tư thế và hướng nhìn cuối clip A khớp 1–2s đầu clip B (Rule 44). Không khớp được thì cắt trong khung che hoặc J-cut (§7, `transitions.md`).
