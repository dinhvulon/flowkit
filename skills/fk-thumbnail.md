Generate 4 YouTube-optimized thumbnail variants for a project video.

Usage: `/fk-thumbnail [project_id] [--provider <name>]`
## Provider (optional)

Usage: `/fk-thumbnail [project_id] [--provider <name>]`

Pass `"provider"` in the `generate-thumbnail` payload (`flow` | `assistant` |
`muse2api`; default is the server `DEFAULT_PROVIDER`). The assistant provider queues a
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
- **Language**: text on thumbnail = **ngôn ngữ thoại của video** (CLAUDE.md Rule 20). Thoại tiếng Tây Ban Nha → đọc mục "Tiếng Tây Ban Nha (es-419)" cuối file

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
  - Option 2 (Sinh tồn): Line 1 = "LET ME IN?" / Line 2 = "24 HOURS WITH CAVEMEN" hoặc "NEANDERTHALS • 51,000 YEARS AGO"
  - Option 3 (Shock văn hóa): Line 1 = "THEY SAW FIRE!" / Line 2 = "20,000 BC CULTURE SHOCK"

### Rules:
- Both lines in the **dialogue language** (Rule 20): thoại tiếng Anh → chữ tiếng Anh; thoại tiếng Tây Ban Nha → chữ tiếng Tây Ban Nha Mỹ Latinh; thoại tiếng Nhật → chữ tiếng Nhật. Không dùng tiếng Anh cho video thoại ngôn ngữ khác, kể cả POV vlog
- Chữ thumbnail **bổ sung** cho tiêu đề, không lặp lại nguyên câu tiêu đề
- Line 1: Provocative, uses urgent power words (ALMOST TRAMPLED, -40°C SURVIVAL, THEY SAW FIRE, BARELY ESCAPED, DON'T LOOK BACK, ATTACK, DEATH)
- Line 2: Gives context — People/Era/Stakes (ICE AGE • 20,000 BC, NEANDERTHALS • 51,000 YEARS AGO, 24 HOURS WITH CAVEMEN). "24 HOURS WITH CAVEMEN" được dùng trên thumbnail (user chốt 2026-10-06) khi video có countdown đủ 24 giờ; tiêu đề thì không dùng "I Survived 24 Hours" (xem `/fk-youtube-seo`)
- Line 2 makes Line 1 specific: "ALMOST TRAMPLED!" + "ICE AGE • 20,000 BC" → viewer immediately understands the deadly stakes

### Mandatory Rules for Historical / Time-Travel POV Vlogs (BẮT BUỘC):
> [!CRITICAL]
> **CẤM THUMBNAIL KIỂU DU LỊCH NGẮM CẢNH HIỀN LÀNH**: Tuyệt đối không để vlogger mỉm cười tạo dáng hiền từ hoặc dùng text yếu ớt kiểu postcard (`ANCIENT EGYPT • 2400 BC / THE PYRAMIDS WERE BRAND NEW!`). Thumbnail phải toát lên cảm giác **Sinh Tồn Nghẹt Thở & Hiểm Họa Cận Kề**!

1. **Character & Body References**: Bắt buộc đính kèm cả nhân vật (`[Character]`) và Body đã mặc trang phục (`[Character] Body` theo Rule 46) từ entity references vào `character_names` (ví dụ `["Nora", "Nora Body"]`) để đảm bảo khuôn mặt, vóc dáng và bộ trang phục cổ đại thời kỳ đó đồng nhất 100% với video.
2. **Extreme Facial Expression (Adrenaline / Terror / Shock)**: Mặt vlogger chiếm 35-45% khung hình, biểu cảm kinh hoàng tột độ hoặc adrenaline nghẹt thở (`extreme panic and adrenaline, wide eyes, panting breath, frost on eyelashes and eyebrows, flushed cheeks from -40°C blizzard`).
3. **Imminent Threat & Overwhelming Danger**: Phải có mối đe dọa sinh tử áp sát trong khung hình (chân voi ma mút khổng lồ giẫm tuyết ngay góc máy, cặp ngà xoắn 4m quét sát lưng, thợ săn tiền sử bao vây chĩa giáo đá, bão tuyết gầm thét).
4. **Text on Thumbnail (Mandatory High-Stakes, ngôn ngữ thoại — Rule 20)**: Bắt buộc hiển thị chữ nổi bật ở nửa trên thumbnail. Ví dụ dưới đây là bản tiếng Anh; bản tiếng Tây Ban Nha ở mục es-419 cuối file:
   - **Line 1 (Urgent Hook / Shock / Danger)**: 2-3 từ in hoa cực gắt, font dày đậm (bold yellow hoặc fiery orange/red with black outline): `ALMOST TRAMPLED!`, `-40°C SURVIVAL!`, `THEY SAW FIRE!`, `DON'T LOOK BACK!`.
   - **Line 2 (Location & Era Context)**: 3-5 từ màu trắng in hoa có bóng đổ đen dày: `ICE AGE • 20,000 BC`, `24 HOURS WITH CAVEMEN`, `NEANDERTHALS • 51,000 YEARS AGO`, `20,000 BC CULTURE SHOCK`.
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

Spanish:
```
bold yellow text in Spanish clearly "¡CASI ME APLASTA!" at top-left in thick sans-serif font with black outline,
smaller white text in Spanish clearly "EDAD DE HIELO • 20,000 A. C." below in bold font with heavy black shadow
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

**V2 — Survival Question (Câu hỏi sinh tồn — bị chặn ở cửa hang):**
Nora shivering at dusk outside a glowing cave mouth, face flushed and iced, looking up in desperate hope. A towering Neanderthal hunter blocks the entrance, arm across the opening, firelight behind him.
Text: bold cyan/yellow "LET ME IN?" at top, white "24 HOURS WITH CAVEMEN" (hoặc "NEANDERTHALS • 51,000 YEARS AGO") below.
Cảnh trên thumbnail phải có trong video (Spam Policy — Malicious clickbait).

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
- Is the text spelled exactly right, letter by letter? Non-English text: every accent, `Ñ`, `¿ ¡` (Spanish), diacritic (Vietnamese) present and in place. One wrong or missing mark = WEAK; fix theo mục es-419 "Model vẽ sai chữ"
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

## Tiếng Tây Ban Nha (es-419) — Mexico & Mỹ Latinh

Dùng khi thoại là tiếng Tây Ban Nha Mỹ Latinh (cùng project với `/fk-youtube-seo --language es`). Research 2026-10-13: RAE (chính tả chữ in hoa), các hướng dẫn thumbnail tiếng Tây Ban Nha, các bài test khả năng vẽ chữ có dấu của model ảnh.

### 4 cặp chữ cho POV vlog (theo 4 variant ở Step 3)

| Variant | Line 1 (hook) | Line 2 (bối cảnh) |
|---|---|---|
| V1 — Nguy hiểm cận kề | `¡CASI ME APLASTA!` | `EDAD DE HIELO • 20,000 A. C.` |
| V2 — Câu hỏi sinh tồn | `¿ME DEJAN ENTRAR?` | `NEANDERTALES • HACE 51,000 AÑOS` (hoặc `24 HORAS CON CAVERNÍCOLAS` khi video có countdown đủ 24 giờ) |
| V3 — Shock văn hóa | `¡VIERON EL FUEGO!` | `CHOQUE CULTURAL • 20,000 A. C.` |
| V4 — Chạy thoát | `¡NO MIRES ATRÁS!` | `ESCAPÉ POR POCO • 20,000 A. C.` |

Ví dụ là cho vlog Kỷ Băng Hà; đổi theo đúng mối nguy có trong video (Spam Policy).

### Luật chữ

- **Ngắn hơn bản tiếng Anh.** Tiếng Tây Ban Nha dài hơn ~15–20%. Các hướng dẫn thumbnail tiếng Tây Ban Nha khuyên tổng 3–5 từ, đọc được ở cỡ thumbnail trên điện thoại. Line 1 tối đa 3 từ; Line 2 tối đa 5 từ kể cả niên đại.
- **Chữ in hoa vẫn phải có dấu**: `ATRÁS`, `ESCAPÉ`, `CAVERNÍCOLAS`, `AÑOS`. Theo RAE, luật dấu áp dụng cho mọi chữ, in hoa hay không; chỉ từ viết tắt in hoa toàn bộ mới bỏ dấu. Bỏ dấu trên chữ in hoa là lỗi chính tả mà khán giả nói tiếng Tây Ban Nha nhận ra ngay.
- **Câu hỏi và câu cảm thán có cả dấu mở lẫn dấu đóng**: `¿…?`, `¡…!`.
- **Từ Mỹ Latinh**, giống `/fk-youtube-seo`: `ENCENDEDOR` (không `MECHERO`), `CELULAR` (không `MÓVIL`).
- **Số và niên đại** giống tiêu đề: Mexico `20,000`, Nam Mỹ `20.000`; `A. C.` / `D. C.`. Giữ thống nhất với tiêu đề của chính video đó.
- Không chửi thề, kể cả từ đã bíp trong video (checklist Studio của `/fk-youtube-seo`).

### Prompt

Dùng mẫu `text in Spanish clearly "..."` ở mục Non-English Text: đủ dấu, đủ `¿ ¡`, viết in hoa sẵn trong ngoặc kép.

### Model vẽ sai chữ → xử lý thế nào

Khả năng model ảnh vẽ chữ có dấu chưa được kiểm chứng cho tiếng Tây Ban Nha. Một bài test so sánh thấy Nano Banana Pro đôi khi làm rơi hoặc đặt lệch dấu (`CAFÉ RÉSUMÉ`), và không bài nào test `Ñ`, `¿`, `¡`. Vì vậy:

1. **Soi từng ký tự** ở Step 7 (`Á É Í Ó Ú Ñ ¿ ¡`). Sai một dấu = WEAK.
2. **Ưu tiên chữ không dấu cho Line 1** khi hai lựa chọn mạnh ngang nhau (`¡CASI ME APLASTA!` an toàn hơn `¡ESCAPÉ!`). Line 2 thường không tránh được `AÑOS`, nên đổi khung nếu cần (`EDAD DE HIELO • 20,000 A. C.` không có dấu).
3. **Sai 2 lần → chèn chữ bằng ffmpeg** (không tốn credit sinh lại). Hỏi user trước khi sinh lại bản không chữ (Rule 29): bỏ hai dòng `text in Spanish clearly …` khỏi prompt, chừa nửa trên trống, rồi chèn chữ:

```bash
# Chữ để trong file UTF-8 (tránh lỗi mã hóa dấu khi truyền qua shell Windows)
printf '¡CASI ME APLASTA!' > "${OUTDIR}/thumbnails/line1.txt"
printf 'NEANDERTALES • HACE 51,000 AÑOS' > "${OUTDIR}/thumbnails/line2.txt"
cd "${OUTDIR}/thumbnails" && ffmpeg -y -i thumbnail_v1_yt.png -vf \
"drawtext=fontfile='C\:/Windows/Fonts/impact.ttf':textfile=line1.txt:fontsize=110:fontcolor=yellow:borderw=8:bordercolor=black:x=60:y=50,\
drawtext=fontfile='C\:/Windows/Fonts/impact.ttf':textfile=line2.txt:fontsize=58:fontcolor=white:borderw=5:bordercolor=black:x=64:y=185" \
thumbnail_v1_yt_text.png
```

Đã test trên máy này (2026-10-13): font Impact hiển thị đúng `¡`, `Ñ` và `•`. Chạy sau Step 6 (ảnh đã 1280x720), giữ chữ ở nửa trên, tránh góc dưới bên phải (nhãn thời lượng của YouTube).
