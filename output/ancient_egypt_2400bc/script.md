# Master Script: "I Time Traveled to Ancient Egypt in 2400 BC! (Vlog)"
**Target Format:** Long-form YouTube POV Vlog (16:9)  
**Total Scenes:** 49 scenes × 10s = 490s (~8 minutes 10 seconds)  
**Credits Budget:** ~735 credits baseline (with ~25% failure/regen margin = ~918 / 920 credits available)  
**Historical Era:** Ancient Egypt, Old Kingdom, 5th Dynasty (reign of Pharaoh Djedkare Isesi, c. 2400 BC)  
**Primary Locations:** Memphis (Ineb-Hedj), Saqqara Necropolis, Abu Gorab Sun Temple, Nile River, Giza Plateau View  

---

## 1. Project Assumptions & Technical Specs

- **Era & Setting:** Memphis, Nile River Valley, and Giza/Saqqara, Ancient Egypt, exactly 2400 BC (Old Kingdom, 5th Dynasty).
- **Duration & Scope:** 49 sequential 10-second scenes (Total: 490 seconds = 8m 10s).
- **Aspect Ratio:** HORIZONTAL 16:9 (`1280x720` raw generation $\rightarrow$ Review $\rightarrow$ Upscale to `1920x1080`).
- **Material Preset:** `phone_vlog` (custom smartphone vlog material) or `realistic` fallback.
- **Visual Style:** Handheld front-camera vlog footage, ultra-wide 0.5x lens, natural desert daylight, subtle organic hand shake, lens barrel distortion, documentary realism.
- **Camera Anchor Rule (Mục 11, Rule 23):** The camera IS the phone recording from Nora's hand. Absolutely NO floating phones, no phone screens, no phone bodies, no UI overlays, and no visible selfie sticks.
- **Audio & Voice:** Native in-video dialogue synthesized with Google Gemini **Achernar** voice profile (soft, conversational, expressive, breathy when amazed, hushed whisper when scared). No on-screen text or hardcoded subtitles.

---

## 2. Character Bible & Entity Locks (Rule 15 & Rule 24)

### Vlogger Character Lock (`Nora`) — Matched to Reference Image `F:\affilate\main.jpg`
```
CHARACTER_LOCK:
Nora, a 24-year-old female traveler with a soft oval face, warm hazel-green eyes with delicate dark lashes, natural fair radiant skin with a subtle soft rose blush on her cheeks, full soft pink glossy lips, and tiny gold hoop earrings. Her warm honey-blonde hair has parted curtain bangs elegantly framing her forehead and temples, gathered neatly into a high textured wavy ponytail with soft ends. She wears period-accurate Ancient Egyptian attire: an unbleached natural white translucent linen kalasiris sheath dress with dual shoulder straps, bare feet lightly dusted with golden desert sand. Her right arm extends toward the bottom-right corner holding the camera at arm's length.
Reference Source: F:\affilate\main.jpg (c:\flowkit\uploads\nora_main.jpg)
Voice: Achernar — soft, higher-pitched, natural expressive conversational female voice, casual vlog tone, breathy when amazed, hushed whisper when nervous.
```

### Visual Asset Lock (`Nora Outfit` — Bài học S31 Atlantis)
```
ENTITY_LOCK: Nora Outfit (visual_asset)
An era-accurate Old Kingdom 5th Dynasty Ancient Egyptian woman's dress: an unbleached natural white woven flax linen kalasiris sheath dress, ankle-length, form-fitting, supported by two wide shoulder straps, fine natural linen wrinkles and raw hem, accompanied by a small beaded collar of turquoise and faience beads.
```

### Supporting Entity Aliases (Role-Based Bypass per Rule 15)
- **`Ancient Egyptian Watchman` (NPC / Guard):** A tall, muscular bronze-skinned Egyptian guard with closely shaven head, stiff pleated linen triangular apron (*shendyt*), gripping an ox-hide covered wooden shield and a bronze battle axe lashed with raw rawhide to an acacia wood handle.
- **`The Grand Vizier` (Ptahhotep Alias):** A 62-year-old aristocratic Egyptian statesman with a trimmed short grey-streaked beard, short scholar wig of black wool, fine pleated ankle-length linen robe with a green serpentine amulet of Ma'at, holding an unrolled papyrus scroll and a reed pen.
- **`The Sun King` (Pharaoh Djedkare Isesi Alias):** A 45-year-old Egyptian monarch with sharp noble features, kohl-rimmed eyes, wearing the White Crown (Hedjet), a gold-embroidered royal shendyt with a ceremonial lion tail, and a massive gold-and-lapis lazuli usekh collar.
- **`Memphis Quay` (Location):** The bustling riverbank harbor of Memphis, whitewashed mudbrick storehouses, palm trees, stacks of woven grain baskets, papyrus skiffs, and large wooden cedar-planked trading barges.
- **`Abu Gorab Sun Temple` (Location):** The open-air solar sanctuary of Nyuserre Ini, featuring a colossal stone obelisk on a high truncated pyramid pedestal, and a central four-winged monolithic altar carved from translucent golden-yellow Egyptian alabaster.
- **`Giza Pristine Pyramids` (Location):** The Great Pyramids of Khufu and Khafre viewed from distance across the Nile valley, completely intact, sheathed in blindingly white polished Tura limestone with gleaming electrum capstones reflecting the sun.

---

## 3. Verified Research Facts & Beat Alignment

| # | Beat / Historical Topic | Verified Fact | Source & Confidence | Screen Translation |
|---|---|---|---|---|
| 1 | Setting & Dynasty | 5th Dynasty Old Kingdom, 2400 BC, Memphis capital | ARCE, Shaw ✅ | Mudbrick capital, "White Walls", bustling riverfront |
| 2 | No Coins (Barter & Deben) | Universal unit of account was the copper *Deben* (~91g) | Yale Ancient Money, Lehner ✅ | Nora trades a copper hairpin weighed on balance scales |
| 3 | Staples: Bread & Beer | Emmer sourdough (*t*) and thick unfiltered beer (*henket*) | British Museum, Samuel ✅ | Drinking thick beer through a hollow reed straw |
| 4 | No Camels / No Horses | Donkeys, oxen, and Nile boats only. Zero chariots. | Shaw, Oxford History ✅ | Pack donkeys carrying grain; no horses anywhere |
| 5 | Pristine White Pyramids | Giza pyramids were ~150 years old, clad in white Tura limestone | Lehner (*The Complete Pyramids*) ✅ | Blinding white pyramids with gold/electrum capstones |
| 6 | Abu Gorab Altar | Monolithic alabaster altar with 4 *hotep* arms | Borchardt, Verner ✅ | Nora touches the honey-colored alabaster altar |
| 7 | Hygiene & Toilets | Limestone toilet seats over sandboxes in wealthy homes | World History, Ikram ✅ | Nora observes limestone slab sanitation |
| 8 | Kohl Eyeliner | Galena and malachite eye paint for glare & infection | Forbes, Lucas ✅ | Local woman applying black kohl with an ivory stick |
| 9 | Wisdom of Ptahhotep | Grand Vizier active in 2400 BC writing *Sebayt* | Prisse Papyrus, Lichtheim ✅ | Vizier reading royal proclamation from a papyrus roll |

---

## 4. 7-Act Master Outline & Continuous Sequence Chains (49 Scenes × 10s = 490s)

Toàn bộ 49 cảnh được nhóm thành **16 Chuỗi Phân Đoạn Liền Mạch (Continuous Micro-Sequences)**. Trong mỗi chuỗi, cảnh A và cảnh B nối với nhau qua chuyển động có sẵn trong khung (Foreground Wipe, Swing, Look-away, Action Match, hoặc F2V). Giữa các Hồi dùng chuyển cảnh che khung lớn để cắt thẳng (Hard Cut) trong CapCut/Premiere mà không lộ vết cắt:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ HỒI 1: HOOK (0-5%) ── [2 cảnh: S01-S02]                                                │
│ └─ Chuỗi 1: Cú mở màn Wipe & Giới thiệu đường thủy sông Nile (S01 ➔ S02)              │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ HỒI 2: ĐỜI THƯỜNG DÂN SINH (5-40%) ── [17 cảnh: S03-S19]                               │
│ ├─ Chuỗi 2: Bước vào chợ & Sạp cá khô sông Nile (S03 ➔ S04)                            │
│ ├─ Chuỗi 3: Bánh mì Emmer & Vị ngọt quả sung (S05 ➔ S06 ➔ S07)                         │
│ ├─ Chuỗi 4: Đổi hàng Cân Deben & Uống bia quán cổ (S08 ➔ S09 ➔ S10 ➔ S11 ➔ S12)        │
│ ├─ Chuỗi 5: Xưởng ép giấy Papyrus ven sông (S13 ➔ S14)                                 │
│ └─ Chuỗi 6: Nhà ngõ mát, Bệ toilet đá vôi, Kohl mắt & Đoàn lừa thồ (S15 ➔ S16-S19)    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ HỒI 3: QUYỀN LỰC & CÔNG TRƯỜNG (40-55%) ── [8 cảnh: S20-S27]                           │
│ ├─ Chuỗi 7: Lính tuần rìu đồng & Lao dịch kéo đá trên cát ướt (S20 ➔ S24)             │
│ └─ Chuỗi 8: Quảng trường im phăng phắc & Tể Tướng Ptahhotep đọc chiếu chỉ (S25 ➔ S27) │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ HỒI 4: CAO TRÀO NGUY HIỂM (55-70%) ── [7 cảnh: S28-S34]                                │
│ └─ Chuỗi 9: CHUỖI RƯỢT ĐUỔI LIÊN TỤC 100% (Phát hiện ➔ Rượt ➔ Lật tỏi ➔ Nhảy thuyền)   │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ HỒI 5: HẠ NHỊP SÔNG NILE (70-75%) ── [3 cảnh: S35-S37]                                 │
│ └─ Chuỗi 10: Thuyền trôi êm đềm & Quả chà là ngọt lành của bác lái thuyền (S35 ➔ S37)  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ HỒI 6: DI SẢN KỲ QUAN (75-95%) ── [9 cảnh: S38-S46]                                    │
│ ├─ Chuỗi 11: Đền Mặt Trời Abu Gorab & Bàn thờ Alabaster mật ong (S38 ➔ S42)           │
│ └─ Chuỗi 12: Đại Kim Tự Tháp Giza trắng muốt nguyên bản & Nhân Sư đỏ tươi (S43 ➔ S46) │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ HỒI 7: KẾT TRẦM HOÀNG HÔN (95-100%) ── [3 cảnh: S47-S49]                               │
│ └─ Chuỗi 13: Một góc máy dựng cố định ── Tâm sự hoàng hôn & Bàn tay che ống kính       │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 5. Master Storyboard & Scene Specifications (Scenes 01 – 49)

### Act 1: The Hook (Scenes 01 – 02)
* **Scene 01 (S01) — The Wipe Entrance:**
  * *Shot:* Ultra-wide selfie 0.5x, arm extended bottom-right.
  * *Action:* 0-2s A bundle of dried papyrus reeds slides out of frame right very close to the lens, revealing Nora standing on the bustling earthen quay of Memphis; 2-8s Nora turns slightly, gasping in disbelief, eyes wide. 8-10s She leans into the mic.
  * *Dialogue:* Nora whispers breathlessly: *"Guys... I actually made it. This is Memphis, Ancient Egypt... exactly 2400 BC!"*
  * *Transitions:* In: Papyrus bundle wipe right $\rightarrow$ Out: Nora begins turning camera toward the water.
* **Scene 02 (S02) — The Nile Highway:**
  * *Shot:* Ultra-wide selfie panning toward the river.
  * *Action:* 0-3s Nora smoothly rotates the phone to show the river behind her; 3-8s The glittering Nile unfolds with dozens of papyrus skiffs and massive wooden cargo barges under the blazing sun; 8-10s Nora steps forward onto the dirt street.
  * *Dialogue:* Nora says: *"The Nile is their only highway. No cars, no roads—just endless wooden barges and donkeys."*
  * *Transitions:* In: Smooth rotation from S01 $\rightarrow$ Out: A walking merchant enters the left frame edge.

### Act 2: Daily Life & Sensory Beats (Scenes 03 – 19)
* **Scene 03 (S03) — The Market Stares:**
  * *Shot:* Walking selfie backward, low angle showing dirt road.
  * *Action:* 0-3s Nora walks backward cautiously; 3-8s Egyptian market vendors in plain white linen stop and stare curiously at her golden-blonde hair and curtain bangs; 8-10s She laughs nervously.
  * *Dialogue:* Nora says: *"Everyone is staring at my blonde hair, but thank god my linen dress blends right in."*
  * *Transitions:* In: Cut on forward motion $\rightarrow$ Out: Nora turns toward a food stall on the right.
* **Scene 04 (S04) — The Salted Nile Fish Stall:**
  * *Shot:* Handheld POV eye-level, Nora's left hand in lower frame.
  * *Action:* 0-4s Handheld camera pans across racks of split, salted Nile catfish drying in the desert sun; 4-8s Nora's hand gestures toward the glistening dried fish; 8-10s Flies buzz over the clay jars.
  * *Dialogue:* Nora whispers: *"Salted tilapia and catfish drying on reeds... the smell is intense, but this fed the whole empire."*
  * *Transitions:* In: Panning into stall $\rightarrow$ Out: Pan continues to adjacent bread ovens.
* **Scene 05 (S05) — Tactile POV: Emmer Bread:**
  * *Shot:* First-person POV, Nora's bare empty hands entering lower frame.
  * *Action:* 0-3s Nora's hands reach down and pick up a conical loaf of coarse emmer sourdough; 3-7s Her fingers press into the dark crust, breaking off a piece; 7-10s Tiny grains and stone mill grit crumble onto the woven mat.
  * *Dialogue:* Nora says: *"Feel this crust. It’s emmer wheat... heavy as a brick, and you can literally feel the stone grit."*
  * *Transitions:* In: Cut to close-up $\rightarrow$ Out: Baker hands her a basket.
* **Scene 06 (S06) — The Baker's Conical Ovens:**
  * *Shot:* Ultra-wide selfie with the conical clay ovens in background.
  * *Action:* 0-4s A bare-chested Egyptian baker shoves bread pots into glowing clay bell ovens; 4-8s Heat ripples shimmer in the air; Nora fans herself with one hand; 8-10s She steps toward the fruit section.
  * *Dialogue:* Nora says: *"They bake them inside preheated ceramic cones. It's like a 4,400-year-old pizza oven."*
  * *Transitions:* In: Baker's movement right $\rightarrow$ Out: Nora glances down at a fruit basket.
* **Scene 07 (S07) — Sweet Sycamore Figs:**
  * *Shot:* First-person POV, bare left hand in lower frame.
  * *Action:* 0-4s Nora's hand gently lifts a cluster of soft, wrinkled purple sycamore figs from a wicker bowl; 4-8s She turns a fig between thumb and forefinger; 8-10s Sand dust gently settles on the woven reeds.
  * *Dialogue:* Nora whispers: *"Fresh sycamore figs and dates... this was their only refined sugar back then."*
  * *Transitions:* In: Cut to basket $\rightarrow$ Out: Nora turns toward a balance scale.
* **Scene 08 (S08) — The Barter Transaction:**
  * *Shot:* Ultra-wide selfie showing merchant and bronze scale.
  * *Action:* 0-4s Nora approaches a merchant's stall with a small copper hairpin in her palm; 4-8s The merchant looks intrigued, reaching out with both hands; 8-10s He pulls out a wooden balance beam.
  * *Dialogue:* Nora says: *"Let's try buying some beer with this copper pin. Remember: no coins exist anywhere on earth!"*
  * *Transitions:* In: Approaching counter $\rightarrow$ Out: Merchant sets balance beam on table.
* **Scene 09 (S09) — Weighing the Deben:**
  * *Shot:* Close-up POV on wooden balance scale.
  * *Action:* 0-4s The merchant places a polished copper weight on one dish and Nora's hairpin on the other; 4-8s The dishes balance perfectly; 8-10s The merchant nods approvingly and hands over a clay jar.
  * *Dialogue:* Nora says: *"One deben of copper! Everything is priced by weight against copper or grain."*
  * *Transitions:* In: Focus on scales $\rightarrow$ Out: Merchant hands clay jar into Nora's hand.
* **Scene 10 (S10) — The Ancient Beer (Table-Propped Phone):**
  * *Shot:* Static frame, phone propped securely against a pottery bowl on the table facing Nora.
  * *Action:* 0-4s Nora sits cross-legged on a woven reed mat with a porous clay jar; 4-8s She dips a hollow reed straw into the thick, frothy beer and takes a sip; 8-10s Her eyes widen in taste surprise.
  * *Dialogue:* Nora says: *"Ancient beer, henket! It’s thick, hazy, and tastes like sour, yeasty honey porridge!"*
  * *Transitions:* In: Static cut to table $\rightarrow$ Out: Nora lowers the reed straw.
* **Scene 11 (S11) — The Nutrition of Beer:**
  * *Shot:* Static table-propped phone facing Nora.
  * *Action:* 0-3s Nora chuckles softly, swirling the straw in the jar; 3-8s In the background, laborers walk past carrying sacks of grain, chatting animatedly; 8-10s Nora picks up the phone from the table.
  * *Dialogue:* Nora says: *"It’s basically liquid bread. Full of B-vitamins, and way safer to drink than raw Nile water."*
  * *Transitions:* In: Continuation from S10 $\rightarrow$ Out: Nora's hand reaches for lens, swinging upward.
* **Scene 12 (S12) — The Blessing: "T-Henket":**
  * *Shot:* Ultra-wide selfie walking away from the beer tavern.
  * *Action:* 0-3s The tavern keeper waves from the stall, placing one hand over his chest; 3-7s Nora returns the gesture with a bright smile; 7-10s She turns back into the sunny alley.
  * *Dialogue:* The Tavern Keeper smiles: *"T-Henket, swnw!"* Nora says: *"He just blessed me with 'Bread and Beer!' The ultimate ancient compliment."*
  * *Transitions:* In: Handheld swing right $\rightarrow$ Out: Turning corner into papyrus district.
* **Scene 13 (S13) — Papyrus Workshop Entrance:**
  * *Shot:* Walking selfie along riverbank reed huts.
  * *Action:* 0-4s Nora walks past bundles of fresh, 10-foot-tall green papyrus stalks leaning against a sunbaked mud wall; 4-8s A craftsman strips outer green rind with a bronze scraper; 8-10s Nora leans in closer.
  * *Dialogue:* Nora whispers: *"We found the papyrus workshops right by the river. Look at the length of these stalks!"*
  * *Transitions:* In: Tracking shot $\rightarrow$ Out: Nora moves camera toward the craftsman's table.
* **Scene 14 (S14) — Papyrus Weaving POV:**
  * *Shot:* First-person POV, empty bare hand pointing.
  * *Action:* 0-4s Craftsman places sticky, translucent white pith strips side by side horizontally; 4-8s He lays a second vertical layer across them and pounds them gently with a wooden mallet; 8-10s Sap glazes the fiber.
  * *Dialogue:* Nora says: *"Horizontal strips, then vertical strips, hammered flat so the natural sap glues them together."*
  * *Transitions:* In: Close-up table $\rightarrow$ Out: Pan up toward the drying racks.
* **Scene 15 (S15) — Mudbrick Residential Alleys:**
  * *Shot:* Ultra-wide selfie walking through residential quarters of Memphis.
  * *Action:* 0-4s Nora walks down a narrow, sun-dappled alley flanked by towering whitewashed mudbrick walls; 4-8s Date palm fronds hang over wooden roof beams; 8-10s Nora notices an open wooden door.
  * *Dialogue:* Nora says: *"The walls are thick mudbrick plastered in white gypsum. Inside, it's shockingly cool."*
  * *Transitions:* In: Cut on forward stride $\rightarrow$ Out: Nora peeks through a wooden doorway.
* **Scene 16 (S16) — Sanitation & The Bronze Age Toilet (Humor Beat):**
  * *Shot:* Handheld peek through doorway, tight angle.
  * *Action:* 0-4s Nora points camera into an enclosed washroom: a carved limestone toilet seat with a keyhole slot set over a sand box; 4-8s Nora looks back at camera grinning; 8-10s She steps back into the street.
  * *Dialogue:* Nora whispers: *"You guys, look: a limestone toilet slab over a sandbox! Elite ancient sanitation in 2400 BC."*
  * *Transitions:* In: Peek through door $\rightarrow$ Out: Nora steps back into sunlight.
* **Scene 17 (S17) — Kohl Eye Makeup Ritual:**
  * *Shot:* Ultra-wide selfie with an Egyptian noblewoman seated in background.
  * *Action:* 0-4s An Egyptian lady dips a small ivory stick into a green glazed dish of dark galena powder; 4-8s She expertly lines her lower eyelid with thick black kohl; 8-10s Nora touches her own eyes.
  * *Dialogue:* Nora says: *"Kohl eyeliner isn't just vanity—crushed galena repels flies and blocks the burning desert sun glare."*
  * *Transitions:* In: Tracking past patio $\rightarrow$ Out: Panning toward an outdoor weaving loom.
* **Scene 18 (S18) — Flax Linen Weaving:**
  * *Shot:* Handheld mid-shot of a horizontal ground loom.
  * *Action:* 0-4s Two female weavers pass wooden shuttles through taut warp threads; 4-8s Gleaming white, feather-light linen fabric extends several yards across the sand; 8-10s Linen ripples in the breeze.
  * *Dialogue:* Nora says: *"Pure flax linen. No cotton, no silk—just ultra-fine linen woven so light it looks like gauze."*
  * *Transitions:* In: Loom close-up $\rightarrow$ Out: Two pack donkeys walk directly across lens from left to right.
* **Scene 19 (S19) — Donkey Caravan Wipe:**
  * *Shot:* Ultra-wide selfie as donkeys pass.
  * *Action:* 0-3s Nora pauses beside a mudbrick wall; 3-8s A train of pack donkeys laden with wicker baskets of grain passes right across the lens, momentarily obscuring the camera; 8-10s Nora steps into the open square.
  * *Dialogue:* Nora says: *"Donkeys everywhere... zero camels. If you see a camel in a 2400 BC movie, it's totally fake!"*
  * *Transitions:* In: Donkey flank wipe across lens $\rightarrow$ Out: Frame opens onto the administrative palace plaza.

### Act 3: Power, Statecraft & Scale (Scenes 20 – 27)
* **Scene 20 (S20) — Reveal #1: City Watchmen (Look-Away Reveal):**
  * *Shot:* Back of Nora's head fills left frame; she turns her head left, revealing the central avenue behind her.
  * *Action:* 0-3s Nora turns away from camera; 3-8s A disciplined squad of bronze-skinned Egyptian watchmen marches forward in matching linen kilts, carrying hide-covered shields; 8-10s Sunlight flashes off copper axe blades.
  * *Dialogue:* Nora hushed whisper: *"Look-away reveal... City watchmen. Look at those copper battleaxes and cowhide shields."*
  * *Transitions:* In: Nora's hair bun turns away $\rightarrow$ Out: Nora pulls back into the shadow of an acacia tree.
* **Scene 21 (S21) — Military Discipline in 2400 BC:**
  * *Shot:* Ultra-wide selfie, Nora tucked against an acacia trunk.
  * *Action:* 0-4s Nora glances nervously over her shoulder as guards march in sync; 4-8s Bronze battleaxe heads reflect harsh white light; 8-10s Nora lowers her voice to a tense whisper.
  * *Dialogue:* Nora whispers: *"No standing professional army yet, but these provincial guards are razor-sharp. Total discipline."*
  * *Transitions:* In: Shadow framing $\rightarrow$ Out: Panning right toward a monumental limestone gate.
* **Scene 22 (S22) — Royal Granary Sledges:**
  * *Shot:* Handheld mid-shot from side of avenue.
  * *Action:* 0-4s Four barefoot laborers drag a heavy wooden sledge laden with sacks of grain across wet, lubricated sand; 4-8s A scribe with a clay seal stamps the jars; 8-10s Wooden runners hiss over the sand.
  * *Dialogue:* Nora says: *"They don't use wheels for heavy loads—wooden sleds pulled over wet sand reduce friction by half!"*
  * *Transitions:* In: Tracking sledge motion $\rightarrow$ Out: Pan up toward the grand administrative portico.
* **Scene 23 (S23) — Overseer of Works:**
  * *Shot:* Ultra-wide selfie with overseer in background.
  * *Action:* 0-4s An imposing official in a starched triangular kilt holds a long wooden baton; 4-8s He shouts orders in resonant Old Egyptian, gesturing toward the Saqqara road; 8-10s Laborers hurry to comply.
  * *Dialogue:* Overseer shouts in Old Egyptian: *"Iry khet! Shemsu Ra!"* Nora says: *"The Overseer of Works... organizing stone cutters for the Saqqara necropolis."*
  * *Transitions:* In: Overseer pointing staff $\rightarrow$ Out: Camera follows his staff toward seated scribes.
* **Scene 24 (S24) — Scribes at Work (The Seated Scribes):**
  * *Shot:* First-person POV, waist level.
  * *Action:* 0-4s Three young scribes sit cross-legged on woven mats, holding rectangular wooden palettes with red and black ink wells; 4-8s Their reed pens glide smoothly across papyrus scrolls in rapid Hieratic script; 8-10s Nora leans closer.
  * *Dialogue:* Nora whispers: *"They’re writing in cursive Hieratic, not monumental hieroglyphs! Recording every single basket of grain."*
  * *Transitions:* In: Close on papyrus $\rightarrow$ Out: Scribes suddenly bow heads to the ground.
* **Scene 25 (S25) — Silence Falls on the Plaza:**
  * *Shot:* Ultra-wide selfie, Nora looking around in sudden tension.
  * *Action:* 0-4s The market chatter abruptly dies down; 4-8s Citizens, vendors, and laborers drop to their knees and press their palms to the dust in the Adoration pose; 8-10s Nora hastily drops down behind a pillar.
  * *Dialogue:* Nora whispers: *"Wait... everyone is dropping to their knees. Complete silence just hit the square."*
  * *Transitions:* In: Quick drop to knee $\rightarrow$ Out: Panning past pillar toward the palace gate.
* **Scene 26 (S26) — The Grand Vizier Appears:**
  * *Shot:* Telephoto handheld shot through palm fronds.
  * *Action:* 0-4s A dignified elder statesman with a short black scholar wig and long pleated white robe steps out onto the stone terrace; 4-8s He unrolls a crisp papyrus scroll held in both hands, wearing a green amulet of Ma'at; 8-10s Guards flank him motionless.
  * *Dialogue:* Nora hushed gasp: *"That’s the Grand Vizier himself... Ptahhotep! The man who wrote the earliest philosophy book in history!"*
  * *Transitions:* In: Framing between leaves $\rightarrow$ Out: The Vizier begins speaking.
* **Scene 27 (S27) — The Royal Decree of Djedkare:**
  * *Shot:* Mid-shot of Grand Vizier on terrace.
  * *Action:* 0-5s The Vizier recites the royal decree with resonant, measured cadence; 5-8s He raises his right hand to the sky; 8-10s The crowd bows in solemn reverence.
  * *Dialogue:* The Grand Vizier speaks in Old Egyptian: *"Djed-ef en Ra, Djedkare Ankh Djet!"* Nora whispers: *"He's declaring the royal mining expedition to the turquoise mountains of Sinai."*
  * *Transitions:* In: Vizier speaking $\rightarrow$ Out: A guard at the periphery suddenly turns his gaze toward Nora.

### Act 4: Peak Danger & The Chase (Scenes 28 – 34)
* **Scene 28 (S28) — The Phone Catches the Sun (The Spark):**
  * *Shot:* Ultra-wide selfie, Nora still crouching behind the pillar.
  * *Action:* 0-3s Nora leans slightly too far forward; 3-7s Sunlight strikes the glass lens and metal edge of her phone, casting a bright lens flare into the plaza; 7-10s A guard 30 feet away locks eyes directly onto the reflection.
  * *Dialogue:* Nora gasps: *"Oh no... the sun just caught the camera lens! That guard saw the glare!"*
  * *Transitions:* In: Lens flare pulse $\rightarrow$ Out: Guard points his bronze axe.
* **Scene 29 (S29) — The Accusation:**
  * *Shot:* Handheld shot from Nora's low vantage point.
  * *Action:* 0-3s The tall watchman steps forward aggressively, pointing his bronze axe straight toward Nora's pillar; 3-8s He shouts loudly, alerting two other guards; 8-10s He breaks into a fast march.
  * *Dialogue:* Guard shouts in Old Egyptian: *"Nem tey?! Iyi rek!"* Nora: *"He thinks this glowing device is black magic! TIME TO GO!"*
  * *Transitions:* In: Axe point $\rightarrow$ Out: Nora whips camera around and sprints.
* **Scene 30 (S30) — Sprint Through the Mudbrick Alley:**
  * *Shot:* Handheld front-camera sprint. Nora clutches the camera firmly in her right hand at arm's length pointed continuously at her face; the camera shakes violently with her sprint.
  * *Action:* 0-4s Nora runs full tilt down a narrow dirt alleyway; 4-8s Whitewashed mudbrick walls blur past behind her; heavy breathing and rapid footfalls echo off the walls; 8-10s Sand kicks up behind her.
  * *Dialogue:* Nora panting heavily: *"Run! In 2400 BC, an iPhone looks like demonic sorcery!"*
  * *Transitions:* In: Violent camera shake $\rightarrow$ Out: Rounding a sharp corner.
* **Scene 31 (S31) — The Reed Curtain Obstacle:**
  * *Shot:* Handheld running selfie.
  * *Action:* 0-3s Nora bursts through hanging reed screens, snapping cords and scattering dried papyrus leaves; 3-8s She glances back over her shoulder—two guards are sprinting around the corner 40 paces behind; 8-10s She pushes harder.
  * *Dialogue:* Nora gasps: *"They’re right behind me! Those guards are fast on barefoot sand!"*
  * *Transitions:* In: Reed curtain crash $\rightarrow$ Out: Bustling open bazaar ahead.
* **Scene 32 (S32) — The Garlic Cart Collision:**
  * *Shot:* Handheld running camera, dipping low.
  * *Action:* 0-4s Nora swerves sharply to avoid an old farmer carrying wicker baskets of onions and garlic; 4-8s The baskets tip, rolling dozens of white onions across the alley floor; 8-10s The pursuing guards stumble and curse in the background.
  * *Dialogue:* Nora pants: *"Sorry! So sorry! Oh thank god, onion barricade!"*
  * *Transitions:* In: Stumbling swerve $\rightarrow$ Out: The open blue water of the Nile appears ahead.
* **Scene 33 (S33) — The Leap Onto the River Skiff:**
  * *Shot:* Action Leap Physics. Nora clutches the camera tightly in her right hand; camera experiences a sharp physical vertical jolt as her feet slam onto wooden boat floorboards.
  * *Action:* 0-3s Nora sprints down the wooden quay embankment; 3-6s She leaps across 4 feet of open river water, landing firmly on the deck of a departing papyrus cargo skiff; 6-10s The wooden boat rocks heavily on river swells; Nora ducks low.
  * *Dialogue:* Nora gasping, adrenaline pumping: *"Push off! Push off! Please go!"*
  * *Transitions:* In: Heavy landing thud & water splash $\rightarrow$ Out: The shoreline begins drifting away.
* **Scene 34 (S34) — Watching the Shore Fade:**
  * *Shot:* Handheld selfie sitting on boat deck, looking toward receding shore.
  * *Action:* 0-4s Nora sits hunched against bundles of flax, clutching her knees; 4-8s On the distant quay, the three guards stop at the water's edge, brandishing axes in frustration; 8-10s Nora collapses back with relief.
  * *Dialogue:* Nora exhales deeply: *"We made it... They stopped at the water. Look at them on the bank."*
  * *Transitions:* In: Boat rocking gently $\rightarrow$ Out: Pan toward the open river horizon.

### Act 5: Decompression & Nile Drift (Scenes 35 – 37)
* **Scene 35 (S35) — Serenity on the Nile:**
  * *Shot:* Handheld ultra-wide selfie, camera resting on boat gunwale.
  * *Action:* 0-4s Nora leans against the woven papyrus bulwark, wind gently blowing loose copper tendrils of her hair; 4-8s Behind her, the wide, calm expanse of the blue Nile stretches out; white egrets soar overhead; 8-10s Deep silence except for water ripples.
  * *Dialogue:* Nora soft whisper: *"Everything just went completely silent. Look at this river... It's so peaceful."*
  * *Transitions:* In: Gentle water lap J-cut $\rightarrow$ Out: Nora turns toward the stern.
* **Scene 36 (S36) — The Old Boatman's Gift:**
  * *Shot:* Mid-shot of an elderly Egyptian boatman at the stern steering oar.
  * *Action:* 0-4s The weathered, dark-skinned boatman holds the steering paddle with one arm; 4-8s He smiles kindly with crinkled eyes and extends a small woven palm leaf pouch of dried fruits; 8-10s Nora reaches out.
  * *Dialogue:* Old Boatman in soft Old Egyptian: *"Wenet nefer, swnw."* Nora: *"He saw how terrified I was... He's offering me food."*
  * *Transitions:* In: Hand reaching into frame $\rightarrow$ Out: Close-up on Nora's hands.
* **Scene 37 (S37) — Tactile POV: Sharing Dates on Water:**
  * *Shot:* First-person POV, bare hand holding wrinkled dark date.
  * *Action:* 0-4s Nora's hand holds a plump, glossy brown date; 4-8s She bites into it, showing the sweet fibrous amber center; 8-10s Nile water droplets sparkle on the boat deck below.
  * *Dialogue:* Nora sighs with warmth: *"Pure honey date. 4,400 years ago, genuine human kindness was exactly the same as today."*
  * *Transitions:* In: Close on fruit $\rightarrow$ Out: Nora looks toward the distant western desert ridge.

### Act 6: Legacy & The Wonders of the Sun Kings (Scenes 38 – 46)
* **Scene 38 (S38) — Reveal #2: Approaching Abu Gorab:**
  * *Shot:* Ultra-wide selfie standing on boat bow, pointing toward western shore.
  * *Action:* 0-3s Nora stands up on the bow; 3-8s On a high desert plateau in the middle ground, the massive stone silhouette of the Sun Temple of Abu Gorab rises; 8-10s Nora's jaw drops.
  * *Dialogue:* Nora in awe: *"Look on the ridge ahead... That's the Sun Temple of Abu Gorab! Built by Pharaoh Nyuserre!"*
  * *Transitions:* In: Boat sliding past shore reeds $\rightarrow$ Out: Nora steps onto sandy river landing.
* **Scene 39 (S39) — The Ascent to the Solar Sanctuary:**
  * *Shot:* Walking selfie up a paved limestone causeway.
  * *Action:* 0-4s Nora hikes up an ancient limestone causeway cutting through golden sand dunes; 4-8s The colossal pedestal of the temple looms above her; heat waves shimmer over the stones; 8-10s Dust kicks up around her feet.
  * *Dialogue:* Nora says: *"Fifth Dynasty pharaohs were called the Sun Kings. They built massive temples purely dedicated to Ra."*
  * *Transitions:* In: Uphill walking stride $\rightarrow$ Out: Stepping through the massive granite entrance portal.
* **Scene 40 (S40) — The Open-Air Courtyard of Ra:**
  * *Shot:* Handheld 360-degree slow pan from where Nora stands in the center.
  * *Action:* 0-4s The blinding white open-air courtyard opens up, flooded with brilliant desert sun; 4-8s In the center stands a colossal squat stone obelisk on a 60-foot pyramid base; 8-10s Deep azure sky contrasts with limestone.
  * *Dialogue:* Nora whispers: *"An open-air sun courtyard... No dark ceilings, no shadows. Just pure, unadulterated sunlight."*
  * *Transitions:* In: Gateway shadow to blazing light $\rightarrow$ Out: Camera tracks toward the central alabaster altar.
* **Scene 41 (S41) — The "Wow" Detail: The Alabaster Altar:**
  * *Shot:* Ultra-wide selfie with the four-winged alabaster altar behind her.
  * *Action:* 0-4s Nora walks up to the monolithic circular altar; 4-8s Four massive blocks carved into the hieroglyph *hotep* radiate outward; 8-10s The yellow-white calcite stone glows translucently like frozen honey.
  * *Dialogue:* Nora says: *"Look at this altar! Carved from solid Egyptian alabaster... It literally glows like honey in the sun!"*
  * *Transitions:* In: Circling the altar $\rightarrow$ Out: Nora's hand reaches out to touch the stone.
* **Scene 42 (S42) — Tactile POV: Touching 4400-Year-Old Alabaster:**
  * *Shot:* First-person POV, bare left hand touching stone.
  * *Action:* 0-4s Nora's fingertips gently trace the carved outline of the *hotep* symbol on the silky-smooth stone surface; 4-8s Dust wipes away under her palm, revealing the crystalline mineral veins; 8-10s Silence except for desert wind.
  * *Dialogue:* Nora whispers in reverent awe: *"It’s ice-cold despite the blazing desert heat. The craftsmanship is flawless."*
  * *Transitions:* In: Close on stone texture $\rightarrow$ Out: Nora turns back toward the northern desert horizon.
* **Scene 43 (S43) — The Distant View of Giza:**
  * *Shot:* Ultra-wide selfie, Nora standing at the northern parapet of the temple.
  * *Action:* 0-4s Nora looks out across the 8 miles of desert plateau toward the north; 4-8s In the far distance, three razor-sharp white geometric shapes shimmer above the horizon; 8-10s Nora adjusts her gaze.
  * *Dialogue:* Nora says: *"And look north... across the desert plateau. Do you see what I see?"*
  * *Transitions:* In: Parapet framing $\rightarrow$ Out: Camera zooms in telephoto toward the northern pyramids.
* **Scene 44 (S44) — Reveal #3: The Great Pyramids in Pristine White:**
  * *Shot:* Telephoto shot from high ground looking at the Giza Plateau.
  * *Action:* 0-4s The Great Pyramid of Khufu and Pyramid of Khafre rise in monumental perfection; 4-8s Every inch of their casing is seamless, polished white Tura limestone gleaming like polished porcelain; 8-10s Not a single stone is broken or missing.
  * *Dialogue:* Nora gasps in pure wonder: *"The Great Pyramids! But they aren't weathered brown ruins... They are blinding, seamless white!"*
  * *Transitions:* In: Telephoto settle $\rightarrow$ Out: Zooming in tighter on Khufu's pyramidion.
* **Scene 45 (S45) — The Electrum Pyramidion:**
  * *Shot:* Extreme telephoto on the peak of Khufu's pyramid.
  * *Action:* 0-4s Sunlight strikes the capstone (*pyramidion*) at the apex; 4-8s The gold-silver electrum casing flares like a miniature sun, casting a beam of golden light across the desert floor; 8-10s Shimmering heat waves distort the sky.
  * *Dialogue:* Nora says: *"The very tip is clad in electrum—gold and silver! It literally acts as a beacon reflecting the sun for miles."*
  * *Transitions:* In: Flaring light pulse $\rightarrow$ Out: Panning down to the base of the plateau.
* **Scene 46 (S46) — The Painted Great Sphinx:**
  * *Shot:* Telephoto view across the causeway toward the Sphinx.
  * *Action:* 0-4s The Great Sphinx sits proud and fully intact; 4-8s Its face is freshly painted in rich terracotta-red ochre, wearing a striped yellow-and-blue nemes headdress and ceremonial braided beard; 8-10s Zero erosion on the body.
  * *Dialogue:* Nora whispers: *"The Sphinx has a nose, a beard, and its face is painted bright red ochre! It looks alive."*
  * *Transitions:* In: Sphinx portrait $\rightarrow$ Out: Pan right toward the setting sun over the dunes.

### Act 7: Sunset Sign-Off & Wrap (Scenes 47 – 49)
* **Scene 47 (S47) — The Propped Phone at Golden Hour:**
  * *Shot:* Static frame. The phone is propped securely against a flat desert sandstone slab facing Nora.
  * *Action:* 0-4s Nora sits with her knees pulled up on a high sandy ridge overlooking the Nile valley; 4-8s The late afternoon sun turns molten gold, casting long purple shadows from the distant pyramids; 8-10s Nora looks into the lens quietly.
  * *Dialogue:* Nora says softly: *"The sun is going down over the Sahara... and I have to find a way back."*
  * *Transitions:* In: Static cut to golden dunes $\rightarrow$ Out: Nora rests her chin on her knees.
* **Scene 48 (S48) — Philosophical Reflection on 2400 BC:**
  * *Shot:* Static frame, propped phone, warm crimson dusk glow on Nora's face.
  * *Action:* 0-4s Nora speaks with quiet emotion; 4-8s Behind her in the valley, small cooking fires send thin plumes of blue smoke from Memphis homes; 8-10s A distant temple horn sounds faintly.
  * *Dialogue:* Nora says: *"They didn’t build all this out of fear of death. They built it because they were obsessed with eternal life and light."*
  * *Transitions:* In: Continuation from S47 $\rightarrow$ Out: Nora reaches forward to tap the screen.
* **Scene 49 (S49) — The Sign-off & Final Horizon:**
  * *Shot:* Static frame, dusk settling into deep indigo and amber.
  * *Action:* 0-4s Nora smiles warmly and waves one hand at the camera; 4-8s She reaches forward with her hand filling the lower frame toward the lens; 8-10s Her palm gently covers the camera, fading the shot to dark indigo night.
  * *Dialogue:* Nora whispers: *"Memphis, 2400 BC... an unforgettable journey. See you guys in the next era. Bye."*
  * *Transitions:* In: Deep sunset glow $\rightarrow$ Out: Hand covers lens $\rightarrow$ Fade to black.

---

## 6. Physical Motion & Anti-Morphing Checklist (Mục 11, Quy tắc 21)

| Scene | Camera Placement & Aim | What is in Frame at 0s | Moving Objects: Direction, Speed, Effect | Real Physical Motion Details | Exit Method |
|---|---|---|---|---|---|
| **S01** | Ultra-wide selfie, arm bottom-right | Dried papyrus bundle covering 80% lens | Reeds slide out frame-right fast $\rightarrow$ reveals Nora & quay | Nora planted firmly on dirt quay; no boat rocking | Papyrus bundle exits right |
| **S02** | Rotating selfie, Nora walking | Nora face left-third, Nile background | Nora walks forward slowly; boats on river drift left | Natural walking bobbing gait (0.5x lens distortion) | Merchant steps into frame edge |
| **S05** | POV eye-level, looking down at table | Woven reed basket with bread loaves | Nora's bare hands reach down at 1s | Realistic tactile grip; crumbs crumble down | Hand pulls loaf toward chest |
| **S10** | Phone propped on pottery bowl | Nora seated cross-legged on reed mat | Laborers walk past slowly in far background | Static frame; liquid beer swirls in clay jar | Hand reaches for phone at 9s |
| **S20** | Back of Nora's head fills left frame | Back of Nora's hair bun & shoulder | Nora turns head away to reveal soldiers | Marching soldiers in locked step, dust rising | Nora ducks behind tree trunk |
| **S30** | Running selfie at arm's length | Nora face centered, wide terrified eyes | Nora sprinting full speed away from camera | Heavy violent camera shake; arm clutches phone tight | Sharp left turn down alley |
| **S33** | Action leap selfie | Nora mid-stride leaping toward boat | Boat deck rises to meet feet; water splashes | Heavy vertical jolt on landing; boat pitches on wave | Nora ducks low behind flax cargo |
| **S41** | Walking selfie around altar | Honey alabaster altar on right side | Nora circles clockwise slowly around altar | Altar stays completely stationary; stone reflects sun | Nora extends left hand to touch |
| **S47** | Phone propped on sandstone slab | Nora seated on sand, pyramids far back | Dust wind blowing loose hair tendrils | Static tripod-like framing; sun sinks slowly | Nora leans closer to lens |
| **S49** | Phone propped on sandstone slab | Nora face lit by amber sunset | Hand raises toward lens at 7s | Palm grows larger until covering entire lens | Hand completely blacks out frame |

---

## 7. FlowKit Batch Deployment Strategy (Phase A & Phase B)

1. **Entity Registration:**
   * Create Project `POST /api/projects` with `material: "phone_vlog"`.
   * Register Entities: `Nora`, `Nora Outfit`, `Ancient Egyptian Watchman`, `The Grand Vizier`, `Memphis Quay`, `Abu Gorab Altar`, `Giza Pristine Pyramids`.
2. **Reference Image Generation (`/fk-gen-refs`):**
   * Lock Nora's face and `Nora Outfit` into UUID `media_id`s before touching any scene.
3. **Phase A — Scene Frame 0 Generation:**
   * Submit 49 scene prompts (`GENERATE_IMAGE`).
   * Clean watermarks immediately (`tools/remove_watermark_from_image.py`).
   * Review on Image Review Board (`review_images.html`).
4. **Phase B — Omni Flash / Veo 3 Video Synthesis:**
   * Submit video batch in 7-Act clusters.
   * Auto-review via `/fk-review-video` on raw 720p clips.
   * Conditional Upscale to 1080p only on approved scenes.
5. **Final Concat (`/fk-concat`):**
   * Straight hard cuts on foreground wipes and motion blurs.
   * Continuous background ambient audio (desert wind, river laps, ancient market murmurs).
