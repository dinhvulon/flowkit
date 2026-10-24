Generate 4 YouTube-optimized **PURE TEXTLESS** cinematic thumbnail variants for a project video.

Usage: `/fk-thumbnail [project_id] [--provider <name>]`
## Provider (optional)

Usage: `/fk-thumbnail [project_id] [--provider <name>]`

Pass `"provider"` in the `generate-thumbnail` payload (`flow` | `assistant` |
`muse2api`; default is the server `DEFAULT_PROVIDER`). The assistant provider queues a
provider job — make sure a worker is running (see `/fk-provider`). Flow
thumbnail generation needs the Chrome extension; assistant needs none.

> [!CRITICAL]
> **QUY TẮC BẮT BUỘC 100% (USER LOCK 24/10/2026 — KHÔNG CÓ CHỮ TRÊN THUMBNAIL):**
> 1. **ZERO TEXT ON THUMBNAIL (`strictly NO text, NO words, NO letters, NO typography, NO titles, NO numbers, NO logos, NO badges`)**:
>    - **TUYỆT ĐỐI KHÔNG đưa bất kỳ chữ viết nào lên ảnh Thumbnail** (cấm nhúng chữ vào prompt sinh ảnh và cấm chèn chữ bằng FFmpeg `drawtext` hay Pillow).
>    - Mọi ảnh Thumbnail phải là **100% khung hình điện ảnh 35mm thuần khiết (Pure Textless Cinematic 35mm Movie Still — chuẩn ZOVEN STUDIOS)**: tập trung hoàn toàn vào nhân vật chính, nguồn sáng thực tế (đèn bão, đuốc, phát quang sinh học) và vật thể/sinh vật bí ẩn tạo độ tò mò cực đại.
> 2. **BẮT BUỘC tẩy watermark (`remove_watermark_from_image.py`) trước khi xuất bản 1280×720**:
>    - Mọi ảnh Thumbnail sinh từ Google Flow đều phải chạy `python tools/remove_watermark_from_image.py` để xóa logo ở góc dưới bên phải trước khi resize về `1280x720`.

## Step 1: Load project context

```bash
curl -s http://127.0.0.1:8100/api/projects/<PID>
curl -s "http://127.0.0.1:8100/api/videos?project_id=<PID>"
curl -s "http://127.0.0.1:8100/api/projects/<PID>/characters"
curl -s "http://127.0.0.1:8100/api/scenes?video_id=<VID>"
```

Extract and understand:
- **Story**: what is this film/video about? What is the core mystery, discovery, or life-or-death conflict?
- **Main character(s) & Creature/Prop**: who drives the story? Collect both `<Name>` and `<Name> Body` (Rule 46) plus any key creature/prop entity (`<Creature>`) that has a clean `media_id`.
- **Key visual hook moment**: what single frame makes a viewer stop scrolling and wonder *"What is that / What happens next?"*

## Step 2: Design 4 Pure Textless Cinematic Key-Frame Concepts (NO TEXT)

Every thumbnail variant must tell a clear visual story **without a single word of text**:

1. **Character & Body References (Rule 46)**: Bắt buộc đính kèm cả nhân vật (`[Character]`) và Body đã mặc trang phục (`[Character] Body`) cùng sinh vật/đạo cụ (`[Creature/Prop]`) từ entity references vào `character_names` (ví dụ `["Nora", "Nora Body", "Omen Fish"]`) để đảm bảo khuôn mặt, vóc dáng và bộ trang phục đồng nhất 100% với phim.
2. **Authentic 35mm Cinematic Expression & Blocking**: Khuôn mặt nhân vật chính chiếm 30–45% khung hình, lộ rõ 100% (`unobstructed face`), biểu cảm điện ảnh chân thực (kinh ngạc, căng thẳng, cảnh giác cao độ, ánh mắt khóa chặt vào phát hiện kỳ dị hoặc mối nguy trước mặt).
3. **Two-Point Visual Curiosity Gap (ZOVEN STUDIOS Style)**:
   - **Điểm 1 (Con người & Ánh sáng ấm)**: Nhân vật chính cầm nguồn sáng thực tế (đèn lồng đồng, đuốc, đèn pin) chiếu luồng sáng vàng cam ấm áp xuyên qua bóng tối.
   - **Điểm 2 (Phát hiện kỳ dị / Hiểm họa lạnh)**: Vật thể bí ẩn, sinh vật khổng lồ hoặc nhân vật bí ẩn hiện ra trong màn sương đêm xanh lạnh (teal/cyan) hoặc phát sáng kỳ dị (bioluminescent/golden glow).
4. **Zero Text Lock**: Luôn khóa ở cuối mọi prompt:
   `strictly NO text, NO words, NO letters, NO typography, NO titles, NO numbers, NO logos, NO watermarks, NO split-screen borders, NO 2D illustration`.

## Step 3: Build 4 thumbnail prompts (100% Textless 35mm Movie Stills)

**ALL prompts MUST include:**
1. `35mm live-action theatrical movie frame, Panavision anamorphic lens, deep focus (f/8 aperture)`
2. Character & creature names in `character_names` for 100% visual consistency
3. High-contrast warm-vs-cold dramatic lighting
4. Mandatory negative lock: `strictly NO text, NO words, NO letters, NO typography, NO titles, NO numbers, NO logos, NO watermarks`

### Prompt template:

```
[MATERIAL_PREFIX] 35mm live-action theatrical movie still, Panavision anamorphic lens, deep focus f/8,
[MAIN_CHARACTER_ACTION_AND_INTENSE_EXPRESSION],
[HOLDING_PRACTICAL_LIGHT_SOURCE_ILLUMINATING_DISCOVERY_OR_THREAT],
[CAMERA_ANGLE + RULE_OF_THIRDS_COMPOSITION],
[SETTING/ENVIRONMENT_WITH_ATMOSPHERIC_FOG_OR_SPRAY],
[HIGH_CONTRAST_WARM_AMBER_VS_COLD_TEAL_LIGHTING],
photorealistic 35mm film grain, rich shadow detail, theatrical color grading, 16:9 widescreen frame,
strictly NO text, NO words, NO letters, NO typography, NO titles, NO numbers, NO logos, NO watermarks, NO split-screen
```

### 4 Variants Example (Narrative Film `/fk-film` — ZOVEN STUDIOS Style):

**V1 — The Lantern Confrontation / Uncanny Discovery (ZOVEN STUDIOS Benchmark):**
Medium two-shot on a dark, fog-shrouded night. The protagonist holds up a glowing brass oil lantern in the left foreground, her rain-slicked face tense with shock and awe as the warm amber lantern light illuminates a mysterious discovery/being in the right mid-ground against cold teal night fog. Zero text.

**V2 — The Forbidden Anatomy / Glowing Secret Reveal:**
Dramatic high-angle medium close-up. The protagonist and first mate lean over a heavy timber table as a split-open abyssal creature or ancient chest emits an eerie golden-emerald bioluminescent glow from within, lighting their stunned, weathered faces from below. Zero text.

**V3 — Scale Contrast / Vessel Against the Abyssal Threat:**
Cinematic low-angle wide-medium frame. The protagonist stands at the wet timber rail holding a flickering lantern as a colossal silhouette or glowing anomaly rises just beneath the black ocean surface alongside the hull. Zero text.

**V4 — Extreme Close-Up Reaction & Foreground Peril:**
Tight 35mm close-up on the protagonist's eyes and weathered face (40% of frame) glistening with sea spray and amber firelight, staring in breathless dread at a glowing golden root or monstrous claw partially visible in the sharp foreground. Zero text.

## Step 4: Collect character refs

From entity list, include ALL main characters (`<Name>`, `<Name> Body`) and key creatures/props that have clean `media_id` in `character_names`.
This ensures faces, costumes, and creatures match the film 100%.

If character refs fail (400 error), retry without refs but warn user.

## Step 5: Generate 4 thumbnails & Clean Watermarks (Rule 28)

Generate sequentially, then **IMMEDIATELY remove the watermark** using `python tools/remove_watermark_from_image.py`:

```bash
# Get project output directory
PROJ_OUT=$(curl -s http://127.0.0.1:8100/api/projects/<PID>/output-dir)
OUTDIR=$(echo "$PROJ_OUT" | python3 -c "import sys,json; print(json.load(sys.stdin)['path'])")
mkdir -p "${OUTDIR}/thumbnails"

for i in 1 2 3 4; do
  curl -s -m 90 -X POST "http://127.0.0.1:8100/api/projects/<PID>/generate-thumbnail" \
    -H "Content-Type: application/json" \
    -d '{
      "prompt": "<textless_35mm_cinematic_variant_prompt>",
      "character_names": ["<main_char1>", "<main_char1 Body>", "<creature_or_char2>"],
      "aspect_ratio": "LANDSCAPE",
      "output_filename": "thumbnail_v'$i'.png",
      "provider": "flow"
    }'
  sleep 8
done
```

## Step 6: Remove Watermark & Resize to YouTube (1280x720, < 2MB)

```bash
for i in 1 2 3 4; do
  python tools/remove_watermark_from_image.py "${OUTDIR}/thumbnails/thumbnail_v${i}.png" -o "${OUTDIR}/thumbnails/thumbnail_v${i}_clean.png"
  rm -f "${OUTDIR}/thumbnails/thumbnail_v${i}.png"
  ffmpeg -y -i "${OUTDIR}/thumbnails/thumbnail_v${i}_clean.png" \
    -vf "scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2:color=black" \
    "${OUTDIR}/thumbnails/thumbnail_v${i}_yt.jpg" -q:v 2 2>/dev/null
done
```

## Step 7: Show all 4 and evaluate

Display all 4 cleaned thumbnails (`thumbnail_v*_yt.jpg`) using Read tool.

For EACH thumbnail, evaluate honestly:
- **Zero Text Check (CRITICAL)**: Is the image 100% free of any accidental text, letters, numbers, logos, or watermarks? (Any text on the image = FAIL -> regenerate immediately).
- **Character & Costume Fidelity**: Do the face and outfit match the film's approved entity references?
- **Focal Point & Lighting Contrast**: Is the warm-vs-cold contrast strong? Does the eye immediately lock onto the character's expression and the mysterious discovery/threat?
- **Curiosity Gap**: Would YOU click this movie on YouTube when paired with the `| Full Movie 4K` title?

Rate each: STRONG / OK / WEAK with reason.

Ask user: "Which one? 1-4, 'regenerate N', or 'all' to redo everything"

## Step 8: Output

```
Thumbnails for: <project> — <video_title>
Style: Pure Textless 35mm Cinematic Key Frame (ZOVEN STUDIOS style)
Character refs: <names used>

V1 (Lantern Confrontation): [RATING] — thumbnail_v1_yt.jpg
V2 (Glowing Discovery):     [RATING] — thumbnail_v2_yt.jpg
V3 (Scale & Peril):         [RATING] — thumbnail_v3_yt.jpg
V4 (Close-Up Reaction):     [RATING] — thumbnail_v4_yt.jpg

Files: ${OUTDIR}/thumbnails/thumbnail_v*_yt.jpg (1280x720, watermark-cleaned, zero text)
```
