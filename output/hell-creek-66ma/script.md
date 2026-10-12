# I Time Travelled to the Last 18 Hours of the Dinosaurs

**Slug:** `hell-creek-66ma` · **Vlogger:** Nora · **Bối cảnh:** Hell Creek Formation, Montana, 66.043 triệu năm trước (Maastrichtian muộn), cách tâm va chạm Chicxulub ~3.000 km
**Định dạng:** Long-form ~10 phút · HORIZONTAL 16:9 · material `cretaceous_vlog`
**Model:** Omni Flash R2V Ingredients (`GENERATE_VIDEO_REFS` / `abra_r2v_<N>s`, RPC `MZZa6b`) — KHÔNG start frame, KHÔNG i2v (Rule 27)

**Toán clip:** 1 master 10s + 76 clip 8s + 3 EST (6s + 4s + 4s) = **80 lần sinh**
Thời lượng dựng ≈ **9:45**

---

## Changelog

| Ngày | Thay đổi |
|---|---|
| 2026-10-12 | Bản đầu. Chốt 4 lựa chọn: long-form ~10 phút / Nora tái dùng / Hell Creek 3.000 km từ tâm / kết "ở lại chứng kiến, im lặng". Output 4 subagent (action-choreography, camera-guide, cinematic-transitions, add-material) đã nhúng. |

---

## Khai báo chữ trên màn hình

Chỉ **3 loại chữ**, **toàn bộ làm ở hậu kỳ**, không bao giờ nằm trong `video_prompt` (story-engine §9):

1. **Thẻ năm** — `66,043,000 BC · HELL CREEK, MONTANA` — 1 lần, ngay sau EST-01.
2. **Thẻ nhiệm vụ** — `3,000 KM FROM GROUND ZERO` — 1 lần, cuối Act 1.
3. **Thẻ đếm ngược** — `HOUR X — Y HOURS REMAINING` — 7 lần, bảng dưới.

Mọi `video_prompt` mang câu khẳng định: *"No subtitles, captions, labels, icons or text of any kind appear anywhere in the frame."*

### 7 mốc đếm ngược

| # | Thẻ | Clip | Sự kiện neo |
|---|---|---|---|
| C1 | `HOUR 0 — 18 HOURS REMAINING` | A1-02 | Nora bò lên bãi sỏi |
| C2 | `HOUR 2 — 16 HOURS REMAINING` | A1-12 | Bò đực dọa-xông giả |
| C3 | `HOUR 7 — 11 HOURS REMAINING` | A2-09 | Cả đàn cùng đứng sững — T. rex đi ngang |
| C4 | `HOUR 11 — 7 HOURS REMAINING` | A3-02 | Đàn rời đi, Nora chạy theo |
| C5 | `HOUR 13 — 5 HOURS REMAINING` | A3-08 | Vỡ bầu nước |
| C6 | `HOUR 17 — 1 HOUR REMAINING` | A3-15 | Thắng giả — uống nước ở hố nước |
| C7 | `HOUR 18 — 0 HOURS REMAINING` | A4-03 | Bóng thứ hai mọc ngược hướng |

---

## 1. GIẢ ĐỊNH

1. Nora chọn **đúng ngày này** và biết mình chọn gì — cô nói ra **một lần duy nhất** ở A1-05, rồi không nhắc lại. Mọi cảnh bình yên sau đó mang sức nặng của điều khán giả biết mà đám thú không biết.
2. Ở Hell Creek, cách tâm 3.000 km, **không ai nhìn thấy quả cầu lửa**. Chỉ thấy: một thứ sáng hơn mặt trời ở chân trời đông nam → ~10 phút sau mặt đất chuyển mình → ~30 phút sau mưa hạt thủy tinh nóng → ~1 giờ sau trời bốc cháy. Phim bám đúng trình tự này.
3. Nora **không có bộ tộc**. Vai "người bản địa" do **một đàn Triceratops horridus** đảm nhiệm — thứ duy nhất trong thung lũng biết đọc vùng đất này. Ngôn ngữ không hiểu được = tiếng kêu và tín hiệu cơ thể.
4. Nora **không bao giờ đánh nhau với bất cứ con gì** (Rule 51). Cô né, nấp, bám theo, chịu đựng. Khoảng cách là vũ khí duy nhất.
5. Cô **ở lại**. Không có cảnh quay về. Cảnh cuối không thoại.

---

## 2. CHARACTER BIBLE

### 2.1 CHARACTER_LOCK

```
CHARACTER_LOCK:
Nora, a 26-year-old Western woman with a heart-shaped face, hazel-green eyes, dense freckles across nose and cheeks,
bright copper-red hair in a high bun held by a dark wooden hairpin, a few loose strands at the temples,
wearing an olive-drab waxed-canvas field shirt with sleeves rolled above the elbow and the collar open,
a dark brown leather chest harness with two flat pouches, heavy slate-grey canvas trousers, scuffed brown leather boots.
Voice: Laomedeia - upbeat, mid-high pitched, energetic expressive conversational female voice, fast confident vlog delivery with dry humor, rises into real cracking screams when in danger, drops to a fast whisper when hiding.
```

### 2.2 BODY LOCK (CRITICAL) — verbatim, không sửa một chữ

```
BODY LOCK (CRITICAL): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and a voluptuous hourglass figure, featuring an exceptionally large, full, voluminous heavy bust with prominent deep cleavage valley in plunging V-neckline, a tiny narrow waist, and wide curvaceous hips matching Nora Body ref; she is NOT skinny, NOT slender, NOT petite, NOT flat-chested.
```

### 2.3 OUTFIT LOCK — khóa thuần ảnh ref (Rule 52 §2)

```
OUTFIT LOCK: Nora wears the exact field outfit shown in the Nora Body reference sheet (NO fur, NO hood, NO shearling collar, NO cloak, NO modern logo, NO outfit variations). From the very first frame to the last, Nora is fully dressed in the complete outfit. No part of the outfit appears, disappears or changes.
```

> **Tuyệt đối không mô tả lại trang phục bằng lời trong `video_prompt`** — chỉ trỏ ref. Bài học Scene 21 (lông cổ cừu trắng tự mọc).

### 2.4 ID-LOCK (khối 5 của mọi `video_prompt`)

```
[ID-LOCK] Nora keeps her face and hair from the Nora face sheet, and her build and clothing from the Nora Body sheet (which shows her full body dressed in this field outfit). Her face, hair colour, hairline, freckles, eye colour and body proportions are identical in every frame and never drift.
```

### 2.5 Tài sản cố định

| Asset | Nguồn | Ghi chú |
|---|---|---|
| `Nora` (mặt + tóc) | `uploads/nora_main.jpg` (đã có) | Tái dùng, không sinh lại |
| `Nora Body` (sheet 3 panel ĐÃ MẶC outfit) | `EDIT_CHARACTER_IMAGE` **1 lần** từ `uploads/nora_base_body_clean.jpg` | **Không chain edit.** Xóa logo → upload lại → UUID sạch (Rule 28) |
| `Hell Creek Bank` (bãi sỏi ven sông) | ref bối cảnh 16:9 | Dùng chung 14 clip |
| `Hell Creek Trail` (lối mòn rừng cọ) | ref bối cảnh 16:9 | Dùng chung 18 clip |
| `Hell Creek Waterhole` (hố nước) | ref bối cảnh 16:9 | Dùng chung 16 clip |

**Q1 — Proportion lock trước khi sinh `Nora Body`** (cổng 5.5): chốt thành câu chữ trong prompt ảnh Body —
`net height 178 cm; head height = 1/7.6 of total; shoulder width = 1/4.1 of height; leg length from hip crease to floor = 0.54 of height; foot baseline level across all three panels; identical camera distance and identical eye-level in all three panels.`

**Giới hạn ref mỗi clip = 3.** Phân bổ: `Nora` + `Nora Body` + **1** ref bối cảnh HOẶC 1 ref sinh vật. Không bao giờ 4.

### 2.6 Bảng "nhân vật" — đàn Triceratops & các loài

Không loài nào có thoại. Cột *Tiếng* tả bằng chữ trong khối `Audio:` — **không** gán voice id (voice id chỉ dành cho người).

| Tên nội bộ | Loài | Dấu nhận diện (Q3) | Vai trò kịch | Tiếng |
|---|---|---|---|---|
| **Bò Đực** | Triceratops horridus, đực trưởng thành | Sừng trái gãy cụt 1/3; vết rạch cũ chạy ngang diềm xương; mõm rộng vuông | "Thủ lĩnh" — kẻ từ chối Nora ở Act 1, kẻ chấp nhận cô ở Act 2 | Gầm trầm cộng hưởng từ lồng ngực, cào chân trước |
| **Con Cái Già** | Triceratops horridus, cái già | Diềm xương bạc màu, mép diềm sứt nhiều; dáng đứng trũng lưng | Con **đầu tiên** đứng sững khi nguy hiểm tới — tín hiệu của Act 2 | Thở phì dài qua mũi |
| **Con Non** | Triceratops horridus, non ~2 tuổi | Sừng mới nhú, diềm còn mềm bo tròn, bùn đỏ khô kín bụng | Con duy nhất chịu lại gần Nora. Trở lại ở payoff và cảnh cuối | Kêu ngắn cao, hai nhịp |
| **T. rex** | Tyrannosaurus rex trưởng thành | Sẹo dọc mõm, nhiều ruồi quanh miệng, da vảy hoàn toàn **không lông** | Mối nguy gieo ở Act 1 (xác thú), hiện thân ở Act 2 — **không bao giờ bị đánh** | Bước nặng làm rung đất, thở ồm sâu |
| **Borealosuchus** | Borealosuchus sternbergii ×2 | Chỉ lộ dải lưng sần + chóp mõm | Mối nguy mở màn, đẩy Nora khỏi nước | Nước vỗ, không kêu |
| **Edmontosaurus** | Edmontosaurus annectens | Xác bị ăn dở, vết răng to bằng bàn tay | **Không sống.** Lời cảnh báo bằng hình, không bằng chữ | — |
| **Quetzalcoatlus** | Quetzalcoatlus northropi | Cao như hươu cao cổ, đi bốn chân, mỏ giáo thẳng | Dấu hiệu "trời" — 2 lần; lần 2 là cầu nối sang Act 4 | Cánh da quạt, **không** kêu như đại bàng |

**Khóa khi ≥2 con cùng khung:** `each animal is a separate body with its own complete outline; they never overlap, merge, share a limb or pass through one another.`

**Q2 — Permanent prop geometry** (chỉ dùng trong prompt **ảnh ref**, không dùng trong `video_prompt`):
`Water vessel: the upper shell of a small turtle, 22 cm across, a flattened dome with six visible scute plates and a chipped rear edge, two holes drilled near the front rim with a twisted plant-fibre cord knotted through them, carried hanging at her LEFT hip from the chest harness; the inner face is pale and scraped smooth, the outer face is dark olive and scratched. It is not a round ball, not a bottle, not a bowl on a strap, not a pouch, not a gourd.`

---

## 3. MATERIAL

```json
{
  "id": "cretaceous_vlog",
  "name": "Cretaceous Field Documentary",
  "style_instruction": "Raw handheld natural-history field footage shot on location in a hot humid Late Cretaceous floodplain forest. Unprocessed documentary look: true-to-life colours, no grade, no colour filter, mild high-ISO grain crawling in the shadows, highlights that clip to flat white where the sun hits, shallow-depth background falloff with a soft bokeh that never looks painted. Subtropical haze softens everything past thirty metres; sweat, humidity and fine airborne grit sit in the air. Extinct animals are rendered to current palaeontological reconstruction standards with real animal skin physics: slack dewlaps, scar tissue, insect bites, caked red mud on the belly and feet, flies, laboured breathing that visibly moves the ribcage. Everything carries the weight and imperfection of real wildlife footage recorded by one person who is physically present and in danger.",
  "negative_prompt": "NOT a 3D render, NOT CGI, NOT a video-game cinematic, NOT a movie trailer, NOT concept art, NOT matte painting, NOT colour-graded teal-and-orange, NOT HDR tone-mapped, NOT a slow-motion hero shot, NOT a smooth flying aerial move, NOT a snowy landscape, NOT a desert, NOT a volcano erupting in the foreground, NOT mountains, NOT clean studio lighting, NOT plastic or rubbery skin, NOT oversaturated, NOT sharpened, NOT any modern manufactured object, NOT any on-image interface, icon, label, watermark or text.",
  "scene_prefix": "Raw handheld field documentary footage, Hell Creek floodplain 66 million years ago: Sabalites palm groves, magnolia and tree ferns under tall conifers, churned red mud, silty brown creek water, hot haze. Natural light only, true colours, visible grain, real amateur recording, not a 3D render.",
  "lighting": "Hot humid subtropical daylight filtered through palm and conifer canopy; hard dappled patches on the mud, heavy green bounce, thick haze in the depth, highlights clipping to white, no artificial fill"
}
```

**3 biến thể `scene_prefix`** (PATCH theo cụm cảnh — một prefix sẽ sai màu ở 2/3 phim):

- **A — ban ngày** (Cold open → A3-15): như trên + `Ordinary hot hazy daylight, a normal pale blue sky with high cloud.`
- **B — trời bốc cháy** (A4-04 → A4-18): `...now lit only by a sky burning deep orange shading to blood red from horizon to zenith. Every surface takes a hot copper rim light and the shadows go dark red; glowing specks of molten glass streak down and hiss into the mud, thin smoke rising where they land. No sun disc is visible.`
- **C — impact winter** (Act 5): `...after the strike: grey ash falls steadily like dry snow and lies ankle deep over the drooping palms, the burnt ferns and the dead creek. The sun is gone; light is a flat dim brown-grey dusk with no shadows and almost no colour left, visibility under forty metres.` — **kèm bắt buộc:** `warm dry grey volcanic-looking ash, not snow; the air is still hot and humid and nothing is frozen.`

### 7 mốc ánh sáng (khối `Setting:`, chạy **một chiều**, không quay lui)

| # | Mốc | Clip | Câu EN |
|---|---|---|---|
| L1 | Bình minh | CO, EST-01, A1-01→06 | `Thin cool dawn light filters sideways through the palm fronds in long soft bars; the air is heavy with river mist, colors are still desaturated, and every surface is beaded with cold dew.` |
| L2 | Giữa sáng | A1-07→14 | `Clean warm morning light, strong but not yet harsh; shadow edges are crisp, greens read bright and saturated, and a faint haze still softens the far tree line.` |
| L3 | Trưa gắt | Act 2, EST-02 | `Flat hard overhead light with almost no shadow length; highlights blow out on bare mud, deep shadows sit directly under every leaf, the air shimmers with heat, and the whole frame looks bleached and glaring.` |
| L4 | Chiều, ánh sáng bắt đầu sai | Act 3, EST-03 | `Low amber light with long raking shadows, but the color sits a half-step too orange and too still for the hour; dust hangs in the beams and refuses to settle, and everything feels oddly motionless.` |
| L5 | **Khoảnh khắc va chạm** | A4-03 | `A single silent flash floods the entire frame from beyond the horizon and washes all color out to white for an instant; as it decays, every shadow on the ground has reversed direction and stretched the wrong way, and a hard pale rim now edges every leaf and every body.` |
| L6 | Trời đỏ rực | A4-04→18 | `The whole sky burns a deep furnace red and lights the forest from above like an open hearth; faces and leaves catch a hot copper glow from overhead instead of from the side, shadows pool thick and black beneath everything, and the light pulses slightly as streaks cross the sky.` |
| L7 | Tro phủ | Act 5 | `A heavy grey fall of ash drains the color out of everything to a dim monochrome; the light is flat, sourceless and failing minute by minute, ash settles thick on every upward-facing surface, and visibility closes in until only the nearest few metres remain readable.` |

### 10 từ cấm thêm cho tập này

`apocalyptic` → `the sky has gone wrong` · `epic` → `she cannot see the far side of it` · `cinematic` → `raw field footage` · `movie dinosaur` → `current palaeontological reconstruction` · `meteor`/`asteroid impact`/`fireball` → `the whole sky turns orange then deep red` · `extinction event`/`doomsday` → `the last hours` · `volcanic eruption`/`lava` → `hot ash falls` · `dramatic lighting`/`god rays` → `light from the sky only, no other source` · `slow motion`/`hero shot`/`sweeping` → `handheld, every stride jolts the frame` · `hyperrealistic`/`8K`/`octane render` → `visible grain, natural skin texture, real animal weight`

(Bổ sung: `survivor`, `inferno`, `war-torn` cũng kéo tone trailer.)

### Khối anti-CGI (dán cuối mọi `video_prompt` cảnh thảm họa — Act 4 & 5)

```
This is real amateur footage recorded by one frightened person standing in the middle of it, not a 3D render and not a film production. The image carries visible high-ISO grain that crawls in the shadows, and where the burning sky or a glowing fragment is brightest the picture clips to a flat blown-out white with no detail left inside it. Every breath and every stride jolts the whole frame, the horizon tilts a few degrees and rights itself, and a hard streak of light smears diagonally across the picture whenever the brightest part of the sky passes near the edge of frame. Twice the picture drifts soft for about half a second and then snaps back sharp as focus resettles on whatever is closest. Fine grit and spatter show as fixed soft smears in the same spots of the picture while the scene moves behind them, blooming whenever light passes through them. Nothing happens in slow motion, nothing is smoothed or stabilised, no move is repeated from a second angle, and the picture is clean footage only with no interface, no indicator, no icon, no label and no text anywhere in it.
```

---

## 4. CHUỖI NHÂN QUẢ

Mọi mắt xích nối bằng **"vì vậy"** hoặc **"nhưng"**. Không có "và rồi".

| # | Mắt xích | Nối |
|---|---|---|
| 1 | Nora hiện ra giữa lạch nước nông, ngập ngang đùi | — |
| 2 | Hai dải lưng Borealosuchus đã nằm sẵn trong nước cách 5 m | **NHƯNG** |
| 3 | Cô đẩy người lên bãi sỏi | **VÌ VẬY** |
| 4 | Trên bãi sỏi là xác Edmontosaurus bị ăn dở, vết răng to bằng bàn tay | **NHƯNG** |
| 5 | Cô hiểu bãi trống là chỗ chết — phải rời khỏi đó | **VÌ VẬY** |
| 6 | Bìa rừng là bức tường dương xỉ không đọc được | **NHƯNG** |
| 7 | Chỉ một thứ đọc được: lối mòn rộng đầy dấu chân ba ngón | **VÌ VẬY** |
| 8 | Cô bám theo lối mòn, tìm được đàn Triceratops — thú lớn là tấm khiên | **VÌ VẬY** |
| 9 | **HỎNG 1** — Bò Đực dọa-xông giả, cô đổ người vào bụi dương xỉ. Hết Act 1 cô vẫn ở **ngoài** đàn | **NHƯNG** |
| 10 | Cô phải học khoảng cách mà đàn cho phép | **VÌ VẬY** |
| 11 | Act 2: quan sát, bắt chước, học tín hiệu — diềm ửng máu, cào chân, yếm rung. Bài học cốt lõi: **khi tất cả cùng đứng sững, có thứ đang tới** | **VÌ VẬY** |
| 12 | Bài học bị kiểm tra: cả đàn đứng sững → T. rex đi ngang → cô nấp sau thân cây đổ, **không một từ** | **VÌ VẬY** |
| 13 | **THẮNG MỘT PHẦN** — cô sống vì đã đọc được chúng. Đàn chịu cho cô đứng cách 20 bước | **NHƯNG** |
| 14 | Trời nóng lên, mai rùa đựng nước gần cạn | **VÌ VẬY** |
| 15 | Act 3: mục tiêu có hạn chót — theo kịp đàn khi chúng kéo tới hố nước | **NHƯNG** |
| 16 | Đàn đi nhanh, cô tụt lại | **VÌ VẬY** |
| 17 | **HỎNG 2** — cô làm rơi mai rùa trên bãi bùn, nó vỡ, nước ngấm hết vào cát. **Mất cả nước lẫn đàn** | **VÌ VẬY** |
| 18 | Cô phải lần dấu một mình qua bãi trống — đúng thứ xác Edmontosaurus đã dạy cô đừng làm | **NHƯNG** |
| 19 | **THẮNG GIẢ** — cô tìm được đàn ở hố nước, uống được, Con Non cho cô lại gần. Lần đầu tiên thấy an toàn | **NHƯNG** |
| 20 | Tất cả cùng đứng sững — đúng tín hiệu Act 2. Cô quét mắt tìm T. rex. **Dưới đất không có gì cả** | **VÌ VẬY** |
| 21 | Act 4: một cái bóng thứ hai mọc ra, cứng hơn, chỉ ngược hướng | **VÌ VẬY** |
| 22 | ~10 phút sau: sóng địa chấn. Cây đổ. Cô bị quật sấp | **VÌ VẬY** |
| 23 | Đàn vỡ chạy. Cô chạy theo nhưng không theo kịp | **VÌ VẬY** |
| 24 | Cô một mình giữa bãi trống khi trời bắt đầu rơi thủy tinh | **NHƯNG** |
| 25 | Con Non đã lao sẵn về hốc dưới bờ sông theo bản năng | **VÌ VẬY** |
| 26 | Cô chạy theo **con vật**, không phải cứu nó — bài học Act 2 dùng lần cuối | **VÌ VẬY** |
| 27 | **PAYOFF** `MASTER-GLASS` 6→10s: dưới bờ đất, tấm da ướt, hạt thủy tinh trên cẳng tay, bùn dập | **VÌ VẬY** |
| 28 | Act 5: rừng cháy → tro rơi → mặt trời tắt → im lặng → Con Non đi vào màn tro → hết, không thoại | — |

---

## 5. OUTLINE 5 ACT

### Cold open (8s) — cắt từ `MASTER-GLASS`
Nora ép mình dưới bờ sông, trời đỏ rực, hạt thủy tinh nóng cắm xuống cát quanh cô. Cô kéo tấm da ướt trùm lên, còn một chiếc giày ngoài. **CẮT ĐEN.**

### EST-01 (6s) — aerial wide, bình minh, không thoại → thẻ năm

### ACT 1 — ARRIVAL (14 clip, HOUR 0 → HOUR 2)
**Câu hỏi:** *Thứ gì ở đây sẽ giết cô trước — và cô bám vào đâu để sống?*
**Hỏng thì thấy gì:** Bò Đực dọa-xông giả; hết Act cô ngồi một mình ngoài rìa đàn, trời đã sáng rõ, tay không.
→ thẻ nhiệm vụ `3,000 KM FROM GROUND ZERO`

### ACT 2 — READING THE HERD (16 clip, HOUR 2 → HOUR 7)
**Câu hỏi:** *Cô có học nổi thứ ngôn ngữ không phải của người không?*
**Hỏng thì thấy gì:** T. rex đi ngang cách 15 bước. Không đọc được tín hiệu đứng sững thì cô đã ở giữa lối mòn.
**Thắng một phần:** đàn chịu cho cô ở trong vòng 20 bước.

### EST-02 (4s) — aerial very high, trưa gắt, **một vệt sáng mảnh đơn độc** trên nền trời xanh. Không ai dưới đất nhận ra.

### ACT 3 — THE WATER HOLE (16 clip, HOUR 7 → HOUR 17)
**Câu hỏi:** *Cô giữ được chỗ của mình trong đàn khi đàn di chuyển không?*
**Hỏng thì thấy gì:** mai rùa vỡ, vũng nước sẫm lại rồi co mất vào cát; đàn đã thành những chấm xa.
**Thắng giả:** cô đuổi kịp, uống được, Con Non đứng cách một sải tay.
→ thẻ `HOUR 17 — 1 HOUR REMAINING`

### EST-03 (4s) — aerial cực cao, kéo lùi, rừng trải vô tận không một dấu vết người, chính giữa khung một đốm lửa nhỏ xíu. Trời đã sang màu đồng. Không có đàn thú. **Cô lập tuyệt đối.**

### ACT 4 — IMPACT (18 clip, HOUR 18 → +40 phút)
**Câu hỏi:** *Thứ cô học được từ đám thú có cứu nổi cô không?*
**Hỏng thì thấy gì:** đàn vỡ chạy bỏ cô lại; cô một mình giữa bãi trống khi trời bắt đầu rơi.
**Payoff:** `MASTER-GLASS` 6→10s — cô chui được xuống hốc bờ sông, dập hạt thủy tinh bằng bùn ướt, và một bàn chân Con Non đặt xuống ngay cạnh cô.

### ACT 5 — IMPACT WINTER (12 clip)
**Câu hỏi:** *Khi không còn gì để làm nữa thì làm gì?*
Rừng cháy ở chân trời → tro rơi dày như tuyết → mặt trời tắt hẳn → mọi tiếng sinh vật biến mất.
**Cảnh cuối (7s, FIXED CAM, 0 từ):** Con Non đứng dậy khỏi chỗ nấp, đi chậm vào màn tro, mất hút. Nora ngồi yên trong khung, tro phủ dần lên vai. Cô không nói gì. **CẮT THẲNG SANG ĐEN, không fade.**

---

## 6. NHỊP DỰNG (clip 8s → `-ss 1` → 7.0s khả dụng; "cắt sớm" = cắt đuôi)

| Act | Nhịp | Độ dài sau trim | Ghi chú |
|---|---|---|---|
| Cold open + EST-01 | Dài | 8.0s + 7.0s | Cold open giữ nguyên master take |
| Act 1 | Dài (thiết lập) | 6.5–7.0s | Tối đa 1 clip cắt xuống 5.5s làm điểm nhấn |
| Act 2 | Chậm → vừa | 5.5–7.0s so le | Clip quan sát giữ 7.0s; clip chi tiết tay cắt 5.5s |
| Act 3 | Ngắn dần → payoff dài | 5.0 → 4.5 → 4.0s, rồi **7.0s** | Chuỗi dồn 3–4 clip, rồi giữ đủ ở "thắng giả" |
| Act 4 | **Ngắn nhất phim** | 3.0 → 3.5 → 4.5s | **Ngoại lệ giữ đủ 7.0s:** A4-03 (Shadow-flip) và A4-07 (sóng địa chấn đầu) |
| Act 5 | **Dài nhất** | 7.0s, clip kết không trim đuôi | Đảo ngược hoàn toàn Act 4 |

**Kiểm tra:** không 3 clip liên tiếp cùng độ dài (±0.3s); mỗi Act ≥1 clip giữ đủ 7.0s làm điểm neo thở; Act 4 nhiều clip nhất nhưng tổng thời lượng **không** dài nhất.

---

## 7. CHU KỲ GÓC MÁY (Rule 42 — không tỷ lệ %, chỉ ràng buộc định tính)

| Bước | Góc máy | Cỡ cảnh | Vai trò |
|---|---|---|---|
| R1 | POV | EWS/WS | Mở không gian, đặt mối nguy ở xa |
| R2 | POV nhìn xuống tay | CU tay | Xúc giác, hạ nhịp |
| R3 | POV từ chỗ nấp (Nora off-screen) | MS qua lỗ nhìn lá | Căng thẳng, Sonic Isolation |
| R4 | Selfie / OTS | MCU / MS | Thoại 18–22 từ, phản ứng cảm xúc |
| R5 | Máy dựng cố định | MS ngang ngực | Thao tác 2 tay, cho mắt nghỉ |
| R6 | POV macro | ECU | Chi tiết chốt beat, mở chuyển cảnh |

**Ràng buộc:** cấm 100% selfie · cấm 3 selfie liên tiếp · **cấm 2 clip liền nhau cùng cỡ cảnh + cùng góc máy**. Khi beat buộc POV hai clip liền nhau → **bắt buộc đổi cỡ cảnh** (van xả hợp lệ duy nhất).

---

## 8. "VIỆC" — mỗi shot phải làm ≥1

`1` = tăng nguy hiểm · `2` = tạo câu hỏi · `3` = quan hệ với đàn · `4` = tiến gần mục tiêu
