# EMBERS — Script v6 (storyboard · "breathless" cut, 10-minute pass)

- **Package:** She Broke the One Rule Firefighters Never Break | EMBERS · Nora's soot-and-retardant-streaked face under the yellow "HALE" helmet, a crown fire behind, grey horse in the smoke, text "DON'T GO BACK" · A young firefighter defies orders and walks into a wildfire to save her brother — and the horse she sold.
- Format: cinematic short drama, English dialogue, 16:9, ~10:20. Story bible: `story-bible.md`. v3 (`script.md`), v4 (`script_v4.md`) and v5 (`script_v5.md`) are kept unchanged.
- Cast: **Nora Hale** (23, wildland firefighter), **Eli Hale** (14, her brother), **Capt. Ray Duran** (~55), **Juniper** (old grey mare). Off-screen voices: dispatch, Walt Pruitt (county volunteer), crew, a rookie. Keller (buyer) never appears.
- v4 (2026-10-17): rebuilt for retention after the user found v3 slow. Trailer cold open (premise by 0:07), morning cut from 2:50 to 0:44, fire spectacle every 20–30 s on the line (ember storm → burnout → walls meet → fire whirl → retardant drop → wind shift → run), Eli's danger cross-cut from 1:38. Two native voices per clip now allowed (tested 2026-10-17). Skill review in §17.
- v5 (2026-10-17): independent per-minute retention review (weak spots 4:00–5:00 and 8:00–9:00 scored 5/10). Fixes: Eli's voicemail now ends in a crash and a dead line, cut off at 3:09 and heard in full only at RR-04 · Ridge Road filler cut (CH-08, RR-03, RR-05, RR-09), new clue RR-14 (bike track in the ash), near-miss in RR-13 · the mother reveal moves under the foil during the burnover (BK-07 → BK-15 → BK-11 → BK-12), BK-10 cut, confession BK-08 becomes the foil-off reveal · briefings compressed (RA-07, FL-05), FL-03 cut · "most stubborn Hale" line moves to Ray at DW-08.
- v6 (2026-10-17): runtime 8:45 → ~10:20 (user: must be 10–11 min). No filler — every added block raises stakes or adds spectacle: **B-story "the last line"** (Ray and the crew hold Cedar Flat while Nora is gone — two cross-cuts LH-01→04 and LH-05→08: evacuation, Nora's radio on Ray's chest, the fire front pouring at the town, a slopover knocked down; pays at dawn DW-06 "Not one house") · **escape from the barn** (ES-01→05: burning lane, falling rail, the way down cut off — explains why they end up trapped on the rise) · **the climb** (TR-07/08: a snag falls, Eli saves Nora — role reversal pays in action) · Eli cross-cut on the line (EL-07) · crew retreat (MP-05) · BK-16 (hands under the foil) · RA-07 and BK-01 back to 8s. New location ref `Cedar Flat`.

## Look

- **Nora** (adult, 23): striking, very pretty face, athletic and strong with a fit, full figure; a confident, hard stare. Ranch: fitted flannel shirt or fitted t-shirt, jeans, boots. Field: realistic wildland gear — yellow Nomex shirt, green fire pants, pack, gloves, goggles. Soot on her face from FL-04; pink retardant streaks from FL-12. Attractive, never posed: the camera treats her as a firefighter.
- **Eli** (14): an ordinary boy — hoodie, jeans, sneakers, backpack. Described only by clothes, age and actions. No other physical or body description, ever.
- **Ray** (~55): grey stubble, weathered face, white captain's helmet.
- **Juniper**: old grey mare, a dark eye, a braided forelock.

## Voices (Gemini TTS library — first word of `voice_description`)

| Character | Voice ID | Why | Used |
|---|---|---|---|
| Nora | `kore` | firm, low-mid female, clipped orders | native (Slot 7) + post |
| Eli | `fenrir` | young, excitable, cracks when shouting | native + post |
| Ray | `algenib` | gravelly older male | native + post |
| Walt Pruitt | `sadaltager` | older rural male | post only, radio / off-screen |
| Dispatch | `erinome` | clear, flat female | post only, radio EQ |
| Crew, rookie | `alnilam` | neutral male | post only |

- **Two native voices per clip** (tested 2026-10-17, `voicetest/RA-03_voicetest.mp4`): Slot 7 takes a list, e.g. `[["fenrir"],["kore"]]`, and lip-sync follows the speaker named in the prompt. Used only when both speakers face the camera (rows marked `native: A + B`). **Pipeline note:** FlowKit's scene `GENERATE_VIDEO_REFS` still sends only the first voiced character — wire multi-voice before generating these rows (code change, done only while no job is running).
- **Post-VO** = line added in the edit in that voice: speaker off-screen, back to camera, or mouth covered. Radio lines get radio EQ. The prompt says "[name]'s mouth stays closed". Words column = native + post together (Rule 49).
- Every spoken line in a video_prompt ends with "(no subtitles)".

## Camera & continuity plan

- **Screen direction:** toward the fire = left → right. Toward home / safety (and the black) = right → left.
- **Axis:** Ray screen-left, Nora screen-right in every two-shot. Planned axis flip at TR-05.
- **Lenses:** 35–50mm static at the ranch → 24–35mm handheld on the line → 85mm for confrontations (CH, BN) → locked-off 85mm two-shots at dawn. Ray low angle until CH-07, high angle after.
- **Fire rule (anti-CGI):** documentary look — 35mm grain, handheld, faces lit by glow, smoke and embers in the air, fire never fills the foreground of a face shot. Big-fire shots (FL-08, FL-09, FL-11, RR-13, BK-14) are framed as real news/IR-crew footage: long lens, heat shimmer, smoke-dimmed sun. Test the hardest one (FL-08) first.
- **Helmets:** Nora wears a plain yellow `Crew Helmet` FL-01→CH-09. The mother's `HALE Helmet` (scorched brim) rides on the pickup seat from RA-07 until RR-06, where Nora puts it on; she wears it until BK-04, Eli from BK-04. Ray wears a white helmet.
- **Nora Body Fire states:** A clean (FL-01→FL-02) · A1 sooted (FL-04→FL-11) · A2 sooted + pink retardant streaks (FL-12→CH-09) · B sooted + retardant + scorched sleeve (RR-01→end).
- **Refs:** faces `Nora`, `Eli`, `Ray`, `Juniper` (creature turnaround). Bodies `Nora Body Ranch`, `Nora Body Fire`. Locations `Hale Ranch`, `Fire Line`, `Staging Area`, `Cedar Flat` (v6: town edge, dozer line between the last houses and the brush), `Ridge Road`, `Keller Barn`, `The Black`. Props `HALE Helmet`, `Crew Helmet`, `Nora Pickup`, `Eli Bike`, `Eli Pack`. (`Hale Kitchen`, `Hale Barn Stall` from v3 are no longer needed.)
- SF: **G** = new start frame, no ref person · **E** = new start frame with refs (Rule 63) · **P** = last frame of the previous clip (Rule 65) · **R** = re-cut from a later clip in the edit (nothing generated).
- No readable text is generated. Every video_prompt ends with "no background music".
- Dialogue cell: speaker in parentheses (not counted). Rule 49: 4s 0 or 6–8 · 6s 12–15 · 8s 18–22 · 10s 24–28.
- Edit-only after the hook: smash to black, title EMBERS (~2s), card "THAT MORNING".

## 1. Cold open — trailer (re-cut, 0:00–0:38)

Built in the edit from later clips (trailer-intro structure: conflict 0–3s → premise 3–9s → escalation → button). Every piece asks a question; none shows how it ends.

| Clip | Dur | Shot | Ref | SF | Light | Visual | Dialogue | Words | Voice | Beat |
|---|---|---|---|---|---|---|---|---|---|---|
| HK-01 | 4s | ECU | re-cut of RR-06 | R | night, orange fire glow | Embers rain onto the yellow helmet stenciled HALE as Nora buckles the strap. | (post-VO Ray, truck radio) "Hale. Do not go back in there." | 7 | post: Ray (radio) | Hook · 3-second conflict |
| HK-02 | 4s | CU | re-cut of EM-02 | R | dusk, orange | Nora, soot and pink retardant on her face, freezes with her hand on the truck door. | (audio lifted from EM-01, Walt on radio) "He biked up Ridge Road at four." | 7 | post: Walt (radio) | Hook · premise |
| HK-03 | 4s | EWS | re-cut of FL-08 | R | dusk, smoke-red sun | A crown fire rolls down a canyon toward the lights of a small town. | (post-VO Dispatch, radio) "It's crowning. Coming straight down on Cedar Flat." | 8 | post: Dispatch | Hook · stakes |
| HK-04 | 4s | ECU | re-cut of FL-06 | R | dusk | A drip torch dribbles a line of fire into dry grass. | (no dialogue, torch hiss) | 0 | none | Hook · fight fire with fire |
| HK-05 | 4s | EWS | re-cut of FL-08 | R | dusk | Two walls of fire meet and tear upward into one column. | (no dialogue, roar) | 0 | none | Hook · spectacle |
| HK-06 | 4s | WS | re-cut of FL-11 | R | dusk | An air tanker drops a red cloud of retardant over the crew. | (no dialogue, engine roar) | 0 | none | Hook · spectacle |
| HK-07 | 4s | CU 85mm | re-cut of CH-02 | R | dusk, orange | Nora, unblinking, to someone off-frame. | (Nora) "Move, Ray. I'm not asking twice." | 6 | native: Nora | Hook · defiance |
| HK-08 | 4s | WS | re-cut of RR-02 | R | night, headlights | A burning pine crashes across the road in the headlights. | (no dialogue, crash) | 0 | none | Hook · obstacle |
| HK-09 | 4s | MS | re-cut of BN-02 | R | night, orange through slats | Inside a smoky barn, a boy fights a knotted rope while a grey mare rears. | (no dialogue, horse scream) | 0 | none | Hook · question |
| HK-10 | 4s | ECU | re-cut of LS-02 | R | night, fire glow | A foil fire shelter snaps open in a gale of embers. | (no dialogue, foil roar) | 0 | none | Hook · question |
| HK-11 | 4s | WS | re-cut of RR-07 | R | night, orange | Nora, back to camera, walks toward a wall of fire. Smash to black, title. | (audio lifted from FL-13, Nora) "You never go back on a fire." | 7 | native: Nora | Hook · button (irony) |

## 2. Morning — the sale (0:38–1:21)

| Clip | Dur | Shot | Ref | SF | Light | Visual | Dialogue | Words | Voice | Beat |
|---|---|---|---|---|---|---|---|---|---|---|
| RA-01 | 6s | EWS | Hale Ranch | G | dawn, golden, dry haze | A small ranch in dry golden hills; a horse trailer waits in the yard; on the far ridge a brown smoke column already rises. | (no dialogue, wind, trailer ramp clanks) | 0 | none | Establishing · threat already visible |
| RA-02 | 8s | MS | Nora, Nora Body Ranch, Eli, Juniper, Hale Ranch | E | dawn, golden | Nora (fitted flannel) walks the grey mare up the trailer ramp; Eli runs in and grabs the lead rope; both face each other in profile. | (Eli) "Mom rode her through the Pine Gulch burn. You can't sell her." (Nora) "Let go. Mom isn't paying the bank, Eli. I am." | 22 | native: Eli (fenrir) + Nora (kore) | Wound · plant: Pine Gulch |
| RA-03 | 4s | ECU | Juniper, Nora Body Ranch, Hale Ranch | E | dawn, golden | Juniper's dark eye; rack focus to Nora's hand stopping near her muzzle, then pulling back. | (no dialogue) | 0 | none | Plant: the look |
| RA-04 | 6s | MCU | Nora, Nora Body Ranch, Hale Ranch | E | morning, hard sun | The pager on Nora's belt buzzes; she reads it, then looks at the smoke column. | (Nora) "All crews called in. It's moving. Eli, stay home today. I mean it." | 13 | native: Nora | Clock set |
| RA-05 | 6s | OTS→Eli | Eli, Nora Body Ranch, Hale Ranch | E | morning, hard sun | Over Nora's shoulder: Eli turns away from her toward the trailer. | (Eli) "Go, then. You're good at going. Mom went. Now you go too." | 12 | native: Eli | Plant: "good at going" |
| RA-06 | 4s | WS | Juniper, Hale Ranch | E | morning, dust | Keller's trailer pulls out; the mare's head turns in the slats; she whinnies. | (no dialogue, hooves knocking) | 0 | none | Loss |
| RA-07 | 8s | MCU | Nora, Nora Body Fire, HALE Helmet, Nora Pickup | E | truck cab, morning | Nora drives in her yellow fire shirt; the scorched yellow HALE helmet rides on the passenger seat; through the windshield the column has bloomed into a white pyrocumulus cloud. | (post-VO Dispatch, truck radio) "Evacuation warning for Cedar Flat, Ridge Road and Keller Lane. Fire's making a run. All crews report to Division Alpha." | 20 | post: Dispatch (radio) | RH · stakes · plant: helmet, Keller Lane |
| RA-08 | 4s | MS | Eli, Eli Pack, Hale Ranch | E | morning | By the fence, eyes on the smoke, Eli stuffs a halter and lead rope into his backpack. | (no dialogue) | 0 | none | Plant: halter |
| RA-09 | 4s | EWS | Eli, Eli Bike, Eli Pack, Hale Ranch | E | morning | Eli pedals off down the lane, left to right, toward the smoke. Ray's briefing pre-laps. | (no dialogue, bike freewheel ticking) | 0 | none | Eli goes |

## 3. The line — fighting it (1:21–2:29)

| Clip | Dur | Shot | Ref | SF | Light | Visual | Dialogue | Words | Voice | Beat |
|---|---|---|---|---|---|---|---|---|---|---|
| FL-01 | 8s | WS | Ray, Fire Line | E | midday, smoke haze | A crew in yellow shirts on a dry ridge; a white pyrocumulus towers behind; Ray (white helmet) points at a black, already-burned slope far off. | (Ray) "Wind's twenty and climbing. Town's four miles back. We hold here. Fire goes wrong, get in the black above Keller's." | 20 | native: Ray | Stakes · plant: the black |
| FL-02 | 6s | MCU | Nora, Nora Body Fire, Crew Helmet, Fire Line | E | midday haze | Nora snaps the fire shelter pouch on her belt shut and glances off-frame right at a rookie. | (post-VO rookie, off-screen) "You ever had to deploy one of those?" (Nora) "No. My mother did. Once." | 13 | native: Nora · post: rookie | Plant: shelter, mother |
| FL-04 | 6s | WS | Ray, Fire Line | E | afternoon, ember rain | An ember storm: glowing embers blow sideways across the crew cutting line; Ray slaps a smoking spot off a rookie's pack. | (Ray) "Embers! Check your partner's back! Keep cutting, keep moving, don't stop now!" | 12 | native: Ray | RH · ember storm |
| EL-01 | 6s | MS head-on | Eli, Eli Bike, Eli Pack, Ridge Road | E | afternoon, smoke haze | Eli pedals hard up a gravel road through dry pines, straight toward camera, a halter strap hanging from his pack. | (no dialogue, gravel, breath) | 0 | none | Cross-cut · danger begins |
| EL-02 | 6s | EWS | Eli, Eli Bike, Ridge Road | E | afternoon haze | Eli lifts his bike around a road barricade and rides on into the haze; far behind, a man by a pickup waves both arms. Eli's mouth stays closed. | (post-VO Walt, off-screen shout) "Hey! Eli Hale! That road's closed! Get back here right now, son!" | 12 | post: Walt | Plant: Walt saw him |
| FL-05 | 4s | 2S MS | Ray, Nora, Nora Body Fire, Crew Helmet, Fire Line | E | late afternoon, smoke-red sun | Ray (screen-left) hands Nora (screen-right) a drip torch; both in profile; Nora takes it with one sharp nod, mouth closed. | (Ray) "Hale, torch. Burn it before it gets here." | 8 | native: Ray | Plan: burnout |
| FL-06 | 4s | ECU | Nora Body Fire, Fire Line | E | late afternoon | The drip torch dribbles a line of flame into dry grass, left to right. | (no dialogue, torch hiss) | 0 | none | Fight fire with fire |
| FL-07 | 6s | MCU | Nora, Nora Body Fire, Crew Helmet, Fire Line | E | late afternoon, smoke | Walking the torch, Nora answers a rookie off-frame. | (post-VO rookie) "We're lighting more fire?" (Nora) "Burn the fuel before it does. The black can't burn twice." | 15 | native: Nora · post: rookie | Plant: "can't burn twice" |
| EL-07 | 6s | WS | Eli, Eli Bike, Eli Pack, Ridge Road | E | late afternoon, ember rain | Eli pedals left to right through drifting embers; a spot fire flares in the dry grass beside the road; he swerves, wobbles, and keeps pedaling into the smoke. | (no dialogue, crackle, his ragged breath) | 0 | none | Cross-cut · he's riding into it |
| FL-08 | 8s | EWS long lens | Fire Line | G | dusk, smoke-red sun | Long lens, heat shimmer: the burnout races uphill into a crown fire coming down the canyon; the two walls meet and tear upward into one towering column. | (no dialogue, roar, the crew falls silent) | 0 | none | RH · the walls meet |
| FL-09 | 4s | WS low angle | Fire Line | G | dusk | A fire whirl spins up off the burnout edge, a twisting column of flame and ash. | (no dialogue, freight-train roar) | 0 | none | Escalation |
| FL-10 | 6s | MS | Ray, Fire Line | E | dusk, heat blast | Ray shoves crew back from the edge as heat blasts their faces. | (Ray) "Whirl! Back off the edge! Everybody back! Hale, kill the torch, now!" | 12 | native: Ray | Danger |
| FL-11 | 4s | EWS | Fire Line | G | dusk | A red air tanker drops a cloud of red retardant across the ridge above the crew. | (no dialogue, engine roar) | 0 | none | Spectacle |
| FL-12 | 6s | MS | Nora, Nora Body Fire, Crew Helmet, Fire Line | E | dusk | Nora stands drenched in pink retardant, coughing out a laugh; the crew laughs around her. | (post-VO crew) "Hey, Hale, you're pink!" (Nora) "Put it on my tab. The bank takes anything." | 13 | native: Nora · post: crew | Midpoint · false victory |

## 4. Midpoint — the wind turns (2:29–2:58)

| Clip | Dur | Shot | Ref | SF | Light | Visual | Dialogue | Words | Voice | Beat |
|---|---|---|---|---|---|---|---|---|---|---|
| MP-01 | 4s | ECU | Fire Line | G | dusk | Dry grass on the ridge suddenly lays down the other way. | (no dialogue, wind rising, laughter drops out) | 0 | none | Turn |
| MP-02 | 4s | MCU | Nora, Nora Body Fire, Crew Helmet, Fire Line | E | dusk, wind | Nora turns to Ray off-frame, pointing at the grass. | (Nora) "Cap. The grass. It's laying down uphill." | 7 | native: Nora | She sees it first |
| MP-03 | 8s | EWS | Ray, Fire Line | E | dusk, blood-orange sun | The column leans; embers stream over the ridge into the valley behind the crew. | (Ray) "She's spotting over the top! Packs on, tools up! Everybody to the trucks, now! Lookouts, you're last off!" | 18 | native: Ray | RH · fire jumps the ridge |
| MP-04 | 6s | Track handheld | Nora, Nora Body Fire, Crew Helmet, Fire Line | E | dusk, smoke | The crew runs downhill along the line as spot fires bloom in the grass on both sides. | (no dialogue, roar, breath, radios) | 0 | none | Escape |
| FL-13 | 6s | MS | Nora, Nora Body Fire, Crew Helmet, Fire Line | E | dusk, smoke | A rookie turns back for a dropped saw; Nora hauls him back by his pack strap. | (Nora) "Leave it! You never go back on a fire. Not for anything." | 12 | native: Nora | Plant: the rule (title) |
| MP-05 | 6s | EWS | Staging Area | G | dusk, smoke, orange | Long lens: a line of crew trucks races right to left down a dirt road while the fire runs along the ridge above them, faster than the trucks. | (no dialogue, engines, roar) | 0 | none | Retreat · the fire outruns them |

## 5. Eli at the barn (cross-cut, 2:58–3:17)

| Clip | Dur | Shot | Ref | SF | Light | Visual | Dialogue | Words | Voice | Beat |
|---|---|---|---|---|---|---|---|---|---|---|
| EL-03 | 6s | WS | Eli, Eli Bike, Eli Pack, Keller Barn | E | dusk, smoky orange | Eli drops his bike at Keller's lane gate; an empty farmyard, a red barn; embers drift past. | (Eli) "Mr. Keller? It's Eli Hale! I'm here to buy her back! I've got forty dollars!" | 15 | native: Eli | Alone |
| EL-04 | 4s | ECU | Keller Barn | G | dusk, smoky orange | An empty horse trailer by the barn, ramp dented by hoof kicks, a snapped lead rope swinging from the tie ring. | (no dialogue, wind) | 0 | none | Why she's alone |
| EL-05 | 6s | MCU | Eli, Juniper, Keller Barn | E | dim barn, orange slats | Blind spot: Eli frame-left, forehead pressed to the mare's face; frame-right, smoke curls in under the door behind him. | (Eli) "Hey, girl. Hey. I told you. I told you I'd come back." | 12 | native: Eli | Danger rising |
| EL-06 | 6s | CU | Eli, Keller Barn | E | dim barn, orange slats | Eli holds a phone to his ear, watching the smoke under the door; near the end a crash behind him and the mare screams; Eli spins toward the sound and the line goes dead. Minimal ambience (full audio reused in RR-04). **Edit:** here only to "I'm at Keller's." then smash to EM-01. | (Eli) "Nora, it's me. I'm at Keller's. Don't be mad. I couldn't leave—" | 12 | native: Eli | RH · voicemail cut off (question held) |

## 6. Eli is missing (3:17–3:36)

| Clip | Dur | Shot | Ref | SF | Light | Visual | Dialogue | Words | Voice | Beat |
|---|---|---|---|---|---|---|---|---|---|---|
| EM-01 | 6s | WS | Ray, Staging Area | E | dusk, orange sky | At the staging area, crew trucks idle; the radio on Ray's chest crackles; Nora by her truck. | (post-VO Walt, radio) "Walt Pruitt, county volunteers. Hale boy with you? He biked up Ridge Road at four." | 15 | post: Walt (radio) | RH · Eli missing |
| EM-02 | 4s | CU | Nora, Nora Body Fire, Crew Helmet, Staging Area | E | dusk, orange | Nora, soot and pink retardant on her face, freezes with her hand on the truck door. | (no dialogue) | 0 | none | Shock |
| EM-03 | 8s | MS | Nora, Nora Body Fire, Crew Helmet, Staging Area | E | dusk, orange | Opens on her hand leaving the truck door; Nora strides to Ray and grabs the radio off his chest. | (Nora) "Walt, it's Nora. Which way was he headed?" (post-VO Walt, radio) "Keller's place. Had a halter and rope over his shoulder." | 18 | native: Nora · post: Walt (radio) | Stakes |
| EM-04 | 4s | ECU | Nora, Nora Body Fire, Crew Helmet | E | fire glow on face | Nora's eyes go to the burning ridge. | (no dialogue) | 0 | none | Decision forming |

## 7. The choice (3:36–4:13)

| Clip | Dur | Shot | Ref | SF | Light | Visual | Dialogue | Words | Voice | Beat |
|---|---|---|---|---|---|---|---|---|---|---|
| CH-01 | 8s | OTS→Ray low angle | Ray, Nora Body Fire, Staging Area | E | dusk, orange | Over Nora's shoulder: Ray (screen-left) steps in front of her truck door. | (Ray) "Nora. Truck's not getting past the switchbacks. You go up there tonight, I lose two Hales. And you're off my crew." | 21 | native: Ray | Antagonist of choice · the paycheck is the house |
| CH-02 | 4s | CU 85mm | Nora, Nora Body Fire, Crew Helmet, Staging Area | E | dusk, orange | Nora doesn't blink. | (Nora) "Move, Ray. I'm not asking twice." | 6 | native: Nora | Choice |
| CH-03 | 6s | OTS→Ray dolly-in | Ray, Nora Body Fire, Staging Area | E | dusk, orange | Slow push in on Ray over Nora's shoulder; his voice drops. | (Ray) "Nine years ago your mother said that to me. Same two words. Move, Ray." | 14 | native: Ray | Reveal |
| CH-04 | 4s | ECU | Nora Body Fire, Ray | E | dusk | Nora presses her handheld radio into Ray's palm; his fingers close on it. | (no dialogue) | 0 | none | Cuts the cord |
| CH-05 | 6s | OTS→Nora | Nora, Nora Body Fire, Crew Helmet, Nora Pickup, Staging Area | E | dusk, orange | Opens on Ray's eyes dropping to the radio; Nora steps around him, yanks the truck door open and looks back. | (Nora) "Then hang on to this. I'm coming back for it. With him." | 12 | native: Nora | Promise |
| CH-06 | 4s | WS | Ray, Staging Area | E | dusk, orange | Opens on the door swinging; Nora climbs in; Ray shouts after her. | (Ray) "Hale! Get out of that truck! Nora!" | 7 | native: Ray | Order broken |
| CH-07 | 6s | EWS high angle | Ray, Nora Pickup, Staging Area | E | dusk, orange | The pickup tears out left to right toward the burning ridge; Ray stands alone in its dust. | (no dialogue, engine roar) | 0 | none | Break |
| CH-09 | 6s | MCU | Ray, Staging Area | E | dusk, orange | Ray lifts his own radio, eyes on the ridge. | (Ray) "Dispatch, Duran. One of mine is past the closure on Ridge Road. Hale." | 13 | native: Ray | Ray covers her (L-cut into RR-01) |

## 8. Ridge Road (4:13–4:42)

| Clip | Dur | Shot | Ref | SF | Light | Visual | Dialogue | Words | Voice | Beat |
|---|---|---|---|---|---|---|---|---|---|---|
| RR-01 | 8s | EWS | Nora Pickup, Ridge Road | G | night-orange, embers | A small pickup climbs left to right between burning pines on both sides; embers stream across the road. | (no dialogue, wind roar) | 0 | none | RH · into the fire |
| RR-02 | 4s | WS | Ridge Road | G | night-orange, headlights | In the headlights, a burning pine crashes across the road. | (no dialogue, crash) | 0 | none | Blocked |
| RR-04 | 6s | MCU passenger side | Nora, Nora Body Fire, Nora Pickup | E | cab lit orange, truck stopped | From the passenger seat of the stopped truck, Nora holds her phone to her ear; her breath stops mid-inhale; her knuckles whiten on the wheel. | (no dialogue; Eli's FULL voicemail from EL-06 plays in the edit — first time we hear the end: "Don't be mad. I couldn't leave—", a crash, the mare screams, dead line) | 0 | none | Voicemail lands · new information |
| RR-06 | 4s | CU | Nora, Nora Body Fire, HALE Helmet, Nora Pickup | E | cab lit orange | Nora grabs the yellow HALE helmet off the passenger seat and buckles it on in one move. | (no dialogue) | 0 | none | Prop pays · becomes her mother |
| RR-07 | 6s | MS | Nora, Nora Body Fire, HALE Helmet, Nora Pickup, Ridge Road | E | night-orange | Nora steps out into the wind, leaving the door open, and pulls her goggles down; the truck radio crackles. Her mouth stays closed. | (post-VO Ray, truck radio) "Hale, answer me. The whole ridge is going up. Nora, turn around." | 12 | post: Ray (radio) | Hook source |
| RR-08 | 6s | Track handheld-leading | Nora, Nora Body Fire, HALE Helmet, Ridge Road | E | night-orange, smoke | Nora runs left to right up the smoky road on foot; flames climb the pines in the background. | (no dialogue, roar and breath) | 0 | none | Ordeal |

## 9. Cedar Flat — the last line (cross-cut, 4:42–5:01)

| Clip | Dur | Shot | Ref | SF | Light | Visual | Dialogue | Words | Voice | Beat |
|---|---|---|---|---|---|---|---|---|---|---|
| LH-01 | 6s | EWS | Cedar Flat | G | night, fire glow on the ridge | Headlights of evacuating cars stream right to left out of a small town; above the rooftops the ridge glows orange. | (post-VO Dispatch, radio) "All units, Cedar Flat is now mandatory evacuation. Fire is two miles out." | 13 | post: Dispatch (radio) | RH · B-story · the town is next |
| LH-02 | 6s | MS low angle | Ray, Cedar Flat | E | night, orange glow, work lights | Ray (white helmet) stands on a fresh dozer line between the last houses and the brush; his crew digs behind him. | (Ray) "Last line. Behind us, a school and three hundred homes. Nobody leaves." | 12 | native: Ray | Ray's stakes |
| LH-03 | 4s | ECU | Ray, Cedar Flat | E | night, orange glow | Two radios on Ray's chest harness, his own and Nora's; his thumb rests on hers. | (no dialogue, static hiss) | 0 | none | He's carrying her promise |
| LH-04 | 6s | MS | Cedar Flat | G | night, ember rain | On a ladder at the edge of town, a firefighter hoses down a smoking shake roof as embers rain; a dog barks in an empty yard below. | (no dialogue, hose, barking, wind) | 0 | none | Pressure on the town |

## 10. Ridge Road — the trail (5:01–5:21)

| Clip | Dur | Shot | Ref | SF | Light | Visual | Dialogue | Words | Voice | Beat |
|---|---|---|---|---|---|---|---|---|---|---|
| RR-13 | 6s | WS low angle | Nora, Nora Body Fire, HALE Helmet, Ridge Road | E | night, crown fire overhead | Crown fire: flames leap from treetop to treetop across the road above her; a burning limb drops across the road a few steps ahead; Nora drops flat, then scrambles up and on under the burning canopy. | (no dialogue, crown-fire roar, limb crash) | 0 | none | Spectacle · near miss |
| RR-14 | 4s | ECU | Nora Body Fire, Ridge Road | E | night-orange, ash on the road | Nora's gloved hand brushes ash off a thin bicycle-tire track pressed into the road. | (no dialogue, wind, her breath catches) | 0 | none | Clue · he came this way |
| RR-10 | 4s | CU low angle | Eli Bike, Keller Barn | G | night-orange | Eli's bike lies dumped at Keller's lane gate, front wheel still turning. | (no dialogue, bike freewheel ticking) | 0 | none | RH · evidence |
| RR-11 | 6s | MS | Nora, Nora Body Fire, HALE Helmet, Keller Barn | E | night-orange, smoke | Nora stands at the gate and shouts into the smoke. | (Nora) "Eli! Eli Hale! I got your message! I'm not mad! I'm not mad!" | 13 | native: Nora | Search |
| RR-12 | 4s | WS | Nora, Nora Body Fire, HALE Helmet, Keller Barn | E | night, smoke, orange | A horse screams; Nora turns; a red barn roof shows through the smoke. | (no dialogue) | 0 | none | Found |

## 11. The barn (5:21–6:25)

| Clip | Dur | Shot | Ref | SF | Light | Visual | Dialogue | Words | Voice | Beat |
|---|---|---|---|---|---|---|---|---|---|---|
| BN-01 | 8s | EWS | Nora, Nora Body Fire, HALE Helmet, Keller Barn | E | night, smoke rolling, embers | Smoke rolls off the red barn's roof; Nora runs left to right across the yard and through the open door. | (no dialogue, roar) | 0 | none | Arrival |
| BN-02 | 6s | MS | Eli, Eli Pack, Juniper, Keller Barn | E | night, orange through slats, smoke | Inside, Eli tears at a knotted tie rope, his own halter in his other hand, while the mare spins and rears. | (Eli) "Easy, girl! I'll give you all my apples! Just hold still! Please!" | 12 | native: Eli | Danger |
| BN-03 | 4s | MCU | Nora, Nora Body Fire, HALE Helmet, Keller Barn | E | night, orange, smoke | Nora pushes her goggles up, grabs Eli's shoulder and spins him around. | (Nora) "Drop the rope. We're leaving. Right now." | 7 | native: Nora | Order |
| BN-04 | 8s | 2S profile | Eli, Nora, Nora Body Fire, HALE Helmet, Juniper, Keller Barn | E | night, orange, smoke | Opens on Nora's grip on his shoulder; Eli wrenches free and plants himself between her and the horse, both in profile. | (Eli) "You go. You're good at going." (Nora) "Leave the horse, Eli. Now." (Eli) "Like you left her at the trailer?" | 18 | native: Eli (fenrir) + Nora (kore) | Conflict peak · "good at going" pays |
| BN-05 | 8s | OTS→Eli Dutch | Eli, Nora Body Fire, Keller Barn | E | night, orange, smoke | Over Nora's shoulder, slight Dutch tilt: face to face, both shouting over the roar. | (post-VO Nora, back to camera) "I sold her so we could keep the house!" (Eli) "You sold her because she looks at you like Mom did." | 20 | native: Eli · post: Nora | Truth |
| BN-06 | 4s | CU | Nora, Nora Body Fire, HALE Helmet, Keller Barn | E | night, orange flicker | Nora goes still; a line cuts through the soot on her cheek. | (no dialogue, roar drops away) | 0 | none | Hit |
| BN-07 | 4s | WS | Keller Barn | G | night, flames on rafters | Flames run along the rafters; burning hay drops into the aisle. | (no dialogue) | 0 | none | RH · roof catches |
| BN-08 | 4s | ECU | Nora Body Fire, Juniper, Keller Barn | E | night, flames overhead | Nora's knife saws through the knotted tie rope. | (no dialogue) | 0 | none | First yield |
| BN-09 | 6s | MCU | Nora, Nora Body Fire, HALE Helmet, Keller Barn | E | night, flames overhead | Nora sheathes the knife; behind her Eli buckles his halter onto the mare. | (Nora) "Fine. She comes. But you hold my hand and you don't let go." | 13 | native: Nora | First yield |
| BN-10 | 4s | CU | Eli, Juniper, Keller Barn | E | night, flames overhead | Eli's hands clip the lead rope onto the halter. | (no dialogue) | 0 | none | Halter pays |
| BN-11 | 6s | MCU (Nora) | Nora, Nora Body Fire, HALE Helmet, Juniper, Keller Barn | E | night, flames overhead | Nora ties her red bandana over the mare's eyes. | (Nora) "Horses won't leave a burning barn. They think it's home. Hold her tight." | 13 | native: Nora | Skill |
| BN-12 | 4s | CU (Eli) | Eli, Keller Barn | E | night, flames overhead | Eli goes still, lips parted, the lead slack in his hand. | (Eli) "How do you know that?" (post-VO Nora, off-screen) "Mom." | 6 | native: Eli · post: Nora | Mother |
| BN-13a | 4s | WS static | Nora, Nora Body Fire, Eli, Juniper, Keller Barn | E | night, fire behind, smoke | The three walk fast out of the barn door, right to left, Eli leading the blindfolded mare. | (no dialogue, roar) | 0 | none | Escape |
| BN-13b | 4s | WS static | Nora, Nora Body Fire, Eli, Juniper, Keller Barn | P | night, sparks | Same frame: behind them the barn roof collapses in a burst of sparks; they don't look back. | (no dialogue, crash) | 0 | none | No way back |

## 12. Out of the barn (6:25–6:47)

| Clip | Dur | Shot | Ref | SF | Light | Visual | Dialogue | Words | Voice | Beat |
|---|---|---|---|---|---|---|---|---|---|---|
| ES-01 | 6s | Track handheld-leading | Nora, Nora Body Fire, HALE Helmet, Eli, Juniper, Ridge Road | E | night, fence lines burning | They run right to left down Keller's lane between burning fence posts, Nora gripping Eli's hand, Eli leading the blindfolded mare. | (no dialogue, roar, hooves, breath) | 0 | none | Escape |
| ES-02 | 4s | WS | Nora, Nora Body Fire, HALE Helmet, Eli, Juniper, Ridge Road | E | night, fire glow | A burning fence rail collapses across the lane in front of them; the mare shies and pulls back on the rope. | (no dialogue, crack, horse squeal) | 0 | none | Obstacle |
| ES-03 | 6s | MCU | Nora, Nora Body Fire, HALE Helmet, Ridge Road | E | night, fire glow | Nora kicks the burning rail aside with her boot and shouts back over her shoulder. | (Nora) "Keep her moving! Eyes on my back! Don't stop for anything, Eli!" | 12 | native: Nora | Command |
| ES-04 | 4s | CU | Eli, Ridge Road | E | night, fire glow, smoke | Eli, shirt pulled over his mouth, coughing, clutches the lead rope and keeps walking. | (no dialogue, coughing) | 0 | none | He holds on |
| ES-05 | 6s | WS high angle | Nora, Nora Body Fire, HALE Helmet, Eli, Juniper, Ridge Road | E | night, embers | Embers land in the dry grass ahead; flames race across the lane below them and cut off the way down; Nora turns them uphill. | (no dialogue, whoosh, roar) | 0 | none | RH · way down cut off |

## 13. Cedar Flat — slopover (cross-cut, 6:47–7:09)

| Clip | Dur | Shot | Ref | SF | Light | Visual | Dialogue | Words | Voice | Beat |
|---|---|---|---|---|---|---|---|---|---|---|
| LH-05 | 8s | EWS long lens | Cedar Flat | G | night, heat shimmer | Long lens, heat shimmer: the fire front crests the last ridge above Cedar Flat and pours downhill toward the dozer line and the rooftops. | (no dialogue, roar) | 0 | none | RH · the fire reaches the town |
| LH-06 | 6s | MS | Ray, Cedar Flat | E | night, orange, embers | A spot fire jumps the dozer line into a backyard; Ray points and shouts at the crew. | (Ray) "Slopover! Right flank! Engine Two, hit it! Hit it now before it finds the houses!" | 15 | native: Ray | Line breaks |
| LH-07 | 6s | WS | Cedar Flat | G | night, orange, spray | An engine crew blasts the backyard flames with a hose; the fire dies to smoke beside a child's swing set; town lights still burn behind. | (no dialogue, hose roar, hiss) | 0 | none | Line holds — for now |
| LH-08 | 6s | MCU | Ray, Cedar Flat | E | night, orange | Ray, soot on his face, looks up at the burning ridge where Ridge Road is. | (post-VO crew, off-screen) "Cap, Hale's truck radio is just static." (Ray) "She'll answer. Hales always answer late." | 13 | native: Ray · post: crew | Ray's faith |

## 14. All is lost (7:09–7:47)

| Clip | Dur | Shot | Ref | SF | Light | Visual | Dialogue | Words | Voice | Beat |
|---|---|---|---|---|---|---|---|---|---|---|
| LS-01 | 8s | EWS | Nora, Nora Body Fire, Eli, Juniper, Ridge Road | E | night, fire both sides | On a rise, the three stop: fire fills the road below and the slopes to both sides. | (no dialogue, roar) | 0 | none | RH · trapped |
| LS-02 | 6s | MS | Nora, Nora Body Fire, HALE Helmet, Ridge Road | E | night, fire glow | Nora rips the shelter pouch off her belt and shakes the foil out toward Eli. | (Nora) "Shake it out. Step in. Face down. Feet to the fire. It fits one." | 14 | native: Nora | All is lost · shelter pays (1) |
| LS-03 | 8s | OTS→Eli | Eli, Nora Body Fire, Ridge Road | E | night, fire glow | Over Nora's shoulder: Eli won't take the foil. | (Eli) "And you?" (post-VO Nora, back to camera) "I'll be right here. I'll lie on top of you." (Eli) "That's what Mom said. Isn't it?" | 18 | native: Eli · post: Nora | Dark night |
| LS-04 | 4s | CU | Nora, Nora Body Fire, HALE Helmet, Ridge Road | E | night, fire glow | Nora's lips part with no sound; she swallows twice and looks at the fire. | (no dialogue, roar drops away) | 0 | none | Broken |
| LS-05a | 4s | WS low angle | Juniper, Eli, Ridge Road | E | night, fire glow | The mare shakes off the blindfold and rears. | (no dialogue) | 0 | none | Twist |
| LS-05b | 4s | WS low angle | Juniper, Eli, Ridge Road | P | night, fire glow | Same frame: she yanks the rope out of Eli's hand and bolts uphill, right to left, out of frame. | (no dialogue, hooves) | 0 | none | Twist |
| LS-06 | 6s | EWS 85mm | Juniper, The Black | E | night, smoke, orange edge | Far away, the grey mare gallops uphill right to left through the smoke toward a dark slope. | (no dialogue, hooves) | 0 | none | Horse knows |
| LS-07 | 4s | MCU | Eli, Ridge Road | E | night, fire glow | Eli points after her. | (Eli) "Nora! She's heading for the burned side!" | 7 | native: Eli | Idea |

## 15. Trust (7:47–8:23)

| Clip | Dur | Shot | Ref | SF | Light | Visual | Dialogue | Words | Voice | Beat |
|---|---|---|---|---|---|---|---|---|---|---|
| TR-01 | 8s | 2S profile | Eli, Nora, Nora Body Fire, HALE Helmet, Ridge Road | E | night, fire glow | Eli grabs Nora's arm, pointing up the slope; both in profile, faces lit orange. | (Eli) "Nora, she's done this before. The Pine Gulch burn. She walks where it's already burned." (Nora) "Horses run from fire." | 19 | native: Eli (fenrir) + Nora (kore) | Argument · Pine Gulch pays |
| TR-02 | 6s | MCU (Eli) | Eli, Ridge Road | E | night, fire glow | Eli's breathing slows; he plants his feet and holds her eyes. | (Eli) "You said they won't leave a burning barn. She left. She ran uphill." | 13 | native: Eli | Ask |
| TR-03 | 4s | ECU | Nora, Nora Body Fire, HALE Helmet | E | night, fire glow | Nora's jaw unclenches; her eyes track the horse's path up the dark slope; a long exhale. | (Nora, whisper) "The black. It can't burn twice." | 6 | native: Nora | Change · the black pays |
| TR-04 | 4s | CU | Nora Body Fire, Eli | E | night, fire glow | Eli holds out his open hand; Nora looks at it, swallows once, and takes it. | (no dialogue) | 0 | none | Trust |
| TR-05 | 4s | MS axis flip | Eli, Nora Body Fire, Ridge Road | E | night, fire glow, smoke | Opens on the hand grip; Eli turns uphill first, pulling his sister after him. | (Eli) "My turn. Hold on and don't let go." | 8 | native: Eli | Role reversal |
| TR-06 | 6s | Static low angle | Nora, Nora Body Fire, HALE Helmet, Eli, The Black | E | night, smoke, orange | Hand in hand they run right to left past camera, uphill through the smoke after the grey shape of the horse, Eli in front. | (no dialogue, roar and breath, Theme A in full) | 0 | none | Climax run |
| TR-07 | 4s | WS | Nora, Nora Body Fire, HALE Helmet, Eli, Ridge Road | E | night, smoke, orange | A burning snag topples across the slope; Eli yanks Nora sideways out of its path as it hits the ground in a burst of sparks. | (no dialogue, crack, crash) | 0 | none | RH · he saves her |
| TR-08 | 6s | MCU | Nora, Nora Body Fire, HALE Helmet, Eli, Ridge Road | E | night, sparks | Nora is down on one knee; Eli hauls her up by the arm. | (Eli) "Get up! You told me don't let go. So you don't let go either!" | 14 | native: Eli | Role reversal in action |

## 16. The black — burnover (8:23–9:30)

| Clip | Dur | Shot | Ref | SF | Light | Visual | Dialogue | Words | Voice | Beat |
|---|---|---|---|---|---|---|---|---|---|---|
| BK-01 | 8s | EWS | Nora, Nora Body Fire, Eli, Juniper, The Black | E | night, smoke thinning, dark | They crest onto a blackened slope of burned grass and charred stumps; the mare stands in the middle. | (no dialogue, wind) | 0 | none | Arrival |
| BK-02 | 4s | MS | Nora, Nora Body Fire, HALE Helmet, The Black | E | night, distant glow | Nora kneels and presses her palm into the ash. | (Nora) "Cold. It's cold. Eli, she found it." | 7 | native: Nora | Payoff |
| BK-03 | 8s | WS | Nora, Nora Body Fire, HALE Helmet, Juniper, The Black | E | night, fire wall at the edge | The fire front roars along the edge of the black; Nora pulls Eli down against the mare's legs. | (Nora) "Down! Face in the dirt! Shirt over your mouth! Don't look up. Count your breaths. I'm counting with you." | 19 | native: Nora | Climax · RH · fire front |
| BK-04 | 4s | CU | Nora, Nora Body Fire, HALE Helmet, Eli, The Black | E | night, fire glow | Nora takes off the yellow HALE helmet and puts it on Eli's head. | (no dialogue) | 0 | none | Gift |
| BK-05 | 6s | MS | Nora, Nora Body Fire, The Black | E | night, fire glow | Nora pulls the fire shelter over Eli and herself, fists pinning its edges into the ash, the foil rippling orange. | (Nora) "It fits one person. Out here in the black, it fits two." | 12 | native: Nora | Shelter pays (2) |
| BK-14 | 6s | EWS long lens | The Black | G | night, burnover | Burnover: a wall of flame and a storm of embers sweeps across the edge of the black; a small silver shelter lies glowing in the middle, the grey mare's shape lying beside it. | (no dialogue, burnover roar like a jet engine) | 0 | none | Spectacle · peak danger |
| BK-06 | 4s | ECU | Nora, Eli | E | orange light through foil | Under the foil, their faces inches apart. | (no dialogue, Sonic Isolation: fire cuts to two heartbeats and breathing) | 0 | none | Silence |
| BK-07 | 6s | MCU (Eli) | Eli, HALE Helmet | E | orange light through foil | Under the foil, the roar outside, Eli touches the helmet on his head and whispers to his sister off-frame. | (Eli) "That's Mom's. Were you there when she went back?" (post-VO Nora, off-screen) "I was your age." | 13 | native: Eli · post: Nora | RH · origin revealed at peak danger |
| BK-15 | 4s | ECU | Nora Body Fire | E | orange light through foil | Wind lifts the edge of the foil; Nora's gloved fist slams it back down into the ash. | (no dialogue, roar surges, foil snapping) | 0 | none | Danger keeps pressing |
| BK-11 | 6s | MCU (Eli) | Eli, HALE Helmet | E | orange light through foil | Still under the foil, Eli turns his face toward his sister. | (Eli) "Mom went back in. You came back out. With both of us." | 12 | native: Eli | Misbelief broken |
| BK-12 | 4s | CU | Nora, Nora Body Fire | E | orange light through foil | Under the foil, a broken laugh shakes Nora's shoulders; tears cut lines through the soot. | (no dialogue, the roar starts to fade) | 0 | none | Release |
| BK-16 | 4s | ECU | Nora Body Fire, Eli | E | orange light through foil | Under the foil, Eli's hand finds his sister's gloved hand in the ash and squeezes; she squeezes back. | (no dialogue, the roar fades to wind) | 0 | none | Together |
| BK-08 | 4s | WS | Nora, Nora Body Fire, Juniper, The Black | E | night, glow fading, smoke | Nora throws back the scorched foil; a few steps away the grey mare lies still in the ash. | (no dialogue, silence, crackle) | 0 | none | Last scare: is she dead? |
| BK-09 | 4s | CU | Juniper, Nora Body Fire, The Black | E | night, glow fading | The lying mare lifts her head and nudges Nora's shoulder. | (no dialogue, a soft snort) | 0 | none | Forgiveness · the look pays |
| BK-13 | 6s | MS | Nora, Nora Body Fire, Eli, HALE Helmet, Juniper, The Black | E | night, ember glow | Eli sleeps against the mare's side under the helmet; Nora, awake, holds his hand and watches the embers. Dissolve to dawn. | (no dialogue, breathing and crackle) | 0 | none | Rest |

## 17. Dawn (9:30–10:21)

| Clip | Dur | Shot | Ref | SF | Light | Visual | Dialogue | Words | Voice | Beat |
|---|---|---|---|---|---|---|---|---|---|---|
| DW-01 | 8s | EWS | Ray, The Black | E | grey dawn, ash falling | Ash falls like snow over black hills; a line of yellow-shirted firefighters, a white helmet in front, walks up the slope. | (no dialogue, footsteps, wind) | 0 | none | RH · rescue |
| DW-02 | 4s | CU | Ray, The Black | E | grey dawn | Ray spots something uphill, stops, then breaks into a run. | (no dialogue) | 0 | none | Found |
| DW-03 | 6s | OTS→Nora | Nora, Nora Body Fire, The Black | E | grey dawn | Over Ray's shoulder: Nora stands up from the ash beside Eli and the mare; hoarse, smoke-ruined voice. | (post-VO Ray, back to camera) "Nora." (Nora) "Captain. Brought him back. Like I said. Plus one stubborn horse." | 12 | native: Nora · post: Ray | Promise kept |
| DW-04 | 4s | MCU (Ray) | Ray, The Black | E | grey dawn | Ray holds out her radio and a thermos cup. | (Ray) "Think you came back for this." | 6 | native: Ray | Return |
| DW-05 | 6s | 2S locked-off 85mm | Ray, Nora Body Fire, The Black | E | grey dawn | Ray screen-left, Nora screen-right: she takes the radio and drinks the coffee, the cup covering her mouth; Ray keeps a straight face. | (Ray) "I should write you up, Hale." (post-VO Nora, behind the cup) "Write it up." (Ray) "Lost my pen." | 12 | native: Ray · post: Nora | Rule bends |
| DW-06 | 8s | EWS | Cedar Flat | G | grey dawn, ash falling | From high on the black slope, far below: Cedar Flat stands, rooftops intact; the burned ground stops at the dozer line. | (post-VO Ray) "Town held, Hale. We lost two barns and a mile of fence. Not one house. Not one person." | 18 | post: Ray | B-story pays · the town held |
| DW-07 | 8s | OTS→Nora | Nora, Nora Body Fire, Juniper, The Black | E | dawn, first sun | Over Eli's shoulder: Nora picks up the lead rope and puts it in his hands. | (Nora) "She's yours. I'll call Keller. We'll figure out the money." (post-VO Eli, back to camera) "I'll sell my bike." (Nora) "Genius, your bike's at Keller's gate." | 20 | native: Nora · post: Eli | Resolution |
| DW-08 | 4s | CU | Ray, The Black | E | dawn, first sun | Ray sees the yellow HALE helmet on the boy's head, smiles and mutters to himself. | (Ray, quietly) "Most stubborn Hale left alive. Figures." | 6 | native: Ray | Ray's peace |
| DW-09 | 10s | EWS | Nora, Nora Body Fire, Eli, HALE Helmet, Juniper, The Black | E | sunrise through ash | Eli, wearing the helmet, leads the mare down the black slope right to left; Nora walks one step behind them as ash drifts in the first sun. | (no dialogue, silent ending, wind and hooves) | 0 | none | Final image |

## 18. Plants → payoffs

| Plant | Where | Pays off |
|---|---|---|
| "You never go back on a fire" (title rule) | HK-11, FL-13 | CH-02, RR-07 (she breaks it) · BK-11 (she came back *out*) |
| Eli's voicemail | EL-06 (cut off at "I'm at Keller's") | RR-04 (full: crash, scream, dead line) |
| "My mother did. Once." | FL-02 | BK-07 "I was your age." (under the foil) |
| "You're good at going" | RA-05 | BN-04 (Eli throws it back) |
| Pine Gulch burn | RA-02 | TR-01 (the horse knows the black) |
| The black / "can't burn twice" | FL-01, FL-07 | TR-03, BK-02, BK-05 |
| Fire shelter / "My mother did. Once." | FL-02 | LS-02 "fits one" → BK-05 "fits two" |
| The look (Juniper ↔ Nora) | RA-03 | BN-05 truth · BK-09 nudge |
| HALE helmet | RA-07 | RR-06 → BK-04 → DW-08 (Ray) → DW-09 |
| Halter | RA-08, EM-03 | BN-09/10 |
| "Move, Ray" | HK-07, CH-02 | CH-03 (mother said it) |
| Radio | CH-04/05 → LH-03 (on Ray's chest) | DW-04 |
| "Hold my hand and don't let go" | BN-09 | TR-05 "My turn" → TR-08 (Eli saves her) → BK-16 |
| Cedar Flat / "the town is next" | HK-03, RA-07, FL-01 | LH-01→08 (B-story) → DW-06 "Not one house" |
| Eli's bike | RA-09, EL-03, RR-14 (track), RR-10 | DW-07 joke |

## 19. Retention map

| Time | Beat | Why the viewer stays |
|---|---|---|
| 0:00 | Hook: "Do not go back in there" | conflict in 3 s |
| 0:04 | "He biked up Ridge Road at four." | premise: her brother is in the fire |
| 0:10–0:32 | crown fire · backfire · walls meet · retardant · "Move, Ray" · tree · barn · shelter | spectacle + three open questions (does she go? is he alive? who is the shelter for?) |
| 0:35 | button: "You never go back on a fire." | irony — she is about to break her own rule |
| 1:07 | dispatch: evacuation for Keller Lane | the horse's new home is in the fire's path |
| 1:21–2:29 | ember storm → burnout → Eli rides through embers → walls meet → fire whirl → retardant | a spectacle beat every 15–25 s; Eli cross-cut twice |
| 2:36 | wind turns, fire jumps the ridge; trucks outrun by the fire | false victory flips |
| 3:12 | Eli's voicemail cut off at "I'm at Keller's" | dramatic irony: we know, she doesn't — and we don't hear the end |
| 3:17 | Walt: "He biked up Ridge Road at four." | hook line pays — the cold open catches up |
| 4:13–4:42 | Ridge Road: full voicemail (crash, scream, dead line) · helmet on | new information |
| 4:42–5:01 | **Cedar Flat B-story:** mandatory evacuation, "Nobody leaves", her radio on Ray's chest | second clock: the town — and someone still holds her promise |
| 5:01–5:21 | limb near miss · bike track · bike wheel | ordeal + evidence every 10 s |
| 5:21–6:25 | barn fight, roof collapses | conflict peak + "good at going" |
| 6:25–6:47 | **escape:** burning lane, falling rail, way down cut off | the barn was not the end — new danger |
| 6:47–7:09 | **Cedar Flat:** fire front pours at the town, slopover knocked down, "Hales always answer late" | spectacle + the town clock + Ray's faith |
| 7:09 | trapped, "It fits one" | all is lost |
| 8:08 | **snag falls, Eli saves Nora** | role reversal in action |
| 8:23–9:30 | burnover in the black; mother reveal under the foil; foil off — is the mare dead? | climax + reveal at peak danger + last scare |
| 9:30–10:21 | dawn; Ray: "Town held. Not one house." · "Most stubborn Hale left alive." | both stories pay, silent ending |

## 20. Credits needed (for approval later — nothing generated yet)

- Hook: 11 re-cuts (R) — **0 generations**.
- Video clips to generate: **123** (51×4s · 51×6s · 20×8s · 1×10s) — v5 was 104; +19 new clips, RA-07 and BK-01 6→8s. The paper-edit tool also counts the 11 hook re-cuts (134), but they are not generated.
- Start frames: 104 E + 17 G = 121 images; 2 P (last frame: BN-13b, LS-05b), 11 R (none).
- Before anything: 4 character/creature turnaround sheets (Nora, Eli, Ray, Juniper) + 2 body sheets + 7 location refs (new: Cedar Flat) + 5 prop refs. Test FL-08 (hardest fire shot) first.

## 21. Skill review scorecard (v3 → v4), plus v5 and v6 passes

### v6 — 10-minute pass (8:45 → 10:21)

| Added | Time | Length | Why it is not filler |
|---|---|---|---|
| RA-07, BK-01 back to 8s | 1:07, 8:23 | +4 s | dispatch line now names the crews' fallback; the arrival in the black gets room to breathe before the burnover |
| EL-07 Eli rides through embers | 2:05 | +5 s | second Eli cross-cut on the line: the viewer sees he is riding into it while the crew is busy |
| MP-05 trucks outrun by the fire | 2:53 | +5 s | spectacle; shows how fast the run is, makes "nobody can go back" visual |
| LH-01→04 Cedar Flat, part 1 | 4:42 | +18.5 s | B-story opens a second clock (the town) and keeps Ray alive in the story; her radio on his chest = he still holds her promise |
| ES-01→05 escape from the barn | 6:25 | +22 s | new danger right after the barn; explains why they are trapped on a rise instead of driving out |
| LH-05→08 Cedar Flat, part 2 | 6:47 | +22 s | the fire reaches the town; slopover knocked down; "Hales always answer late" sets up dawn |
| TR-07/08 snag, Eli saves Nora | 8:08 | +8.5 s | the role reversal is acted, not just said |
| BK-16 hands under the foil | 9:13 | +3.5 s | one silent beat of closeness before the last scare |
| DW-06 the town held | 9:52 | +7 s | B-story payoff: "Not one house. Not one person." — her choice did not cost the town |

Longest gap between hooks: 60 s (LS-01 7:09 → TR-07 8:08). Cross-cuts to Cedar Flat are placed where v5 had its two weakest minutes (4:00–5:00 and after the barn).

### v5 — independent per-minute retention review (v4 scores → fix)

| Minute (v4) | v4 score | Problem | v5 fix |
|---|---|---|---|
| 0–1 | 8 | — | — |
| 1–2 | 6 | briefing-heavy morning and line | RA-07 8→6s; FL-03 cut; FL-05 8→4s ("Hale, torch.") |
| 2–3 | 7 | — | EL-06 now ends cut off (crash, scream, dead line held back) |
| 3–4 | 8 | CH-08 static | CH-08 cut |
| 4–5 | 5 | Ridge Road filler: brake, helmet in two clips, walking in smoke | RR-03, RR-05, RR-09 cut; RR-04 plays the full voicemail (new info); RR-06 one-move helmet; RR-13 near miss; new RR-14 bike track |
| 5–6 | 7 | — | — |
| 6–7 | 8 | — | — |
| 7–8 | 7 | burnover talk drifts | BK-01 8→6s, BK-02 6→4s; mother reveal moved under the foil (BK-07); new BK-15 foil fight |
| 8–9 | 5 | after the danger: two long sit-down talks (BK-08 confession, BK-10 origin) | BK-10 cut; BK-11/BK-12 under the foil; BK-08 = foil off, mare lies still (last scare) → BK-09 nudge |
| 9–end | 7 | — | DW-08 Ray line pays the helmet |

Runtime 9:17 → 8:45. Longest gap between hooks: 74 s (LS-01 → BK-03), under the 90 s limit; Ridge Road now has a new beat every 10–15 s.

### v3 → v4

| Skill | Check | v3 | v4 | What changed |
|---|---|---|---|---|
| fk-scriptwriter G2 | title + thumbnail + promise; promise pays < 0:30 | pays ~0:15 (hook) but then stalls 2:50 | pays 0:04–0:21 and again 3:14 | hook re-built as a trailer; Walt's line lands at 0:04 |
| fk-scriptwriter re-hook | gap ≤ 90 s, aim 60–90 | longest gap ~110 s (morning) | longest gap 60 s (EM-01 → RR-01); spectacle every 15–30 s on the line | morning cut 2:50 → 0:44 |
| fk-scriptwriter Quality Gate #9 | no two blocks in a row with the same shot | ok | ok (checked by tool) | — |
| trailer-intro (fk-capcut-edit) | conflict 0–3 s, premise 3–9 s, escalation, button, no spoiler, works muted | 4 clips, no premise until later | 11 pieces, premise at 0:04, button = her own rule | shelter shown without faces (no spoiler) |
| sw-story-structure | inciting ≤ 11 %, midpoint = false victory, all-is-lost ≈ 68–75 % | inciting 1:30, midpoint ok | inciting (sale + Eli leaves) 0:43–1:18; midpoint "you're pink" 2:26 (26 %); all is lost 6:16 (68 %) | midpoint earlier, it now flips into the fire jump |
| sw-genre-anatomy (disaster / survival) | the disaster grows on screen; ticking clock; the hero's skill solves the climax | fire mostly heard, not seen | fire escalates on screen 6 times; clock = "town's four miles back" + evacuation; climax solved by fire skill (the black, shelter) | — |
| sw-scene-craft | every scene turns a value | ok | ok; cut 3 static scenes (kitchen, bank envelope, signing) whose turn now happens inside RA-02 | — |
| sw-dialogue | no on-the-nose; lines are actions | ok | ok; callbacks used as weapons ("good at going", "move, Ray", "can't burn twice") | — |
| fk-action-choreography | one action per 4 s clip; physics-safe | ok | ok; big fire shots have no people close to flame (FL-08, FL-09, BK-14 long lens) | — |
| fk-camera-guide | lens plan, screen direction, no repeated scale | ok | ok; documentary long-lens grammar for the big fire | — |
| fk-cinematic-transitions | J/L-cuts, no crossfade except dawn dissolve | ok | ok; pre-laps at RA-09, CH-09 | — |
| fk-sound-design | sonic isolation at peak; −14 LUFS | ok | ok; BK-14 roar → BK-06 silence is the biggest contrast in the film | — |
| Safety (user request on looks) | — | — | Nora: very pretty, fit, moderately attractive, adult, never posed. Eli (14): clothes/age/actions only | — |
