#!/usr/bin/env python3
"""
FlowKit — Script Khởi Tạo Dự Án: Babylon 570 BC (Time Travel POV Vlog)
Thời kỳ vua Nebuchadnezzar II, Cổng Ishtar, Đường Diễu Hành Processional Way, Tháp Etemenanki.
Chuẩn 23 Beat theo format video mẫu 10 phút, màn hình 16:9 HORIZONTAL.
"""

import json
import os
import sys
import urllib.request
import urllib.error
import sqlite3

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

BASE_URL = os.environ.get("FLOWKIT_API_URL", "http://127.0.0.1:8100")
FLOW_PROJECT_ID = "6224591f-b884-42f2-8f57-613bc86d66fb"
MIA_MEDIA_ID = "3904fece-f12e-47ef-9018-361f1a74f315"


def flush_stale_queue():
    print("[*] BƯỚC 0: Dọn dẹp hàng đợi cũ (Rule 21)...")
    db_path = "flow_agent.db"
    if os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        conn.execute("UPDATE request SET status='FAILED' WHERE status='PENDING'")
        conn.commit()
        conn.close()
        print("    -> Đã flush sạch các PENDING request tồn đọng.")


def api_request(endpoint: str, method: str = "GET", data: dict = None) -> dict:
    url = f"{BASE_URL}{endpoint}"
    payload = json.dumps(data, ensure_ascii=False).encode("utf-8") if data else None
    headers = {"Content-Type": "application/json; charset=utf-8"} if data else {}
    req = urllib.request.Request(url, data=payload, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as res:
            return json.loads(res.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8", errors="ignore")
        print(f"[-] HTTP Error {e.code} on {endpoint}: {err_msg}", file=sys.stderr)
        raise
    except Exception as e:
        print(f"[-] Lỗi kết nối {endpoint}: {e}", file=sys.stderr)
        raise


def create_project() -> tuple[str, str]:
    print("\n[*] BƯỚC 1: Tạo dự án mới trên FlowKit...")

    project_payload = {
        "name": "Time Travel Vlog — Babylon 570 BC",
        "description": "POV time-travel vlog: a modern traveler with a selfie stick explores Babylon in 570 BC during the golden reign of Nebuchadnezzar II, wandering vibrant markets, clay tablet archives, the grand Ishtar Gate, and the 90m Etemenanki ziggurat.",
        "story": "In 570 BC, Babylon stands at the absolute zenith of the Neo-Babylonian Empire under Nebuchadnezzar II. A young vlogger named Mia, disguised in native Mesopotamian linen robes but carrying a short selfie stick with an ultra-wide smartphone, navigates the bustling riverfront markets where silver shekels buy barley beer and sweet dates. She observes scribes pressing cuneiform into wet clay, feasts at a street stall, and gets caught in the overwhelming majesty of the royal procession along the Processional Way. Narrowly escaping royal guards, she catches an ox cart into the outer sanctuary, gazes upon the breathtaking cobalt-blue Ishtar Gate, and reaches the towering Etemenanki ziggurat as the desert sun dips below the Euphrates.",
        "language": "en",
        "material": "realistic",
        "flow_project_id": FLOW_PROJECT_ID,
        "allow_voice": True,
        "allow_music": False,
        "characters": [
            {
                "name": "Mia",
                "entity_type": "character",
                "description": "Mia, a 23-year-old Western woman with a soft oval face, hazel-green eyes, full rosy lips, delicate features, honey-blonde hair with parted curtain bangs in a textured mid-high ponytail, wearing an era-appropriate deep cream and indigo-bordered Mesopotamian linen tunic with fringed hem and a woven sash, holding a short black selfie stick with a smartphone on ultra-wide 0.5x front camera, arm visible at the edge of frame.",
                "voice_description": "Warm, curious American English, casual vlog tone, breathy when amazed, hushed whisper when nervous."
            },
            {
                "name": "Ishtar Gate",
                "entity_type": "location",
                "description": "Babylon Ishtar Gate, monumental double gateway of vibrant deep-blue glazed bricks adorned with alternating relief rows of yellow and white sirrush dragons and aurochs bulls, grand crenellated battlements."
            },
            {
                "name": "Etemenanki Ziggurat",
                "entity_type": "location",
                "description": "Etemenanki great ziggurat of Babylon, massive seven-tiered mud-brick stepped tower rising 90 meters high beside the Esagila temple, blue glazed shrine on the top terrace against the open Mesopotamian sky."
            },
            {
                "name": "Processional Way",
                "entity_type": "location",
                "description": "Babylon Processional Way, broad straight avenue paved with large limestone and breccia slabs, flanked by high defensive walls lined with over one hundred walking lion reliefs on turquoise-blue glazed brick."
            },
            {
                "name": "Babylonian Market",
                "entity_type": "location",
                "description": "Ancient Babylonian street market along the Euphrates, sun-baked mudbrick buildings, timber fabric awnings, woven date palm mats, earthen jars, dried date baskets, merchants in fringed wool tunics."
            }
        ]
    }

    proj = api_request("/api/projects", method="POST", data=project_payload)
    pid = proj["id"]
    print(f"    -> Đã tạo dự án thành công: {pid} ('{proj['name']}')")

    # Patch Mia's entity with the uploaded reference image media_id
    print("\n[*] BƯỚC 2: Gán Media ID từ ảnh thật F:\\affilate\\main.jpg cho nhân vật Mia...")
    chars = api_request(f"/api/projects/{pid}/characters")
    mia_char = next((c for c in chars if c.get("name") == "Mia"), None)
    if mia_char:
        api_request(f"/api/characters/{mia_char['id']}", method="PATCH", data={"media_id": MIA_MEDIA_ID})
        print(f"    -> Đã gán media_id={MIA_MEDIA_ID} cho Mia (Entity ID: {mia_char['id']})")
    else:
        print("    [-] Không tìm thấy nhân vật Mia trong danh sách entities!")

    # Switch active project
    try:
        api_request("/api/active-project", method="PUT", data={"project_id": pid})
        print("    -> Đã set làm Active Project.")
    except Exception:
        pass

    # Create video
    print("\n[*] BƯỚC 3: Tạo Video 16:9 (HORIZONTAL)...")
    video_payload = {
        "project_id": pid,
        "title": "I Time Traveled to Babylon in 570 BC! (Vlog)",
        "orientation": "HORIZONTAL",
        "display_order": 0
    }
    vid_data = api_request("/api/videos", method="POST", data=video_payload)
    vid = vid_data["id"]
    print(f"    -> Đã tạo Video thành công: {vid} ('{vid_data['title']}')")

    return pid, vid


SCENES_23_BEATS = [
    # --- HỒI 1: HOOK (0:00) ---
    {
        "beat": 1,
        "role": "Hook vào thẳng",
        "prompt": "An ancient heavy wooden chariot wheel rolls past right across the lens from left to right kicking up desert dust, revealing a crowded sunlit street in ancient Babylon with mudbrick buildings and merchants in fringed robes walking in the background.",
        "video_prompt": "0-3s: A massive wooden cart wheel rolls past inches from the lens in a heavy wipe, revealing Mia standing in the bustling street of Babylon. 3-6s: Mia extends her selfie stick, looks directly into the camera lens with wide excited eyes and says \"Guys, welcome to Babylon, 570 BC... and it is completely insane!\" 6-8s: People in ancient fringed wool tunics walk behind her as she begins walking backward down the packed dirt avenue.",
        "character_names": ["Mia"],
        "chain_type": "ROOT"
    },
    # --- HỒI 2: ĐỜI THƯỜNG (0:30 - 4:15) ---
    {
        "beat": 2,
        "role": "Định hướng phố xá",
        "prompt": "Handheld selfie vlog shot of a young traveler walking through a bustling ancient Mesopotamian avenue under bright sun, date palms swaying over mudbrick facades, Babylonian civilians and donkey carts passing in background.",
        "video_prompt": "0-3s: Mia walks along the sun-drenched dirt street, dodging passing donkeys laden with woven palm baskets. 3-6s: She glances around in wonder, leaning toward the mic whispering \"We are in the reign of King Nebuchadnezzar... and everything here is alive.\" 6-8s: Two city laborers carrying heavy clay amphorae pass in front of the lens from right to left, momentarily occluding the frame.",
        "character_names": ["Mia"],
        "chain_type": "CONTINUATION"
    },
    {
        "beat": 3,
        "role": "Quy mô công trình",
        "prompt": "Handheld selfie camera tilting up toward a massive sun-baked mudbrick city wall under construction, wooden scaffolding with ropes and bronze tools, laborers carrying stacks of heavy rectangular bricks.",
        "video_prompt": "0-3s: The camera pans across a colossal defensive wall where dozens of Babylonian workmen haul bricks up timber ramps. 3-6s: Mia turns back to the camera, pointing her thumb over her shoulder saying \"Look at the thickness of these walls. They say two chariots could pass each other on top.\" 6-8s: Dust billows softly as a loaded wooden cart creaks by, camera swings smoothly to the right.",
        "character_names": ["Mia"],
        "chain_type": "CONTINUATION"
    },
    {
        "beat": 4,
        "role": "Nguy hiểm nhẹ: Lính tuần tra",
        "prompt": "Two Babylonian city watchmen in lamellar armor and conical bronze helmets carrying tall bronze-tipped spears walking across a sunlit street, camera peeking from behind a timber canopy.",
        "video_prompt": "0-3s: A large wooden construction beam carried by two workers swings across the foreground, parting to reveal two stern guards in bronze helmets. 3-6s: Mia ducks slightly to the side, whispering quietly into the lens \"Okay, city guards... let's keep moving before anyone questions what I'm holding.\" 6-8s: She steps briskly down a dusty side alley between high mudbrick walls.",
        "character_names": ["Mia"],
        "chain_type": "CONTINUATION"
    },
    {
        "beat": 5,
        "role": "Đời sống dân sinh",
        "prompt": "First-person POV walking through a lively Babylonian alleyway near the canal, mothers in dark wool shawls carrying clay water jugs, children playing with clay knuckle-bones in the dust.",
        "video_prompt": "0-3s: First-person eye-level view moving smoothly along the beaten earth path beside a canal, water shimmering in morning light. 3-6s: Mia's voice speaks over the footage \"No modern noise, just the sound of the Euphrates, wind, and ancient voices speaking Akkadian.\" 6-8s: She approaches an open doorway of a scribe's open-air terrace with rolled reed mats.",
        "character_names": ["Mia"],
        "chain_type": "ROOT"
    },
    {
        "beat": 6,
        "role": "Sự thật hành chính: Thẻ đất sét chữ hình nêm",
        "prompt": "Close-up first-person POV of an elderly Babylonian scribe holding a triangular reed stylus, pressing intricate cuneiform wedge symbols into a soft wet clay tablet on a low wooden bench.",
        "video_prompt": "0-3s: The camera settles close to the weathered hands of a scribe pressing crisp cuneiform marks into wet clay. 3-6s: Mia's hand enters the frame pointing gently, her voice murmuring \"Look closely... this isn't paper. Every single transaction, law, and tax is pressed directly into river clay.\" 6-8s: The scribe glances up with a curious smile, nod of his head, as the camera tilts back up toward the sunlit market street.",
        "character_names": ["Mia"],
        "chain_type": "ROOT"
    },
    {
        "beat": 7,
        "role": "Chợ phiên & đời thường",
        "prompt": "Ultra-wide selfie of a young traveler navigating a crowded food bazaar in Babylon, stalls piled with dried dates, figs, piles of raw sesame seeds, and clay beer fermentation jars under palm leaf awnings.",
        "video_prompt": "0-3s: Mia weaves through vibrant merchant stalls overflowing with dark sticky dates and grains, the atmosphere rich with desert spices. 3-6s: A merchant holds up a string of dried figs, Mia laughs warmly at the camera saying \"The smell of roasting barley and dates is everywhere, you guys... I have to try something.\" 6-8s: She approaches a small food vendor's low wooden table and sets her device down.",
        "character_names": ["Mia"],
        "chain_type": "CONTINUATION"
    },
    {
        "beat": 8,
        "role": "Ẩm thực (Máy dựng bàn)",
        "prompt": "Smartphone propped on a rough wooden table facing a young woman sitting on a woven palm stool eating warm barley flatbread drizzled with dark date syrup from a terracotta dish, vendor smiling in background.",
        "video_prompt": "0-3s: Static frame from table height showing Mia breaking a warm piece of rustic barley bread and dipping it into thick golden date honey. 3-6s: She takes a bite, eyes widening in genuine delight, and looks into the lens saying \"It's nutty, dense, and naturally sweet. Honestly, way better than I expected!\" 6-8s: The friendly stall owner pours her a bowl of fermented barley water as she smiles gratefully.",
        "character_names": ["Mia"],
        "chain_type": "CONTINUATION"
    },
    {
        "beat": 9,
        "role": "Chuyển tiếp vận tải sông",
        "prompt": "A circular woven reed coracle boat (quffa) coated in dark bitumen gliding across the muddy green waters of the Euphrates river, loaded with grain sacks, waterfront quayside in background.",
        "video_prompt": "0-3s: The camera sweeps past the busy riverbank where circular bitumen-lined boats navigate the gentle current of the Euphrates. 3-6s: Mia's voiceover reflects \"Everything entering Babylon moves through this water... the lifeblood of ancient Mesopotamia.\" 6-8s: A dock worker carrying a woven sack walks directly across the lens from left to right in a fast foreground wipe.",
        "character_names": ["Mia"],
        "chain_type": "ROOT"
    },
    {
        "beat": 10,
        "role": "POV xúc giác: Đo lường bằng Bạc",
        "prompt": "Close-up first-person POV looking down at a bronze balance scale on a merchant stall, one pan holding stone weights, the other holding curled silver wire and silver shekel fragments.",
        "video_prompt": "0-3s: In first-person POV, Mia's fingertips lightly touch the cool bronze pan of the scale as curled silver clippings are weighed. 3-6s: Mia says in a soft fascinated tone \"No coins here. In 570 BC, they literally cut pieces of silver wire called shekels to buy daily food.\" 6-8s: The merchant's calloused hand lifts the balance scale, the pans swaying gently as the camera tilts upward.",
        "character_names": ["Mia"],
        "chain_type": "ROOT"
    },
    {
        "beat": 11,
        "role": "Nghề thủ công: Xưởng dệt nhuộm",
        "prompt": "A Babylonian textile workshop courtyard with giant ceramic dyeing vats bubbling with deep indigo blue and saffron yellow dye, long strips of dyed woolen cloth hanging to dry on high timber poles.",
        "video_prompt": "0-3s: Mia walks under billowing curtains of freshly dyed brilliant blue and crimson woolen fabrics swaying in the warm breeze. 3-6s: She reaches out feeling the coarse woven texture, speaking to camera \"Look at this deep cobalt color. Color here is power and wealth.\" 6-8s: She turns her head quickly away from the camera as the sound of distant bronze horns echoes through the city.",
        "character_names": ["Mia"],
        "chain_type": "CONTINUATION"
    },
    # --- HỒI 3: QUYỀN LỰC (5:05) ---
    {
        "beat": 12,
        "role": "Reveal #1: Quyền lực (Quay gáy)",
        "prompt": "Behind the traveler's head, turning around from behind her ponytail to reveal an expansive paved military plaza where dozens of Babylonian royal chariots with spoked bronze wheels and armored spearmen stand in rigid formation.",
        "video_prompt": "0-3s: Camera opens tight on the back of Mia's head and ponytail; she turns around smoothly toward the camera, revealing an imposing royal chariot division drilling behind her. 3-6s: Her eyes widen in awe, she lowers her voice to an urgent whisper \"Oh wow... look at that. That is the elite royal guard of the king.\" 6-8s: The camera pans across gleaming bronze spear points and ornate horse bridles stamped with rosettes.",
        "character_names": ["Mia"],
        "chain_type": "ROOT"
    },
    {
        "beat": 13,
        "role": "Chuẩn bị căng thẳng",
        "prompt": "Handheld selfie shot of a traveler walking cautiously near high stone arches, armored archers assembling along the ramparts, Babylonian citizens gathering along the royal street.",
        "video_prompt": "0-3s: Mia steps quietly alongside the stone pillars, citizens beginning to clear the main thoroughfare. 3-6s: Mia looks over her shoulder, speaking softly to the mic \"The whole street is being cleared... something huge is coming through.\" 6-8s: Loud bronze trumpets blare off-screen as the crowd begins to drop to their knees.",
        "character_names": ["Mia"],
        "chain_type": "CONTINUATION"
    },
    # --- HỒI 4: CAO TRÀO NGUY HIỂM (6:05 - 7:05) ---
    {
        "beat": 14,
        "role": "Cao trào: Đoàn xe Hoàng gia",
        "prompt": "The grand Processional Way lined with towering turquoise glazed brick walls, an ornate royal golden chariot surrounded by heavily armored guards marching forward, citizens kneeling on stone pavement.",
        "video_prompt": "0-3s: From behind a heavy brick pillar, Mia watches the magnificent golden royal chariot advance down the Processional Way amidst kneeling crowds. 3-6s: Mia whispers in tension \"It's the royal entourage... King Nebuchadnezzar.\" Suddenly, a tall armored guard turns his head and locks eyes directly onto her and her phone. 6-8s: The guard steps forward shouting a command in ancient Akkadian, pointing his bronze spear toward her position.",
        "character_names": ["Mia"],
        "chain_type": "CONTINUATION"
    },
    {
        "beat": 15,
        "role": "Rượt đuổi qua ngõ",
        "prompt": "Fast handheld chase shot through a narrow winding mudbrick alley, camera shaking with rapid footsteps, sunlight casting dramatic sharp shadows on dusty walls.",
        "video_prompt": "0-3s: Camera shakes violently as Mia sprints around a tight corner of the mudbrick alleyway, breathless breathing audible. 3-6s: She glances back into the lens for a split second, heart racing \"Gotta run, gotta run! They definitely don't like my camera!\" 6-8s: She ducks beneath a low hanging awning, pushing past woven palm screens as shouting guards echo behind her.",
        "character_names": ["Mia"],
        "chain_type": "CONTINUATION"
    },
    {
        "beat": 16,
        "role": "Thoát hiểm ra ngoại ô",
        "prompt": "A sunlit outer gate of ancient Babylon leading toward rural outskirts, a wooden gate swinging open as dust settles in the warm afternoon glare.",
        "video_prompt": "0-3s: Mia bursts through the shadow of the outer city gate arch into the open glare of the countryside. 3-6s: She slows to a rapid walk, leaning against a sun-warmed wall catching her breath \"Okay... okay, we made it past the inner wall. That was way too close.\" 6-8s: A slow-moving wooden ox cart loaded with dry straw comes into view heading down the dirt road.",
        "character_names": ["Mia"],
        "chain_type": "CONTINUATION"
    },
    # --- HỒI 5: HẠ NHỊP (7:25) ---
    {
        "beat": 17,
        "role": "Hạ nhịp (Đi nhờ xe bò)",
        "prompt": "Handheld selfie shot of a traveler sitting comfortably in the back of a rustic wooden ox cart filled with golden straw, a friendly elderly Babylonian farmer in a simple wool tunic smiling as the cart rolls through rural date palm groves.",
        "video_prompt": "0-3s: The camera settles into a gentle rhythmic sway as the ox cart trundles through peaceful palm groves, peaceful desert birds calling. 3-6s: Mia relaxes against the straw, smiling softly at the lens \"This kind farmer offered me a ride out toward the sacred district. The relief is unreal.\" 6-8s: The camera turns toward the horizon where massive blue structures begin to peek through the palm tops.",
        "character_names": ["Mia"],
        "chain_type": "ROOT"
    },
    # --- HỒI 6: DI SẢN (7:50 - 10:05) ---
    {
        "beat": 18,
        "role": "Reveal #2: Di sản từ xa",
        "prompt": "Wide view from a dirt country lane looking past date palms toward the monumental city walls of Babylon and the top of the brilliant blue Ishtar Gate glistening in the afternoon sun.",
        "video_prompt": "0-3s: Through the parting palm fronds, the colossal blue and gold battlements of Babylon rise dramatically against the skyline. 3-6s: Mia turns the camera toward the horizon, whispering in wonder \"You can see it from miles away... that vivid, shimmering blue in the middle of the desert.\" 6-8s: A clay brick kiln chimney puffs faint smoke into the sky, leading into the artisans' quarter.",
        "character_names": ["Mia"],
        "chain_type": "CONTINUATION"
    },
    {
        "beat": 19,
        "role": "Hậu trường: Lò nung men gốm",
        "prompt": "An open courtyard ceramic kiln workshop, artisan ovens glowing with hot fire, stacks of raw mudbricks and vibrant cobalt-blue glazed tiles cooling in the shade, clay pigments ground in stone mortars.",
        "video_prompt": "0-3s: Mia walks among stacks of brilliant lapis-blue glazed bricks, heat shimmering from domed clay kilns. 3-6s: Mia stoops down beside a cooling tile, showing it to the lens \"They ground cobalt and copper to create this glaze... this is where every single brick of the Ishtar Gate was born.\" 6-8s: She steps forward through an archway opening onto the grand royal avenue.",
        "character_names": ["Mia"],
        "chain_type": "CONTINUATION"
    },
    {
        "beat": 20,
        "role": "Chi tiết 'Wow' trái hình dung",
        "prompt": "First-person POV approaching the grand Ishtar Gate, the entire monumental gateway shining with intense vivid cobalt-blue glazed brick, alternating embossed rows of yellow sirrush dragons and white bulls.",
        "video_prompt": "0-3s: The camera moves forward revealing the full height of the breathtaking Ishtar Gate towering overhead in radiant deep blue and yellow. 3-6s: Mia's voice captures pure astonishment \"In movies, ancient cities are always dusty brown and beige... but Babylon is electric blue! It feels like entering another dimension.\" 6-8s: She walks up to the base of the gate wall where the dragon reliefs are within arm's reach.",
        "character_names": ["Mia"],
        "chain_type": "ROOT"
    },
    {
        "beat": 21,
        "role": "POV xúc giác: Chạm tay vào Di sản",
        "prompt": "Close-up first-person POV of the traveler's hand gently reaching out and placing fingers on the glazed ceramic surface of an ancient yellow sirrush dragon relief set in the deep-blue Ishtar Gate wall.",
        "video_prompt": "0-3s: Mia's fingers gently make contact with the smooth, cool glazed brick of the mythical horned dragon relief. 3-6s: Mia speaks in a hushed, reverent whisper \"Cold, glassy smooth... and perfectly preserved. Over two and a half thousand years before our time.\" 6-8s: The camera slowly tilts up the towering gateway toward the massive crenellations against the golden sky.",
        "character_names": ["Mia"],
        "chain_type": "ROOT"
    },
    {
        "beat": 22,
        "role": "Reveal #3: Đỉnh cao Etemenanki Ziggurat",
        "prompt": "Standing on a high earthen terrace overlooking the city, slow handheld pan revealing the gargantuan seven-tiered Etemenanki Ziggurat rising 90 meters high beside the Euphrates, crowned with a blue shrine in the golden sunset.",
        "video_prompt": "0-3s: Handheld camera rises above the temple terrace railing, panning slowly to reveal the colossal Etemenanki stepped ziggurat dominating the entire Mesopotamian landscape. 3-6s: Mia turns back to the camera, breathless and radiant in golden hour light \"Behold... Etemenanki. The true inspiration for the Tower of Babel. Ninety meters tall, reaching right into the heavens.\" 6-8s: The setting sun paints the massive tiers in amber and purple hues as river breezes flutter through her hair.",
        "character_names": ["Mia"],
        "chain_type": "CONTINUATION"
    },
    # --- HỒI 7: KẾT (10:22) ---
    {
        "beat": 23,
        "role": "Kết trầm lúc hoàng hôn",
        "prompt": "Smartphone propped on a low ancient brick parapet facing a young traveler sitting quietly at sunset, the shimmering Euphrates river reflecting purple and orange evening sky in the background, palms silhouetted.",
        "video_prompt": "0-3s: Static frame from the propped phone camera showing Mia sitting peacefully on the brick wall as the sun sinks below the ancient horizon. 3-6s: She looks warmly into the lens, speaking softly \"Babylon in 570 BC isn't just ruins in a textbook. It's people, art, and ambition that defied time. Where should we travel to next?\" 6-8s: She offers a gentle wave with a smile, reaching toward the camera as the frame fades gracefully into the twilight.",
        "character_names": ["Mia"],
        "chain_type": "CONTINUATION"
    }
]


def create_scenes(vid: str):
    print(f"\n[*] BƯỚC 4: Tạo 23 Scene chuẩn 7 Hồi & 3 Cú Reveal (Long-form 10p, 16:9)...")
    for i, s in enumerate(SCENES_23_BEATS, 1):
        payload = {
            "video_id": vid,
            "display_order": i - 1,
            "prompt": s["prompt"],
            "video_prompt": s["video_prompt"],
            "character_names": s.get("character_names", []),
            "chain_type": s.get("chain_type", "ROOT")
        }
        res = api_request("/api/scenes", method="POST", data=payload)
        sid = res["id"]
        print(f"    [Beat {s['beat']:02d}] Scene {i:02d} ({sid[:8]}...): {s['role']}")


def main():
    flush_stale_queue()
    pid, vid = create_project()
    create_scenes(vid)
    print("\n" + "=" * 70)
    print("✅ HOÀN TẤT KHỞI TẠO DỰ ÁN MỚI THÀNH CÔNG!")
    print(f"  - Project ID:     {pid}")
    print(f"  - Video ID:       {vid}")
    print(f"  - Flow Project:   {FLOW_PROJECT_ID}")
    print(f"  - Orientation:    HORIZONTAL (16:9)")
    print(f"  - Nhân vật chính: Mia (Ref Media ID: {MIA_MEDIA_ID})")
    print(f"  - Tổng số Scene:  23 scenes (chuẩn 7 Hồi, 3 Cú Reveal, ẩm thực dựng bàn, hạ nhiệt xe bò)")
    print("=" * 70)


if __name__ == "__main__":
    main()
