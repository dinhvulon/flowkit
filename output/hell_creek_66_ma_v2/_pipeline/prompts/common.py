"""Shared locks + script.md parser + clip composer for Hell Creek 66 Ma v2 (fk-script-to-prompts)."""
import re
from pathlib import Path

OUT = Path("C:/flowkit/output/hell_creek_66_ma_v2")
SCRIPT = (OUT / "script.md").read_text(encoding="utf-8")

ENT = {"N": "Nora", "NB": "Nora Body", "NH": "Nora Hand", "BD": "Bò Đực", "CG": "Con Cái Già", "CN": "Con Non",
       "TR": "T. rex", "AR": "Acheroraptor", "ED": "Edmontosaurus", "BS": "Borealosuchus", "IN": "Infernodrakon",
       "CA": "Edmontosaurus Carcass", "LB": "Hell Creek Bank", "LC": "Hell Creek Game Corridor",
       "LW": "Hell Creek Waterhole"}


def _block(title):
    s = SCRIPT.index(title)
    a = SCRIPT.index("```", s) + 3
    return SCRIPT[a:SCRIPT.index("```", a)].strip()


CHAR_LOCK = _block("### 2.1 CHARACTER_LOCK")
BODY_LOCK = _block("### 2.2 BODY LOCK")
OUTFIT_LOCK = _block("### 2.3 OUTFIT LOCK")
ID_LOCK = _block("### 2.4 ID-LOCK")
BODY_LOCK_V = BODY_LOCK.replace("the Nora Body reference sheet", "{{ref:Nora Body}}")
OUTFIT_LOCK_V = OUTFIT_LOCK.replace("the Nora Body reference sheet", "{{ref:Nora Body}}")
VOICE = ("Nora's voice (Laomedeia): upbeat, mid-high, energetic conversational female voice, fast confident vlog "
         "delivery with dry humor; rises into real cracking screams in danger; drops to a fast whisper when hiding.")
ACCENT_LOCK = ('Nora is a native Spanish speaker from Mexico City, in her early twenties. She speaks fast, casual '
               'Mexico City Spanish: every "s" crisp and fully pronounced, unstressed vowels relaxed and quick, a light '
               'rise-and-fall melody at the end of phrases. She has no American or English accent when she speaks '
               'Spanish, never a Spain accent, never lisps the "z" or "c", and says no English words.')
HAIR = ("Her honey-blonde ponytail is tied high at the crown of her head, never low at the nape; the wispy curtain "
        "bangs stay over the edges of her forehead and frame both cheeks.")

LIGHT = {
    "L0": "cool blue pre-dawn twilight turning to soft pale-gold light on the eastern horizon, low river mist lying over still brown water, damp air, muted colours, dew on leaves, long soft shadows",
    "L1": "plain natural early-morning daylight, the low sun off to one side, light thin cloud, clear air, everything evenly and naturally lit, ordinary soft shadows, natural documentary exposure",
    "L2": "plain natural mid-morning daylight, sun at a moderate angle, soft broken cloud, clear air, ordinary dappled shade under small broadleaf trees, crisp detail, true-to-life muted greens and browns",
    "L3": "plain bright overcast midday daylight, high thin cloud, even soft light with gentle shadows under bodies, clear air, natural colour",
    "L4": "plain natural afternoon daylight from the side, scattered cumulus, moving cloud shadows on the floodplain, clear air, natural contrast",
    "L5": "plain, still, warm late-afternoon daylight, soft and even, clear air, birds and insects active, ordinary peaceful light",
    "LQ": "the same plain, still, warm late-afternoon daylight as the clip before, clear air; only the motion changes: trees sway with no wind, water sloshing, dust shaken off branches",
    "LG": "the sky above streaked with countless thin bright meteor-like trails, tiny glassy beads pattering down like fine hail, pitting the wet mud and dimpling the river surface, daylight turning hazy and brassy-orange",
    "LT": "the whole sky glowing a dull orange-red, harsh hot diffuse light with no clear sun, shimmering heat haze, leaves curling and browning, thin wisps rising from dry leaf litter in places",
    "LD": "dim brownish-grey sky, sun reduced to a faint pale disc or invisible, flat murky light, fine grey dust settling on every surface, muted desaturated colours, low visibility",
}
LIGHT_GENERAL = ("Plain natural daylight only, exactly as on an ordinary field day: the sun lights the scene from the "
                 "side or above, never as a glowing backlight; clear air, no glow and no shafts of light; organic "
                 "micro-shadows under leaves and bodies; no artificial fill light.")

PLACE = {
    "LB": "the creek exactly as in the Hell Creek Bank reference: a slow silty brown creek about 15 m wide flowing from left to right; on the near side a bar of grey gravel and buff sand with driftwood; on the far side a near-vertical 2 m bank of layered grey-brown silt and olive-grey clay with roots hanging from its top and one dark, dry, low hollow about 1.5 m wide just above the waterline; horsetails at the water's edge; a spring broadleaf woodland edge with a few fan palms and a tall dawn redwood behind the bank",
    "LC": "the game corridor exactly as in the Hell Creek Game Corridor reference: a wide, chaotic animal-trampled corridor of deeply churned grey-brown silt and olive-grey clay with massive rounded ceratopsian foot depressions holding cloudy water, cutting from a small clearing into a spring broadleaf woodland; one big moss-covered fallen log lies along the right side of the corridor; a shallow grey mud wallow in the clearing; low shrubs, vines, moss, leaf litter and a few fan palms",
    "LW": "the waterhole exactly as in the Hell Creek Waterhole reference: a shrinking murky brown waterhole about 30 m across with a trampled grey mud rim full of rounded foot depressions; on the far north side a grove of tall dawn redwoods and swamp cypress with one dead grey cypress trunk leaning at the left edge of the grove; a wide flat of dry cracked grey mud in the foreground; white water lilies at the right edge of the water; horsetails along the shallows; a flat smooth stone at the south edge",
}
WORLD = "Hell Creek river floodplain, Montana, 66 million years ago, spring, on the day of the Chicxulub impact"

STYLE = ("Raw handheld natural-history field footage, Hell Creek floodplain in spring: small broadleaf trees with "
         "sycamore-, magnolia- and laurel-like leaves, a few fan palms and tall dawn redwoods at wet sites, horsetails "
         "at the water's edge, leaf litter and moss on grey-brown silt. True-to-life muted colours, fine 35mm film "
         "grain, raw 35mm wildlife documentary realism, deep focus, deep depth of field (f/8 aperture), entire frame "
         "sharp from foreground to distant horizon. Real amateur footage filmed by one person who is physically present.")

BIO_BASE = ("Visceral living animal biology filmed in the wild: rough non-reflective hide, matte scales, deep "
            "biological wrinkles and folds, grey-brown silt caked into crevices and on the lower limbs, flanks visibly "
            "moving with each breath; clean dry nostrils with faint moisture at the rim only, breathing transparent clean air.")
BIOLOGY = {
    "BD": BIO_BASE + " Triceratops hide like an African black rhinoceros: matte polygonal basement scales, prominent conical keratin tubercles, dry keratin horn sheaths with hairline micro-fractures.",
    "CG": BIO_BASE + " Triceratops hide like an African black rhinoceros: matte polygonal basement scales, prominent conical keratin tubercles, dry worn keratin horn sheaths with hairline micro-fractures.",
    "CN": BIO_BASE + " Young Triceratops hide: fine matte pebbly scales, small keratin horn nubs.",
    "TR": BIO_BASE + " Tyrannosaurus hide: fine pebbly scales over the body, larger matte scales on the snout and legs, deep folds at the neck; no feathers.",
    "ED": BIO_BASE + " Hadrosaur hide: tiny matte pebbly scales, larger polygonal scales on the lower body and tail, thin skin wrinkled over the ribs.",
    "BS": "Living crocodylian: rough dark olive-grey armoured scutes, wet silt on the flanks, thin real highlights only where water sits; clean dry nostrils at the snout tip, no vapour.",
}
CREATURE = {
    "BD": ("the bull Triceratops", "Matches the Bò Đực reference exactly: adult bull Triceratops, its LEFT brow horn broken off to a short rough stump, its RIGHT brow horn long and intact, an old pale scar across the LEFT half of its frill. The broken horn is always on its own left side and never heals."),
    "CG": ("the old female Triceratops", "Matches the Con Cái Già reference exactly: old female Triceratops, smaller than the bull, faded pale grey-beige frill with a chipped, notched edge, worn blunt brow horns, sway-backed."),
    "CN": ("the juvenile Triceratops", "Matches the Con Non reference exactly: a two-year-old Triceratops about 3 m long and hip-high to an adult, tiny rounded horn nubs, short frill, a pale crescent patch on its RIGHT cheek only."),
    "TR": ("the Tyrannosaurus", "Matches the T. rex reference exactly: adult Tyrannosaurus, fully scaly with no feathers, body held level, thick tail held off the ground, mouth firmly shut with thick scaly lips hiding every tooth, a long healed scar down the LEFT side of its snout, a few flies around its mouth."),
    "AR": ("the two Acheroraptors", "Match the Acheroraptor reference exactly: two coyote-sized feathered dromaeosaurs in mottled brown-grey, bodies and long stiff tails held level, sickle claws raised off the ground. Exactly two, never more."),
    "ED": ("the Edmontosaurus herd", "Matches the Edmontosaurus reference: long, low duck-billed hadrosaurs walking on four legs, flat broad bills, a fleshy crest along the back, long thick tails held level and fully visible; not horned, no frills."),
    "BS": ("the Borealosuchus crocodiles", "Match the Borealosuchus reference: crocodylians with long moderately narrow snouts; in the water only their rough ridged scute backs, eyes and snout tips show."),
    "IN": ("the Infernodrakon", "Matches the Infernodrakon reference: an azhdarchid pterosaur about as tall as a person when walking on all fours, long stiff neck, long straight pointed beak, short brown-grey fuzz, wings folded shut tight along its forelimbs like a closed umbrella while on the ground."),
    "CA": ("the Edmontosaurus carcass", "Matches the Edmontosaurus Carcass reference: the remains of a large 10 m duck-billed dinosaur lying sunken into the silt, ribs showing, a few flies."),
}
ANIMALS = {"BD", "CG", "CN", "TR", "AR", "ED", "BS", "IN"}

# ---------------------------------------------------------------- script.md parser
def parse_storyboard():
    sec = SCRIPT[SCRIPT.index("## §9 STORYBOARD"):SCRIPT.index("## §10")]
    rows = {}
    order = []
    for line in sec.splitlines():
        m = re.match(r"\| \*\*([A-Za-z0-9-]+)\*\* \|(.*)\|\s*$", line)
        if not m:
            continue
        cid = m.group(1)
        c = [x.strip() for x in m.group(2).split("|")]
        if cid == "CO":
            continue
        dur, shot, refs, sf, light, hinh, thoai, words, viec, beat, dung = c
        dlg = "" if thoai.startswith("*(") else thoai
        rows[cid] = {"dur": int(dur.rstrip("s")), "shot": shot, "refs": [r.strip() for r in refs.split(",")],
                     "sf": sf, "light": light, "hinh": hinh, "lines": [x.strip() for x in dlg.split(" / ")] if dlg else [],
                     "words": int(words), "beat": beat}
        order.append(cid)
    return order, rows


ORDER, ROWS = parse_storyboard()
IDX = {c: i for i, c in enumerate(ORDER)}


def segs(dur):
    return {4: ["0-2s", "2-4s"], 6: ["0-2s", "2-4s", "4-6s"], 8: ["0-3s", "3-6s", "6-8s"],
            10: ["0-3s", "3-7s", "7-10s"]}[dur]


def wc(s):  # unicode-aware: Spanish accents count inside one word (dialogue-es-latam.md §3)
    return len(re.findall(r"\w+(?:'\w+)*", s))


def after(cid, ref):
    return IDX[cid] >= IDX[ref]


def nora_state(cid):
    """Continuity ledger §11.4 -> sentences."""
    s = []
    if IDX[cid] <= IDX["A1-14"]:
        s.append("Her hair and clothes are still soaking wet from the creek.")
    if IDX[cid] < IDX["A1-07"]:
        s.append("The turtle-shell flask is not on her yet: nothing hangs at her left hip.")
    elif IDX[cid] <= IDX["A3-06a"]:
        s.append("The turtle-shell flask hangs at her left hip on its twisted plant-fibre cord, exactly as on the Nora Body sheet.")
    elif IDX[cid] >= IDX["A3-07"]:
        s.append("The turtle-shell flask is gone; only a short snapped plant-fibre cord end hangs at her left hip.")
    if after(cid, "A2-08"):
        s.append("Dried grey mud is smeared on her forearms and neck.")
    if IDX["A2-08"] <= IDX[cid] <= IDX["A2-10"]:
        s.append("She holds one fallen fan-palm frond in her free left hand.")
    if after(cid, "A4-08"):
        s.append("Grey-brown mud is smeared across her left cheek.")
    if after(cid, "A4-P2"):
        s.append("Dust coats her face and hair.")
    if after(cid, "A4-12") and not after(cid, "A5-01"):
        s.append("Tiny glass beads are caught in her hair.")
    if after(cid, "A4-19"):
        s.append("Wet mud covers her arms, neck and clothes.")
    if after(cid, "A5-03"):
        s.append("A thin layer of fine grey dust lies on her hair and shoulders.")
    return " ".join(s)


OUTFIT_WORDS = ("Outfit check (image only, exactly as on the Nora Body sheet): a short-sleeved olive-tan raw linen tunic "
                "with an X-laced V-neck, a wide dark-brown tied leather belt with NO metal buckle, skin-tight olive-brown "
                "leather trousers and mid-calf laced brown leather boots; never long sleeves, never a green shirt.")
REF_FACE_LOCK = ("FACE LOCK: Nora's face is exactly the face in {{ref:Nora}}, kept 1:1 as it is in "
                 "that image, including her makeup and hairstyle, in every frame. Do not redraw, restyle, retouch, age or "
                 "change anything about her face. MAKEUP LOCK: keep her makeup exactly as in {{ref:Nora}}, unchanged in every frame.")
HANDS_TXT_V = ("First-person view looking down at her own hands; the hands look exactly like {{ref:Nora Hand}}, with "
               "short clean unpainted nails and no rings or watch; her sleeves, trousers and boots are exactly as in {{ref:Nora Body}}.")
HANDS_TXT_I = ("First-person view looking down at her own hands; the hands look exactly like {{ref:Nora Hand}}, with "
               "short clean unpainted nails and no rings or watch; the edge of an olive-tan linen short sleeve shows at the side of the frame.")
FEET_TXT = ("First-person view looking down at her own feet: the toe of one mid-calf laced brown leather boot, "
            "described in words only, with no reference image for it.")
FLASK_X = ("The only exception is the turtle-shell flask at her left hip: whether it is there, tied on, or "
           "gone follows the state sentence and the timeline of this clip, not the Body sheet.")
BLIND = "The camera viewpoint and her gripping arm are completely outside the visible frame and never seen."
NOTEXT = "No subtitles, captions, labels, icons or text of any kind appear anywhere in the frame."
CLEAN = ("The image is clean footage only: no interface, no recording indicator, no battery icon, no zoom label, "
         "no names, no text or symbols.")


def camera(kind, size, extra):
    if kind == "SELFIE":
        vp = ("Self-filmed vlog view at chest height, tilted very slightly up toward her face; the viewpoint itself is "
              "the lens, so no arm, no hand and nothing holding the view ever appears in the frame. " + extra)
        desc = (BLIND + " She never reaches toward, touches, covers, taps or points at the lens. Her free left hand "
                "is empty unless the timeline says otherwise. Pure front-facing self-filmed view from the very first "
                "frame; the shot never switches to a third-person view.")
    elif kind == "OTS":
        vp = ("Over-the-shoulder vlog view filmed by Nora herself from just behind her own shoulder at shoulder "
              "height; no arm, no hand and nothing holding the view ever appears in the frame. " + extra)
        desc = BLIND + " She never reaches toward or touches the lens. The shot never switches to a third-person view."
    elif kind == "FIXED":
        vp = "Static footage from a fixed viewpoint " + extra + " The frame does not move; nobody touches the viewpoint."
        desc = ("Nothing that records the scene is ever visible. Both of Nora's hands are free. The shot never "
                "switches angle.")
    elif kind == "AERIAL":
        vp = extra
        desc = "A very smooth, slow documentary establishing view from high above; no people anywhere."
    else:  # POV / HIDE / MACRO
        vp = "First-person view through Nora's own eyes. " + extra
        desc = ("All recording gear and her gripping arm are completely outside the visible frame and never seen. "
                "The shot stays a first-person view through her own eyes for the whole clip.")
    return {"viewpoint": vp, "shot_size": size, "description": desc}


SIZE = {"EWS": "extreme wide shot", "WS": "wide shot", "MS": "medium shot", "MCU": "medium close-up",
        "CU": "close-up", "ECU": "extreme close-up"}


def build(cid, d, chain_head=None):
    r = ROWS[cid]
    kind, sz = [x.strip() for x in r["shot"].split("·")]
    refs = list(d.get("refs_override") or r["refs"])
    codes = set(refs)
    face = "N" in codes and kind in ("SELFIE", "OTS", "FIXED")
    hands = "N" in codes and not face
    animals = [c for c in refs if c in CREATURE]
    loc = next((c for c in refs if c in PLACE), None)
    light = LIGHT[r["light"]]
    if r["light"] == "LQ" and IDX[cid] > IDX["A4-07b"]:
        light += "; the dead grey cypress now lies fallen across the north edge of the water"

    place_v = PLACE[loc].replace(f"the {ENT[loc]} reference", "{{ref:%s}}" % ENT[loc]) if loc else ""
    setting = f"{WORLD}. Location: {place_v}. {d.get('setting_extra', '')} Light: {light}. {LIGHT_GENERAL}"
    setting = re.sub(r"\s+", " ", setting).strip()

    chars = []
    if face:
        chars.append({"name": "Nora", "visual_lock": " ".join([REF_FACE_LOCK, BODY_LOCK_V, OUTFIT_LOCK_V, FLASK_X]),
                      "state": (d.get("state", "") + " " + nora_state(cid)).strip()})
    elif hands:
        chars.append({"name": "Nora's hands (first-person)",
                      "visual_lock": (FEET_TXT if d.get("feet_only") else HANDS_TXT_V),
                      "state": (d.get("state", "") + " " + nora_state(cid)).strip()})
    for a in animals:
        name, lock = CREATURE[a]
        lock_v = lock.replace(f"the {ENT[a]} reference", "{{ref:%s}}" % ENT[a])
        chars.append({"name": name, "visual_lock": lock_v + (" " + BIOLOGY[a] if a in BIOLOGY else ""),
                      "state": d.get("anim", {}).get(a, "")})

    keys = d.get("keys") or segs(r["dur"])
    assert len(d["tl"]) == len(keys), (cid, len(d["tl"]), keys)
    tl = dict(zip(keys, d["tl"]))
    if chain_head:
        first = keys[0]
        tl[first] = f"The clip opens exactly on the final frame of {chain_head['prev']}: {chain_head['opens']} " + tl[first]

    if r["lines"]:
        lk = d.get("line_keys") or segs(r["dur"])
        dialogue = [{"t": k, "speaker": "Nora", "line": ln} for k, ln in zip(lk, r["lines"])]
        assert len(dialogue) == len(r["lines"]), cid
        n = sum(wc(x) for x in r["lines"])
        assert n == r["words"], (cid, n, r["words"])
        start = "From the very first frame at second 0, Nora begins speaking immediately. " if face or True else ""
        speech = {"speaker": "Nora", "language": "es-419 Latin American Spanish, Mexico City accent",
                  "delivery": start + d["deliv"] + " " + VOICE + " " + ACCENT_LOCK + (
            "" if face else " She is the viewer: her voice comes from behind the view; her face never appears."),
                  "dialogue": dialogue}
        speak_rule = "Only Nora speaks, and only in Latin American Spanish; nobody speaks over anyone else; the animals make only animal sounds, never words."
    else:
        speech = {"speaker": "none", "delivery": d.get("silence", (
            "Strictly NO spoken dialogue for the whole clip. " + ("Her mouth stays firmly closed; " if face else "")
            + "only held breathing through the nose and the real sounds of the place are heard."))}
        speak_rule = "Strictly NO spoken words in this clip."

    neg = [BLIND if kind != "AERIAL" else "No people, no aircraft, nothing man-made anywhere in the frame.",
           NOTEXT, CLEAN, speak_rule,
           "Deep focus: strictly NO shallow depth of field, strictly NO bokeh, no blurred background.",
           f"Dialogue word count strictly {r['words']} words, exactly as written in script.md."]
    if face:
        neg.append("FACE and MAKEUP LOCK: no face drift: her face, makeup and hairstyle never differ from the attached Nora reference image; no bare-faced or restyled look.")
        neg.append("BODY and OUTFIT LOCK: build, proportions and outfit exactly as the Nora Body reference sheet; NO fur, NO hood, NO cloak, NO outfit variations.")
    if hands:
        neg.append("HAND LOCK: strictly NO male hands, NO hairy knuckles, NO rings, NO watch, NO painted nails, NO extra or fused fingers.")
    if any(a in ANIMALS for a in animals):
        neg.append("ANTI-SMOKE LOCK: strictly NO smoke, strictly NO breath vapour, strictly NO steam, strictly NO white plumes from any nostril; clean dry nostrils breathing transparent clean air.")
        neg.append("ANTI-CGI LOCK: strictly NOT a 3D digital render, NOT a plastic toy model, NOT a museum resin statue, NO specular plastic sheen, NO artificial god rays, NO sunlight streaming beams, NO studio rim light.")
    if len([a for a in animals if a in ANIMALS]) >= 2 or animals and any(a in ("ED", "AR", "BS") for a in animals):
        neg.append("Each animal is a separate body; animals never overlap, merge, duplicate or vanish.")
    neg += d.get("neg", [])

    clip = {
        "clip_id": cid, "scene_name": d["name"], "duration": r["dur"], "aspect_ratio": "16:9",
        "refs": [ENT[c] for c in refs],
        "camera": camera(kind, SIZE[sz], d["cam"]),
        "style": STYLE,
        "setting": setting,
        "characters": chars,
        "in_place": "Everything is already in place from the very first frame: " + d["inplace"] +
                    " Every person, animal and object stays where it is placed unless the timeline moves it; nothing appears suddenly, nothing vanishes.",
        "shot": d["frame"],
        "timeline_action": tl,
        "speech": speech,
        "dramatic_craft": dict(zip(["beat", "value_turn", "subtext", "prop_and_detail"], d["craft"])),
        "audio": d["audio"],
        "physics": d["phys"],
        "negative_constraints": neg,
    }
    sf = r["sf"]
    if sf == "P":
        clip["start_frame"] = {"type": "PREV_LAST_FRAME", "note": f"use the last frame of {chain_head['prev']}"}
    else:
        # Subject + identity first, then composition, then place/light/style (short). User 2026-10-14:
        # Nora's face goes in as a REFERENCE image (GENERATE_IMAGE + refs), never as the edited base image.
        if kind == "AERIAL":
            image_refs = []
        elif face:
            image_refs = ["Nora", "Nora Body"] + ([ENT[loc]] if loc else [])
        elif d.get("image_refs"):
            image_refs = [ENT[c] for c in d["image_refs"]]
        elif hands:
            # hands/feet-only frames: never attach the face or body sheet (UNSAFE_GENERATION on A1-04/06/09)
            image_refs = [ENT[c] for c in refs if c not in ("N", "NB") and not (d.get("feet_only") and c == "NH")]
        else:
            image_refs = [ENT[c] for c in refs]
        img = [f"Single still photograph, frame 0 of this shot before any movement, {SIZE[sz]}."]
        if kind not in ("SELFIE", "OTS"):
            # where the viewpoint physically is (aerial height, waist-deep in water, flat on the ground...)
            img.append("VIEWPOINT: " + (d["cam"] if kind != "FIXED" else "a fixed viewpoint " + d["cam"]))
        if face:
            # User 2026-10-14: do not re-describe the face; lock it to the mentioned reference image.
            # {{ref:<entity>}} = inline image mention, replaced by Flow's mention chip when the request is built.
            img.append("EXACTLY ONE person in the whole frame: Nora; she appears only once, never duplicated, no second woman.")
            img.append("FACE LOCK: Nora's face is exactly the face in {{ref:Nora}}, kept 1:1 as it is in that image, "
                       "including her makeup and hairstyle. Do not redraw, restyle, retouch, age or change anything about her face.")
            img.append("MAKEUP LOCK: keep her makeup exactly as in {{ref:Nora}}, unchanged.")
            img.append("BODY and OUTFIT LOCK: her build and complete outfit are exactly as shown in {{ref:Nora Body}}; "
                       "do not redraw or change any part of the outfit. " + FLASK_X + " " + nora_state(cid) + " " + d.get("state", ""))
        elif hands:
            img.append(FEET_TXT.replace(", described in words only, with no reference image for it", "") if d.get("feet_only") else HANDS_TXT_I)
        else:
            img.append("No people anywhere in the frame.")
        for a in animals:
            # frames with Nora's face carry only [face, body, location] refs, so animals are described in words only
            mention = f"{CREATURE[a][0][0].upper() + CREATURE[a][0][1:]}: exactly as shown in {{{{ref:{ENT[a]}}}}}. " if ENT[a] in image_refs else ""
            desc = CREATURE[a][1].split(": ", 1)[1] if ENT[a] not in image_refs and CREATURE[a][1].startswith("Match") else CREATURE[a][1]
            img.append(mention + desc)
        img.append(f"Composition: {d['frame']} Already in place: {d['inplace']}")
        if kind == "SELFIE":
            img.append("Self-filmed vlog framing, close: only Nora's head, shoulders and chest are in the frame, her face large "
                       "and sharp in the upper third, looking straight into the lens. " + BLIND)
        elif kind == "OTS":
            img.append("Over-the-shoulder vlog framing: " + BLIND)
        elif kind != "AERIAL":
            img.append("First-person or fixed documentary view; nothing that records the scene is visible.")
        if kind == "AERIAL" or not loc or ENT[loc] not in image_refs:
            place_txt = PLACE[loc].split(": ", 1)[-1] if loc else ""
            img.append(f"Place: {WORLD}; seen from high above: {place_txt}. Light: {light}.")
        else:
            img.append(f"Place: {WORLD}; the same place as {{{{ref:{ENT[loc]}}}}} (same creek, banks, plants and ground), "
                       f"but seen from THIS frame's own viewpoint and composition above; do not copy the reference photo's framing. "
                       f"{PLACE[loc].split(': ', 1)[-1]}. Light: {light}.")
        img.append("Raw 35mm wildlife documentary photograph, true muted colours, fine film grain, deep focus f/8 with "
                   "the whole frame sharp; real living animals with rough matte non-reflective hide, clean dry "
                   "nostrils, not a 3D render, not a plastic toy, no studio light.")
        img.append(NOTEXT)
        clip["start_frame"] = {"type": "GENERATE_IMAGE", "image_refs": image_refs,
                               "refs": "scene character_names (Nora face + Nora Body attached as reference images)" if face else "scene character_names",
                               "image_prompt": re.sub(r"\s+", " ", " ".join(img)).strip()}
    clip["_vi"] = {"hinh": r["hinh"], "beat": r["beat"], "thoai_vi": d.get("vi", [])}
    return clip
