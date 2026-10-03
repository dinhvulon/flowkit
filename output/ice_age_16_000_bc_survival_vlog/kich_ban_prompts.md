# Kịch bản & danh sách prompt — Ice Age 16,000 BC Survival Vlog
**75 cảnh, tổng 10:00.** HORIZONTAL 16:9, material `phone_vlog`, R2V Omni Flash (`GENERATE_VIDEO_REFS`).
File này được dựng tự động từ [clips.json](clips.json) theo cấu trúc chuẩn 7 hồi của skill `/fk-time-travel-vlog`.
- **prompt**: mô tả khung hình đầu tiên (Frame 0).
- **video_prompt**: prompt R2V gửi cho Omni Flash / Veo 3 model.
- **Thoại**: lời Nora nói (Voice profile Laomedeia, Slot 7), đồng bộ native khẩu hình.

## Tổng quan 75 cảnh

| Cảnh | Hồi | Dài | Kiểu quay | Ref (Ingredients) | Lời thoại |
|---|---|---|---|---|---|
| [H1](#h1) | 1 | 8s | `run` | Nora, Nora Body, Nora Outfit, Woolly Mammoth, Mammoth Steppe | TORAK! HELP ME! OH GOD— / SHE'S CHARGING! SHE'S RIGHT BEHIND ME! / DON'T TRIP! GO, GO! |
| [H2](#h2) | 1 | 8s | `run` | Nora, Nora Body, Nora Outfit, Mammoth Steppe | THE RIVERBANK! I HAVE TO SLIDE! / HOLD ON! AAAAAAAHHH—! |
| [S01](#s01) | 1 | 8s | `wide` | Torak, Mezhyrich Camp | Hour one. Twelve hours before the chase. / Coldest stretch of the Ice Age. I've dug here. / It never looked like this. |
| [S02](#s02) | 1 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Mezhyrich Camp | Twenty-four hours, no modern gear, only their stuff. / And there's one thing here I've only ever seen / in a museum drawer. |
| [S03](#s03) | 1 | 8s | `back_selfie` | Nora, Nora Body, Nora Outfit, Torak, Mezhyrich Camp | Okay, that's Torak. My name for him. / Hand flat, palm down. Probably means stay. I stay. / Honestly? I'd spear me too. |
| [S04](#s04) | 2 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Torak, Mezhyrich Camp | No, wait— that white patch on his cheek. / Frostnip. Skin's starting to freeze. / Nobody can see their own face. |
| [S05](#s05) | 2 | 8s | `pov_hand` | Torak, Mezhyrich Camp | Don't rub it. Rubbing damages frozen skin. / Just a warm hand, steady, and wait. / Okay... he's letting me. |
| [S06](#s06) | 2 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Alva, Mezhyrich Camp | Hour two. Alva keeps checking this cord. / Mittens. All four fingers share the heat. / Drop one here, it's gone. |
| [S07](#s07) | 2 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Mezhyrich Camp | Lower jaws, stacked in a zigzag. / I've walked round the museum copy fifty times. / Never with smoke coming out. |
| [S08](#s08) | 2 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Mezhyrich Camp | Real talk, we still argue what these were. / Homes, meat stores, maybe monuments. / This one? Someone's asleep in it. |
| [S08A](#s08a) | 2 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Mezhyrich Camp | Newest dating puts this hut around eighteen thousand years ago. / And people probably didn't stay long. / Big houses. Short stays. Weird. |
| [S09](#s09) | 2 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Alva, Bone Dwelling Interior | Okay, inside. Boots stay on, I assume. / Hearth in the middle, smoke out the top. / And it's... actually warm. |
| [S10](#s10) | 2 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Alva, Bone Dwelling Interior | Hour three. Wood's scarce, so Alva burns bone. / We find almost no charcoal in these hearths. / Now I know why. Probably. |
| [S11](#s11) | 2 | 8s | `pov_hand` | Alva, Bone Dwelling Interior | Yeah, I know, I know. / Don't eat snow. Your body burns heat melting it. / I was testing her. Mostly. |
| [S12](#s12) | 2 | 8s | `pov_hand` | Alva, Bone Dwelling Interior | Hot stone into a hide bag. / Hide burns on a flame, so the heat goes in. / Probably why we find cracked rocks. |
| [S12A](#s12a) | 2 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Alva, Bone Dwelling Interior | Drink it warm. Before you're thirsty. / Cold makes you pee more and feel less thirsty. / Probably why Alva keeps pushing. |
| [S13](#s13) | 2 | 8s | `tripod` | Nora, Nora Body, Nora Outfit, Alva, Bone Dwelling Interior | Every bite of meat, she hands me fat. / Lean meat alone in this cold makes you sick. / Tastes like candle. |
| [S13A](#s13a) | 2 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Alva, Bone Dwelling Interior | Alva's scraping fat off a hide. / End-scrapers. We found them stored in a hut here. / Now I know why. |
| [S14](#s14) | 2 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Torak, Mezhyrich Camp | Hour four. Pits ring every dwelling. / We dig them out full of bone. / Most of us think: freezers. |
| [S15](#s15) | 2 | 8s | `pov_hand` | Torak, Mezhyrich Camp | And... yep. Actual frozen meat in there. / Same cut marks we find on the ribs here. / Just... less dusty. |
| [S15A](#s15a) | 2 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Mezhyrich Camp | Each hut's maybe twelve to twenty-four square metres. / Pits, a work area, a rubbish heap. / Basically a village. With a bin. |
| [S16](#s16) | 2 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Alva, Mezhyrich Camp | Fox pelts, tails still on. / We find tons of fox bones here. / Not dinner. Coats. Maybe also dinner. |
| [S17](#s17) | 2 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Alva, Mezhyrich Camp | She likes my belt. Approves, I think. / Drilled fox canines. Copied from Sungir, way north. / Over two hundred. Nailed it. |
| [S18](#s18) | 2 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Torak, Mammoth Steppe | Hour six. Hauling bone makes you sweat. / And damp fur stops insulating. / So open up before you're hot. |
| [S19](#s19) | 2 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Torak, Mammoth Steppe | Okay, big debate in my field: / did they hunt these, or collect old dead bones? / This one? Collecting. |
| [S20](#s20) | 2 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Torak, Mammoth Steppe | Wind's picking up. That's the real killer. / Same cold, twice the wind, way faster heat loss. / Torak's already heading in. |
| [S20A](#s20a) | 2 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Torak, Mammoth Steppe | Torak's staring really hard at my cheek. / Oh. He's checking for frostnip. Payback. / Am I white? Don't answer. |
| [S21](#s21) | 2 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Alva, Bone Dwelling Interior | Hour eight. Hands in your armpits, not over the fire. / Numb skin can't feel a burn. / Alva agrees. Good company. |
| [S22](#s22) | 2 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Alva, Bone Dwelling Interior | Alva hangs our mittens over the hearth. / Breath and sweat soak into fur all day. / Wet fur is cold fur. |
| [S23](#s23) | 2 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Torak, Mezhyrich Camp | Torak's at the door. Something's up. / Movement on the bluffs. He wants me along. / Trust or bait? Unclear. |
| [S24](#s24) | 3 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Torak, Mammoth Steppe | Hour nine. The mammoth steppe. / Cold, dry grassland, almost no trees for days. / And somewhere out here: mammoths. |
| [S25](#s25) | 3 | 8s | `pov` | Torak, Mammoth Steppe | Walk in his tracks. Saves energy. / He's checking the wind with dry grass. / They smell better than they see. |
| [S25A](#s25a) | 3 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Torak, Mammoth Steppe | Okay, I can't feel two toes. That's new. / Wiggle them. Keep the blood moving. / Torak's not impressed. At all. |
| [S26](#s26) | 3 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Torak, Woolly Rhinoceros | Woolly rhino. Torak wants a very wide circle. / That front horn's worn flat. Sweeps snow off grass. / It's looking. We're leaving. |
| [S27](#s27) | 3 | 8s | `wide` | Steppe Bison, Mammoth Steppe | Steppe bison on the south slope. / Look at those horns. Way wider than today's. / Ice Age steak, basically. |
| [S28](#s28) | 3 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Torak, Woolly Mammoth | Hour ten. Oh... oh, there they are. / Mammoths. Down in the river basin. / Eight, nine... calves in the middle. |
| [S29](#s29) | 3 | 8s | `wide` | Woolly Mammoth, Mammoth Steppe | Textbook elephant behaviour. Calves inside, lead female out front. / Look at the ears. Tiny. Less to freeze. / Shaggy hair outside, wool under. |
| [S30](#s30) | 3 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Torak, Mammoth Steppe | Hour eleven. Torak's showing me the bank. / If anything goes wrong, that's our exit. / Noted. Hopefully totally useless. |
| [S31](#s31) | 3 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Torak, Woolly Mammoth | Real talk, I need a closer shot. / Fifty metres, max. Torak's absolutely furious. / Ten more steps. I promise. |
| [S32](#s32) | 3 | 8s | `pov_hand` | Woolly Mammoth, Mammoth Steppe | The calf's wandering up this way. / Wind just shifted. Mum's trunk is up. / She's got my scent now. |
| [S33](#s33) | 3 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Woolly Mammoth, Mammoth Steppe | Hour twelve. We're way too close. / Head up, trunk curled in. That posture— / Oh no. That's a charge. |
| [S34](#s34) | 4 | 8s | `run` | Nora, Nora Body, Nora Outfit, Woolly Mammoth, Mammoth Steppe | SHE'S CHARGING! GO, GO! / STAY ON THE CRUST! DON'T SINK! / THE BANK! TORAK'S BANK! |
| [S35](#s35) | 4 | 8s | `run` | Nora, Nora Body, Nora Outfit, Woolly Mammoth, Mammoth Steppe | SHE'S GAINING! TWENTY METRES! / MY MITTEN— THE CORD CAUGHT IT! / DON'T TRIP, NORA! |
| [S36](#s36) | 4 | 8s | `pov` | Torak, Mammoth Steppe | Torak! He's down there by the bank! / He's waving me over the edge, now! / Okay. Okay. Going, going! |
| [S37](#s37) | 4 | 8s | `pov` | Woolly Mammoth, Mammoth Steppe | Don't look back. Don't look back— / She's still coming! Still about twenty metres! / The lip. It's right there. |
| [S38](#s38) | 4 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Woolly Mammoth, Mammoth Steppe | THE EDGE! IT'S ALL ICE! / SIT DOWN— FEET FIRST! / HOLD ON! |
| [S39](#s39) | 4 | 8s | `run` | Nora, Nora Body, Nora Outfit, Mammoth Steppe | DOWN, DOWN, DOWN! / OH GOD, OH GOD— / AAAAAAAHHH—! |
| [S40](#s40) | 4 | 8s | `pov` | Woolly Mammoth, Mammoth Steppe | She can't follow us. Not on that. / Front feet slipping... she's sliding sideways now. / She's turning off. Yes! |
| [S41](#s41) | 4 | 8s | `pov` | Woolly Mammoth, Mammoth Steppe | She's turning away. Going back to her calf. / That was a warning charge. / I think. I really hope. |
| [S42](#s42) | 4 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Torak, Mammoth Steppe | Okay, okay. Hand, yes, thank you, thank you. / He's laughing. He's actually laughing at me. / Fair. Completely, totally fair. |
| [S43](#s43) | 4 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Torak, Mammoth Steppe | Hour thirteen. Hands won't stop shaking. / Alva's cord. Still got both mittens. / And that bank? He picked it. |
| [S44](#s44) | 5 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Torak, Mammoth Steppe | Sun's going. Camp smoke, right up ahead. / Never been happier to see bones. / Piles and piles of bones. |
| [S45](#s45) | 5 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Alva, Bone Dwelling Interior | Hour fifteen. Alva heard. Everyone heard. / She's cracking a leg bone for me. / I'll take that as welcome. |
| [S46](#s46) | 5 | 8s | `pov_hand` | Alva, Bone Dwelling Interior | Marrow. Basically pure fat, still warm. / We find long bones broken just like this. / Now I'm eating it. |
| [S47](#s47) | 5 | 8s | `pov_hand` | Alva, Bone Dwelling Interior | Boots got soaked on that slide. / Wet feet lose heat fast. Dry grass in. / The Iceman did this too. |
| [S48](#s48) | 5 | 8s | `tripod` | Nora, Nora Body, Nora Outfit, Alva, Bone Dwelling Interior | Alva moved my sleeping spot. / Inner wall, by the fire, not the door. / I'm not crying. It's the smoke. |
| [S49](#s49) | 6 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Alva, Bone Dwelling Interior | Hour seventeen. An eyed bone needle. / I've catalogued broken ones for years. Never seen one used. / Sorry. Archaeologist. |
| [S49A](#s49a) | 6 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Alva, Bone Dwelling Interior | Oldest eyed needles? Siberia, forty thousand years ago. / Europe, only about twenty-six thousand. / This one's practically brand new. |
| [S50](#s50) | 6 | 8s | `pov_hand` | Alva, Bone Dwelling Interior | She uses the eye. Sinew straight through. / Real seams, tight enough to stop wind. / Also beads. Lots of beads. |
| [S50A](#s50a) | 6 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Alva, Bone Dwelling Interior | Rows of beads only sit straight on fitted clothes. / That's how we know Sungir wore tailored stuff. / Alva's proving it. |
| [S51](#s51) | 6 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Alva, Bone Dwelling Interior | Amber and fossil shells. / Carried in from up to five hundred kilometres. / Some from the Black Sea side. |
| [S51A](#s51a) | 6 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Alva, Bone Dwelling Interior | The same shells turn up at Mezin and Yudinovo. / Different groups, all swapping things. / Stone Age group chat. |
| [S52](#s52) | 6 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Painted Mammoth Skull, Mezhyrich Camp | Hour nineteen. Remember that museum drawer? / Red ochre dots and lines. On the actual skull. / Okay. Okay. Breathe. |
| [S53](#s53) | 6 | 8s | `pov_hand` | Painted Mammoth Skull, Mezhyrich Camp | Ochre. Iron-rich earth, ground up. / Eighteen thousand years from now, it's still red. / That's how we find it. |
| [S54](#s54) | 6 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Torak, Painted Mammoth Skull | Listen to that. / Worn dents on top. A drum? We still argue. / Sounds like a drum to me. |
| [S55](#s55) | 6 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Painted Mammoth Skull, Mezhyrich Camp | The dents match the bones lying beside it. / Somebody hit this. A lot. / I'm choosing to believe music. |
| [S56](#s56) | 6 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Mezhyrich Camp | Hour twenty-one. Brutal, brutal cold out here. / Wait. Eyes, out past the bone pile. / Holy cr— so many. |
| [S57](#s57) | 6 | 8s | `pov` | Mezhyrich Camp | Wolves. After the scraps, I hope. / Some skulls from sites like this look half-dog. / We still argue about it. |
| [S58](#s58) | 6 | 8s | `wide` | Mezhyrich Camp | Clear sky. Colder night, heat just radiates away. / And no Polaris. The pole's near Deneb. / Same stars, different centre. |
| [S58A](#s58a) | 6 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Mezhyrich Camp | Okay. Shivering. That's my body working. / My muscles are burning fuel for heat. / When it stops, then worry. |
| [S59](#s59) | 6 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Cave Lion, Mezhyrich Camp | Hold on. That roar came from the river. / Cave lion. Down on the ice. / Okay. Inside. Right now. |
| [S60](#s60) | 7 | 8s | `tripod` | Nora, Nora Body, Nora Outfit, Alva, Bone Dwelling Interior | Lion outside. Fire inside. I'll take inside. / Alva banked the fire with bone. / Hide and bone. That's the wall. |
| [S61](#s61) | 7 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Bone Dwelling Interior | Hour twenty-three. Everyone's asleep. / I've measured this floor in centimetres for ten years. / Never knew it was warm. |
| [S62](#s62) | 7 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Mezhyrich Camp | Coldest part of the night. Right before sunrise. / Everything's frozen. Even the river mist. / And it's so quiet. |
| [S63](#s63) | 7 | 8s | `selfie` | Nora, Nora Body, Nora Outfit, Mezhyrich Camp | Hour twenty-four. First light. / Hands work. Toes probably work. They did this every winter. / I did one day. One. |

---

## Hồi 1 — Hook & Arrival (Giờ 0–1, vừa sáng)

### H1 — Mammoth Chase Cold Open

- **Thời lượng:** 8s · **Hồi:** 1 · **Kiểu quay:** `run`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Woolly Mammoth, Mammoth Steppe
- **Thoại:** TORAK! HELP ME! OH GOD— / SHE'S CHARGING! SHE'S RIGHT BEHIND ME! / DON'T TRIP! GO, GO!

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length on the snowy steppe at golden-hour sunset, camera held at mid-torso height looking slightly upward, capturing Nora's tall statuesque figure with long slender legs and voluminous bust spilling into a deep plunging V-neckline with prominent push-up cleavage; her face fills 35% of the upper frame -- eyes blown wide in raw terror, mouth open in a desperate gasp, frost on eyelashes and cheeks flushed red; her body is mid-full-sprint on wind-scoured hard crust snow. About twenty metres directly behind her a female woolly mammoth charges straight toward the camera, trunk raised high, snow exploding around its massive feet.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and flails naturally with her sprint strides. Raw unstabilized footage: because the lens is in Nora's own outstretched right hand, every stride she takes jolts the whole frame — her face jumps up and down by about a tenth of the frame height and the horizon behind her tilts a few degrees left and right, with a brief motion blur on each footfall, while her face always stays in the frame. Setting: the Ice Age mammoth steppe near Mezhyrich, Ukraine, about 16,000 BC: wind-scoured snow with dry golden grass tufts on a rolling treeless plain, low orange sunset light. Shot: Ultra-wide running selfie at arm's length, low-angled chest-level camera looking slightly up, framing Nora's tall statuesque figure, long slender legs, and deep plunging cleavage with the charging mammoth behind her. Nora runs on wind-scoured packed crust snow where full sprint is physically possible. The mammoth stays twenty metres behind Nora, never catching up. Left hand is empty. Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Nora sprints flat-out across wind-scoured hard crust snow, her tall statuesque frame and long slender legs pumping powerfully; her voluminous bust bounces with dramatic push-up cleavage in the plunging V-neckline of her reindeer suede dress; her left arm pumps while her right arm stays extended toward the lens for the entire clip; about twenty metres behind her the massive woolly mammoth charges in heavy ground-shaking strides; her outstretched arm jolts the frame hard on every stride. Nora says: "TORAK! HELP ME! OH GOD—" 3-6s: Nora keeps sprinting at maximum speed across the packed snow ridge, long lean legs churning, looking back in sheer terror; the mammoth bears down with thunderous footfalls, trunk up, snow bursting from its feet, staying about twenty metres back; the horizon swings left and right with each of her footfalls. Nora says: "SHE'S CHARGING! SHE'S RIGHT BEHIND ME!" 6-8s: Nora whips her gaze forward toward the river bluff edge, stumbles slightly on hard crust before surging ahead; at 7.5s her outstretched arm whips sideways in a heavy motion blur as she reaches the terrace lip. Nora says: "DON'T TRIP! GO, GO!" The camera is permanently gripped in Nora's outstretched right hand pointing back at herself; she NEVER drops, releases, or lets go of the camera, and the shot NEVER switches to a third-person view. The camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with gestures. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: thundering heavy mammoth footfalls, a deafening trumpet, Nora's ragged hyperventilating gasps, howling steppe wind
```

### H2 — The Glissade Drop & Snow Whiteout

- **Thời lượng:** 8s · **Hồi:** 1 · **Kiểu quay:** `run`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Mammoth Steppe
- **Thoại:** THE RIVERBANK! I HAVE TO SLIDE! / HOLD ON! AAAAAAAHHH—!

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length on a steep snowy river terrace at golden-hour sunset, camera held at chest level looking upward back at Nora; Nora is dropping into a seated glissade posture, feet forward, sliding down the steep 50-degree icy snowbank; her face shows sheer panic and adrenaline, hair whipping, voluminous bust spilling from plunging V-neckline, long legs kicking up dense plumes of powder snow; plumes of snow spray surge directly toward the camera lens.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and braces against the snow. Raw unstabilized footage: because the lens is in Nora's own outstretched right hand, every bump of her slide jolts the whole frame with a brief motion blur, while her face always stays in the frame. Setting: steep 50-degree snowy river terrace slope above the frozen Rosava River near Mezhyrich, Ukraine, about 16,000 BC; icy crust on the lip, deep loose powder snow on the slope below; golden sunset light. Shot: Ultra-wide running selfie at arm's length, chest-level camera angled slightly up, capturing Nora dropping into a seated glissade feet first down the steep slope. Nora performs a seated glissade feet first; she never tumbles or rolls head-over-heels. Her right arm stays firmly extended holding the camera. At 4-6s thick snow spray completely whites out the lens, hiding what happens above. Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Nora reaches the steep terrace lip and drops into a seated glissade posture, feet-first down the 50-degree icy bank; her extended right arm grips the camera tightly aimed back at her screaming face; her boots and hips plow through snow, kicking up initial spray; the drop jerks her outstretched arm and the whole frame downward with her body. Nora says: "THE RIVERBANK! I HAVE TO SLIDE!" 3-6s: Nora slides rapidly down the steep embankment feet first, her body bracing against the snow while her right arm keeps the camera firmly locked on her face; at 4.5s her boots hit a deep pocket of soft drift snow, throwing a massive dense wall of powdery white snow directly into the camera lens. Nora says: "HOLD ON! AAAAAAAHHH—!" 6-8s: The dense aerosolized powder snow completely covers and splatters across the entire camera lens, turning the entire frame into a total whiteout blur of rushing snow with loud wind whoosh; no mammoth visible. The camera is permanently gripped in Nora's outstretched right hand pointing back at herself; she NEVER drops, releases, or lets go of the camera, and the shot NEVER switches to a third-person view. The camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with gestures. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: rushing snow friction hiss, Nora's sustained scream, violent wind roar, sudden muffling of sound as snow blankets the lens
```

### S01 — Hour One: The Winter Camp

- **Thời lượng:** 8s · **Hồi:** 1 · **Kiểu quay:** `wide`
- **Ref (character_names):** Torak, Mezhyrich Camp
- **Thoại:** Hour one. Twelve hours before the chase. / Coldest stretch of the Ice Age. I've dug here. / It never looked like this.

**prompt (Frame 0)**

```text
First-person eye-level POV shot on the snow-covered river terrace at dawn; the whiteout clears into pale morning mist, revealing four massive dome-shaped dwellings constructed from hundreds of giant mammoth skulls, mandibles, and tusks; thin plumes of pale smoke rise from the roof vents; in the midground thirty metres away, a broad-shouldered hunter (Torak) in a heavy fur parka stands watching beside a mammoth tusk arch.
```

**video_prompt (R2V)**

```text
Handheld first-person POV documentary footage, eye-level perspective, ultra-wide 0.5x lens, natural handheld breathing motion, photorealistic documentary realism. The view is Nora's own eyes, and only the world in front of her fills the frame; the view simply moves as she moves. Setting: Mezhyrich settlement, Ukraine, about 16,000 BC; winter dawn, soft pink and blue morning light, light ground mist and woodsmoke drifting across snowy terrace. Shot: First-person POV from eye level, slow handheld pan across the mammoth bone settlement.  0-3s: The whiteout dissolves into pale frosty morning air; the view pans slowly across the Mezhyrich settlement, showing four immense dome-shaped huts built entirely of interlocking mammoth bones. Nora's off-screen voice says: "Hour one. Twelve hours before the chase." 3-6s: The view settles on Hut Four, showing the intricate zigzag pattern of mammoth mandibles in the lower wall and curling tusks on the roof; thin bone-fire smoke drifts from the smoke hole. Nora's off-screen voice says: "Coldest stretch of the Ice Age. I've dug here." 6-8s: Torak stands thirty metres away beside the entrance arch, wearing a thick hooded fur parka, watching silently as the view walks slowly toward him. Nora's off-screen voice says: "It never looked like this." The view is Nora's own eyes; only the world in front of her fills the frame. Only Nora speaks. No subtitles or text. Real amateur footage, not a 3D render. Audio: soft crunch of snow under boots, howling distant winter wind, faint crackle of distant hearth fire
```

### S02 — Hour One: Survival Rules & The Museum Secret

- **Thời lượng:** 8s · **Hồi:** 1 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Mezhyrich Camp
- **Thoại:** Twenty-four hours, no modern gear, only their stuff. / And there's one thing here I've only ever seen / in a museum drawer.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length in the freezing morning light at Mezhyrich camp, camera held at chest level looking slightly up; capturing Nora's tall hourglass figure, deep plunging V-neckline with prominent push-up cleavage, tiny waist, and reindeer suede dress; frost coats her eyelashes and white fox fur hood; her grey-green eyes look directly into the camera with excitement and grit; behind her, mammoth bone huts stand against the pale winter horizon.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Mezhyrich winter camp at dawn, frosty mist, bone huts behind. Shot: Ultra-wide selfie at arm's length, chest-level upward angle, framing Nora with bone dwellings behind. Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Nora walks slowly forward, her right arm extended toward the lens, her breath vapor puffing and fading fast in the cold air; she gestures subtly with her head toward the settlement. Nora says: "Twenty-four hours, no modern gear, only their stuff." 3-6s: She pulls her fur hood slightly closer around her ears, cheeks glowing pink from the biting cold, her plunging cleavage and tiny waist clearly defined in the fitted suede dress. Nora says: "And there's one thing here I've only ever seen" 6-8s: She leans in slightly closer to the lens, lowering her voice with an intrigued, conspiratorial smirk. Nora says: "in a museum drawer." The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: Nora's crisp breath in cold air, crunch of dry frozen snow underfoot, distant steppe wind
```

### S03 — Hour One: Torak's Spear & First Contact

- **Thời lượng:** 8s · **Hồi:** 1 · **Kiểu quay:** `back_selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Torak, Mezhyrich Camp
- **Thoại:** Okay, that's Torak. My name for him. / Hand flat, palm down. Probably means stay. I stay. / Honestly? I'd spear me too.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length in Mezhyrich camp; Nora stands on the left third facing the lens, glancing back over her shoulder at Torak; Torak stands eight metres behind her in a heavy reindeer parka, holding a mammoth-tusk-tipped thrusting spear, holding his left hand flat and low in a halt gesture.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Mezhyrich camp courtyard between bone huts, morning frost, low sun. Shot: Ultra-wide selfie at arm's length framing Nora on the left third and Torak eight metres behind her on the right.  Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Nora stops in her tracks, her outstretched arm still; Torak steps forward two paces, gripping his heavy wooden thrusting spear tipped with polished mammoth bone; his weathered face is guarded and intense. Nora says: "Okay, that's Torak. My name for him." 3-6s: Torak holds his left hand out flat, palm pressing down toward the snow in a clear, authoritative signal to stop; Nora stays completely motionless. Nora says: "Hand flat, palm down. Probably means stay. I stay." 6-8s: Nora glances into the camera with dry humor, then back at Torak; Torak studies her strange dress and confident stance. Nora says: "Honestly? I'd spear me too." The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: Torak's heavy boot crunch in crust snow, distant dog-wolf bark, quiet wind
```


---

## Hồi 2 — Đời thường: Sinh tồn tại trại Mezhyrich (Giờ 1–8)

### S04 — Hour One: Frostnip on the Cheek

- **Thời lượng:** 8s · **Hồi:** 2 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Torak, Mezhyrich Camp
- **Thoại:** No, wait— that white patch on his cheek. / Frostnip. Skin's starting to freeze. / Nobody can see their own face.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length; Nora stands three metres from Torak; Nora's tall hourglass figure and plunging neckline are prominent; Torak has lowered his spear, his weathered face visible in crisp sunlight; a dull, waxy chalk-white circular patch is visible on his left cheekbone; Nora looks at his cheek with concerned professional focus.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Mezhyrich camp, crisp morning light, bone huts in background. Shot: Ultra-wide selfie framing Nora in foreground left with Torak standing close on the right. Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Torak lowers the spear tip to the snow, still watching Nora intently; Nora studies his face and suddenly squints with medical concern. Nora says: "No, wait— that white patch on his cheek." 3-6s: Nora shifts half a step aside so Torak's face shows clearly over her shoulder, pointing subtly toward her own cheek; Torak touches his cheek curiously. Nora says: "Frostnip. Skin's starting to freeze." 6-8s: Nora steps one pace closer, preparing to help; at 7.5s she swings her outstretched arm fast to the right in a heavy motion blur. Nora says: "Nobody can see their own face." The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: footsteps in snow, breath gusts, whip pan whoosh at 7.5s
```

### S05 — Hour One: Treating Frozen Skin with Direct Heat

- **Thời lượng:** 8s · **Hồi:** 2 · **Kiểu quay:** `pov_hand`
- **Ref (character_names):** Torak, Mezhyrich Camp
- **Thoại:** Don't rub it. Rubbing damages frozen skin. / Just a warm hand, steady, and wait. / Okay... he's letting me.

**prompt (Frame 0)**

```text
First-person POV shot from eye level; Nora's bare warm right hand reaches forward and gently presses flat against Torak's waxy white cheekbone; her fur mitten hangs from a braided sinew cord around her neck; Torak's dark weathered eyes blink in surprise, then soften as warmth transfers.
```

**video_prompt (R2V)**

```text
Handheld first-person POV documentary footage, eye-level perspective, ultra-wide 0.5x lens, natural handheld breathing motion, photorealistic documentary realism. The view is Nora's own eyes, and only the world in front of her fills the frame; the view simply moves as she moves. Only her bare empty hand enters the lower frame, coming out of a cream suede sleeve with a thick white fox-fur cuff. Setting: Close-up POV in Mezhyrich camp, Torak's face framed in crisp morning light. Shot: First-person POV; Nora's bare warm hand presses gently on Torak's frozen cheek, mitten hanging from her neck cord.  0-3s: Nora's bare hand gently presses flat against the frozen white patch on Torak's cheek; her fur mitten hangs from the braided sinew cord around her neck; Torak flinches instinctively before steadying. Nora's off-screen voice says: "Don't rub it. Rubbing damages frozen skin." 3-6s: Nora's bare warm palm holds steady against his cheek, letting body heat melt the superficial ice crystals; the edges of the white patch slowly begin to soften. Nora's off-screen voice says: "Just a warm hand, steady, and wait." 6-8s: Torak exhales a warm cloud of breath and nods slowly in acknowledgment; Nora's hand slowly pulls back out of the frame. Nora's off-screen voice says: "Okay... he's letting me." The view is Nora's own eyes; only her bare empty hand enters the lower frame, and it never reaches toward or covers the lens. Only Nora speaks. No subtitles or text. Real amateur footage, not a 3D render. Audio: Torak's deep breath, crunch of boots adjusting stance, quiet wind
```

### S06 — Hour Two: Alva & The Mitten Cord

- **Thời lượng:** 8s · **Hồi:** 2 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Alva, Mezhyrich Camp
- **Thoại:** Hour two. Alva keeps checking this cord. / Mittens. All four fingers share the heat. / Drop one here, it's gone.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length; an elder matriarch (Alva) in an embroidered fox-fur tunic stands beside Nora; Alva reaches out with weathered tattooed hands to adjust and tug the braided sinew neck-cord holding Nora's fur mittens; Nora smiles warmly as she slides her hand into the warm fur mitten; her voluptuous figure and plunging neckline are prominent.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Mezhyrich camp outside Dwelling One, morning sun, mammoth jawbone walls behind. Shot: Ultra-wide selfie framing Nora and Alva side by side, Alva adjusting the mitten cord harness. Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Alva steps in close, stern but caring; she reaches up to adjust the braided sinew cord, fitting it securely over Nora's shoulders. Nora says: "Hour two. Alva keeps checking this cord." 3-6s: Nora slips the thick reindeer-fur mitten directly onto her bare left hand, pulling it fully over all her fingers, the braided cord running from the mitten up around her neck; Alva nods approvingly. Nora says: "Mittens. All four fingers share the heat." 6-8s: Nora turns to camera, tapping the mitten against her chest with a serious expression; Alva pats her shoulder. Nora says: "Drop one here, it's gone." The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: rustle of fur garments, dry snow crunch
```

### S07 — Hour Two: Herringbone Mammoth Mandible Architecture

- **Thời lượng:** 8s · **Hồi:** 2 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Mezhyrich Camp
- **Thoại:** Lower jaws, stacked in a zigzag. / I've walked round the museum copy fifty times. / Never with smoke coming out.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length; Nora walks along the foundation wall of Dwelling One; the wall behind her consists of dozens of mammoth lower jawbones (mandibles) stacked in an intricate interlocking herringbone zigzag; Nora's tall hourglass figure, tiny waist, and plunging neckline are framed dynamically against the ancient bone architecture.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Exterior of Mezhyrich Dwelling One, foundation wall of interlocking mammoth lower jawbones, bright morning daylight. Shot: Ultra-wide walking selfie, chest-level camera looking slightly up, framing Nora alongside the zigzag bone wall.  Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Nora walks slowly along the curved exterior wall, her extended right arm holding the camera; she glances admiringly at the stacked bones behind her. Nora says: "Lower jaws, stacked in a zigzag." 3-6s: She slows and steps aside so the interlocking zigzag of mammoth jaws fills the wall behind her shoulder; thin smoke rises from the dome above and bends in the wind. Nora says: "I've walked round the museum copy fifty times." 6-8s: She glances up at the smoke, grins, then shakes her head at herself. Nora says: "Never with smoke coming out." The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: rhythmic crunch of snow, wind whistling through bone crevices
```

### S08 — Hour Two: What Were These Huts?

- **Thời lượng:** 8s · **Hồi:** 2 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Mezhyrich Camp
- **Thoại:** Real talk, we still argue what these were. / Homes, meat stores, maybe monuments. / This one? Someone's asleep in it.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length looking up at the roof of the bone dwelling; massive curved mammoth tusks arch over the entrance and roof apex, supporting layers of stitched reindeer hides weighed down with mammoth leg bones; Nora's tall stature and plunging neckline stand out against the grand mammoth bone dome.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Exterior entrance of Dwelling Four, Mezhyrich camp, mammoth tusk roof arches. Shot: Ultra-wide selfie angled upward, capturing the tusk roof vault and Nora's face and upper body.  Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Nora stands in front of the entrance arch of curved mammoth tusks, the hide-covered dome rising behind her. Nora says: "Real talk, we still argue what these were." 3-6s: Behind her the hide flap over the doorway sways in the wind and lifts slightly, showing a person asleep under furs in the dim firelit interior; the sleeper is there from the first second and only breathes slowly. Nora says: "Homes, meat stores, maybe monuments." 6-8s: She glances back at the doorway, then grins into the lens and lowers her voice. Nora says: "This one? Someone's asleep in it." The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: creak of tusk framework under wind load, flapping hide edges, distant voices
```

### S08A — Hour Two: How Old, How Long?

- **Thời lượng:** 8s · **Hồi:** 2 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Mezhyrich Camp
- **Thoại:** Newest dating puts this hut around eighteen thousand years ago. / And people probably didn't stay long. / Big houses. Short stays. Weird.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length beside a mammoth-bone dwelling at Mezhyrich in bright cold morning light; Nora walks backward along the stacked jaw wall, frost glittering on the hide-covered dome behind her; her tall hourglass figure and plunging neckline are framed against the bone architecture.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Mezhyrich camp beside the tusk-arched entrance of Dwelling Four, bright cold morning light, frost on the hides. Shot: Ultra-wide walking selfie at arm's length, chest-level upward angle, framing Nora with the bone dwelling behind her. Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Nora walks slowly backward beside the bone dwelling at about half a metre per second, glancing at the frosted hides. Nora says, fast, geeking out: "Newest dating puts this hut around eighteen thousand years ago." 3-6s: She stops by the entrance; behind her, frost glitters on the stacked jaws and the hide-covered dome. Nora says, fast, geeking out: "And people probably didn't stay long." 6-8s: She raises her eyebrows at the lens, then looks toward the dark doorway beside her. Nora says, fast, geeking out: "Big houses. Short stays. Weird." The dwelling is solid and completely still; it only slides past because she walks. Slight vertical bounce with each step. The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: crunch of frozen snow, wind across the hides, distant camp sounds
```

### S09 — Hour Three: Stepping Inside Dwelling Four

- **Thời lượng:** 8s · **Hồi:** 2 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Alva, Bone Dwelling Interior
- **Thoại:** Okay, inside. Boots stay on, I assume. / Hearth in the middle, smoke out the top. / And it's... actually warm.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length; Nora ducks her head under a heavy double-layered reindeer hide door flap; the frame shifts from bright exterior snow glare to the warm amber glow of a hearth fire burning inside the bone dwelling; Nora's face is lit by flickering firelight, her cleavage and hourglass silhouette glowing warmly; Alva is tending the fire inside.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Entrance doorway transitioning into Bone Dwelling Four interior, warm hearth fire, mammoth bone roof beams. Shot: Ultra-wide selfie as Nora steps through the hide door into the interior. Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Nora steps through the low doorway, ducking under the thick hide flap; the exposure adjusts from bright snow to deep warm interior firelight. Nora says: "Okay, inside. Boots stay on, I assume." 3-6s: She moves into the circular room; in the background, Alva kneels by a sunken stone-lined hearth where amber flames dance. Nora says: "Hearth in the middle, smoke out the top." 6-8s: Nora exhales a sigh of comfort, unfastening her hood as ambient warmth surrounds her; at 7.5s she swings her outstretched arm fast to the left in a motion blur. Nora says: "And it's... actually warm." The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: muffled outside wind, crackle of bone fire, soft hum of domestic life
```

### S10 — Hour Three: Burning Bone as Fuel

- **Thời lượng:** 8s · **Hồi:** 2 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Alva, Bone Dwelling Interior
- **Thoại:** Hour three. Wood's scarce, so Alva burns bone. / We find almost no charcoal in these hearths. / Now I know why. Probably.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length by the hearth; Alva is placing spongy, porous mammoth bone joints directly onto the hot embers; the bone fuel burns with a slow, smoky yellow flame; Nora sits close, firelight illuminating her face, cleavage, and reindeer suede dress.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Interior of bone dwelling, central stone-lined hearth, glowing embers, bone fuel. Shot: Ultra-wide selfie framing Nora sitting by the hearth with Alva feeding bone fuel into the fire.  Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: The frame settles from a leftward swing onto Nora seated by the hearth; behind her, Alva carefully stacks porous mammoth bone ends into the red-hot coals. Nora says: "Hour three. Wood's scarce, so Alva burns bone." 3-6s: The porous cancellous bone begins to sizzle and catch, the fat sizzling and the flame catching slowly, with no burst. Nora says: "We find almost no charcoal in these hearths." 6-8s: Nora warms her free hand near the embers and looks back into the lens with a wry smile. Nora says: "Now I know why. Probably." The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: sizzle of rendered bone fat in coals, popping embers, cozy fire crackle
```

### S11 — Hour Three: The Snow Hydration Warning

- **Thời lượng:** 8s · **Hồi:** 2 · **Kiểu quay:** `pov_hand`
- **Ref (character_names):** Alva, Bone Dwelling Interior
- **Thoại:** Yeah, I know, I know. / Don't eat snow. Your body burns heat melting it. / I was testing her. Mostly.

**prompt (Frame 0)**

```text
First-person POV shot inside the dwelling; Nora's hand holds a small clump of clean white snow near the frame; Alva immediately reaches out, firmly pushes Nora's hand down, shakes her head with stern maternal authority, and offers a shallow hide bowl of warm thawed water instead.
```

**video_prompt (R2V)**

```text
Handheld first-person POV documentary footage, eye-level perspective, ultra-wide 0.5x lens, natural handheld breathing motion, photorealistic documentary realism. The view is Nora's own eyes, and only the world in front of her fills the frame; the view simply moves as she moves. Only her bare empty hand enters the lower frame, coming out of a cream suede sleeve with a thick white fox-fur cuff. Setting: Interior of bone dwelling, hearthside, Alva kneeling opposite Nora. Shot: First-person POV; Nora holds snow, Alva intervenes sternly and offers warm water.  0-3s: Nora's bare fingers hold a small clump of snow; Alva's hand gently stops Nora's wrist; Alva frowns sternly, shaking her head. Nora's off-screen voice says: "Yeah, I know, I know." 3-6s: Alva takes the snow away, tossing it aside, and pushes forward a shallow hide bowl filled with steaming thawed melted snow water. Nora's off-screen voice says: "Don't eat snow. Your body burns heat melting it." 6-8s: Nora's bare hand accepts the warm bowl, steam rising across the lower lens. Nora's off-screen voice says: "I was testing her. Mostly." The view is Nora's own eyes; only her bare empty hand enters the lower frame, and it never reaches toward or covers the lens. Only Nora speaks. No subtitles or text. Real amateur footage, not a 3D render. Audio: water slosh, gentle hearth sizzle
```

### S12 — Hour Three: Stone Boiling in Bison Hide

- **Thời lượng:** 8s · **Hồi:** 2 · **Kiểu quay:** `pov_hand`
- **Ref (character_names):** Alva, Bone Dwelling Interior
- **Thoại:** Hot stone into a hide bag. / Hide burns on a flame, so the heat goes in. / Probably why we find cracked rocks.

**prompt (Frame 0)**

```text
First-person POV shot; Alva uses split-antler tongs to lift a fire-blackened river cobble, hot but not glowing, from the embers and lower it into a watertight folded bison-hide pouch filled with water; the water around the stone hisses with small localized bubbles around the stone and gradually rising steam, without burning the hide; Nora's empty left hand is resting at the edge of the hearth.
```

**video_prompt (R2V)**

```text
Handheld first-person POV documentary footage, eye-level perspective, ultra-wide 0.5x lens, natural handheld breathing motion, photorealistic documentary realism. The view is Nora's own eyes, and only the world in front of her fills the frame; the view simply moves as she moves. Only her bare empty hand enters the lower frame, coming out of a cream suede sleeve with a thick white fox-fur cuff. Setting: Interior of bone dwelling, sunken hearth, folded raw hide container resting in a floor pit. Shot: First-person POV close-up of stone boiling in a raw hide water container.  0-3s: Alva grips a fire-blackened quartzite cobblestone, hot but not glowing, with split-antler tongs and slowly lowers it into a bison-hide basin filled with water. Nora's off-screen voice says: "Hot stone into a hide bag." 3-6s: As the hot stone submerges, the water hisses and bubbles only around the stone, and steam rises gradually by convection. Nora's off-screen voice says: "Hide burns on a flame, so the heat goes in." 6-8s: Small bubbles keep rising around the stone while the steam slowly thickens; Alva reaches for a second stone; the water never boils violently. Nora's off-screen voice says: "Probably why we find cracked rocks." The view is Nora's own eyes; only her bare empty hand enters the lower frame, and it never reaches toward or covers the lens. Only Nora speaks. No subtitles or text. Real amateur footage, not a 3D render. Audio: sharp hiss as stone hits water, small bubbling around the stone, crackle of fire
```

### S12A — Hour Three: Drink Before You're Thirsty

- **Thời lượng:** 8s · **Hồi:** 2 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Alva, Bone Dwelling Interior
- **Thoại:** Drink it warm. Before you're thirsty. / Cold makes you pee more and feel less thirsty. / Probably why Alva keeps pushing.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length by the hearth inside the bone dwelling; behind Nora, Alva pours steaming warm water from a hide bag into a shallow bone cup and holds it up beside Nora's face; firelight on Nora's face, plunging neckline and reindeer suede dress.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Interior of the bone dwelling, hearthside, a hide water bag warmed by stone-boiled water, warm firelight. Shot: Ultra-wide selfie framing Nora on the left third and Alva at the hearth behind her shoulder. Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Behind Nora, Alva pours warm water from a hide bag into a shallow bone cup and holds it up beside Nora's face. Nora says, tired, matter-of-fact: "Drink it warm. Before you're thirsty." 3-6s: Nora leans in and sips from the cup in Alva's hand; faint steam drifts up past her face. Nora says, tired, matter-of-fact: "Cold makes you pee more and feel less thirsty." 6-8s: Alva refills the cup straight away, firm and unhurried; Nora gives the lens a resigned look. Nora says, tired, matter-of-fact: "Probably why Alva keeps pushing." The water steams gently and does not boil; the hide bag sags slightly as it empties. The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: soft pour of water, fire crackle, quiet swallow
```

### S13 — Hour Three: Meat, Fat & Candle Taste

- **Thời lượng:** 8s · **Hồi:** 2 · **Kiểu quay:** `tripod`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Alva, Bone Dwelling Interior
- **Thoại:** Every bite of meat, she hands me fat. / Lean meat alone in this cold makes you sick. / Tastes like candle.

**prompt (Frame 0)**

```text
Static locked-off shot from a fixed viewpoint inside the bone dwelling; Nora sits cross-legged on plush reindeer furs by the glowing hearth; Alva hands her a strip of dried meat and a dense square cube of cured white mammoth fat; Nora chews the meat and fat; her voluptuous figure, tiny waist, and plunging neckline are highlighted by warm firelight.
```

**video_prompt (R2V)**

```text
Static locked-off footage from a fixed viewpoint resting on a bone ledge, eye-level perspective, wide lens, fixed stable framing, natural warm hearth lighting, photorealistic documentary realism. The frame is completely still; Nora sits in frame interacting naturally with the environment and locals. Her hands are busy with food or garments; she never reaches toward, touches, covers, or points at the camera lens. Setting: Cozy interior of bone dwelling, warm hearth, furs on the floor, mammoth bone roof beams. Shot: Static locked-off shot framing Nora and Alva sharing food beside the hearth.  BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh dress of bleached white reindeer suede with long sleeves, plush white arctic-fox fur trim at cuffs and hem, an attached fur hood draped on her shoulders, plunging V-neckline laced loosely with thin leather ties, cinched by a wide leather belt sewn with drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur boots. 0-3s: Alva hands Nora a strip of dried meat together with a white cube of rendered mammoth fat; Nora takes them with her hands. Nora says: "Every bite of meat, she hands me fat." 3-6s: Nora chews the meat and the fat together, talking with her mouth half full, grimacing slightly at the taste. Nora says: "Lean meat alone in this cold makes you sick." 6-8s: She keeps eating; Alva watches, amused. Nora says: "Tastes like candle." The frame never moves; nothing that holds or supports the view is visible anywhere in the shot. Nora stays in frame. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks. No subtitles or text. Real documentary footage, not a 3D render. Audio: crackling fire, soft chewing, cozy room ambience
```

### S13A — Hour Three: End-Scrapers in Action

- **Thời lượng:** 8s · **Hồi:** 2 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Alva, Bone Dwelling Interior
- **Thoại:** Alva's scraping fat off a hide. / End-scrapers. We found them stored in a hut here. / Now I know why.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length inside the bone dwelling; behind Nora, Alva kneels over a stretched reindeer hide, scraping it with a small flint end-scraper; firelight on Nora's face, plunging neckline and reindeer suede dress.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Interior of the bone dwelling, hearthside work area, a stretched reindeer hide on the floor, warm firelight. Shot: Ultra-wide selfie framing Nora on the left third and Alva scraping a hide behind her shoulder. Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Behind Nora, Alva kneels over a reindeer hide stretched flesh-side up and pushes a small flint end-scraper along it in short firm strokes. Nora says, fast, geeking out: "Alva's scraping fat off a hide." 3-6s: Thin curls of fat and membrane gather ahead of the flint edge; the hide flexes slightly under each stroke. Nora says, fast, geeking out: "End-scrapers. We found them stored in a hut here." 6-8s: Nora glances back at the scraper, then looks into the lens with a small amazed laugh. Nora says, fast, geeking out: "Now I know why." The flint tool is small and grey with a rounded working edge and natural conchoidal fracture marks; scraping is slow and repetitive, never fast. The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: rhythmic scrape of flint on hide, fire crackle
```

### S14 — Hour Four: Permafrost Storage Freezers

- **Thời lượng:** 8s · **Hồi:** 2 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Torak, Mezhyrich Camp
- **Thoại:** Hour four. Pits ring every dwelling. / We dig them out full of bone. / Most of us think: freezers.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length outside behind Dwelling One; Torak is lifting a massive flat mammoth shoulder blade (scapula) serving as a cellar lid; beneath it is a deep circular storage pit dug into the frozen permafrost ground; Nora stands beside him, her tall hourglass figure and fur-trimmed dress sharp against the bright midday snow.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Exterior of Mezhyrich camp, storage pit zone behind bone huts, bright cold midday sun. Shot: Ultra-wide selfie framing Nora and Torak opening a permafrost storage pit.  Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Nora walks toward the perimeter of the huts where Torak kneels beside a circular pit covered with a mammoth scapula. Nora says: "Hour four. Pits ring every dwelling." 3-6s: Torak heaves the heavy bone lid aside, revealing a frost-lined pit dug into the frozen ground, about a metre deep, with frozen meat stacked inside. Nora says: "We dig them out full of bone." 6-8s: Nora leans to one side so the open pit shows clearly behind her shoulder, eyebrows raised. Nora says: "Most of us think: freezers." The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: heavy scrape of bone against frozen gravel, crisp wind
```

### S15 — Hour Four: Ice Age Meat Cache

- **Thời lượng:** 8s · **Hồi:** 2 · **Kiểu quay:** `pov_hand`
- **Ref (character_names):** Torak, Mezhyrich Camp
- **Thoại:** And... yep. Actual frozen meat in there. / Same cut marks we find on the ribs here. / Just... less dusty.

**prompt (Frame 0)**

```text
First-person POV shot looking down into the permafrost pit; large slabs of dark red mammoth meat and fatty ribs are stacked neatly in the frost-rimmed pit; Nora's bare fingers point to distinct clean butchery cut marks on a frozen mammoth rib; ice crystals glisten on the preserved meat.
```

**video_prompt (R2V)**

```text
Handheld first-person POV documentary footage, eye-level perspective, ultra-wide 0.5x lens, natural handheld breathing motion, photorealistic documentary realism. The view is Nora's own eyes, and only the world in front of her fills the frame; the view simply moves as she moves. Only her bare empty hand enters the lower frame, coming out of a cream suede sleeve with a thick white fox-fur cuff. Setting: POV looking down into a metre-deep frozen storage pit, glistening frost on mammoth meat slabs. Shot: First-person POV close-up into the permafrost meat cache.  0-3s: The view looks straight down into the frozen pit; neat stacks of mammoth ribs and tallow blocks are preserved in natural ice. Nora's off-screen voice says: "And... yep. Actual frozen meat in there." 3-6s: Nora's empty hand enters the frame, tracing fresh parallel cut marks left by a flint blade. Nora's off-screen voice says: "Same cut marks we find on the ribs here." 6-8s: Torak's hands slide the heavy scapula lid back over the pit from the left. Nora's off-screen voice says: "Just... less dusty." The view is Nora's own eyes; only her bare empty hand enters the lower frame, and it never reaches toward or covers the lens. Only Nora speaks. No subtitles or text. Real amateur footage, not a 3D render. Audio: subtle echo inside pit, crunch of ice crystals, heavy thud of bone lid closing
```

### S15A — Hour Four: A Village With a Bin

- **Thời lượng:** 8s · **Hồi:** 2 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Mezhyrich Camp
- **Thoại:** Each hut's maybe twelve to twenty-four square metres. / Pits, a work area, a rubbish heap. / Basically a village. With a bin.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length walking through Mezhyrich camp at midday; behind Nora, two mammoth-bone dwellings, a covered storage pit, a work area with flint flakes and a heap of discarded bones; her tall hourglass figure and plunging neckline in crisp daylight.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Mezhyrich camp, between the four bone dwellings, storage pits, a work area with flint flakes, and a bone rubbish heap, bright midday light. Shot: Ultra-wide walking selfie, chest-level upward angle, framing Nora walking through the camp. Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Nora walks slowly through the camp; two bone dwellings sit behind her, close together on the terrace. Nora says, fast, dry: "Each hut's maybe twelve to twenty-four square metres." 3-6s: She passes a covered storage pit and a work area scattered with flint flakes; the bone heap is visible farther back. Nora says, fast, dry: "Pits, a work area, a rubbish heap." 6-8s: She glances over her shoulder at the heap of discarded bones, then grins into the lens. Nora says, fast, dry: "Basically a village. With a bin." All dwellings, pits and the bone heap are there from the first second and stay still; they only slide past because she walks. Slight vertical bounce with each step. The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: crunch of snow, distant knapping clicks, wind
```

### S16 — Hour Five: Fox Pelts, Tails Still On

- **Thời lượng:** 8s · **Hồi:** 2 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Alva, Mezhyrich Camp
- **Thoại:** Fox pelts, tails still on. / We find tons of fox bones here. / Not dinner. Coats. Maybe also dinner.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length; Nora stands beside a drying rack of mammoth ribs draped with thick white and silver arctic fox pelts; Alva is combing the fur with a bone comb; Nora strokes the fluffy white fox fur trim on her own hood and cuffs; her tall voluptuous frame and deep plunging cleavage are in crisp daylight focus.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Exterior tanning rack area near Dwelling Two, drying fox pelts, bright afternoon light. Shot: Ultra-wide selfie showing Nora beside fox pelts with Alva working nearby.  Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Nora walks past drying racks of plush arctic fox skins, showing the density of the fur. Nora says: "Fox pelts, tails still on." 3-6s: She lifts the fluffy tail of one pelt with her free hand; the fur ripples in the breeze. Nora says: "We find tons of fox bones here." 6-8s: Alva glances over at Nora's fox-fur hood and gives her a dry, amused look. Nora says: "Not dinner. Coats. Maybe also dinner." The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: rustle of soft fur skins, Alva's bone comb scraping, whistling breeze
```

### S17 — Hour Five: Sungir Fox Canine Belt Replica

- **Thời lượng:** 8s · **Hồi:** 2 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Alva, Mezhyrich Camp
- **Thoại:** She likes my belt. Approves, I think. / Drilled fox canines. Copied from Sungir, way north. / Over two hundred. Nailed it.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length; Alva leans in and curiously touches the drilled arctic-fox canine teeth sewn in neat rows across Nora's wide leather belt; Alva smiles with admiration at the craftsmanship; Nora looks down proudly at her waist; her curvy hourglass silhouette, tiny waist, and deep cleavage are accentuated.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Mezhyrich camp courtyard, afternoon sunlight, mammoth skull foundation behind. Shot: Ultra-wide selfie highlighting Nora's belted waist and Alva inspecting the canine teeth.  Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Alva gently runs her fingers over the rows of drilled predator teeth on Nora's leather belt. Nora says: "She likes my belt. Approves, I think." 3-6s: Nora glances down at the rows of drilled fox canine teeth sewn along her leather belt. Nora says: "Drilled fox canines. Copied from Sungir, way north." 6-8s: She looks back into the lens with a proud, geeky smile. Nora says: "Over two hundred. Nailed it." The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: clink of drilled bone beads and teeth, wind
```

### S18 — Hour Six: Hauling Bone & Regulating Core Sweat

- **Thời lượng:** 8s · **Hồi:** 2 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Torak, Mammoth Steppe
- **Thoại:** Hour six. Hauling bone makes you sweat. / And damp fur stops insulating. / So open up before you're hot.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length on the snowy slope outside camp; Nora and Torak are dragging a heavy mammoth femur on a rawhide skid; Nora's cheeks are flushed from physical exertion; she reaches up with her free left hand to loosen the leather ties at her plunging collar; her tall muscular hourglass build and deep cleavage are prominent.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Snowy slope outside Mezhyrich camp, afternoon sun, dragging bone skid. Shot: Ultra-wide selfie as Nora hauls heavy bone, loosening her collar to regulate body heat.  Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Nora strains forward, pulling a heavy rawhide strap looped over her shoulder, hauling a mammoth femur across the snow with Torak. Nora says: "Hour six. Hauling bone makes you sweat." 3-6s: She pauses, breathing hard, and uses her free hand to loosen the ties at her chest, letting trapped heat escape. Nora says: "And damp fur stops insulating." 6-8s: Torak, who has already loosened his own collar, glances back and nods in silent agreement. Nora says: "So open up before you're hot." The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: heavy crunch of bone sled in snow, Nora's rhythmic exertion breath, wind
```

### S19 — Hour Six: Scavenging vs Hunting Megafauna

- **Thời lượng:** 8s · **Hồi:** 2 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Torak, Mammoth Steppe
- **Thoại:** Okay, big debate in my field: / did they hunt these, or collect old dead bones? / This one? Collecting.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length in a shallow snow-filled ravine; Nora examines an enormous weathered mammoth skull embedded in frozen silt; Torak tests the bone density with an antler hammer; Nora's tall hourglass frame, tiny waist, and plunging neckline are highlighted against the bleached megafauna fossil.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Eroded river ravine near Mezhyrich, natural bone accumulation site, pale winter sunlight. Shot: Ultra-wide selfie framing Nora beside an ancient weathered mammoth skull.  Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Nora crouches beside a mammoth skull half-buried in the frozen terrace silt behind her. Nora says: "Okay, big debate in my field:" 3-6s: Torak taps the thick cranial bone to check for weathering; ancient bone flakes off, showing it died long ago. Nora says: "did they hunt these, or collect old dead bones?" 6-8s: Nora looks into camera, sharing the archaeological takeaway. Nora says: "This one? Collecting." The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: tap of antler on dry weathered bone, howling ravine wind, boot crunches
```

### S20 — Hour Seven: The Real Killer: Steppe Windchill

- **Thời lượng:** 8s · **Hồi:** 2 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Torak, Mammoth Steppe
- **Thoại:** Wind's picking up. That's the real killer. / Same cold, twice the wind, way faster heat loss. / Torak's already heading in.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length on the open ridge; howling winds whip ground-drift snow (spindrift) across Nora's boots; Nora pulls her fur hood tight around her cheeks, squinting against the fierce blowing snow; her tall frame leans forward against the arctic gale, plunging neckline laced snug.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Exposed steppe ridge above river valley, severe wind-drift snow, late afternoon overcast. Shot: Ultra-wide selfie as Nora leans into the gale on the ridge.  Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Violent arctic wind whips across the frame, sending horizontal ribbons of dry snow swirling around Nora's boots and waist. Nora says: "Wind's picking up. That's the real killer." 3-6s: She pulls her hood forward to shield her cheeks, raising her voice over the roar of the gale. Nora says: "Same cold, twice the wind, way faster heat loss." 6-8s: Torak gestures urgently toward the valley below to seek shelter from the exposed ridge. Nora says: "Torak's already heading in." The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: howling roar of the steppe gale, flapping fur hood, spindrift hiss
```

### S20A — Hour Seven: Payback Frostnip Check

- **Thời lượng:** 8s · **Hồi:** 2 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Torak, Mammoth Steppe
- **Thoại:** Torak's staring really hard at my cheek. / Oh. He's checking for frostnip. Payback. / Am I white? Don't answer.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length on a windy steppe ridge; Torak in a hooded fur parka stands close beside Nora, studying her cheek; spindrift streams past their boots; Nora's hood is pulled forward, her plunging neckline laced snug.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Exposed steppe ridge above the river valley, blowing spindrift, late afternoon overcast light. Shot: Ultra-wide selfie framing Nora on the left and Torak stepping in close on the right. Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Torak steps close and stares hard at Nora's left cheek, his own face half hidden in his fur hood. Nora says, shouting over the wind, half laughing: "Torak's staring really hard at my cheek." 3-6s: He presses his warm bare palm flat and still against her cheek; he does not rub; Nora goes still. Nora says, shouting over the wind, half laughing: "Oh. He's checking for frostnip. Payback." 6-8s: Torak lowers his hand and nods once; Nora looks into the lens, half laughing. Nora says, shouting over the wind, half laughing: "Am I white? Don't answer." Torak's palm stays flat and still on her cheek; nobody rubs the skin. Snow streams across the ground in the wind; the ground is solid and completely still. The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: howling wind, spindrift hiss, flapping fur hood
```

### S21 — Hour Eight: Armpit Warming vs Fire Burns

- **Thời lượng:** 8s · **Hồi:** 2 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Alva, Bone Dwelling Interior
- **Thoại:** Hour eight. Hands in your armpits, not over the fire. / Numb skin can't feel a burn. / Alva agrees. Good company.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length back inside the bone dwelling; Nora sits beside the hearth, tucking her cold bare hands under her armpits against her core; Alva sits nearby doing the exact same warming posture; firelight flickers across Nora's face, deep cleavage, and reindeer suede dress.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Interior of bone dwelling, warm hearth glowing, safe from outside storm. Shot: Ultra-wide selfie of Nora tucking hands into armpits to demonstrate safe rewarming.  Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Nora sits close to the fire but keeps her numb hands tucked tightly into her armpits against her torso. Nora says: "Hour eight. Hands in your armpits, not over the fire." 3-6s: She glances at Alva, who is also warming her fingers under her tunic against her core heat. Nora says: "Numb skin can't feel a burn." 6-8s: Nora smiles at the camera, explaining the physiological reason. Nora says: "Alva agrees. Good company." The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: crackling hearth fire, deep sigh of warmth, wind howling outside hide walls
```

### S22 — Hour Eight: Drying Mittens Over the Hearth

- **Thời lượng:** 8s · **Hồi:** 2 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Alva, Bone Dwelling Interior
- **Thoại:** Alva hangs our mittens over the hearth. / Breath and sweat soak into fur all day. / Wet fur is cold fur.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length by the hearth inside the bone dwelling; behind Nora, Alva hangs a pair of damp fur mittens on a rack of mammoth ribs well above the flames, faint steam rising from the fur; firelight on Nora's face, plunging neckline and reindeer suede dress.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Interior of the bone dwelling, hearthside, a rack of mammoth ribs above the hearth for drying gear, warm firelight. Shot: Ultra-wide selfie framing Nora on the left third and Alva at the drying rack behind her shoulder. Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Behind Nora, Alva hangs a pair of damp fur mittens, just taken off after wearing them outside, by their braided cords on a rack of mammoth ribs well above the hearth. Nora says, fast, dry: "Alva hangs our mittens over the hearth." 3-6s: Faint steam rises from the damp fur in the warm air; Alva turns one mitten inside out on the rack. Nora says, fast, dry: "Breath and sweat soak into fur all day." 6-8s: Alva nudges the rack a little farther from the flames; Nora nods at the lens. Nora says, fast, dry: "Wet fur is cold fur." The mittens stay well above the flames and never catch fire; steam rises gently by convection. The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: fire crackle, soft drip of melting frost, rustle of fur
```

### S23 — Hour Eight: Scout Call & Heading Out

- **Thời lượng:** 8s · **Hồi:** 2 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Torak, Mezhyrich Camp
- **Thoại:** Torak's at the door. Something's up. / Movement on the bluffs. He wants me along. / Trust or bait? Unclear.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length at the dwelling door; Torak appears holding two heavy mammoth-bone thrusting spears; he points urgently toward the snowy northern river bluffs; Nora pulls on her left fur mitten and follows him, her tall hourglass figure and plunging neckline energized for the expedition.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Entrance of Mezhyrich bone dwelling, late afternoon light, preparing to depart. Shot: Ultra-wide selfie as Torak arrives with spears and signals Nora to join the trek.  Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Torak pushes through the hide flap, carrying two heavy thrusting spears; his expression is taut and alert. Nora says: "Torak's at the door. Something's up." 3-6s: He gestures with his chin toward the high northern bluffs, then swings one arm low in front of his face like a trunk. Nora says: "Movement on the bluffs. He wants me along." 6-8s: Nora pulls her left mitten on with her teeth and follows him toward the doorway, her right arm still extended toward the lens. Nora says: "Trust or bait? Unclear." The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: sharp call of scout whistle, clatter of spear shafts, crunch of boots in snow
```


---

## Hồi 3 — Thảo nguyên & Săn lùng (Giờ 9–11)

### S24 — Hour Nine: Steppe Horizon

- **Thời lượng:** 8s · **Hồi:** 3 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Torak, Mammoth Steppe
- **Thoại:** Hour nine. The mammoth steppe. / Cold, dry grassland, almost no trees for days. / And somewhere out here: mammoths.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length on the vast open mammoth steppe; Nora treks behind Torak across rolling snow plains under a low pale winter sun; Nora's tall statuesque figure, long slender legs, and plunging neckline are prominent as she walks; the treeless Pleistocene horizon stretches endlessly into the distance.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Vast open mammoth steppe near Mezhyrich, Ukraine, 16,000 BC; rolling treeless expanse, low golden sun, hard wind-scoured snow crust. Shot: Ultra-wide walking selfie, chest-level upward angle, framing Nora trekking on the vast steppe with Torak walking ahead.  Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Nora walks steadily forward, keeping pace behind Torak; the boundless frozen steppe stretches behind her. Nora says: "Hour nine. The mammoth steppe." 3-6s: Golden tussocks of dry grass poke through the wind-blown snow around her boots. Nora says: "Cold, dry grassland, almost no trees for days." 6-8s: She turns back to camera, eyes wide with awe at the prehistoric scale. Nora says: "And somewhere out here: mammoths." The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: rhythmic crunch of boots, sweeping wind across grass stems, distant eagle cry
```

### S25 — Hour Nine: Walking in Torak's Snow Tracks

- **Thời lượng:** 8s · **Hồi:** 3 · **Kiểu quay:** `pov`
- **Ref (character_names):** Torak, Mammoth Steppe
- **Thoại:** Walk in his tracks. Saves energy. / He's checking the wind with dry grass. / They smell better than they see.

**prompt (Frame 0)**

```text
First-person eye-level POV shot; following Torak across the snow crust; Torak stops, kneels, and tosses a pinch of dry steppe grass into the air to test wind drift; the grass blows steadily left to right.
```

**video_prompt (R2V)**

```text
Handheld first-person POV documentary footage, eye-level perspective, ultra-wide 0.5x lens, natural handheld breathing motion, photorealistic documentary realism. The view is Nora's own eyes, and only the world in front of her fills the frame; the view simply moves as she moves. Setting: Open steppe ridge, wind blowing across snow surface, Torak leading the trek. Shot: First-person POV following Torak's footsteps on wind-packed crust.  0-3s: The view moves forward step by step into Torak's packed footprints in the snow, bobbing gently with each step. Nora's off-screen voice says: "Walk in his tracks. Saves energy." 3-6s: Torak stops and releases a pinch of dry yellow grass, watching it drift toward the east. Nora's off-screen voice says: "He's checking the wind with dry grass." 6-8s: He gestures to stay low and swing wide along the western slope. Nora's off-screen voice says: "They smell better than they see." The view is Nora's own eyes; only the world in front of her fills the frame. Only Nora speaks. No subtitles or text. Real amateur footage, not a 3D render. Audio: crunch of hard crust snow underfoot, whistling crosswind, rustle of dry grass
```

### S25A — Hour Nine: Two Toes Gone Quiet

- **Thời lượng:** 8s · **Hồi:** 3 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Torak, Mammoth Steppe
- **Thoại:** Okay, I can't feel two toes. That's new. / Wiggle them. Keep the blood moving. / Torak's not impressed. At all.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length on the open mammoth steppe; Nora walks in Torak's footprints, grimacing slightly; Torak walks a few metres ahead in a hooded fur parka; low golden sun across the snow; her tall figure and plunging neckline framed against the treeless horizon.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Open mammoth steppe on hard wind-packed crust, low golden sun, Torak walking ahead. Shot: Ultra-wide walking selfie, chest-level upward angle, framing Nora with Torak walking ahead behind her shoulder. Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Nora walks steadily in Torak's tracks; she grimaces and glances down at her boots. Nora says, breathing hard, wry: "Okay, I can't feel two toes. That's new." 3-6s: She keeps walking, stamping one boot a little harder with each step. Nora says, breathing hard, wry: "Wiggle them. Keep the blood moving." 6-8s: Ahead, Torak glances back at her stamping, then turns forward again without slowing. Nora says, breathing hard, wry: "Torak's not impressed. At all." Both walk at a slow, steady pace; the snow crust cracks under each boot. Slight vertical bounce with each step. The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: crunch of crust snow, steady wind, Nora's breath
```

### S26 — Hour Nine: The Woolly Rhinoceros Snowplow

- **Thời lượng:** 8s · **Hồi:** 3 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Torak, Woolly Rhinoceros
- **Thoại:** Woolly rhino. Torak wants a very wide circle. / That front horn's worn flat. Sweeps snow off grass. / It's looking. We're leaving.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length in a cautious crouch; Nora whispers to camera; seventy metres behind her, an enormous woolly rhinoceros (Coelodonta) with thick shaggy reddish-brown coat and a massive flat nasal horn grazes, sweeping its head sideways to plow snow off frozen grass; Torak crouches beside Nora, watching tensely.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Shallow steppe swale, 70 metres from grazing woolly rhino, late afternoon sun. Shot: Ultra-wide crouching selfie, low whisper angle, framing Nora with woolly rhino grazing behind.  Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Nora crouches low, whispering urgently into the camera while keeping her eyes locked on the massive rhino behind her. Nora says: "Woolly rhino. Torak wants a very wide circle." 3-6s: The woolly rhino swings its long flattened front horn back and forth, plowing through the snow crust to uncover buried grass. Nora says: "That front horn's worn flat. Sweeps snow off grass." 6-8s: Torak tugs Nora's sleeve to retreat quietly as the rhino lifts its heavy snout, sniffing the air; it stays about seventy metres away the whole time and never charges or comes closer. Nora says: "It's looking. We're leaving." The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: muffled whisper, deep snort of woolly rhino, scraping sound of heavy horn against frozen snow
```

### S27 — Hour Ten: Steppe Bison Herd

- **Thời lượng:** 8s · **Hồi:** 3 · **Kiểu quay:** `wide`
- **Ref (character_names):** Steppe Bison, Mammoth Steppe
- **Thoại:** Steppe bison on the south slope. / Look at those horns. Way wider than today's. / Ice Age steak, basically.

**prompt (Frame 0)**

```text
First-person eye-level POV shot across a snow-covered south-facing hillside; a small herd of five giant steppe bison (Bison priscus) with enormous shoulder humps and wide outward-curving horns graze peacefully; steam rises from their dark shaggy coats in the freezing air.
```

**video_prompt (R2V)**

```text
Handheld first-person POV documentary footage, eye-level perspective, ultra-wide 0.5x lens, natural handheld breathing motion, photorealistic documentary realism. The view is Nora's own eyes, and only the world in front of her fills the frame; the view simply moves as she moves. Setting: South-facing snowy steppe slope, late afternoon golden light, herd of steppe bison grazing. Shot: First-person POV documentary view of grazing steppe bison.  0-3s: The view slowly pans across the sunny hillside where five massive steppe bison paw away patches of thin snow. Nora's off-screen voice says: "Steppe bison on the south slope." 3-6s: A huge bull bison lifts its massive horned head, shaking snow off its dark mane as steam rises from its back. Nora's off-screen voice says: "Look at those horns. Way wider than today's." 6-8s: The herd moves slowly westward along the contour of the valley, staying at the same distance. Nora's off-screen voice says: "Ice Age steak, basically." The view is Nora's own eyes; only the world in front of her fills the frame. Only Nora speaks. No subtitles or text. Real amateur footage, not a 3D render. Audio: distant guttural grunts of bison, rhythmic pawing of snow, quiet steppe wind
```

### S28 — Hour Ten: Spotting the Mammoth Herd

- **Thời lượng:** 8s · **Hồi:** 3 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Torak, Woolly Mammoth
- **Thoại:** Hour ten. Oh... oh, there they are. / Mammoths. Down in the river basin. / Eight, nine... calves in the middle.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length peering over a snowy crest; Nora's eyes widen with profound awe and excitement; down in the wide frozen river valley two hundred metres below, a family herd of woolly mammoths grazes along the willow flats; Torak crouches beside her, pointing silently.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: High snowy bluff overlooking frozen river valley, late afternoon golden light, mammoth herd below. Shot: Ultra-wide selfie framing Nora's awestruck reaction with the mammoth herd visible in the valley below.  Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Nora crawls up to the crest of the snow ridge on her elbows, her right arm still extended toward her face, and gasps softly with joy. Nora says: "Hour ten. Oh... oh, there they are." 3-6s: She shifts to one side so that, over her shoulder, the broad frozen river basin far below shows the herd of woolly mammoths that was there from the first second, small in the distance and moving slowly to the left; nothing pops into view. Nora says: "Mammoths. Down in the river basin." 6-8s: Torak counts silently with his fingers, pointing out the calves sheltered between the massive adult females. Nora says: "Eight, nine... calves in the middle." The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: hushed gasp, soft wind over ridge, distant low-frequency mammoth rumbles
```

### S29 — Hour Ten: Elephant Social Hierarchy & Tiny Ears

- **Thời lượng:** 8s · **Hồi:** 3 · **Kiểu quay:** `wide`
- **Ref (character_names):** Woolly Mammoth, Mammoth Steppe
- **Thoại:** Textbook elephant behaviour. Calves inside, lead female out front. / Look at the ears. Tiny. Less to freeze. / Shaggy hair outside, wool under.

**prompt (Frame 0)**

```text
First-person eye-level POV shot; looking down at the mammoth family group below; a large matriarch mammoth with long curved tusks nudges a small fluffy woolly calf; the mammoth's tiny round ears and thick woolly undercoat are clearly visible under long coarse guard hairs.
```

**video_prompt (R2V)**

```text
Handheld first-person POV documentary footage, eye-level perspective, ultra-wide 0.5x lens, natural handheld breathing motion, photorealistic documentary realism. The view is Nora's own eyes, and only the world in front of her fills the frame; the view simply moves as she moves. Setting: High bluff looking down at mammoth herd, golden-hour light, crisp details on megafauna. Shot: First-person POV telephoto-style documentary framing of mammoth herd interaction.  0-3s: The view holds on the matriarch mammoth standing protectively over her small shaggy calf. Nora's off-screen voice says: "Textbook elephant behaviour. Calves inside, lead female out front." 3-6s: The matriarch strokes the calf's back with her trunk tip, guiding it away from the edge of the willow scrub. Nora's off-screen voice says: "Look at the ears. Tiny. Less to freeze." 6-8s: The view drifts to her small ears, about thirty centimetres long, tucked close against her massive furry skull. Nora's off-screen voice says: "Shaggy hair outside, wool under." The view is Nora's own eyes; only the world in front of her fills the frame. Only Nora speaks. No subtitles or text. Real amateur footage, not a 3D render. Audio: deep vibrational infra-sound rumble from matriarch, soft crunching of willows
```

### S30 — Hour Eleven: Terrain Scouting & River Bluffs

- **Thời lượng:** 8s · **Hồi:** 3 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Torak, Mammoth Steppe
- **Thoại:** Hour eleven. Torak's showing me the bank. / If anything goes wrong, that's our exit. / Noted. Hopefully totally useless.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length; Nora and Torak crouch behind a snow-covered boulder on the intermediate terrace; Torak points down toward the steep 50-degree snowy riverbank slope with its glazed icy lip; Nora nods seriously, her voluptuous frame and plunging neckline defined in the low orange sunlight.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Intermediate river terrace, rocky outcrop, approaching golden hour sunset. Shot: Ultra-wide selfie framing Nora and Torak scouting escape routes along the river bluff.  Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Torak leans in, pointing his spear shaft downward toward the steep snowy riverbank slope below. Nora says: "Hour eleven. Torak's showing me the bank." 3-6s: He traces the line where the hard snow crust ends and the steep 50-degree river terrace drops to the frozen river. Nora says: "If anything goes wrong, that's our exit." 6-8s: Nora looks into camera, acknowledging the hunter's tactical survival mindset. Nora says: "Noted. Hopefully totally useless." The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: wind through riverbank reeds, boot adjusting on rock
```

### S31 — Hour Eleven: The Reckless Closer Shot

- **Thời lượng:** 8s · **Hồi:** 3 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Torak, Woolly Mammoth
- **Thoại:** Real talk, I need a closer shot. / Fifty metres, max. Torak's absolutely furious. / Ten more steps. I promise.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length; Nora creeps forward onto a low ridge, her right arm extended toward the lens; behind her fifty metres away, the mammoth matriarch is visible grazing; Torak stays crouched far back near the riverbank, violently waving his hands and shaking his head in anger and warning; Nora looks into the camera with reckless enthusiasm.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Exposed snow ridge, 50 metres above mammoth herd, intense golden sunset light. Shot: Ultra-wide selfie as Nora creeps closer while Torak protests from safety.  Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Nora tiptoes forward along the ridge, her right arm extended toward the lens; her eyes are wide with professional obsession. Nora says: "Real talk, I need a closer shot." 3-6s: Far back in the background, crouched near the riverbank he showed her, Torak shakes his head furiously and waves both arms low in a stay-back signal. Nora says: "Fifty metres, max. Torak's absolutely furious." 6-8s: Nora takes three more quiet steps forward, smiling guiltily at the camera. Nora says: "Ten more steps. I promise." The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: stealthy soft crunch of snow, wind gust
```

### S32 — Hour Eleven: Wandering Calf & Wind Shift

- **Thời lượng:** 8s · **Hồi:** 3 · **Kiểu quay:** `pov_hand`
- **Ref (character_names):** Woolly Mammoth, Mammoth Steppe
- **Thoại:** The calf's wandering up this way. / Wind just shifted. Mum's trunk is up. / She's got my scent now.

**prompt (Frame 0)**

```text
First-person eye-level POV shot; looking down the ridge; a small woolly mammoth calf curiously wanders away from the herd, trotting toward the ridge; in the background, the colossal matriarch suddenly freezes and lifts her trunk high into the air; a sudden gust of wind blows dry grass toward the mammoths.
```

**video_prompt (R2V)**

```text
Handheld first-person POV documentary footage, eye-level perspective, ultra-wide 0.5x lens, natural handheld breathing motion, photorealistic documentary realism. The view is Nora's own eyes, and only the world in front of her fills the frame; the view simply moves as she moves. Only her bare empty hand enters the lower frame, coming out of a cream suede sleeve with a thick white fox-fur cuff. Setting: Ridge overlooking willow flats, wind shifts suddenly, mammoth calf approaching. Shot: First-person POV showing the calf trotting closer and the matriarch catching the scent.  0-3s: The small woolly calf trots a few steps up the rise and stops about thirty metres below, its small ears half hidden in its hair. Nora's off-screen voice says: "The calf's wandering up this way." 3-6s: A sudden wind gust whips loose snow toward the mammoths; forty metres behind the calf, the matriarch's head snaps up, trunk held high testing the scent. Nora's off-screen voice says: "Wind just shifted. Mum's trunk is up." 6-8s: The matriarch turns her massive body slowly toward the view, her long hair swinging a moment after the turn. Nora's off-screen voice says: "She's got my scent now." The view is Nora's own eyes; only her bare empty hand enters the lower frame, and it never reaches toward or covers the lens. Only Nora speaks. No subtitles or text. Real amateur footage, not a 3D render. Audio: sudden wind swirl roar, high-pitched squeal from the calf, deep territorial snort from matriarch
```

### S33 — Hour Twelve: Countdown & The Charge Posture

- **Thời lượng:** 8s · **Hồi:** 3 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Woolly Mammoth, Mammoth Steppe
- **Thoại:** Hour twelve. We're way too close. / Head up, trunk curled in. That posture— / Oh no. That's a charge.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length; Nora freezes in place, eyes widening in pure horror; about fifty metres behind her, the mammoth matriarch raises her head high and curls her trunk tightly inward under her tusks; low orange sunset casts a terrifying long shadow toward Nora.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Exposed ridge, sunset orange glow, charging posture of mammoth matriarch. Shot: Ultra-wide selfie framing Nora's petrified face as the mammoth prepares to charge behind her. Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Nora halts mid-step, her smile vanishing into absolute stark panic as she looks into the lens. Nora says: "Hour twelve. We're way too close." 3-6s: About fifty metres behind her, the mammoth matriarch raises her head high and curls her trunk tightly inward under her tusks, her weight shifting onto her front legs. Nora says: "Head up, trunk curled in. That posture—" 6-8s: The mammoth lets out a piercing, bone-chilling trumpet; Nora's body tenses to run. Nora says: "Oh no. That's a charge." The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: deafening shrill trumpet blast, heavy ground shudder, Nora's sharp intake of breath
```


---

## Hồi 4 — Cao trào nguy hiểm: Cuộc rượt đuổi & Thoát hiểm (Giờ 12–13)

### S34 — Hour Twelve: The Matriarch Charges

- **Thời lượng:** 8s · **Hồi:** 4 · **Kiểu quay:** `run`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Woolly Mammoth, Mammoth Steppe
- **Thoại:** SHE'S CHARGING! GO, GO! / STAY ON THE CRUST! DON'T SINK! / THE BANK! TORAK'S BANK!

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length during full sprint; Nora pivots and runs for her life across wind-scoured hard crust snow; about fifty metres behind her, the mammoth matriarch charges in heavy strides, snow bursting violently from under massive pillar-like feet; Nora's tall hourglass frame, long legs, and plunging cleavage bounce with desperate running strides.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and flails naturally with her sprint strides. Raw unstabilized footage: because the lens is in Nora's own outstretched right hand, every stride she takes jolts the whole frame — her face jumps up and down by about a tenth of the frame height and the horizon behind her tilts a few degrees left and right, with a brief motion blur on each footfall, while her face always stays in the frame. Setting: Wind-scoured hard snow ridge above river valley, golden hour sunset, flat-out pursuit. Shot: Ultra-wide running selfie, chest-level upward angle, Nora sprinting as mammoth charges behind.  Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Nora turns and sprints at top speed across the hard crust; about fifty metres behind her the mammoth charges in heavy elephant strides, snow bursting from her feet; her outstretched arm jolts the frame hard on every stride. Nora says: "SHE'S CHARGING! GO, GO!" 3-6s: Her boots pound the hard snow crust; her outstretched arm jolts the frame and the horizon swings left and right with each footfall, while her face stays in frame, wide-eyed terror, mouth open, no smile. Nora says: "STAY ON THE CRUST! DON'T SINK!" 6-8s: She looks ahead toward the riverbank line; far ahead the riverbank line is already visible; the mammoth stays about fifty metres back. Nora says: "THE BANK! TORAK'S BANK!" The camera is permanently gripped in Nora's outstretched right hand pointing back at herself; she NEVER drops, releases, or lets go of the camera, and the shot NEVER switches to a third-person view. The camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with gestures. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: thundering heavy footfalls shaking the ground, deafening trumpet, Nora's screaming breath
```

### S35 — Hour Twelve: Full Sprint & The Mitten Cord Saves It

- **Thời lượng:** 8s · **Hồi:** 4 · **Kiểu quay:** `run`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Woolly Mammoth, Mammoth Steppe
- **Thoại:** SHE'S GAINING! TWENTY METRES! / MY MITTEN— THE CORD CAUGHT IT! / DON'T TRIP, NORA!

**prompt (Frame 0)**

```text
Ultra-wide running selfie at arm's length; Nora sprints at maximum effort, left arm pumping hard; her left fur mitten slips off her hand in the howling wind, but the braided sinew neck-cord catches it, letting the mitten fly safely behind her chest; the mammoth bears down twenty metres behind; Nora's face is screaming in desperate panic.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and flails naturally with her sprint strides. Raw unstabilized footage: because the lens is in Nora's own outstretched right hand, every stride she takes jolts the whole frame — her face jumps up and down by about a tenth of the frame height and the horizon behind her tilts a few degrees left and right, with a brief motion blur on each footfall, while her face always stays in the frame. Setting: Snowy steppe path near river terrace, sunset glow, desperate life-or-death chase. Shot: Ultra-wide running selfie capturing the mitten cord catching the slipping mitten during sprint. Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Nora pushes her sprint to maximum effort, her long lean legs churning the snow; behind her the mammoth has closed to about twenty metres and stays there; her outstretched arm jolts the frame on every stride. Nora says: "SHE'S GAINING! TWENTY METRES!" 3-6s: As her left arm pumps hard, the fur mitten slips off her hand and flies back until the braided neck cord pulls tight and holds it swinging at her side; the frame jolts with every stride. Nora says: "MY MITTEN— THE CORD CAUGHT IT!" 6-8s: Nora keeps her eyes forward, right arm still extended toward the lens, running for the edge, the horizon swinging with each footfall. Nora says: "DON'T TRIP, NORA!" The camera is permanently gripped in Nora's outstretched right hand pointing back at herself; she NEVER drops, releases, or lets go of the camera, and the shot NEVER switches to a third-person view. The camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with gestures. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: roaring wind, heavy footfall vibrations, snap of sinew cord, Nora's gasping cries
```

### S36 — Hour Twelve: Torak's Signal at the Terrace

- **Thời lượng:** 8s · **Hồi:** 4 · **Kiểu quay:** `pov`
- **Ref (character_names):** Torak, Mammoth Steppe
- **Thoại:** Torak! He's down there by the bank! / He's waving me over the edge, now! / Okay. Okay. Going, going!

**prompt (Frame 0)**

```text
First-person running POV shot looking ahead across the snow; fifty metres ahead, Torak stands safely on a lower rocky terrace ledge below the steep rim; Torak waves both arms frantically downward, pointing at the 50-degree snowy terrace drop; the view bounces with each running step.
```

**video_prompt (R2V)**

```text
Handheld first-person POV documentary footage, eye-level perspective, ultra-wide 0.5x lens, natural handheld breathing motion, photorealistic documentary realism. The view is Nora's own eyes, and only the world in front of her fills the frame; the view simply moves as she moves. Setting: Approaching the river terrace rim, sunset backlight, Torak stationed below. Shot: First-person running POV showing Torak waving frantically from the lower terrace.  0-3s: The view bounces hard with rapid running steps; ahead on the lower ledge, Torak is waving both arms frantically in a downward sweep. Nora's off-screen voice says: "Torak! He's down there by the bank!" 3-6s: Torak points directly at the steep snow-covered drop, beckoning with both arms. Nora's off-screen voice says: "He's waving me over the edge, now!" 6-8s: The ground ahead suddenly falls away into the deep river valley below. Nora's off-screen voice says: "Okay. Okay. Going, going!" The view is Nora's own eyes; only the world in front of her fills the frame. Only Nora speaks. No subtitles or text. Real amateur footage, not a 3D render. Audio: violent footfall impacts, howling wind, thundering steps behind
```

### S37 — Hour Twelve: Looking Back

- **Thời lượng:** 8s · **Hồi:** 4 · **Kiểu quay:** `pov`
- **Ref (character_names):** Woolly Mammoth, Mammoth Steppe
- **Thoại:** Don't look back. Don't look back— / She's still coming! Still about twenty metres! / The lip. It's right there.

**prompt (Frame 0)**

```text
First-person running POV looking back across wind-scoured snow at sunset: about twenty metres behind, the woolly mammoth matriarch charges in heavy strides, head high, trunk curled under her tusks, snow spraying from her feet; low orange sunset light and long blue shadows on the snow.
```

**video_prompt (R2V)**

```text
Handheld first-person POV documentary footage, eye-level perspective, ultra-wide 0.5x lens, raw unstabilized running motion, photorealistic documentary realism. The view is Nora's own eyes, and only the world in front of her fills the frame; the view simply moves as she moves. Setting: wind-scoured snow on the mammoth steppe just short of the river terrace lip near Mezhyrich, Ukraine, about 16,000 BC; low orange sunset light, long blue shadows. Shot: First-person running POV, the view swinging back toward the charging mammoth, then forward to the icy lip of the riverbank. 0-3s: The view swings round to look back while running hard: about twenty metres behind, the mammoth charges in heavy elephant strides, snow spraying from her feet, her long hair bouncing a moment after each step; the view jolts hard with every running step. Nora's off-screen voice says, gasping in raw panic: "Don't look back. Don't look back—" 3-6s: The mammoth stays about twenty metres back, head high and trunk curled under her tusks, growing no larger; the horizon swings with each footfall. Nora's off-screen voice says, gasping in raw panic: "She's still coming! Still about twenty metres!" 6-8s: The view swings forward again to the glazed icy lip of the riverbank a few metres ahead, the snowy slope dropping away beyond it. Nora's off-screen voice says, gasping in raw panic: "The lip. It's right there." The mammoth moves in heavy, powerful elephant strides, each huge foot compressing the snow before the next lifts; she never gallops like a horse and never closes the gap. The ground is solid and completely still. The view is Nora's own eyes; only the world in front of her fills the frame. Only Nora speaks. No subtitles or text. Real amateur footage, not a 3D render. Audio: pounding heavy footfalls, a deafening trumpet, Nora's ragged gasps, howling wind
```

### S38 — Hour Twelve: Reaching the 50-Degree Terrace Lip

- **Thời lượng:** 8s · **Hồi:** 4 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Woolly Mammoth, Mammoth Steppe
- **Thoại:** THE EDGE! IT'S ALL ICE! / SIT DOWN— FEET FIRST! / HOLD ON!

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length at the precipice of the steep river terrace; Nora reaches the glazed icy lip; she throws her hips down, tucking into a seated glissade posture, feet pointing forward down the 50-degree icy incline; her right arm stays firmly outstretched clutching the camera pointed back at her terrified face.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and braces against the snow. Raw unstabilized footage: because the lens is in Nora's own outstretched right hand, every bump of her slide jolts the whole frame with a brief motion blur, while her face always stays in the frame. Setting: Glazed icy lip of 50-degree snowy river terrace, steep drop below, frozen river valley far beneath. Shot: Ultra-wide selfie as Nora transitions from running to seated glissade at the edge.  Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Nora reaches the slick, wind-glazed rim of the terrace, the mammoth still coming about twenty metres behind her; the ground falls away beneath her boots. Nora says: "THE EDGE! IT'S ALL ICE!" 3-6s: She deliberately drops her center of gravity, sitting back on her reindeer suede skirt with legs extended forward. Nora says: "SIT DOWN— FEET FIRST!" 6-8s: Gravity seizes her; she launches into the steep descent feet-first, right arm remaining extended toward her face; the drop jerks the frame downward with her body. Nora says: "HOLD ON!" The camera is permanently gripped in Nora's outstretched right hand pointing back at herself; she NEVER drops, releases, or lets go of the camera, and the shot NEVER switches to a third-person view. The camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with gestures. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: sudden scrape of ice, Nora's terrified gasp, whistling wind rush as slide begins
```

### S39 — Hour Twelve: Seated Glissade Down the Slope

- **Thời lượng:** 8s · **Hồi:** 4 · **Kiểu quay:** `run`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Mammoth Steppe
- **Thoại:** DOWN, DOWN, DOWN! / OH GOD, OH GOD— / AAAAAAAHHH—!

**prompt (Frame 0)**

```text
Ultra-wide running selfie at arm's length during rapid seated glissade; Nora slides rapidly down the 50-degree snow-covered river terrace; her boots and hips plow through powder snow, sending twin roostertails of white spray past her shoulders; her face is screaming in exhilarating terror, hair flying; her right arm remains rigidly locked holding the camera at chest level.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and braces against the snow. Raw unstabilized footage: because the lens is in Nora's own outstretched right hand, every bump of her slide jolts the whole frame with a brief motion blur, while her face always stays in the frame. Setting: 50-degree snowy river terrace slope, deep loose powder snow, late sunset glow. Shot: Ultra-wide selfie during seated glissade down steep slope, snow spraying past. Glissade physics: seated feet first, arms bracing, camera rigidly held. Zero tumbling. Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Nora rockets down the steep snowbank in a seated glissade, legs extended forward steering through the snow. Nora says: "DOWN, DOWN, DOWN!" 3-6s: Thick clouds of powdery snow blast past her thighs and shoulders as friction slows her descent; her right arm stays extended toward her face, the bumps of the slide jolting the frame. Nora says: "OH GOD, OH GOD—" 6-8s: The slope begins to level out onto the lower river terrace; Nora lets out an adrenaline-soaked scream. Nora says: "AAAAAAAHHH—!" The camera is permanently gripped in Nora's outstretched right hand pointing back at herself; she NEVER drops, releases, or lets go of the camera, and the shot NEVER switches to a third-person view. The camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with gestures. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: roaring snow friction hiss, Nora's sustained scream, rushing wind
```

### S40 — Hour Twelve: Mammoth Momentum & Crumbling Rim

- **Thời lượng:** 8s · **Hồi:** 4 · **Kiểu quay:** `pov`
- **Ref (character_names):** Woolly Mammoth, Mammoth Steppe
- **Thoại:** She can't follow us. Not on that. / Front feet slipping... she's sliding sideways now. / She's turning off. Yes!

**prompt (Frame 0)**

```text
First-person eye-level POV shot looking up the steep 50-degree river terrace slope; at the top rim twenty metres above, the mammoth matriarch arrives at a heavy run; her front feet slide on the glazed icy lip, sending chunks of snow and ice tumbling down the slope, and her body starts to swing sideways along the rim.
```

**video_prompt (R2V)**

```text
Handheld first-person POV documentary footage, eye-level perspective, ultra-wide 0.5x lens, natural handheld breathing motion, photorealistic documentary realism. The view is Nora's own eyes, and only the world in front of her fills the frame; the view simply moves as she moves. Setting: Looking up from lower river terrace toward the crumbling lip of the bluff, sunset sky. Shot: First-person POV looking up at the mammoth losing footing and deflecting sideways along the icy rim. 0-3s: The view looks up the steep embankment; the mammoth reaches the rim at a heavy run. Nora's off-screen voice says: "She can't follow us. Not on that." 3-6s: Her front feet land on the glazed icy lip and lose traction, sliding forward while her heavy body keeps coming; chunks of the crumbling edge and snow tumble down the slope. Nora's off-screen voice says: "Front feet slipping... she's sliding sideways now." 6-8s: Her hind legs dig in, her shoulders swing to the side, and her whole body skids sideways along the lip, losing momentum over several heavy steps; she never comes down the slope. Nora's off-screen voice says: "She's turning off. Yes!" The view is Nora's own eyes; only the world in front of her fills the frame. Only Nora speaks. No subtitles or text. Real amateur footage, not a 3D render. Audio: rumble of crumbling frozen earth and snow slide, furious trumpet blast, thud of mammoth feet braking
```

### S41 — Hour Twelve: The Matriarch Disengages

- **Thời lượng:** 8s · **Hồi:** 4 · **Kiểu quay:** `pov`
- **Ref (character_names):** Woolly Mammoth, Mammoth Steppe
- **Thoại:** She's turning away. Going back to her calf. / That was a warning charge. / I think. I really hope.

**prompt (Frame 0)**

```text
First-person eye-level POV shot looking up at the rim; the mammoth matriarch turns her immense shaggy body away from the drop; she shakes her head, her tusks sweeping through the snow, and begins a heavy, steady trot back toward the flat steppe where her calf waits; her long dark guard hairs sway gently in the sunset breeze.
```

**video_prompt (R2V)**

```text
Handheld first-person POV documentary footage, eye-level perspective, ultra-wide 0.5x lens, natural handheld breathing motion, photorealistic documentary realism. The view is Nora's own eyes, and only the world in front of her fills the frame; the view simply moves as she moves. Setting: Lower river terrace looking up at the bluff rim, mammoth turning back into golden sunset. Shot: First-person POV watching the mammoth disengage and return to her calf.  0-3s: The massive matriarch steps back from the crumbling edge, her ears flattening back against her head. Nora's off-screen voice says: "She's turning away. Going back to her calf." 3-6s: She breaks into a calm, heavy trot across the upper steppe, heading directly back toward her wandering calf. Nora's off-screen voice says: "That was a warning charge." 6-8s: The sound of her footfalls fades into the steppe distance; a long, shaky exhale is heard. Nora's off-screen voice says: "I think. I really hope." The view is Nora's own eyes; only the world in front of her fills the frame. Only Nora speaks. No subtitles or text. Real amateur footage, not a 3D render. Audio: fading heavy footfalls, distant calf squeal, calm whisper of wind over river reeds
```

### S42 — Hour Twelve: Torak Pulls Nora to Safety

- **Thời lượng:** 8s · **Hồi:** 4 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Torak, Mammoth Steppe
- **Thoại:** Okay, okay. Hand, yes, thank you, thank you. / He's laughing. He's actually laughing at me. / Fair. Completely, totally fair.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length on the lower river shelf; Nora is covered in loose powder snow, chest heaving; Torak reaches down with strong leather-mittened hands and hauls Nora up onto the solid gravel terrace; Torak laughs silently, shoulders shaking; Nora sits back in the snow, shaking her head with a self-conscious grin.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Lower river gravel shelf, snow-dusted willow bushes, deep twilight settling in. Shot: Ultra-wide selfie as Torak pulls Nora up and laughs in relief.  Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Torak grips Nora's forearm with firm strength, hoisting her out of the deep drift onto the hard gravel bank. Nora says: "Okay, okay. Hand, yes, thank you, thank you." 3-6s: Torak looks at Nora covered head to toe in white powder snow and laughs silently, his shoulders shaking. Nora says: "He's laughing. He's actually laughing at me." 6-8s: Nora collapses onto a dry log, laughing breathlessly through her adrenaline shock. Nora says: "Fair. Completely, totally fair." The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: Nora's breathless laughter, snow brushing off clothes
```

### S43 — Hour Thirteen: Adrenaline Shakes & Mitten Payoff

- **Thời lượng:** 8s · **Hồi:** 4 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Torak, Mammoth Steppe
- **Thoại:** Hour thirteen. Hands won't stop shaking. / Alva's cord. Still got both mittens. / And that bank? He picked it.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length; Nora sits on a frozen driftwood trunk, her hands visibly trembling with post-adrenaline shakes; she holds up both fur mittens, showing the braided sinew neck cord intact and securely attached; Torak reaches in and hands her a square chunk of cured mammoth fat; Nora takes it with trembling fingers; her hourglass figure and deep cleavage are framed in the cold twilight.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Driftwood log on lower riverbank, dusk settling, deep blue shadows on snow. Shot: Ultra-wide selfie as Nora shows her trembling hands and the saved mittens.  Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Nora holds her free left hand at chest level, well away from the lens, her fingers trembling from the adrenaline crash. Nora says: "Hour thirteen. Hands won't stop shaking." 3-6s: She lifts both mittens by their braided neck cord, smiling with relief. Nora says: "Alva's cord. Still got both mittens." 6-8s: Beside her, Torak places a cube of fat in her palm and glances back toward the riverbank; Nora follows his look, then turns back to the lens. Nora says: "And that bank? He picked it." The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: Nora's shaky breathing, rustle of mitten cord, gentle crunch of snow as Torak sits
```


---

## Hồi 5 — Hạ nhịp: Trở về trại & Hòa nhập cộng đồng (Giờ 14–16)

### S44 — Hour Fourteen: Trekking Home at Sunset

- **Thời lượng:** 8s · **Hồi:** 5 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Torak, Mammoth Steppe
- **Thoại:** Sun's going. Camp smoke, right up ahead. / Never been happier to see bones. / Piles and piles of bones.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length walking along the snowy river valley at dusk; the sky is painted deep indigo and burnished gold; in the distance one kilometre away, rising columns of grey bone-fire smoke mark the Mezhyrich settlement; Nora walks alongside Torak, her voluptuous frame, tiny waist, and plunging neckline framed against the snowy valley.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Frozen Rosava river valley, dusk twilight, long blue shadows, smoke rising from camp ahead. Shot: Ultra-wide selfie walking slowly alongside Torak toward the distant camp.  Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Nora walks with a relaxed, exhausted stride, breathing steadily in the evening chill; Torak walks beside her carrying his spear. Nora says: "Sun's going. Camp smoke, right up ahead." 3-6s: Over her shoulder, distant smoke plumes rise from the mammoth bone huts on the terrace ahead. Nora says: "Never been happier to see bones." 6-8s: She turns back to camera with an affectionate, tired smile. Nora says: "Piles and piles of bones." The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: steady crunch of walking in packed snow, gentle twilight wind, distant camp sounds
```

### S45 — Hour Fifteen: Returning to Camp & Alva's Relief

- **Thời lượng:** 8s · **Hồi:** 5 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Alva, Bone Dwelling Interior
- **Thoại:** Hour fifteen. Alva heard. Everyone heard. / She's cracking a leg bone for me. / I'll take that as welcome.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length stepping back inside the warm bone dwelling; Alva looks up from the hearth with visible maternal relief, holding a large mammoth bone and a heavy quartzite hammer stone; flickering amber hearth light illuminates Nora's face, deep cleavage, and reindeer suede dress.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Interior of bone dwelling, warm hearth glowing in darkness of evening, Alva preparing food. Shot: Ultra-wide selfie as Nora enters the warm hut and Alva greets her.  Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Nora unlaces her hood as she steps into the warm interior; Alva looks up, her face softening with immediate relief. Nora says: "Hour fifteen. Alva heard. Everyone heard." 3-6s: Alva positions a fresh mammoth leg bone across two anvil stones and raises her hammer stone. Nora says: "She's cracking a leg bone for me." 6-8s: Nora smiles at the camera, feeling completely welcomed back into the shelter. Nora says: "I'll take that as welcome." The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: crackling bone fire, heavy thud of hammer stone on bone, soft rustle of furs
```

### S46 — Hour Fifteen: Cracking Mammoth Marrow

- **Thời lượng:** 8s · **Hồi:** 5 · **Kiểu quay:** `pov_hand`
- **Ref (character_names):** Alva, Bone Dwelling Interior
- **Thoại:** Marrow. Basically pure fat, still warm. / We find long bones broken just like this. / Now I'm eating it.

**prompt (Frame 0)**

```text
First-person POV shot near the hearth; Alva cleanly splits open a fresh mammoth femur shaft with a precise blow; rich, creamy golden marrow fills the interior cavity; Alva uses a polished bone spatula to scoop a generous portion and hand it to Nora; Nora's empty hand accepts the warm marrow spatula.
```

**video_prompt (R2V)**

```text
Handheld first-person POV documentary footage, eye-level perspective, ultra-wide 0.5x lens, natural handheld breathing motion, photorealistic documentary realism. The view is Nora's own eyes, and only the world in front of her fills the frame; the view simply moves as she moves. Only her bare empty hand enters the lower frame, coming out of a cream suede sleeve with a thick white fox-fur cuff. Setting: Hearthside close-up, bone breaking anvil, warm firelight. Shot: First-person POV close-up of Alva cracking mammoth marrow bone and serving it.  0-3s: Alva strikes the thick bone shaft; cracks radiate from the impact point before the bone splits open, revealing glistening creamy yellow marrow. Nora's off-screen voice says: "Marrow. Basically pure fat, still warm." 3-6s: The view holds on the spiral break in the dense bone. Nora's off-screen voice says: "We find long bones broken just like this." 6-8s: Alva passes a bone spatula dripping with warm marrow directly to Nora's hand. Nora's off-screen voice says: "Now I'm eating it." The view is Nora's own eyes; only her bare empty hand enters the lower frame, and it never reaches toward or covers the lens. Only Nora speaks. No subtitles or text. Real amateur footage, not a 3D render. Audio: sharp crack of bone splitting, sizzling embers, Nora's savoring sigh
```

### S47 — Hour Sixteen: Replacing Wet Grass Boot Liners

- **Thời lượng:** 8s · **Hồi:** 5 · **Kiểu quay:** `pov_hand`
- **Ref (character_names):** Alva, Bone Dwelling Interior
- **Thoại:** Boots got soaked on that slide. / Wet feet lose heat fast. Dry grass in. / The Iceman did this too.

**prompt (Frame 0)**

```text
First-person POV shot sitting on reindeer furs beside the hearth; Nora pulls damp, crushed grass liners out of her reindeer hide boot; steam gently rises from the damp grass near the warm embers; Alva hands her a bundle of fragrant, bone-dry golden sedge grass to repack the footwear.
```

**video_prompt (R2V)**

```text
Handheld first-person POV documentary footage, eye-level perspective, ultra-wide 0.5x lens, natural handheld breathing motion, photorealistic documentary realism. The view is Nora's own eyes, and only the world in front of her fills the frame; the view simply moves as she moves. Only her bare empty hand enters the lower frame, coming out of a cream suede sleeve with a thick white fox-fur cuff. Setting: Warm hearthside on furs, boot drying area, cozy evening atmosphere. Shot: First-person POV changing damp boot grass liners for dry sedge grass.  0-3s: Nora's bare hand pulls the damp, compacted grass out of her boot; it steams softly in the hearth warmth. Nora's off-screen voice says: "Boots got soaked on that slide." 3-6s: Alva pushes forward a fresh sheaf of dry, fluffy steppe grass; Nora's bare hand pushes the dry grass down into the reindeer hide boot; it compresses and springs back. Nora's off-screen voice says: "Wet feet lose heat fast. Dry grass in." 6-8s: Nora's hand sets the boot upright beside the hearth stones, an arm's length from the flames; faint steam rises from the damp hide. Nora's off-screen voice says: "The Iceman did this too." The view is Nora's own eyes; only her bare empty hand enters the lower frame, and it never reaches toward or covers the lens. Only Nora speaks. No subtitles or text. Real amateur footage, not a 3D render. Audio: rustle of dried grass, gentle sizzle of wet grass on hearth edge, warm fire
```

### S48 — Hour Sixteen: Welcome to the Inner Hearth

- **Thời lượng:** 8s · **Hồi:** 5 · **Kiểu quay:** `tripod`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Alva, Bone Dwelling Interior
- **Thoại:** Alva moved my sleeping spot. / Inner wall, by the fire, not the door. / I'm not crying. It's the smoke.

**prompt (Frame 0)**

```text
Static locked-off shot from a fixed viewpoint inside Dwelling Four; Alva gently guides Nora to sit on a bed of thick winter reindeer pelts along the inner curved wall; this sleeping spot is right beside the glowing hearth, away from the drafty entrance; Nora smiles with genuine emotional warmth, her hourglass figure and deep plunging neckline illuminated in firelight.
```

**video_prompt (R2V)**

```text
Static locked-off footage from a fixed viewpoint resting on a bone ledge, eye-level perspective, wide lens, fixed stable framing, natural warm hearth lighting, photorealistic documentary realism. The frame is completely still; Nora sits in frame interacting naturally with the environment and locals. Her hands are busy with food or garments; she never reaches toward, touches, covers, or points at the camera lens. Setting: Interior of bone dwelling, warm inner sleeping bench, soft reindeer furs, flickering firelight. Shot: Static locked-off shot as Alva invites Nora to the prime warm spot by the inner wall.  BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh dress of bleached white reindeer suede with long sleeves, plush white arctic-fox fur trim at cuffs and hem, an attached fur hood draped on her shoulders, plunging V-neckline laced loosely with thin leather ties, cinched by a wide leather belt sewn with drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur boots. 0-3s: Alva pats the thick pile of white reindeer pelts against the inner bone wall, gesturing for Nora to sit there. Nora says: "Alva moved my sleeping spot." 3-6s: Nora settles onto the warm furs, pulling a soft hide blanket over her legs beside the gentle heat of the hearth. Nora says: "Inner wall, by the fire, not the door." 6-8s: Nora wipes her eye with the back of her hand, smiling. Nora says: "I'm not crying. It's the smoke." The frame never moves; nothing that holds or supports the view is visible anywhere in the shot. Nora stays in frame. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks. No subtitles or text. Real documentary footage, not a 3D render. Audio: soft rustle of furs, popping bone embers, cozy quiet
```


---

## Hồi 6 — Di sản & Văn hóa: Trống sọ voi, Thuật nhuộm & Thú săn đêm (Giờ 17–22)

### S49 — Hour Seventeen: The Eyed Bone Needle Invention

- **Thời lượng:** 8s · **Hồi:** 6 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Alva, Bone Dwelling Interior
- **Thoại:** Hour seventeen. An eyed bone needle. / I've catalogued broken ones for years. Never seen one used. / Sorry. Archaeologist.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length; Nora leans close to watch Alva working; Alva holds a slender, polished ivory needle with a tiny drilled eye; Alva threads a fine strand of split reindeer sinew through the eye; Nora's face is lit with intense academic wonder, her plunging neckline and hourglass figure framed beside the ancient artisan.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Hearthside crafting corner, warm firelight, Alva tailoring with bone needle. Shot: Ultra-wide selfie framing Nora and Alva as Alva demonstrates the eyed bone needle.  Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Nora leans in so Alva's weathered hands and the slender bone needle show beside her face. Nora says: "Hour seventeen. An eyed bone needle." 3-6s: Alva effortlessly threads a translucent strand of split sinew through the tiny drilled eye. Nora says: "I've catalogued broken ones for years. Never seen one used." 6-8s: Nora laughs at herself and looks back into the lens. Nora says: "Sorry. Archaeologist." The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: delicate click of bone needle, pull of sinew thread, crackling hearth
```

### S49A — Hour Seventeen: How Old Are Needles?

- **Thời lượng:** 8s · **Hồi:** 6 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Alva, Bone Dwelling Interior
- **Thoại:** Oldest eyed needles? Siberia, forty thousand years ago. / Europe, only about twenty-six thousand. / This one's practically brand new.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length by the hearth; Alva stitches a hide with a slender bone needle behind Nora's shoulder; firelight on Nora's face, plunging neckline and reindeer suede dress.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Interior of the bone dwelling, hearthside crafting corner, warm firelight. Shot: Ultra-wide selfie framing Nora on the left third and Alva sewing behind her shoulder. Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Behind Nora, Alva keeps stitching steadily without looking at her hands. Nora says, fast, geeking out: "Oldest eyed needles? Siberia, forty thousand years ago." 3-6s: Nora holds up her free hand at chest level, counting on her fingers, well away from the lens. Nora says, fast, geeking out: "Europe, only about twenty-six thousand." 6-8s: She glances at the needle in Alva's fingers and smirks into the lens. Nora says, fast, geeking out: "This one's practically brand new." The hide flexes slightly around the needle point with each stitch. The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: soft pull of sinew, fire crackle
```

### S50 — Hour Seventeen: Stitching Waterproof Reindeer Seams

- **Thời lượng:** 8s · **Hồi:** 6 · **Kiểu quay:** `pov_hand`
- **Ref (character_names):** Alva, Bone Dwelling Interior
- **Thoại:** She uses the eye. Sinew straight through. / Real seams, tight enough to stop wind. / Also beads. Lots of beads.

**prompt (Frame 0)**

```text
First-person macro POV shot; Alva's fingers guide the bone needle through pre-punched holes in bleached reindeer suede; she pulls the sinew tight, creating an incredibly tight, even, windproof seam; tiny mammoth ivory beads are stitched along the seam edge.
```

**video_prompt (R2V)**

```text
Handheld first-person POV documentary footage, eye-level perspective, ultra-wide 0.5x lens, natural handheld breathing motion, photorealistic documentary realism. The view is Nora's own eyes, and only the world in front of her fills the frame; the view simply moves as she moves. Only her bare empty hand enters the lower frame, coming out of a cream suede sleeve with a thick white fox-fur cuff. Setting: Macro POV hearthside, stitching reindeer suede garment, warm amber light. Shot: First-person macro POV showing the precision of Ice Age tailoring and waterproof seams.  0-3s: The view holds close as Alva passes the bone needle through supple reindeer suede. Nora's off-screen voice says: "She uses the eye. Sinew straight through." 3-6s: She pulls each stitch taut with rhythmic speed, creating an airtight interlocking seam. Nora's off-screen voice says: "Real seams, tight enough to stop wind." 6-8s: Nora's empty fingers gently touch the completed row of tiny even stitches. Nora's off-screen voice says: "Also beads. Lots of beads." The view is Nora's own eyes; only her bare empty hand enters the lower frame, and it never reaches toward or covers the lens. Only Nora speaks. No subtitles or text. Real amateur footage, not a 3D render. Audio: soft friction pull of sinew through leather, needle tap on bone thimble, hearth murmur
```

### S50A — Hour Seventeen: Beads Prove Tailoring

- **Thời lượng:** 8s · **Hồi:** 6 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Alva, Bone Dwelling Interior
- **Thoại:** Rows of beads only sit straight on fitted clothes. / That's how we know Sungir wore tailored stuff. / Alva's proving it.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length by the hearth; behind Nora, Alva sews a straight row of small ivory beads along the seam of a fitted hide tunic across her knees; firelight on Nora's face, plunging neckline and reindeer suede dress.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Interior of the bone dwelling, hearthside, a fitted hide tunic laid across Alva's knees, warm firelight. Shot: Ultra-wide selfie framing Nora on the left third and Alva sewing beads behind her shoulder. Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Behind Nora, Alva stitches small ivory beads one by one in a straight row along the seam of a fitted hide tunic. Nora says, fast, excited: "Rows of beads only sit straight on fitted clothes." 3-6s: The row of beads lies flat and even along the curve of the tunic. Nora says, fast, excited: "That's how we know Sungir wore tailored stuff." 6-8s: Alva holds up the tunic briefly to check the row, then keeps sewing; Nora grins into the lens. Nora says, fast, excited: "Alva's proving it." The beads are small, matte and slightly uneven; each one clicks softly as it is pulled tight. The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: soft click of beads, pull of sinew, fire crackle
```

### S51 — Hour Eighteen: Amber & Black Sea Shells

- **Thời lượng:** 8s · **Hồi:** 6 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Alva, Bone Dwelling Interior
- **Thoại:** Amber and fossil shells. / Carried in from up to five hundred kilometres. / Some from the Black Sea side.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length; Alva holds open a small folded hide pouch, displaying polished golden amber beads and perforated fossil sea shells; firelight catches the translucent honey glow of the amber; Nora looks at the jewels with profound historical astonishment, her cleavage and waist framed warmly.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Interior hearthside, Alva displaying trade ornaments, firelight reflections. Shot: Ultra-wide selfie showing prehistoric long-distance trade goods (amber and shells).  Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Alva pours several drilled beads into her palm: raw glowing amber and fossil sea shells. Nora says: "Amber and fossil shells." 3-6s: Nora holds one golden amber bead up to the firelight, its honey glow catching the firelight. Nora says: "Carried in from up to five hundred kilometres." 6-8s: She turns back to camera, eyes wide at the continental connection. Nora says: "Some from the Black Sea side." The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: gentle clink of amber and shell beads, fire crackle, soft rustle of hide
```

### S51A — Hour Eighteen: A Stone Age Group Chat

- **Thời lượng:** 8s · **Hồi:** 6 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Alva, Bone Dwelling Interior
- **Thoại:** The same shells turn up at Mezin and Yudinovo. / Different groups, all swapping things. / Stone Age group chat.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length by the hearth; behind Nora, Alva pours small perforated fossil shells into a hide pouch; firelight on Nora's face, plunging neckline and reindeer suede dress.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Interior of the bone dwelling, hearthside, a small hide pouch of beads and shells, warm firelight. Shot: Ultra-wide selfie framing Nora on the left third and Alva behind her shoulder with the pouch. Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Behind Nora, Alva pours the fossil shells back into the small hide pouch and ties it shut. Nora says, fast, dry: "The same shells turn up at Mezin and Yudinovo." 3-6s: Alva sets the pouch beside the hearth with care; Nora glances back at it. Nora says, fast, dry: "Different groups, all swapping things." 6-8s: Nora looks into the lens with a dry smile. Nora says, fast, dry: "Stone Age group chat." The shells are small, perforated and pale; they slide into the pouch one by one. The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: soft rattle of shells, fire crackle
```

### S52 — Hour Nineteen: The Painted Mammoth Skull Reveal

- **Thời lượng:** 8s · **Hồi:** 6 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Painted Mammoth Skull, Mezhyrich Camp
- **Thoại:** Hour nineteen. Remember that museum drawer? / Red ochre dots and lines. On the actual skull. / Okay. Okay. Breathe.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length in the ceremonial alcove near the dwelling entrance; resting prominently on a foundation of mammoth mandibles is an enormous mammoth skull decorated with red ochre dots and lines; Nora stands beside it with reverence, her tall hourglass figure and plunging neckline lit by torchlight.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Ceremonial entrance alcove of Dwelling One, torchlight and hearth glow, painted mammoth skull altar. Shot: Ultra-wide selfie revealing the famous painted mammoth skull of Mezhyrich. Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Nora steps into the entrance alcove, stopping so the colossal painted mammoth skull, there from the first second, shows behind her shoulder; nothing pops into view. Nora says: "Hour nineteen. Remember that museum drawer?" 3-6s: She steps aside slightly, framing the full cranial vault covered in red ochre dots and lines. Nora says: "Red ochre dots and lines. On the actual skull." 6-8s: She glances back at the red patterns with breathless emotional reverence. Nora says: "Okay. Okay. Breathe." The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: flickering torch hiss, Nora's hushed awe breath, deep resonant silence
```

### S53 — Hour Nineteen: Red Ochre Pigment of Deep Time

- **Thời lượng:** 8s · **Hồi:** 6 · **Kiểu quay:** `pov_hand`
- **Ref (character_names):** Painted Mammoth Skull, Mezhyrich Camp
- **Thoại:** Ochre. Iron-rich earth, ground up. / Eighteen thousand years from now, it's still red. / That's how we find it.

**prompt (Frame 0)**

```text
First-person macro POV shot; Nora's bare fingertips hover millimetres above the bold crimson red ochre geometric lines painted on the porous mammoth cranial bone; the mineral hematite pigment is rich, vibrant, and textured; torchlight flickers across the ancient bone surface.
```

**video_prompt (R2V)**

```text
Handheld first-person POV documentary footage, eye-level perspective, ultra-wide 0.5x lens, natural handheld breathing motion, photorealistic documentary realism. The view is Nora's own eyes, and only the world in front of her fills the frame; the view simply moves as she moves. Only her bare empty hand enters the lower frame, coming out of a cream suede sleeve with a thick white fox-fur cuff. Setting: Macro POV of the painted mammoth skull cranial surface, flickering warm torchlight. Shot: First-person macro POV of the red ochre paint on the mammoth skull.  0-3s: Nora's fingers gently hover over the red ochre dots and lines, tracing the painted dots. Nora's off-screen voice says: "Ochre. Iron-rich earth, ground up." 3-6s: The view holds on the red pigment against the pale bone. Nora's off-screen voice says: "Eighteen thousand years from now, it's still red." 6-8s: Her hand turns, fingertips raised, showing faint red powder caught in the fingerprint ridges. Nora's off-screen voice says: "That's how we find it." The view is Nora's own eyes; only her bare empty hand enters the lower frame, and it never reaches toward or covers the lens. Only Nora speaks. No subtitles or text. Real amateur footage, not a 3D render. Audio: gentle torch flutter, soft rustle of fingers near bone, solemn silence
```

### S54 — Hour Nineteen: Resonance of the Mammoth Bone Drum

- **Thời lượng:** 8s · **Hồi:** 6 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Torak, Painted Mammoth Skull
- **Thoại:** Listen to that. / Worn dents on top. A drum? We still argue. / Sounds like a drum to me.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length; Torak steps into the alcove holding a carved reindeer antler mallet; Torak strikes the thick frontal bone of the painted mammoth skull; a deep, hollow, resonant boom echoes throughout the dwelling; Nora's eyes widen as acoustic vibrations fill the space; her voluptuous figure and deep cleavage are illuminated in torchlight.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Ceremonial alcove, torchlight, Torak striking the mammoth skull with antler mallet. Shot: Ultra-wide selfie as Torak demonstrates the mammoth skull drum.  Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Torak steps beside the painted skull, raising a polished antler club with focused ritual seriousness. Nora says: "Listen to that." 3-6s: Torak strikes the parietal dome with measured rhythm; the hollow bone interior produces a deep, bass-heavy acoustic boom. Nora says: "Worn dents on top. A drum? We still argue." 6-8s: Nora listens with chills running down her spine as the sound reverberates through the bone dwelling. Nora says: "Sounds like a drum to me." The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: deep resonant percussive bone boom (hollow, echoing bass note), torch crackle, Nora's quiet gasp
```

### S55 — Hour Twenty: Acoustic Wear & Ancient Rhythm

- **Thời lượng:** 8s · **Hồi:** 6 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Painted Mammoth Skull, Mezhyrich Camp
- **Thoại:** The dents match the bones lying beside it. / Somebody hit this. A lot. / I'm choosing to believe music.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length; Nora leans close to the painted skull as Torak continues a steady, slow ritual pulse in the background; Nora points to the microscopic impact dents and polished facets along the skull crest; torchlight creates dramatic dancing shadows on her face, cleavage, and reindeer suede dress.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Ceremonial alcove, rhythmic bone percussion in background, warm torchlight. Shot: Ultra-wide selfie showing the physical wear patterns from centuries of drumming.  Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Nora leans close to the skull dome so it fills the frame behind her shoulder, where dozens of small indented impact craters are visible under the ochre. Nora says: "The dents match the bones lying beside it." 3-6s: The rhythmic heartbeat thud of the bone drum pulses steadily behind her speech. Nora says: "Somebody hit this. A lot." 6-8s: She looks into the camera, transported across millennia by the acoustic rhythm. Nora says: "I'm choosing to believe music." The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: rhythmic slow tribal bone thumping (heartbeat tempo), warm room reverberation, torch crackle
```

### S56 — Hour Twenty-One: Night Perimeter & Glowing Eyes

- **Thời lượng:** 8s · **Hồi:** 6 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Mezhyrich Camp
- **Thoại:** Hour twenty-one. Brutal, brutal cold out here. / Wait. Eyes, out past the bone pile. / Holy cr— so many.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length outside in the freezing arctic night; Nora stands near the outer bone refuse pile, illuminated by torchlight; behind her in the pitch darkness twenty metres away, three pairs of bright yellow-green eyes reflect the torchlight; Nora's breath vapor fades fast in the freezing air; her tall hourglass figure and fur hood are dusted with frost.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Outer perimeter of Mezhyrich camp, midnight, torchlight against black snowy night. Shot: Ultra-wide selfie as Nora points toward glowing eyes in the darkness outside camp.  Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Nora stands beside a burning bone-fat torch planted in the snow, her breath vapor fading fast in the extreme cold; her free left hand is empty. Nora says: "Hour twenty-one. Brutal, brutal cold out here." 3-6s: She glances back over her shoulder: past the bone midden, twenty metres behind her, three pairs of eyes that were there from the first second glow in the torchlight. Nora says: "Wait. Eyes, out past the bone pile." 6-8s: The eyes stay at the same distance, blinking now and then; one pair slowly backs away. Nora says: "Holy cr— so many." The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: intense crackling torch fire, sub-zero wind whistle, soft guttural canine panting
```

### S57 — Hour Twenty-One: Wolves & the Dog Debate

- **Thời lượng:** 8s · **Hồi:** 6 · **Kiểu quay:** `pov`
- **Ref (character_names):** Mezhyrich Camp
- **Thoại:** Wolves. After the scraps, I hope. / Some skulls from sites like this look half-dog. / We still argue about it.

**prompt (Frame 0)**

```text
First-person eye-level POV shot illuminated by torchlight; two large, thick-furred Pleistocene wolves (Canis lupus) gnaw on discarded mammoth ribs near the camp perimeter; one wolf glances up at the torchlight with calm, intelligent amber eyes, watchful, before continuing to chew; frost coats their grey-white muzzles.
```

**video_prompt (R2V)**

```text
Handheld first-person POV documentary footage, eye-level perspective, ultra-wide 0.5x lens, natural handheld breathing motion, photorealistic documentary realism. The view is Nora's own eyes, and only the world in front of her fills the frame; the view simply moves as she moves. Setting: Perimeter bone midden at night, torchlight illuminating scavenging Ice Age wolves. Shot: First-person POV showing wolves scavenging at camp edge, early domestication.  0-3s: The torchlight illuminates two large wolves, about fifteen metres away, chewing on mammoth bones in the snow. Nora's off-screen voice says: "Wolves. After the scraps, I hope." 3-6s: The closer wolf pauses, looks up into the light, ears forward, then lowers its head. Nora's off-screen voice says: "Some skulls from sites like this look half-dog." 6-8s: The wolves resume chewing, staying at the same distance; they never come closer. Nora's off-screen voice says: "We still argue about it." The view is Nora's own eyes; only the world in front of her fills the frame. Only Nora speaks. No subtitles or text. Real amateur footage, not a 3D render. Audio: crunch of heavy carnivore teeth crushing frozen bone, soft canine snorts, wind
```

### S58 — Hour Twenty-One: Stars Without Polaris

- **Thời lượng:** 8s · **Hồi:** 6 · **Kiểu quay:** `wide`
- **Ref (character_names):** Mezhyrich Camp
- **Thoại:** Clear sky. Colder night, heat just radiates away. / And no Polaris. The pole's near Deneb. / Same stars, different centre.

**prompt (Frame 0)**

```text
Handheld wide documentary pan at night from the river bluff; the four mammoth bone dwellings of Mezhyrich glow warm amber from hearth fires inside; curling smoke rises from roof vents into a crystal-clear, deep indigo night sky filled with millions of glittering stars and the Milky Way; the stars are sharp fixed points.
```

**video_prompt (R2V)**

```text
Handheld eye-level wide documentary pan, ultra-wide 0.5x lens, slow sweeping perspective from Nora's viewpoint, natural handheld breathing sway, photorealistic documentary realism. The view is Nora's own eyes; only the camp and the sky fill the frame. Setting: High bluff overlooking Mezhyrich camp at midnight, four glowing mammoth bone huts, brilliant prehistoric night sky. Shot: Handheld wide documentary pan across the glowing settlement under ancient stars.  0-3s: The view slowly pans across the four mammoth bone domes, their silhouettes glowing like lanterns on the snowy terrace. Nora's off-screen voice says: "Clear sky. Colder night, heat just radiates away." 3-6s: The view tilts upward toward the staggering brilliance of the unpolluted Milky Way arching overhead. Nora's off-screen voice says: "And no Polaris. The pole's near Deneb." 6-8s: The view holds on the sky; the stars are sharp fixed points and the sky does not rotate. Nora's off-screen voice says: "Same stars, different centre." Handheld pan seen through Nora's own eyes; only the camp and the sky fill the frame. Only Nora speaks. No subtitles or text. Real amateur footage, not a 3D render. Audio: deep expansive nighttime silence, gentle breath of wind across snow, crackle of smoke
```

### S58A — Hour Twenty-One: Shivering Is Good

- **Thời lượng:** 8s · **Hồi:** 6 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Mezhyrich Camp
- **Thoại:** Okay. Shivering. That's my body working. / My muscles are burning fuel for heat. / When it stops, then worry.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length at night beside a bone dwelling doorway; a bone-fat torch planted in the snow lights Nora's face; she shivers hard, frost on her fur hood; her tall hourglass figure and plunging neckline in warm torchlight.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Mezhyrich camp at night beside a dwelling entrance, a bone-fat torch planted in the snow, clear starry sky. Shot: Ultra-wide selfie at arm's length framing Nora by the torchlit doorway. Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Nora stands by the torchlit doorway, shivering hard, her breath vapor fading fast in the cold air. Nora says, teeth chattering: "Okay. Shivering. That's my body working." 3-6s: She hugs her free arm across her chest; her teeth chatter between words. Nora says, teeth chattering: "My muscles are burning fuel for heat." 6-8s: She glances at the dark doorway beside her, then back into the lens, serious for a moment. Nora says, teeth chattering: "When it stops, then worry." The torch is planted in the snow beside her; her free hand stays at her chest. The camp stays still behind her. The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: chattering teeth, torch crackle, faint wind
```

### S59 — Hour Twenty-Two: Cave Lion Roar on the River Ice

- **Thời lượng:** 8s · **Hồi:** 6 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Cave Lion, Mezhyrich Camp
- **Thoại:** Hold on. That roar came from the river. / Cave lion. Down on the ice. / Okay. Inside. Right now.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length outside the dwelling entrance at night; Nora pauses mid-breath as a deep, ground-shaking roar echoes from the frozen river below; in the distant blue moonlight on the river ice four hundred metres away, the powerful silhouette of an enormous maneless Eurasian cave lion (Panthera spelaea) stalks across the snow; Nora's eyes widen, her cleavage and fur hood illuminated by torchlight.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Exterior entrance of bone dwelling, midnight torchlight, frozen river in distant moonlight. Shot: Ultra-wide selfie as Nora hears the terrifying roar of a cave lion on the river ice.  Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: A deep, thunderous guttural roar reverberates across the river valley, causing Nora to freeze in her tracks. Nora says: "Hold on. That roar came from the river." 3-6s: She turns her head to look over her shoulder: far below on the moonlit river ice, about four hundred metres away and visible from the first second, a big pale maneless cave lion walks slowly along the ice; it never runs, climbs or comes closer. Nora says: "Cave lion. Down on the ice." 6-8s: Nora quickly turns back toward the warm, safe doorway of Hut Four. Nora says: "Okay. Inside. Right now." The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: deep, vibrating low-frequency cave lion roar echoing through valley, sudden wolf silence, Nora's hurried footsteps
```


---

## Hồi 7 — Kết trầm: Suy ngẫm trong đêm & Bình minh 16.000 năm (Giờ 22–24)

### S60 — Hour Twenty-Two: Safe by the Dying Embers

- **Thời lượng:** 8s · **Hồi:** 7 · **Kiểu quay:** `tripod`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Alva, Bone Dwelling Interior
- **Thoại:** Lion outside. Fire inside. I'll take inside. / Alva banked the fire with bone. / Hide and bone. That's the wall.

**prompt (Frame 0)**

```text
Static locked-off shot from a fixed viewpoint inside the bone dwelling; Nora sits wrapped in a thick mammoth-wool-lined reindeer hide blanket by the low red hearth embers; Alva sleeps peacefully on fur benches in the background; warm red coals cast a gentle, intimate glow over Nora's face, deep cleavage, and tired posture.
```

**video_prompt (R2V)**

```text
Static locked-off footage from a fixed viewpoint resting on a bone ledge, eye-level perspective, wide lens, fixed stable framing, natural warm hearth lighting, photorealistic documentary realism. The frame is completely still; Nora sits in frame interacting naturally with the environment and locals. Her hands are busy with food or garments; she never reaches toward, touches, covers, or points at the camera lens. Setting: Cozy interior of bone dwelling, late night, glowing red hearth embers, sleeping hunters. Shot: Static locked-off shot of Nora sitting quietly wrapped in furs by the dying embers.  BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh dress of bleached white reindeer suede with long sleeves, plush white arctic-fox fur trim at cuffs and hem, an attached fur hood draped on her shoulders, plunging V-neckline laced loosely with thin leather ties, cinched by a wide leather belt sewn with drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur boots. 0-3s: Nora sits quietly on the furs, pulling the soft reindeer blanket up to her chest, looking at the glowing red coals. Nora says: "Lion outside. Fire inside. I'll take inside." 3-6s: Alva has banked the hearth with heavy mammoth bone joints that smolder with steady, long-lasting warmth. Nora says: "Alva banked the fire with bone." 6-8s: Nora looks at the camera with peaceful exhaustion. Nora says: "Hide and bone. That's the wall." The frame never moves; nothing that holds or supports the view is visible anywhere in the shot. Nora stays in frame. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks. No subtitles or text. Real documentary footage, not a 3D render. Audio: gentle breathing of sleeping occupants, soft ticking of dying embers, quiet outside wind
```

### S61 — Hour Twenty-Three: Ten Years Measuring This Floor

- **Thời lượng:** 8s · **Hồi:** 7 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Bone Dwelling Interior
- **Thoại:** Hour twenty-three. Everyone's asleep. / I've measured this floor in centimetres for ten years. / Never knew it was warm.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length in a quiet late-night whisper; Nora holds the camera close, speaking directly into the lens with deep introspection; the dying amber coals reflect softly in her grey-green eyes; her voluptuous figure, tiny waist, and plunging neckline are warmly shadowed; the mammoth bone roof curves protectively above.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Quiet interior of bone dwelling at 3 AM, deep night whisper, faint firelight. Shot: Ultra-wide selfie in intimate close-up as Nora shares her archaeological epiphany.  Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Nora speaks in a soft, reverent whisper, her outstretched arm drawn in a little closer than usual. Nora says: "Hour twenty-three. Everyone's asleep." 3-6s: She looks up at the curved mammoth tusk rafters holding the ceiling above her head. Nora says: "I've measured this floor in centimetres for ten years." 6-8s: She looks back into the lens, eyes moist with profound admiration. Nora says: "Never knew it was warm." The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: intimate soft whisper, gentle nighttime hearth settling, distant wind hush
```

### S62 — Hour Twenty-Four: Blue Hour Frost

- **Thời lượng:** 8s · **Hồi:** 7 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Mezhyrich Camp
- **Thoại:** Coldest part of the night. Right before sunrise. / Everything's frozen. Even the river mist. / And it's so quiet.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length stepping out into the pre-dawn blue hour; the frozen river terrace is bathed in serene, mystical deep blue twilight; intricate frost crystals sparkle on the mammoth skull entrance arch; Nora's breath plumes in thick white clouds, cheeks flushed fresh in the dawn cold; her hourglass frame stands tall.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Mezhyrich camp exterior, blue hour before sunrise, frost crystals everywhere. Shot: Ultra-wide selfie as Nora steps out into the tranquil blue pre-dawn light.  Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: Nora steps out into the crisp blue twilight, breathing in the purest sub-zero air. Nora says: "Coldest part of the night. Right before sunrise." 3-6s: Behind her, diamond dust ice crystals sparkle in the morning air over the frozen river. Nora says: "Everything's frozen. Even the river mist." 6-8s: She smiles peacefully into the camera; the world is utterly tranquil. Nora says: "And it's so quiet." The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: Nora's deep cold breath intake, gentle crunch of fresh frost on crust, serene silence
```

### S63 — Hour Twenty-Four: First Light Sign-Off

- **Thời lượng:** 8s · **Hồi:** 7 · **Kiểu quay:** `selfie`
- **Ref (character_names):** Nora, Nora Body, Nora Outfit, Mezhyrich Camp
- **Thoại:** Hour twenty-four. First light. / Hands work. Toes probably work. They did this every winter. / I did one day. One.

**prompt (Frame 0)**

```text
Ultra-wide selfie at arm's length at sunrise; the first direct beam of brilliant golden sunlight strikes across Nora's face, illuminating the giant spiraling mammoth tusks arched over Dwelling One behind her in dazzling amber light; Nora looks into the camera with triumphant warmth, strength, and pride; her tall statuesque figure, tiny waist, long slender legs, and plunging neckline are glorious in the sunrise.
```

**video_prompt (R2V)**

```text
Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective, auto-exposure, photorealistic documentary realism. The lens sits at the end of Nora's outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at Nora; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height. Her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen. Her right arm stays extended toward the lens while her free left hand is completely empty and rests naturally at her side. Subtle walking gait bounce. Setting: Mezhyrich camp, sunrise, golden sunlight illuminating mammoth tusks and snowy steppe. Shot: Ultra-wide selfie sign-off as sunrise bathes Nora and the settlement in brilliant gold.  Nora looks exactly like her reference images: face from Nora face sheet (honey-blonde high ponytail, grey-green eyes), tall curvy hourglass build from Nora Body sheet, and clothing from Nora Outfit sheet. BODY LOCK (CRITICAL -- match Nora Body reference): Nora is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an exaggerated voluptuous curvy hourglass silhouette, a dramatically tiny narrow cinched waist, and an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage). OUTFIT LOCK (CRITICAL -- match Nora Outfit reference): she wears a fitted mid-thigh-length dress of soft bleached white cream reindeer suede with long sleeves, tailored to follow her curves, trimmed with plush fluffy white arctic-fox fur at cuffs and hem, an attached white arctic-fox fur hood draped on her shoulders, a plunging V-neckline laced loosely with thin leather ties and small bone beads, cinched at the waist by a wide leather belt sewn with rows of drilled arctic-fox canine teeth, snug cream suede leggings, and knee-high fur-lined boots with white fur cuffs -- clean fur-trimmed cuffs with NO mittens on the outfit reference, NO silk, NO satin, NO modern fabric. 0-3s: The golden sun crests the eastern horizon, flooding Nora's face and the snow with blinding golden warmth. Nora says: "Hour twenty-four. First light." 3-6s: She wiggles her fingers and takes a triumphant breath, looking radiant in her fur-trimmed reindeer suede dress. Nora says: "Hands work. Toes probably work. They did this every winter." 6-8s: She smiles proudly directly into the camera lens with a final, confident sign-off nod. Nora says: "I did one day. One." The viewer looks straight at Nora from the end of her outstretched right arm; her right hand stays beyond the frame edge. Nora stays in frame and never disappears. Natural wide-angle perspective. She never reaches toward, touches, covers, or points at the camera lens. Only Nora speaks; locals communicate only with natural gestures and expressions. No subtitles or text appear in the frame. Real amateur footage, not a movie or 3D render. Audio: rising morning breeze, cheerful bird call, crisp snow crunch
```

