# YouTube Thumbnail Guide — Hook-Worthy Design Rules (Pure Textless Cinematic Key Frame)

> [!CRITICAL]
> **QUY TẮC VÀNG (USER LOCK 24/10/2026 — TUYỆT ĐỐI KHÔNG CÓ CHỮ TRÊN THUMBNAIL):**
> - **ZERO TEXT ON THUMBNAIL (`strictly NO text, NO words, NO letters, NO typography, NO numbers, NO titles, NO logos, NO badges`)**: Khi tạo ảnh Thumbnail cho phim và video trên kênh, **TUYỆT ĐỐI KHÔNG đưa bất kỳ chữ viết nào lên ảnh Thumbnail** (không nhúng chữ vào prompt sinh ảnh và không chèn chữ bằng FFmpeg/Pillow).
> - **100% Pure Cinematic 35mm Movie Still (Chuẩn ZOVEN STUDIOS)**: Thumbnail phải là một **khung hình điện ảnh 35mm thuần khiết** (Movie Key Frame) giàu kịch tính, độ tương phản ánh sáng mạnh, kể trọn câu chuyện và gây tò mò tột độ chỉ bằng hình ảnh (nhân vật chính + phát hiện kỳ dị / hiểm họa trực diện + ánh sáng thực tế).

## Required Elements

| Element | Rule |
|---------|------|
| **Text** | **STRICTLY ZERO TEXT (0 words).** Never put any title, words, letters, numbers, or badges on the thumbnail. Always lock `strictly NO text, NO words, NO letters, NO typography, NO watermark` in the prompt |
| **Face & Subject** | 30-50% of frame. Authentic cinematic acting: shock, dread, intense focus, fear, or determination. Clear unobstructed face. Never neutral/calm |
| **Colors & Contrast** | High-contrast cinematic color grade: Teal/Cold Night Fog vs. Warm Amber Lantern/Torch/Bioluminescent Glow; Red/Orange Fire vs. Deep Abyssal Blue. High clarity, never flat or washed out |
| **Composition** | ONE clear narrative focal point (Two-Point Story Tension: Protagonist + The Mysterious Discovery / Threat). Rule of thirds, 35mm anamorphic depth (`f/8` deep focus) |
| **Lighting** | Dramatic practical lighting — lantern glow, torchlight, glowing artifact/creature, cold moonlight rim light, high-contrast chiaroscuro shadows |

## 6 Textless Cinematic Thumbnail Formulas (ZOVEN STUDIOS Style)

### Formula 1: The Discovery / Mystery Confrontation (Best for Sci-Fi / Fantasy / Adventure Films — ZOVEN STUDIOS Benchmark)
- Medium two-shot or over-the-shoulder cinematic framing: the protagonist holds a practical light source (lantern, torch, flashlight) illuminating a mysterious being, glowing creature, or ancient artifact in the dark.
- Strong warm-vs-cold color contrast (warm amber light on faces vs. cold teal/blue night fog or forest/sea).
- **Prompt pattern:** `35mm live-action cinematic movie frame, [PROTAGONIST] holding a glowing [LIGHT SOURCE], illuminating [MYSTERIOUS CHARACTER / CREATURE / ARTIFACT] in the darkness, intense dramatic expressions, warm amber light against cold dark teal fog, deep focus f/8, strictly NO text, NO words, NO letters, NO typography`

### Formula 2: Reaction & Partial Reveal (Best for Drama / Thrillers)
- Tight medium close-up of protagonist's face (40-50% of frame) with intense dread or awe, reacting to an ominous glowing or towering element in the foreground/background.
- **Prompt pattern:** `35mm cinematic close-up of [CHARACTER] face, [INTENSE EMOTION], illuminated by the eerie glow of [THREAT/OBJECT partially visible in frame], dramatic rim lighting, high contrast, strictly NO text, NO words, NO letters`

### Formula 3: Scale Contrast / Underdog vs. Behemoth (Best for Monster / Sea / Action Films)
- Two visually incompatible scales: human protagonist / wooden ship facing a colossal creature, monstrous wave, or impossible natural anomaly.
- **Prompt pattern:** `35mm anamorphic wide cinematic frame, [PROTAGONIST / VESSEL] facing [MASSIVE THREAT / GIANT CREATURE], extreme scale contrast, dramatic lighting, strictly NO text, NO words, NO letters`

### Formula 4: The Forbidden Object / Anatomy Reveal (Best for Mystery / Lore)
- Tightly framed group of characters gathered around a table/deck as a glowing object, ancient map, or opened creature reveals an impossible secret inside.
- **Prompt pattern:** `35mm cinematic medium shot, [CHARACTERS] gathered closely over [OPENED CREATURE / ARTIFACT], eerie bioluminescent or golden glow illuminating their stunned faces from below, dark atmospheric background, strictly NO text, NO words, NO letters`

### Formula 5: Stakes Frame / Surrounded in Peril (Best for Survival / Action)
- Single character in immediate physical peril against an overwhelming environment or threat.
- **Prompt pattern:** `35mm cinematic frame, [CHARACTER] bracing against [IMMINENT DANGER], wet weathered textures, dramatic practical lighting, high tension, strictly NO text, NO words, NO letters`

### Formula 6: Before/After Split Composition (Textless Visual Contrast)
- Pure visual split or foreground/background contrast without any labels or text.
- **Prompt pattern:** `35mm cinematic composition contrasting [NORMAL STATE] and [TRANSFORMED/DANGEROUS STATE], high contrast lighting, strictly NO text, NO words, NO letters`

## Psychology Hooks (Pick 1-2 — Pure Visual Storytelling)

1. **Curiosity Gap** — Show the shocking discovery or confrontation moment without giving away the ending (+50% CTR)
2. **Emotional Mirror** — Viewers instinctively mirror authentic human fear, awe, and urgency on the protagonist's face
3. **Stakes/Urgency** — Immediate visual danger or uncanny mystery that demands an explanation
4. **Warm vs. Cold Color Clash** — The human eye is immediately drawn to a warm amber/golden light source piercing a dark, cold blue/teal environment

## Genre: Narrative Film (`/fk-film`), Action, Sci-Fi & Dark Adventure

- **Zero Text:** **Strictly NO text, NO title, NO words, NO letters, NO numbers anywhere on the image.** Let the title (`[TITLE] | [Hook] | Full Movie 4K`) do the verbal hook while the thumbnail delivers a pure, theatrical movie still.
- **Character Consistency:** Always attach the approved entity reference UUIDs (`<Name>`, `<Name> Body`, `<Creature>`) so the faces, wardrobe, and creature anatomy match the film 100%.
- **Face & Acting:** Sweat, sea spray, rain, grit, intense eye line — never a posed portrait looking blankly at the lens unless dramatically motivated.
- **Colors:** Rich 35mm theatrical grading — deep shadows, cold cyan/teal night or fog, and a vivid practical accent light (amber lantern, torchfire, emerald/golden bioluminescence).
- **Watermark Removal:** Every generated thumbnail MUST be cleaned with `python tools/remove_watermark_from_image.py` before resizing to `1280x720`.

## Genre: Historical & Time-Travel Survival

- **Character & Emotion:** Protagonist face (35-45% of frame) showing breathless survival, adrenaline, or shock in period-accurate attire locked from entity references (`[Character]` + `[Character] Body`).
- **Immediate Threat:** Overwhelming danger or uncanny encounter clearly visible in frame (mammoth, ancient hunters, volcanic eruption, sea monster).
- **Zero Text:** **Strictly NO text, NO words, NO letters on the thumbnail** (User Lock 24/10/2026).

## Technical Specs

| Spec | Value |
|------|-------|
| Dimensions | 1280 x 720 px (16:9) |
| Design master | 1920 x 1080 px (cleaned via `remove_watermark_from_image.py`) |
| Text on image | **NONE (0 words — strictly textless)** |
| File format | PNG or JPG 85-90% |
| Max file size | 2 MB |
| Safe zone | Central 90% — keep key faces and focal discovery away from bottom-right corner (YouTube duration badge) |
| Mobile test | Subject + discovery/threat must be instantly recognizable at 120px wide without needing any text |

## AI Prompt Template (Pure Textless 35mm Key Frame)

When generating a thumbnail, apply in this order:

1. **Medium & Lens Lock:** `35mm live-action theatrical movie frame, Panavision anamorphic lens, deep focus f/8`
2. **Subject & Reference Lock:** Main character(s) and creature/prop locked to entity references, specifying exact facial expression and physical action
3. **Focal Discovery / Threat:** The mysterious being, creature, or glowing object that creates the curiosity gap
4. **Lighting & Color Contrast:** Warm practical light source (lantern, torch, bioluminescence) contrasting against cold atmospheric darkness/fog
5. **Composition:** Rule of thirds, clear silhouettes, nothing important in the bottom-right duration badge zone
6. **Negative Lock (MANDATORY):** `strictly NO text, NO words, NO letters, NO typography, NO titles, NO numbers, NO logos, NO watermarks, NO split-screen borders, NO 2D illustration`
