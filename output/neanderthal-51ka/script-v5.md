# Script v5: I Survived 24 Hours with Neanderthals (51,000 Years Ago)

**Bản nháp chờ duyệt.** Gồm storyboard toàn tập, bảng vật lý toàn tập, và `video_prompt` đầy đủ cho Cold open + Act 1. Prompt Act 2–5 viết sau khi user duyệt bảng vật lý và Act 1 (cổng duyệt từng Act, skill mục 6). `script.md` (v4) giữ làm tham chiếu.

Nguồn: `outline-v5.md` (khung đã duyệt) + research §1–13 (`.omc/research/neanderthals_pech_de_l_aze_51ka_research.md`) + `/fk-camera-guide` + PROMPT LOCK §10b.

---

## 1. Giả định

| | |
|---|---|
| Khung hình | Horizontal 16:9 |
| Độ dài | ≈ 7:54 |
| Số lần sinh | 60: 1 master 10s, EST-01 6s, EST-02/03 4s (giữ 4s, user duyệt 2026-10-05), 56 clip × 8s |
| Model | `GENERATE_VIDEO_REFS` (Omni Flash `abra_r2v_<N>s`). `duration` PATCH đúng 4/6/8/10 cho từng scene, vì giá trị thiếu sẽ thành 10s |
| Voice Slot 7 | Laomedeia, chỉ cho Nora. Giọng người bản địa tả bằng chữ trong prompt |
| Material | `prehistoric_vlog` (đã tạo, mục 9) |
| Outfit Nora tập 2 | ĐÃ DUYỆT (v7 clean: `4cba3314-40ad-4ed1-a90a-a7d63870308c` — đảo ngược chuẩn từ video MASTER-FIRE) |
| Sinh đầu tiên | MASTER-FIRE: clip khó nhất, gánh cả hook lẫn payoff |
| Project | `4cc4b500-6e3b-4379-96c3-dd18b7412c1a` (tạo 2026-10-05, `allow_voice: true`) · video HORIZONTAL `15076345-ca4a-48cb-8afa-4a79c2a52028` |
| Ref đã upload | Nora ← `ice_age.../refs/nora_main_clean.jpg` (`1454fb46-8510-4f14-99fe-8464720632b6`) · Nora Body ← `refs/nora_body_v7_clean.jpg`, không mặt (`4cba3314-40ad-4ed1-a90a-a7d63870308c`) |

---

## 2. Character Bible

### Nora (giữ từ tập 1)
- **CHARACTER_LOCK:** honey-blonde hair, grey-green eyes, fair skin with a natural pink flush. Build and clothing from the `Nora Body` sheet (Rule 46); video nhận `["Nora", "Nora Body", ...]`.
- **Câu khóa tóc (Bài học 55):** `hair pulled up into a high wavy ponytail tied at the crown of her head (not low at the nape), with wispy curtain bangs parted in the middle that cover the edges of her forehead and frame both cheeks, plus a few loose face-framing strands at the temples; her hair is never slicked back.`
- **Câu trước `0-3s`:** `Her curtain bangs stay over her forehead and her ponytail stays tied high at the crown for the entire clip; wind only makes the ponytail swing, it never pulls the hair back or loose.`
- **Voice:** Laomedeia, Slot 7. `voice_description`: upbeat, mid-high pitched, energetic, expressive conversational female voice; fast confident vlog delivery with dry humor; rises into real cracking screams in danger; drops to a fast whisper when hiding.
- **VOICE_LOCK:** dùng nguyên khối trong `voice-bible.md` §1. Nora là chuyên gia sinh tồn, không giảng lịch sử, câu ngắn, chửi thề bị cắt và bíp ở hậu kỳ.

### Nora Body tập 2: ĐÃ DUYỆT (2026-10-05). Ref v7 sạch logo = `refs/nora_body_v7_clean.jpg` (`4cba3314-40ad-4ed1-a90a-a7d63870308c`), tạo bằng `EDIT_CHARACTER_IMAGE` từ `Nora Body` (`uploads/nora_body_v3_clean.jpg`, `49a24c0f-bf32-4a2f-bbeb-6fed89ee98bb`). Đóng vai trò là bản **Nora Body + Outfit** hợp nhất: khóa chuẩn 100% vóc dáng hourglass (ngực đầy nhô cao, eo thon con kiến, hông cong, chân dài có thigh gap) lẫn trang phục ôm sát. Đảo ngược chính xác từ video `MASTER-FIRE`: loại bỏ mũ trùm/viền lông ở cổ và vai, giữ cổ V khoét sâu đan dây da mảnh, viền lông sói xám dày ở cổ tay áo, thắt lưng da nâu ôm sát eo nối liền quần legging da hươu bó sát.

**Ý tưởng:** đồ da **may khâu, vừa người**, kiểu người hiện đại thời kỳ băng hà. Nhóm Neanderthal chỉ khoác da sống buộc dây, không có đường may (research §5: không kim, không may). Vì vậy ở A1-05 Thủ Lĩnh véo **đường chỉ gân** trên vai áo cô: chi tiết lạ là **cách may**, không phải "vải hiện đại". Vẫn đúng luật "vlogger mặc đồ đúng thời kỳ từ clip đầu", và da ướt sũng vẫn không giữ được ấm.

```
OUTFIT (golden-tan): a form-fitting tailored tunic of smoked golden-tan deer suede,
visibly sewn with neat rows of fine sinew stitches along the shoulder, side and sleeve seams;
clean unadorned shoulders and completely open neck with NO fur collar or hood; a deep plunging
laced V-neckline closed with thin criss-crossing leather thongs; long sleek fitted suede sleeves ending
cleanly and neatly at the wrists with smooth stitched cuffs (strictly NO fur cuffs, NO fur at wrists,
NO fur trim anywhere on sleeves); a wide dark-brown leather belt at her waist; skin-tight golden-tan
hide leggings; knee-high hide boots wrapped with leather thongs.
COLOR LOCK: This outfit is GOLDEN-TAN throughout -- NOT dark brown, NOT a draped caveman pelt,
NOT white or cream, NOT sleeveless, NOT bare legs, NOT loose unkempt hair, NOT modern clothing.
```

- **Màu vàng nâu** để tách khỏi da nâu sẫm của nhóm (đọc được ở drone shot, Nora là "chấm vàng") và khác bộ trắng kem của tập 1.
- **Cổ, bờ vai và tay áo trơn thoáng gọn gàng**, loại bỏ hoàn toàn viền lông ở cổ tay giúp chuyển động thanh thoát, khoe trọn vóc dáng đồng hồ cát.
- **Trạng thái ướt** (A1-01 tới A2-07): `The suede is soaked from the chest down and darker where wet, with water dripping from the sleek sleeves, the belt and the hem; the colour stays golden-tan and the shape never changes.` Từ A2-08 trở đi bỏ câu này (đã hơ khô bên lửa).
- **Quy trình:** user duyệt mô tả → sinh mannequin 3-view (cần "yes") → user duyệt ảnh → mới viết tiếp.

### Nhóm Neanderthal (9 người; Đứa Bé đã bỏ khỏi kịch bản, user 2026-10-05)

**Câu đặc điểm chung** (dán vào mọi clip có họ):
`The Neanderthals are short, very stocky and barrel-chested, with heavy brow ridges, wide noses, receding chins, weathered skin and dark shaggy hair, wearing untailored hides draped and tied around their bodies with no sewn seams; they are real people, NOT apes, NOT costumes, NOT wax figures.`

| Nhân vật | Ref | Nhận diện | Giọng (chữ trong prompt) |
|---|---|---|---|
| **Leader** (Thủ Lĩnh) | có | Đàn ông ~35, vạm vỡ, gờ mày rất dày, da nâu sẫm, tóc đen bờm xờm ngang vai, da hươu sẫm | `a gravelly, low-pitched male voice — short guttural sounds, consonant-heavy, no recognizable words` |
| **Old Woman** (Người Già) | có | Nhỏ, hơi còng, tóc xám dài, mắt sáng; **một túi da nhỏ đeo ở hông** (đựng bột sẫm) | `a mature, mid-pitched female voice — slow guttural murmurs, no recognizable words` |
| **Strongest** (Người Mạnh Nhất) | có | Trẻ hơn, vai rộng nhất, mặt không biểu cảm | `a firm, mid-low-pitched male voice — clipped guttural sounds, no recognizable words` |
| **Strongest Spear** | có (EDIT từ ref Strongest) | Một cây giáo gỗ dài, mũi gỗ vót nhọn, đã hơ lửa, không mũi đá | — |
| A | không | Sẹo trắng ngang lông mày trái | không thoại |
| B | không | Tóc đen dài buộc sau gáy bằng dây da | không thoại |
| C | không | Râu rậm, mũi bè | không thoại |
| D | không | Tóc cắt sát | không thoại |
| E | không | Tấm da sói khoác một vai | không thoại |
| **Injured Hunter** (Người Bị Thương) | không | Râu lốm đốm xám, **chân trái quấn da**, vết thấm sẫm màu, nằm trên da thú cạnh lửa | không thoại |

### Ai có mặt ở đâu (khóa số người, §2c)
- **C03–Act 2:** 5 người ngoài trời (Leader, Old Woman, Strongest, A, B); Injured + C/D/E ở trong hang.
- **Act 3 (đi săn):** 7 Neanderthal + Nora: Leader, Strongest, A–E. → `Exactly seven Neanderthals and Nora are present`.
- **Act 3 #15 – Act 4 #2 (trong hang):** 9 Neanderthal + Nora.
- **Act 4 đêm:** 7 + Nora (Leader, Strongest, A–E). Old Woman, Injured ở lại.

### Sinh vật & đạo cụ có ref

| Ref | Vì sao cần | Câu khóa |
|---|---|---|
| **Cave Hyena** | Xuất hiện ở master + 6 clip Act 4; loài tuyệt chủng | `Each hyena is a large cave hyena with a heavy, thick-necked body, a back that slopes down from high shoulders to lower hips, round ears, a broad blunt muzzle and a pale sandy coat with dark spots; they are hyenas, NOT wolves, NOT dogs, NOT big cats. Each hyena is a separate animal; they never merge or overlap.` |
| **Ember Bundle** | Gieo ở A2-11, gặt ở A4-05/09, A5-03 | Khóa bọc than mới (mục 3) |
| **Pech Valley** (landscape) | EST-01/02/03, cảnh thung lũng | Thung lũng hẹp, vách đá vôi vàng nhạt, suối nông viền băng, cửa hang hình đường hầm cao ~50 m bên vách phải |
| **Cave Mouth** (scene) | Act 1 #6 trở đi, Act 2, Act 5 | Cửa hang rộng thấp, bếp lửa lõm có vòng đá bên trong |

Mỗi clip tối đa 7 ref. Nora + Nora Body chiếm 2 chỗ trong **mọi** clip có Nora, kể cả POV (Rule 46 / bài học 60). `Nora Body` chỉ là ảnh nguồn để EDIT outfit, không gửi vào video.

---

## 3. Khóa vật lý (dán nguyên văn)

| Quy trình | Câu khóa |
|---|---|
| **Tạo lửa (đã sửa hướng đánh)** | `She strikes the pyrite in a fast glancing stroke down along the flat face of the flint biface, lengthwise. Only a few tiny, short-lived orange sparks jump from the point of contact and fall onto the dry moss. The moss first shows one small red glowing spot and a thin wisp of smoke; she lowers her face close and blows gently; only after several seconds does a small flame appear. There is no shower of sparks and no instant flame.` |
| Đá | `exactly one grey flint biface, an oval stone flaked on both faces with no handle` · `exactly one brassy gold lump of pyrite`. Không có kim loại ở bất kỳ đâu |
| Bột | `a pinch of dark mineral powder` (không viết "black powder") |
| **Bọc than (nâng cấp)** | `A small roll of birch bark, lined inside with fresh green leaves, holds one glowing ember resting on a piece of dry hoof fungus and moss, with an opening at one end for air. The bark does not burn; only faint warmth and a thin thread of smoke rise from it.` |
| Than chết | `Inside, the ember is black and crushed flat; no glow, no smoke.` |
| Ánh sáng | Theo giờ: `pale grey dawn light` → `flat overcast winter daylight` → `long shadows, low winter sunlight, daylight fading fast` → `dusk` → `moonlight`. Không tả vị trí mặt trời |
| Bếp trong hang | `an open fire in a shallow sunken hearth ringed with stones in the earth floor; no fireplace, no chimney, no brick or built wall, no grate, no metal objects.` |
| Hơi thở | `dense short-lived breath vapor that dissipates rapidly` |

---

## 4. Research mới đưa vào v5 (chi tiết + link ở research §13)

| # | Phát hiện | Đổi gì trong kịch bản |
|---|---|---|
| 1 | Vết đập trên biface nằm ở **mặt phẳng**, chạy dọc trục dài (Sorensen 2018) | Sửa khóa tạo lửa ở mọi clip + Bài học 57 |
| 2 | Tia pyrite yếu, không bắt được mồi thường | Nora hỏng với rêu trần là đúng vật lý. **Gieo** ở A2-01: Người Già rắc một nhúm từ túi da rất nhanh, không ai để ý; A2-06 mới lộ ra |
| 3 | 37/40 nhóm săn hái mang lửa theo, không nhóm mới (McCauley 2020); nấm móng ngựa giữ than 8–12 giờ; bọc vỏ bạch dương lót lá tươi (Ötzi) | Bọc than nâng cấp; lý do nhóm canh giữ nó; "the fire held" ở H20 hợp lý |
| 4 | Hạ thân nhiệt nhẹ = "umbles": vụng tay, môi tím; da/quần áo ướt mất nhiệt rất nhanh | A1-02: *"Wet clothes kill faster than cold."* · A2-04: *"Can't feel my fingers. That's stage one."* |
| 5 | Hươu cái thấy nguy: ngẩng đầu, **dậm chân, sủa một tiếng gắt**, cả đàn chạy | A3-04 có đủ chuỗi này; người xem nghe được khoảnh khắc lỗi |
| 6 | Neanderthal săn bằng **giáo đâm tầm gần, từ dưới lên** (Neumark-Nord, 2018) | A3-05: Người Mạnh Nhất nhào ra đâm, không phóng giáo |
| 7 | Linh cẩu ngửi xác ~4 km xuôi gió; dựng lông lưng khi dọa; "cười" = căng thẳng/phục tùng | A3-12: cỏ ngả về phía đông, Thủ Lĩnh ngửi gió; A4-08 lông gáy dựng; A4-14 tiếng "cười" lúc lùi |
| 8 | Linh cẩu đốm giấu xác **dưới nước**, không dưới đá | Đống đá là của **người**; linh cẩu chỉ bới. Không để Nora nói "hyenas bury meat" |

---

## 5. Storyboard toàn tập

**Ký hiệu máy:** SEL = selfie (tay phải cầm), OTS = selfie qua vai (Nora 1/3, chủ thể 2/3), POV = mắt Nora (tay ngoài khung trừ khi ghi rõ), FIX = máy đặt cố định (hai tay rảnh), DR = drone.
**Ref:** `N2` = Nora, Nora Body (Rule 46: ảnh mặt + body đã mặc outfit; KHÔNG gửi Nora Body vào video).

### COLD OPEN | 0:00–0:14

| ID | s | Máy | Hình | Thoại Nora | Ref |
|---|---|---|---|---|---|
| MASTER-FIRE | 10 | FIX | Đêm trăng, bên đống đá bị bới. Nora quỳ, bọc than chết mở bên trái, ba linh cẩu trong bóng tối phía sau. 0–2 một con nhích lên, lông gáy dựng; 2–4 nhát 1 trượt; 4–6 nhát 2: vài tia, tắt trong không khí; 6–8 nhát 3: tia rơi vào rêu → chấm đỏ, khói; 8–10 thổi → lửa nhỏ | 0–2 *"Three. Getting closer."* · 4–6 *"Come on—"* | N2, Cave Hyena |
| C01 = MASTER 0–8s | | | **CUT ĐEN ở 8.0s** (chấm đỏ, chưa thấy lửa) | | |
| EST-01 | 6 | DR | Bình minh, sương trên suối, sợi khói mảnh từ cửa hang, Nora là chấm vàng bên bờ. Hậu kỳ: `51,000 YEARS AGO` | — | N2, Pech Valley |

### ACT 1 "COLD" | H0–H1 | 0:14–1:34

| ID | s | Máy | Hình | Thoại Nora | Ref |
|---|---|---|---|---|---|
| A1-01 | 8 | SEL | **HOUR 0.** Bờ đất đóng băng sụp, Nora trượt xuống suối, nước tới ngực. Tay trái túm rễ cây, leo lên, quỳ run | 6–8 *"Ten seconds in. Soaked."* | N2 |
| A1-02 | 8 | FIX | Hai tay cố vắt ống tay áo, ngón tay cứng, trượt. Nhét tay vào nách. Chạm cành bạch dương đổ: đóng băng, ướt | 3–6 *"Wet clothes kill faster than cold."* | N2 |
| A1-03 | 8 | OTS | Cành gãy. Nora ngoái lại. Năm Neanderthal (đã đứng sẵn trong bóng cây) bước ra, dừng cách ~6 m | 6–8 (thì thầm) *"Don't run."* + 1s im lặng | N2, Leader, Old Woman, Strongest, Strongest Spear |
| A1-04 | 8 | OTS | Thủ Lĩnh tới cách 1,5 m, ngửi không khí hai lần, nói vài âm tiết cụt | 5–8 *"No idea what he said. But that wasn't a question."* | N2, Leader, Strongest, Old Woman, Strongest Spear |
| A1-05 | 8 | SEL | Tay Thủ Lĩnh véo vai áo trái ướt của cô, miết **đường chỉ gân** giữa ngón cái và ngón trỏ, nhìn tấm da khoác của chính ông, nhìn lại đường may; nước nhỏ lên tay ông; ông nhìn hàm cô run | 6–8 *"Yeah. Stitches. Still freezing."* | N2, Leader |
| A1-06 | 8 | SEL | Đi sau nhóm lên dốc tới cửa hang có ánh lửa. Người Mạnh Nhất (đứng sẵn cạnh cửa) bước ngang chắn, giáo ngang người, hất cằm về phía rừng | 6–8 *"Okay. Outside. Got it."* | N2, Strongest, Strongest Spear, Leader, Cave Mouth |
| A1-07 | 8 | POV | Nhìn xuống: hàng dấu chân linh cẩu trên sương giá ở cửa hang → ngẩng lên: Người Bị Thương nằm cạnh lửa, chân trái quấn da thấm sẫm; Người Già đắp rêu lên vết thương | 6–8 (giọng thấp) *"Something bit him. Something that comes at night."* | N2, Old Woman, Cave Mouth |
| A1-08 | 8 | OTS | Thủ Lĩnh đánh **một nhát** pyrite: vài tia nhỏ. Thả hai viên đá xuống chân cô. Chỉ lần lượt: đá → lửa trong hang → Nora → rừng tối. Hậu kỳ: `MISSION: MAKE FIRE BEFORE NIGHTFALL` | 6–8 *"My own fire. Or I sleep out there."* | N2, Leader, Strongest, Cave Mouth |
| A1-09 | 8 | FIX | Cô **cạo chậm** mép đá xuống pyrite như cạo que thép: một tia mờ chết trên đất trần (chưa có mồi). Phía sau, bốn người quay vào hang | 0–3 *"Like a ferro rod. Right?"* | N2, Leader, Strongest, Cave Mouth |
| A1-10 | 8 | OTS | Người Già đi ra, ngồi xổm, đặt **đúng 4 nhúm rêu khô** thành hàng trên miếng vỏ cây, đứng dậy đi vào, không nói | 6–8 *"Okay."* + im lặng | N2, Old Woman, Cave Mouth |

### ACT 2 "FIRE" | H1–H3 | 1:34–3:02

| ID | s | Máy | Hình | Thoại Nora | Ref |
|---|---|---|---|---|---|
| A2-01 | 8 | OTS | Người Già ngồi xuống cạnh cô, làm mẫu bằng rêu **của bà**. **Gieo:** 0–1s bà nhón từ túi da ở hông một nhúm rắc lên rêu, rất nhanh, không nhìn Nora. Ba nhát dọc mặt đá → chấm đỏ → thổi → lửa → **bà dập tắt bằng đất** (để cô phải tự làm) | 6–8 *"Three strikes. She does it in three."* | N2, Old Woman, Cave Mouth |
| A2-02 | 8 | FIX | Hỏng 1: tay run, pyrite trượt khỏi mặt đá, gạt văng một nhúm rêu xuống sương → ướt, bỏ. **4 → 3** | 6–8 *"No— okay. Three left."* | N2, Cave Mouth |
| A2-03 | 8 | FIX | Hỏng 2: chấm đỏ, cô thổi **quá mạnh**, nhúm rêu tung ra. Người Mạnh Nhất, A, B đứng xem, khoanh tay. **3 → 2** | 6–8 *"Too hard. Two left."* | N2, Strongest, Strongest Spear, Cave Mouth |
| A2-04 | 8 | SEL | Cận: môi tím, run dữ, nhìn bàn tay trái cứng đờ, cố gập ngón | 3–6 *"Can't feel my fingers. That's stage one."* | N2 |
| A2-05 | 8 | FIX | Hỏng 3: cô khom người che gió, đánh; một cơn gió từ thung lũng nhấc **cả hai nhúm cuối** khỏi miếng vỏ, thổi xuống dốc. Người Mạnh Nhất quay vào hang. **2 → 0** | 3–6 *"No no no—"* | N2, Strongest, Cave Mouth |
| A2-06 | 8 | OTS | Người Già quay lại. Đặt một nhúm rêu của bà. **Lần này chậm:** mở túi da, giơ nhúm bột sẫm cho Nora thấy, rắc lên rêu, gõ ngón tay đúng chỗ đó. Đặt pyrite vào tay cô, để túi da và **một bó que khô** (lấy từ trong hang) lại bên cạnh | 6–8 *"Something dark. Right where the spark lands."* | N2, Old Woman, Cave Mouth |
| A2-07 | 8 | FIX | Rêu đã rắc bột; nhát 1 trượt, nhát 2 → chấm đỏ, khói → cúi thổi → lửa → mồi ba que khô → **ngọn lửa nhỏ của riêng cô** (khóa tạo lửa) | 0–3 *"Come on… come on."* | N2, Cave Mouth |
| A2-08 | 8 | SEL | Hơ tay trái trên lửa nhỏ, run rẩy, gần khóc. Hơi nước bốc khỏi ống tay áo | *(không thoại)* | N2, Cave Mouth |
| A2-09 | 8 | OTS | Thủ Lĩnh đứng ở cửa hang nhìn ngọn lửa của cô, bước sang bên, hất đầu vào trong | *(không thoại)* | N2, Leader, Cave Mouth |
| A2-10 | 8 | POV | Trong hang (khóa bếp): giá phơi bằng cây sào **trống trơn**; C (râu rậm, mũi bè) gặm khúc xương đã sạch | 3–8 *"No meat. I haven't eaten since I got here."* | N2, Cave Mouth |
| A2-11 | 8 | OTS | Người Già gắp một hòn than bằng hai que, đặt lên miếng nấm + rêu trong cuộn vỏ bạch dương lót lá tươi, cuộn lại, đưa Thủ Lĩnh, ấn tay ông mở lỏng ra | 6–8 *"Fire travels with them. Don't crush it."* | N2, Old Woman, Leader, Ember Bundle, Cave Mouth |

### ACT 3 "THE HUNT" | H3–H8 | 3:02–5:06

| ID | s | Máy | Hình | Thoại Nora | Ref |
|---|---|---|---|---|---|
| A3-01 | 8 | OTS | **HOUR 3.** Thủ Lĩnh chỉ Người Bị Thương, rồi chỉ Nora. Người Mạnh Nhất nhìn cô, không biểu cảm | 6–8 *"He can't walk. So I'm the hunter now."* | N2, Leader, Strongest, Cave Mouth |
| EST-02 | 4 | DR | Hàng tám bóng người (7 + Nora, chấm vàng ở cuối hàng) đi xuống thung lũng phủ sương giá | — | N2, Pech Valley |
| A3-02 | 8 | SEL | Cỏ cao phủ sương gần lối hươu qua suối. Thủ Lĩnh ấn vai cô xuống sau tảng đá, xòe bàn tay úp xuống: chờ | 6–8 (thì thầm) *"Wait for his hand. Then I drive them."* | N2, Leader |
| A3-03 | 8 | POV | Ngó qua tảng đá phủ sương: đàn hươu đỏ gặm cỏ cách ~30 m. **Im lặng 2s**, tiếng gặm cỏ | *(không thoại)* | N2 |
| A3-04 | 8 | OTS | **Lỗi của Nora:** cô nhích người để nhìn rõ, ủng trượt trên đá phủ sương, sỏi lăn lách cách. Một con cái ngẩng đầu, **dậm chân, sủa một tiếng gắt**; cả đàn chạy **sớm**, sai hướng | 6–8 *"Sh—"* (bíp) | N2 |
| A3-05 | 8 | POV | Đàn lao qua chỗ nấp của Người Mạnh Nhất quá sớm; anh nhào ra **đâm giáo từ dưới lên** vào sườn một con; nó giằng ra, chạy vào rừng. Anh quay lại nhìn thẳng vào cô | 6–8 *"That was me. That was all me."* | N2, Strongest, Strongest Spear |
| A3-06 | 8 | SEL | Vệt máu đỏ trên sương trắng kéo qua thung lũng. Nhóm lần theo phía trước, không ai quay lại nhìn cô | *(chỉ tiếng thở)* | N2, Leader, Strongest |
| A3-07 | 8 | SEL | Đi lần dấu, bóng cây dài dần, nắng đông thấp, ngày tắt nhanh | 3–6 *"Every hour we track, we lose light."* | N2 |
| A3-08 | 8 | OTS | Người Mạnh Nhất lùi lại đi cạnh cô, dừng, chỉ một giọt máu trên lá cô vừa bước qua, không nhìn cô, đi tiếp | 6–8 *"…Thanks, boss."* | N2, Strongest, Strongest Spear |
| A3-09 | 8 | POV | Con hươu nằm chết trong bụi rậm, Thủ Lĩnh ngồi xổm bên cạnh. Ánh sáng tắt nhanh | 6–8 (thở ra) *"Found it."* | N2, Leader |
| A3-10 | 8 | FIX | Thủ Lĩnh đưa mảnh đá cắt, chỉ một đùi, chỉ phía ánh sáng đang tắt (**mini-goal**). Cô cắt vụng; Người Mạnh Nhất nắn lại cổ tay cô một lần | 6–8 *"Better. Not good. But better."* | N2, Leader, Strongest |
| A3-11 | 8 | OTS | C và D lăn đá đè lên phần lớn con hươu (**kho thịt**). Người Mạnh Nhất buộc gói thịt trong da, ném cho cô | 6–8 *"Oof—"* | N2, Strongest |
| A3-12 | 8 | OTS | Tiếng whoop xa. Thủ Lĩnh xoay về phía đông, ngửi gió; cỏ ngả về hướng đó. Nora đứng sững | *(im lặng)* | N2, Leader, Strongest |
| A3-13 | 8 | SEL | Chạy lên dốc, gói thịt trên vai trái, khung nảy theo từng bước | 3–6 *"Heavy. Uphill. Nobody's slowing down."* | N2, Strongest |
| A3-14 | 8 | POV | Ngoái lại từ lưng dốc: vệt máu đỏ trên sương chạy dài từ suối tới đống đá | 3–8 *"The blood. It goes right to the meat."* | N2, Pech Valley |
| A3-15 | 8 | OTS | **HOUR 8.** Chạng vạng, trong hang. Thịt sống vừa xiên lên bếp; Nora ngồi giữa nhóm, thở ra | 3–8 *"Fire. Food. Inside. We made it."* (**FALSE VICTORY**) | N2, Leader, Old Woman, Strongest, Cave Mouth |

### ACT 4 "HYENAS" | H8–H11 | 5:06–7:06

| ID | s | Máy | Hình | Thoại Nora | Ref |
|---|---|---|---|---|---|
| A4-01 | 8 | OTS | Thịt chưa chín. Tiếng whoop từ phía kho. Thủ Lĩnh đứng dậy ra cửa hang. Người Già nhấc thịt khỏi lửa, gói vào da, cất. Bụng Nora sôi | 6–8 *"…Or not."* | N2, Leader, Old Woman, Cave Mouth |
| A4-02 | 8 | SEL | Nora nhìn gói thịt đã cất, rồi nhìn chín người quanh bếp | 2–8 *"That's two days of food. The rest is down there. I led them to it."* | N2, Leader, Old Woman, Strongest, Cave Mouth |
| EST-03 | 4 | DR | Đêm: hang là đốm sáng duy nhất giữa thung lũng đen | — | N2, Pech Valley |
| A4-04 | 8 | OTS | **HOUR 10.** Thủ Lĩnh nói một câu; sáu người đứng dậy cầm giáo và đuốc chưa đốt. **Nora đứng dậy trước**, nhận bọc than từ tay Người Già. Người Mạnh Nhất chắn; Thủ Lĩnh gật đầu; anh lùi sang bên | 6–8 *"My trail. My job."* | N2, Leader, Strongest, Old Woman, Ember Bundle, Cave Mouth |
| A4-05 | 8 | SEL | Đi đêm dưới trăng, đuốc không đốt. 5–8s cô vấp rễ cây, ngã sấp đè lên bọc than | 0–4 *"Torches stay dark. They'd see us coming."* · 7–8 *"—fine."* | N2, Strongest, Ember Bundle |
| A4-06 | 8 | POV | Kho thịt dưới trăng, đá đã bị bới lệch. Tiếng kêu 1/2/3 từ ba hướng, mỗi tiếng một người quay đầu | *(im lặng)* | N2, Leader, Strongest |
| A4-07 | 8 | SEL | Thì thầm, mắt đảo theo từng hướng | 3–8 *"Three calls. Three places. Three of them."* | N2 |
| A4-08 | 8 | POV | Ba linh cẩu đang đào đống đá, cách ~25 m, lông lưng và gáy dựng | *(im lặng, tiếng gầm gừ)* | N2, Cave Hyena |
| A4-09 | 8 | OTS | Thủ Lĩnh gật về phía bọc than. Nora mở ra: than đen, nát (khóa than chết) | 6–8 *"It's dead. I crushed it."* | N2, Leader, Ember Bundle |
| A4-10 | 8 | FIX | Quỳ xuống, lấy rêu và bột từ túi da của Người Già, đặt lên vỏ cây. Nhát 1: pyrite trượt, không tia (**khớp nhát 1 của master**) | 6–8 *"Not now. Not now."* | N2, Cave Hyena |
| A4-11 | 8 | OTS | Một linh cẩu tiến một bước về phía họ. Nhát 2: vài tia tắt trong không khí (**khớp nhát 2 của master**) | 6–8 *"Come on—"* | N2, Strongest, Strongest Spear, Cave Hyena |
| A4-12 | 8 | OTS | Người Mạnh Nhất chĩa giáo về phía linh cẩu, không tiến, liếc lại chờ cô. Cô nhìn xuống tay (**khớp tư thế giây 6 của master**, Rule 44) | 3–6 *"They're waiting for me."* | N2, Strongest, Strongest Spear, Cave Hyena |
| PAYOFF = MASTER 6–10s | 4 | FIX | Nhát 3 → chấm đỏ → thổi → **lửa bắt** | — | (dùng lại master) |
| A4-14 | 8 | OTS | Cô châm đuốc đầu tiên, lửa chuyền tay. Bảy người giơ đuốc, đội hình sát, tiến chậm, gằn giọng thấp. Linh cẩu "cười" khúc khích, lùi về phía đống ruột | *(im lặng)* | N2, Leader, Strongest, Strongest Spear, Cave Hyena |
| A4-15 | 8 | OTS | Lăn đá, nhấc thịt; linh cẩu lấy phần thừa. Người Mạnh Nhất **trao đuốc cho Nora** để cô dẫn đường về | 6–8 *"Not me. Eight people."* | N2, Strongest, Leader |
| A4-16 | 8 | SEL | Đi về dưới trăng, đuốc trong tay trái. Thủ Lĩnh lùi lại, đi ngang hàng cô, không nhìn cô | *(không thoại)* | N2, Leader |

### ACT 5 "AFTER" | H12–H24 | 7:06–7:54

| ID | s | Máy | Hình | Thoại Nora | Ref |
|---|---|---|---|---|---|
| A5-01 | 8 | OTS | **HOUR 12.** Người Mạnh Nhất xé miếng thịt nướng đầu tiên, đưa cho Nora. Cô ăn | 6–8 *"First food in twelve hours."* | N2, Strongest, Cave Mouth |
| A5-02 | 8 | OTS | Thủ Lĩnh nói một câu qua đống lửa, nhìn cô | 5–8 *"No idea what he said. But that wasn't a question."* (mirror) | N2, Leader, Cave Mouth |
| A5-03 | 8 | POV | **HOUR 20.** Sao qua cửa hang → nhìn xuống bọc than mới trong hai tay cô (thấy tay áo) | 0–3 *"Fifty thousand years."* … 6–8 *"And the fire held."* | N2, Ember Bundle, Cave Mouth |
| A5-04 | 8 | SEL | **HOUR 24.** Bình minh ngoài cửa hang, cả nhóm đang thức dậy. Cô đặt pyrite và biface của Thủ Lĩnh lên tảng đá cạnh ông | 3–8 *"Everyone's alive. Time to go."* | N2, Leader, Cave Mouth |
| ~~A5-05~~ | — | — | **Đã bỏ** (user duyệt 2026-10-05): tiếng chân chạy theo chuyển vào 0–2s của A5-06 | — | — |
| A5-06 | 8 | OTS | Cô đã đi vài bước xuống lối mòn, cửa hang phía sau. 0–2s tiếng chân chậm trên sương, cô ngoái lại: Người Già (thấy từ giây 0, đứng trên lối mòn ~3 m phía sau) bước chậm xuống tới. Bà đặt **cục pyrite nhỏ của chính bà** vào tay trái cô, gập ngón tay cô lại, rồi chậm rãi đi về hang | *(không thoại)* | N2, Old Woman, Cave Mouth |
| A5-07 | 8 | SEL | Cô nhìn pyrite, nhìn hang. **CUT ĐEN** | *(không thoại)* | N2, Cave Mouth |

---

## 6. Bảng vật lý từng clip (5b): CẦN USER DUYỆT trước khi viết prompt Act 2–5

| # | Máy đặt ở đâu, nhìn về đâu | Có gì trong khung ở giây 0 | Vật di chuyển: hướng + tốc độ + hệ quả | Chuyển động vật lý thật | Ai/cái gì rời khung, bằng cách nào |
|---|---|---|---|---|---|
| MASTER | Trên phiến đá phẳng sát đất, 1 m trước Nora, ngang gối, góc 3/4 | Nora quỳ; vỏ cây + rêu rắc bột trước gối; bọc than chết mở bên trái; biface tay trái, pyrite tay phải; 3 linh cẩu cách 8–12 m (trái/giữa/phải) | Linh cẩu giữa nhích **một bước** chậm; tia lửa rơi từ điểm chạm xuống rêu; khói bốc thẳng (đêm lặng gió) | Pyrite trượt khỏi mặt đá ở nhát 1 (vai giật); khói mảnh; lửa nhỏ liếm lên, hắt sáng cam từ dưới lên mặt cô | Không ai rời khung; linh cẩu không bao giờ băng qua trước mặt cô |
| EST-01 | Drone cao, lướt chậm tới trước và hơi xuống | Thung lũng, suối có băng, sương, cửa hang vách phải có sợi khói, Nora là chấm vàng bên trái suối | Sương trôi chậm dọc suối; khói nghiêng theo gió nhẹ | Lắc nhẹ theo gió, không xoay | Không ai |
| A1-01 | Selfie, tay phải duỗi giơ cao trên mặt nước | Nora đứng mép bờ đóng băng; rễ cây lòi ra ở mép trái | Bờ sụp → cô trượt lùi xuống nước (nhanh), nước dâng tới ngực, bắn lên khung | Khung giật mạnh xuống và nghiêng theo cơ thể; nước chảy khỏi tay áo; ủng trượt trên bùn | Không ai; tay phải luôn giữ trên mặt nước |
| A1-02 | Đặt trên tảng đá bờ suối, cách 1,5 m, ngang ngực | Nora quỳ trên cỏ phủ sương; cây bạch dương đổ đóng băng phía sau | Nước nhỏ vài giọt khi vắt; tay nhét vào nách rồi rút ra | Ngón cứng trượt khỏi da ướt; run toàn thân; hơi thở thành khói tan nhanh | Không ai |
| A1-03 | Selfie OTS, Nora 1/3 trái tiền cảnh | 5 Neanderthal đứng sẵn trong bóng cây, cách ~15 m, nửa khuất sau thân cây | Cành gãy dưới chân một người; cả năm đi bộ chậm tới trước, dừng ở ~6 m | Nora quay đầu qua vai trái rồi quay lại; khung rung nhẹ theo nhịp thở | Không ai; không người nào mọc thêm hay biến mất |
| A1-04 | Selfie OTS | Thủ Lĩnh cách ~3 m bên phải; 4 người còn lại cách ~6 m | Thủ Lĩnh bước tới 1,5 m, nghiêng người ngửi | Cánh mũi phập phồng; Nora đứng im, chỉ mắt di chuyển | Không ai |
| A1-05 | Selfie cận, ngang vai | Thủ Lĩnh sát bên trái cô, tay phải ông đã ở cạnh vai áo cô | Ngón tay ông véo, miết đường chỉ; nước nhỏ xuống ngón ông | Da ướt lõm dưới ngón tay; ông rụt tay khi bị lạnh | Tay ông rời khung khi buông ra |
| A1-06 | Selfie, đi bộ lên dốc | Nhóm đi trước 3–5 m; Người Mạnh Nhất đứng sẵn cạnh cửa hang; ánh lửa trong hang | Nhóm đi vào hang (đi bộ); Người Mạnh Nhất bước ngang một bước chắn cửa | Khung nảy nhẹ theo bước lên dốc; dừng đột ngột khi bị chắn | Các người khác đi vào bóng tối trong hang (đi bộ) |
| A1-07 | POV đứng ngoài cửa hang, nhìn xuống rồi ngẩng lên | Dấu chân linh cẩu trên sương ở tiền cảnh; Người Bị Thương nằm cạnh bếp cách 4 m; Người Già quỳ cạnh anh | Ánh nhìn nghiêng xuống rồi lên chậm như mắt người | Người Bị Thương nhăn mặt, cựa người; lửa lay động | Không ai; tay Nora ngoài khung |
| A1-08 | Selfie OTS | Thủ Lĩnh cách 1,5 m, tay trái biface, tay phải pyrite; Người Mạnh Nhất ở cửa hang phía sau | Vài tia rơi xuống đất; hai viên đá rơi xuống sương ngay chân cô | Đá rơi nảy nhẹ một lần, nằm im; tay ông chỉ theo thứ tự | Không ai |
| A1-09 | Đặt trên tảng đá thấp dưới dốc, nhìn lên Nora, cửa hang phía sau | Nora quỳ, hai tay cầm hai viên đá; Thủ Lĩnh, Người Mạnh Nhất, A, B đứng ở cửa hang | Một tia mờ rơi xuống đất trần, tắt ngay | Cạo chậm, áp lực đều (sai kỹ thuật) | Bốn người lần lượt đi bộ vào trong hang |
| A1-10 | Selfie OTS | Nora ngồi; Người Già đứng sẵn ngay trong cửa hang, tay chụm 4 nhúm rêu | Bà đi ra (đi chậm), ngồi xổm, đặt từng nhúm một, đứng dậy đi vào | Rêu đặt xuống không nảy; bà chống gối đứng dậy chậm | Bà đi bộ vào bóng tối trong hang |
| A2-01 | Selfie OTS | Người Già ngồi bên phải cô, rêu của bà trên vỏ cây, túi da ở hông | Nhúm bột rắc xuống (1s, nhanh); tia rơi vào rêu; khói bốc; bà dập lửa bằng một nắm đất đóng băng | Theo khóa tạo lửa | Không ai; 4 nhúm của Nora giữ nguyên |
| A2-02 | Đặt trên đá, 1 m, ngang gối | 4 nhúm rêu trên vỏ cây; hai viên đá trong tay cô | Pyrite trượt, gạt một nhúm văng xuống sương (bay ngắn ~30 cm) | Tay run rõ; nhúm rêu thấm ướt, sẫm màu | Không ai; còn 3 nhúm trên vỏ |
| A2-03 | Như A2-02 | 3 nhúm; Người Mạnh Nhất, A, B đứng ở cửa hang phía sau | Cô thổi quá mạnh → rêu tung tơi xuống đất | Chấm đỏ tắt ngay khi rêu tung ra | Không ai; còn 2 nhúm |
| A2-04 | Selfie cận | Mặt Nora, tay trái giơ ngang ngực | Ngón tay gập chậm, không gập hết | Run hàm, môi tím, hơi thở khói | Không ai |
| A2-05 | Như A2-02 | 2 nhúm; Người Mạnh Nhất ở cửa hang | Gió từ thung lũng nhấc cả hai nhúm, bay xuống dốc (nhanh) | Tóc đuôi ngựa đung đưa theo gió; cô khom người che nhưng muộn | Hai nhúm rêu bay ra mép khung; Người Mạnh Nhất đi bộ vào hang |
| A2-06 | Selfie OTS | Người Già quỳ bên phải, tay cầm rêu, bó que khô kẹp nách, túi da ở hông | Bà giơ nhúm bột lên chậm, rắc, gõ ngón tay; đặt pyrite vào tay trái cô | Bột rơi thành lớp mỏng, không bay | Bà đi bộ vào hang; túi da và bó que nằm lại cạnh cô |
| A2-07 | Như A2-02 | Rêu của bà rắc bột trên vỏ cây; bó que khô và túi da bên cạnh; hai viên đá trong tay | Theo khóa tạo lửa; mồi 3 que, lửa nhỏ cháy trên vỏ cây | Cô cúi sát thổi nhiều lần; ngón tay run khi đặt que | Không ai |
| A2-08 | Selfie cận | Lửa nhỏ trước mặt, tay trái hơ trên lửa | Hơi nước bốc khỏi ống tay áo | Run giảm dần; lửa lay | Không ai |
| A2-09 | Selfie OTS | Thủ Lĩnh đứng giữa cửa hang | Ông bước ngang một bước, hất đầu | Chậm, nặng | Không ai |
| A2-10 | POV đứng trong hang | Bếp lõm cháy; giá sào trống; C ngồi gặm xương cách 2 m | C gặm, xoay xương | Ánh lửa lay trên vách đá | Không ai |
| A2-11 | Selfie OTS trong hang | Người Già ngồi bên bếp, cuộn vỏ bạch dương mở sẵn trên đùi; Thủ Lĩnh ngồi bên cạnh | Than được gắp chậm bằng hai que, đặt vào; cuộn lại; chuyền tay | Than đỏ sáng, khói mảnh; vỏ không bén | Không ai |
| A3-01 | Selfie OTS ở cửa hang | Người Bị Thương nằm cạnh bếp; Thủ Lĩnh và Người Mạnh Nhất đứng | Tay Thủ Lĩnh chỉ người bị thương rồi chỉ cô | — | Không ai |
| EST-02 | Drone cao, lướt theo hàng người | Hàng 8 bóng đi xuống thung lũng | Đi bộ chậm từ phải sang trái | Lắc nhẹ theo gió | Không ai |
| A3-02 | Selfie thấp, sau tảng đá | Cỏ cao phủ sương; Thủ Lĩnh ngồi xổm bên cạnh | Tay ông ấn vai cô xuống; bàn tay úp xuống giữ yên | Cỏ rung khẽ | Thủ Lĩnh bò ra mép phải khung |
| A3-03 | POV ngó qua mép đá | Mép đá phủ sương ở tiền cảnh; ~12 hươu đỏ gặm cỏ cách 30 m bên suối | Hươu gặm cỏ, nhích chậm | Hơi thở hươu thành khói | Không ai |
| A3-04 | Selfie OTS sau đá | Nora sau đá 1/3 trái; đàn hươu 2/3 phía sau | Sỏi lăn xuống dốc (lách cách); con cái dậm chân; đàn bỏ chạy sang trái (nhanh) | Ủng trượt, người chúi xuống, khung giật | Cả đàn chạy ra mép trái khung |
| A3-05 | POV từ chỗ nấp | Người Mạnh Nhất nấp trong cỏ cách 10 m, giáo trong tay; đàn đang lao tới từ phải | Hươu lao qua (nhanh); anh nhào ra đâm từ dưới lên; con hươu giằng ra, mũi giáo dính máu | Cỏ đổ rạp; đất văng dưới móng | Con hươu chạy vào rừng ở mép trái |
| A3-06 | Selfie, đi bộ | Vệt máu trên sương phía trước; nhóm đi trước 5–10 m | Nhóm đi bộ đều | Khung nảy nhẹ theo bước | Không ai |
| A3-07 | Selfie, đi bộ | Cây trơ trụi, bóng dài trên sương | Đi bộ; bóng kéo dài | Nắng thấp hắt một bên mặt cô | Không ai |
| A3-08 | Selfie OTS, đi bộ | Người Mạnh Nhất đi bên phải cô, giáo tay phải | Anh dừng, chỉ xuống giọt máu trên lá bằng tay trái, rồi đi tiếp (đi bộ) | Lá rung khi bị chạm | Anh đi ra trước, vẫn trong khung |
| A3-09 | POV, bước vào bụi rậm | Con hươu chết nằm nghiêng trong bụi; Thủ Lĩnh ngồi xổm cạnh | Ánh nhìn tiến chậm tới | Hơi thở khói; cành rậm rung khi gạt qua | Không ai; tay Nora ngoài khung |
| A3-10 | Đặt trên khúc gỗ, 1 m, ngang ngực | Nora quỳ cạnh con hươu, mảnh đá cắt tay phải; Thủ Lĩnh bên trái, Người Mạnh Nhất bên phải | Tay cô cắt; tay Người Mạnh Nhất nắn cổ tay cô một lần | Da hươu kéo căng khi cắt | Không ai |
| A3-11 | Selfie OTS | C và D bên con hươu với các tảng đá; Người Mạnh Nhất cầm gói thịt | Đá lăn chậm (hai người đẩy); gói thịt ném vào ngực cô | Cô lảo đảo lùi một bước khi đỡ gói | Không ai |
| A3-12 | Selfie OTS | Thủ Lĩnh đứng giữa cỏ, nhìn về phía nam | Ông xoay người về phía đông; cỏ ngả về phía đông | Gió lùa tóc đuôi ngựa của cô đung đưa | Không ai |
| A3-13 | Selfie, chạy lên dốc | Người Mạnh Nhất chạy trước 3 m; gói thịt trên vai trái cô | Chạy lên dốc | Khung nảy dọc theo từng bước, hơi trễ khi rẽ, nhòe chuyển động thật | Không ai |
| A3-14 | POV ngoái lại từ lưng dốc | Thung lũng phía dưới; vệt máu đỏ trên sương từ suối tới đống đá | Ánh nhìn quét chậm theo vệt máu | Thở dốc làm khung lắc nhẹ | Không ai |
| A3-15 | Selfie OTS trong hang | Nhóm ngồi quanh bếp; thịt sống trên que | Thịt mới đặt lên lửa; mỡ xèo | Ánh lửa ấm | Không ai |
| A4-01 | Selfie OTS trong hang | Thủ Lĩnh ngồi bên bếp; Người Già cạnh que thịt | Thủ Lĩnh đứng dậy đi ra cửa hang; Người Già nhấc thịt ra, gói | Thịt còn đỏ hồng | Thủ Lĩnh đi bộ tới cửa hang (vẫn trong khung) |
| A4-02 | Selfie | 9 Neanderthal quanh bếp phía sau cô; gói thịt cạnh Người Già | Không | Ánh lửa lay | Không ai |
| EST-03 | Drone cao, tĩnh, lùi chậm | Thung lũng đen, một đốm lửa ở cửa hang | Lùi chậm | — | Không ai |
| A4-04 | Selfie OTS trong hang | Nhóm ngồi; Người Già cầm bọc than; giáo dựng vách | Sáu người đứng dậy; Nora đứng dậy, cầm bọc; Người Mạnh Nhất bước chắn, rồi lùi sang | — | Không ai |
| A4-05 | Selfie, đi bộ đêm | Người Mạnh Nhất đi trước 2 m; bọc than tay trái cô | 5–8s: cô vấp, ngã sấp về trước | Khung lao xuống đất, nghiêng; tiếng hự | Không ai |
| A4-06 | POV đứng sau Thủ Lĩnh | Đống đá bị bới dưới trăng cách 30 m; Thủ Lĩnh và Người Mạnh Nhất phía trước | Ba người lần lượt quay đầu theo ba tiếng kêu | — | Không ai |
| A4-07 | Selfie thì thầm | Mặt cô; bóng người cầm giáo phía sau | Mắt đảo theo hướng tiếng | — | Không ai |
| A4-08 | POV ngồi thấp | Ba linh cẩu đào đống đá cách 25 m | Chúng đào; đá lăn | Lông gáy dựng | Không ai |
| A4-09 | Selfie OTS | Thủ Lĩnh bên phải; bọc than trong tay trái cô | Cô mở bọc ra | Than đen nát, không khói | Không ai |
| A4-10 | Đặt trên đá phẳng 1 m, ngang gối (khác góc master) | Nora quỳ, túi da, rêu, vỏ cây; ba linh cẩu xa phía sau | Pyrite trượt, không tia | Tay run | Không ai |
| A4-11 | Selfie OTS thấp | Nora quỳ 1/3; Người Mạnh Nhất đứng trước với giáo; linh cẩu ở 20 m | Một linh cẩu tiến **một bước**; vài tia tắt | — | Không ai |
| A4-12 | Selfie OTS thấp | Người Mạnh Nhất chĩa giáo phía trước | Anh liếc lại; cô nhìn xuống tay | — | Không ai |
| A4-14 | Selfie OTS, đuốc tay trái | Bảy người cầm đuốc chưa đốt; ngọn lửa nhỏ dưới đất | Lửa chuyền đuốc; đội hình tiến chậm; linh cẩu lùi | Lửa đuốc phần phật | Linh cẩu lùi dần vào bóng tối (đi lùi rồi quay, đi chậm) |
| A4-15 | Selfie OTS | Hai người lăn đá; Người Mạnh Nhất cầm đuốc | Đá lăn; đuốc chuyền sang tay trái cô | — | Không ai |
| A4-16 | Selfie, đi bộ đêm | Đuốc tay trái cô; Thủ Lĩnh đi trước 3 m | Thủ Lĩnh chậm lại tới ngang hàng | — | Không ai |
| A5-01 | Selfie OTS trong hang | Người Mạnh Nhất bên bếp, thịt nướng | Anh xé miếng thịt, đưa | Hơi nóng bốc từ thịt | Không ai |
| A5-02 | Selfie OTS | Thủ Lĩnh ngồi đối diện qua bếp | Ông nói | Lửa lay | Không ai |
| A5-03 | POV ngồi trong hang | Cửa hang với trời sao; bọc than trong hai tay cô ở mép dưới | Ánh nhìn hạ từ sao xuống bọc than | Khói mảnh từ bọc | Không ai |
| A5-04 | Selfie ngoài cửa hang | Nhóm đang thức dậy phía sau; Thủ Lĩnh ngồi cạnh tảng đá | Cô đặt hai viên đá lên tảng đá bằng tay trái | Nắng sớm hồng nhạt | Không ai |
| A5-06 | Selfie OTS trên lối mòn, cách cửa hang ~10 m | Nora 1/3 trái; cửa hang 2/3 phía sau; Người Già đứng sẵn trên lối mòn ~3 m phía sau cô | 0–2s Người Già bước chậm ba bước xuống tới cô (đi bộ, hơi còng); đặt pyrite vào tay trái cô, gập ngón tay cô lại; quay lưng đi chậm lên dốc | Nora ngoái qua vai trái khi nghe tiếng chân; sương lạo xạo dưới chân bà | Bà đi bộ lên lối mòn về phía cửa hang, nhỏ dần nhưng vẫn trong khung |
| A5-07 | Selfie | Nora, cục pyrite trong tay trái, hang phía sau | Không | Thở ra khói | Không ai → CUT ĐEN |

---

## 7. `video_prompt`: Cold open + Act 1 (bảng vật lý + Act 1 đã duyệt 2026-10-05)

Mọi prompt theo thứ tự khối của PROMPT LOCK §10b. Camera guide khuyên 100–150 từ, nhưng các khối khóa §10b được ưu tiên vì đã chống được lỗi thật ở tập 1. Phần văn xuôi hành động vẫn giữ ngắn và tách câu chuyển động máy riêng.

**Khối dùng chung** (dán nguyên văn vào chỗ `[ID-LOCK]`):

```
IDENTITY & OUTFIT LOCK (CRITICAL -- match reference images exactly): her face and hair from the Nora face sheet, and her build and clothing from the Nora Body sheet (which serves as her dressed Body reference). BODY LOCK: Nora has a curvaceous, statuesque hourglass build with a large, prominent high natural bust, tiny narrow waist, shapely curvy hips, and long athletic legs matching the Nora Body sheet exactly; she is NOT flat-chested, NOT slender, NOT wearing a loose or boxy coat. Nora has honey-blonde hair pulled up into a high wavy ponytail tied at the crown of her head (not low at the nape), with wispy curtain bangs parted in the middle that cover the edges of her forehead and frame both cheeks, plus a few loose face-framing strands at the temples; her hair is never slicked back. She has grey-green eyes and fair skin with a natural pink flush. Nora wears the exact outfit from the Nora Body reference: a form-fitting tailored tunic of smoked golden-tan deer suede, precision-sewn with neat rows of fine sinew stitches along the shoulder, side and sleeve seams, with clean unadorned shoulders and completely open neck (strictly NO fur collar, NO fur on neck or shoulders, NO hood), hugging her full bust with a deep plunging laced V-neckline tied with thin criss-crossing leather thongs, tightly cinched at her tiny waist with a wide dark-brown leather belt that transitions seamlessly without any peplum flare into skin-tight golden-tan suede leggings hugging her athletic long legs; long fitted sleeves ending in thick plush fluffy grey wolf-fur cuffs at the wrists only; knee-high hide boots wrapped with leather thongs. This outfit is GOLDEN-TAN throughout -- NOT dark brown, NOT a draped caveman pelt, NOT white or cream, NOT sleeveless, NOT bare legs, NOT loose unkempt hair, NOT modern clothing. From the very first frame to the last, Nora is fully dressed in the complete outfit: clean suede shoulders, long sleeves with fur cuffs at the wrists, belt, leggings and boots. No part of the outfit appears, disappears or changes.
```

`[WET]` = `The suede is soaked from the chest down and darker where wet, with water dripping from the sleeves, the fur cuffs and the hem; the colour stays golden-tan and the shape never changes.`
`[HAIR]` = `Her curtain bangs stay over her forehead and her ponytail stays tied high at the crown for the entire clip; wind only makes the ponytail swing, it never pulls the hair back or loose.`
`[NEANDERTHAL]` = câu đặc điểm chung ở mục 2.
`[HYENA]` = câu khóa Cave Hyena ở mục 2.
`[SETTING-VALLEY]` = `a narrow limestone valley in the Dordogne, southwest France, about 51,000 years ago, in a cold glacial winter: pale yellow limestone cliffs, a shallow fast stream with thin white ice along its banks, frost-whitened short grass, scattered bare birches and dark pines; early morning, pale grey dawn light, cold mist low over the stream, no sun in the sky. Nothing modern exists anywhere.`
`[SETTING-CAVE]` = `the mouth of a low, wide tunnel-like cave in pale yellow limestone high on the valley side, about 51,000 years ago, in a cold glacial winter; frost-whitened earth and stones outside; flat overcast winter daylight. Inside, an open fire in a shallow sunken hearth ringed with stones in the earth floor; no fireplace, no chimney, no brick or built wall, no grate, no metal objects. Nothing modern exists anywhere.`
`[END-SELFIE]` = `Pure front-facing selfie view; the shot never switches to a third-person view. Only Nora speaks English; nobody speaks over anyone else. No subtitles or text appear in the frame. Real amateur footage, not a 3D render.`
`[END-CLEAN]` = `Only Nora speaks English; nobody speaks over anyone else. No subtitles or text appear in the frame. The image is clean footage only: no on-screen interface, no recording indicator, no battery icon, no zoom label, no names, no text or symbols. Real amateur footage, not a 3D render.`

> Khi POST/PATCH, các placeholder được **thay bằng văn bản đầy đủ**. Không gửi chữ `[ID-LOCK]` lên Flow.

---

### MASTER-FIRE · `duration: 10` · FIX · refs `["Nora","Nora Body","Cave Hyena"]`

```
Static footage from a fixed viewpoint resting on a flat stone on the frozen ground about one metre in front of Nora, low at her knee height, looking at her in a three-quarter view; the frame does not move; nobody touches the viewpoint. Both of Nora's hands are free. Natural wide-angle perspective, no exaggerated fisheye distortion.
Setting: a frost-covered grassy slope in a limestone valley in the Dordogne, southwest France, about 51,000 years ago, on a still winter night with no wind: moonlight only, cold blue-grey light on the frost, deep darkness beyond ten metres. A low pile of grey stones behind her has been dug open, with pale bones and torn hide scattered beside it. Nothing modern exists anywhere.
Everything is already in place from the very first frame: Nora kneels in the centre of the frame on the frost. On the ground directly in front of her knees lies one flat piece of bark holding a small tuft of dry moss dusted with a pinch of dark mineral powder. To her left on the ground lies one opened roll of birch bark with a black, crushed ember inside; no glow, no smoke. Her left hand holds exactly one grey flint biface, an oval stone flaked on both faces with no handle, held just above the moss; her right hand holds exactly one brassy gold lump of pyrite. Eight to twelve metres behind her in the moonlit darkness stand exactly three cave hyenas, one on the left, one in the centre, one on the right, their eyes catching faint moonlight. Everything stays in that same spot except where described; nothing appears suddenly, nothing vanishes. No other person is in the frame.
Shot: medium close-up; Nora fills the left two-thirds of the frame from the waist up, the moss and her hands in the lower third, the three hyenas small and dark in the background on the right.
[HYENA]
[ID-LOCK]
[HAIR]
Fire process: She strikes the pyrite in a fast glancing stroke down along the flat face of the flint biface, lengthwise. Only a few tiny, short-lived orange sparks jump from the point of contact and fall onto the dry moss. The moss first shows one small red glowing spot and a thin wisp of smoke; she lowers her face close and blows gently; only after several seconds does a small flame appear. There is no shower of sparks and no instant flame.
0-2s: The centre hyena takes one slow step forward, head low, the hair along its neck and back standing up. Nora's hands tremble as she sets the pyrite against the flat face of the biface; the grey wolf-fur cuff on her right sleeve shakes with her hand; her breath leaves dense short-lived vapor that dissipates rapidly. Nora says in a fast whisper: "Three. Getting closer." (no subtitles)
2-4s: She strikes in a fast glancing stroke down along the flat face of the biface; the pyrite slips off the stone and no spark appears. Her shoulders jerk with the miss.
4-6s: She strikes again the same way; only two or three tiny orange sparks jump from the contact point and die in the air before reaching the moss. Nora says through her teeth: "Come on—" (no subtitles)
6-8s: Third strike, the same glancing stroke lengthwise along the flat face; a few tiny orange sparks fall straight onto the dusted moss; one small red glowing spot appears and a thin wisp of smoke rises straight up. She freezes, holding her breath.
8-10s: She lowers her face close to the moss and blows gently, twice; the red spot spreads; one small yellow flame appears and licks up from the moss, lighting her face warm orange from below while the hyenas stay dark behind her. She exhales shakily.
The hyenas never cross in front of her and never touch her. [END-CLEAN]
Audio: near silence; Nora's fast shaky breathing; the dry scrape and click of stone on stone; low hyena growls; one distant hyena whoop; at 8-10s the soft crackle of catching moss.
```

### EST-01 · `duration: 6` · DR · refs `["Nora","Nora Body","Pech Valley"]`

```
Aerial footage from high above a valley, gliding slowly forward and slightly downward at a steady pace; the frame drifts smoothly with gentle wind sway and never spins. Natural wide-angle perspective, no exaggerated fisheye distortion.
Setting: [SETTING-VALLEY] At dawn a dark tunnel-like cave opening sits high in the right-hand cliff, about fifty metres above the valley floor, with a faint thread of smoke rising from inside. No buildings, roads, fences or fields.
Everything is already in place from the very first frame: one tiny figure, Nora, in golden-tan clothing, stands still on the left bank of the stream in the lower centre of the frame, small as a dot; she stays in that same spot; nothing appears suddenly or vanishes. No animals and no other people are visible.
Shot: extreme wide aerial shot; the valley fills the frame, the stream runs from the bottom to the top, the cave opening in the upper right.
0-3s: The view glides forward over the mist; the mist drifts slowly along the stream.
3-6s: The view keeps gliding toward the tiny figure; the thread of smoke from the cave opening bends gently in the light wind; the figure stays tiny and still.
No subtitles or text appear in the frame. The image is clean footage only: no on-screen interface, no recording indicator, no battery icon, no zoom label, no names, no text or symbols. Real amateur footage, not a 3D render.
Audio: cold wind, the soft rush of the stream, one distant crow. No voice.
```

### A1-01 · `duration: 8` · SEL · refs `["Nora","Nora Body"]`

```
The lens sits at the end of Nora's outstretched right arm, completely outside the visible frame and never seen; her right arm stays extended toward the lens and held up above the water for the entire clip, and she never reaches toward, touches, covers, taps, or points at the lens. Only her left hand is free. Handheld footage with natural wide-angle perspective, no exaggerated fisheye distortion; the frame jolts hard with her body.
Setting: [SETTING-VALLEY] The edge of the stream: a steep bank of frozen mud and frost-whitened grass, fast dark water about chest deep, one thick tree root sticking out of the bank.
Everything is already in place from the very first frame: Nora stands at the very edge of the frosted bank with the misty stream right behind her; exactly one thick exposed root sticks out of the bank at the left edge of the frame. Everything stays in that same spot; nothing appears suddenly, nothing vanishes. No other people and no animals.
Shot: medium selfie; Nora's face and upper body in the centre third, the misty stream and the far bank behind her.
[ID-LOCK]
[HAIR]
0-3s: Nora steps back onto the edge of the bank; the frozen mud cracks under her boot and the bank gives way; she slides backward down into the stream with a hard splash, the frame lurching down and sideways with her body; icy water surges up to her chest and sprays across the frame; her wolf-fur collar is splashed dark. Nora gasps sharply.
3-6s: Gasping from the cold shock, she grabs the exposed root with her free left hand and drags herself up the bank, her boots slipping on the mud; water streams off her golden-tan suede sleeves and her wide belt.
6-8s: She kneels on the frosted bank, shaking hard. [WET] Her breath leaves dense short-lived vapor that dissipates rapidly. Nora says through chattering teeth: "Ten seconds in. Soaked." (no subtitles)
[END-SELFIE]
Audio: crack of frozen mud, heavy splash, rushing cold water, Nora's sharp gasps, chattering teeth, a crow far away.
```

### A1-02 · `duration: 8` · FIX · refs `["Nora","Nora Body"]`

```
Static footage from a fixed viewpoint resting on a flat boulder on the stream bank about one and a half metres in front of Nora at her chest height; the frame does not move; nobody touches the viewpoint. Both of Nora's hands are free. Natural wide-angle perspective, no exaggerated fisheye distortion.
Setting: [SETTING-VALLEY]
Everything is already in place from the very first frame: Nora kneels on frost-whitened grass in the centre of the frame; behind her lies exactly one fallen birch trunk, its bare branches coated in white frost; every blade of grass and every stone is frozen; there is no dry wood anywhere. Everything stays in that same spot; nothing appears suddenly, nothing vanishes. No other people and no animals.
Shot: medium shot; Nora from the knees up in the centre, the frozen birch behind her on the right.
[ID-LOCK]
[WET]
[HAIR]
0-3s: She grips the soaked end of her right sleeve with both hands and tries to wring it; her fingers are stiff and clumsy and slip off the wet suede; only a few drops fall onto the frost.
3-6s: She shoves both hands into her armpits under the grey wolf-fur collar, shaking hard, her breath leaving dense short-lived vapor that dissipates rapidly. Nora says, fast and tense: "Wet clothes kill faster than cold." (no subtitles)
6-8s: She pulls her left hand out and touches one frosted birch branch behind her: the frost is wet under her fingers; she pulls the hand back and stares at her stiff red fingers.
[END-CLEAN]
Audio: thin cold wind, the stream rushing, Nora's chattering teeth and fast breathing, a drop of water hitting the frost.
```

### A1-03 · `duration: 8` · OTS · refs `["Nora","Nora Body","Leader","Old Woman","Strongest","Strongest Spear"]`

```
The lens sits at the end of Nora's outstretched right arm, completely outside the visible frame and never seen; her right arm stays extended toward the lens for the entire clip, and she never reaches toward, touches, covers, taps, or points at the lens. Only her left hand is free, and it stays empty. Handheld footage with natural wide-angle perspective, no exaggerated fisheye distortion, subtle hand shake.
Setting: [SETTING-VALLEY] Behind her, the edge of a pine and birch wood on the valley side.
Everything is already in place from the very first frame: Nora stands in the left third of the frame, close to the lens. About fifteen metres behind her, at the edge of the wood and half hidden behind tree trunks in shadow, stand exactly five Neanderthals: the Leader in the centre; the Strongest on the right holding exactly one long wooden spear upright in his right hand; the Old Woman on the left; one man with a white scar across his left eyebrow; one man with long black hair tied at the nape with leather. All five are visible from the first frame; nobody appears suddenly, nobody vanishes; there are no other people anywhere in the frame.
Shot: over-the-shoulder selfie; Nora fills the left third, the five Neanderthals the right two-thirds.
[NEANDERTHAL]
[ID-LOCK]
[WET]
Every Neanderthal's lips stay closed for the entire clip; the only moving mouth in the frame is Nora's.
[HAIR]
0-3s: A dry branch snaps loudly under the Strongest's foot; Nora jerks her head round over her left shoulder toward the sound, her ponytail swinging.
3-6s: The five Neanderthals walk slowly out of the trees side by side toward her, the Strongest's spear held low, and stop about six metres behind her, staring; Nora turns her face back toward the lens, eyes wide, her wet golden-tan sleeve trembling.
6-8s: Nora says in a fast whisper: "Don't run." (no subtitles) Then one second of silence; nobody moves.
[END-SELFIE]
Audio: the loud snap of a branch, footsteps crunching on frost, Nora's held breath, the stream far behind.
```

### A1-04 · `duration: 8` · OTS · refs `["Nora","Nora Body","Leader","Strongest","Old Woman","Strongest Spear"]`

```
The lens sits at the end of Nora's outstretched right arm, completely outside the visible frame and never seen; her right arm stays extended toward the lens for the entire clip, and she never reaches toward, touches, covers, taps, or points at the lens. Only her left hand is free, and it stays empty. Handheld footage with natural wide-angle perspective, no exaggerated fisheye distortion; the frame stays almost still because she is holding her breath.
Setting: [SETTING-VALLEY]
Everything is already in place from the very first frame: Nora stands in the left third, close to the lens. The Leader stands about three metres behind her on the right. Six metres behind him stand the Strongest holding exactly one long wooden spear in his right hand, the Old Woman, one man with a white scar across his left eyebrow, and one man with long black hair tied at the nape. Exactly five Neanderthals and Nora are present; there are no other people anywhere in the frame. Everyone stays in place except the Leader; nobody appears suddenly, nobody vanishes.
Shot: over-the-shoulder selfie; Nora in the left third, the Leader in the right two-thirds, the group soft behind him.
[NEANDERTHAL] The Leader is a broad man about thirty-five with a very heavy brow ridge, dark-brown skin and shaggy black shoulder-length hair, wearing a dark deer hide.
[ID-LOCK]
[WET]
[HAIR]
0-3s: The Leader walks forward to about one and a half metres from her shoulder and leans in, sniffing the air near her twice, his nostrils flaring; his lips stay closed. Nora stays completely still; only her eyes move toward him.
3-5s: The Leader speaks a few short syllables in a gravelly, low-pitched male voice — short guttural sounds, consonant-heavy, no recognizable words. Nora stays silent while he speaks. All other Neanderthals keep their lips closed.
5-8s: The Leader's lips close. Nora says quietly to the lens, deadpan: "No idea what he said. But that wasn't a question." (no subtitles) Her wet wolf-fur collar trembles with her shivering.
[END-SELFIE]
Audio: the Leader's sniffing, his gravelly guttural syllables, Nora's shaky breath, wind in the pines.
```

### A1-05 · `duration: 8` · SEL · refs `["Nora","Nora Body","Leader"]`

```
The lens sits at the end of Nora's outstretched right arm, completely outside the visible frame and never seen; her right arm stays extended toward the lens for the entire clip, and she never reaches toward, touches, covers, taps, or points at the lens. Only her left hand is free, and it hangs empty at her side. Handheld footage with natural wide-angle perspective, no exaggerated fisheye distortion, subtle hand shake from her shivering.
Setting: [SETTING-VALLEY]
Everything is already in place from the very first frame: Nora fills the centre of the frame from the chest up. The Leader stands close at her left side, his right hand already raised beside her left shoulder. No other person is in the frame. Everyone stays in place; nobody appears suddenly, nobody vanishes.
Shot: close selfie; Nora's face and shoulders in the centre, her left shoulder seam and the Leader's hand in the left third, the Leader's face partly in the frame behind it.
[NEANDERTHAL] The Leader is a broad man about thirty-five with a very heavy brow ridge, dark-brown skin and shaggy black shoulder-length hair, wearing a dark deer hide draped and tied with no seams.
[ID-LOCK]
[WET]
The Leader's lips stay closed for the entire clip; the only moving mouth in the frame is Nora's.
[HAIR]
0-3s: The Leader pinches the wet suede at her left shoulder seam between his thumb and finger and slowly rubs the neat row of sinew stitches, frowning; cold water drips onto his fingers.
3-6s: He looks down at the untied edge of his own draped hide, then back at her stitched seam; then his eyes move to her jaw, which is shaking.
6-8s: He lets go and lowers his hand out of the frame with one closed-mouth grunt. Nora says, dry, through chattering teeth: "Yeah. Stitches. Still freezing." (no subtitles)
[END-SELFIE]
Audio: the soft squeak of wet suede under his fingers, water dripping, Nora's chattering teeth, one low grunt.
```

### A1-06 · `duration: 8` · SEL · refs `["Nora","Nora Body","Strongest","Strongest Spear","Leader","Cave Mouth"]`

```
The lens sits at the end of Nora's outstretched right arm, completely outside the visible frame and never seen; her right arm stays extended toward the lens for the entire clip, and she never reaches toward, touches, covers, taps, or points at the lens. Only her left hand is free, and it stays empty. Handheld footage with natural wide-angle perspective, no exaggerated fisheye distortion, with natural vertical bounce synchronized to each uphill step.
Setting: [SETTING-CAVE] A narrow frosted path climbs the last few metres to the entrance.
Everything is already in place from the very first frame: Nora walks uphill in the left third of the frame, the lens slightly ahead of her. Three to five metres ahead, the Leader, the Old Woman and two men walk up the path toward the cave. The Strongest already stands at the right side of the cave entrance holding exactly one long wooden spear in his right hand. Warm firelight glows inside the cave. Exactly five Neanderthals and Nora are present outside; nobody appears suddenly, nobody vanishes.
Shot: walking selfie; Nora in the left third, the path and the cave entrance in the right two-thirds.
[NEANDERTHAL]
[ID-LOCK]
[WET]
Every Neanderthal's lips stay closed for the entire clip; the only moving mouth in the frame is Nora's.
[HAIR]
0-3s: The group walks into the cave one after another and disappears into the dark interior past the firelight; Nora keeps walking up after them, shivering, her wet belt and fur cuffs dripping.
3-6s: As Nora reaches the entrance, the Strongest takes one step sideways across it in front of her, holding the spear across his body; she stops short and the frame stops with her.
6-8s: He jerks his chin toward the dark wood down the slope, expressionless. Nora says, flat: "Okay. Outside. Got it." (no subtitles)
[END-SELFIE]
Audio: footsteps on frosted gravel, the crackle of the fire inside, Nora's shivering breath, wind.
```

### A1-07 · `duration: 8` · POV · refs `["Nora","Nora Body","Old Woman","Cave Mouth"]`

```
The view is Nora's own eyes; all recording gear is completely outside the visible frame, and her hands stay out of frame for the whole clip. Her face never appears. Natural wide-angle perspective, no exaggerated fisheye distortion; the view moves slowly like a person's eyes, with a slight sway from her shivering.
Setting: [SETTING-CAVE]
Everything is already in place from the very first frame: on the frost-whitened ground at the cave entrance, in the foreground, lies a line of large paw prints, each with four rounded toes and short blunt claw marks, bigger at the front feet than the back. About four metres inside, beside the fire, a Neanderthal man with a grey-streaked beard lies on hides, his left leg wrapped in hide stained dark; the Old Woman kneels beside him. Exactly two Neanderthals are in view; nobody appears suddenly, nobody vanishes.
Shot: first the ground in the lower two-thirds, then the interior.
[NEANDERTHAL] The Old Woman is small and slightly stooped with long grey hair and bright eyes.
Both Neanderthals' lips stay closed for the entire clip.
0-3s: The view looks down at the paw prints and slowly follows them toward the entrance.
3-6s: The view rises to the injured man by the fire; he shifts on the hides and grimaces in silence, clutching his wrapped leg; the Old Woman presses a pad of moss against the dark stain.
6-8s: The view drops back to one paw print near her feet. Nora's voice says, low and quiet: "Something bit him. Something that comes at night." (no subtitles)
[END-CLEAN]
Audio: crackling fire, the injured man's strained breathing, wind at the entrance, Nora's low voice.
```

### A1-08 · `duration: 8` · OTS · refs `["Nora","Nora Body","Leader","Strongest","Cave Mouth"]`

```
The lens sits at the end of Nora's outstretched right arm, completely outside the visible frame and never seen; her right arm stays extended toward the lens for the entire clip, and she never reaches toward, touches, covers, taps, or points at the lens. Only her left hand is free, and it stays empty. Handheld footage with natural wide-angle perspective, no exaggerated fisheye distortion, subtle hand shake.
Setting: [SETTING-CAVE]
Everything is already in place from the very first frame: Nora stands just outside the entrance in the left third of the frame. The Leader stands about one and a half metres in front of her on the right, holding exactly one grey flint biface, an oval stone flaked on both faces with no handle, in his left hand and exactly one brassy gold lump of pyrite in his right hand. The Strongest stands in the cave entrance behind him holding exactly one long wooden spear. There is no metal anywhere. Exactly two Neanderthals and Nora are present; nobody appears suddenly, nobody vanishes.
Shot: over-the-shoulder selfie; Nora in the left third, the Leader in the right two-thirds, the firelit cave entrance behind him.
[NEANDERTHAL] The Leader is a broad man about thirty-five with a very heavy brow ridge, dark-brown skin and shaggy black shoulder-length hair.
[ID-LOCK]
[WET]
Both Neanderthals' lips stay closed for the entire clip; the only moving mouth in the frame is Nora's.
[HAIR]
0-3s: The Leader strikes the pyrite once in a fast glancing stroke down along the flat face of the biface, lengthwise; only a few tiny, short-lived orange sparks jump and die before they touch the ground; there is no shower of sparks.
3-6s: He drops both stones onto the frost at her feet, where they bounce once and lie still. Then he points slowly with his right hand: at the stones, then into the cave at the fire, then at Nora, then down the slope at the dark wood.
6-8s: Nora looks from the stones to the dark wood and back to the lens, her wet fur collar shaking. Nora says, low and fast: "My own fire. Or I sleep out there." (no subtitles)
[END-SELFIE]
Audio: the sharp click of stone on stone, the soft thud of stones on frost, the crackle of the fire inside, wind.
```

### A1-09 · `duration: 8` · FIX · refs `["Nora","Nora Body","Leader","Strongest","Cave Mouth"]`

```
Static footage from a fixed viewpoint resting on a low rock on the slope about one and a half metres below Nora, looking slightly up at her with the cave entrance behind her; the frame does not move; nobody touches the viewpoint. Both of Nora's hands are free. Natural wide-angle perspective, no exaggerated fisheye distortion.
Setting: [SETTING-CAVE]
Everything is already in place from the very first frame: Nora kneels on the bare frozen earth in the centre of the frame, exactly one grey flint biface in her left hand and exactly one brassy gold lump of pyrite in her right hand; there is nothing on the ground in front of her. In the cave entrance behind her stand four Neanderthals watching: the Leader, the Strongest holding exactly one long wooden spear, one man with a white scar across his left eyebrow, and one man with long black hair tied at the nape. There is no metal anywhere. Nobody appears suddenly; nobody vanishes except by walking into the cave.
Shot: medium shot; Nora from the knees up in the lower centre, the four Neanderthals in the entrance in the upper part of the frame.
[NEANDERTHAL]
[ID-LOCK]
[WET]
Every Neanderthal's lips stay closed for the entire clip; the only moving mouth in the frame is Nora's.
[HAIR]
0-3s: Nora slowly scrapes the edge of the biface down the pyrite with steady pressure, the way someone scrapes a steel rod; one single faint spark drops onto the bare frozen earth and dies at once. Nora says, half to herself: "Like a ferro rod. Right?" (no subtitles)
3-6s: She scrapes again, harder, her wet sleeves trembling; nothing appears at all.
6-8s: Behind her, the four Neanderthals turn and walk into the cave one after another and disappear into the dark interior. Nora looks over her shoulder after them, then back down at the two stones in her hands, silent.
[END-CLEAN]
Audio: the dry grinding scrape of stone, wind, footsteps fading into the cave, the faint crackle of the fire inside.
```

### A1-10 · `duration: 8` · OTS · refs `["Nora","Nora Body","Old Woman","Cave Mouth"]`

```
The lens sits at the end of Nora's outstretched right arm, completely outside the visible frame and never seen; her right arm stays extended toward the lens for the entire clip, and she never reaches toward, touches, covers, taps, or points at the lens. Only her left hand is free, and it rests empty on her knee. Handheld footage with natural wide-angle perspective, no exaggerated fisheye distortion, subtle hand shake.
Setting: [SETTING-CAVE]
Everything is already in place from the very first frame: Nora sits on the frozen ground outside the entrance in the left third of the frame; the biface and the pyrite lie on the ground beside her; in front of her lies one flat piece of bark. The Old Woman already stands just inside the entrance behind her on the right, holding exactly four small tufts of dry moss cupped in both hands. Exactly one Neanderthal and Nora are present; nobody appears suddenly, nobody vanishes except by walking into the cave.
Shot: over-the-shoulder selfie; Nora in the left third, the Old Woman and the entrance in the right two-thirds.
[NEANDERTHAL] The Old Woman is small and slightly stooped with long grey hair and bright eyes.
[ID-LOCK]
[WET]
The Old Woman's lips stay closed for the entire clip; the only moving mouth in the frame is Nora's.
[HAIR]
0-3s: The Old Woman walks slowly out of the entrance to Nora and crouches beside the piece of bark.
3-6s: She places exactly four small tufts of dry moss in a row on the bark, one by one, without looking at Nora; the count stays exactly four.
6-8s: She pushes herself up with a hand on her knee and walks back into the cave without a sound. Nora looks at the four tufts, then at the lens; her wet fur cuff trembles. Nora says quietly: "Okay." (no subtitles) Then silence.
[END-SELFIE]
Audio: soft footsteps on frost, the fire crackling inside, wind, one long breath from Nora.
```

---

## 7b. `video_prompt`: Act 2 "FIRE" (nháp, chờ duyệt)

Thêm 2 placeholder cho Act 2:
`[OLD-WOMAN]` = `The Old Woman is small and slightly stooped with long grey hair and bright eyes; a small hide pouch tied with a thong hangs at her left hip.`
`[LEADER]` = `The Leader is a broad man about thirty-five with a very heavy brow ridge, dark-brown skin and shaggy black shoulder-length hair, wearing a dark deer hide draped and tied with no seams.`

### A2-01 · `duration: 8` · OTS · refs `["Nora","Nora Body","Old Woman","Cave Mouth"]`

```
The lens sits at the end of Nora's outstretched right arm, completely outside the visible frame and never seen; her right arm stays extended toward the lens for the entire clip, and she never reaches toward, touches, covers, taps, or points at the lens. Only her left hand is free, and it rests empty on her knee. Handheld footage with natural wide-angle perspective, no exaggerated fisheye distortion, subtle hand shake.
Setting: [SETTING-CAVE]
Everything is already in place from the very first frame: Nora sits on the frozen ground outside the entrance in the left third of the frame. The Old Woman kneels close beside her on the right, facing a flat piece of bark on the ground that holds one small tuft of dry moss of her own; she already holds exactly one grey flint biface, an oval stone flaked on both faces with no handle, in her left hand and exactly one brassy gold lump of pyrite in her right hand. Beside Nora's knee, a second piece of bark holds exactly four small tufts of dry moss in a row. There is no metal anywhere. Exactly one Neanderthal and Nora are present; nobody appears suddenly, nobody vanishes.
Shot: over-the-shoulder selfie; Nora in the left third, the Old Woman and her bark in the right two-thirds, the cave entrance behind them.
[NEANDERTHAL] [OLD-WOMAN]
[ID-LOCK]
[WET]
The Old Woman's lips stay closed for the entire clip; the only moving mouth in the frame is Nora's.
[HAIR]
Fire process: She strikes the pyrite in a fast glancing stroke down along the flat face of the flint biface, lengthwise. Only a few tiny, short-lived orange sparks jump from the point of contact and fall onto the dry moss. The moss first shows one small red glowing spot and a thin wisp of smoke; she lowers her face close and blows gently; only after several seconds does a small flame appear. There is no shower of sparks and no instant flame.
0-2s: In one quick, casual movement, without looking at Nora, the Old Woman pinches something from the pouch at her hip and sprinkles it onto her moss; it is so fast it is easy to miss.
2-5s: She strikes three times in fast glancing strokes down along the flat face of the biface; on the third strike a few tiny sparks land on her moss, one small red glowing spot appears and a thin wisp of smoke rises; she lowers her face and blows gently until one small flame appears.
5-8s: She lets the flame burn for a moment, then presses it out with a handful of frozen earth, sets the two stones down beside Nora and looks at her. Nora stares at the smothered moss, then at the lens. Nora says, fast and low: "Three strikes. She does it in three." (no subtitles)
The four tufts beside Nora's knee stay exactly four. [END-SELFIE]
Audio: three sharp clicks of stone on stone, the faint hiss of catching moss, a soft breath of blowing, the dull pat of earth smothering it, wind.
```

### A2-02 · `duration: 8` · FIX · refs `["Nora","Nora Body","Cave Mouth"]`

```
Static footage from a fixed viewpoint resting on a flat stone on the frozen ground about one metre in front of Nora, low at her knee height; the frame does not move; nobody touches the viewpoint. Both of Nora's hands are free. Natural wide-angle perspective, no exaggerated fisheye distortion.
Setting: [SETTING-CAVE]
Everything is already in place from the very first frame: Nora kneels on the frozen ground outside the cave entrance in the centre of the frame. On the ground in front of her knees lies one flat piece of bark holding exactly four small tufts of dry moss in a row. Her left hand holds exactly one grey flint biface, an oval stone flaked on both faces with no handle, just above the first tuft; her right hand holds exactly one brassy gold lump of pyrite. There is no metal anywhere. No other person is in the frame; nothing appears suddenly, nothing vanishes.
Shot: medium close-up; Nora from the waist up in the upper two-thirds, the bark, the moss and her hands in the lower third, the cave entrance soft behind her.
[ID-LOCK]
[WET]
[HAIR]
0-3s: Her hands shake hard. She strikes the pyrite in a fast glancing stroke down along the flat face of the biface; her trembling hand slips and the pyrite skids off the stone.
3-6s: The slipping pyrite knocks the first tuft of moss off the bark; it tumbles about thirty centimetres onto the white frost and darkens as it soaks up the wet. She picks it up with her left fingertips, feels that it is wet, and drops it.
6-8s: Exactly three tufts remain on the bark. Nora says through chattering teeth: "No— okay. Three left." (no subtitles)
[END-CLEAN]
Audio: the scrape and skid of stone, a soft pat of moss on frost, Nora's chattering teeth and fast breathing, wind.
```

### A2-03 · `duration: 8` · FIX · refs `["Nora","Nora Body","Strongest","Strongest Spear","Cave Mouth"]`

```
Static footage from a fixed viewpoint resting on a flat stone on the frozen ground about one metre in front of Nora, low at her knee height; the frame does not move; nobody touches the viewpoint. Both of Nora's hands are free. Natural wide-angle perspective, no exaggerated fisheye distortion.
Setting: [SETTING-CAVE]
Everything is already in place from the very first frame: Nora kneels in the centre of the frame; in front of her knees lies one flat piece of bark holding exactly three small tufts of dry moss. Her left hand holds exactly one grey flint biface, an oval stone flaked on both faces with no handle; her right hand holds exactly one brassy gold lump of pyrite. In the cave entrance behind her stand exactly three Neanderthals watching: the Strongest holding exactly one long wooden spear upright in his right hand, one man with a white scar across his left eyebrow with his arms folded, and one man with long black hair tied at the nape with his arms folded. There is no metal anywhere. Nobody appears suddenly, nobody vanishes.
Shot: medium close-up; Nora from the waist up in the centre, the moss and her hands in the lower third, the three watchers small in the entrance behind her.
[NEANDERTHAL]
[ID-LOCK]
[WET]
Every Neanderthal's lips stay closed for the entire clip; the only moving mouth in the frame is Nora's.
[HAIR]
0-3s: She strikes the pyrite in a fast glancing stroke down along the flat face of the biface, lengthwise; only a few tiny, short-lived orange sparks fall onto the first tuft, and one faint red speck appears for a moment.
3-6s: She bends down and blows on it hard, much too hard; the tuft bursts apart and scatters over the frost in loose strands, and the red speck dies at once. There is no flame.
6-8s: Exactly two tufts remain on the bark. Behind her the three watchers stay still and expressionless. Nora says flatly, breathing hard: "Too hard. Two left." (no subtitles)
[END-CLEAN]
Audio: the click of stone on stone, one sharp puff of breath, the dry rustle of scattering moss, wind.
```

### A2-04 · `duration: 8` · SEL · refs `["Nora","Nora Body"]`

```
The lens sits at the end of Nora's outstretched right arm, completely outside the visible frame and never seen; her right arm stays extended toward the lens for the entire clip, and she never reaches toward, touches, covers, taps, or points at the lens. Only her left hand is free. Handheld footage with natural wide-angle perspective, no exaggerated fisheye distortion; the frame shakes with her shivering.
Setting: [SETTING-CAVE]
Everything is already in place from the very first frame: Nora kneels outside the cave entrance, filling the centre of the frame from the chest up; her left hand is raised empty in front of her chest. No other person is in the frame; nothing appears suddenly, nothing vanishes.
Shot: close selfie; Nora's face and her raised left hand fill the frame.
[ID-LOCK]
[WET]
[HAIR]
0-3s: She shakes violently; her lips have turned faintly bluish and her jaw chatters; her breath leaves dense short-lived vapor that dissipates rapidly.
3-6s: She looks down at her stiff, red left hand and tries to close it into a fist; the fingers bend only halfway and stop. Nora says, fast, through her teeth: "Can't feel my fingers. That's stage one." (no subtitles)
6-8s: She tucks the hand into her armpit under the wet wolf-fur collar and looks back at the lens, eyes watering from the cold.
[END-SELFIE]
Audio: chattering teeth, fast shallow breathing, wind across the slope.
```

### A2-05 · `duration: 8` · FIX · refs `["Nora","Nora Body","Strongest","Strongest Spear","Cave Mouth"]`

```
Static footage from a fixed viewpoint resting on a flat stone on the frozen ground about one metre in front of Nora, low at her knee height; the frame does not move; nobody touches the viewpoint. Both of Nora's hands are free. Natural wide-angle perspective, no exaggerated fisheye distortion.
Setting: [SETTING-CAVE] A cold wind blows up the slope from the valley.
Everything is already in place from the very first frame: Nora kneels in the centre of the frame, hunched low over one flat piece of bark that holds exactly two small tufts of dry moss. Her left hand holds exactly one grey flint biface, an oval stone flaked on both faces with no handle; her right hand holds exactly one brassy gold lump of pyrite. The Strongest stands in the cave entrance behind her holding exactly one long wooden spear upright in his right hand. There is no metal anywhere. Nobody appears suddenly; nobody vanishes except by walking into the cave.
Shot: medium close-up; Nora from the waist up in the centre, the moss in the lower third, the Strongest small in the entrance behind her.
[NEANDERTHAL]
[ID-LOCK]
[WET]
The Strongest's lips stay closed for the entire clip; the only moving mouth in the frame is Nora's.
[HAIR]
0-3s: Hunched over to shield the moss with her body, she strikes the pyrite in a fast glancing stroke down along the flat face of the biface; a few tiny sparks fall short and die.
3-6s: A strong gust comes up the slope; her ponytail swings hard; the gust lifts both tufts off the bark at once and blows them down the slope past the bottom edge of the frame. She lunges after them with her left hand and catches only air. Nora says, rising and cracking: "No no no—" (no subtitles)
6-8s: The bark in front of her is empty. Behind her, the Strongest turns away and walks into the cave. Nora stays on her knees, staring at the empty bark, the two stones hanging in her hands.
[END-CLEAN]
Audio: the click of stone, a rushing gust of wind, Nora's cracking voice, footsteps fading into the cave.
```

### A2-06 · `duration: 8` · OTS · refs `["Nora","Nora Body","Old Woman","Cave Mouth"]`

```
The lens sits at the end of Nora's outstretched right arm, completely outside the visible frame and never seen; her right arm stays extended toward the lens for the entire clip, and she never reaches toward, touches, covers, taps, or points at the lens. Only her left hand is free. Handheld footage with natural wide-angle perspective, no exaggerated fisheye distortion, subtle hand shake.
Setting: [SETTING-CAVE]
Everything is already in place from the very first frame: Nora sits on the frozen ground outside the entrance in the left third of the frame; the empty piece of bark lies in front of her and the biface and the pyrite lie on the frost beside it. The Old Woman kneels close beside her on the right, already holding one small tuft of dry moss in her left hand and a small bundle of thin dry twigs under her arm; the hide pouch hangs at her hip. There is no metal anywhere. Exactly one Neanderthal and Nora are present; nobody appears suddenly, nobody vanishes except by walking into the cave.
Shot: over-the-shoulder selfie; Nora in the left third, the Old Woman's hands and face in the right two-thirds.
[NEANDERTHAL] [OLD-WOMAN]
[ID-LOCK]
[WET]
The Old Woman's lips stay closed for the entire clip; the only moving mouth in the frame is Nora's.
[HAIR]
0-3s: The Old Woman sets the moss on the bark and the twigs beside it. Slowly this time, she opens the pouch, takes out a small pinch of dark mineral powder and holds it up close in front of Nora's eyes.
3-6s: She sprinkles the dark powder onto the middle of the moss, then taps her fingertip twice on that exact spot, looking straight at Nora.
6-8s: She picks up the pyrite and presses it into Nora's free left hand, unties the pouch from her hip and sets it down on the frost beside Nora, then pushes herself up and walks back into the cave. Nora looks down at the pouch. Nora says quietly: "Something dark. Right where the spark lands." (no subtitles)
[END-SELFIE]
Audio: the soft rustle of the pouch opening, two light taps on the moss, footsteps on frost, the fire crackling inside.
```

### A2-07 · `duration: 8` · FIX · refs `["Nora","Nora Body","Cave Mouth"]`

```
Static footage from a fixed viewpoint resting on a flat stone on the frozen ground about one metre in front of Nora, low at her knee height; the frame does not move; nobody touches the viewpoint. Both of Nora's hands are free. Natural wide-angle perspective, no exaggerated fisheye distortion.
Setting: [SETTING-CAVE]
Everything is already in place from the very first frame: Nora kneels in the centre of the frame. In front of her knees lies one flat piece of bark holding one small tuft of dry moss dusted with dark mineral powder; beside it lie a small bundle of thin dry twigs and the open hide pouch. Her left hand holds exactly one grey flint biface, an oval stone flaked on both faces with no handle, just above the moss; her right hand holds exactly one brassy gold lump of pyrite. There is no metal anywhere. No other person is in the frame; nothing appears suddenly, nothing vanishes.
Shot: medium close-up; Nora from the waist up in the upper two-thirds, the moss and her hands in the lower third.
[ID-LOCK]
[WET]
[HAIR]
Fire process: She strikes the pyrite in a fast glancing stroke down along the flat face of the flint biface, lengthwise. Only a few tiny, short-lived orange sparks jump from the point of contact and fall onto the dry moss. The moss first shows one small red glowing spot and a thin wisp of smoke; she lowers her face close and blows gently; only after several seconds does a small flame appear. There is no shower of sparks and no instant flame.
0-3s: She strikes once; the pyrite slips and nothing happens. She sets her jaw and strikes again the same way, lengthwise along the flat face; a few tiny sparks fall onto the dark powder and one small red glowing spot appears with a thin wisp of smoke. Nora whispers: "Come on… come on." (no subtitles)
3-6s: She sets the stones down, lowers her face close and blows gently, again and again; the red spot spreads; one small yellow flame appears on the moss.
6-8s: With trembling fingers she feeds three thin twigs onto the flame one by one; the twigs catch and a small fire burns on the bark, lighting her face warm orange. She stares at it, open-mouthed, silent.
[END-CLEAN]
Audio: two clicks of stone, soft repeated blowing, the hiss and crackle of catching moss and twigs, Nora's shaky breath.
```

### A2-08 · `duration: 8` · SEL · refs `["Nora","Nora Body","Cave Mouth"]`

```
The lens sits at the end of Nora's outstretched right arm, completely outside the visible frame and never seen; her right arm stays extended toward the lens for the entire clip, and she never reaches toward, touches, covers, taps, or points at the lens. Only her left hand is free. Handheld footage with natural wide-angle perspective, no exaggerated fisheye distortion; the frame shakes a little less as the clip goes on.
Setting: [SETTING-CAVE]
Everything is already in place from the very first frame: Nora kneels outside the entrance, close to the lens, from the chest up; just below the bottom of the frame burns her own small fire of twigs, its warm orange glow lighting her face and her raised left hand from below. No other person is in the frame; nothing appears suddenly, nothing vanishes.
Shot: close selfie; Nora's face in the centre, her left hand held palm-down over the unseen fire in the lower left.
[ID-LOCK]
The suede is still damp and darker at the sleeves and the hem, and thin steam rises from her left sleeve and fur cuff in the heat; the colour stays golden-tan and the shape never changes.
[HAIR]
0-3s: She holds her left hand over the fire, fingers spread; her shivering is still strong; thin steam drifts up from the wet sleeve.
3-6s: Her shivering eases; she closes her eyes for a moment and her lips tremble as if she might cry, but she says nothing.
6-8s: She opens her eyes, looks at the lens and lets out one long shaky breath that turns to vapor and dissipates rapidly. Nora does not speak in this clip.
[END-SELFIE]
Audio: the soft crackle of a small twig fire, Nora's slowing breath, wind.
```

### A2-09 · `duration: 8` · OTS · refs `["Nora","Nora Body","Leader","Cave Mouth"]`

```
The lens sits at the end of Nora's outstretched right arm, completely outside the visible frame and never seen; her right arm stays extended toward the lens for the entire clip, and she never reaches toward, touches, covers, taps, or points at the lens. Only her left hand is free, and it rests empty on her knee. Handheld footage with natural wide-angle perspective, no exaggerated fisheye distortion, steady.
Setting: [SETTING-CAVE]
Everything is already in place from the very first frame: Nora sits outside the entrance in the left third of the frame; her small twig fire burns low on the bark beside her. The Leader stands in the middle of the cave entrance about four metres behind her, looking at her fire. There is no metal anywhere. Exactly one Neanderthal and Nora are present; nobody appears suddenly, nobody vanishes.
Shot: over-the-shoulder selfie; Nora in the left third, the Leader framed in the entrance in the right two-thirds.
[NEANDERTHAL] [LEADER]
[ID-LOCK]
Her suede is almost dry now, only slightly darker at the hem.
The Leader's lips stay closed for the entire clip. Nora's lips stay closed for the entire clip as well; nobody speaks.
[HAIR]
0-3s: The Leader looks from her small fire to her face, expressionless.
3-6s: He takes one heavy step sideways, out of the middle of the entrance, leaving the way into the cave open.
6-8s: He jerks his head once toward the firelit inside. Nora looks at the open entrance, then at the lens, and breathes out slowly.
[END-SELFIE]
Audio: the low crackle of her fire, the bigger fire crackling inside the cave, wind dropping away. No voices.
```

### A2-10 · `duration: 8` · POV · refs `["Nora","Nora Body","Cave Mouth"]`

```
The view is Nora's own eyes; all recording gear is completely outside the visible frame, and her hands stay out of frame for the whole clip. Her face never appears. Natural wide-angle perspective, no exaggerated fisheye distortion; the view moves slowly like a person's eyes.
Setting: inside a low, wide limestone cave about 51,000 years ago, in a cold glacial winter; grey daylight from the entrance behind, warm firelight in front. In the centre of the earth floor, an open fire in a shallow sunken hearth ringed with stones in the earth floor; no fireplace, no chimney, no brick or built wall, no grate, no metal objects. Nothing modern exists anywhere.
Everything is already in place from the very first frame: beside the hearth stands one simple drying rack of three wooden poles lashed together with thongs; it is completely empty. About two metres away, one Neanderthal man with a thick bushy beard and a broad flat nose sits cross-legged on a hide, gnawing on a long bone that has already been picked clean. Behind the hearth, the injured man with a grey-streaked beard lies on hides with his left leg wrapped. Exactly two Neanderthals are in view; nobody appears suddenly, nobody vanishes.
Shot: first the empty rack in the centre, then the bearded man in the right third.
[NEANDERTHAL]
Both Neanderthals' lips stay closed for the entire clip; the only voice is Nora's.
0-3s: The view rests on the empty drying rack, firelight flickering on the bare poles.
3-6s: The view moves slowly to the bearded man, who scrapes his teeth along the bare bone and glances up at the view without expression.
6-8s: The view stays on him. Nora's voice says, low and flat: "No meat. I haven't eaten since I got here." (no subtitles)
[END-CLEAN]
Audio: the fire crackling, the scrape of teeth on bone, a faint stomach growl, wind at the entrance.
```

### A2-11 · `duration: 8` · OTS · refs `["Nora","Nora Body","Old Woman","Leader","Ember Bundle","Cave Mouth"]`

```
The lens sits at the end of Nora's outstretched right arm, completely outside the visible frame and never seen; her right arm stays extended toward the lens for the entire clip, and she never reaches toward, touches, covers, taps, or points at the lens. Only her left hand is free, and it rests empty on her knee. Handheld footage with natural wide-angle perspective, no exaggerated fisheye distortion, subtle hand shake.
Setting: inside a low, wide limestone cave about 51,000 years ago; warm firelight, grey daylight from the entrance. In the centre of the earth floor, an open fire in a shallow sunken hearth ringed with stones in the earth floor; no fireplace, no chimney, no brick or built wall, no grate, no metal objects. Nothing modern exists anywhere.
Everything is already in place from the very first frame: Nora sits by the hearth in the left third of the frame. On the right, the Old Woman kneels at the hearth with an open roll of birch bark lying on her thigh, lined inside with fresh green leaves, with a piece of dry hoof fungus and a little moss in it; she holds two thin sticks. The Leader kneels beside her, waiting. Exactly two Neanderthals and Nora are present; nobody appears suddenly, nobody vanishes.
Shot: over-the-shoulder selfie; Nora in the left third, the Old Woman's hands, the bark roll and the Leader in the right two-thirds.
[NEANDERTHAL] [OLD-WOMAN] [LEADER]
[ID-LOCK]
Every Neanderthal's lips stay closed for the entire clip; the only moving mouth in the frame is Nora's.
[HAIR]
0-3s: With the two sticks the Old Woman lifts one glowing ember from the edge of the hearth and sets it down gently on the hoof fungus inside the bark roll.
3-6s: She rolls the bark loosely closed, leaving one end open for air; only faint warmth and a thin thread of smoke rise from the opening; the bark does not burn. She hands it to the Leader; his big hand closes tight around it, and she presses his fingers looser, one by one.
6-8s: The Leader holds the roll gently against his chest. Nora watches, then turns to the lens. Nora says quietly: "Fire travels with them. Don't crush it." (no subtitles)
[END-SELFIE]
Audio: the crackle of the hearth, the dry rustle of birch bark, a soft click of sticks, low breathing.
```

---

## 7c. Nối cảnh Cold open → Act 2 (`transition_in` / `transition_out` / `join`)

Phần lớn là **CUT cứng cùng bối cảnh**: tư thế cuối clip A khớp tư thế đầu clip B (Rule 44). Không xoay 180°, không quay từ sau đầu (Rule 41/42).

| Mối nối | Cuối clip A | Đầu clip B | Join |
|---|---|---|---|
| MASTER(0–8s) → EST-01 | Chấm đỏ, khói, Nora nín thở | Thung lũng bình minh | **CUT ĐEN 0.5s**, rồi mở bằng tiếng gió |
| EST-01 → A1-01 | Chấm vàng bên bờ trái | Nora đứng mép bờ | CUT. J-cut tiếng suối vào sớm 0.5s |
| A1-01 → A1-02 | Quỳ run trên bờ | Quỳ run, máy đặt trên tảng đá | CUT, match on action (cùng tư thế quỳ). Cắt bỏ 1s đầu A1-02 |
| A1-02 → A1-03 | Nhìn bàn tay đỏ | Đứng, quay lưng về rừng | CUT. Âm cành gãy của A1-03 vào sớm 0.3s, đè lên cuối A1-02 |
| A1-03 → A1-04 | Im lặng, sáu người cách 6 m | Thủ Lĩnh cách 3 m | CUT (jump ngắn thời gian, cùng góc) |
| A1-04 → A1-05 | Câu thoại, run | Tay Thủ Lĩnh đã ở vai áo | CUT, cận hơn |
| A1-05 → A1-06 | Ông buông tay | Đi lên dốc theo nhóm | CUT |
| A1-06 → A1-07 | Bị chặn ở cửa | POV nhìn xuống dấu chân | CUT, match on action: ánh mắt cô hạ xuống đất |
| A1-07 → A1-08 | POV một dấu chân | Thủ Lĩnh trước mặt cầm hai viên đá | CUT |
| A1-08 → A1-09 | Nhìn rừng tối | Quỳ với hai viên đá | CUT, nhảy thời gian ngắn |
| A1-09 → A1-10 | Bốn người vào hang | Nora ngồi, Người Già trong cửa | CUT |
| A1-10 → A2-01 | "Okay." + im lặng | Người Già ngồi cạnh làm mẫu | CUT |
| A2-01 → A2-02 | Bà dập lửa, đặt đá xuống | Nora cầm đá, 4 nhúm rêu | CUT sang máy cố định |
| A2-02 → A2-03 → A2-05 | Đếm rêu 3 / 2 / 0 | Cùng góc máy cố định | CUT ngắn dần (7s → 6s → 5s), cắt A2-04 xen giữa A2-03 và A2-05 |
| A2-05 → A2-06 | Vỏ cây trống | Người Già quay lại | CUT |
| A2-06 → A2-07 | Nhìn túi da | Quỳ với rêu rắc bột | CUT sang máy cố định |
| A2-07 → A2-08 | Lửa cháy trên vỏ, nhìn trân trân | Cận mặt, hơ tay | CUT, giữ âm lửa liền |
| A2-08 → A2-09 | Thở ra dài | Thủ Lĩnh ở cửa hang | CUT, nhảy thời gian (lửa đã cháy thấp) |
| A2-09 → A2-10 | Nhìn vào cửa hang mở | POV trong hang | CUT, match on action: ánh mắt đi vào trong |
| A2-10 → A2-11 | POV người gặm xương | OTS bên bếp | CUT |
| A2-11 → A3-01 | Thủ Lĩnh ôm bọc than | Thủ Lĩnh chỉ người bị thương | CUT + card **HOUR 3** |

---

## 8. Nhịp dựng (story-engine §13b)

| Đoạn | Nhịp | Ghi chú |
|---|---|---|
| Cold open | Giữ trọn 8.0s, CUT ĐEN cứng | Không nhạc, chỉ tiếng thở và đá |
| EST-01 | Chậm, giữ đủ 6s | Thở sau cú cắt đen; chữ năm hiện 1–5s |
| A1-01 → A1-02 | Nhanh | Cắt bỏ 1s đầu A1-02 |
| A1-03 → A1-05 | Chậm | Giữ trọn nhịp im lặng sau "Don't run." |
| A1-08 | Giữ đủ | Mission card 6–8s |
| A2-02 → A2-05 | Ngắn dần: 7s → 6s → 5s | Chuỗi hỏng, mỗi lần đếm rêu |
| A2-07 → A2-08 | Chậm | Lửa đầu tiên, không nhạc |
| A3-03 | Giữ đủ | Im lặng căng 2s |
| A3-04 → A3-05 | Nhanh | Hành động |
| A3-06 → A3-09 | Trung bình | Thời gian trôi bằng bóng dài |
| A3-15 | Chậm | False victory, ấm |
| A4-06 → A4-08 | Dài | Căng |
| A4-09 → A4-12 | Ngắn → ngắn → ngắn | 6s → 5s → 5s → 6s |
| PAYOFF | Giữ trọn 4s | Âm thanh lửa bắt to lên |
| A4-14 | Dài | Thở sau payoff |
| A5-06 → A5-07 | Chậm | Giữ ambient; A5-07 cắt đen sau 2s im lặng cuối |

---

## 9. Material: ĐÃ TẠO 2026-10-05 (`GET /api/materials/prehistoric_vlog`)

**Vì sao không dùng `phone_vlog` nguyên trạng:** prefix của nó là `ultra-wide 0.5x front camera`, mâu thuẫn với các shot FIX/POV/drone của tập này và với bài học "không fisheye". Trong luồng R2V (không có `GENERATE_IMAGE`), `scene_prefix` không đi vào `video_prompt` (`agent/api/scenes.py:30-42`). Material chủ yếu tác động lúc **sinh ref** qua `style_instruction` và `negative_prompt`. Nên đây là chỗ khóa "người thật, không phải tượng sáp hay hóa trang".

```json
{
  "id": "prehistoric_vlog",
  "name": "Prehistoric Survival Vlog (Photoreal)",
  "style_instruction": "Photorealistic RAW photograph, natural available light only, real skin pores and weathered lived-in textures: frost, mud, soot, smoke, worn hide. Documentary realism.",
  "negative_prompt": "NOT 3D render, NOT CGI, NOT museum diorama, NOT wax figure, NOT costume or prosthetic makeup, NOT cosplay, NOT modern haircut, NOT clean white teeth, NOT fantasy, NOT cinematic color grade, NOT studio lighting, NO fisheye warping.",
  "scene_prefix": "Real handheld amateur footage frame, natural wide-angle perspective without fisheye distortion, documentary realism, prehistoric wilderness.",
  "lighting": "Soft even overcast daylight, natural colors"
}
```

- Không đưa ngoại hình nhân vật vào material (rule 2: ref lo việc đó).
- Dùng lại được cho mọi tập thời tiền sử (băng hà, đồ đá).
- Phương án thay thế: `realistic` (kiểu máy ảnh Canon, hơi "ảnh đẹp") hoặc `phone_vlog` (giữ nguyên tập 1).

---

## 10. Tự review theo story-engine §14

| Nhóm clip | Người xem hiểu | Có thể chưa hiểu → đã sửa bằng hình | Retention /10 |
|---|---|---|---|
| Cold open | Nguy hiểm ngay giây 0, ba con thú, đánh lửa đang hỏng | Vì sao cô ở đó? → cố ý để mở; bọc than chết nằm trong khung là đầu mối cho người xem tinh ý | 9 |
| A1-01 → A1-02 | Cô ướt, rét, không có gì để nhóm lửa | Vì sao không tự đốt lửa? → A1-02 cho thấy mọi cành đều đóng băng | 8.5 |
| A1-03 → A1-05 | Họ nghi ngờ, họ để ý đường may | "Stitches" có thể khó hiểu → ông nhìn tấm da của mình rồi nhìn đường may, so sánh bằng hình | 8.5 |
| A1-06 → A1-08 | Bị chặn, có linh cẩu, phải tự đánh lửa | Nhiệm vụ đọc được bằng chuỗi chỉ tay + mission card | 9 |
| A1-09 → A1-10 | Cô làm sai; được cho 4 nhúm rêu | Làm sao biết cô sai? → nhát nhanh của Thủ Lĩnh tương phản với nhát cạo chậm của cô | 8 |
| A2-01 → A2-05 | Kỹ thuật đúng, ba lần hỏng, mỗi lần mất rêu | Gieo bột: chỉ người tinh mắt thấy, có chủ đích | 8 |
| A2-06 → A2-11 | Bí quyết là bột sẫm; có lửa; vào hang; đói; bọc than | "Bột gì?" → cố ý không giải thích (persona không giảng) | 8.5 |
| A3-01 → A3-05 | Cô thay người bị thương; lỗi của cô; con hươu thoát | Nghe được lỗi bằng chuỗi sỏi lăn → hươu dậm chân → sủa | 9 |
| A3-06 → A3-11 | Lần dấu, ngày tắt, xẻ thịt, kho đá | Vì sao không mang hết? → gói thịt nặng ném vào cô, cô lảo đảo | 8 |
| A3-12 → A3-15 | Linh cẩu nghe/ngửi được; vệt máu dẫn tới kho; về hang | Mùi theo gió khó thấy → cỏ ngả về phía đông + Thủ Lĩnh ngửi gió; câu *"The blood…"* chốt ý | 8.5 |
| A4-01 → A4-05 | Nhóm sẽ đói; lỗi của cô; cô tự nhận việc; ngã đè bọc than | — | 9 |
| A4-06 → PAYOFF | Ba con, than chết, hai lần hỏng, rồi lửa | Nhận ra cold open? → hai nhát hỏng ở A4-10/11 khớp đúng master, nhát 3 là đoạn phát lại | 9.5 |
| A4-14 → A4-16 | Cả nhóm thắng; Người Mạnh Nhất ghi nhận; Thủ Lĩnh chấp nhận cô | — | 8.5 |
| Act 5 | Bữa ăn đầu tiên, mirror, lửa giữ được, tạm biệt | Đoạn sau payoff hơi dài (xem lỗi 4 bên dưới) | 7.5 |

**Ước lượng tổng: 8.6/10** (v4: 8.2).

### Lỗi logic tìm thấy khi review (đã sửa trong storyboard v5)
1. **Cơn đói lúc H8:** outline cho nướng thịt ở H8 mà mãi H12 cô mới "ăn lần đầu". Sửa: A3-15 thịt **vừa đặt lên lửa**; A4-01 tiếng whoop vang lên trước khi thịt chín, Người Già cất thịt đi để chia khẩu phần (*"…Or not."*). Bữa ăn H12 trở thành phần thưởng thật.
2. **Đếm rêu 4 → 0 không khớp:** outline có 3 lần hỏng nhưng 4 nhúm. Sửa: A2-05 cơn gió cuốn **cả hai nhúm cuối**.
3. **Hai cục pyrite:** cô đã có đá của Thủ Lĩnh từ A1-08, nên món quà pyrite ở cuối bị trùng. Sửa: A5-04 cô **trả đá lại** cho Thủ Lĩnh, A5-06 Người Già đi theo đưa **cục pyrite nhỏ của chính bà** (thay Đứa Bé, user bỏ nhân vật này 2026-10-05): người dạy cô đánh lửa trao cho cô viên đá riêng.
4. **Sau payoff dài 76s,** vượt mức 45–60s. **Đã sửa (user duyệt 2026-10-05):** bỏ A5-05 (4s), tiếng chân chạy theo chuyển vào 0–2s của A5-06 → còn 72s. Nếu dựng xong vẫn thấy dài: cắt thêm A4-16 hoặc A5-02 (→ 64s).
5. **Bếp lửa ở kho thịt:** cô lấy mồi và bột ở đâu? Sửa: A2-06 Người Già **để túi da lại** cho cô; A4-10 cô lấy từ túi đó. Đây là đạo cụ được gieo đúng cách, không gây câu hỏi "sao không dùng cái đó sớm hơn", vì bột chỉ là mồi, không thay được than đã mang theo.
6. **Số người Act 3:** đi săn là 7 Neanderthal + Nora (Leader, Strongest, A–E). Câu khóa số người viết theo số này.
7. **Act 4 #2:** trong hang có 9 Neanderthal (sau khi bỏ Đứa Bé). Câu thoại/hình ghi chín.
8. **Lửa mẫu của Người Già ở A2-01** (thêm khi viết prompt Act 2): nếu bà để lửa cháy, Nora chỉ việc mồi từ đó. Sửa: bà **dập tắt bằng đất** ngay sau khi lửa bắt. Thông điệp bằng hình: tự làm đi.
9. **Lửa trên rêu cháy vài giây là hết, mà A1-02 đã cho thấy mọi cành đều đóng băng.** Sửa: A2-06 Người Già để lại **bó que khô lấy từ trong hang** cùng túi da; A2-07 cô mồi ba que, A2-08 hơ tay trên lửa que.

### Checklist §10b cho các prompt Cold open + Act 1
- [x] Mỗi clip đúng một loại máy; thao tác hai tay đều dùng FIX (MASTER, A1-02, A1-09)
- [x] Không có từ chỉ thiết bị trong phần hình (phone, camera, selfie stick, device, screen). Chữ "ferro rod" chỉ nằm trong thoại; khung có câu "there is no metal anywhere"
- [x] Không có dòng `Negative:`
- [x] Linh cẩu có đặc điểm loài + câu loại trừ; mỗi con là một thân riêng
- [x] Đá chỉ rơi khi có tay thả; rêu chỉ bay khi có gió
- [x] POV (A1-07) có ref Nora + Nora Body, khóa mặt không bao giờ xuất hiện
- [x] Giáo của Người Mạnh Nhất có ref riêng ở A1-06 (các clip còn lại thiếu chỗ, nên tả bằng chữ)
- [x] Câu khóa miệng cho người phụ; Thủ Lĩnh nói trong sub-clip riêng, Nora im lặng lúc đó
- [x] Mọi clip có `Setting` + ánh sáng khớp clip kề
