import json
import urllib.request
import sqlite3
import os
import sys

# 1. Flush stale queue
print("1. Flushing stale queue...", flush=True)
conn = sqlite3.connect("flow_agent.db")
conn.execute("UPDATE request SET status='FAILED' WHERE status='PENDING'")
conn.commit()
conn.close()

# 2. Create Project
project_payload = {
    "name": "Time Travel Vlog — Ancient Babylon (570 BC)",
    "description": "POV Time Travel Vlog: A modern young traveler named Mia journeys back to ancient Babylon at its peak in 570 BC, exploring the bustling Euphrates markets and discovering the engineering secrets of the legendary Hanging Gardens.",
    "story": "In 570 BC, Babylon stands at the absolute zenith of the Neo-Babylonian Empire under Nebuchadnezzar II. A young vlogger named Mia, disguised in native Mesopotamian linen robes, navigates the lively riverfront markets where silver shekels buy barley beer and sweet dates. She explores the monumental vaults supporting the legendary Hanging Gardens of Babylon, tastes fresh figs, gets caught in a royal procession, narrowly escapes palace guards, and witnesses the breathtaking engineering of the rooftop oasis at sunset.",
    "material": "realistic",
    "language": "en",
    "characters": [
        {
            "name": "Mia",
            "entity_type": "character",
            "description": "Mia, a 23-year-old traveler with a soft oval face, hazel-green eyes, natural radiant skin, full lips, honey-blonde hair with parted curtain bangs tied in a textured mid-high ponytail, wearing an authentic ancient Mesopotamian deep-cream linen tunic with subtle embroidered neckline and woven sash.",
            "voice_description": "Achernar — soft, higher-pitched, natural expressive conversational female voice, casual vlog tone, breathy when amazed, hushed whisper when nervous"
        },
        {
            "name": "Hanging Gardens of Babylon",
            "entity_type": "location",
            "description": "Colossal multi-tiered stepped terrace garden rising 75 feet above the Euphrates river, cascading waterfalls, turquoise pools, overflowing with lush date palms, climbing grapevines, cypress trees, and flowering oleanders."
        },
        {
            "name": "Euphrates Riverbank",
            "entity_type": "location",
            "description": "Sun-drenched dirt embankment along the shimmering green waters of the Euphrates river in Babylon, traditional circular black bitumen quffa boats and palm frond docks."
        },
        {
            "name": "Ishtar Gate",
            "entity_type": "location",
            "description": "Babylon Ishtar Gate, monumental double gateway of vibrant deep-blue glazed bricks adorned with alternating relief rows of yellow and white sirrush dragons and aurochs bulls."
        },
        {
            "name": "Etemenanki Ziggurat",
            "entity_type": "location",
            "description": "Etemenanki great ziggurat of Babylon, massive seven-tiered mud-brick stepped tower rising 90 meters high beside the Esagila temple, blue glazed shrine on the top terrace."
        }
    ]
}

print("2. Creating Project...", flush=True)
req = urllib.request.Request(
    "http://127.0.0.1:8100/api/projects",
    data=json.dumps(project_payload).encode("utf-8"),
    headers={"Content-Type": "application/json"}
)
with urllib.request.urlopen(req, timeout=30) as resp:
    project_res = json.loads(resp.read())

pid = project_res["id"]
print(f"Project created! ID: {pid}", flush=True)

# Re-link Mia's character reference image media_id
MIA_REF_MEDIA_ID = "3904fece-f12e-47ef-9018-361f1a74f315"
conn = sqlite3.connect("flow_agent.db")
c = conn.cursor()
c.execute("""
    UPDATE character
    SET media_id = ?,
        image_url = 'https://flow-content.google/image/3904fece-f12e-47ef-9018-361f1a74f315'
    WHERE id IN (
        SELECT character_id FROM project_character WHERE project_id = ?
    ) AND name = 'Mia'
""", (MIA_REF_MEDIA_ID, pid))
conn.commit()
print("Mia face reference image linked successfully!", flush=True)

# 3. Create Video
print("3. Creating Video...", flush=True)
video_payload = {
    "project_id": pid,
    "title": "I Time Traveled to Ancient Babylon in 570 BC! (Vlog)",
    "display_order": 0
}
req = urllib.request.Request(
    "http://127.0.0.1:8100/api/videos",
    data=json.dumps(video_payload).encode("utf-8"),
    headers={"Content-Type": "application/json"}
)
with urllib.request.urlopen(req, timeout=30) as resp:
    video_res = json.loads(resp.read())

vid = video_res["id"]
print(f"Video created! ID: {vid}", flush=True)

# 4. Switch Active Project
req = urllib.request.Request(
    "http://127.0.0.1:8100/api/active-project",
    data=json.dumps({"project_id": pid}).encode("utf-8"),
    headers={"Content-Type": "application/json"},
    method="PUT"
)
urllib.request.urlopen(req)
print(f"Active project switched to {pid}", flush=True)

# 5. Define All 23 Scenes
scenes_data = [
    # Act 1: Hook (0-5%)
    {
        "order": 0,
        "prompt": "Handheld selfie vlog shot of a young traveler smiling warmly with bright eyes directly into the camera on the dirt riverbank of ancient Babylon under bright morning sunlight, an ancient wooden ox-cart with large wooden wheels rolling past on the dusty road behind her, the Euphrates river and the distant terraced Hanging Gardens rising in the background. Photorealistic documentary realism, natural skin texture, cinematic desert daylight, authentic ancient linen clothing, 8k resolution, no 2D, no drawing, no illustration, no painting.",
        "video_prompt": '0-3s: Handheld ultra-wide 0.5x selfie camera with subtle natural hand shake. Mia looks directly into the lens smiling warmly on the sunlit Euphrates riverbank as an ancient wooden ox-cart rumbles past in the background. 3-7s: Mia leans in slightly toward the camera, speaking with sparkling eyes in a cheerful conversational tone "You guys... welcome to Babylon, 570 BC! And right behind me is the legendary Hanging Gardens!" 7-10s: She gestures with her free hand, panning the selfie camera slightly to reveal the breathtaking green terraces of the gardens and the shimmering river under the desert sun. Audio: no background music. Keep character dialogue and natural ambient sounds. Negative: second smartphone, floating phone, phone clamp, subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands, morphing.',
        "narrator_text": "You guys... welcome to Babylon, 570 BC! And right behind me is the legendary Hanging Gardens!",
        "character_names": ["Mia", "Euphrates Riverbank", "Hanging Gardens of Babylon"]
    },
    {
        "order": 1,
        "prompt": "Handheld selfie vlog shot of a young traveler walking along the lively river embankment of Babylon under morning sunlight, the Euphrates river on one side and the distant terraced gardens towering ahead. Photorealistic documentary realism, authentic ancient textures.",
        "video_prompt": '0-3s: Handheld selfie tracking Mia walking briskly along the bustling dirt embankment as Babylonian boatmen shout near the docks. 3-7s: Mia leans in close to the lens, speaking in a warm storytelling whisper "King Nebuchadnezzar built this entire mountain of green for Queen Amytis because she missed the forested hills of Media." 7-10s: She looks back toward the river as two donkeys laden with woven river reed hampers walk past in the foreground, briefly occluding the frame. Audio: no background music. Keep character dialogue and natural ambient sounds. Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.',
        "narrator_text": "King Nebuchadnezzar built this entire mountain of green for Queen Amytis because she missed the forested hills of Media.",
        "character_names": ["Mia", "Euphrates Riverbank", "Hanging Gardens of Babylon"]
    },
    # Act 2: Everyday Life (5-40%)
    {
        "order": 2,
        "prompt": "First-person POV looking out over the green waters of the Euphrates river, circular woven bitumen-coated quffa boats ferrying rich alluvial soil and palm saplings toward the palace docks.",
        "video_prompt": '0-3s: Eye-level first-person POV tracking circular black bitumen-coated quffa boats gliding across the glittering Euphrates river. 3-7s: Mia\'s voice captures deep fascination "Every single drop of water and every basket of rich soil feeding those rooftop trees starts right here from this river." 7-10s: The camera whips fast to the right with heavy natural motion blur, settling on towering timber scaffolding and brick pillars. Audio: no background music. Keep character dialogue and natural ambient sounds. Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.',
        "narrator_text": "Every single drop of water and every basket of rich soil feeding those rooftop trees starts right here from this river.",
        "character_names": ["Mia", "Euphrates Riverbank"]
    },
    {
        "order": 3,
        "prompt": "Handheld camera gazing up at an enormous wooden chain-of-buckets water pump system turning smoothly beside a high brick aqueduct pillar, lifting glistening water from a deep river trench.",
        "video_prompt": '0-3s: Camera settles from the whip pan looking up at the colossal wooden chain-of-buckets wheel creaking steadily as it lifts tons of river water upward. 3-7s: Mia steps into the lower third of the frame, shielding her eyes and shouting over the rushing water "Look at this mechanical chain pump! 2,500 years ago, lifting thousands of gallons into the desert sky every hour!" 7-10s: Cool water droplets mist over the lens as the camera tilts up along the brick aqueduct channel. Audio: no background music. Keep character dialogue and natural ambient sounds. Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.',
        "narrator_text": "Look at this mechanical chain pump! 2,500 years ago, lifting thousands of gallons into the desert sky every hour!",
        "character_names": ["Mia"]
    },
    {
        "order": 4,
        "prompt": "Close-up first-person POV of the traveler's fingers touching a thick black layer of natural bitumen pitch and reed mats pressed between heavy baked brick tiers beneath giant cedar roots.",
        "video_prompt": '0-3s: Close-up first-person POV of Mia\'s fingertips pressing against the firm, black waterproof asphalt layer and woven reeds between the baked brick courses. 3-7s: Mia whispers in amazement "Feel this texture. Natural tar and reeds waterproofing the stone so water doesn\'t flood the royal palace chambers below." 7-10s: A Babylonian laborer carrying a woven basket walks past in front of the lens, his fringed linen tunic creating a natural wipe cut. Audio: no background music. Keep character dialogue and natural ambient sounds. Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.',
        "narrator_text": "Feel this texture. Natural tar and reeds waterproofing the stone so water doesn't flood the royal palace chambers below.",
        "character_names": ["Mia"]
    },
    {
        "order": 5,
        "prompt": "Ultra-wide selfie of a traveler walking beneath monumental baked-brick barrel vaults and stone pillars supporting the towering first terrace of the Hanging Gardens above, shafts of bright sunlight piercing through leafy gaps.",
        "video_prompt": '0-3s: Mia walks beneath towering baked-brick arches that resemble a cavernous underground crypt supporting the mountain of trees above. 3-7s: She tilts her selfie camera upward, looking around in awe and saying "Walking under these colossal vaults feels like being inside an artificial mountain. You can actually hear water trickling above our heads!" 7-10s: Shafts of bright sunlight pierce through gaps in the masonry as she steps forward through an arched stone portal. Audio: no background music. Keep character dialogue and natural ambient sounds. Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.',
        "narrator_text": "Walking under these colossal vaults feels like being inside an artificial mountain. You can actually hear water trickling above our heads!",
        "character_names": ["Mia", "Hanging Gardens of Babylon"]
    },
    {
        "order": 6,
        "prompt": "Handheld selfie navigating a vibrant bazaar stall nestled in the shaded arches of the gardens, tables loaded with ruby red pomegranates, fresh green figs, and fragrant jars of mountain oils.",
        "video_prompt": '0-3s: Mia weaves through colorful wooden stalls piled high with fresh garden harvests, split ruby-red pomegranates and green figs glistening in the light. 3-7s: The vendor smiles warmly and offers a ripe fig; Mia laughs with delight and says "The aromas here are unbelievable... wild pomegranates, mountain thyme, and sweet figs fresh off the royal terraces!" 7-10s: She smiles thanking the vendor in Akkadian, then sets her smartphone down against a terracotta jug on a low wooden table. Audio: no background music. Keep character dialogue and natural ambient sounds. Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.',
        "narrator_text": "The aromas here are unbelievable... wild pomegranates, mountain thyme, and sweet figs fresh off the royal terraces!",
        "character_names": ["Mia"]
    },
    {
        "order": 7,
        "prompt": "Photorealistic live-action vlog still, smartphone camera propped upright on a rustic wooden table in an outdoor Babylonian terrace. Mia sits on a woven reed stool facing the lens in eye-level candid framing, smiling naturally as she holds a fresh split ripe fig, with flatbread and an unglazed earthenware cup on the wooden table. Warm sun-dappled natural lighting filtering through lush green grapevines hanging overhead. Candid real-life travel vlog photography, authentic ancient textures, depth of field, photoreal, no 2D, no drawing, no illustration.",
        "video_prompt": '0-3s: Static wide frame from the propped smartphone showing Mia sitting relaxed on a reed stool, taking a delicate bite of the ripe sweet fig. 3-7s: She closes her eyes in pure culinary bliss, leaning toward the camera and whispering "Honestly, tasting a fig picked directly from the Hanging Gardens of Babylon? This is absolute bucket-list perfection." 7-10s: She takes a sip of cool water from her unglazed clay cup, smiles at the camera, and picks the phone back up. Audio: no background music. Keep character dialogue and natural ambient sounds. Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.',
        "narrator_text": "Honestly, tasting a fig picked directly from the Hanging Gardens of Babylon? This is absolute bucket-list perfection.",
        "character_names": ["Mia"]
    },
    {
        "order": 8,
        "prompt": "First-person POV walking alongside a carved limestone water channel lined with maidenhair ferns, clear water cascading gently down miniature stone steps alongside a spiral staircase.",
        "video_prompt": '0-3s: Smooth first-person tracking forward up the stone steps beside a crystal-clear stream gurgling down a carved limestone canal. 3-7s: Mia\'s voice observes with admiration "This gravity-fed aqueduct system circulates water to every single terrace like a living biological bloodstream in the desert." 7-10s: Overhanging maidenhair ferns and fragrant jasmine blossoms brush softly across the camera lens. Audio: no background music. Keep character dialogue and natural ambient sounds. Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.',
        "narrator_text": "This gravity-fed aqueduct system circulates water to every single terrace like a living biological bloodstream in the desert.",
        "character_names": ["Mia"]
    },
    {
        "order": 9,
        "prompt": "First-person POV looking down at an ancient bronze pan balance on a garden stone pedestal, a merchant weighing curled silver wire clippings against stone seed weights.",
        "video_prompt": '0-3s: Mia\'s hand enters the frame holding a coiled silver wire as the merchant carefully balances hematite stone weights on the bronze scales. 3-7s: Mia whispers in fascination "No minted coins here in 570 BC... just little curls of silver wire called shekels, weighed by hand to trade for rare mountain spices." 7-10s: The merchant hands her a bundle of fragrant mountain herbs; Mia tucks a blossom behind her ear and turns toward a grand stairway. Audio: no background music. Keep character dialogue and natural ambient sounds. Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.',
        "narrator_text": "No minted coins here in 570 BC... just little curls of silver wire called shekels, weighed by hand to trade for rare mountain spices.",
        "character_names": ["Mia"]
    },
    # Act 3: Power & Reveal #1 (40-55%)
    {
        "order": 10,
        "prompt": "Handheld selfie of a traveler cautiously ascending a wide monumental stone stairway lined with potted cypress trees and flowering oleander, looking up nervously toward the private upper terraces.",
        "video_prompt": '0-3s: Mia walks up the wide stone staircase, the warm Mesopotamian wind rustling through cypress branches and fluttering her blonde hair. 3-7s: She lowers her voice to an anxious whisper, glancing left and right "We\'re sneaking up toward Queen Amytis\'s private upper sanctuary... definitely a restricted royal zone for unauthorized travelers." 7-10s: She turns her back completely to the camera to check the landing ahead, her ponytail and back filling the frame. Audio: no background music. Keep character dialogue and natural ambient sounds. Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.',
        "narrator_text": "We're sneaking up toward Queen Amytis's private upper sanctuary... definitely a restricted royal zone for unauthorized travelers.",
        "character_names": ["Mia"]
    },
    {
        "order": 11,
        "prompt": "Medium shot opening on the back of the traveler's head, turning around to reveal an astonishing multi-tiered terrace filled with blooming white lilies, pomegranate trees, and two Babylonian palace guards in scale armor standing sentinel.",
        "video_prompt": '0-3s: Camera opens tight on the back of Mia\'s hair; she spins around 180 degrees, revealing a breathtaking floral terrace and two tall Babylonian guards standing guard. 3-7s: Her eyes widen in stunned shock as she murmurs "Look at this grand terrace... an explosion of royal flowers! But wait... armed imperial guards are patrolling right ahead!" 7-10s: She ducks swiftly to the right, crouching low behind an ornamental carved limestone column. Audio: no background music. Keep character dialogue and natural ambient sounds. Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.',
        "narrator_text": "Look at this grand terrace... an explosion of royal flowers! But wait... armed imperial guards are patrolling right ahead!",
        "character_names": ["Mia"]
    },
    {
        "order": 12,
        "prompt": "Handheld selfie ducking behind a purple bougainvillea trellis on an elevated garden terrace, royal archers and guards walking along a stone walkway in the background.",
        "video_prompt": '0-3s: Handheld camera tilted low as Mia crouches behind blooming purple bougainvillea vines while bronze-armored guards march along the parapet thirty feet away. 3-7s: She whispers urgently into the microphone with rapid shallow breaths "Stay quiet... if they catch someone with a glowing camera in the Queen\'s private botanical court, I\'m done for." 7-10s: Heavy bronze greaves and leather boots clatter loudly on stone as guards pass just out of sight. Audio: no background music. Keep character dialogue and natural ambient sounds. Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.',
        "narrator_text": "Stay quiet... if they catch someone with a glowing camera in the Queen's private botanical court, I'm done for.",
        "character_names": ["Mia"]
    },
    # Act 4: High Danger & Climax (55-70%)
    {
        "order": 13,
        "prompt": "An ornate royal procession passing through a garden terrace: court ladies in embroidered Median robes and silk veils, fan-bearers, and an imposing royal officer who suddenly turns and spots the traveler.",
        "video_prompt": '0-3s: Through parted palm fronds, Queen Amytis\'s royal court glides past in embroidered Median robes and silk parasols amidst fragrant myrrh incense. 3-7s: A tall royal officer with a spear suddenly snaps his head around, his eyes locking directly onto Mia\'s phone! Mia gasps in terror "He sees the camera! RUN!" 7-10s: She spins abruptly around, sprinting down the stone terrace as alarmed Akkadian shouts echo behind her. Audio: no background music. Keep character dialogue and natural ambient sounds. Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.',
        "narrator_text": "He sees the camera! RUN!",
        "character_names": ["Mia"]
    },
    {
        "order": 14,
        "prompt": "Dynamic shaky handheld chase through a misty cavernous corridor behind an artificial waterfall in the Hanging Gardens, water droplets spraying, lantern light flickering on wet stone.",
        "video_prompt": '0-3s: High-energy shaky handheld chase camera as Mia sprints full tilt through a shadowy stone gallery directly behind a thundering curtain of falling water. 3-7s: Water spray drenches her face; she glances backward into the camera, panting heavily "Running for my life behind a 2,500-year-old waterfall... completely terrifying but insane!" 7-10s: She leaps over a stone water sluice, dodging sharply around a mossy arched corner into a side garden. Audio: no background music. Keep character dialogue and natural ambient sounds. Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.',
        "narrator_text": "Running for my life behind a 2,500-year-old waterfall... completely terrifying but insane!",
        "character_names": ["Mia"]
    },
    {
        "order": 15,
        "prompt": "A quiet sheltered nursery terrace filled with terra-cotta sapling pots and shade cloths, Mia slipping through a narrow arched wooden gate, closing it softly behind her.",
        "video_prompt": '0-3s: Mia dashes through a weathered cedar gate, pulls it shut until the wooden latch clicks, and slides down against the sun-baked mudbrick wall. 3-7s: She takes deep shuddering breaths, pressing a trembling hand to her chest "Okay... we lost them. The guards just thundered down toward the lower barracks. We\'re safe in the upper nursery." 7-10s: The loud pursuit fades into distant courtyard echoes, replaced by gentle afternoon bird calls in the quiet nursery. Audio: no background music. Keep character dialogue and natural ambient sounds. Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.',
        "narrator_text": "Okay... we lost them. The guards just thundered down toward the lower barracks. We're safe in the upper nursery.",
        "character_names": ["Mia"]
    },
    # Act 5: Decompression (70-75%)
    {
        "order": 16,
        "prompt": "Handheld selfie shot on a quiet terrace, an elderly Babylonian gardener with a warm wrinkled face in a simple wool tunic pruning a pomegranate tree, smiling kindly at the traveler.",
        "video_prompt": '0-3s: The camera settles into a serene handheld shot as an elderly gardener in a coarse wool tunic looks up from pruning a pomegranate tree with a gentle smile. 3-7s: Mia smiles warmly with profound relief, whispering to the camera "This sweet gardener just handed me a fresh sprig of mountain thyme without asking a single question. Pure Mesopotamian kindness." 7-10s: The old man points his weathered finger toward an ornate spiral staircase leading directly to the summit. Audio: no background music. Keep character dialogue and natural ambient sounds. Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.',
        "narrator_text": "This sweet gardener just handed me a fresh sprig of mountain thyme without asking a single question. Pure Mesopotamian kindness.",
        "character_names": ["Mia"]
    },
    # Act 6: Legacy & Grand Reveal (75-95%)
    {
        "order": 17,
        "prompt": "Ultra-wide shot emerging onto a magnificent high terrace: cascades of water pouring into carved turquoise pools, climbing red roses hanging over stone railings high above the city.",
        "video_prompt": '0-3s: Mia steps through the final floral archway out onto a sun-drenched marble terrace where azure water cascades into carved turquoise basins. 3-7s: She glides the camera across blooming climbing roses, whispering in total awe "Look at this... an entire river oasis floating eighty feet in the sky above the Mesopotamian desert." 7-10s: The camera tilts down toward the sparkling pools where red rose petals drift on the crystal water. Audio: no background music. Keep character dialogue and natural ambient sounds. Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.',
        "narrator_text": "Look at this... an entire river oasis floating eighty feet in the sky above the Mesopotamian desert.",
        "character_names": ["Mia", "Hanging Gardens of Babylon"]
    },
    {
        "order": 18,
        "prompt": "First-person POV looking down at the massive base of a towering Lebanese cedar tree planted on the rooftop terrace, thick soil banked high with stone retaining walls.",
        "video_prompt": '0-3s: The camera tilts slowly down from the dense emerald cedar branches to the colossal tree trunk rooted deeply in rich black river silt. 3-7s: Mia\'s voice resonates with deep historical respect "Just imagine the engineering... hauling thousands of tons of mountain soil up to this roof just so full-grown Lebanese cedars could flourish in the clouds." 7-10s: She walks forward toward the outer stone parapet overlooking the boundless desert horizon. Audio: no background music. Keep character dialogue and natural ambient sounds. Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.',
        "narrator_text": "Just imagine the engineering... hauling thousands of tons of mountain soil up to this roof just so full-grown Lebanese cedars could flourish in the clouds.",
        "character_names": ["Mia"]
    },
    {
        "order": 19,
        "prompt": "Ultra-wide selfie of the traveler standing on the overhanging balcony with blooming vines draping over the edge, Babylon spreading out below in the afternoon light.",
        "video_prompt": '0-3s: Mia stands at the edge of the cantilevered stone balcony as desert winds whip through lush climbing vines and her hair. 3-7s: She beams directly into the camera with an engaging smile "Historical myth busted: the gardens weren\'t \'hanging\' on ropes! The Greek term \'kremastos\' means \'overhanging\'—just like these dramatic terraces jutting out over the city!" 7-10s: She turns and walks smoothly over toward the sparkling fountain pool at the highest peak. Audio: no background music. Keep character dialogue and natural ambient sounds. Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.',
        "narrator_text": "Historical myth busted: the gardens weren't 'hanging' on ropes! The Greek term 'kremastos' means 'overhanging'—just like these dramatic terraces jutting out over the city!",
        "character_names": ["Mia", "Hanging Gardens of Babylon"]
    },
    {
        "order": 20,
        "prompt": "Close-up first-person POV of the traveler cupping both hands into the crystal-clear rushing water of the summit fountain pool, water splashing through fingers against the golden afternoon sun.",
        "video_prompt": '0-3s: First-person POV as Mia plunges both hands into the cool, bubbling summit fountain, lifting a handful of sparkling water into the golden afternoon sun. 3-7s: Mia speaks in a hushed, reverent voice "Ice-cold water from the Euphrates river, lifted eighty feet high into a living paradise in 570 BC. Touching this feels like pure magic." 7-10s: Water cascades through her fingers as the camera slowly rises up over the stone balustrade toward the horizon. Audio: no background music. Keep character dialogue and natural ambient sounds. Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.',
        "narrator_text": "Ice-cold water from the Euphrates river, lifted eighty feet high into a living paradise in 570 BC. Touching this feels like pure magic.",
        "character_names": ["Mia"]
    },
    {
        "order": 21,
        "prompt": "Standing at the highest point of the Hanging Gardens, majestic handheld panoramic shot looking out over all of ancient Babylon: the gleaming blue Ishtar Gate in the distance, the 90m Etemenanki ziggurat, and the Euphrates river reflecting golden hour light.",
        "video_prompt": '0-3s: Sweeping cinematic handheld pan from the peak terrace showing the grand panorama of ancient Babylon bathed in amber golden-hour light. 3-7s: Mia turns back into frame, her eyes shining with emotion "Behold... all of Babylon from the crown of the ancient world! The blue glazed Ishtar Gate, the towering Etemenanki ziggurat, and the Euphrates glowing like gold." 7-10s: The warm sunset breeze sweeps across the terraced palms as the golden sun dips toward the Mesopotamian horizon. Audio: no background music. Keep character dialogue and natural ambient sounds. Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.',
        "narrator_text": "Behold... all of Babylon from the crown of the ancient world! The blue glazed Ishtar Gate, the towering Etemenanki ziggurat, and the Euphrates glowing like gold.",
        "character_names": ["Mia", "Hanging Gardens of Babylon", "Ishtar Gate", "Etemenanki Ziggurat"]
    },
    # Act 7: Conclusion (95-100%)
    {
        "order": 22,
        "prompt": "Smartphone propped securely on an ancient carved stone balustrade draped with pink flowers, facing the young traveler sitting peacefully at sunset, the golden Euphrates river and purple evening sky behind her.",
        "video_prompt": '0-3s: Static frame from the propped smartphone showing Mia seated peacefully on the stone parapet as the sky turns into rich violet, amber, and gold. 3-7s: Mia gazes warmly into the lens, speaking with heartfelt sincerity "A wonder built entirely out of love for a queen who longed for home. Ancient Babylon in 570 BC is unforgettable. Where should we travel next?" 7-10s: She smiles softly, gives a gentle wave toward the camera, and taps the screen as the scene fades peacefully into twilight. Audio: no background music. Keep character dialogue and natural ambient sounds. Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.',
        "narrator_text": "A wonder built entirely out of love for a queen who longed for home. Ancient Babylon in 570 BC is unforgettable. Where should we travel next?",
        "character_names": ["Mia"]
    }
]

print("4. Creating 23 Scenes in Video...", flush=True)
created_scene_ids = []
for s in scenes_data:
    sp = {
        "video_id": vid,
        "display_order": s["order"],
        "prompt": s["prompt"],
        "video_prompt": s["video_prompt"],
        "narrator_text": s["narrator_text"],
        "character_names": s["character_names"],
        "chain_type": "ROOT"
    }
    s_req = urllib.request.Request(
        "http://127.0.0.1:8100/api/scenes",
        data=json.dumps(sp).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(s_req, timeout=15) as s_resp:
        sc = json.loads(s_resp.read())
        created_scene_ids.append((s["order"], sc["id"]))

print(f"Created {len(created_scene_ids)} scenes successfully!", flush=True)

# Update durations to 10.0
conn = sqlite3.connect("flow_agent.db")
conn.execute("UPDATE scene SET duration = 10.0 WHERE video_id = ?", (vid,))
conn.commit()
conn.close()

# 5. Submit Batch GENERATE_IMAGE for all 23 scenes
print("5. Submitting Batch GENERATE_IMAGE requests...", flush=True)
batch_requests = []
for order, sid in created_scene_ids:
    batch_requests.append({
        "type": "GENERATE_IMAGE",
        "scene_id": sid,
        "project_id": pid,
        "video_id": vid,
        "orientation": "HORIZONTAL"
    })

batch_payload = {"requests": batch_requests}
b_req = urllib.request.Request(
    "http://127.0.0.1:8100/api/requests/batch",
    data=json.dumps(batch_payload).encode("utf-8"),
    headers={"Content-Type": "application/json"}
)
with urllib.request.urlopen(b_req, timeout=30) as b_resp:
    b_res = json.loads(b_resp.read())
    print(f"Submitted batch successfully! Total requests: {len(b_res.get('requests', []))}", flush=True)

print("\nPROJECT CREATION & BATCH SUBMISSION COMPLETE!")
print(f"PID: {pid}")
print(f"VID: {vid}")
