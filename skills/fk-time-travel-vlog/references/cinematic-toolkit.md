# Cinematic toolkit cho time-travel vlog

Đọc ở các bước ghi trong từng mục. File này gom phần dùng được của 5 skill upstream — `/fk-action-choreography`, `/fk-scriptwriter`, `/fk-character-bible`, `/fk-sound-design`, `/fk-cinematic-transitions` — đã chỉnh theo luật vlog. **Dùng bản trong file này**, không chép nguyên template từ skill gốc: các template gốc có dòng `Negative:`, góc máy người thứ ba (dolly, orbit 180°, telephoto), lời dẫn TTS và thoại 10–12 từ — đều trái luật vlog.

Cách chuyển một template gốc sang vlog:

| Template gốc có | Đổi thành |
|---|---|
| `Negative: ...` | Câu khẳng định trước dòng `Audio:` (`prompt-lock.md` khối 8) |
| "The camera tracks / dollies / orbits / pushes in" | Góc nhìn của vlogger: selfie, POV hoặc máy dựng (`prompt-lock.md` khối 1) + rung tay theo bước chân (Bài học 25, 35) |
| `narrator_text` lời dẫn | Thoại native của vlogger 18–22 từ trong `video_prompt` (Rule 49) |
| Nhân vật chính là chiến binh/tướng | Vlogger là người sống sót bị cuốn vào; người bản địa làm phần khó |
| Kiếm, khiên, kỵ binh | Vũ khí và mối nguy đúng thời kỳ: giáo, đá, đuốc, thú lớn, bão |

---

## 1. Hành động & cảnh săn — 3 pha (từ `/fk-action-choreography`) · Bước 5

Mỗi clip hành động 8s đúng 3 pha, khớp luôn 3 sub-clip thoại:

| Sub-clip | Pha | Hình | Thoại (18–22 từ, câu ngắn đứt quãng) |
|---|---|---|---|
| `0-3s` | **Chuẩn bị** — hạ trọng tâm, siết tay cầm, khóa mắt vào mục tiêu | Mọi người/thú/vật đã ở đúng chỗ từ giây 0 (khối "already in place") | 6–7 từ, thì thầm / nín thở |
| `3-6s` | **Một đòn theo một hướng duy nhất** — đâm, ném, chạy, né | Tả quỹ đạo và tác động lên môi trường (tuyết tung, đá văng, lửa bùng), không tả xuyên thịt | 7–8 từ, đứt quãng, thở dốc |
| `6-8s` | **Thu thế & neo** — dừng trượt, giữ thế thủ, ngực phập phồng | Bụi/tuyết lắng, khói tan; máy rung dần ổn định | 5–7 từ, phản ứng / micro-hook |

**Góc máy cho hành động** (vlogger là người cầm máy):
- Chạy trốn, né: selfie một tay, máy nảy theo từng bước, cánh tay không bao giờ buông máy (Bài học 25, 39).
- Đâm/ném giáo, kéo thú, trèo, hai tay làm việc: **POV hoặc máy dựng** (Bài học 50) — vlogger không thể vừa giữ máy vừa dùng hai tay.
- Người bản địa ra đòn chính: selfie qua vai (vlogger 1/3 tiền cảnh) hoặc POV từ chỗ nấp (`/fk-camera-guide` mục 6 "quay lén").

**Từ vựng an toàn chống méo người:**

| Hành động | ❌ Dễ méo / bị chặn | ✅ Viết thế này |
|---|---|---|
| Đâm giáo vào thú | `spear pierces the bison's chest, blood sprays` | `thrusts the spear forward in one straight line toward the bison's flank; snow bursts up where the bison stumbles` |
| Ném giáo | `throws three spears in two seconds` | `draws the spear back to her shoulder, then throws once; the spear streaks diagonally across the frame` |
| Thú lao tới | `the mammoth charges straight into the lens` | `the mammoth charges diagonally from the far left toward the right edge, snow churning under its feet` |
| Né | `she backflips away` | `she drops low and sidesteps to the right, the tusk sweeping past above her` |
| Vật lộn với thú / người | `wrestles the wolf on the ground` | Giữ khoảng cách một sải tay; cho thấy hậu quả: tuyết tung, máy chúi, thở dốc |
| Đập đá, đánh lửa | `smashes rocks rapidly` | `strikes the flint once against the pyrite above the tinder; a single spark drops onto it` (`story-engine.md` mục 7d) |
| Quay người | `spins 360 degrees` | Tách 2 clip, cắt thẳng (Rule 42, 44) |

Thương tích, máu, cái chết: chỉ cho thấy **hậu quả** (tuyết đỏ ở xa, con thú nằm yên, nhóm im lặng), không cho thấy lúc xuyên/thương — vừa tránh `UNSAFE_GENERATION` vừa tránh model làm cong vũ khí.

**Mẫu khung một clip săn** (ghép vào khung 9 khối của `prompt-lock.md`, không thay thế nó):
```text
0-3s: Torak crouches low behind the snow ridge, gripping one spear with both hands, eyes locked on the bison twenty paces ahead. Nora whispers (barely breathing): "Don't move. Don't even blink. He's waiting."
3-6s: Torak rises and thrusts the spear forward in one straight line toward the bison's flank; snow bursts up as the bison stumbles sideways. Nora says (sharp gasp, voice cracking): "He hit it— it's turning toward us!"
6-8s: The bison skids to a halt, breath steaming; Torak holds his ground, chest heaving. Nora says (shaky laugh): "Okay. Okay. Still alive. Barely."
```
(Thoại = 7 + 7 + 5 = 19 từ.)

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
| **Sonic isolation** | Hậu kỳ: tắt nhạc 1–2s trước reveal, chỉ còn tiếng thở + gió. Ghi `[im lặng Xs]` trong kịch bản |
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
