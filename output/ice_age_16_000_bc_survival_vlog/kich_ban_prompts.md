# Kịch bản & danh sách prompt — Ice Age 16,000 BC Survival Vlog

**52 cảnh, tổng 8:22.** HORIZONTAL 16:9, material `phone_vlog`, R2V Omni Flash (`GENERATE_VIDEO_REFS`).

File này được dựng tự động từ [clips.json](clips.json) theo quy tắc ở [script.md](script.md) mục 6. Muốn sửa cảnh nào thì sửa trong clips.json rồi dựng lại, đừng sửa trực tiếp file này. Với mỗi cảnh:

- **prompt** là mô tả khung hình đầu tiên. Khi sinh, server tự chèn thêm phần mở đầu của material `phone_vlog`.
- **video_prompt** là prompt gửi cho model video.
- **Thoại** là lời Nora nói, tách riêng để dễ đọc.

Ký hiệu trong bảng: 🆕 = cảnh mới thêm, ✂️ = cảnh rút từ 10s xuống 8s.

## Tổng quan

| Cảnh | Hồi | Dài | Kiểu quay | Ref | Lời thoại |
|---|---|---|---|---|---|
| [S01](#s01) | 1 | 10s | pov | Nora, Torak, Mezhyrich Camp | Hour one. Central Ukraine, roughly eighteen thousand years ago, / coldest stretch of the Ice Age. I've dug at this site. / It never looked like this. |
| [S02](#s02) | 1 | 10s | selfie | Nora, Mezhyrich Camp | Twenty-four hours, no tent, no gear, only what they use. / These people got through the harshest phase of the Ice Age / living around domes of mammoth bone. |
| [S03](#s03) | 1 | 10s | back_selfie | Nora, Torak, Mezhyrich Camp | Okay, that's Torak. My name for him. / Hand flat, palm down, probably means stay. I stay. / A stranger walking into a winter camp? I'd spear me too. |
| [S04](#s04) | 2 | 10s | selfie | Nora, Torak, Mezhyrich Camp | No, wait— see that white patch on his cheek? Frostnip. / Skin's starting to freeze and he can't feel it. / Nobody can see their own face out here. |
| [S05](#s05) | 2 | 10s | pov_hand | Nora, Torak, Mezhyrich Camp | Don't rub it. Rubbing frozen skin just tears it. / Warm hand, steady pressure, wait. Field medics still teach exactly this. / Okay... he's letting me. |
| [S06](#s06) | 2 | 10s | selfie | Nora, Alva, Mezhyrich Camp | Hour two. Alva just checked my mitten cord, twice. Fair. / Mittens beat gloves, fingers share heat. / And drop one in this wind, it's gone. |
| [S07](#s07) | 2 | 10s | selfie | Nora, Mezhyrich Camp | Lower jaws, stacked in that zigzag. / I've walked around the museum reconstruction maybe fifty times. / Never once with smoke coming out the top. Okay, okay, focus. |
| [S08](#s08) | 2 | 10s | selfie | Nora, Mezhyrich Camp | Real talk, we still argue what these were. / Homes, food stores, maybe monuments. Newer dating says people weren't here long. / Someone's clearly sleeping in this one. |
| [S09](#s09) | 2 | 10s | selfie | Nora, Alva, Bone Dwelling Interior | Hardly any trees out here, so Alva burns bone. / The greasy ends, mostly. We find barely any charcoal in these hearths. / That's why, probably. |
| [S10](#s10) | 2 | 10s | pov_hand | Nora, Alva, Bone Dwelling Interior | Yeah, I know, I know. / Don't eat snow, ever. Your body burns its own heat just melting it. / I was testing her. Mostly. |
| [S11](#s11) | 2 | 10s | selfie | Nora, Alva, Bone Dwelling Interior | Hot stone into a hide bag. / Hide can't sit on a flame, it burns. We dig up heat-cracked rock / at sites like this. Probably from exactly this. |
| [S12](#s12) 🆕 | 2 | 10s | selfie | Nora, Alva, Bone Dwelling Interior | Drinking before I'm thirsty. Cold makes you pee more / and quietly switches thirst off. Dehydration probably makes frostbite likelier. / So: warm water, small sips, all day. |
| [S13](#s13) | 2 | 10s | tripod | Nora, Alva, Bone Dwelling Interior | Every bite of meat, she hands me a lump of fat. / Lean meat alone in this cold makes you sick. The fat's the actual fuel. / Tastes like candle. |
| [S14](#s14) | 2 | 10s | selfie | Nora, Torak, Mezhyrich Camp | Hour four. These pits ring every hut. / We dig them out full of bone. Ground's frozen year-round here, / so most of us think: freezers. And... yep. Meat. |
| [S15](#s15) | 2 | 10s | selfie | Nora, Torak, Mezhyrich Camp | Fox pelts, tails still on. / We find tons of fox bones at this site and wondered why. / Not dinner. Coats. Maybe also dinner. |
| [S16](#s16) | 2 | 10s | selfie | Nora, Alva, Mezhyrich Camp | She likes my belt. / Fox canines, drilled and sewn on. Copied from a burial at Sungir, / way north of here, over two hundred teeth. Nailed it, apparently. |
| [S17](#s17) 🆕 | 2 | 10s | selfie | Nora, Alva, Mezhyrich Camp | Flint end-scraper. Every scrap of fat comes off, / or the hide rots. Dwelling one here had these stored inside, / right next to the flint cores. Same tool. |
| [S18](#s18) | 2 | 10s | selfie | Nora, Torak, Mammoth Steppe | Hour six. Hauling bone makes me sweat, and damp fur stops insulating. / So I open up before I'm hot, not after. / Torak's already done it. |
| [S19](#s19) | 2 | 10s | selfie | Nora, Torak, Mammoth Steppe | Big debate in my field: / did they hunt all these mammoths, or collect bones from old natural piles? / This one's been dead for years. So today, collecting. |
| [S20](#s20) | 2 | 10s | selfie | Nora, Torak, Mammoth Steppe | Wind's picking up— sh— that's the real killer, not the temperature. / Same cold, twice the wind, you lose heat way faster. / Torak's already heading in. |
| [S21](#s21) | 2 | 10s | selfie | Nora, Alva, Bone Dwelling Interior | Hour eight. Warm hands in your armpits, not over the fire. / Numb skin can't feel a burn. / Alva's doing the same thing, so I'm in good company. |
| [S22](#s22) | 3 | 10s | selfie | Nora, Torak, Mezhyrich Camp | Hour nine. Torak's back from the ridge, / arm swinging low like a trunk. Herd. And he wants me along. / Not sure if that's trust or bait. |
| [S23](#s23) | 3 | 10s | back | Nora, Torak, Mammoth Steppe | Walk in his tracks. Saves energy, / and he knows where the crust holds. We stay downwind too. / Mammoths probably smell like elephants: way better than they see. |
| [S24](#s24) | 3 | 10s | back | Nora, Woolly Mammoth, Mammoth Steppe | Oh. Oh, there they are. / Eight, nine... calves in the middle. That's textbook elephant behaviour. / I did not expect textbook to be this big. |
| [S25](#s25) | 3 | 10s | wide | Nora, Woolly Mammoth, Mammoth Steppe | Small ears, see? Big ears dump heat, they'd freeze. / Shaggy outer hair, dense wool underneath. / We have frozen carcasses from Siberia with ears this size. |
| [S26](#s26) | 3 | 10s | selfie | Nora, Torak, Woolly Mammoth | Torak's hand says stay low, and I'm staying low. / No, wait— lead female, probably, trunk up, sniffing. / She's testing the wind. Is our wind still good? |
| [S27](#s27) | 3 | 10s | selfie | Nora, Torak, Woolly Mammoth | Real talk, I need a closer shot. Fifty metres, max. / He's shaking his head. I know. I know. / Ten more steps and I'm done. |
| [S28](#s28) | 3 | 10s | pov_hand | Nora, Woolly Mammoth, Mammoth Steppe | Calf's wandering this way. Mum's watching it. / Mum's watching me now. Okay... / head up, trunk tucked, that's the posture. That's the posture before— |
| [S29](#s29) | 4 | 8s | run | Nora, Woolly Mammoth, Mammoth Steppe | She's charging— sh— don't run straight, she's way faster than me. / Riverbank. Get something big between us. / Go, go! |
| [S30](#s30) | 4 | 6s | pov | Nora, Torak, Mammoth Steppe | Knee-deep, I can't run, just big heavy steps. / The bank's right there, Torak's waving. / Go. |
| [S31](#s31) | 4 | 8s | selfie | Nora, Woolly Mammoth, Mammoth Steppe | Down, down, down. Steep bank, glazed ice on the lip. / Something that heavy can't get footing on that. / Probably. Please, probably. |
| [S32](#s32) | 4 | 6s | selfie | Nora, Woolly Mammoth, Mammoth Steppe | Oh no no no— she's slipping, she's slipping— / she's turning. / She's turning away! |
| [S33](#s33) | 4 | 8s | pov | Nora, Woolly Mammoth, Mammoth Steppe | Going back to her calf. Warning charge, probably, not a kill. / Elephants do that. / Didn't feel like a warning. |
| [S34](#s34) | 4 | 10s | selfie | Nora, Torak, Mammoth Steppe | Okay, okay. Hand, yes, thank you. / He's... laughing at me. Fair. / I just did everything I tell my students never to do. |
| [S35](#s35) | 4 | 10s | selfie | Nora, Torak, Mammoth Steppe | Hour thirteen. Hands won't stop shaking. That's adrenaline dumping, not cold. / Eat something, sit, breathe slow. / Torak's handing me fat. Of course he is. |
| [S36](#s36) ✂️ | 4 | 8s | back_selfie | Nora, Woolly Mammoth, Mammoth Steppe | Front feet slid, she twisted, she bailed. / Ice turned her, not me. No accident. / Torak picked this bank on purpose. |
| [S37](#s37) | 5 | 10s | selfie | Nora, Alva, Bone Dwelling Interior | Hour fifteen. Alva heard. Everyone heard. / She's cracking a leg bone for me, / which I'm choosing to read as 'welcome to the family'. |
| [S38](#s38) | 5 | 10s | pov_hand | Nora, Alva, Bone Dwelling Interior | Marrow. Basically pure fat. We find long bones / smashed open at sites like this. That exact break, right through the shaft. / And now I'm eating it. |
| [S39](#s39) 🆕 | 5 | 10s | pov_hand | Nora, Alva, Bone Dwelling Interior | Soaked at the riverbank. Wet feet lose heat fast. / Dry grass inside, it pulls moisture and traps warm air. / The Alps Iceman lined his shoes like this. |
| [S40](#s40) | 5 | 10s | tripod | Nora, Alva, Bone Dwelling Interior | Alva's giving me a spot by the fire now. / Near the wall, not the door. I know what that means. / I'm not crying, it's the smoke. |
| [S41](#s41) | 6 | 10s | selfie | Nora, Alva, Bone Dwelling Interior | Hour seventeen. An eyed bone needle. / I've catalogued broken ones in museum drawers for years, never seen one used. / She's stitching without looking. Sorry. Archaeologist. |
| [S42](#s42) | 6 | 10s | pov_hand | Nora, Alva, Bone Dwelling Interior | Hide flexes, sinew pulls tight. / Awls only punch holes. The eye means finer seams, fitted sleeves, no gaps for wind. / Also beads. Lots of beads. |
| [S43](#s43) | 6 | 10s | selfie | Nora, Alva, Bone Dwelling Interior | Amber and fossil shells, / carried here from three to five hundred kilometres away. Some from the Black Sea side. / So: neighbours, trading, long before farming. |
| [S44](#s44) ✂️ | 6 | 8s | selfie | Nora, Painted Mammoth Skull, Mezhyrich Camp | Hour nineteen. That skull by the entrance. Red ochre, / dots and lines. I've only seen it in records. / Okay, breathe. |
| [S45](#s45) | 6 | 10s | selfie | Nora, Torak, Painted Mammoth Skull | Calling this a drum is controversial. / The top has worn dents, and the long bones near it are damaged to match. / Sounds like a drum to me. |
| [S46](#s46) | 6 | 10s | pov_hand | Nora, Painted Mammoth Skull | Ochre. Iron-rich earth, ground up. / It's still on my fingertips. Eighteen thousand years in the ground and the red survives. / That's how we found it. |
| [S47](#s47) | 6 | 10s | selfie | Nora, Mezhyrich Camp | Hour twenty-one. Holy cr— eyes past the bone pile. / Wolves, after scraps. Up north we argue whether skulls like theirs were early dogs. / From here? Wolves. |
| [S48](#s48) | 6 | 10s | wide | Nora, Mezhyrich Camp | Four dwellings, hearths going, the river frozen below. / On the dig it's a pit with string lines and numbered bags. / This is what the string lines meant. |
| [S49](#s49) 🆕 | 6 | 10s | wide | Nora, Mezhyrich Camp | Clear sky, colder night. Heat just radiates away. / And no Polaris up there. The pole sits near Deneb / right now. Same stars, different centre. |
| [S50](#s50) | 6 | 10s | selfie | Nora, Mezhyrich Camp | Hour twenty-two. Toes are numb again, so I'm going in. / Alva left a gap by the fire for me. / I'm not wasting it on a better shot. |
| [S51](#s51) | 7 | 10s | tripod | Nora, Alva, Bone Dwelling Interior | Hour twenty-three. Everyone's asleep. / I've spent ten years measuring this floor in centimetres. / Never thought about how warm it was. It is. Barely. |
| [S52](#s52) | 7 | 10s | tripod | Nora, Mezhyrich Camp | Hour twenty-four. First light. / My hands work, my toes probably work. / They do this every single winter. I did one day. One. |

---

## Hồi 1 — Hook (Giờ 0–1, vừa sáng)

### S01

- **Thời lượng:** 10s · **Kiểu quay:** `pov` · **Bối cảnh:** CAMP / dawn
- **Ref (character_names):** Nora, Torak, Mezhyrich Camp
- **Giọng:** in a hoarse, fast whisper
- **Vào cảnh:** opens with the tusk covering most of the frame right in front of the lens · **Ra cảnh:** fast whip pan to the right, motion blur from 8s · **Nối:** CUT inside the blur; S02 opens mid-blur and settles on Nora
- **Thoại:**
  - `0-3s` “Hour one. Central Ukraine, roughly eighteen thousand years ago,”
  - `3-7s` “coldest stretch of the Ice Age. I've dug at this site.”
  - `7-10s` “It never looked like this.”

**prompt**

```
First-person view at eye level on a snowy river terrace at dawn; a huge curved mammoth tusk carried by two hunters fills most of the frame very close to the lens; behind it, partly visible, four low mammoth-bone dwellings stand on the terrace. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; cold blue first light with a faint pink glow on the horizon.
```

**video_prompt**

```
First-person handheld smartphone footage at Nora's eye level, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; cold blue first light with a faint pink glow on the horizon. Shot: Eye-level first-person view on a snowy river terrace looking toward the camp. 0-3s: Torak and a second hunter in hooded hide parkas carry one long curved mammoth tusk on their shoulders right across the lens from left to right at walking pace, bent forward under the weight, taking short steps, the tusk bobbing with each step. Nora says from behind the camera, in a hoarse, fast whisper: "Hour one. Central Ukraine, roughly eighteen thousand years ago," 3-7s: The tusk slides out of frame to the right and reveals the camp that was already there: four low round dwellings of stacked mammoth jaws and tusks under frosted hides, thin smoke rising, on the snowy terrace above a frozen river. Nora says from behind the camera, in a hoarse, fast whisper: "coldest stretch of the Ice Age. I've dug at this site." 7-10s: The camera holds on the camp, then at 8s whips fast to the right in a motion blur. Nora says from behind the camera, in a hoarse, fast whisper: "It never looked like this." The two hunters walk on out of frame to the right without speaking. The dwellings are in the frame from the first second behind the tusk and stay completely still; nothing pops into view. The hunters' boots press into the snow and leave compressed prints. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. First-person point-of-view shot. Nora is completely behind the camera holding it firmly; her own hands stay out of the frame. No phone, no device, and no selfie stick appear anywhere in the frame. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: wind over snow, crunching footsteps, the hunters' heavy breathing, distant crackle of fires, Nora's voice.
```

### S02

- **Thời lượng:** 10s · **Kiểu quay:** `selfie` · **Bối cảnh:** CAMP / dawn
- **Ref (character_names):** Nora, Mezhyrich Camp
- **Giọng:** fast and breathless, half-smiling
- **Vào cảnh:** opens mid whip pan, motion blur settling on Nora · **Ra cảnh:** look-away: she turns her head toward the camp · **Nối:** CUT on the back of her head; S03 opens on the back of her head
- **Thoại:**
  - `0-3s` “Twenty-four hours, no tent, no gear, only what they use.”
  - `3-7s` “These people got through the harshest phase of the Ice Age”
  - `7-10s` “living around domes of mammoth bone.”

**prompt**

```
Ultra-wide selfie at arm's length on the edge of a snowy terrace at dawn, slight motion blur settling; Nora's face in the left third, the mammoth-bone camp on the right behind her. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; cold blue first light with a faint pink glow on the horizon.
```

**video_prompt**

```
Handheld front-camera vlog footage, ultra-wide 0.5x lens, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Nora holds the camera at arm's length with her right arm extended toward the bottom-right corner of the frame. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; cold blue first light with a faint pink glow on the horizon. Shot: Ultra-wide selfie at arm's length on the edge of the terrace, Nora's face in the left third, the camp on the right behind her. 0-3s: The frame opens mid-swing in motion blur and settles on Nora standing at the edge of the terrace; wind blows powder snow across the frame from right to left. Nora says, fast and breathless, half-smiling: "Twenty-four hours, no tent, no gear, only what they use." 3-7s: She talks fast, her breath vapor puffing and vanishing quickly, her ponytail and the fur of her pushed-back hood trailing in the wind; half a smile. Nora says, fast and breathless, half-smiling: "These people got through the harshest phase of the Ice Age" 7-10s: At 9s she turns her head to look back at the camp, so the back of her head and ponytail fill half the frame. Nora says, fast and breathless, half-smiling: "living around domes of mammoth bone." No one else is near her. Nora stands firmly without moving her feet; the camp behind her stays completely still. Only snow, hair and fur move with the wind. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The camera is the phone itself recording from Nora's hand, so the viewer looks directly at Nora; no phone, no phone body, no phone screen, no UI or app overlay, no case, and no selfie stick appear anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: steady wind, hissing snow, distant fire crackle, Nora's voice.
```

### S03

- **Thời lượng:** 10s · **Kiểu quay:** `back_selfie` · **Bối cảnh:** CAMP / dawn
- **Ref (character_names):** Nora, Torak, Mezhyrich Camp
- **Giọng:** in a fast nervous whisper
- **Vào cảnh:** back of her head · **Ra cảnh:** jump cut on a held still frame · **Nối:** CUT; S04 jump cut
- **Thoại:**
  - `0-3s` “Okay, that's Torak. My name for him.”
  - `3-7s` “Hand flat, palm down, probably means stay. I stay.”
  - `7-10s` “A stranger walking into a winter camp? I'd spear me too.”

**prompt**

```
Smartphone frame from just behind Nora's head at dawn: her honey-blonde ponytail and pushed-back white fox-fur hood fill the left half; on the right, about six metres away in the snow, Torak already stands holding a flint-tipped spear pointed down. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; cold blue first light with a faint pink glow on the horizon.
```

**video_prompt**

```
Handheld smartphone vlog footage that starts from Nora's raised hand just behind her head and then turns around to face her at arm's length, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; cold blue first light with a faint pink glow on the horizon. Shot: From just behind Nora's head, then turning around to a selfie. 0-3s: Torak takes two slow steps toward Nora through the snow, spear tip down, raises one hand flat, palm down, in a stop gesture, and stops about four metres away. Nora says, in a fast nervous whisper: "Okay, that's Torak. My name for him." 3-7s: Nora slowly brings the camera around her side to face herself, keeping Torak visible over her right shoulder; she stays completely still, eyes wide. Nora says, in a fast nervous whisper: "Hand flat, palm down, probably means stay. I stay." 7-10s: Torak keeps staring at her without moving; Nora gives a tight nervous smile into the camera. Nora says, in a fast nervous whisper: "A stranger walking into a winter camp? I'd spear me too." Torak never speaks; his face is wary. Torak is in the frame from the first second; nobody appears suddenly. His boots sink into the snow with each step and his heavy parka swings with a slight delay. The camera turns smoothly at arm's length and she never lets go of it. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The camera is the phone itself recording from Nora's hand; no phone, no phone body, no phone screen, no UI or app overlay, no case, and no selfie stick appear anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: wind, snow crunching under Torak's boots, Nora's tense breathing, Nora's voice.
```


---

## Hồi 2 — Đời thường (Giờ 1–8, ban ngày)

### S04

- **Thời lượng:** 10s · **Kiểu quay:** `selfie` · **Bối cảnh:** CAMP / day
- **Ref (character_names):** Nora, Torak, Mezhyrich Camp
- **Giọng:** in a fast whisper
- **Vào cảnh:** jump cut · **Ra cảnh:** her hand sweeps across the lens at 9s · **Nối:** CUT as the hand covers the lens; S05 opens with her hand entering from below
- **Thoại:**
  - `0-3s` “No, wait— see that white patch on his cheek? Frostnip.”
  - `3-7s` “Skin's starting to freeze and he can't feel it.”
  - `7-10s` “Nobody can see their own face out here.”

**prompt**

```
Ultra-wide selfie at arm's length in the camp; Nora's face in the left third; just behind her right shoulder Torak stands close, with a waxy white patch of skin on his left cheekbone. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; overcast late-winter daylight, soft flat light.
```

**video_prompt**

```
Handheld front-camera vlog footage, ultra-wide 0.5x lens, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Nora holds the camera at arm's length with her right arm extended toward the bottom-right corner of the frame. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; overcast late-winter daylight, soft flat light. Shot: Ultra-wide selfie at arm's length in the camp, Nora's face in the left third, Torak just behind her right shoulder. 0-3s: Nora glances back at Torak, then points at her own cheek with her free left hand. Nora says, in a fast whisper: "No, wait— see that white patch on his cheek? Frostnip." 3-7s: She points back over her shoulder toward Torak's cheek; Torak frowns and stays still. Nora says, in a fast whisper: "Skin's starting to freeze and he can't feel it." 7-10s: At 9s she leans toward the camera and her free hand sweeps across the lens. Nora says, in a fast whisper: "Nobody can see their own face out here." Torak stands completely still and does not speak. Only Torak's frosted beard and hood fur move in the wind. The dwellings behind stay still. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The camera is the phone itself recording from Nora's hand, so the viewer looks directly at Nora; no phone, no phone body, no phone screen, no UI or app overlay, no case, and no selfie stick appear anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: wind, quiet camp sounds, Nora's whisper, Nora's voice.
```

### S05

- **Thời lượng:** 10s · **Kiểu quay:** `pov_hand` · **Bối cảnh:** CAMP / day
- **Ref (character_names):** Nora, Torak, Mezhyrich Camp
- **Giọng:** fast and focused, then softer
- **Vào cảnh:** her hand enters from the bottom · **Ra cảnh:** POV wipe: Torak's parka crosses the lens · **Nối:** CUT when his parka covers the frame; S06 jump cut
- **Thoại:**
  - `0-3s` “Don't rub it. Rubbing frozen skin just tears it.”
  - `3-7s` “Warm hand, steady pressure, wait. Field medics still teach exactly this.”
  - `7-10s` “Okay... he's letting me.”

**prompt**

```
First-person view at eye level; Torak's bearded face about sixty centimetres away with a waxy white patch on his left cheekbone; the snowy camp behind him; Nora's bare hand entering from the bottom of the frame. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; overcast late-winter daylight, soft flat light.
```

**video_prompt**

```
First-person handheld smartphone footage at Nora's eye level, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; overcast late-winter daylight, soft flat light. Shot: First-person view at Nora's eye level, Torak's face about sixty centimetres away. 0-3s: Nora's bare empty hand rises from the bottom of the frame and presses gently and flat on the white patch on Torak's cheek; her fur mitten dangles from a cord at her wrist. Nora says from behind the camera, fast and focused, then softer: "Don't rub it. Rubbing frozen skin just tears it." 3-7s: The hand holds still with steady pressure; the skin of his cheek dents slightly under her palm; Torak looks down at the hand, then slowly nods once. Nora says from behind the camera, fast and focused, then softer: "Warm hand, steady pressure, wait. Field medics still teach exactly this." 7-10s: The hand withdraws; at 9s Torak steps sideways right across the lens from left to right, his parka filling the frame. Nora says from behind the camera, fast and focused, then softer: "Okay... he's letting me." Torak does not speak. The mitten swings on its cord with inertia as her hand moves. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. First-person point-of-view shot. Nora is completely behind the camera holding it firmly; only her bare empty hand enters the lower frame. No phone, no device, and no selfie stick appear anywhere in the frame. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: wind, faint rustle of hide, Nora's low voice, Nora's voice.
```

### S06

- **Thời lượng:** 10s · **Kiểu quay:** `selfie` · **Bối cảnh:** CAMP / day
- **Ref (character_names):** Nora, Alva, Mezhyrich Camp
- **Giọng:** half-smiling, fast
- **Vào cảnh:** jump cut · **Ra cảnh:** whip pan left, motion blur in the last half second · **Nối:** CUT in the blur; S07 opens mid-swing to the left
- **Thoại:**
  - `0-3s` “Hour two. Alva just checked my mitten cord, twice. Fair.”
  - `3-7s` “Mittens beat gloves, fingers share heat.”
  - `7-10s` “And drop one in this wind, it's gone.”

**prompt**

```
Ultra-wide selfie at arm's length between the dwellings; Nora's face left of centre; Alva stands at her right side; a fur mitten hangs on a hide cord from Nora's left wrist. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; overcast late-winter daylight, soft flat light.
```

**video_prompt**

```
Handheld front-camera vlog footage, ultra-wide 0.5x lens, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Nora holds the camera at arm's length with her right arm extended toward the bottom-right corner of the frame. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; overcast late-winter daylight, soft flat light. Shot: Ultra-wide selfie at arm's length in an open space between dwellings, Alva at Nora's right. 0-3s: Alva takes the hide cord at Nora's left wrist and tugs it twice; Nora's wrist jerks slightly with each tug. Nora says, half-smiling, fast: "Hour two. Alva just checked my mitten cord, twice. Fair." 3-7s: Alva nods once, satisfied; Nora half-smiles into the camera, the mitten swinging on its cord. Nora says, half-smiling, fast: "Mittens beat gloves, fingers share heat." 7-10s: Nora lifts the mitten to show it; at 9.5s she swings the camera fast to the left in a motion blur. Nora says, half-smiling, fast: "And drop one in this wind, it's gone." Alva does not speak. The cord pulls tight, then goes slack. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The camera is the phone itself recording from Nora's hand, so the viewer looks directly at Nora; no phone, no phone body, no phone screen, no UI or app overlay, no case, and no selfie stick appear anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: wind, muffled camp sounds, Nora's voice.
```

### S07

- **Thời lượng:** 10s · **Kiểu quay:** `selfie` · **Bối cảnh:** CAMP / day
- **Ref (character_names):** Nora, Mezhyrich Camp
- **Giọng:** fast, geeking out
- **Vào cảnh:** mid-swing blur settling · **Ra cảnh:** jump cut · **Nối:** CUT
- **Thoại:**
  - `0-3s` “Lower jaws, stacked in that zigzag.”
  - `3-7s` “I've walked around the museum reconstruction maybe fifty times.”
  - `7-10s` “Never once with smoke coming out the top. Okay, okay, focus.”

**prompt**

```
Ultra-wide selfie at arm's length beside a mammoth-bone dwelling, motion blur settling; on the left of the frame the dwelling's wall base of mammoth lower jaws stacked in a tight zigzag; Nora's face right of centre. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; overcast late-winter daylight, soft flat light.
```

**video_prompt**

```
Handheld front-camera vlog footage, ultra-wide 0.5x lens, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Nora holds the camera at arm's length with her right arm extended toward the bottom-right corner of the frame. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; overcast late-winter daylight, soft flat light. Shot: Ultra-wide selfie at arm's length walking slowly backward alongside a dwelling, the jaw wall on the left of the frame. 0-3s: The frame settles from a leftward swing onto Nora, who walks slowly backward alongside the dwelling at about half a metre per second. Nora says, fast, geeking out: "Lower jaws, stacked in that zigzag." 3-7s: The jaw wall slides slowly past on the left as she walks; thin smoke rises from the top of the dome and bends in the wind. Nora says, fast, geeking out: "I've walked around the museum reconstruction maybe fifty times." 7-10s: She glances up at the smoke, grins, then shakes her head at herself. Nora says, fast, geeking out: "Never once with smoke coming out the top. Okay, okay, focus." No locals in the shot. The dwelling is solid and completely still; it only slides past because she walks. Slight vertical bounce with each step. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The camera is the phone itself recording from Nora's hand, so the viewer looks directly at Nora; no phone, no phone body, no phone screen, no UI or app overlay, no case, and no selfie stick appear anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: wind, crunching snow, crackle from inside the dwelling, Nora's voice.
```

### S08

- **Thời lượng:** 10s · **Kiểu quay:** `selfie` · **Bối cảnh:** CAMP / day
- **Ref (character_names):** Nora, Mezhyrich Camp
- **Giọng:** low-voiced
- **Vào cảnh:** jump cut · **Ra cảnh:** walk-through: she ducks through the hide flap and the frame goes dark · **Nối:** CUT on dark; S09 opens from dark inside
- **Thoại:**
  - `0-3s` “Real talk, we still argue what these were.”
  - `3-7s` “Homes, food stores, maybe monuments. Newer dating says people weren't here long.”
  - `7-10s` “Someone's clearly sleeping in this one.”

**prompt**

```
Ultra-wide selfie at arm's length in front of a dwelling entrance; a pair of curved mammoth tusks arch over a low hide-covered doorway on the right; Nora's face on the left. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; overcast late-winter daylight, soft flat light.
```

**video_prompt**

```
Handheld front-camera vlog footage, ultra-wide 0.5x lens, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Nora holds the camera at arm's length with her right arm extended toward the bottom-right corner of the frame. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; overcast late-winter daylight, soft flat light. Shot: Ultra-wide selfie at arm's length in front of a dwelling entrance arched with tusks. 0-3s: Nora stands in front of the tusk-arched entrance and speaks low. Nora says, low-voiced: "Real talk, we still argue what these were." 3-7s: The hide flap over the doorway sways slightly in the wind; she glances at it. Nora says, low-voiced: "Homes, food stores, maybe monuments. Newer dating says people weren't here long." 7-10s: At 8.5s she turns her head toward the doorway and ducks through the hide flap, so the back of her head fills the frame and the image goes dark. Nora says, low-voiced: "Someone's clearly sleeping in this one." No locals in the shot. The tusk arch and the dwelling stay completely still. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The camera is the phone itself recording from Nora's hand, so the viewer looks directly at Nora; no phone, no phone body, no phone screen, no UI or app overlay, no case, and no selfie stick appear anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: wind, rustle of the hide flap, faint sleeping breath inside, Nora's voice.
```

### S09

- **Thời lượng:** 10s · **Kiểu quay:** `selfie` · **Bối cảnh:** INT / day_in
- **Ref (character_names):** Nora, Alva, Bone Dwelling Interior
- **Giọng:** fast, rubbing her hands warm
- **Vào cảnh:** from dark into firelight · **Ra cảnh:** her hand reaches toward the lens · **Nối:** CUT; S10 POV with her hand
- **Thoại:**
  - `0-3s` “Hardly any trees out here, so Alva burns bone.”
  - `3-7s` “The greasy ends, mostly. We find barely any charcoal in these hearths.”
  - `7-10s` “That's why, probably.”

**prompt**

```
Inside the dwelling, the frame brightening from dark into firelight; Nora's face lit warm on the left; the central bone hearth behind her with Alva sitting beside it. Setting: inside a mammoth-bone dwelling at Mezhyrich, central Ukraine, about 16,000 BC: a low dome of tusks and long bones between hanging reindeer hides, a shallow stone-ringed central hearth burning greasy bone ends (no wood anywhere), fur hides on the floor, a hide water bag hanging from a bone tripod, a low bone ledge along the wall; warm firelight from the hearth mixed with cold blue daylight from the low entrance.
```

**video_prompt**

```
Handheld front-camera vlog footage, ultra-wide 0.5x lens, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Nora holds the camera at arm's length with her right arm extended toward the bottom-right corner of the frame. Setting: inside a mammoth-bone dwelling at Mezhyrich, central Ukraine, about 16,000 BC: a low dome of tusks and long bones between hanging reindeer hides, a shallow stone-ringed central hearth burning greasy bone ends (no wood anywhere), fur hides on the floor, a hide water bag hanging from a bone tripod, a low bone ledge along the wall; warm firelight from the hearth mixed with cold blue daylight from the low entrance. Shot: Ultra-wide selfie inside the dwelling, the hearth behind Nora. 0-3s: The image brightens from dark into warm firelight; Nora rubs her cold free hand on her sleeve. Nora says, fast, rubbing her hands warm: "Hardly any trees out here, so Alva burns bone." 3-7s: Behind her, Alva places a greasy mammoth bone end onto the hearth; the flames lick up slowly around it. Nora says, fast, rubbing her hands warm: "The greasy ends, mostly. We find barely any charcoal in these hearths." 7-10s: Fat on the bone sizzles softly and smoke rises toward the smoke hole; at 9s Nora reaches her free hand toward the lens. Nora says, fast, rubbing her hands warm: "That's why, probably." Alva does not speak. The flames catch gradually, with no burst; there is no wood or log anywhere, only bone. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The camera is the phone itself recording from Nora's hand, so the viewer looks directly at Nora; no phone, no phone body, no phone screen, no UI or app overlay, no case, and no selfie stick appear anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: crackling bone fire, soft sizzle of fat, wind outside, Nora's voice.
```

### S10

- **Thời lượng:** 10s · **Kiểu quay:** `pov_hand` · **Bối cảnh:** INT / day_in
- **Ref (character_names):** Nora, Alva, Bone Dwelling Interior
- **Giọng:** with a dry laugh, from behind the camera
- **Vào cảnh:** her hand already in the lower frame · **Ra cảnh:** steam drifts across the lens · **Nối:** CUT in the steam; S11 opens as the steam clears
- **Thoại:**
  - `0-3s` “Yeah, I know, I know.”
  - `3-7s` “Don't eat snow, ever. Your body burns its own heat just melting it.”
  - `7-10s` “I was testing her. Mostly.”

**prompt**

```
First-person view sitting inside the dwelling near the hearth; Nora's bare hand at the bottom of the frame holding a scoop of snow; Alva sitting on the left by the fire. Setting: inside a mammoth-bone dwelling at Mezhyrich, central Ukraine, about 16,000 BC: a low dome of tusks and long bones between hanging reindeer hides, a shallow stone-ringed central hearth burning greasy bone ends (no wood anywhere), fur hides on the floor, a hide water bag hanging from a bone tripod, a low bone ledge along the wall; warm firelight from the hearth mixed with cold blue daylight from the low entrance.
```

**video_prompt**

```
First-person handheld smartphone footage at Nora's eye level, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Setting: inside a mammoth-bone dwelling at Mezhyrich, central Ukraine, about 16,000 BC: a low dome of tusks and long bones between hanging reindeer hides, a shallow stone-ringed central hearth burning greasy bone ends (no wood anywhere), fur hides on the floor, a hide water bag hanging from a bone tripod, a low bone ledge along the wall; warm firelight from the hearth mixed with cold blue daylight from the low entrance. Shot: First-person view sitting by the hearth. 0-3s: Nora's bare hand lifts the scoop of snow toward the lens. Nora says from behind the camera, with a dry laugh, from behind the camera: "Yeah, I know, I know." 3-7s: Alva's hand comes in from the left and grips Nora's wrist, stopping it; Alva shakes her head; snow crumbles from the palm. Nora says from behind the camera, with a dry laugh, from behind the camera: "Don't eat snow, ever. Your body burns its own heat just melting it." 7-10s: Nora lowers her hand and lets the snow fall; at 9s steam from a hide water bag drifts across the lens and fogs the frame. Nora says from behind the camera, with a dry laugh, from behind the camera: "I was testing her. Mostly." Alva does not speak. Snow falls loosely from her palm. First-person point-of-view shot. Nora is completely behind the camera holding it firmly; only her bare hand, holding nothing but a scoop of snow, enters the lower frame. No phone, no device, and no selfie stick appear anywhere in the frame. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: fire crackle, Nora's laugh, Nora's voice.
```

### S11

- **Thời lượng:** 10s · **Kiểu quay:** `selfie` · **Bối cảnh:** INT / day_in
- **Ref (character_names):** Nora, Alva, Bone Dwelling Interior
- **Giọng:** fast, hands busy
- **Vào cảnh:** steam clearing · **Ra cảnh:** jump cut · **Nối:** CUT
- **Thoại:**
  - `0-3s` “Hot stone into a hide bag.”
  - `3-7s` “Hide can't sit on a flame, it burns. We dig up heat-cracked rock”
  - `7-10s` “at sites like this. Probably from exactly this.”

**prompt**

```
Ultra-wide selfie inside the dwelling, steam clearing; a hide water bag hanging from a bone tripod behind Nora's left shoulder; Alva beside it gripping a glowing hot stone between two bone sticks. Setting: inside a mammoth-bone dwelling at Mezhyrich, central Ukraine, about 16,000 BC: a low dome of tusks and long bones between hanging reindeer hides, a shallow stone-ringed central hearth burning greasy bone ends (no wood anywhere), fur hides on the floor, a hide water bag hanging from a bone tripod, a low bone ledge along the wall; warm firelight from the hearth mixed with cold blue daylight from the low entrance.
```

**video_prompt**

```
Handheld front-camera vlog footage, ultra-wide 0.5x lens, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Nora holds the camera at arm's length with her right arm extended toward the bottom-right corner of the frame. Setting: inside a mammoth-bone dwelling at Mezhyrich, central Ukraine, about 16,000 BC: a low dome of tusks and long bones between hanging reindeer hides, a shallow stone-ringed central hearth burning greasy bone ends (no wood anywhere), fur hides on the floor, a hide water bag hanging from a bone tripod, a low bone ledge along the wall; warm firelight from the hearth mixed with cold blue daylight from the low entrance. Shot: Ultra-wide selfie inside, the hide water bag behind Nora's left shoulder. 0-3s: Alva lowers the hot stone with the bone sticks into the hide bag. Nora says, fast, hands busy: "Hot stone into a hide bag." 3-7s: Water bubbles rapidly around the submerged stone and steam rises gradually; the bag sags slightly under the stone's weight. Nora says, fast, hands busy: "Hide can't sit on a flame, it burns. We dig up heat-cracked rock" 7-10s: Nora nods at the bag as the steam slowly thickens. Nora says, fast, hands busy: "at sites like this. Probably from exactly this." Alva does not speak. Only localized bubbling around the stone, no instant violent boil; steam rises by convection. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The camera is the phone itself recording from Nora's hand, so the viewer looks directly at Nora; no phone, no phone body, no phone screen, no UI or app overlay, no case, and no selfie stick appear anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: hiss and bubbling water, fire crackle, Nora's voice.
```

### S12

> 🆕 Cảnh mới trong bản 52 cảnh.

- **Thời lượng:** 10s · **Kiểu quay:** `selfie` · **Bối cảnh:** INT / day_in
- **Ref (character_names):** Nora, Alva, Bone Dwelling Interior
- **Giọng:** fast, between sips
- **Vào cảnh:** jump cut · **Ra cảnh:** jump cut · **Nối:** CUT; S13 opens on a static frame
- **Thoại:**
  - `0-3s` “Drinking before I'm thirsty. Cold makes you pee more”
  - `3-7s` “and quietly switches thirst off. Dehydration probably makes frostbite likelier.”
  - `7-10s` “So: warm water, small sips, all day.”

**prompt**

```
Ultra-wide selfie inside the dwelling by the hearth; Alva stands at Nora's left holding the hide water bag, a thin wisp of steam rising from its open mouth. Setting: inside a mammoth-bone dwelling at Mezhyrich, central Ukraine, about 16,000 BC: a low dome of tusks and long bones between hanging reindeer hides, a shallow stone-ringed central hearth burning greasy bone ends (no wood anywhere), fur hides on the floor, a hide water bag hanging from a bone tripod, a low bone ledge along the wall; warm firelight from the hearth mixed with cold blue daylight from the low entrance.
```

**video_prompt**

```
Handheld front-camera vlog footage, ultra-wide 0.5x lens, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Nora holds the camera at arm's length with her right arm extended toward the bottom-right corner of the frame. Setting: inside a mammoth-bone dwelling at Mezhyrich, central Ukraine, about 16,000 BC: a low dome of tusks and long bones between hanging reindeer hides, a shallow stone-ringed central hearth burning greasy bone ends (no wood anywhere), fur hides on the floor, a hide water bag hanging from a bone tripod, a low bone ledge along the wall; warm firelight from the hearth mixed with cold blue daylight from the low entrance. Shot: Ultra-wide selfie inside the dwelling by the hearth, Alva at Nora's left holding the hide water bag. 0-3s: Alva lifts the hide water bag off the bone tripod and holds its open mouth toward Nora; Nora takes it with her free left hand. Nora says, fast, between sips: "Drinking before I'm thirsty. Cold makes you pee more" 3-7s: Nora tips the bag and takes two small sips of warm water, then wipes her lips with the back of her hand. Nora says, fast, between sips: "and quietly switches thirst off. Dehydration probably makes frostbite likelier." 7-10s: She hands the bag back to Alva, who hangs it on the tripod again; Nora nods at the camera. Nora says, fast, between sips: "So: warm water, small sips, all day." Alva does not speak. The full hide bag is soft and heavy and sags in her hand; the water sloshes slightly inside; only a thin wisp of steam rises. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The camera is the phone itself recording from Nora's hand, so the viewer looks directly at Nora; no phone, no phone body, no phone screen, no UI or app overlay, no case, and no selfie stick appear anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: fire crackle, water sloshing in the hide bag, small swallows, Nora's voice.
```

### S13

- **Thời lượng:** 10s · **Kiểu quay:** `tripod` · **Bối cảnh:** INT / day_in
- **Ref (character_names):** Nora, Alva, Bone Dwelling Interior
- **Giọng:** fast, chewing
- **Vào cảnh:** static frame · **Ra cảnh:** hard cut · **Nối:** CUT
- **Thoại:**
  - `0-3s` “Every bite of meat, she hands me a lump of fat.”
  - `3-7s` “Lean meat alone in this cold makes you sick. The fat's the actual fuel.”
  - `7-10s` “Tastes like candle.”

**prompt**

```
Static frame from a phone propped on a bone ledge about half a metre high, looking level at Nora sitting by the hearth; Alva sits to her right. Setting: inside a mammoth-bone dwelling at Mezhyrich, central Ukraine, about 16,000 BC: a low dome of tusks and long bones between hanging reindeer hides, a shallow stone-ringed central hearth burning greasy bone ends (no wood anywhere), fur hides on the floor, a hide water bag hanging from a bone tripod, a low bone ledge along the wall; warm firelight from the hearth mixed with cold blue daylight from the low entrance.
```

**video_prompt**

```
Static smartphone footage from a phone propped on a ledge, locked-off frame, natural smartphone perspective, photorealistic documentary realism. Setting: inside a mammoth-bone dwelling at Mezhyrich, central Ukraine, about 16,000 BC: a low dome of tusks and long bones between hanging reindeer hides, a shallow stone-ringed central hearth burning greasy bone ends (no wood anywhere), fur hides on the floor, a hide water bag hanging from a bone tripod, a low bone ledge along the wall; warm firelight from the hearth mixed with cold blue daylight from the low entrance. Shot: Locked-off frame from a bone ledge about half a metre high, looking level at Nora by the hearth. 0-3s: Alva hands Nora a lump of soft white fat together with a strip of meat. Nora says, fast, chewing: "Every bite of meat, she hands me a lump of fat." 3-7s: Nora chews, talking fast with her mouth half full. Nora says, fast, chewing: "Lean meat alone in this cold makes you sick. The fat's the actual fuel." 7-10s: She grimaces at the taste, then keeps eating; Alva watches, amused. Nora says, fast, chewing: "Tastes like candle." Alva does not speak. The fat is soft and squashes slightly in her fingers. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The phone is the camera, resting still on a ledge; the frame never moves, and no phone, tripod or selfie stick appears anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: fire crackle, chewing, Nora's voice.
```

### S14

- **Thời lượng:** 10s · **Kiểu quay:** `selfie` · **Bối cảnh:** CAMP / day
- **Ref (character_names):** Nora, Torak, Mezhyrich Camp
- **Giọng:** fast, excited
- **Vào cảnh:** jump cut · **Ra cảnh:** whip pan right, motion blur · **Nối:** CUT in the blur; S15 opens mid-swing
- **Thoại:**
  - `0-3s` “Hour four. These pits ring every hut.”
  - `3-7s` “We dig them out full of bone. Ground's frozen year-round here,”
  - `7-10s` “so most of us think: freezers. And... yep. Meat.”

**prompt**

```
Ultra-wide selfie outside beside a dwelling; behind Nora's left shoulder Torak kneels at a shallow pit covered with a stiff frozen hide. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; overcast late-winter daylight, soft flat light.
```

**video_prompt**

```
Handheld front-camera vlog footage, ultra-wide 0.5x lens, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Nora holds the camera at arm's length with her right arm extended toward the bottom-right corner of the frame. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; overcast late-winter daylight, soft flat light. Shot: Ultra-wide selfie outside beside a dwelling, the covered pit behind Nora's left shoulder. 0-3s: Torak grips the edge of the hide cover. Nora says, fast, excited: "Hour four. These pits ring every hut." 3-7s: He lifts the stiff frozen hide from left to right; snow slides off it and frozen chunks of meat are revealed inside the pit. Nora says, fast, excited: "We dig them out full of bone. Ground's frozen year-round here," 7-10s: Nora leans to look, eyebrows up; at 9.5s she swings the camera fast to the right. Nora says, fast, excited: "so most of us think: freezers. And... yep. Meat." Torak does not speak. The frozen hide is stiff and bends only at the corner; the meat is in the pit from the start. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The camera is the phone itself recording from Nora's hand, so the viewer looks directly at Nora; no phone, no phone body, no phone screen, no UI or app overlay, no case, and no selfie stick appear anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: wind, creak of frozen hide, Nora's voice.
```

### S15

- **Thời lượng:** 10s · **Kiểu quay:** `selfie` · **Bối cảnh:** CAMP / day
- **Ref (character_names):** Nora, Torak, Mezhyrich Camp
- **Giọng:** fast, dry
- **Vào cảnh:** mid-swing blur · **Ra cảnh:** jump cut · **Nối:** CUT
- **Thoại:**
  - `0-3s` “Fox pelts, tails still on.”
  - `3-7s` “We find tons of fox bones at this site and wondered why.”
  - `7-10s` “Not dinner. Coats. Maybe also dinner.”

**prompt**

```
Ultra-wide selfie, motion blur settling; behind Nora, Torak stretches white arctic-fox pelts with the tails still on across a frame of bones. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; overcast late-winter daylight, soft flat light.
```

**video_prompt**

```
Handheld front-camera vlog footage, ultra-wide 0.5x lens, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Nora holds the camera at arm's length with her right arm extended toward the bottom-right corner of the frame. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; overcast late-winter daylight, soft flat light. Shot: Ultra-wide selfie, a pelt-stretching frame behind Nora. 0-3s: The frame settles on Nora; behind her Torak pulls a sinew cord tight on a fox pelt. Nora says, fast, dry: "Fox pelts, tails still on." 3-7s: The pelts stretch taut, their bushy tails swaying in the wind. Nora says, fast, dry: "We find tons of fox bones at this site and wondered why." 7-10s: Nora shrugs at the camera, deadpan. Nora says, fast, dry: "Not dinner. Coats. Maybe also dinner." Torak does not speak. The pelts stretch and the fur ripples in the wind. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The camera is the phone itself recording from Nora's hand, so the viewer looks directly at Nora; no phone, no phone body, no phone screen, no UI or app overlay, no case, and no selfie stick appear anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: wind, sinew cord creaking, Nora's voice.
```

### S16

- **Thời lượng:** 10s · **Kiểu quay:** `selfie` · **Bối cảnh:** CAMP / day
- **Ref (character_names):** Nora, Alva, Mezhyrich Camp
- **Giọng:** half-laughing, proud
- **Vào cảnh:** jump cut · **Ra cảnh:** jump cut · **Nối:** CUT
- **Thoại:**
  - `0-3s` “She likes my belt.”
  - `3-7s` “Fox canines, drilled and sewn on. Copied from a burial at Sungir,”
  - `7-10s` “way north of here, over two hundred teeth. Nailed it, apparently.”

**prompt**

```
Ultra-wide selfie held a little high; Alva stands at Nora's right; Nora's wide leather belt sewn with rows of drilled arctic-fox canine teeth is visible at the bottom edge of the frame. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; overcast late-winter daylight, soft flat light.
```

**video_prompt**

```
Handheld front-camera vlog footage, ultra-wide 0.5x lens, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Nora holds the camera at arm's length with her right arm extended toward the bottom-right corner of the frame. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; overcast late-winter daylight, soft flat light. Shot: Ultra-wide selfie held a little high, Alva at Nora's right, the fox-tooth belt at the bottom edge. 0-3s: Alva points at Nora's belt. Nora says, half-laughing, proud: "She likes my belt." 3-7s: Alva bends and touches one fox tooth with a fingertip; the teeth click softly against each other. Nora says, half-laughing, proud: "Fox canines, drilled and sewn on. Copied from a burial at Sungir," 7-10s: Alva straightens up, nods and smiles slightly; Nora grins proudly. Nora says, half-laughing, proud: "way north of here, over two hundred teeth. Nailed it, apparently." Alva does not speak. The teeth swing and tap together lightly. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The camera is the phone itself recording from Nora's hand, so the viewer looks directly at Nora; no phone, no phone body, no phone screen, no UI or app overlay, no case, and no selfie stick appear anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: wind, soft clicking of teeth, Nora's voice.
```

### S17

> 🆕 Cảnh mới trong bản 52 cảnh.

- **Thời lượng:** 10s · **Kiểu quay:** `selfie` · **Bối cảnh:** CAMP / day
- **Ref (character_names):** Nora, Alva, Mezhyrich Camp
- **Giọng:** fast, low, watching closely
- **Vào cảnh:** jump cut · **Ra cảnh:** jump cut · **Nối:** CUT
- **Thoại:**
  - `0-3s` “Flint end-scraper. Every scrap of fat comes off,”
  - `3-7s` “or the hide rots. Dwelling one here had these stored inside,”
  - `7-10s` “right next to the flint cores. Same tool.”

**prompt**

```
Low ultra-wide selfie, Nora crouching in the camp; behind her right shoulder Alva kneels over a fresh reindeer hide pegged flat on the snow, flesh side up, a small flint scraper in her hand. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; overcast late-winter daylight, soft flat light.
```

**video_prompt**

```
Handheld front-camera vlog footage, ultra-wide 0.5x lens, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Nora holds the camera at arm's length with her right arm extended toward the bottom-right corner of the frame. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; overcast late-winter daylight, soft flat light. Shot: Low ultra-wide selfie, Nora crouching; behind her right shoulder Alva kneels over a reindeer hide pegged flat on the snow. 0-3s: Alva pushes the flint scraper across the flesh side of the hide in short firm strokes away from her body; thin curls of white fat and membrane peel up ahead of the edge. Nora says, fast, low, watching closely: "Flint end-scraper. Every scrap of fat comes off," 3-7s: She flicks the curls off onto the snow and keeps stroking; the scraped area turns pale and smooth. Nora says, fast, low, watching closely: "or the hide rots. Dwelling one here had these stored inside," 7-10s: Alva holds the scraper up for a second so its rounded working edge is visible, then goes back to work; Nora nods. Nora says, fast, low, watching closely: "right next to the flint cores. Same tool." Alva does not speak. The hide is pegged flat and does not slide; only the scraper and Alva's hands move; the fat comes off in thin curls, not chunks. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The camera is the phone itself recording from Nora's hand, so the viewer looks directly at Nora; no phone, no phone body, no phone screen, no UI or app overlay, no case, and no selfie stick appear anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: wind, rasping scrape of flint on hide, Nora's voice.
```

### S18

- **Thời lượng:** 10s · **Kiểu quay:** `selfie` · **Bối cảnh:** STEP / day
- **Ref (character_names):** Nora, Torak, Mammoth Steppe
- **Giọng:** breathing hard, fast
- **Vào cảnh:** jump cut · **Ra cảnh:** jump cut · **Nối:** CUT
- **Thoại:**
  - `0-3s` “Hour six. Hauling bone makes me sweat, and damp fur stops insulating.”
  - `3-7s` “So I open up before I'm hot, not after.”
  - `7-10s` “Torak's already done it.”

**prompt**

```
Ultra-wide selfie on open snowy steppe; Nora and, behind her, Torak both grip one long mammoth leg bone lying in the snow. Setting: the Ice Age mammoth steppe near Mezhyrich, central Ukraine, about 16,000 BC: wind-scoured snow with dry golden grass tufts, a rolling treeless plain, a broad frozen river valley below with a steep three-metre snowy riverbank whose top lip is glazed with shiny ice; overcast late-winter daylight, soft flat light.
```

**video_prompt**

```
Handheld front-camera vlog footage, ultra-wide 0.5x lens, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Nora holds the camera at arm's length with her right arm extended toward the bottom-right corner of the frame. Setting: the Ice Age mammoth steppe near Mezhyrich, central Ukraine, about 16,000 BC: wind-scoured snow with dry golden grass tufts, a rolling treeless plain, a broad frozen river valley below with a steep three-metre snowy riverbank whose top lip is glazed with shiny ice; overcast late-winter daylight, soft flat light. Shot: Ultra-wide selfie on open snowy steppe, Nora and Torak dragging a bone. 0-3s: Nora (with her free hand) and Torak drag the heavy bone slowly sideways to the left, leaning forward with short steps; the bone carves a groove in the snow. Nora says, breathing hard, fast: "Hour six. Hauling bone makes me sweat, and damp fur stops insulating." 3-7s: Nora stops and, with her free hand, loosens the leather ties at the collar of her parka. Nora says, breathing hard, fast: "So I open up before I'm hot, not after." 7-10s: She tilts the camera toward Torak, whose collar is already open. Nora says, breathing hard, fast: "Torak's already done it." Torak does not speak. The bone is heavy: both lean forward and move slowly; the snow is pushed aside into a groove. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The camera is the phone itself recording from Nora's hand, so the viewer looks directly at Nora; no phone, no phone body, no phone screen, no UI or app overlay, no case, and no selfie stick appear anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: wind, scraping bone on snow, heavy breathing, Nora's voice.
```

### S19

- **Thời lượng:** 10s · **Kiểu quay:** `selfie` · **Bối cảnh:** STEP / day
- **Ref (character_names):** Nora, Torak, Mammoth Steppe
- **Giọng:** fast, breath steaming
- **Vào cảnh:** jump cut · **Ra cảnh:** jump cut · **Nối:** CUT
- **Thoại:**
  - `0-3s` “Big debate in my field:”
  - `3-7s` “did they hunt all these mammoths, or collect bones from old natural piles?”
  - `7-10s` “This one's been dead for years. So today, collecting.”

**prompt**

```
Ultra-wide selfie at the edge of a shallow ravine on the steppe; below, behind Nora's shoulder, Torak stands at an old weathered pile of mammoth bones half buried in snow. Setting: the Ice Age mammoth steppe near Mezhyrich, central Ukraine, about 16,000 BC: wind-scoured snow with dry golden grass tufts, a rolling treeless plain, a broad frozen river valley below with a steep three-metre snowy riverbank whose top lip is glazed with shiny ice; overcast late-winter daylight, soft flat light.
```

**video_prompt**

```
Handheld front-camera vlog footage, ultra-wide 0.5x lens, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Nora holds the camera at arm's length with her right arm extended toward the bottom-right corner of the frame. Setting: the Ice Age mammoth steppe near Mezhyrich, central Ukraine, about 16,000 BC: wind-scoured snow with dry golden grass tufts, a rolling treeless plain, a broad frozen river valley below with a steep three-metre snowy riverbank whose top lip is glazed with shiny ice; overcast late-winter daylight, soft flat light. Shot: Ultra-wide selfie at the edge of a shallow ravine, Torak below behind Nora's shoulder. 0-3s: Torak grips a weathered tusk sticking out of the pile with both hands. Nora says, fast, breath steaming: "Big debate in my field:" 3-7s: He pulls; the tusk inches out, the snow cracks around it and frozen chunks fall. Nora says, fast, breath steaming: "did they hunt all these mammoths, or collect bones from old natural piles?" 7-10s: The tusk comes free; it is grey and cracked with age. Nora says, fast, breath steaming: "This one's been dead for years. So today, collecting." Torak does not speak. The tusk comes out bit by bit, not all at once; the bone pile is there from the first second. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The camera is the phone itself recording from Nora's hand, so the viewer looks directly at Nora; no phone, no phone body, no phone screen, no UI or app overlay, no case, and no selfie stick appear anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: wind, cracking frozen snow, Torak grunting, Nora's voice.
```

### S20

- **Thời lượng:** 10s · **Kiểu quay:** `selfie` · **Bối cảnh:** STEP / day
- **Ref (character_names):** Nora, Torak, Mammoth Steppe
- **Giọng:** shouting over the wind, fast · **Bleep tại:** 1.4s
- **Vào cảnh:** jump cut · **Ra cảnh:** blown snow covers the lens · **Nối:** CUT on white; S21 opens as the snow melts off the lens
- **Thoại:**
  - `0-3s` “Wind's picking up— sh— that's the real killer, not the temperature.”
  - `3-7s` “Same cold, twice the wind, you lose heat way faster.”
  - `7-10s` “Torak's already heading in.”

**prompt**

```
Ultra-wide selfie on the steppe; wind blowing snow low across the ground from right to left; far behind, Torak walks away toward the camp with his back to the camera. Setting: the Ice Age mammoth steppe near Mezhyrich, central Ukraine, about 16,000 BC: wind-scoured snow with dry golden grass tufts, a rolling treeless plain, a broad frozen river valley below with a steep three-metre snowy riverbank whose top lip is glazed with shiny ice; overcast late-winter daylight, soft flat light.
```

**video_prompt**

```
Handheld front-camera vlog footage, ultra-wide 0.5x lens, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Nora holds the camera at arm's length with her right arm extended toward the bottom-right corner of the frame. Setting: the Ice Age mammoth steppe near Mezhyrich, central Ukraine, about 16,000 BC: wind-scoured snow with dry golden grass tufts, a rolling treeless plain, a broad frozen river valley below with a steep three-metre snowy riverbank whose top lip is glazed with shiny ice; overcast late-winter daylight, soft flat light. Shot: Ultra-wide selfie on the steppe, wind from the right. 0-3s: The wind gusts harder and snow streams across the frame; Nora squints and leans into the wind. Nora says, shouting over the wind, fast: "Wind's picking up— sh— that's the real killer, not the temperature." 3-7s: Far behind her Torak keeps walking away, getting smaller. Nora says, shouting over the wind, fast: "Same cold, twice the wind, you lose heat way faster." 7-10s: At 9s a gust of blown snow sweeps over and covers the lens completely. Nora says, shouting over the wind, fast: "Torak's already heading in." Torak does not speak. Nora leans into the wind but her feet stay planted; Torak only gets smaller as he walks away. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The camera is the phone itself recording from Nora's hand, so the viewer looks directly at Nora; no phone, no phone body, no phone screen, no UI or app overlay, no case, and no selfie stick appear anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: howling wind, hissing snow, Nora's voice.
```

### S21

- **Thời lượng:** 10s · **Kiểu quay:** `selfie` · **Bối cảnh:** INT / day_in
- **Ref (character_names):** Nora, Alva, Bone Dwelling Interior
- **Giọng:** teeth chattering, fast
- **Vào cảnh:** snow melting off the lens · **Ra cảnh:** hard cut · **Nối:** CUT
- **Thoại:**
  - `0-3s` “Hour eight. Warm hands in your armpits, not over the fire.”
  - `3-7s` “Numb skin can't feel a burn.”
  - `7-10s` “Alva's doing the same thing, so I'm in good company.”

**prompt**

```
Inside the dwelling; the frame is white with snow on the lens, clearing to show Nora in firelight; Alva behind her by the hearth. Setting: inside a mammoth-bone dwelling at Mezhyrich, central Ukraine, about 16,000 BC: a low dome of tusks and long bones between hanging reindeer hides, a shallow stone-ringed central hearth burning greasy bone ends (no wood anywhere), fur hides on the floor, a hide water bag hanging from a bone tripod, a low bone ledge along the wall; warm firelight from the hearth mixed with cold blue daylight from the low entrance.
```

**video_prompt**

```
Handheld front-camera vlog footage, ultra-wide 0.5x lens, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Nora holds the camera at arm's length with her right arm extended toward the bottom-right corner of the frame. Setting: inside a mammoth-bone dwelling at Mezhyrich, central Ukraine, about 16,000 BC: a low dome of tusks and long bones between hanging reindeer hides, a shallow stone-ringed central hearth burning greasy bone ends (no wood anywhere), fur hides on the floor, a hide water bag hanging from a bone tripod, a low bone ledge along the wall; warm firelight from the hearth mixed with cold blue daylight from the low entrance. Shot: Ultra-wide selfie inside the dwelling, Alva behind Nora by the hearth. 0-3s: The snow melts off the lens; Nora brushes snow from her hood fur with her free hand. Nora says, teeth chattering, fast: "Hour eight. Warm hands in your armpits, not over the fire." 3-7s: She tucks her free left hand into her right armpit, shivering. Nora says, teeth chattering, fast: "Numb skin can't feel a burn." 7-10s: Behind her, Alva also sits with both hands tucked into her armpits. Nora says, teeth chattering, fast: "Alva's doing the same thing, so I'm in good company." Alva does not speak. Snow drops off the hood fur in small clumps. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The camera is the phone itself recording from Nora's hand, so the viewer looks directly at Nora; no phone, no phone body, no phone screen, no UI or app overlay, no case, and no selfie stick appear anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: fire crackle, wind outside, chattering teeth, Nora's voice.
```


---

## Hồi 3 — Quyền lực (Giờ 9–12, chiều, nắng xiên)

### S22

- **Thời lượng:** 10s · **Kiểu quay:** `selfie` · **Bối cảnh:** CAMP / afternoon
- **Ref (character_names):** Nora, Torak, Mezhyrich Camp
- **Giọng:** in a fast whisper
- **Vào cảnh:** jump cut · **Ra cảnh:** jump cut · **Nối:** CUT
- **Thoại:**
  - `0-3s` “Hour nine. Torak's back from the ridge,”
  - `3-7s` “arm swinging low like a trunk. Herd. And he wants me along.”
  - `7-10s` “Not sure if that's trust or bait.”

**prompt**

```
Ultra-wide selfie on the terrace in afternoon light; behind Nora, Torak is already walking toward her from the terrace edge. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; low afternoon sun, long shadows, golden light on the snow.
```

**video_prompt**

```
Handheld front-camera vlog footage, ultra-wide 0.5x lens, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Nora holds the camera at arm's length with her right arm extended toward the bottom-right corner of the frame. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; low afternoon sun, long shadows, golden light on the snow. Shot: Ultra-wide selfie on the terrace, the terrace edge behind Nora. 0-3s: Torak walks toward Nora at walking pace, growing larger. Nora says, in a fast whisper: "Hour nine. Torak's back from the ridge," 3-7s: He swings one arm low in front of his face like an elephant's trunk, then points down toward the valley. Nora says, in a fast whisper: "arm swinging low like a trunk. Herd. And he wants me along." 7-10s: He beckons her to follow; Nora raises her eyebrows at the camera. Nora says, in a fast whisper: "Not sure if that's trust or bait." Torak does not speak. His boots sink into the snow with each step. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The camera is the phone itself recording from Nora's hand, so the viewer looks directly at Nora; no phone, no phone body, no phone screen, no UI or app overlay, no case, and no selfie stick appear anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: wind, crunching steps, Nora's voice.
```

### S23

- **Thời lượng:** 10s · **Kiểu quay:** `back` · **Bối cảnh:** STEP / afternoon
- **Ref (character_names):** Nora, Torak, Mammoth Steppe
- **Giọng:** breathing hard, low-voiced
- **Vào cảnh:** jump cut · **Ra cảnh:** look-away over the rise · **Nối:** CUT; S24 opens behind her head on the rise
- **Thoại:**
  - `0-3s` “Walk in his tracks. Saves energy,”
  - `3-7s` “and he knows where the crust holds. We stay downwind too.”
  - `7-10s` “Mammoths probably smell like elephants: way better than they see.”

**prompt**

```
Smartphone frame from just behind Nora's right shoulder on the snowy steppe in low afternoon sun; her shoulder and ponytail at the left edge; Torak walks about three metres ahead with his back to the camera, leaving deep footprints. Setting: the Ice Age mammoth steppe near Mezhyrich, central Ukraine, about 16,000 BC: wind-scoured snow with dry golden grass tufts, a rolling treeless plain, a broad frozen river valley below with a steep three-metre snowy riverbank whose top lip is glazed with shiny ice; low afternoon sun, long shadows, golden light on the snow.
```

**video_prompt**

```
Handheld smartphone vlog footage from Nora's raised right hand just behind her shoulder, looking where she looks, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Setting: the Ice Age mammoth steppe near Mezhyrich, central Ukraine, about 16,000 BC: wind-scoured snow with dry golden grass tufts, a rolling treeless plain, a broad frozen river valley below with a steep three-metre snowy riverbank whose top lip is glazed with shiny ice; low afternoon sun, long shadows, golden light on the snow. Shot: From Nora's raised hand just behind her right shoulder, looking forward along the trail; Torak walks about three metres ahead. 0-3s: Both walk slowly; Nora steps exactly into Torak's footprints. Nora says, breathing hard, low-voiced: "Walk in his tracks. Saves energy," 3-7s: Torak glances at the wind direction and keeps going, the camera bouncing gently with Nora's steps. Nora says, breathing hard, low-voiced: "and he knows where the crust holds. We stay downwind too." 7-10s: At 9s Nora turns her head to look over the top of the rise. Nora says, breathing hard, low-voiced: "Mammoths probably smell like elephants: way better than they see." Torak does not speak. The snow crust cracks under each boot; both move at a slow walking pace. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The camera is the phone itself in Nora's raised hand; no phone, no phone screen, no UI and no selfie stick appear anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: wind, crust cracking under boots, Nora's voice.
```

### S24

- **Thời lượng:** 10s · **Kiểu quay:** `back` · **Bối cảnh:** STEP / afternoon
- **Ref (character_names):** Nora, Woolly Mammoth, Mammoth Steppe
- **Giọng:** breathless whisper
- **Vào cảnh:** back of her head · **Ra cảnh:** camera swings forward in a blur · **Nối:** CUT in the blur; S25 opens mid-swing on the herd
- **Thoại:**
  - `0-3s` “Oh. Oh, there they are.”
  - `3-7s` “Eight, nine... calves in the middle. That's textbook elephant behaviour.”
  - `7-10s` “I did not expect textbook to be this big.”

**prompt**

```
Smartphone frame from just behind Nora's head as she kneels on a snowy rise in low afternoon sun: the back of her head and ponytail fill the left half; on the right, far below in the broad frozen valley, a herd of woolly mammoths is already visible, small in the distance. Setting: the Ice Age mammoth steppe near Mezhyrich, central Ukraine, about 16,000 BC: wind-scoured snow with dry golden grass tufts, a rolling treeless plain, a broad frozen river valley below with a steep three-metre snowy riverbank whose top lip is glazed with shiny ice; low afternoon sun, long shadows, golden light on the snow.
```

**video_prompt**

```
Handheld smartphone vlog footage from Nora's raised right hand just behind her shoulder, looking where she looks, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Setting: the Ice Age mammoth steppe near Mezhyrich, central Ukraine, about 16,000 BC: wind-scoured snow with dry golden grass tufts, a rolling treeless plain, a broad frozen river valley below with a steep three-metre snowy riverbank whose top lip is glazed with shiny ice; low afternoon sun, long shadows, golden light on the snow. Shot: From just behind Nora's head, the back of her head on the left, the valley on the right (Reveal #1). 0-3s: Nora stays still; the herd far below walks slowly to the left, staying small and far away. Nora says, breathless whisper: "Oh. Oh, there they are." 3-7s: Nora lowers herself and shifts slowly to the left, revealing the whole herd; calves walk in the middle between the adults. Nora says, breathless whisper: "Eight, nine... calves in the middle. That's textbook elephant behaviour." 7-10s: At 9s the camera swings smoothly forward over the valley in a motion blur. Nora says, breathless whisper: "I did not expect textbook to be this big." No people in the shot. The herd is in the frame from the first second and never gets closer; nothing pops into view. The valley is completely still. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The camera is the phone itself in Nora's raised hand; no phone, no phone screen, no UI and no selfie stick appear anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: wind, distant low mammoth rumbles, Nora's voice.
```

### S25

- **Thời lượng:** 10s · **Kiểu quay:** `wide` · **Bối cảnh:** STEP / afternoon
- **Ref (character_names):** Nora, Woolly Mammoth, Mammoth Steppe
- **Giọng:** in a fast whisper from behind the camera
- **Vào cảnh:** mid-swing · **Ra cảnh:** jump cut · **Nối:** CUT
- **Thoại:**
  - `0-3s` “Small ears, see? Big ears dump heat, they'd freeze.”
  - `3-7s` “Shaggy outer hair, dense wool underneath.”
  - `7-10s` “We have frozen carcasses from Siberia with ears this size.”

**prompt**

```
Handheld view from a snowy ridge across the valley at medium distance: woolly mammoths grazing with heads low, pushing through shallow snow for grass. Setting: the Ice Age mammoth steppe near Mezhyrich, central Ukraine, about 16,000 BC: wind-scoured snow with dry golden grass tufts, a rolling treeless plain, a broad frozen river valley below with a steep three-metre snowy riverbank whose top lip is glazed with shiny ice; low afternoon sun, long shadows, golden light on the snow.
```

**video_prompt**

```
Handheld smartphone footage from where Nora stands, slow steady pan, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Setting: the Ice Age mammoth steppe near Mezhyrich, central Ukraine, about 16,000 BC: wind-scoured snow with dry golden grass tufts, a rolling treeless plain, a broad frozen river valley below with a steep three-metre snowy riverbank whose top lip is glazed with shiny ice; low afternoon sun, long shadows, golden light on the snow. Shot: Handheld view from the ridge across the valley at medium distance, slow pan left to right. 0-3s: The camera settles from a swing and pans slowly left to right across the herd. Nora says from behind the camera, in a fast whisper from behind the camera: "Small ears, see? Big ears dump heat, they'd freeze." 3-7s: The mammoths walk very slowly, tusks occasionally pushing through shallow snow; long coarse guard hairs sway in the wind over a dense woolly undercoat. Nora says from behind the camera, in a fast whisper from behind the camera: "Shaggy outer hair, dense wool underneath." 7-10s: The pan passes a female with very small furry ears half hidden in her hair. Nora says from behind the camera, in a fast whisper from behind the camera: "We have frozen carcasses from Siberia with ears this size." No people in the shot. Their feet compress the snow before the heavy bodies shift. The ears are very small, about thirty centimetres, tucked close to the head. The herd stays at the same distance. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. Nora is behind the camera and not visible. No phone, no device, and no selfie stick appear anywhere in the frame. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: wind, low rumbles, crunch of snow under huge feet, Nora's voice.
```

### S26

- **Thời lượng:** 10s · **Kiểu quay:** `selfie` · **Bối cảnh:** STEP / afternoon
- **Ref (character_names):** Nora, Torak, Woolly Mammoth
- **Giọng:** in a very fast whisper
- **Vào cảnh:** jump cut · **Ra cảnh:** jump cut · **Nối:** CUT
- **Thoại:**
  - `0-3s` “Torak's hand says stay low, and I'm staying low.”
  - `3-7s` “No, wait— lead female, probably, trunk up, sniffing.”
  - `7-10s` “She's testing the wind. Is our wind still good?”

**prompt**

```
Low ultra-wide selfie just above the snow: Nora lies on her stomach behind a low snow ridge; Torak lies to her right; far behind them across the valley the mammoth herd, the largest female in front. Setting: the Ice Age mammoth steppe near Mezhyrich, central Ukraine, about 16,000 BC: wind-scoured snow with dry golden grass tufts, a rolling treeless plain, a broad frozen river valley below with a steep three-metre snowy riverbank whose top lip is glazed with shiny ice; low afternoon sun, long shadows, golden light on the snow.
```

**video_prompt**

```
Handheld front-camera vlog footage, ultra-wide 0.5x lens, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Nora holds the camera at arm's length with her right arm extended toward the bottom-right corner of the frame. Setting: the Ice Age mammoth steppe near Mezhyrich, central Ukraine, about 16,000 BC: wind-scoured snow with dry golden grass tufts, a rolling treeless plain, a broad frozen river valley below with a steep three-metre snowy riverbank whose top lip is glazed with shiny ice; low afternoon sun, long shadows, golden light on the snow. Shot: Low ultra-wide selfie just above the snow, Nora lying behind a snow ridge, Torak on her right, the herd far behind. 0-3s: Torak presses his flat hand downward twice, signalling stay low; Nora nods. Nora says, in a very fast whisper: "Torak's hand says stay low, and I'm staying low." 3-7s: Far behind them, the largest female slowly raises her trunk high, curling the tip, sniffing the air; she stands still. Nora says, in a very fast whisper: "No, wait— lead female, probably, trunk up, sniffing." 7-10s: Nora whispers into the camera with wide eyes, glancing back at the herd. Nora says, in a very fast whisper: "She's testing the wind. Is our wind still good?" Torak does not speak. The trunk curls up slowly; the herd stays far away and does not move closer. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The camera is the phone itself recording from Nora's hand, so the viewer looks directly at Nora; no phone, no phone body, no phone screen, no UI or app overlay, no case, and no selfie stick appear anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: wind, a distant snort, Nora's voice.
```

### S27

- **Thời lượng:** 10s · **Kiểu quay:** `selfie` · **Bối cảnh:** STEP / afternoon
- **Ref (character_names):** Nora, Torak, Woolly Mammoth
- **Giọng:** in a reckless whisper
- **Vào cảnh:** jump cut · **Ra cảnh:** camera turns toward the herd · **Nối:** CUT; S28 POV low over the snow
- **Thoại:**
  - `0-3s` “Real talk, I need a closer shot. Fifty metres, max.”
  - `3-7s` “He's shaking his head. I know. I know.”
  - `7-10s` “Ten more steps and I'm done.”

**prompt**

```
Low ultra-wide selfie just above the snow: Nora on her elbows crawling; Torak lying behind her shoulder; the mammoth herd far off on the right side of the frame. Setting: the Ice Age mammoth steppe near Mezhyrich, central Ukraine, about 16,000 BC: wind-scoured snow with dry golden grass tufts, a rolling treeless plain, a broad frozen river valley below with a steep three-metre snowy riverbank whose top lip is glazed with shiny ice; low afternoon sun, long shadows, golden light on the snow.
```

**video_prompt**

```
Handheld front-camera vlog footage, ultra-wide 0.5x lens, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Nora holds the camera at arm's length with her right arm extended toward the bottom-right corner of the frame. Setting: the Ice Age mammoth steppe near Mezhyrich, central Ukraine, about 16,000 BC: wind-scoured snow with dry golden grass tufts, a rolling treeless plain, a broad frozen river valley below with a steep three-metre snowy riverbank whose top lip is glazed with shiny ice; low afternoon sun, long shadows, golden light on the snow. Shot: Low ultra-wide selfie just above the snow, Nora crawling on her elbows, Torak behind. 0-3s: Nora crawls forward on her elbows about one metre, elbows sinking into the snow. Nora says, in a reckless whisper: "Real talk, I need a closer shot. Fifty metres, max." 3-7s: Behind her Torak shakes his head and reaches a hand toward her without touching her. Nora says, in a reckless whisper: "He's shaking his head. I know. I know." 7-10s: She keeps crawling; at 9s she turns the camera away from her face toward the herd in a blur. Nora says, in a reckless whisper: "Ten more steps and I'm done." Torak does not speak. Her elbows leave dents in the snow; the herd stays far away. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The camera is the phone itself recording from Nora's hand, so the viewer looks directly at Nora; no phone, no phone body, no phone screen, no UI or app overlay, no case, and no selfie stick appear anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: wind, snow crunching under elbows, Nora's voice.
```

### S28

- **Thời lượng:** 10s · **Kiểu quay:** `pov_hand` · **Bối cảnh:** STEP / afternoon
- **Ref (character_names):** Nora, Woolly Mammoth, Mammoth Steppe
- **Giọng:** whispering, faster and faster
- **Vào cảnh:** hand already on the snow · **Ra cảnh:** cut as the mother shifts her weight forward · **Nối:** CUT on the lunge; S29 opens mid-run
- **Thoại:**
  - `0-3s` “Calf's wandering this way. Mum's watching it.”
  - `3-7s` “Mum's watching me now. Okay...”
  - `7-10s` “head up, trunk tucked, that's the posture. That's the posture before—”

**prompt**

```
First-person view low just above the snow crust, Nora's bare hand pressed flat on the snow at the bottom of the frame; a mammoth calf at medium distance ahead, its mother a little behind it. Setting: the Ice Age mammoth steppe near Mezhyrich, central Ukraine, about 16,000 BC: wind-scoured snow with dry golden grass tufts, a rolling treeless plain, a broad frozen river valley below with a steep three-metre snowy riverbank whose top lip is glazed with shiny ice; low afternoon sun, long shadows, golden light on the snow.
```

**video_prompt**

```
First-person handheld smartphone footage at Nora's eye level, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Setting: the Ice Age mammoth steppe near Mezhyrich, central Ukraine, about 16,000 BC: wind-scoured snow with dry golden grass tufts, a rolling treeless plain, a broad frozen river valley below with a steep three-metre snowy riverbank whose top lip is glazed with shiny ice; low afternoon sun, long shadows, golden light on the snow. Shot: First-person view low just above the snow crust. 0-3s: The calf wanders slowly toward the camera; the mother keeps grazing. Nora says from behind the camera, whispering, faster and faster: "Calf's wandering this way. Mum's watching it." 3-7s: The mother mammoth turns her head and looks straight toward the camera; her long hair swings with a delay after the turn. Nora says from behind the camera, whispering, faster and faster: "Mum's watching me now. Okay..." 7-10s: The mother mammoth raises her head high and curls her trunk inward under her tusks, then shifts her weight forward onto her front legs. Nora says from behind the camera, whispering, faster and faster: "head up, trunk tucked, that's the posture. That's the posture before—" No people in the shot. Heavy body inertia: her feet compress the snow before the body moves. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. First-person point-of-view shot. Nora is completely behind the camera holding it firmly; only her bare empty hand enters the lower frame. No phone, no device, and no selfie stick appear anywhere in the frame. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: wind, a low rumble rising to a trumpet, Nora's voice.
```


---

## Hồi 4 — Cao trào (Giờ 12–14, hoàng hôn)

### S29

- **Thời lượng:** 8s · **Kiểu quay:** `run` · **Bối cảnh:** STEP / sunset
- **Ref (character_names):** Nora, Woolly Mammoth, Mammoth Steppe
- **Giọng:** running, voice cracking · **Bleep tại:** 1.2s
- **Vào cảnh:** hard cut mid-run · **Ra cảnh:** whip down toward the snow · **Nối:** CUT in the blur; S30 opens mid-wade
- **Thoại:**
  - `0-3s` “She's charging— sh— don't run straight, she's way faster than me.”
  - `3-6s` “Riverbank. Get something big between us.”
  - `6-8s` “Go, go!”

**prompt**

```
Ultra-wide selfie at arm's length on the snowy steppe at sunset, Nora's face close and frightened; far behind her a female woolly mammoth charging, snow spraying. Setting: the Ice Age mammoth steppe near Mezhyrich, central Ukraine, about 16,000 BC: wind-scoured snow with dry golden grass tufts, a rolling treeless plain, a broad frozen river valley below with a steep three-metre snowy riverbank whose top lip is glazed with shiny ice; low orange sunset light, long blue shadows on the snow.
```

**video_prompt**

```
Handheld front-camera vlog footage, ultra-wide 0.5x lens, natural smartphone perspective, auto-exposure, photorealistic documentary realism. Nora holds the camera at arm's length with her right arm extended toward the bottom-right corner of the frame. Handheld smartphone footage with natural vertical bounce synchronized to each footfall, slight rotational lag when turning, and realistic motion blur. Setting: the Ice Age mammoth steppe near Mezhyrich, central Ukraine, about 16,000 BC: wind-scoured snow with dry golden grass tufts, a rolling treeless plain, a broad frozen river valley below with a steep three-metre snowy riverbank whose top lip is glazed with shiny ice; low orange sunset light, long blue shadows on the snow. Shot: Ultra-wide running selfie at arm's length, the charging mammoth far behind. 0-3s: Nora runs forward through knee-deep snow with shortened heavy strides, twisting her upper body to look back over her shoulder; far behind her the female mammoth charges, snow spraying from her feet. Nora says, running, voice cracking: "She's charging— sh— don't run straight, she's way faster than me." 3-6s: Nora keeps running; the mammoth grows slowly larger in the background but stays far behind and never catches up during the clip. Nora says, running, voice cracking: "Riverbank. Get something big between us." 6-8s: At 7.5s the camera whips down toward the snow in a blur. Nora says, running, voice cracking: "Go, go!" No one else in the shot. Her boots sink deep and leave raised rims of displaced snow. The mammoth is heavy: feet compress the snow, the body sways with a lag, the long hair bounces. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The camera is the phone itself recording from Nora's hand, so the viewer looks directly at Nora; no phone, no phone body, no phone screen, no UI or app overlay, no case, and no selfie stick appear anywhere in the shot. Nora clutches the camera firmly in her right hand at arm's length pointed continuously at her face; she never drops, releases, or lets go of it. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: pounding heavy footfalls, trumpeting, Nora's ragged breathing, Nora's voice.
```

### S30

- **Thời lượng:** 6s · **Kiểu quay:** `pov` · **Bối cảnh:** STEP / sunset
- **Ref (character_names):** Nora, Torak, Mammoth Steppe
- **Giọng:** panting
- **Vào cảnh:** mid-wade · **Ra cảnh:** camera pitches down over the lip · **Nối:** CUT; S31 opens as she slides down
- **Thoại:**
  - `0-2s` “Knee-deep, I can't run, just big heavy steps.”
  - `2-4s` “The bank's right there, Torak's waving.”
  - `4-6s` “Go.”

**prompt**

```
First-person view at chest height wading through knee-deep snow at sunset; about ten metres ahead the edge of a steep riverbank; Torak stands on it waving one arm. Setting: the Ice Age mammoth steppe near Mezhyrich, central Ukraine, about 16,000 BC: wind-scoured snow with dry golden grass tufts, a rolling treeless plain, a broad frozen river valley below with a steep three-metre snowy riverbank whose top lip is glazed with shiny ice; low orange sunset light, long blue shadows on the snow.
```

**video_prompt**

```
First-person handheld smartphone footage at Nora's eye level, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Setting: the Ice Age mammoth steppe near Mezhyrich, central Ukraine, about 16,000 BC: wind-scoured snow with dry golden grass tufts, a rolling treeless plain, a broad frozen river valley below with a steep three-metre snowy riverbank whose top lip is glazed with shiny ice; low orange sunset light, long blue shadows on the snow. Shot: First-person view at chest height wading toward the riverbank edge. 0-2s: The camera pushes forward slowly at wading speed, bouncing hard with each heavy step. Nora says from behind the camera, panting: "Knee-deep, I can't run, just big heavy steps." 2-4s: Snow bulges up around each step; the bank edge gets closer; Torak waves urgently. Nora says from behind the camera, panting: "The bank's right there, Torak's waving." 4-6s: At the edge the camera pitches down sharply as Nora slides over the lip. Nora says from behind the camera, panting: "Go." Torak does not speak. Natural vertical bounce synchronized to each step; the camera only moves at slow wading speed. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. First-person point-of-view shot. Nora is completely behind the camera holding it firmly; her own hands stay out of the frame. No phone, no device, and no selfie stick appear anywhere in the frame. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: heavy breathing, snow crunching, distant trumpeting, Nora's voice.
```

### S31

- **Thời lượng:** 8s · **Kiểu quay:** `selfie` · **Bối cảnh:** STEP / sunset
- **Ref (character_names):** Nora, Woolly Mammoth, Mammoth Steppe
- **Giọng:** in a breathless whisper
- **Vào cảnh:** camera pitched down · **Ra cảnh:** hard cut · **Nối:** CUT
- **Thoại:**
  - `0-3s` “Down, down, down. Steep bank, glazed ice on the lip.”
  - `3-6s` “Something that heavy can't get footing on that.”
  - `6-8s` “Probably. Please, probably.”

**prompt**

```
Ultra-wide selfie pointing up: Nora pressed with her back against a steep snowy riverbank wall about three metres high; above her the bank's top lip glazed with smooth shiny ice against the sunset sky. Setting: the Ice Age mammoth steppe near Mezhyrich, central Ukraine, about 16,000 BC: wind-scoured snow with dry golden grass tufts, a rolling treeless plain, a broad frozen river valley below with a steep three-metre snowy riverbank whose top lip is glazed with shiny ice; low orange sunset light, long blue shadows on the snow.
```

**video_prompt**

```
Handheld front-camera vlog footage, ultra-wide 0.5x lens, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Nora holds the camera at arm's length with her right arm extended toward the bottom-right corner of the frame. Setting: the Ice Age mammoth steppe near Mezhyrich, central Ukraine, about 16,000 BC: wind-scoured snow with dry golden grass tufts, a rolling treeless plain, a broad frozen river valley below with a steep three-metre snowy riverbank whose top lip is glazed with shiny ice; low orange sunset light, long blue shadows on the snow. Shot: Ultra-wide selfie pointing up, Nora pressed against the bank wall. 0-3s: Nora finishes sliding down the bank and stops, snow trickling after her; she presses her back to the wall. Nora says, in a breathless whisper: "Down, down, down. Steep bank, glazed ice on the lip." 3-6s: Above, the female mammoth approaches the top of the bank at a run, so her head and shoulders appear gradually over the lip as she gets closer. Nora says, in a breathless whisper: "Something that heavy can't get footing on that." 6-8s: Nora looks up, breathing hard. Nora says, in a breathless whisper: "Probably. Please, probably." No one else in the shot. Snow trickles down after her slide; the bank wall is solid and still. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The camera is the phone itself recording from Nora's hand, so the viewer looks directly at Nora; no phone, no phone body, no phone screen, no UI or app overlay, no case, and no selfie stick appear anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: thudding footfalls above, Nora's breathing, Nora's voice.
```

### S32

- **Thời lượng:** 6s · **Kiểu quay:** `selfie` · **Bối cảnh:** STEP / sunset
- **Ref (character_names):** Nora, Woolly Mammoth, Mammoth Steppe
- **Giọng:** in a panicked whisper
- **Vào cảnh:** hard cut · **Ra cảnh:** hard cut · **Nối:** CUT
- **Thoại:**
  - `0-2s` “Oh no no no— she's slipping, she's slipping—”
  - `2-4s` “she's turning.”
  - `4-6s` “She's turning away!”

**prompt**

```
Low ultra-wide selfie pointing upward past Nora's face toward the top lip of the riverbank about three metres above, glazed with shiny ice; the female mammoth arriving at the top edge. Setting: the Ice Age mammoth steppe near Mezhyrich, central Ukraine, about 16,000 BC: wind-scoured snow with dry golden grass tufts, a rolling treeless plain, a broad frozen river valley below with a steep three-metre snowy riverbank whose top lip is glazed with shiny ice; low orange sunset light, long blue shadows on the snow.
```

**video_prompt**

```
Handheld front-camera vlog footage, ultra-wide 0.5x lens, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Nora holds the camera at arm's length with her right arm extended toward the bottom-right corner of the frame. Setting: the Ice Age mammoth steppe near Mezhyrich, central Ukraine, about 16,000 BC: wind-scoured snow with dry golden grass tufts, a rolling treeless plain, a broad frozen river valley below with a steep three-metre snowy riverbank whose top lip is glazed with shiny ice; low orange sunset light, long blue shadows on the snow. Shot: Low-angle ultra-wide selfie pointing up past Nora's face toward the bank's icy top lip about three metres above. 0-2s: The mammoth's front feet step onto the glazed ice lip and lose traction, sliding. Nora says, in a panicked whisper: "Oh no no no— she's slipping, she's slipping—" 2-4s: The mammoth's heavy body lurches sideways to the right to regain balance; she tosses her head defensively, tusks sweeping through the snow. Nora says, in a panicked whisper: "she's turning." 4-6s: The mammoth swings her body around and turns away to the right, out of view beyond the top edge; snow and ice fragments tumble down past Nora's face. Nora says, in a panicked whisper: "She's turning away!" No one else in the shot. This is a deflection, not a stop: the feet slide first and the body lags behind; she never skids to a halt like a car and never comes down the bank. Nora stays pressed against the wall. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The camera is the phone itself recording from Nora's hand, so the viewer looks directly at Nora; no phone, no phone body, no phone screen, no UI or app overlay, no case, and no selfie stick appear anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: scraping ice, heavy thud, trumpet, falling ice, Nora's voice.
```

### S33

- **Thời lượng:** 8s · **Kiểu quay:** `pov` · **Bối cảnh:** STEP / sunset
- **Ref (character_names):** Nora, Woolly Mammoth, Mammoth Steppe
- **Giọng:** exhaling shakily
- **Vào cảnh:** hard cut · **Ra cảnh:** Torak's hand crosses the lens · **Nối:** CUT on the hand; S34 opens with Torak pulling her up
- **Thoại:**
  - `0-3s` “Going back to her calf. Warning charge, probably, not a kill.”
  - `3-6s` “Elephants do that.”
  - `6-8s` “Didn't feel like a warning.”

**prompt**

```
First-person view from just below the riverbank lip looking up and out over the snow: the female mammoth running away toward the distant herd at sunset. Setting: the Ice Age mammoth steppe near Mezhyrich, central Ukraine, about 16,000 BC: wind-scoured snow with dry golden grass tufts, a rolling treeless plain, a broad frozen river valley below with a steep three-metre snowy riverbank whose top lip is glazed with shiny ice; low orange sunset light, long blue shadows on the snow.
```

**video_prompt**

```
First-person handheld smartphone footage at Nora's eye level, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Setting: the Ice Age mammoth steppe near Mezhyrich, central Ukraine, about 16,000 BC: wind-scoured snow with dry golden grass tufts, a rolling treeless plain, a broad frozen river valley below with a steep three-metre snowy riverbank whose top lip is glazed with shiny ice; low orange sunset light, long blue shadows on the snow. Shot: First-person view from just below the bank lip, looking up and out. 0-3s: The mammoth trots heavily away toward the herd, getting smaller, snow kicking up behind her feet. Nora says from behind the camera, exhaling shakily: "Going back to her calf. Warning charge, probably, not a kill." 3-6s: The mammoth's long hair bounces with each stride as she shrinks into the distance. Nora says from behind the camera, exhaling shakily: "Elephants do that." 6-8s: At 7s Torak's mittened hand reaches down from above across the lens. Nora says from behind the camera, exhaling shakily: "Didn't feel like a warning." Torak does not speak. The mammoth only gets smaller; she never turns back. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. First-person point-of-view shot. Nora is completely behind the camera holding it firmly; her own hands stay out of the frame. No phone, no device, and no selfie stick appear anywhere in the frame. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: fading thuds, wind, Nora's voice.
```

### S34

- **Thời lượng:** 10s · **Kiểu quay:** `selfie` · **Bối cảnh:** STEP / sunset
- **Ref (character_names):** Nora, Torak, Mammoth Steppe
- **Giọng:** laughing shakily, fast
- **Vào cảnh:** hand across the lens · **Ra cảnh:** jump cut · **Nối:** CUT
- **Thoại:**
  - `0-3s` “Okay, okay. Hand, yes, thank you.”
  - `3-7s` “He's... laughing at me. Fair.”
  - `7-10s` “I just did everything I tell my students never to do.”

**prompt**

```
Ultra-wide selfie on the riverbank slope at sunset; Torak above gripping Nora's left forearm. Setting: the Ice Age mammoth steppe near Mezhyrich, central Ukraine, about 16,000 BC: wind-scoured snow with dry golden grass tufts, a rolling treeless plain, a broad frozen river valley below with a steep three-metre snowy riverbank whose top lip is glazed with shiny ice; low orange sunset light, long blue shadows on the snow.
```

**video_prompt**

```
Handheld front-camera vlog footage, ultra-wide 0.5x lens, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Nora holds the camera at arm's length with her right arm extended toward the bottom-right corner of the frame. Setting: the Ice Age mammoth steppe near Mezhyrich, central Ukraine, about 16,000 BC: wind-scoured snow with dry golden grass tufts, a rolling treeless plain, a broad frozen river valley below with a steep three-metre snowy riverbank whose top lip is glazed with shiny ice; low orange sunset light, long blue shadows on the snow. Shot: Ultra-wide selfie on the riverbank slope, Torak above gripping Nora's left forearm. 0-3s: Torak pulls Nora up the bank by her left forearm; she scrambles up about a metre, the camera shaking. Nora says, laughing shakily, fast: "Okay, okay. Hand, yes, thank you." 3-7s: Torak is laughing silently as he hauls her onto the top. Nora says, laughing shakily, fast: "He's... laughing at me. Fair." 7-10s: Nora, on her knees at the top, laughs shakily into the camera. Nora says, laughing shakily, fast: "I just did everything I tell my students never to do." Torak laughs without words. Her right hand never lets go of the camera; the frame shakes as she climbs. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The camera is the phone itself recording from Nora's hand, so the viewer looks directly at Nora; no phone, no phone body, no phone screen, no UI or app overlay, no case, and no selfie stick appear anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: snow scraping, breathing, wind, Nora's voice.
```

### S35

- **Thời lượng:** 10s · **Kiểu quay:** `selfie` · **Bối cảnh:** STEP / sunset
- **Ref (character_names):** Nora, Torak, Mammoth Steppe
- **Giọng:** shaky, slowing down
- **Vào cảnh:** jump cut · **Ra cảnh:** look-away toward the valley · **Nối:** CUT; S36 opens behind her head
- **Thoại:**
  - `0-3s` “Hour thirteen. Hands won't stop shaking. That's adrenaline dumping, not cold.”
  - `3-7s` “Eat something, sit, breathe slow.”
  - `7-10s` “Torak's handing me fat. Of course he is.”

**prompt**

```
Ultra-wide selfie at sunset; Nora sits in the snow at the top of the riverbank, hands trembling; Torak crouches on her left. Setting: the Ice Age mammoth steppe near Mezhyrich, central Ukraine, about 16,000 BC: wind-scoured snow with dry golden grass tufts, a rolling treeless plain, a broad frozen river valley below with a steep three-metre snowy riverbank whose top lip is glazed with shiny ice; low orange sunset light, long blue shadows on the snow.
```

**video_prompt**

```
Handheld front-camera vlog footage, ultra-wide 0.5x lens, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Nora holds the camera at arm's length with her right arm extended toward the bottom-right corner of the frame. Setting: the Ice Age mammoth steppe near Mezhyrich, central Ukraine, about 16,000 BC: wind-scoured snow with dry golden grass tufts, a rolling treeless plain, a broad frozen river valley below with a steep three-metre snowy riverbank whose top lip is glazed with shiny ice; low orange sunset light, long blue shadows on the snow. Shot: Ultra-wide selfie, Nora sitting in the snow at the top of the bank, Torak crouching on her left. 0-3s: The frame trembles slightly with her shaking hand. Nora says, shaky, slowing down: "Hour thirteen. Hands won't stop shaking. That's adrenaline dumping, not cold." 3-7s: Torak holds out a lump of white fat; she takes it with her free hand. Nora says, shaky, slowing down: "Eat something, sit, breathe slow." 7-10s: She gives a tired laugh; at 9s she turns her head to look toward the valley. Nora says, shaky, slowing down: "Torak's handing me fat. Of course he is." Torak does not speak. The camera shakes only slightly with her trembling hand. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The camera is the phone itself recording from Nora's hand, so the viewer looks directly at Nora; no phone, no phone body, no phone screen, no UI or app overlay, no case, and no selfie stick appear anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: wind, slowing breath, Nora's voice.
```

### S36

> ✂️ Rút từ 10s xuống 8s trong bản 52 cảnh.

- **Thời lượng:** 8s · **Kiểu quay:** `back_selfie` · **Bối cảnh:** STEP / sunset
- **Ref (character_names):** Nora, Woolly Mammoth, Mammoth Steppe
- **Giọng:** low-voiced, calm now
- **Vào cảnh:** back of her head · **Ra cảnh:** time-skip cut to night · **Nối:** CUT, time-skip
- **Thoại:**
  - `0-3s` “Front feet slid, she twisted, she bailed.”
  - `3-6s` “Ice turned her, not me. No accident.”
  - `6-8s` “Torak picked this bank on purpose.”

**prompt**

```
Smartphone frame from just behind Nora's head at sunset: below the riverbank lip, long slide marks scraped into the glazed ice; far away the mammoth herd walking off into the orange sunset. Setting: the Ice Age mammoth steppe near Mezhyrich, central Ukraine, about 16,000 BC: wind-scoured snow with dry golden grass tufts, a rolling treeless plain, a broad frozen river valley below with a steep three-metre snowy riverbank whose top lip is glazed with shiny ice; low orange sunset light, long blue shadows on the snow.
```

**video_prompt**

```
Handheld smartphone vlog footage that starts from Nora's raised hand just behind her head and then turns around to face her at arm's length, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Setting: the Ice Age mammoth steppe near Mezhyrich, central Ukraine, about 16,000 BC: wind-scoured snow with dry golden grass tufts, a rolling treeless plain, a broad frozen river valley below with a steep three-metre snowy riverbank whose top lip is glazed with shiny ice; low orange sunset light, long blue shadows on the snow. Shot: From just behind Nora's head looking down at the bank and valley, then turning to a selfie. 0-3s: The herd keeps walking away, small and getting smaller; the sun sinks low. Nora says, low-voiced, calm now: "Front feet slid, she twisted, she bailed." 3-6s: Nora brings the camera around to face herself, calm now; the light shifts from orange toward blue. Nora says, low-voiced, calm now: "Ice turned her, not me. No accident." 6-8s: She glances to the side toward Torak and nods. Nora says, low-voiced, calm now: "Torak picked this bank on purpose." No one else speaks. The slide marks are there from the first second; the herd only gets smaller. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The camera is the phone itself recording from Nora's hand; no phone, no phone body, no phone screen, no UI or app overlay, no case, and no selfie stick appear anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: wind dying down, distant rumbles, Nora's voice.
```


---

## Hồi 5 — Hạ nhịp (Giờ 15–16, đêm, trong dwelling)

### S37

- **Thời lượng:** 10s · **Kiểu quay:** `selfie` · **Bối cảnh:** INT / night_in
- **Ref (character_names):** Nora, Alva, Bone Dwelling Interior
- **Giọng:** tired and warm
- **Vào cảnh:** walk-through from dark · **Ra cảnh:** she reaches toward the bone · **Nối:** CUT; S38 POV
- **Thoại:**
  - `0-3s` “Hour fifteen. Alva heard. Everyone heard.”
  - `3-7s` “She's cracking a leg bone for me,”
  - `7-10s` “which I'm choosing to read as 'welcome to the family'.”

**prompt**

```
Ultra-wide selfie, nearly dark, Nora ducking through a hide flap into the dwelling, firelight rising behind her; Alva sits at the hearth behind her. Setting: inside a mammoth-bone dwelling at Mezhyrich, central Ukraine, about 16,000 BC: a low dome of tusks and long bones between hanging reindeer hides, a shallow stone-ringed central hearth burning greasy bone ends (no wood anywhere), fur hides on the floor, a hide water bag hanging from a bone tripod, a low bone ledge along the wall; night; warm firelight from the hearth is the only light.
```

**video_prompt**

```
Handheld front-camera vlog footage, ultra-wide 0.5x lens, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Nora holds the camera at arm's length with her right arm extended toward the bottom-right corner of the frame. Setting: inside a mammoth-bone dwelling at Mezhyrich, central Ukraine, about 16,000 BC: a low dome of tusks and long bones between hanging reindeer hides, a shallow stone-ringed central hearth burning greasy bone ends (no wood anywhere), fur hides on the floor, a hide water bag hanging from a bone tripod, a low bone ledge along the wall; night; warm firelight from the hearth is the only light. Shot: Ultra-wide selfie as Nora ducks into the dwelling, Alva at the hearth behind her. 0-3s: Nora pushes through the hide flap into warm firelight and sits down. Nora says, tired and warm: "Hour fifteen. Alva heard. Everyone heard." 3-7s: Behind her Alva strikes a long mammoth leg bone on a stone anvil with a stone hammer; cracks radiate from the impact point. Nora says, tired and warm: "She's cracking a leg bone for me," 7-10s: The bone splits open; at 9s Nora reaches her free hand toward it. Nora says, tired and warm: "which I'm choosing to read as 'welcome to the family'." Alva does not speak. The bone cracks progressively from the impact point before it splits. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The camera is the phone itself recording from Nora's hand, so the viewer looks directly at Nora; no phone, no phone body, no phone screen, no UI or app overlay, no case, and no selfie stick appear anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: fire crackle, sharp knock of stone on bone, Nora's voice.
```

### S38

- **Thời lượng:** 10s · **Kiểu quay:** `pov_hand` · **Bối cảnh:** INT / night_in
- **Ref (character_names):** Nora, Alva, Bone Dwelling Interior
- **Giọng:** fast, between bites
- **Vào cảnh:** hand enters from below · **Ra cảnh:** hard cut · **Nối:** CUT
- **Thoại:**
  - `0-3s` “Marrow. Basically pure fat. We find long bones”
  - `3-7s` “smashed open at sites like this. That exact break, right through the shaft.”
  - `7-10s` “And now I'm eating it.”

**prompt**

```
First-person view sitting by the hearth: Alva holds a split mammoth leg bone open toward the camera, soft pale marrow inside; Nora's bare hand holding a flat bone spatula enters from below. Setting: inside a mammoth-bone dwelling at Mezhyrich, central Ukraine, about 16,000 BC: a low dome of tusks and long bones between hanging reindeer hides, a shallow stone-ringed central hearth burning greasy bone ends (no wood anywhere), fur hides on the floor, a hide water bag hanging from a bone tripod, a low bone ledge along the wall; night; warm firelight from the hearth is the only light.
```

**video_prompt**

```
First-person handheld smartphone footage at Nora's eye level, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Setting: inside a mammoth-bone dwelling at Mezhyrich, central Ukraine, about 16,000 BC: a low dome of tusks and long bones between hanging reindeer hides, a shallow stone-ringed central hearth burning greasy bone ends (no wood anywhere), fur hides on the floor, a hide water bag hanging from a bone tripod, a low bone ledge along the wall; night; warm firelight from the hearth is the only light. Shot: First-person view sitting by the hearth. 0-3s: Nora's hand scoops marrow slowly with the bone spatula. Nora says from behind the camera, fast, between bites: "Marrow. Basically pure fat. We find long bones" 3-7s: The soft marrow sticks to the spatula; she lifts it toward the lens. Nora says from behind the camera, fast, between bites: "smashed open at sites like this. That exact break, right through the shaft." 7-10s: The spatula leaves the frame toward her mouth; Alva watches. Nora says from behind the camera, fast, between bites: "And now I'm eating it." Alva does not speak. The marrow is soft and sticky and clings to the spatula. First-person point-of-view shot. Nora is completely behind the camera holding it firmly; only her bare hand, holding a flat bone spatula, enters the lower frame. No phone, no device, and no selfie stick appear anywhere in the frame. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: fire crackle, quiet chewing, Nora's voice.
```

### S39

> 🆕 Cảnh mới trong bản 52 cảnh.

- **Thời lượng:** 10s · **Kiểu quay:** `pov_hand` · **Bối cảnh:** INT / night_in
- **Ref (character_names):** Nora, Alva, Bone Dwelling Interior
- **Giọng:** tired, matter-of-fact
- **Vào cảnh:** hard cut · **Ra cảnh:** hard cut · **Nối:** CUT; S40 opens on a static frame
- **Thoại:**
  - `0-3s` “Soaked at the riverbank. Wet feet lose heat fast.”
  - `3-7s` “Dry grass inside, it pulls moisture and traps warm air.”
  - `7-10s` “The Alps Iceman lined his shoes like this.”

**prompt**

```
First-person view sitting by the hearth at night, looking down at a dark, soaked fur-lined hide boot lying on a fur hide; Nora's bare hand entering from below; Alva on the left holding a bundle of dry golden grass. Setting: inside a mammoth-bone dwelling at Mezhyrich, central Ukraine, about 16,000 BC: a low dome of tusks and long bones between hanging reindeer hides, a shallow stone-ringed central hearth burning greasy bone ends (no wood anywhere), fur hides on the floor, a hide water bag hanging from a bone tripod, a low bone ledge along the wall; night; warm firelight from the hearth is the only light.
```

**video_prompt**

```
First-person handheld smartphone footage at Nora's eye level, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Setting: inside a mammoth-bone dwelling at Mezhyrich, central Ukraine, about 16,000 BC: a low dome of tusks and long bones between hanging reindeer hides, a shallow stone-ringed central hearth burning greasy bone ends (no wood anywhere), fur hides on the floor, a hide water bag hanging from a bone tripod, a low bone ledge along the wall; night; warm firelight from the hearth is the only light. Shot: First-person view sitting by the hearth, looking down at a soaked hide boot. 0-3s: Nora's bare hand pulls a wad of wet, matted grass out of the boot; a few drops of water fall from it. Nora says from behind the camera, tired, matter-of-fact: "Soaked at the riverbank. Wet feet lose heat fast." 3-7s: Alva's hand passes the bundle of dry golden grass from the left; Nora's hand takes it and pushes it down into the boot. Nora says from behind the camera, tired, matter-of-fact: "Dry grass inside, it pulls moisture and traps warm air." 7-10s: Her hand sets the boot upright on the floor beside the hearth stones, about an arm's length from the flames; faint steam rises from the damp hide. Nora says from behind the camera, tired, matter-of-fact: "The Alps Iceman lined his shoes like this." Alva does not speak. The wet grass is dark and limp; the dry grass is stiff and springy and compresses as it is pushed in; the boot stays at a safe distance from the fire and does not burn. First-person point-of-view shot. Nora is completely behind the camera holding it firmly; only her bare hand, handling grass and a hide boot, enters the lower frame. No phone, no device, and no selfie stick appear anywhere in the frame. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: fire crackle, rustle of dry grass, dripping water, Nora's voice.
```

### S40

- **Thời lượng:** 10s · **Kiểu quay:** `tripod` · **Bối cảnh:** INT / night_in
- **Ref (character_names):** Nora, Alva, Bone Dwelling Interior
- **Giọng:** softly, smiling
- **Vào cảnh:** static frame · **Ra cảnh:** hard cut · **Nối:** CUT
- **Thoại:**
  - `0-3s` “Alva's giving me a spot by the fire now.”
  - `3-7s` “Near the wall, not the door. I know what that means.”
  - `7-10s` “I'm not crying, it's the smoke.”

**prompt**

```
Static frame from a phone propped on a bone ledge inside the dwelling at night: Nora and Alva by the hearth, a fur hide on the floor near the wall. Setting: inside a mammoth-bone dwelling at Mezhyrich, central Ukraine, about 16,000 BC: a low dome of tusks and long bones between hanging reindeer hides, a shallow stone-ringed central hearth burning greasy bone ends (no wood anywhere), fur hides on the floor, a hide water bag hanging from a bone tripod, a low bone ledge along the wall; night; warm firelight from the hearth is the only light.
```

**video_prompt**

```
Static smartphone footage from a phone propped on a ledge, locked-off frame, natural smartphone perspective, photorealistic documentary realism. Setting: inside a mammoth-bone dwelling at Mezhyrich, central Ukraine, about 16,000 BC: a low dome of tusks and long bones between hanging reindeer hides, a shallow stone-ringed central hearth burning greasy bone ends (no wood anywhere), fur hides on the floor, a hide water bag hanging from a bone tripod, a low bone ledge along the wall; night; warm firelight from the hearth is the only light. Shot: Locked-off frame from a bone ledge, Nora, Alva and the hearth. 0-3s: Alva pats a fur hide on the floor at the spot close to the wall beside the fire. Nora says, softly, smiling: "Alva's giving me a spot by the fire now." 3-7s: Nora shuffles over and sits down there, wrapping her arms around her knees. Nora says, softly, smiling: "Near the wall, not the door. I know what that means." 7-10s: She wipes her eye with the back of her hand, smiling. Nora says, softly, smiling: "I'm not crying, it's the smoke." Alva does not speak. Smoke rises by convection toward the smoke hole. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The phone is the camera, resting still on a ledge; the frame never moves, and no phone, tripod or selfie stick appears anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: fire crackle, soft rustle of furs, Nora's voice.
```


---

## Hồi 6 — Di sản (Giờ 17–22, đêm)

### S41

- **Thời lượng:** 10s · **Kiểu quay:** `selfie` · **Bối cảnh:** INT / night_in
- **Ref (character_names):** Nora, Alva, Bone Dwelling Interior
- **Giọng:** in a whisper, almost choked up
- **Vào cảnh:** jump cut · **Ra cảnh:** her hand reaches for the hide · **Nối:** CUT; S42 POV
- **Thoại:**
  - `0-3s` “Hour seventeen. An eyed bone needle.”
  - `3-7s` “I've catalogued broken ones in museum drawers for years, never seen one used.”
  - `7-10s` “She's stitching without looking. Sorry. Archaeologist.”

**prompt**

```
Ultra-wide selfie by the fire; behind Nora's right shoulder Alva sews a fox pelt with a thin eyed bone needle. Setting: inside a mammoth-bone dwelling at Mezhyrich, central Ukraine, about 16,000 BC: a low dome of tusks and long bones between hanging reindeer hides, a shallow stone-ringed central hearth burning greasy bone ends (no wood anywhere), fur hides on the floor, a hide water bag hanging from a bone tripod, a low bone ledge along the wall; night; warm firelight from the hearth is the only light.
```

**video_prompt**

```
Handheld front-camera vlog footage, ultra-wide 0.5x lens, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Nora holds the camera at arm's length with her right arm extended toward the bottom-right corner of the frame. Setting: inside a mammoth-bone dwelling at Mezhyrich, central Ukraine, about 16,000 BC: a low dome of tusks and long bones between hanging reindeer hides, a shallow stone-ringed central hearth burning greasy bone ends (no wood anywhere), fur hides on the floor, a hide water bag hanging from a bone tripod, a low bone ledge along the wall; night; warm firelight from the hearth is the only light. Shot: Ultra-wide selfie by the fire, Alva sewing behind Nora's right shoulder. 0-3s: Alva pushes the bone needle in and out of the hide steadily without looking at her hands. Nora says, in a whisper, almost choked up: "Hour seventeen. An eyed bone needle." 3-7s: Nora leans in close, eyes shining. Nora says, in a whisper, almost choked up: "I've catalogued broken ones in museum drawers for years, never seen one used." 7-10s: Nora laughs at herself; at 9s she reaches her free hand toward the edge of the hide. Nora says, in a whisper, almost choked up: "She's stitching without looking. Sorry. Archaeologist." Alva does not speak. The hide flexes slightly around the needle. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The camera is the phone itself recording from Nora's hand, so the viewer looks directly at Nora; no phone, no phone body, no phone screen, no UI or app overlay, no case, and no selfie stick appear anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: fire crackle, soft pull of sinew, Nora's voice.
```

### S42

- **Thời lượng:** 10s · **Kiểu quay:** `pov_hand` · **Bối cảnh:** INT / night_in
- **Ref (character_names):** Nora, Alva, Bone Dwelling Interior
- **Giọng:** in a fast whisper
- **Vào cảnh:** hand already holding the hide · **Ra cảnh:** POV wipe: the pelt covers the lens · **Nối:** CUT on the pelt; S43 opens as the pelt leaves the frame
- **Thoại:**
  - `0-3s` “Hide flexes, sinew pulls tight.”
  - `3-7s` “Awls only punch holes. The eye means finer seams, fitted sleeves, no gaps for wind.”
  - `7-10s` “Also beads. Lots of beads.”

**prompt**

```
First-person view: Nora's bare hand holding the edge of a fox pelt at the bottom of the frame; Alva's hands hold a bone needle threaded with sinew. Setting: inside a mammoth-bone dwelling at Mezhyrich, central Ukraine, about 16,000 BC: a low dome of tusks and long bones between hanging reindeer hides, a shallow stone-ringed central hearth burning greasy bone ends (no wood anywhere), fur hides on the floor, a hide water bag hanging from a bone tripod, a low bone ledge along the wall; night; warm firelight from the hearth is the only light.
```

**video_prompt**

```
First-person handheld smartphone footage at Nora's eye level, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Setting: inside a mammoth-bone dwelling at Mezhyrich, central Ukraine, about 16,000 BC: a low dome of tusks and long bones between hanging reindeer hides, a shallow stone-ringed central hearth burning greasy bone ends (no wood anywhere), fur hides on the floor, a hide water bag hanging from a bone tripod, a low bone ledge along the wall; night; warm firelight from the hearth is the only light. Shot: First-person view, Nora's hand holding the edge of a fox pelt. 0-3s: Alva pushes the bone needle through the hide; the hide flexes slightly around the needle point. Nora says from behind the camera, in a fast whisper: "Hide flexes, sinew pulls tight." 3-7s: She pulls the sinew thread tight, then it lies flat in the seam. Nora says from behind the camera, in a fast whisper: "Awls only punch holes. The eye means finer seams, fitted sleeves, no gaps for wind." 7-10s: At 9s Alva lifts the pelt up so it covers the lens completely. Nora says from behind the camera, in a fast whisper: "Also beads. Lots of beads." Alva does not speak. The sinew goes taut, then relaxes. First-person point-of-view shot. Nora is completely behind the camera holding it firmly; only her bare hand, holding the edge of the hide, enters the lower frame. No phone, no device, and no selfie stick appear anywhere in the frame. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: fire crackle, sinew pulling, Nora's voice.
```

### S43

- **Thời lượng:** 10s · **Kiểu quay:** `selfie` · **Bối cảnh:** INT / night_in
- **Ref (character_names):** Nora, Alva, Bone Dwelling Interior
- **Giọng:** excited, fast
- **Vào cảnh:** pelt leaving the frame · **Ra cảnh:** walk-through to dark · **Nối:** CUT on dark; S44 opens outside at night
- **Thoại:**
  - `0-3s` “Amber and fossil shells,”
  - `3-7s` “carried here from three to five hundred kilometres away. Some from the Black Sea side.”
  - `7-10s` “So: neighbours, trading, long before farming.”

**prompt**

```
Ultra-wide selfie, a fox pelt sliding out of the frame; Alva at Nora's right wearing a necklace of honey-colored amber beads and small fossil shells. Setting: inside a mammoth-bone dwelling at Mezhyrich, central Ukraine, about 16,000 BC: a low dome of tusks and long bones between hanging reindeer hides, a shallow stone-ringed central hearth burning greasy bone ends (no wood anywhere), fur hides on the floor, a hide water bag hanging from a bone tripod, a low bone ledge along the wall; night; warm firelight from the hearth is the only light.
```

**video_prompt**

```
Handheld front-camera vlog footage, ultra-wide 0.5x lens, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Nora holds the camera at arm's length with her right arm extended toward the bottom-right corner of the frame. Setting: inside a mammoth-bone dwelling at Mezhyrich, central Ukraine, about 16,000 BC: a low dome of tusks and long bones between hanging reindeer hides, a shallow stone-ringed central hearth burning greasy bone ends (no wood anywhere), fur hides on the floor, a hide water bag hanging from a bone tripod, a low bone ledge along the wall; night; warm firelight from the hearth is the only light. Shot: Ultra-wide selfie, Alva at Nora's right showing her necklace. 0-3s: Alva lifts her necklace in her hand to show it; the amber catches the firelight. Nora says, excited, fast: "Amber and fossil shells," 3-7s: Nora leans in to look, excited. Nora says, excited, fast: "carried here from three to five hundred kilometres away. Some from the Black Sea side." 7-10s: Nora turns and ducks toward the doorway flap; the frame darkens. Nora says, excited, fast: "So: neighbours, trading, long before farming." Alva does not speak. The beads swing and click softly. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The camera is the phone itself recording from Nora's hand, so the viewer looks directly at Nora; no phone, no phone body, no phone screen, no UI or app overlay, no case, and no selfie stick appear anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: fire crackle, beads clicking, Nora's voice.
```

### S44

> ✂️ Rút từ 10s xuống 8s trong bản 52 cảnh.

- **Thời lượng:** 8s · **Kiểu quay:** `selfie` · **Bối cảnh:** CAMP / night
- **Ref (character_names):** Nora, Painted Mammoth Skull, Mezhyrich Camp
- **Giọng:** whispering, trembling with excitement
- **Vào cảnh:** from dark · **Ra cảnh:** jump cut · **Nối:** CUT
- **Thoại:**
  - `0-3s` “Hour nineteen. That skull by the entrance. Red ochre,”
  - `3-6s` “dots and lines. I've only seen it in records.”
  - `6-8s` “Okay, breathe.”

**prompt**

```
Ultra-wide selfie outdoors at night; Nora's face lit by firelight from a doorway; to the right of her head, at the entrance of the largest dwelling, a big mammoth skull painted with red ochre dots and lines, lit by the fire. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; night; firelight from doorways is the main light, only faint pale blue moonlight on the snow.
```

**video_prompt**

```
Handheld front-camera vlog footage, ultra-wide 0.5x lens, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Nora holds the camera at arm's length with her right arm extended toward the bottom-right corner of the frame. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; night; firelight from doorways is the main light, only faint pale blue moonlight on the snow. Shot: Ultra-wide selfie outdoors at night, the painted skull to the right of Nora's head (Reveal #2). 0-3s: Nora steps out of the dark and stops; firelight flickers on her face and on the skull beside her. Nora says, whispering, trembling with excitement: "Hour nineteen. That skull by the entrance. Red ochre," 3-6s: She tilts her head to look at it, breath vapor fading fast. Nora says, whispering, trembling with excitement: "dots and lines. I've only seen it in records." 6-8s: She exhales shakily into the camera. Nora says, whispering, trembling with excitement: "Okay, breathe." No locals speak. The skull is in the frame from the first second and does not move; nothing pops into view. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The camera is the phone itself recording from Nora's hand, so the viewer looks directly at Nora; no phone, no phone body, no phone screen, no UI or app overlay, no case, and no selfie stick appear anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: fire crackle from the doorway, night wind, Nora's voice.
```

### S45

- **Thời lượng:** 10s · **Kiểu quay:** `selfie` · **Bối cảnh:** CAMP / night
- **Ref (character_names):** Nora, Torak, Painted Mammoth Skull
- **Giọng:** almost shouting, fast
- **Vào cảnh:** jump cut · **Ra cảnh:** she leans toward the skull · **Nối:** CUT; S46 POV
- **Thoại:**
  - `0-3s` “Calling this a drum is controversial.”
  - `3-7s` “The top has worn dents, and the long bones near it are damaged to match.”
  - `7-10s` “Sounds like a drum to me.”

**prompt**

```
Ultra-wide selfie at night; the painted mammoth skull in the centre behind Nora, Nora on the left of the frame; Torak stands beside the skull holding a long mammoth leg bone. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; night; firelight from doorways is the main light, only faint pale blue moonlight on the snow.
```

**video_prompt**

```
Handheld front-camera vlog footage, ultra-wide 0.5x lens, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Nora holds the camera at arm's length with her right arm extended toward the bottom-right corner of the frame. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; night; firelight from doorways is the main light, only faint pale blue moonlight on the snow. Shot: Ultra-wide selfie at night, the painted skull in the centre behind Nora, Nora on the left. 0-3s: Torak strikes the top of the skull with the end of the long bone, a deep hollow knock. Nora says, almost shouting, fast: "Calling this a drum is controversial." 3-7s: He strikes three more slow beats; the bone rebounds slightly after each strike while the skull stays completely still. Nora says, almost shouting, fast: "The top has worn dents, and the long bones near it are damaged to match." 7-10s: Nora grins wide; at 9s she leans toward the skull. Nora says, almost shouting, fast: "Sounds like a drum to me." Torak does not speak. There is no drum skin: it is solid bone, and only the striking bone bounces. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The camera is the phone itself recording from Nora's hand, so the viewer looks directly at Nora; no phone, no phone body, no phone screen, no UI or app overlay, no case, and no selfie stick appear anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: deep hollow knocks on bone, fire crackle, Nora's voice.
```

### S46

- **Thời lượng:** 10s · **Kiểu quay:** `pov_hand` · **Bối cảnh:** CAMP / night
- **Ref (character_names):** Nora, Painted Mammoth Skull
- **Giọng:** in a whisper
- **Vào cảnh:** hand enters from below · **Ra cảnh:** POV wipe: Torak crosses the lens · **Nối:** CUT on the parka; S47 jump cut
- **Thoại:**
  - `0-3s` “Ochre. Iron-rich earth, ground up.”
  - `3-7s` “It's still on my fingertips. Eighteen thousand years in the ground and the red survives.”
  - `7-10s` “That's how we found it.”

**prompt**

```
First-person view close to the painted mammoth skull at night, red ochre dots right in front of the lens; Nora's bare hand entering from below. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; night; firelight from doorways is the main light, only faint pale blue moonlight on the snow.
```

**video_prompt**

```
First-person handheld smartphone footage at Nora's eye level, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; night; firelight from doorways is the main light, only faint pale blue moonlight on the snow. Shot: First-person view close to the painted skull. 0-3s: Her fingertips touch the red ochre dots on the bone. Nora says from behind the camera, in a whisper: "Ochre. Iron-rich earth, ground up." 3-7s: She lifts her hand and turns it: red powder clings to the ridges of her fingertips. Nora says from behind the camera, in a whisper: "It's still on my fingertips. Eighteen thousand years in the ground and the red survives." 7-10s: At 9s Torak walks across the lens from left to right, his parka filling the frame. Nora says from behind the camera, in a whisper: "That's how we found it." Torak does not speak. Dry ochre powder sticks to the fingerprint ridges. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. First-person point-of-view shot. Nora is completely behind the camera holding it firmly; only her bare empty hand enters the lower frame. No phone, no device, and no selfie stick appear anywhere in the frame. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: night wind, fire crackle, Nora's voice.
```

### S47

- **Thời lượng:** 10s · **Kiểu quay:** `selfie` · **Bối cảnh:** CAMP / night
- **Ref (character_names):** Nora, Mezhyrich Camp
- **Giọng:** in a startled whisper · **Bleep tại:** 1.6s
- **Vào cảnh:** jump cut · **Ra cảnh:** swing toward the camp · **Nối:** CUT in the blur; S48 opens mid-swing
- **Thoại:**
  - `0-3s` “Hour twenty-one. Holy cr— eyes past the bone pile.”
  - `3-7s` “Wolves, after scraps. Up north we argue whether skulls like theirs were early dogs.”
  - `7-10s` “From here? Wolves.”

**prompt**

```
Ultra-wide selfie at the edge of the camp at night; behind Nora, beyond a dark pile of mammoth bones, several pairs of eyes reflecting the firelight in the darkness. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; night; firelight from doorways is the main light, only faint pale blue moonlight on the snow.
```

**video_prompt**

```
Handheld front-camera vlog footage, ultra-wide 0.5x lens, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Nora holds the camera at arm's length with her right arm extended toward the bottom-right corner of the frame. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; night; firelight from doorways is the main light, only faint pale blue moonlight on the snow. Shot: Ultra-wide selfie at the edge of the camp at night, a bone pile behind Nora. 0-3s: Nora glances back over her shoulder and freezes. Nora says, in a startled whisper: "Hour twenty-one. Holy cr— eyes past the bone pile." 3-7s: The pairs of glowing eyes stay still, blinking now and then; one pair slowly backs away. Nora says, in a startled whisper: "Wolves, after scraps. Up north we argue whether skulls like theirs were early dogs." 7-10s: At 9s the camera swings away from her toward the camp in a blur. Nora says, in a startled whisper: "From here? Wolves." No locals in the shot. The eyes are there from the first second; no wolves come closer. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The camera is the phone itself recording from Nora's hand, so the viewer looks directly at Nora; no phone, no phone body, no phone screen, no UI or app overlay, no case, and no selfie stick appear anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: night wind, a distant howl, Nora's voice.
```

### S48

- **Thời lượng:** 10s · **Kiểu quay:** `wide` · **Bối cảnh:** CAMP / night
- **Ref (character_names):** Nora, Mezhyrich Camp
- **Giọng:** softly, from behind the camera
- **Vào cảnh:** mid-swing · **Ra cảnh:** slow tilt up toward the night sky · **Nối:** CUT mid-tilt; S49 continues the tilt up into the sky
- **Thoại:**
  - `0-3s` “Four dwellings, hearths going, the river frozen below.”
  - `3-7s` “On the dig it's a pit with string lines and numbered bags.”
  - `7-10s` “This is what the string lines meant.”

**prompt**

```
Handheld view from a high terrace edge at night: the first mammoth-bone dwelling on the left lit by firelight and smoke, the rest of the camp along the terrace, the frozen river below under faint blue moonlight. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; night; firelight from doorways is the main light, only faint pale blue moonlight on the snow.
```

**video_prompt**

```
Handheld smartphone footage from where Nora stands, slow steady pan, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; night; firelight from doorways is the main light, only faint pale blue moonlight on the snow. Shot: Handheld view from a high terrace edge, slow pan left to right over the camp (Reveal #3). 0-3s: The camera settles from a swing and pans slowly left to right across the four dwellings, firelight glowing at the doorways, smoke rising straight up. Nora says from behind the camera, softly, from behind the camera: "Four dwellings, hearths going, the river frozen below." 3-7s: The pan continues over the frozen river below. Nora says from behind the camera, softly, from behind the camera: "On the dig it's a pit with string lines and numbered bags." 7-10s: At 9s the camera starts tilting slowly up from the camp toward the clear night sky. Nora says from behind the camera, softly, from behind the camera: "This is what the string lines meant." No people in the shot. All four dwellings are there from the first second and stay still; moonlight is only a faint blue tint and the fires are the main light. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. Nora is behind the camera and not visible. No phone, no device, and no selfie stick appear anywhere in the frame. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: quiet night wind, crackle of distant fires, Nora's voice.
```

### S49

> 🆕 Cảnh mới trong bản 52 cảnh.

- **Thời lượng:** 10s · **Kiểu quay:** `wide` · **Bối cảnh:** CAMP / night
- **Ref (character_names):** Nora, Mezhyrich Camp
- **Giọng:** softly, breath fogging
- **Vào cảnh:** mid-tilt up from the camp · **Ra cảnh:** whip pan down to Nora, motion blur · **Nối:** CUT in the blur; S50 opens mid-swing on Nora
- **Thoại:**
  - `0-3s` “Clear sky, colder night. Heat just radiates away.”
  - `3-7s` “And no Polaris up there. The pole sits near Deneb”
  - `7-10s` “right now. Same stars, different centre.”

**prompt**

```
Handheld view from the high terrace edge at night, mid-tilt upward: the glowing doorways of the camp at the bottom edge of the frame, above them a clear deep black sky full of stars. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; night; firelight from doorways is the main light, only faint pale blue moonlight on the snow.
```

**video_prompt**

```
Handheld smartphone footage from where Nora stands, slow steady pan, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; night; firelight from doorways is the main light, only faint pale blue moonlight on the snow. Shot: Handheld view from the terrace edge tilting up from the camp into the clear night sky. 0-3s: The camera keeps tilting slowly upward from the firelit camp until the clear starry sky fills the frame; thin hearth smoke drifts across the bottom edge. Nora says from behind the camera, softly, breath fogging: "Clear sky, colder night. Heat just radiates away." 3-7s: The camera holds on the sky with a slight handheld drift; the stars are sharp and steady, a faint band of the Milky Way across the frame. Nora says from behind the camera, softly, breath fogging: "And no Polaris up there. The pole sits near Deneb" 7-10s: At 9.5s the camera whips back down toward Nora in a blur. Nora says from behind the camera, softly, breath fogging: "right now. Same stars, different centre." No people in the shot. The stars are fixed points that do not move or swirl; the sky does not rotate; only the camera tilts. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. Nora is behind the camera and not visible. No phone, no device, and no selfie stick appear anywhere in the frame. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: quiet night wind, distant crackle of fires, Nora's voice.
```

### S50

- **Thời lượng:** 10s · **Kiểu quay:** `selfie` · **Bối cảnh:** CAMP / night
- **Ref (character_names):** Nora, Mezhyrich Camp
- **Giọng:** tired, slower
- **Vào cảnh:** mid-swing blur · **Ra cảnh:** walk-through into the doorway · **Nối:** CUT on dark; S51 static inside
- **Thoại:**
  - `0-3s` “Hour twenty-two. Toes are numb again, so I'm going in.”
  - `3-7s` “Alva left a gap by the fire for me.”
  - `7-10s` “I'm not wasting it on a better shot.”

**prompt**

```
Ultra-wide selfie at the terrace edge at night, motion blur settling on Nora; the firelit camp behind her; her lips pale, eyes heavy. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; night; firelight from doorways is the main light, only faint pale blue moonlight on the snow.
```

**video_prompt**

```
Handheld front-camera vlog footage, ultra-wide 0.5x lens, natural smartphone perspective, subtle hand shake, auto-exposure, photorealistic documentary realism. Nora holds the camera at arm's length with her right arm extended toward the bottom-right corner of the frame. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; night; firelight from doorways is the main light, only faint pale blue moonlight on the snow. Shot: Ultra-wide selfie at the terrace edge at night, the firelit camp behind Nora. 0-3s: The frame settles on Nora, exhausted, breath vapor fading fast. Nora says, tired, slower: "Hour twenty-two. Toes are numb again, so I'm going in." 3-7s: She glances back at the camp. Nora says, tired, slower: "Alva left a gap by the fire for me." 7-10s: She turns and walks to a dwelling doorway, holding the camera back over her shoulder so it shows her ponytail and the doorway, and ducks through the hide flap; the frame goes dark. Nora says, tired, slower: "I'm not wasting it on a better shot." No locals in the shot. The camp stays still behind her. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The camera is the phone itself recording from Nora's hand, so the viewer looks directly at Nora; no phone, no phone body, no phone screen, no UI or app overlay, no case, and no selfie stick appear anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: night wind, fading to crackle inside, Nora's voice.
```


---

## Hồi 7 — Kết (Giờ 23–24)

### S51

- **Thời lượng:** 10s · **Kiểu quay:** `tripod` · **Bối cảnh:** INT / night_in
- **Ref (character_names):** Nora, Alva, Bone Dwelling Interior
- **Giọng:** in a whisper
- **Vào cảnh:** static frame · **Ra cảnh:** time-skip to dawn · **Nối:** CUT, time-skip
- **Thoại:**
  - `0-3s` “Hour twenty-three. Everyone's asleep.”
  - `3-7s` “I've spent ten years measuring this floor in centimetres.”
  - `7-10s` “Never thought about how warm it was. It is. Barely.”

**prompt**

```
Static frame from a phone propped on a bone ledge inside the dwelling at night: Nora sits wrapped in fur hides beside glowing embers; Alva sleeps in the background. Setting: inside a mammoth-bone dwelling at Mezhyrich, central Ukraine, about 16,000 BC: a low dome of tusks and long bones between hanging reindeer hides, a shallow stone-ringed central hearth burning greasy bone ends (no wood anywhere), fur hides on the floor, a hide water bag hanging from a bone tripod, a low bone ledge along the wall; night; warm firelight from the hearth is the only light.
```

**video_prompt**

```
Static smartphone footage from a phone propped on a ledge, locked-off frame, natural smartphone perspective, photorealistic documentary realism. Setting: inside a mammoth-bone dwelling at Mezhyrich, central Ukraine, about 16,000 BC: a low dome of tusks and long bones between hanging reindeer hides, a shallow stone-ringed central hearth burning greasy bone ends (no wood anywhere), fur hides on the floor, a hide water bag hanging from a bone tripod, a low bone ledge along the wall; night; warm firelight from the hearth is the only light. Shot: Locked-off frame from a bone ledge inside the dwelling. 0-3s: Nora sits still, wrapped in furs; behind her Alva sleeps. Nora says, in a whisper: "Hour twenty-three. Everyone's asleep." 3-7s: The embers pulse red; Nora breathes slowly. Nora says, in a whisper: "I've spent ten years measuring this floor in centimetres." 7-10s: She pulls the furs tighter around herself. Nora says, in a whisper: "Never thought about how warm it was. It is. Barely." Alva sleeps. Nothing moves except the pulsing embers and slow breathing. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The phone is the camera, resting still on a ledge; the frame never moves, and no phone, tripod or selfie stick appears anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: soft ember crackle, slow breathing, Nora's voice.
```

### S52

- **Thời lượng:** 10s · **Kiểu quay:** `tripod` · **Bối cảnh:** CAMP / dawn
- **Ref (character_names):** Nora, Mezhyrich Camp
- **Giọng:** softly, tired, with a small smile
- **Vào cảnh:** static frame · **Ra cảnh:** end · **Nối:** END
- **Thoại:**
  - `0-3s` “Hour twenty-four. First light.”
  - `3-7s` “My hands work, my toes probably work.”
  - `7-10s` “They do this every single winter. I did one day. One.”

**prompt**

```
Static frame from a phone propped at a dwelling entrance, looking out at Nora sitting on a mammoth bone in the snow; the steppe horizon behind her beginning to glow with first light. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; cold blue first light with a faint pink glow on the horizon.
```

**video_prompt**

```
Static smartphone footage from a phone propped on a ledge, locked-off frame, natural smartphone perspective, photorealistic documentary realism. Setting: Mezhyrich, central Ukraine, about 16,000 BC: a winter camp of four low round dwellings built of mammoth bones, wall bases of mammoth lower jaws stacked in a tight zigzag, domes of tusks and long bones covered with frosted reindeer hides, on a snowy river terrace above a broad frozen river, treeless snowy steppe beyond; cold blue first light with a faint pink glow on the horizon. Shot: Locked-off frame from a dwelling entrance looking out at Nora and the steppe. 0-3s: Nora sits still on the bone, wrapped in her parka; the light slowly grows. Nora says, softly, tired, with a small smile: "Hour twenty-four. First light." 3-7s: She flexes her fingers and looks at them. Nora says, softly, tired, with a small smile: "My hands work, my toes probably work." 7-10s: She smiles faintly at the horizon. Nora says, softly, tired, with a small smile: "They do this every single winter. I did one day. One." No one else in the shot. The light rises gradually; nothing else moves. The ground is solid and completely still. Breath vapor is short-lived and fades quickly in the cold air. Nora looks exactly like her reference sheet: same face, honey-blonde high ponytail with curtain bangs, and the same fitted suede-like hide parka with the fox-tooth belt. The phone is the camera, resting still on a ledge; the frame never moves, and no phone, tripod or selfie stick appears anywhere in the shot. Natural smartphone perspective, no exaggerated fisheye distortion. Only Nora speaks; the locals communicate only with gestures and never speak. No subtitles or text appear on screen. This looks like raw unedited amateur video posted online, not a movie or a 3D render. Audio: quiet dawn wind, Nora's voice.
```

