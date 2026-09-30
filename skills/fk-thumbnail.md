Generate 4 YouTube-optimized thumbnail variants for a project video.

Usage: `/fk-thumbnail [project_id] [--provider <name>]`
## Provider (optional)

Usage: `/fk-thumbnail [project_id] [--provider <name>]`

Pass `"provider"` in the `generate-thumbnail` payload (`flow` | `assistant`;
default is the server `DEFAULT_PROVIDER`). The assistant provider queues a
provider job — make sure a worker is running (see `/fk-provider`). Flow
thumbnail generation needs the Chrome extension; assistant needs none.

## Step 1: Load project context

```bash
curl -s http://127.0.0.1:8100/api/projects/<PID>
curl -s "http://127.0.0.1:8100/api/videos?project_id=<PID>"
curl -s "http://127.0.0.1:8100/api/projects/<PID>/characters"
curl -s "http://127.0.0.1:8100/api/scenes?video_id=<VID>"
```

Extract and understand:
- **Story**: what is this video about? What is the conflict? What is at stake?
- **Main character(s)**: who drives the story? (must have media_id for refs)
- **Key conflict**: what dramatic moment defines the video?
- **Language**: match the project language for text on thumbnail

## Step 2: Create 2-LINE TEXT

Every thumbnail needs **2 lines of text**:

**Line 1 (HOOK):** 2-3 power words — emotion/urgency/shock
**Line 2 (CONTEXT):** 5-8 words — what the video is about, answers "why click?"

### Examples:
- Military: Line 1 = "IRAN TẤN CÔNG!" / Line 2 = "Hải Quân Mỹ Mắc Kẹt Eo Biển Tử Thần"
- Romance: Line 1 = "CÔ ẤY ĐÃ CHẾT?" / Line 2 = "Bí Mật Kinh Hoàng Sau Đám Cưới"
- Action: Line 1 = "KHÔNG AI SỐNG SÓT" / Line 2 = "Vụ Cướp Thế Kỷ Tại Ngân Hàng Trung Ương"
- Time-Travel / Historical POV Vlog (High-Stakes):
  - Option 1 (Nguy hiểm cận kề): Line 1 = "ALMOST TRAMPLED!" / Line 2 = "ICE AGE • 20,000 BC"
  - Option 2 (24 Giờ Sinh Tồn): Line 1 = "-40°C SURVIVAL!" / Line 2 = "24 HOURS WITH CAVEMEN"
  - Option 3 (Shock văn hóa): Line 1 = "THEY SAW FIRE!" / Line 2 = "20,000 BC CULTURE SHOCK"

### Rules:
- Both lines in project's language (LƯU Ý: Đối với POV / Time-Travel Vlogs, **bắt buộc dùng TIẾNG ANH** cho cả 2 dòng để tối ưu CTR quốc tế)
- Line 1: Provocative, uses urgent power words (ALMOST TRAMPLED, -40°C SURVIVAL, THEY SAW FIRE, BARELY ESCAPED, DON'T LOOK BACK, ATTACK, DEATH)
- Line 2: Gives context — Location & Era / Stakes (ICE AGE • 20,000 BC, 24H WITH CAVEMEN)
- Line 2 makes Line 1 specific: "ALMOST TRAMPLED!" + "ICE AGE • 20,000 BC" → viewer immediately understands the deadly stakes

### Mandatory Rules for Historical / Time-Travel POV Vlogs (BẮT BUỘC):
> [!CRITICAL]
> **CẤM THUMBNAIL KIỂU DU LỊCH NGẮM CẢNH HIỀN LÀNH**: Tuyệt đối không để vlogger mỉm cười tạo dáng hiền từ hoặc dùng text yếu ớt kiểu postcard (`ANCIENT EGYPT • 2400 BC / THE PYRAMIDS WERE BRAND NEW!`). Thumbnail phải toát lên cảm giác **Sinh Tồn Nghẹt Thở & Hiểm Họa Cận Kề**!

1. **Character & Outfit References**: Bắt buộc đính kèm cả nhân vật (`[Character]`) và trang phục (`[Character] Outfit`) từ entity references vào `character_names` (ví dụ `["Nora", "Nora Outfit"]`) để đảm bảo khuôn mặt và bộ trang phục cổ đại thời kỳ đó đồng nhất 100% với video.
2. **Extreme Facial Expression (Adrenaline / Terror / Shock)**: Mặt vlogger chiếm 35-45% khung hình, biểu cảm kinh hoàng tột độ hoặc adrenaline nghẹt thở (`extreme panic and adrenaline, wide eyes, panting breath, frost on eyelashes and eyebrows, flushed cheeks from -40°C blizzard`).
3. **Imminent Threat & Overwhelming Danger**: Phải có mối đe dọa sinh tử áp sát trong khung hình (chân voi ma mút khổng lồ giẫm tuyết ngay góc máy, cặp ngà xoắn 4m quét sát lưng, thợ săn tiền sử bao vây chĩa giáo đá, bão tuyết gầm thét).
4. **Text on Thumbnail in ENGLISH (Mandatory High-Stakes)**: Bắt buộc hiển thị chữ TIẾNG ANH nổi bật ở nửa trên thumbnail:
   - **Line 1 (Urgent Hook / Shock / Danger)**: 2-3 từ in hoa cực gắt, font dày đậm (bold yellow hoặc fiery orange/red with black outline): `ALMOST TRAMPLED!`, `-40°C SURVIVAL!`, `THEY SAW FIRE!`, `DON'T LOOK BACK!`.
   - **Line 2 (Location & Era Context)**: 3-5 từ màu trắng in hoa có bóng đổ đen dày: `ICE AGE • 20,000 BC`, `24 HOURS WITH CAVEMEN`, `20,000 BC CULTURE SHOCK`.
   - Vị trí: Upper half (tránh góc dưới bên phải vì dính badge thời lượng YouTube).

## Step 3: Build 4 thumbnail prompts

**ALL prompts MUST include:**
1. The hook text as bold text IN the image (not overlay)
2. Character names in `character_names` for face consistency
3. The project's material style prefix

### Non-English Text (CRITICAL)

For non-English text (Vietnamese, etc.), use the **language hint pattern** in prompts:
```
bold [COLOR] text in [LANGUAGE] clearly "[TEXT WITH DIACRITICS]" at [POSITION]
```

Example:
```
bold yellow text in Vietnamese clearly "IRAN TẤN CÔNG!" at top center in thick sans-serif font with red outline,
smaller white text in Vietnamese clearly "HẢI QUÂN MỸ MẮC KẸT EO BIỂN TỬ THẦN" below in bold font with shadow
```

**Without "in [Language] clearly":** Google Flow returns "invalid argument" for diacritical characters.

### Prompt template:

```
[MATERIAL_PREFIX] YouTube thumbnail,
bold [COLOR1] text in [LANGUAGE] clearly "[LINE1_HOOK]" at [POSITION] in thick sans-serif font with [OUTLINE_COLOR] outline,
smaller [COLOR2] text in [LANGUAGE] clearly "[LINE2_CONTEXT]" below in bold font with [SHADOW] shadow,
[MAIN_SUBJECT + EMOTION + ACTION],
[CAMERA_ANGLE + COMPOSITION],
[SETTING/ENVIRONMENT],
[LIGHTING + COLOR_PALETTE],
4K, 8K, masterpiece, highly detailed, sharp focus, HDR,
1280x720, 16:9 YouTube thumbnail format
```

### 4 variants for Time-Travel / Historical POV Vlog (High-Stakes):

**V1 — Immediate Peril (Nguy hiểm cận kề - Mammoth Trample):**
Low-angle handheld POV. Nora's face takes up 40% of frame, frozen in sheer adrenaline terror, wide eyes, panting breath with frost on eyelashes. Looming directly above/behind her is the colossal shaggy foot of a 6-ton woolly mammoth about to stomp down into spraying snow.
Text: bold yellow "ALMOST TRAMPLED!" at top-left, white "ICE AGE • 20,000 BC" below.

**V2 — 24H Extreme Survival (Format 24 Giờ Sinh Tồn -40°C):**
Nora shivering in a howling blizzard at dusk, face flushed and iced, wrapped in mammoth-wool parka with snow clinging to hood. In background, a massive Mezhirich mammoth-bone hut glows with faint orange embers, prehistoric hunters visible in doorway.
Text: bold cyan/yellow "-40°C SURVIVAL!" at top, white "24 HOURS WITH CAVEMEN" below.

**V3 — Culture Shock & Standoff (Shock văn hóa - Ngọn lửa hiện đại):**
Dramatic night contrast. Nora holds up a modern flame/torch glowing fiercely. The firelight illuminates the stunned, alarmed faces of Cromagnon hunters holding flint spears in defensive stance, eyes wide in disbelief at the sudden light.
Text: bold fiery orange "THEY SAW FIRE!" at top-center, white "20,000 BC CULTURE SHOCK" below.

**V4 — Sprint for Life (Chạy tháo thân trên tuyết):**
High-action running perspective. Nora sprints towards camera through knee-deep snow, looking back over shoulder in desperation. In background, an enraged bull mammoth charges with sweeping 4-meter tusks, snow kicking up in violent clouds.
Text: bold red/yellow "DON'T LOOK BACK!" at top-right, white "BARELY ESCAPED • 20,000 BC" below.

## Step 4: Collect character refs

From entity list, include ALL main characters that have `media_id` in `character_names`.
This ensures faces match the video — critical for channel consistency.

If character refs fail (400 error), retry without refs but warn user.

## Step 5: Generate 4 thumbnails

SEQUENTIALLY with 8s cooldown between each:

```bash
# Get project output directory
PROJ_OUT=$(curl -s http://127.0.0.1:8100/api/projects/<PID>/output-dir)
OUTDIR=$(echo "$PROJ_OUT" | python3 -c "import sys,json; print(json.load(sys.stdin)['path'])")
mkdir -p "${OUTDIR}/thumbnails"

for i in 1 2 3 4; do
  curl -s -m 90 -X POST "http://127.0.0.1:8100/api/projects/<PID>/generate-thumbnail" \
    -H "Content-Type: application/json" \
    -d '{
      "prompt": "<variant_prompt_with_text_embedded>",
      "character_names": ["<main_char1>", "<main_char2>"],
      "aspect_ratio": "LANDSCAPE",
      "output_filename": "thumbnail_v'$i'.png",
      "provider": "assistant"  // or "flow"; omit for server default
    }'
  sleep 8
done
```

If reCAPTCHA fails: retry that variant once.
If 400 (missing refs): retry without character_names.

## Step 6: Resize to YouTube (1280x720)

```bash
for i in 1 2 3 4; do
  ffmpeg -y -i "${OUTDIR}/thumbnails/thumbnail_v${i}.png" \
    -vf "scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2:color=black" \
    "${OUTDIR}/thumbnails/thumbnail_v${i}_yt.png" 2>/dev/null
done
```

## Step 7: Show all 4 and evaluate

Display all 4 thumbnails using Read tool.

For EACH thumbnail, evaluate honestly:
- Is the text readable? Bold enough? Well-positioned?
- Is the face big enough (30-50% of frame)?
- Is the emotion extreme (not neutral)?
- Are colors bright and saturated (not dark/muted)?
- Would YOU click this on YouTube?
- Does it create curiosity — what happens next?

Rate each: STRONG / OK / WEAK with reason.

Ask user: "Which one? 1-4, 'regenerate N', or 'all' to redo everything"

## Step 8: Output

```
Thumbnails for: <project> — <video_title>
Hook text: <the hook words used>
Character refs: <names used>

V1 (Face+Text): [RATING] — thumbnail_v1_yt.png
V2 (Action+Text): [RATING] — thumbnail_v2_yt.png  
V3 (Confrontation+Text): [RATING] — thumbnail_v3_yt.png
V4 (Mystery+Text): [RATING] — thumbnail_v4_yt.png

Files: ${OUTDIR}/thumbnails/thumbnail_v*_yt.png (1280x720)
```
