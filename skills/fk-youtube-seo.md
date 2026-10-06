# fk-youtube-seo — Generate YouTube Metadata (SEO-Optimized)

Generate SEO-optimized YouTube metadata: hook title, description, hashtags, and niche keywords.

Usage: `/fk-youtube-seo <project_id> [--language vi] [--niche military-documentary]`

## Step 1: Load project context + channel rules

```bash
curl -s http://127.0.0.1:8100/api/projects/<PID>
curl -s "http://127.0.0.1:8100/api/videos?project_id=<PID>"
curl -s "http://127.0.0.1:8100/api/scenes?video_id=<VID>"
```

Extract:
- **Story**: full narrative arc — what happens, conflict, resolution
- **Characters**: key names (for title/description keyword density)
- **Language**: target audience language (vi, en, etc.)
- **Material/genre**: realistic, anime, etc. → determines niche
- **Video duration**: from scene count × avg duration

### Load channel rules (if channel specified)

If `--channel <name>` is provided (or inferred from context), load SEO defaults from channel rules:

```bash
cat youtube/channels/<CHANNEL>/channel_rules.json
```

Extract from `seo` section:
- **`niche`** → use as niche in Step 2 (skip guessing)
- **`default_tags`** → merge into generated tags in Step 6
- **`always_include_hashtags`** → prepend to hashtag list in Step 5
- **`hashtag_language`** → controls language mix strategy (e.g., `mixed_vi_en`)
- **`title_max_chars`** → enforce as hard limit in Step 3 (default: 65)
- **`default_category`** → use as YouTube category ID

If no channel rules file exists, fall back to detecting niche from project content and using skill defaults.

## Step 2: Identify the NICHE

The niche determines which keywords, hashtags, and competitors to target.

**If channel rules loaded** and `seo.niche` exists, use it directly (e.g., `geopolitics-military-documentary`). Skip classification below.

**Otherwise**, based on project genre + content, classify into a niche:

| Content Type | Niche | Example Keywords |
|-------------|-------|-----------------|
| Military story | military-documentary | chiến tranh, hải quân, tàu chiến, quân sự |
| Romance | drama-romance | tình yêu, phim tình cảm, cảm động |
| Action/Heist | action-thriller | hành động, kịch tính, phim hành động |
| Historical | history-education | lịch sử, sự kiện, phim tài liệu |
| Fantasy | fantasy-animation | phép thuật, phiêu lưu, anime |
| Horror | horror-suspense | kinh dị, rùng rợn, bí ẩn |

## Step 3: Generate HOOK TITLE

The title is the #1 SEO factor. It must:

### Rules:
- **`seo.title_max_chars` from channel rules** (default: 65) — hard limit. YouTube truncates at ~70
- **Primary keyword in first 5 words** (YouTube weighs early words higher)
- **Power word** to trigger click: SHOCKING, SECRET, IMPOSSIBLE, ATTACK, DEADLY, LAST
- **Curiosity gap** — promises information viewer doesn't have yet
- **Number or specificity** — "2 Million Barrels" is stronger than "lots of oil"
- **Brackets/parentheses** boost CTR: [FULL MOVIE] (Eng Sub) {4K}
- **Language match** — title in target language, but include English keywords if audience searches bilingually

### Title formulas (pick best fit):

1. **Question hook**: `Tại Sao Iran Tấn Công Tàu Dầu Mỹ? | Chiến Dịch Hormuz Shield [Phim Tài Liệu]`
2. **Statement shock**: `Iran Tấn Công Tàu Dầu Mỹ — Hải Quân Mỹ Phản Ứng Thế Nào? [4K]`
3. **Number + stakes**: `2 Triệu Thùng Dầu vs 6 Tàu Tấn Công Iran | Eo Biển Tử Thần Hormuz`
4. **Challenge/Impossible**: `Vượt Qua Eo Biển Tử Thần — Nhiệm Vụ Bất Khả Thi Của Hải Quân Mỹ`
5. **Revelation**: `Bí Mật Chiến Dịch Hormuz Shield — Khi Iran Phong Tỏa Eo Biển Hormuz`
6. **Time Travel & Historical POV Vlog — Bộ 3 Công Thức High-Stakes / Sinh Tồn Nghẹt Thở (BẮT BUỘC)**:
   > [!CRITICAL]
   > **TUYỆT ĐỐI KHÔNG DÙNG TIÊU ĐỀ HIỀN / GIÁO KHOA**: Các tiêu đề như `I time travelled to the Ice Age in 20,000 BC: Surviving with Woolly Mammoths!` hay `A Day in Ancient Egypt` nghe giống phim tài liệu trường học, người xem lướt qua sẽ thấy nhàm chán và bỏ qua.
   > Bắt buộc áp dụng **Bộ 3 Công Thức High-Stakes (Kịch tính cao độ - Nghẹt thở - Shock văn hóa)** để đẩy CTR lên mức tối đa:

   > [!IMPORTANT]
   > **Mọi tiêu đề POV vlog phải có tên tộc người HOẶC niên đại (user chốt 2026-10-06), có cả hai thì càng tốt nếu vẫn ≤ `title_max_chars`.**
   > - **Tên tộc người**: tên cụ thể như `Neanderthals`, `Vikings`, `Romans`, `Aztecs`, `Mammoth Hunters`. Không dùng từ chung chung `Cavemen`, `Ancient People`, `Ice Age Humans`.
   > - **Niên đại**: năm hoặc mốc cụ thể như `51,000 Years Ago`, `20,000 BC`, `79 AD`, `1912`. Chỉ ghi "Ice Age" thì không đủ.
   > - Niên đại phải đúng với research. Ví dụ "51,000 năm trước" là khoảng 49,000 BC, không phải 51,000 BC. Nếu không chắc, ghi dạng `51,000 Years Ago`.

   - **Option 1 (Nguy hiểm cận kề / Immediate Peril & Near-Death Escape — Áp dụng cho Nhóm 1: Thảm Họa Lịch Sử Có Thật)**:
     - **Cấu trúc**: `I Time Travelled to [Year/Era] — And [Imminent Danger / Almost Got Trampled / Barely Escaped]`
     - **Tâm lý học**: Đẩy mối đe dọa sinh tử lên ngay lập tức. Khán giả tò mò tột độ liệu vlogger thoát chết bằng cách nào trong gang tấc khi livestream thảm họa (Titanic 1912, Pompeii 79 SCN, Chernobyl 1986).
     - **Ví dụ**:
       - `I Time Travelled to 20,000 BC — And Almost Got Trampled by a Mammoth`
       - `I Time Travelled to 1912 — And Tried to Warn the Captain of the Titanic`
       - `I Time Travelled to 79 AD — And Mount Vesuvius Started Erupting`
       - `I Time Travelled to 1986 Chernobyl — And the Sirens Went Off`

   - **Option 2 (Câu hỏi sinh tồn / Survival Question Hook — Áp dụng cho Nhóm 3: Newsjacking & Thử Thách Khắc Nghiệt, và mọi vlog dùng Survival Preset của `/fk-time-travel-vlog` mục 5c)**:
     - **Cấu trúc**: `Would [People] Let You [Into Their Cave / Join Their Hunt]? ([Year])` hoặc `What Happens When [Situation có trong video] [with People]? ([Year])`.
     - **Câu hỏi phải được video trả lời rõ.** YouTube xếp tiêu đề hứa điều video không có vào "Malicious clickbait" (Spam Policy). Ví dụ: hỏi "Would Neanderthals Let You In?" thì video phải có cảnh họ chặn cửa rồi cho vào.
     - **Không dùng "Can I Survive…?"** vì trùng kênh đối thủ. **Không dùng "I Survived 24 Hours"** (user bỏ 2026-10-06): tiêu đề này hứa trọn 24 giờ, và cả series dễ bị coi là cùng một khuôn.
     - **Không bịa con số** nhiệt độ, calo, số người chết (vd. "-40°C") nếu bảng nguồn không có.
     - **Tâm lý học**: câu hỏi có/không về việc được chấp nhận hay sống sót giữa một tộc người cụ thể. Người xem bấm vào để biết câu trả lời.
     - **Ví dụ**:
       - `Would Neanderthals Let You Into Their Cave? (51,000 Years Ago)`
       - `What Happens When Hyenas Raid a Neanderthal Camp at Night?`
       - `Would the Romans Let You Watch the Colosseum Open? (80 AD)`
       - `What Happens When You Get Sick in Medieval London? (1348)`
     - **Kiểm tra trùng lặp**: trước khi chốt, web search tiêu đề dự kiến. Nếu đã có video cùng chủ đề, phân biệt bằng địa điểm/năm cụ thể hơn hoặc mối nguy riêng của video mình.

   - **Option 3 (Shock văn hóa & Nghịch lý thời gian — Áp dụng cho Nhóm 2: Va Chạm Văn Minh / Bị Coi Là Phù Thủy)**:
     - **Cấu trúc**: `What Happens When You Show [Modern Object / Technology] to [Ancient People]?` hoặc `I Showed [Modern Item] to [Ancient People] — Their Reaction Was Terrifying`
     - **Tâm lý học**: Va chạm văn minh cực độ, thí nghiệm văn hóa giữa hiện đại và tiền sử/cổ đại. Kích thích sự tò mò về phản ứng ngây thơ, sợ hãi, vây bắt hoặc tôn sùng của người cổ đại.
     - **Ví dụ**:
       - `What Happens When You Show a Lighter to Neanderthals?`
       - `I Showed an iPhone at the Salem Witch Trials (1692) — They Tried to Burn Me`
       - `What Happens When You Show a Smartphone to Roman Soldiers?`
       - `I Showed Modern Medicine to 14th Century Plague Doctors`

   - **Bắt buộc khi chạy `/fk-youtube-seo` cho POV Vlog**: Luôn luôn xuất ra đầy đủ **cả 3 Option High-Stakes** này trong phần `📌 TITLE OPTIONS` để người dùng lựa chọn, kèm phân tích CTR và góc khai thác!

### Generate 3 title variants, ranked by SEO strength.

For each title, explain:
- Primary keyword and position
- Power word used
- Estimated search volume reasoning
- Character count

## Step 4: Generate DESCRIPTION

YouTube description has 3 zones with different SEO purposes:

### Zone 1: Above the fold (first 150 chars — visible without "Show more")

```
[HOOK SENTENCE — restate the title promise with more detail]
[CALL TO ACTION — subscribe/like]
```

This zone MUST contain:
- Primary keyword (same as title)
- Secondary keyword
- Emotional hook matching title

### Zone 2: Main body (150-2000 chars)

```
[STORY SUMMARY — 3-5 sentences, keyword-rich but natural]

[CHAPTER TIMESTAMPS — if video has clear sections]
00:00 — [Section name with keyword]
01:23 — [Section name with keyword]
...

[CONTEXT/FACTS — educational value, real-world context]
```

Rules:
- **Timestamps** boost SEO (YouTube indexes them as chapters)
- **Keyword density**: primary keyword 3-5 times, secondary 2-3 times
- **Natural language** — don't keyword-stuff, write for humans
- **Links to related videos** (placeholder for user to fill)

### Zone 3: Footer (2000-5000 chars)

```
[TAGS/KEYWORDS — natural sentence form]
[CREDITS]
[SOCIAL LINKS — placeholder]
[FICTIONAL CONTENT DISCLAIMER — BẮT BUỘC cho mọi video hư cấu/tái hiện lịch sử]
[COPYRIGHT]
```

### Full description template:

```
[Zone 1 — Hook + CTA]
{hook_sentence}

Like & Subscribe for more {niche} content!
Turn on notifications 🔔 to never miss a video.

[Zone 2 — Body]
{story_summary_3_5_sentences}

⏱️ Timestamps:
{auto_generated_timestamps_from_scenes}

📖 Background:
{real_world_context_2_3_sentences}

[Zone 3 — Footer & Socials]
—————————————————————————
{fictional_disclaimer_block — chọn template ngôn ngữ từ Rule A}

© {year} {channel_name} — All rights reserved.
```

> **CRITICAL RULES (Fiction Disclaimer vs Tool Branding — Tách bạch 2 khái niệm):**
>
> **Rule A — BẮT BUỘC: Fictional Content Disclaimer (Khai báo nội dung hư cấu)**
> Mọi video hư cấu / tái hiện lịch sử / time-travel vlog PHẢI có đoạn disclaimer cuối Zone 3.
> Đây là quy định của kênh, YouTube không bắt buộc. YouTube chỉ bắt buộc bật khai báo AI trong Studio (Rule D), và disclaimer trong description KHÔNG thay thế được bước đó. Disclaimer có ích vì nó nói rõ với người xem phần nào là thật, phần nào là hư cấu, điều mà nhãn AI tự động của YouTube không làm.
> Chọn template theo ngôn ngữ script:
>
> Disclaimer phải có **3 lớp cụ thể** — không viết chung chung "hư cấu, giải trí":
> - **Lớp 1 — Thể loại**: nêu đây là tái hiện sáng tạo dựa trên bằng chứng lịch sử/khảo cổ
> - **Lớp 2 — Ranh giới thật/giả**: cái gì là thật (thời đại, loài người, địa điểm), cái gì là hư cấu (nhân vật, đối thoại, sự kiện cụ thể)
> - **Lớp 3 — Hướng mở**: gợi mở tò mò tìm hiểu thêm — không chỉ "đây là fake"
>
> **Tiếng Việt — template đầy đủ 3 lớp:**
> ```
> ⚠️ VỀ VIDEO NÀY:
> Đây là tác phẩm tái hiện lịch sử sáng tạo, được dựng bằng AI dựa trên bằng chứng khảo cổ
> và nghiên cứu lịch sử — mục đích kích thích trí tưởng tượng và khám phá quá khứ.
>
> ✅ CÓ THẬT: Bối cảnh thời đại, loài người, địa điểm địa lý, công cụ/lối sống được
> tái hiện dựa trên dữ liệu nghiên cứu.
> 🎭 HƯ CẤU: Nhân vật vlogger, tên nhân vật, đoạn đối thoại, chuỗi sự kiện cụ thể
> đều được biên kịch hoặc kịch tính hóa phục vụ câu chuyện.
>
> Muốn tìm hiểu thêm về thời kỳ này? Xem phần nguồn tham khảo trong description.
> ```
>
> **English — 3-layer template:**
> ```
> ⚠️ ABOUT THIS VIDEO:
> This is a creative historical recreation produced with AI, inspired by archaeological
> evidence and historical research — designed to spark imagination about the past.
>
> ✅ BASED ON FACT: The time period, species, geography, tools, and way of life depicted
> are grounded in current research and archaeological findings.
> 🎭 DRAMATIZED: The vlogger character, individual characters, specific dialogue, and
> narrative events are scripted and fictionalized for storytelling purposes.
>
> Curious to learn more? Check the sources linked in the description.
> ```
>
> **Japanese — 3層テンプレート:**
> ```
> ⚠️ この動画について:
> 本作は考古学的証拠と歴史研究にもとづき、AIで制作した歴史的再現フィクションです。
> 過去への想像力を広げることを目的としています。
>
> ✅ 史実にもとづく部分: 時代設定・登場する人類・地理・道具・生活様式は
> 現在の研究・発掘成果を参考にしています。
> 🎭 フィクション部分: Vloggerキャラクター・登場人物の名前・セリフ・
> 具体的な出来事はストーリーのために脚色・創作されています。
>
> この時代についてもっと知りたい方は、概要欄のリンクをご覧ください。
> ```
>
> **Dòng ✅ CÓ THẬT chỉ được liệt kê điều đã kiểm chứng.** Vlog time-travel được phép hư cấu (CLAUDE.md Rule 14), nên nhiều chi tiết trong video có thể là bịa. Đối chiếu với `.omc/research/` hoặc bảng nguồn của dự án: chi tiết nào không có nguồn thì chuyển sang dòng 🎭 HƯ CẤU. Nếu dự án không research gì, bỏ cụm "dựa trên bằng chứng khảo cổ" và chỉ giữ thời đại/địa điểm làm bối cảnh. Ghi "dựa trên nghiên cứu" cho nội dung bịa còn gây hiểu lầm hơn cả không có disclaimer. Câu "Xem nguồn tham khảo" chỉ giữ khi đã thêm link nguồn thật.
>
> **Cách điền `{era}` và `{species}` vào template:**
> - Thay "thời đại" bằng tên cụ thể: "51.000 năm trước — thời kỳ người Neanderthal"
> - Thay "loài người" bằng: "người Neanderthal (*Homo neanderthalensis*)"
> - Thêm 1–2 nguồn tham khảo thật (Wikipedia, Nature, Smithsonian) vào cuối Zone 3
>   ví dụ: `📚 Nguồn: Smithsonian Human Origins — https://humanorigins.si.edu`
>   (link thật, không bịa — chỉ thêm nếu research đã xác nhận)
>
> **Rule B — CẤM: Tool Branding (Không quảng cáo tool nội bộ)**
> NEVER include "Generated with Flow Kit", "Produced with Flow Kit", "Realistic Cinematic Engine",
> or any internal tool/software names anywhere in public metadata.
>
> **Rule C — CẤM: Specific AI Tool Names in Description**
> NEVER name specific AI tools (Google Flow, Veo, Imagen, etc.) in the description or tags.
> The disclaimer says "AI" generically. YouTube's disclosure is a Studio setting, so naming tools adds nothing.
>
> **Rule D — BẮT BUỘC: Khai báo AI trong YouTube Studio (chính sách YouTube, kiểm tra 2026-10-06)**
> Nguồn: [Disclosing use of GenAI content](https://support.google.com/youtube/answer/14328491).
> - **Khi nào phải bật**: YouTube yêu cầu khai báo khi dùng AI để "meaningfully alter or generate photorealistic content", gồm cả nội dung "Generates a realistic scene that didn't actually occur". Vlog time-travel dựng bằng Omni Flash/Veo là cảnh photorealistic chưa từng xảy ra → **luôn bật**. Ngoại lệ "not realistic" (cưỡi kỳ lân, hoạt hình) không áp dụng cho kênh này.
> - **Cách bật**: trong Studio, phần Attributes → "AI use" → **Yes** (trước đây tên là "Altered or synthetic content"). Đây là cài đặt trong Studio, KHÔNG phải dòng chữ trong description.
> - **Nhãn**: với video photorealistic, YouTube có thể hiện nhãn ngay trên trình phát. YouTube cũng tự gắn nhãn nếu hệ thống của họ phát hiện nội dung AI.
> - **Không ảnh hưởng doanh thu**: theo help page, việc khai báo "won't limit a video's audience or impact its eligibility to earn money".
> - **Nếu không khai báo**: kênh "consistently choose not to disclose" có thể bị gắn nhãn thủ công (và không gỡ được), bị xóa video, hoặc bị đình chỉ khỏi YouTube Partner Program.
>
> **Rule E — Chính sách "inauthentic content" (đổi tên từ "repetitious content" ngày 2025-07-15)**
> Nguồn: [YouTube channel monetization policies](https://support.google.com/youtube/answer/1311392).
> - YouTube cho phép "a series following a set of characters across episodes" khi mỗi tập có "a distinct storyline, focus, or concept", và cho phép "using AI to visualize a unique character and narrative you invented".
> - YouTube cấm kiếm tiền với "Videos where characters are put in the same situation over and over again with the same outcome" và "AI-generated content made with generic or unoriginal templates giving the impression of mass production".
> - Áp dụng cho series vlog time-travel: mỗi tập phải có mối nguy, mạch truyện và cái kết khác nhau. Nếu tập mới chỉ đổi bối cảnh còn giữ nguyên cấu trúc (bị đe dọa → chạy trốn → thoát được) thì báo cho user biết.
> - Video về thảm họa có thật (Pompeii, Titanic, Chernobyl): không viết title/description như thể sự việc vừa xảy ra. YouTube cấm "realistic visuals tricking viewers into believing a fake celebrity death or natural disaster has occurred". Luôn ghi năm trong title và để disclaimer nói rõ đây là tái hiện.
>
> Keep all YouTube metadata 100% natural, clean, authentic, and focused on the story and channel.



## Step 5: Generate HASHTAGS

YouTube allows up to 15 hashtags (first 3 shown above title).

**If channel rules loaded**: prepend `seo.always_include_hashtags` (e.g., `#PhimTàiLiệu #QuânSự`) as the first hashtags in Tier 1. Use `seo.hashtag_language` to control language mix (`mixed_vi_en` = Vietnamese + English).

### Hashtag strategy (3 tiers):

**Tier 1 — High volume, broad (5 hashtags):**
Niche-level tags that get massive search. Place first 3 here (shown above title).
Start with `always_include_hashtags` from channel rules if available.
```
#PhimTàiLiệu #QuânSự #HảiQuân
```

**Tier 2 — Medium volume, specific (5 hashtags):**
Topic-specific tags matching this video's content.
```
#EoBiểnHormuz #IranVsMỹ #TàuChiến #ChiếnDịchHormuzShield #TàuDầu
```

**Tier 3 — Long-tail, niche (5 hashtags):**
Highly specific tags with less competition — easier to rank.
```
#USSArleighBurke #IRGC #StraitOfHormuz #NavalEscort #OilTanker
```

### Hashtag rules:
- NO spaces in hashtags: `#PhimTàiLiệu` not `#Phim Tài Liệu`
- Mix languages if audience is bilingual: Vietnamese + English
- First 3 hashtags = most important (shown above title)
- Don't use irrelevant trending tags (YouTube penalizes this)
- Include both Vietnamese and English versions of key terms

## Step 6: Generate KEYWORDS (Tags)

YouTube tags (different from hashtags) are hidden metadata. Max 500 characters total.

**If channel rules loaded**: merge `seo.default_tags` (e.g., `["phim tài liệu", "quân sự", "lịch sử", ...]`) into the generated tag list. Place channel default tags first, then add video-specific tags. Deduplicate.

### Keyword research approach:

**1. Primary keywords (exact match — highest priority):**
What would someone TYPE to find this video?
```
eo biển hormuz, iran tấn công tàu dầu, hải quân mỹ, chiến dịch hormuz shield
```

**2. Secondary keywords (broad match):**
Related topics that expand reach.
```
phim tài liệu quân sự, chiến tranh iran mỹ, tàu khu trục, strait of hormuz
```

**3. Long-tail keywords (low competition, high intent):**
Specific phrases people search for.
```
iran đóng cửa eo biển hormuz, uss arleigh burke, tàu dầu vlcc, irgc navy
```

**4. Trending/seasonal keywords:**
Current events that make this topic relevant.
```
iran 2024, trung đông căng thẳng, giá dầu tăng, chiến tranh trung đông
```

**5. English crossover keywords:**
For bilingual audiences and international reach.
```
strait of hormuz, iran navy, us navy, oil tanker escort, hormuz shield
```

### Keyword rules:
- Total max 500 characters
- Most important keywords first
- Mix exact match + broad match
- Include common misspellings if relevant
- Include both singular and plural forms
- Don't repeat keywords already in title/description

## Step 7: Generate TIMESTAMPS

Auto-generate from scene data:

```python
For each scene group (every 4-5 scenes = 1 chapter):
  timestamp = sum of previous scene durations
  chapter_name = summarize what happens in those scenes (keyword-rich)
```

Format:
```
00:00 Giới thiệu — Eo biển Hormuz tử thần
00:25 Lầu Năm Góc ra lệnh — Chiến dịch Hormuz Shield
01:05 Hải quân Mỹ xuất kích — USS Arleigh Burke
01:45 Iran triển khai IRGC — Căng thẳng leo thang
02:20 Đối đầu trên biển — Tàu cao tốc Iran tấn công
03:00 Phát hiện thủy lôi — Nguy hiểm chết người
03:35 Kết thúc — Vượt qua eo biển tử thần
```

## Step 8: Output all metadata

**CRITICAL: Print ALL metadata directly to terminal as plain text.**
The user needs to copy-paste from the terminal into YouTube Studio.
Do NOT just save to file — the user should NOT need to open any file.
Print each section with clear separators so they can copy individual parts.

```
═══════════════════════════════════════════
  YouTube SEO Metadata — {project_name}
═══════════════════════════════════════════

📌 TITLE OPTIONS (pick one):

  [Đối với Time Travel & Historical POV Vlog — BẮT BUỘC xuất cả 3 Option High-Stakes]:
  1. Option 1 (Nguy hiểm cận kề - Khuyên dùng): {title_option_1} ({char_count} chars)
     CTR Angle: Thoát chết trong gang tấc / Đối mặt hiểm hoạ sinh tử trực diện
     
  2. Option 2 (Câu hỏi sinh tồn): {title_option_2} ({char_count} chars)
     CTR Angle: Câu hỏi có/không về việc được chấp nhận / sống sót giữa tộc người cụ thể (video phải trả lời)

  Mỗi tiêu đề: ghi rõ tên tộc người / niên đại nằm ở đâu, và cảnh nào trong video thực hiện lời hứa của tiêu đề.
     
  3. Option 3 (Shock văn hóa & Nghịch lý): {title_option_3} ({char_count} chars)
     CTR Angle: Va chạm văn minh / Phản ứng kinh ngạc trước công nghệ hiện đại

  [Đối với Niche Quân sự / Tài liệu / Drama khác]:
  1. {title_v1} ({char_count} chars)
  2. {title_v2} ({char_count} chars)
  3. {title_v3} ({char_count} chars)

📝 DESCRIPTION:
─────────────────
{full_description}

#️⃣ HASHTAGS (copy all):
─────────────────
{all_15_hashtags_on_one_line}

🏷️ TAGS (paste into YouTube Studio):
─────────────────
{comma_separated_tags_under_500_chars}

⏱️ TIMESTAMPS (paste into description):
─────────────────
{timestamp_list}

📊 SEO SCORE:
─────────────────
  Title keyword position: {1st/2nd/3rd word}
  Description keyword density: {X}%
  Hashtag coverage: {broad}% / {specific}% / {longtail}%
  Tag character usage: {N}/500
  Timestamp chapters: {N}
  Estimated niche: {niche_name}

🛡️ YOUTUBE STUDIO — BẮT BUỘC TRƯỚC KHI ĐĂNG:
─────────────────
  □ Studio → Attributes → "AI use" → Yes (trước đây là "Altered or synthetic
    content"). Bắt buộc với cảnh AI photorealistic. Khai báo không làm giảm
    lượt hiển thị hay doanh thu; không khai báo nhiều lần có thể bị xóa video
    hoặc đình chỉ khỏi YPP. (Rule D)
  □ Disclaimer hư cấu đã có ở cuối description (Rule A). Nó không thay thế bước trên.
  □ Series: tập này có mạch truyện và kết khác các tập trước (Rule E).
```

## Step 9: Save backup (optional)

Also save a backup copy to project directory for reference:

```bash
# Get project output directory
PROJ_OUT=$(curl -s http://127.0.0.1:8100/api/projects/<PID>/output-dir)
OUTDIR=$(echo "$PROJ_OUT" | python3 -c "import sys,json; print(json.load(sys.stdin)['path'])")
cat > "${OUTDIR}/youtube_seo.md" << 'EOF'
{all_metadata_formatted}
EOF
```

The primary output is the terminal print in Step 8 — the file is just a backup.

## SEO Best Practices Reference

| Factor | Weight | Optimization |
|--------|--------|-------------|
| Title | 30% | Primary keyword in first 5 words, power word, 60-70 chars |
| Description | 25% | Keyword in first 150 chars, timestamps, 2000+ chars total |
| Tags | 15% | Mix exact + broad + long-tail, max 500 chars |
| Hashtags | 10% | First 3 = broad niche, next 12 = specific + long-tail |
| Timestamps | 10% | Chapter markers boost watch time + SEO |
| Thumbnail | 10% | (Handled by /fk-thumbnail) |

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|-------------|-----|
| Keyword stuffing in title | YouTube penalizes unnatural titles | Use 1-2 keywords naturally |
| Generic description | Missed SEO opportunity | Write 2000+ chars with keywords |
| No timestamps | Loses chapter indexing benefit | Add timestamps every 30-60s |
| English-only tags for VN audience | Misses local search | Mix Vietnamese + English |
| Too many broad hashtags | Competes with giant channels | Use 5 broad + 10 specific/long-tail |
| Title > 70 chars | Gets truncated on mobile | Keep under 65 chars ideally |
| No CTA in description | Lower engagement signals | Add subscribe/like CTA above fold |
