import sqlite3
import json

db_path = 'flow_agent.db'
video_id = '71909a60-29f7-460e-807c-ed48b8a12ad1'

scenes_10s_data = [
    # Act 1: Hook (0-5%)
    {
        "order": 0,
        "id": "5fc05aeb-c42e-4721-828f-7dcd560a9104",
        "video_prompt": (
            '0-3s: Mia is already standing on the sunlit Euphrates riverbank holding her selfie stick, looking toward the distant city. '
            'The wooden ox cart on the left rumbles slowly along the dirt path as Mia smoothly turns her head and body toward the camera, smiling warmly with excitement. '
            '3-7s: Looking straight into the lens with wide sparkling eyes, Mia says "You guys... welcome to Babylon, 570 BC! And right behind me is the legendary Hanging Gardens!" '
            '7-10s: She gestures excitedly with her free hand toward the colossal green terraces as desert palm fronds sway gently in the warm breeze. '
            'Audio: no background music. Keep character dialogue and natural ambient sounds. '
            'Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands, morphing, sudden pop-in.'
        ),
        "narrator_text": "You guys... welcome to Babylon, 570 BC! And right behind me is the legendary Hanging Gardens!"
    },
    {
        "order": 1,
        "id": "d06a8ae1-f82d-4e4c-becb-010412db9703",
        "video_prompt": (
            '0-3s: Handheld selfie tracking Mia walking briskly along the bustling dirt embankment as Babylonian boatmen shout near the docks. '
            '3-7s: Mia leans in close to the lens, speaking in a warm storytelling whisper "King Nebuchadnezzar built this entire mountain of green for Queen Amytis because she missed the forested hills of Media." '
            '7-10s: She looks back toward the river as two donkeys laden with woven river reed hampers walk past in the foreground, briefly occluding the frame. '
            'Audio: no background music. Keep character dialogue and natural ambient sounds. '
            'Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.'
        ),
        "narrator_text": "King Nebuchadnezzar built this entire mountain of green for Queen Amytis because she missed the forested hills of Media."
    },
    # Act 2: Everyday Life / Đời thường (5-40%)
    {
        "order": 2,
        "id": "d536ed90-f6f5-45df-924b-b81806365ff6",
        "video_prompt": (
            '0-3s: Eye-level first-person POV tracking circular black bitumen-coated quffa boats gliding across the glittering Euphrates river. '
            '3-7s: Mia\'s voice captures deep fascination "Every single drop of water and every basket of rich soil feeding those rooftop trees starts right here from this river." '
            '7-10s: The camera whips fast to the right with heavy natural motion blur, settling on towering timber scaffolding and brick pillars. '
            'Audio: no background music. Keep character dialogue and natural ambient sounds. '
            'Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.'
        ),
        "narrator_text": "Every single drop of water and every basket of rich soil feeding those rooftop trees starts right here from this river."
    },
    {
        "order": 3,
        "id": "5247145e-390e-4828-b3b8-cbc69bcf76b7",
        "video_prompt": (
            '0-3s: Camera settles from the whip pan looking up at the colossal wooden chain-of-buckets wheel creaking steadily as it lifts tons of river water upward. '
            '3-7s: Mia steps into the lower third of the frame, shielding her eyes and shouting over the rushing water "Look at this mechanical chain pump! 2,500 years ago, lifting thousands of gallons into the desert sky every hour!" '
            '7-10s: Cool water droplets mist over the lens as the camera tilts up along the brick aqueduct channel. '
            'Audio: no background music. Keep character dialogue and natural ambient sounds. '
            'Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.'
        ),
        "narrator_text": "Look at this mechanical chain pump! 2,500 years ago, lifting thousands of gallons into the desert sky every hour!"
    },
    {
        "order": 4,
        "id": "5c24c463-b4d1-4a99-bd81-fc1cee91d264",
        "video_prompt": (
            '0-3s: Close-up first-person POV of Mia\'s fingertips pressing against the firm, black waterproof asphalt layer and woven reeds between the baked brick courses. '
            '3-7s: Mia whispers in amazement "Feel this texture. Natural tar and reeds waterproofing the stone so water doesn\'t flood the royal palace chambers below." '
            '7-10s: A Babylonian laborer carrying a woven basket walks past in front of the lens, his fringed linen tunic creating a natural wipe cut. '
            'Audio: no background music. Keep character dialogue and natural ambient sounds. '
            'Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.'
        ),
        "narrator_text": "Feel this texture. Natural tar and reeds waterproofing the stone so water doesn't flood the royal palace chambers below."
    },
    {
        "order": 5,
        "id": "d7ecb974-e9a4-4f3c-be92-2df4da6f84b7",
        "video_prompt": (
            '0-3s: Mia walks beneath towering baked-brick arches that resemble a cavernous underground crypt supporting the mountain of trees above. '
            '3-7s: She tilts her selfie stick upward, looking around in awe and saying "Walking under these colossal vaults feels like being inside an artificial mountain. You can actually hear water trickling above our heads!" '
            '7-10s: Shafts of bright sunlight pierce through gaps in the masonry as she steps forward through an arched stone portal. '
            'Audio: no background music. Keep character dialogue and natural ambient sounds. '
            'Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.'
        ),
        "narrator_text": "Walking under these colossal vaults feels like being inside an artificial mountain. You can actually hear water trickling above our heads!"
    },
    {
        "order": 6,
        "id": "06798176-ccf1-4d9f-962b-90f68201e038",
        "video_prompt": (
            '0-3s: Mia weaves through colorful wooden stalls piled high with fresh garden harvests, split ruby-red pomegranates and green figs glistening in the light. '
            '3-7s: The vendor smiles warmly and offers a ripe fig; Mia laughs with delight and says "The aromas here are unbelievable... wild pomegranates, mountain thyme, and sweet figs fresh off the royal terraces!" '
            '7-10s: She smiles thanking the vendor in Akkadian, then sets her smartphone down against a terracotta jug on a low wooden table. '
            'Audio: no background music. Keep character dialogue and natural ambient sounds. '
            'Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.'
        ),
        "narrator_text": "The aromas here are unbelievable... wild pomegranates, mountain thyme, and sweet figs fresh off the royal terraces!"
    },
    {
        "order": 7,
        "id": "f5ef363c-ba1e-487b-8053-f9c1a24cf7c4",
        "video_prompt": (
            '0-3s: Static wide frame from the propped smartphone showing Mia sitting relaxed on a reed stool, taking a delicate bite of the ripe sweet fig. '
            '3-7s: She closes her eyes in pure culinary bliss, leaning toward the camera and whispering "Honestly, tasting a fig picked directly from the Hanging Gardens of Babylon? This is absolute bucket-list perfection." '
            '7-10s: She takes a sip of cool water from her unglazed clay cup, smiles at the camera, and picks the phone back up. '
            'Audio: no background music. Keep character dialogue and natural ambient sounds. '
            'Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.'
        ),
        "narrator_text": "Honestly, tasting a fig picked directly from the Hanging Gardens of Babylon? This is absolute bucket-list perfection."
    },
    {
        "order": 8,
        "id": "e650db03-1b31-44b7-b070-0830382d4b0e",
        "video_prompt": (
            '0-3s: Smooth first-person tracking forward up the stone steps beside a crystal-clear stream gurgling down a carved limestone canal. '
            '3-7s: Mia\'s voice observes with admiration "This gravity-fed aqueduct system circulates water to every single terrace like a living biological bloodstream in the desert." '
            '7-10s: Overhanging maidenhair ferns and fragrant jasmine blossoms brush softly across the camera lens. '
            'Audio: no background music. Keep character dialogue and natural ambient sounds. '
            'Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.'
        ),
        "narrator_text": "This gravity-fed aqueduct system circulates water to every single terrace like a living biological bloodstream in the desert."
    },
    {
        "order": 9,
        "id": "3267ed4e-0d9e-4ce6-ac7a-aa25b0a94908",
        "video_prompt": (
            '0-3s: Mia\'s hand enters the frame holding a coiled silver wire as the merchant carefully balances hematite stone weights on the bronze scales. '
            '3-7s: Mia whispers in fascination "No minted coins here in 570 BC... just little curls of silver wire called shekels, weighed by hand to trade for rare mountain spices." '
            '7-10s: The merchant hands her a bundle of fragrant mountain herbs; Mia tucks a blossom behind her ear and turns toward a grand stairway. '
            'Audio: no background music. Keep character dialogue and natural ambient sounds. '
            'Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.'
        ),
        "narrator_text": "No minted coins here in 570 BC... just little curls of silver wire called shekels, weighed by hand to trade for rare mountain spices."
    },
    # Act 3: Power & Reveal #1 / Quyền lực (40-55%)
    {
        "order": 10,
        "id": "f2f004a3-ee77-4ed4-9eab-aa9afd893335",
        "video_prompt": (
            '0-3s: Mia walks up the wide stone staircase, the warm Mesopotamian wind rustling through cypress branches and fluttering her blonde hair. '
            '3-7s: She lowers her voice to an anxious whisper, glancing left and right "We\'re sneaking up toward Queen Amytis\'s private upper sanctuary... definitely a restricted royal zone for unauthorized travelers." '
            '7-10s: She turns her back completely to the camera to check the landing ahead, her ponytail and back filling the frame. '
            'Audio: no background music. Keep character dialogue and natural ambient sounds. '
            'Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.'
        ),
        "narrator_text": "We're sneaking up toward Queen Amytis's private upper sanctuary... definitely a restricted royal zone for unauthorized travelers."
    },
    {
        "order": 11,
        "id": "b4ba835a-aa20-46d4-85cd-c8c0fa0d7786",
        "video_prompt": (
            '0-3s: Camera opens tight on the back of Mia\'s hair; she spins around 180 degrees, revealing a breathtaking floral terrace and two tall Babylonian guards standing guard. '
            '3-7s: Her eyes widen in stunned shock as she murmurs "Look at this grand terrace... an explosion of royal flowers! But wait... armed imperial guards are patrolling right ahead!" '
            '7-10s: She ducks swiftly to the right, crouching low behind an ornamental carved limestone column. '
            'Audio: no background music. Keep character dialogue and natural ambient sounds. '
            'Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.'
        ),
        "narrator_text": "Look at this grand terrace... an explosion of royal flowers! But wait... armed imperial guards are patrolling right ahead!"
    },
    {
        "order": 12,
        "id": "51fb503b-55d2-4ea5-b604-102911d935bb",
        "video_prompt": (
            '0-3s: Handheld camera tilted low as Mia crouches behind blooming purple bougainvillea vines while bronze-armored guards march along the parapet thirty feet away. '
            '3-7s: She whispers urgently into the microphone with rapid shallow breaths "Stay quiet... if they catch someone with a glowing camera in the Queen\'s private botanical court, I\'m done for." '
            '7-10s: Heavy bronze greaves and leather boots clatter loudly on stone as guards pass just out of sight. '
            'Audio: no background music. Keep character dialogue and natural ambient sounds. '
            'Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.'
        ),
        "narrator_text": "Stay quiet... if they catch someone with a glowing camera in the Queen's private botanical court, I'm done for."
    },
    # Act 4: High Danger & Climax / Cao trào nguy hiểm (55-70%)
    {
        "order": 13,
        "id": "b614bf6c-3507-4257-aa32-286b84048188",
        "video_prompt": (
            '0-3s: Through parted palm fronds, Queen Amytis\'s royal court glides past in embroidered Median robes and silk parasols amidst fragrant myrrh incense. '
            '3-7s: A tall royal officer with a spear suddenly snaps his head around, his eyes locking directly onto Mia\'s phone! Mia gasps in terror "He sees the camera! RUN!" '
            '7-10s: She spins abruptly around, sprinting down the stone terrace as alarmed Akkadian shouts echo behind her. '
            'Audio: no background music. Keep character dialogue and natural ambient sounds. '
            'Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.'
        ),
        "narrator_text": "He sees the camera! RUN!"
    },
    {
        "order": 14,
        "id": "141c09bd-3f94-45bb-b924-50f1b198725f",
        "video_prompt": (
            '0-3s: High-energy shaky handheld chase camera as Mia sprints full tilt through a shadowy stone gallery directly behind a thundering curtain of falling water. '
            '3-7s: Water spray drenches her face; she glances backward into the camera, panting heavily "Running for my life behind a 2,500-year-old waterfall... completely terrifying but insane!" '
            '7-10s: She leaps over a stone water sluice, dodging sharply around a mossy arched corner into a side garden. '
            'Audio: no background music. Keep character dialogue and natural ambient sounds. '
            'Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.'
        ),
        "narrator_text": "Running for my life behind a 2,500-year-old waterfall... completely terrifying but insane!"
    },
    {
        "order": 15,
        "id": "c19d1d45-c200-4815-a46a-7ff470d413d0",
        "video_prompt": (
            '0-3s: Mia dashes through a weathered cedar gate, pulls it shut until the wooden latch clicks, and slides down against the sun-baked mudbrick wall. '
            '3-7s: She takes deep shuddering breaths, pressing a trembling hand to her chest "Okay... we lost them. The guards just thundered down toward the lower barracks. We\'re safe in the upper nursery." '
            '7-10s: The loud pursuit fades into distant courtyard echoes, replaced by gentle afternoon bird calls in the quiet nursery. '
            'Audio: no background music. Keep character dialogue and natural ambient sounds. '
            'Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.'
        ),
        "narrator_text": "Okay... we lost them. The guards just thundered down toward the lower barracks. We're safe in the upper nursery."
    },
    # Act 5: Decompression / Hạ nhịp (70-75%)
    {
        "order": 16,
        "id": "17b622d1-72cc-4852-8090-17d0d181f1c8",
        "video_prompt": (
            '0-3s: The camera settles into a serene handheld shot as an elderly gardener in a coarse wool tunic looks up from pruning a pomegranate tree with a gentle smile. '
            '3-7s: Mia smiles warmly with profound relief, whispering to the camera "This sweet gardener just handed me a fresh sprig of mountain thyme without asking a single question. Pure Mesopotamian kindness." '
            '7-10s: The old man points his weathered finger toward an ornate spiral staircase leading directly to the summit. '
            'Audio: no background music. Keep character dialogue and natural ambient sounds. '
            'Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.'
        ),
        "narrator_text": "This sweet gardener just handed me a fresh sprig of mountain thyme without asking a single question. Pure Mesopotamian kindness."
    },
    # Act 6: Legacy & Grand Reveal / Di sản (75-95%)
    {
        "order": 17,
        "id": "17de158e-dee4-4a6c-b87d-51036a891d13",
        "video_prompt": (
            '0-3s: Mia steps through the final floral archway out onto a sun-drenched marble terrace where azure water cascades into carved turquoise basins. '
            '3-7s: She glides the camera across blooming climbing roses, whispering in total awe "Look at this... an entire river oasis floating eighty feet in the sky above the Mesopotamian desert." '
            '7-10s: The camera tilts down toward the sparkling pools where red rose petals drift on the crystal water. '
            'Audio: no background music. Keep character dialogue and natural ambient sounds. '
            'Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.'
        ),
        "narrator_text": "Look at this... an entire river oasis floating eighty feet in the sky above the Mesopotamian desert."
    },
    {
        "order": 18,
        "id": "b04474d4-4c36-4732-a45b-2717a305f54f",
        "video_prompt": (
            '0-3s: The camera tilts slowly down from the dense emerald cedar branches to the colossal tree trunk rooted deeply in rich black river silt. '
            '3-7s: Mia\'s voice resonates with deep historical respect "Just imagine the engineering... hauling thousands of tons of mountain soil up to this roof just so full-grown Lebanese cedars could flourish in the clouds." '
            '7-10s: She walks forward toward the outer stone parapet overlooking the boundless desert horizon. '
            'Audio: no background music. Keep character dialogue and natural ambient sounds. '
            'Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.'
        ),
        "narrator_text": "Just imagine the engineering... hauling thousands of tons of mountain soil up to this roof just so full-grown Lebanese cedars could flourish in the clouds."
    },
    {
        "order": 19,
        "id": "39588e4a-8140-440b-b233-f2a9325af8ad",
        "video_prompt": (
            '0-3s: Mia stands at the edge of the cantilevered stone balcony as desert winds whip through lush climbing vines and her hair. '
            '3-7s: She beams directly into the camera with an engaging smile "Historical myth busted: the gardens weren\'t \'hanging\' on ropes! The Greek term \'kremastos\' means \'overhanging\'—just like these dramatic terraces jutting out over the city!" '
            '7-10s: She turns and walks smoothly over toward the sparkling fountain pool at the highest peak. '
            'Audio: no background music. Keep character dialogue and natural ambient sounds. '
            'Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.'
        ),
        "narrator_text": "Historical myth busted: the gardens weren't 'hanging' on ropes! The Greek term 'kremastos' means 'overhanging'—just like these dramatic terraces jutting out over the city!"
    },
    {
        "order": 20,
        "id": "46944c6a-94bc-495a-8c50-c42ea07cdc09",
        "video_prompt": (
            '0-3s: First-person POV as Mia plunges both hands into the cool, bubbling summit fountain, lifting a handful of sparkling water into the golden afternoon sun. '
            '3-7s: Mia speaks in a hushed, reverent voice "Ice-cold water from the Euphrates river, lifted eighty feet high into a living paradise in 570 BC. Touching this feels like pure magic." '
            '7-10s: Water cascades through her fingers as the camera slowly rises up over the stone balustrade toward the horizon. '
            'Audio: no background music. Keep character dialogue and natural ambient sounds. '
            'Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.'
        ),
        "narrator_text": "Ice-cold water from the Euphrates river, lifted eighty feet high into a living paradise in 570 BC. Touching this feels like pure magic."
    },
    {
        "order": 21,
        "id": "4db4a4f3-d3e3-4636-8ee8-f6c240a112c4",
        "video_prompt": (
            '0-3s: Sweeping cinematic handheld pan from the peak terrace showing the grand panorama of ancient Babylon bathed in amber golden-hour light. '
            '3-7s: Mia turns back into frame, her eyes shining with emotion "Behold... all of Babylon from the crown of the ancient world! The blue glazed Ishtar Gate, the towering Etemenanki ziggurat, and the Euphrates glowing like gold." '
            '7-10s: The warm sunset breeze sweeps across the terraced palms as the golden sun dips toward the Mesopotamian horizon. '
            'Audio: no background music. Keep character dialogue and natural ambient sounds. '
            'Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.'
        ),
        "narrator_text": "Behold... all of Babylon from the crown of the ancient world! The blue glazed Ishtar Gate, the towering Etemenanki ziggurat, and the Euphrates glowing like gold."
    },
    # Act 7: Conclusion / Kết trầm (95-100%)
    {
        "order": 22,
        "id": "52d929dd-d288-4e63-b58d-12a3ae27559f",
        "video_prompt": (
            '0-3s: Static frame from the propped smartphone showing Mia seated peacefully on the stone parapet as the sky turns into rich violet, amber, and gold. '
            '3-7s: Mia gazes warmly into the lens, speaking with heartfelt sincerity "A wonder built entirely out of love for a queen who longed for home. Ancient Babylon in 570 BC is unforgettable. Where should we travel next?" '
            '7-10s: She smiles softly, gives a gentle wave toward the camera, and taps the screen as the scene fades peacefully into twilight. '
            'Audio: no background music. Keep character dialogue and natural ambient sounds. '
            'Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.'
        ),
        "narrator_text": "A wonder built entirely out of love for a queen who longed for home. Ancient Babylon in 570 BC is unforgettable. Where should we travel next?"
    }
]

def update_scenes():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    updated_count = 0
    for scene in scenes_10s_data:
        c.execute('''
            UPDATE scene
            SET video_prompt = ?,
                narrator_text = ?,
                duration = 10.0
            WHERE id = ? AND video_id = ?
        ''', (scene['video_prompt'], scene['narrator_text'], scene['id'], video_id))
        if c.rowcount > 0:
            updated_count += 1
            
    conn.commit()
    conn.close()
    print(f"Successfully updated {updated_count}/{len(scenes_10s_data)} scenes to 10s format in {db_path}!")

if __name__ == '__main__':
    update_scenes()
