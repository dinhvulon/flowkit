import sqlite3
import json
import urllib.request

PID = "ac50c619-1b31-4847-95d6-5379d02554c7"
VID = "dc2afa55-8a7f-42c3-bf8c-a13f580b6830"
ORI = "HORIZONTAL"

# Define the 7 target scenes with their exact prompt fixes
UPDATES = [
    {
        "order": 0,
        "name": "Scene 01",
        "id": "f4a1f353-8228-4382-8400-be8bc3a3900c",
        "prompt": (
            "Cinematic documentary medium-wide vlog shot of young traveler Mia standing on the dusty "
            "Euphrates riverbank in ancient Babylon in 570 BC. She wears a desert-sand linen tunic with "
            "golden woven sash, smiling warmly facing the camera. In the background, an ancient wooden "
            "ox-cart with large spoked wooden wheels rolls along the dirt road, with the shimmering Euphrates "
            "river and the colossal terraced green Hanging Gardens rising in the distance under bright morning "
            "desert sunlight. Photorealistic documentary realism, 8k resolution, authentic ancient textures. "
            "Negative: modern clothes, smartphone, selfie stick, phone clamp, car, modern gadget, distorted hands."
        ),
        "video_prompt": (
            "0-3s: Smooth eye-level vlog shot of Mia standing near the Euphrates riverbank as an ancient wooden "
            "ox-cart rumbles past along the dirt road behind her. Mia turns directly toward the lens with bright "
            "smiling eyes. 3-7s: Mia says \"You guys... welcome to Babylon, 570 BC! And right behind me is the "
            "legendary Hanging Gardens!\" 7-10s: She gestures toward the colossal green terraces as desert palm "
            "fronds sway gently in the warm breeze. Audio: no background music. Keep character dialogue and "
            "natural ambient sounds. Negative: second smartphone, floating phone, subtitles, captions, watermark, "
            "text on screen, logo, blurry faces, distorted hands."
        ),
        "characters": ["Mia", "Mia Outfit"]
    },
    {
        "order": 2,
        "name": "Scene 03",
        "id": "27404416-f641-4587-8340-f0f40c8ef3b7",
        "prompt": (
            "Eye-level first-person POV looking across the sparkling green waters of the Euphrates river in "
            "ancient Babylon. Directly in the foreground center of the frame, inside ONE single circular black "
            "bitumen-coated quffa basket boat, an ancient muscular Babylonian boatman in coarse linen loincloth "
            "stands firmly inside the quffa boat, holding a broad wooden paddle in both hands as he rows vigorously. "
            "The quffa boat carries baskets of dark rich river soil and young date palm saplings. Behind the boat, "
            "the stone docks of Babylon and royal limestone aqueducts rise under warm morning sunlight. Authentic "
            "Mesopotamian archaeology, documentary realism. Negative: empty boat, boat with no rower, unmanned boat, "
            "motorboat, modern boat, modern clothes, smartphone."
        ),
        "video_prompt": (
            "0-3s: First-person eye-level POV tracking the muscular Babylonian boatman standing inside the circular "
            "black bitumen quffa boat, rowing steadily with his broad wooden paddle across the shimmering Euphrates river. "
            "3-7s: Mia's voice speaks with deep fascination \"Every single drop of water and every basket of rich soil "
            "feeding those rooftop trees starts right here from this river.\" 7-10s: The circular boat glides toward a "
            "timber dock as the camera pans toward the stone masonry of the royal aqueduct. Audio: no background music. "
            "Keep character dialogue and natural ambient sounds. Negative: empty boat, modern boat, subtitles, captions, "
            "watermark, text on screen, logo, blurry faces."
        ),
        "characters": []
    },
    {
        "order": 14,
        "name": "Scene 15",
        "id": "e2976cc7-5a59-41c3-a573-b7e3616ed969",
        "prompt": (
            "Dynamic cinematic medium action shot of young female traveler Mia sprinting through a vaulted stone gallery "
            "behind a towering curtain of falling water in the Hanging Gardens of Babylon. Both of her hands are completely "
            "open and empty at her sides, athletic running motion, honey-blonde ponytail trailing behind her, intense yet "
            "determined expression on her face, wearing her desert-sand linen tunic with woven waist sash. Cascades of misty "
            "water spray sparkle in the background between massive ancient carved limestone pillars. Atmospheric ancient "
            "bronze torchlight casting warm golden reflections on wet paving stones. Negative: holding lantern, lamp in hand, "
            "carrying torch, flashlight, modern clothes, smartphone, extra hands, distorted fingers."
        ),
        "video_prompt": (
            "0-3s: High-energy chase camera tracking Mia sprinting with both hands empty through a shadowy stone gallery "
            "directly behind a thundering curtain of falling water. 3-7s: Water spray drenches her face; she glances backward "
            "into the camera, panting heavily \"Running for my life behind a 2,500-year-old waterfall... completely terrifying "
            "but insane!\" 7-10s: She leaps over a stone water sluice, dodging sharply around a mossy arched corner into an "
            "upper courtyard. Audio: no background music. Keep character dialogue and natural ambient sounds. Negative: holding "
            "lantern, lamp in hand, subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands."
        ),
        "characters": ["Mia", "Mia Outfit"]
    },
    {
        "order": 15,
        "name": "Scene 16",
        "id": "19a26b18-4b08-40c0-897b-99b36ca5b421",
        "prompt": (
            "Cinematic eye-level shot of young female traveler Mia inside a quiet, sheltered botanical nursery terrace in "
            "the Hanging Gardens of Babylon. She has just pulled shut a heavy weathered cedar wood door, resting one hand "
            "against the closed wooden door latch and her other hand resting on her chest, catching her breath with wide "
            "alert eyes and an expression of profound relief. She wears her signature desert-sand linen tunic with woven "
            "waist sash. Surrounded by terracotta pots with young date palms and woven reed shade awnings, warm golden "
            "afternoon sunbeams streaming across the earthen floor. Negative: open door, asleep, eyes closed, modern door, "
            "modern pots, distorted hands, smartphone."
        ),
        "video_prompt": (
            "0-3s: Mia steps through a weathered cedar gate, pulls it shut until the wooden latch clicks, and slides down "
            "against the sun-baked mudbrick wall. 3-7s: She takes deep shuddering breaths, pressing a trembling hand to her "
            "chest \"Okay... we lost them. The guards just thundered down toward the lower barracks. We're safe in the upper "
            "nursery.\" 7-10s: The loud pursuit fades into distant courtyard echoes, replaced by gentle afternoon bird calls "
            "in the quiet nursery. Audio: no background music. Keep character dialogue and natural ambient sounds. Negative: "
            "subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands."
        ),
        "characters": ["Mia", "Mia Outfit"]
    },
    {
        "order": 18,
        "name": "Scene 19",
        "id": "06c66a21-bbc7-476d-bc01-06dc1d2f0337",
        "prompt": (
            "Authentic ancient archaeological documentary shot, eye-level POV looking at the colossal gnarled trunk and "
            "massive roots of an ancient Lebanese cedar tree planted on a high stone terrace of the Hanging Gardens of "
            "Babylon. The gigantic tree base is encircled by weathered mudbrick and dry-stacked limestone retaining walls "
            "filled with deep dark alluvial soil and moss. In the background, ancient Babylonian rooftop gardens and "
            "terraced brick battlements stretch out under afternoon desert sunlight. Pure ancient Mesopotamia. "
            "Negative: metal railing, steel pipes, modern handrail, modern fence, modern jewelry, wedding ring, modern garden, smartphone."
        ),
        "video_prompt": (
            "0-3s: The camera tilts slowly down from the dense emerald cedar branches to the colossal tree trunk rooted deeply "
            "in rich black river silt on the stone terrace. 3-7s: Mia's voice resonates with deep historical respect \"Just imagine "
            "the engineering... hauling thousands of tons of mountain soil up to this roof just so full-grown Lebanese cedars "
            "could flourish in the clouds.\" 7-10s: The camera pans across the ancient stone terrace overlooking the boundless "
            "desert horizon. Audio: no background music. Keep character dialogue and natural ambient sounds. Negative: modern "
            "metal railing, modern pipes, subtitles, captions, watermark, text on screen, logo, blurry faces."
        ),
        "characters": []
    },
    {
        "order": 19,
        "name": "Scene 20",
        "id": "0fa349bb-c3db-4049-bab8-de4ddf0c3a8a",
        "prompt": (
            "Wide-angle 0.5x front-camera vlog shot of young female traveler Mia standing on a monumental cantilevered "
            "limestone balcony overlooking ancient Babylon. Mia is standing near the center of the frame smiling radiantly "
            "toward the camera, both of her hands resting naturally on the ancient stone balustrade, wearing her signature "
            "desert-sand linen tunic with woven waist sash and blonde ponytail. Below the overhanging balcony, ancient "
            "Babylonian mudbrick city streets and palm groves stretch into the distance under warm afternoon sunlight. "
            "Lush pink bougainvillea vines drape over the carved stone railing. Only TWO hands belonging to Mia. "
            "Negative: third hand, floating hand, extra arm, extra hand reaching into frame, holding phone, smartphone, "
            "selfie stick, modern gadget, distorted fingers."
        ),
        "video_prompt": (
            "0-3s: Ultra-wide 0.5x vlog camera looking at Mia standing on the cantilevered stone balcony as desert winds whip "
            "through lush climbing vines and her blonde ponytail. 3-7s: Mia beams directly into the camera lens with an "
            "engaging smile \"Historical myth busted: the gardens were not hanging on ropes! The Greek term kremastos means "
            "overhanging - just like these dramatic terraces jutting out over the city!\" 7-10s: She turns smoothly to walk toward "
            "the sparkling summit fountain pool in the background. Audio: no background music. Keep character dialogue and "
            "natural ambient sounds. Negative: third hand, extra arm, holding phone in hand, smartphone, selfie stick, subtitles, "
            "captions, watermark, text on screen, logo, blurry faces, distorted hands."
        ),
        "characters": ["Mia", "Mia Outfit"]
    },
    {
        "order": 22,
        "name": "Scene 23",
        "id": "5695d17a-2861-4987-81c6-8070caaa682c",
        "prompt": (
            "Candid documentary eye-level shot of young female traveler Mia seated on the high summit stone balustrade of "
            "the Hanging Gardens of Babylon at sunset. The camera is propped securely on the opposite stone ledge facing her. "
            "Mia sits sideways along the ancient carved stone parapet draped with climbing roses, both hands resting relaxed on "
            "the warm limestone beside her hips, looking toward the camera with a heartfelt, peaceful smile. Far below and "
            "behind her, the Euphrates river and ancient Babylon glow in rich golden, amber, and deep violet twilight. Hands "
            "completely empty, natural travel vlog signoff portrait. Negative: holding phone, smartphone in hand, selfie stick, "
            "phone clamp, camera, modern clothes, studio lighting, distorted fingers."
        ),
        "video_prompt": (
            "0-3s: Static eye-level camera shot looking at Mia seated peacefully on the stone parapet as the sky turns into rich "
            "violet, amber, and gold. 3-7s: Mia gazes warmly into the lens, speaking with heartfelt sincerity \"A wonder built "
            "entirely out of love for a queen who longed for home. Ancient Babylon in 570 BC is unforgettable. Where should we "
            "travel next?\" 7-10s: She smiles softly, gives a gentle wave toward the camera with her right hand, and the scene "
            "peacefully fades into evening twilight. Audio: no background music. Keep character dialogue and natural ambient "
            "sounds. Negative: holding phone, smartphone, selfie stick, subtitles, captions, watermark, text on screen, logo, "
            "blurry faces, distorted hands."
        ),
        "characters": ["Mia", "Mia Outfit"]
    }
]

# 1. Update SQLite DB
conn = sqlite3.connect("flow_agent.db")
cur = conn.cursor()

batch_requests = []

for item in UPDATES:
    sid = item["id"]
    p = item["prompt"]
    vp = item["video_prompt"]
    chars_json = json.dumps(item["characters"]) if item["characters"] else "[]"
    
    cur.execute("""
        UPDATE scene 
        SET prompt=?, image_prompt=?, video_prompt=?, character_names=?,
            horizontal_image_status='PENDING', horizontal_video_status='PENDING'
        WHERE id=?
    """, (p, p, vp, chars_json, sid))

    batch_requests.append({
        "type": "REGENERATE_IMAGE",
        "scene_id": sid,
        "project_id": PID,
        "video_id": VID,
        "orientation": ORI
    })

conn.commit()
conn.close()
print(f"Updated database for all {len(UPDATES)} target scenes.")

# 2. Submit batch REGENERATE_IMAGE requests
req_payload = json.dumps({"requests": batch_requests}).encode('utf-8')
req = urllib.request.Request(
    "http://127.0.0.1:8100/api/requests/batch",
    data=req_payload,
    headers={"Content-Type": "application/json"}
)

try:
    resp = urllib.request.urlopen(req)
    data = json.loads(resp.read().decode())
    print(f"Successfully submitted batch of {len(data)} REGENERATE_IMAGE requests!")
except Exception as e:
    print(f"Error submitting batch: {e}")
