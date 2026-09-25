import json
import sqlite3

video_id = "03a609d2-54d9-4fbf-95d4-eadb8ea3d9cb"

scenes = [
    {
        "display_order": 0,
        "name": "FPV Crash Zoom Time-Travel Hook",
        "duration": 6.0,
        "character_names": [],
        "prompt": "Deep black void of space with pinpoint sharp stars. Earth is a brilliant blue and white marble in the center of the frame, atmospheric blue haze glowing along the curvature of the planet. Swirling white cloud formations over the ancient Middle East, the Mediterranean Sea, and the Tigris-Euphrates river valley clearly visible in daylight. Ultra-crisp photorealism, authentic planetary scale.",
        "video_prompt": (
            "Kỹ thuật: video 6 giây, 24fps, một cú chuyển động camera FPV liên tục không ngắt quãng duy nhất, chân thực, không phong cách hoạt hình, không cắt cảnh.\n"
            "0s: Trạng thái mở đầu — camera đặt trong không gian hướng về Trái Đất: hành tinh xanh trên nền không gian đen, khu vực Lưỡng Hà và sông Euphrates hiện rõ với các đám mây xoáy.\n"
            "0s-4s: Camera thực hiện một cú đẩy tới liên tục không ngắt quãng kiểu FPV, không bao giờ cắt hay dừng lại:\n"
            "— Đầu tiên, camera tăng tốc nhanh lao thẳng vào Trái Đất, lao thẳng vào bề mặt hành tinh, ánh sáng khí quyển tăng dần khi tiến gần, sau đó xuyên thẳng qua tầng mây — những đám mây trắng dày lướt qua hai bên với hiệu ứng motion blur, một khoảnh khắc trắng xóa ngắn khi xuyên qua lớp mây dày nhất.\n"
            "— Thoát ra khỏi lớp mây, camera tiếp tục cú lao FPV tốc độ cao và đến ngay tầm bối cảnh Babylon 570 TCN — camera giờ bay thấp và nhanh dọc theo bờ sông Euphrates lấp lánh cát sa mạc, lướt sát mặt nước, hai bên là rặng chà là và bóng dáng Vườn Treo Babylon mờ ảo phía xa.\n"
            "— Camera lượn/nghiêng qua phải nép qua cỗ xe bò cổ đại bằng gỗ, tiếp tục hành trình bay FPV thấp, rồi tiến thẳng tới vlogger Mia đang đứng cạnh bờ sông — camera ổn định thành góc lơ lửng chính diện hướng vào Mia.\n"
            "4s-5s: Camera giữ nguyên hoàn toàn tĩnh ở bố cục cuối cùng — Mia đứng trọn khung hình cạnh bờ sông Euphrates trong trang phục lanh cổ đại, không còn chuyển động.\n"
            "5s-6s: Khung hình giữ nguyên tĩnh đến hết video, tạo điểm nối hoàn hảo sang Cảnh 01 khi Mia bắt đầu cất tiếng chào.\n"
            "Khóa chất lượng: một đường di chuyển camera liên tục không ngắt quãng xuyên suốt 0s-4s (không cắt cảnh đột ngột, không hòa mờ — chuyển tiếp tự nhiên chỉ thông qua chuyển động camera), cường độ motion blur nhất quán trong các giai đoạn di chuyển nhanh, vật lý bay FPV chân thực (nghiêng người khi rẽ, quán tính, thay đổi độ cao nhẹ), ánh sáng liên tục hợp lý từ không gian đến tầm mắt ban ngày sa mạc, nét sắc ở khung hình cuối giữ nguyên.\n"
            "Âm thanh: chỉ có hiệu ứng âm thanh — tiếng gió/khí quyển sâu trong lúc lao qua không gian, tiếng vút khi xuyên qua mây, chuyển sang âm thanh môi trường sông nước sa mạc cổ đại khi camera đến mặt đất. Không nhạc nền.\n"
            "Negative prompt: không cắt cảnh đột ngột hay hòa mờ, không nhạc nền, không phong cách hoạt hình/minh họa, không rung giật camera ngoài chuyển động FPV tự nhiên, không biến dạng cơ thể Mia, không thêm chữ overlay."
        ),
        "narrator_text": "(Hiệu ứng âm thanh FPV lao từ không gian xuyên mây xuống bờ sông Euphrates)",
    },
    {
        "display_order": 1,
        "name": "The Shock Arrival (Bờ Sông Euphrates)",
        "duration": 10.0,
        "character_names": ["Mia", "Mia Outfit"],
        "prompt": "Mia standing on the sun-baked dirt riverbank of the Euphrates river in 570 BC Babylon, an ancient Mesopotamian wooden ox cart with solid timber wheels rolling past in the background.",
        "video_prompt": (
            "0-3s: Mia stands on the dirt riverbank, wide-eyed with adrenaline, steadying herself as a heavy wooden ox cart lumbers past right behind her, its solid wheels creaking in the desert dust.\n"
            "3-6s: Mia glances left and right at the bustling ancient riverbank, takes a deep breath, turns directly to face the camera, and says \"Guys... my coordinates did not lie. Welcome to 570 BC.\"\n"
            "6-10s: She raises one arm to gesture toward the shimmering green Euphrates behind her, a faint smile breaking through her shock as dust motes drift in the golden sunlight."
        ),
        "narrator_text": "Guys... my coordinates did not lie. Welcome to Babylon, 570 BC.",
    },
    {
        "display_order": 2,
        "name": "The Legendary Glimpse (Vườn Treo Hiện Ra Bên Kia Sông)",
        "duration": 10.0,
        "character_names": ["Mia", "Mia Outfit"],
        "prompt": "Mia in selfie vlog perspective holding the camera frame, with the monumental stepped terraces of the Hanging Gardens rising across the wide shimmering Euphrates river.",
        "video_prompt": (
            "0-3s: Mia holds the camera steady in a selfie perspective, looking past the lens across the river, whispering \"Look at that... on the horizon.\"\n"
            "3-7s: She pans the camera slightly to reveal the colossal multi-tiered green terraces of the Hanging Gardens rising across the river, cascading waterfalls glistening in the morning light, before turning back to the camera and saying \"That is not a mountain. That is the Hanging Gardens of Babylon. Let us get in.\"\n"
            "7-10s: She smiles with adventurous excitement and nods toward the water, stepping toward the river docks."
        ),
        "narrator_text": "Look across the Euphrates... That green mountain rising over the mud bricks isn't natural. That is the Hanging Gardens of Babylon.",
    },
    {
        "display_order": 3,
        "name": "First Contact (Đoàn Thuyền Quffa & Người Chèo Sông)",
        "duration": 10.0,
        "character_names": [],
        "prompt": "First-person POV looking across the shimmering waters of the Euphrates river at a traditional circular woven-reed bitumen quffa coracle boat steered by a bearded Babylonian boatman.",
        "video_prompt": (
            "0-3s: The camera stays locked in steady first-person POV over the rippling water as a circular bitumen quffa boat bobs gently.\n"
            "3-7s: The bearded Babylonian boatman skillfully strokes the wooden oar, turning his head toward the camera with a calm, curious gaze, nodding slowly as the boat glides smoothly forward.\n"
            "7-10s: The boat drifts past a cluster of tall river reeds, revealing the stone foundation walls of Babylon riverfront quays in crisp focus under the clear sky."
        ),
        "narrator_text": "Circular quffa boats made of woven reeds and coated in pure black bitumen. The water taxis of ancient Mesopotamia.",
    },
    {
        "display_order": 4,
        "name": "The Great Lift (Hệ Thống Thủy Lực Trục Xoắn Vĩ Đại)",
        "duration": 10.0,
        "character_names": ["Mia", "Mia Outfit"],
        "prompt": "Mia standing on a stone terrace beside a colossal ancient bronze and timber Archimedes screw pump mechanism lifting water from the Euphrates into elevated garden conduits.",
        "video_prompt": (
            "0-3s: Mia stands beside the colossal wooden hydraulic screw as rushing water pours through the carved stone chute, fine mist catching the sunlight.\n"
            "3-7s: Mia points up along the rising water screw toward the higher garden tiers, looking into the camera and saying \"How do you irrigate an artificial mountain in the desert? Bronze water screws and endless hydraulic power.\"\n"
            "7-10s: The camera tilts up smoothly following the flowing stream into the elevated terrace aqueduct as Mia steps forward along the stone walkway."
        ),
        "narrator_text": "How do you keep thousands of tropical trees alive in the middle of an Iraqi desert? Archimedes screws and relentless hydraulic engineering.",
    },
    {
        "display_order": 5,
        "name": "The Ancient Snack (Thử Quả Vả Tươi & Bánh Mì Lúa Mạch)",
        "duration": 10.0,
        "character_names": ["Mia", "Mia Outfit"],
        "prompt": "Handheld selfie vlog close-up of Mia holding a fresh ripe purple fig broken open, showing the sweet pink seeded interior in a lively Babylonian open-air street stall.",
        "video_prompt": (
            "0-3s: Mia holds up the broken ripe fig toward the camera lens, showing the fresh juicy pink flesh up close with genuine enthusiasm.\n"
            "3-7s: She takes a bite, chews, her eyes lighting up in pure delight, and she says \"Sweet as pure honey! No wonder the kings loved this.\"\n"
            "7-10s: She gives an authentic thumbs-up to the camera with a joyful laugh, showing the bustling marketplace in the soft-focus background."
        ),
        "narrator_text": "Fresh Babylonian purple fig. Sweeter than honey, straight from the palace orchards.",
    },
    {
        "display_order": 6,
        "name": "Market Economy (Đổi Bạc Shekel & Bí Mật Đất Sét)",
        "duration": 10.0,
        "character_names": [],
        "prompt": "Macro close-up shot of two hands placing small silver wire coil coils onto a brass balance scale beside a wet clay tablet inscribed with cuneiform script and a bone stylus.",
        "video_prompt": (
            "0-3s: Two hands gently place silver coil pieces onto the brass balance scale, which dips and balances accurately under the merchant's watchful eyes.\n"
            "3-7s: The merchant's hands turn the clay tablet slightly toward the camera, using the bone stylus to press one final crisp cuneiform mark into the soft clay to seal the contract.\n"
            "7-10s: The merchant taps the tablet with his thumb, nods firmly, and picks up the silver piece, completing the ancient trade."
        ),
        "narrator_text": "No paper money here. Payments are made in weighed silver coils called shekels, recorded permanently on wet clay tablets.",
    },
    {
        "display_order": 7,
        "name": "Towards the Ziggurat (Cổng Thành Xanh Lapis Lazuli & Ngẩng Nhìn Etemenanki)",
        "duration": 10.0,
        "character_names": ["Mia", "Mia Outfit"],
        "prompt": "Tracking shot from behind Mia walking along the monumental Processional Way toward the colossal cobalt-blue glazed brick Ishtar Gate, with the 90m high Etemenanki ziggurat rising beyond.",
        "video_prompt": (
            "0-3s: Mia walks along the glazed brick avenue, then slows to a halt as the monumental cobalt-blue Ishtar Gate towers before her.\n"
            "3-7s: She turns slightly back toward the camera, her face glowing with awe, pointing upward and whispering \"Look at the glazed blue tiles... and beyond it, the Tower of Babel itself: Etemenanki.\"\n"
            "7-10s: The camera pans smoothly upward from Mia's shoulder past the golden glazed dragon reliefs toward the massive seven tiers of the ziggurat."
        ),
        "narrator_text": "The Ishtar Gate. Real lapis-lazuli glazed tiles shining in the Mesopotamian sun, and behind it, Etemenanki—the 90-meter ziggurat that inspired the Tower of Babel.",
    },
    {
        "display_order": 8,
        "name": "The Shadow of Power (Cổng Vòm Dẫn Vào Khu Cấm Hoàng Gia)",
        "duration": 10.0,
        "character_names": [],
        "prompt": "Eye-level shot looking through a heavy arched entryway of mud brick into a private sunlit palace courtyard guarded by elite sentries with bronze helmets and spears.",
        "video_prompt": (
            "0-3s: The camera holds steady in the cool shadow of the arched entryway, looking into the bright sunlit royal courtyard.\n"
            "3-7s: Two royal guards in bronze helmets and pleated tunics march across the courtyard with synchronized steady footsteps, their bronze spearheads gleaming.\n"
            "7-10s: The guards turn the corner and vanish behind a stone balustrade, leaving the courtyard empty and inviting exploration."
        ),
        "narrator_text": "Beyond these arches lies the private royal domain of Nebuchadnezzar II. Off-limits to ordinary citizens.",
    },
    {
        "display_order": 9,
        "name": "Stepping Past the Gates (Lẻn Qua Hành Lang Cây Cảnh & Mùi Nhựa Thông)",
        "duration": 10.0,
        "character_names": [],
        "prompt": "First-person handheld POV moving cautiously through a secluded palace corridor lined with potted cypress trees, red oleander flowers, and cedar lattice trellises.",
        "video_prompt": (
            "0-3s: The handheld POV camera moves forward cautiously at walking pace, stepping between the lush potted cypress trees and hanging flowering vines.\n"
            "3-7s: The camera pans gently left and right, capturing the scent of pine resin and wet stone, the sound of muffled running water growing louder ahead.\n"
            "7-10s: The camera slips through the stone archway into the cool twilight of the lower terrace vaults."
        ),
        "narrator_text": "The scent of cedar resin and damp soil is overwhelming. I am slipping into the lower vaults.",
    },
    {
        "display_order": 10,
        "name": "Infiltration (Đột Nhập Tầng Hầm Vòm Cuốn Vườn Treo)",
        "duration": 10.0,
        "character_names": ["Mia", "Mia Outfit"],
        "prompt": "Close-up handheld selfie vlog in a dim subterranean arched stone vault supporting the Hanging Gardens, water droplets seeping between bitumen seams in torchlight.",
        "video_prompt": (
            "0-3s: Mia holds the camera close to her face in the cool, dimly lit vault, glancing nervously over her shoulder into the darkness.\n"
            "3-7s: She leans toward the camera lens and whispers urgently \"We are inside the crypt vaults directly underneath the gardens. Hear that water rushing above our heads?\"\n"
            "7-10s: She tilts the camera upward to show the heavy bitumen-sealed ceiling stones glistening with condensation before pulling the camera back to herself."
        ),
        "narrator_text": "Listen closely... That is thousands of gallons of water rushing directly above us through lead-lined vaults.",
    },
    {
        "display_order": 11,
        "name": "The Sacred Aqueduct (Hệ Thống Máng Dẫn Nước Ngầm Bằng Chì)",
        "duration": 10.0,
        "character_names": ["Mia", "Mia Outfit"],
        "prompt": "Medium close-up shot of Mia kneeling beside a subterranean aqueduct channel lined with sheets of grey lead and dark bitumen tar, clear water flowing steadily.",
        "video_prompt": (
            "0-3s: Mia kneels beside the stone conduit, pointing her finger at the dark bitumen and lead waterproof lining where water glides smoothly.\n"
            "3-7s: She looks up at the camera with genuine fascination, whispering \"They used sheets of lead and thick asphalt so the river water would not rot the palace roofs below.\"\n"
            "7-10s: Suddenly, a loud metallic clang of bronze armor echoes from down the stone hallway; Mia stiffens and whips her head toward the noise."
        ),
        "narrator_text": "Sheets of hammered lead and natural asphalt. Ancient waterproof technology keeping the royal palace from collapsing.",
    },
    {
        "display_order": 12,
        "name": "Encounter with the Royal Guard (Đối Đầu Lính Ngự Lâm Babylon)",
        "duration": 10.0,
        "character_names": [],
        "prompt": "Eye-level shot of two Babylonian palace guards in pointed bronze helmets and braided black beards pointing bronze spears toward the camera in a torchlit stone corridor.",
        "video_prompt": (
            "0-3s: The two Babylonian guards spot the intruder, shouting a harsh Akkadian command that echoes loudly off the stone vault walls.\n"
            "3-6s: The lead guard lowers his bronze spear to waist level and charges forward with heavy leather boots thudding against the wet stone floor.\n"
            "6-10s: The camera violently jerks backward as Mia recoils in sheer terror, the guard's outstretched spear lunging within feet of the lens."
        ),
        "narrator_text": "Oh no... Palace guards! RUN!",
    },
    {
        "display_order": 13,
        "name": "The Turn and Sprint (Quay Đầu Tháo Chạy)",
        "duration": 10.0,
        "character_names": [],
        "prompt": "Dynamic first-person running POV down a torchlit stone corridor with intense motion blur as the camera flees toward a distant bright doorway.",
        "video_prompt": (
            "0-3s: The camera violently spins 180 degrees with heavy handheld motion blur as frantic running footsteps slap against the stone floor.\n"
            "3-7s: The camera sprints full tilt down the narrow corridor toward the bright exit doorway, shadows whipping rapidly past on both sides.\n"
            "7-10s: Heavy shouting and clattering armor echo close behind as the camera bursts through the doorway into blinding sunlight."
        ),
        "narrator_text": "(Frantic running footsteps, heavy gasping breath, angry shouts in ancient Akkadian echoing behind)",
    },
    {
        "display_order": 14,
        "name": "Footsteps on Wet Stone (Tiếng Chân Dồn Dập Trên Bậc Thang Đá Ướt)",
        "duration": 10.0,
        "character_names": [],
        "prompt": "Low-angle fast tracking shot of feet in leather sandals bounding up wet stone stairs splashing water, pursued closely by heavy bronze-greaved boots.",
        "video_prompt": (
            "0-3s: The camera tracks rapidly up the steep wet stairs as leather sandals fly upward, splashing water droplets across the stone steps.\n"
            "3-7s: Behind on the lower steps, the heavy bronze greaves and boots of the guards hammer upward in furious pursuit, just paces behind.\n"
            "7-10s: The camera scrambles up over the top landing, swinging sharply left behind a massive stone retaining wall."
        ),
        "narrator_text": "(Splashing water, heavy footsteps, guards shouting on the stairs)",
    },
    {
        "display_order": 15,
        "name": "Chase Behind Waterfall (Chạy Trốn Sau Màn Thác Nước Cổ)",
        "duration": 10.0,
        "character_names": ["Mia", "Mia Outfit"],
        "prompt": "Handheld phone selfie vlog running shot of Mia sprinting along a wet stone ledge behind a thunderous curtain of waterfall, water spray hitting the lens, face flushed with panic.",
        "video_prompt": (
            "0-3s: Handheld phone camera violently shakes with Mia's frantic running footsteps as she sprints along the narrow wet stone ledge behind the thundering water curtain.\n"
            "3-6s: Mia turns the camera slightly toward her face, chest heaving violently, gasping terrified into the microphone: \"They are right behind me! I am behind the waterfall!\"\n"
            "6-10s: Water droplets splash directly against the camera lens as Mia glances back in sheer panic, spots a heavy wooden door ahead, and ducks frantically toward it."
        ),
        "narrator_text": "They are right behind me! I am behind the terrace waterfall—there is a door ahead!",
    },
    {
        "display_order": 16,
        "name": "The Upper Nursery (Chốt Then Cửa Thoát Hiểm Vào Vườn Ươm)",
        "duration": 10.0,
        "character_names": ["Mia", "Mia Outfit"],
        "prompt": "Medium-wide shot of Mia in wet linen tunic leaning all her weight against a solid cedar door, sliding a heavy wooden latch bar into the stone wall bracket inside a peaceful sunlit nursery.",
        "video_prompt": (
            "0-3s: Mia slams the thick cedar door shut and wedges the heavy wooden locking bar into the wall brackets with a heavy resonant thud.\n"
            "3-7s: The guards hammer furiously against the outside of the door twice, but the solid latch holds firm; Mia slumps her back against the door, exhaling in overwhelming relief.\n"
            "7-10s: She wipes sweat and water spray from her forehead, laughing quietly with trembling adrenaline, looking around the peaceful green nursery."
        ),
        "narrator_text": "Locked. Oh my god... That was way too close.",
    },
    {
        "display_order": 17,
        "name": "The Ancient Botanist (Gặp Ông Lão Chăm Sóc Vườn Ươm)",
        "duration": 10.0,
        "character_names": ["Mia", "Mia Outfit"],
        "prompt": "Medium shot of an elderly Babylonian master gardener with a kind wrinkled face and curly grey beard offering a fresh green aromatic fig leaf toward Mia in the sunlit rooftop nursery.",
        "video_prompt": (
            "0-3s: The elderly gardener looks up from trimming a small sapling, noticing Mia with a gentle, reassuring smile rather than alarm.\n"
            "3-7s: He steps forward gracefully, extending a velvety green fig leaf toward Mia, saying a soft, soothing greeting in ancient Babylonian dialect.\n"
            "7-10s: Mia bows her head respectfully with hands clasped, taking the leaf and inhaling its sweet fragrance as calm completely replaces the panic."
        ),
        "narrator_text": "Meet the master botanist of the royal gardens. He wasn't alarmed at all—just offered me a fresh fig leaf and a smile.",
    },
    {
        "display_order": 18,
        "name": "Rooftop Oasis (Bước Ra Bầu Trời: Tầng Thượng Vườn Treo)",
        "duration": 10.0,
        "character_names": ["Mia", "Mia Outfit"],
        "prompt": "Cinematic wide establishing shot of Mia standing in the center of the highest terrace of the Hanging Gardens of Babylon 75 feet above the desert, lush date palms, pools, and clear blue sky.",
        "video_prompt": (
            "0-3s: Mia stands anchored on the sunlit terrace, opening her arms wide as the warm desert breeze ruffles her hair and tunic.\n"
            "3-7s: She turns 360 degrees in place, gazing up at the lush green canopy against the clear Mesopotamian sky, speaking with breathy wonder: \"We made it to the top terrace. This is truly the rooftop of the world.\"\n"
            "7-10s: The camera pushes past Mia toward a massive ancient Lebanese cedar tree growing proudly at the edge of the stone terrace."
        ),
        "narrator_text": "We made it. 75 feet in the air, a complete living paradise suspended between heaven and earth.",
    },
    {
        "display_order": 19,
        "name": "Lebanese Cedar Giant (Gốc Cây Tuyết Tùng Lebanon Khổng Lồ)",
        "duration": 10.0,
        "character_names": ["Mia", "Mia Outfit"],
        "prompt": "Medium-wide shot of Mia resting her palm flat against the massive textured rough bark of a towering Lebanese cedar tree growing on the stone terrace in rich golden sunlight.",
        "video_prompt": (
            "0-3s: Mia approaches the massive cedar trunk and presses her hand against the deeply furrowed fragrant bark, feeling its ancient strength.\n"
            "3-7s: She looks over her shoulder toward the camera, speaking with sincere awe: \"This cedar was brought hundreds of miles from the mountains of Lebanon just to make Queen Amytis feel at home.\"\n"
            "7-10s: She looks up into the dense green needle canopy as golden sunbeams filter through the branches."
        ),
        "narrator_text": "A genuine Lebanese cedar, hauled hundreds of miles across deserts so Queen Amytis wouldn't miss her mountain homeland.",
    },
    {
        "display_order": 20,
        "name": "Myth Busted: Overhanging (Vlog Ban Công Đá Nhô Ra Vực Trời)",
        "duration": 10.0,
        "character_names": ["Mia", "Mia Outfit"],
        "prompt": "Wide vlog selfie perspective of Mia leaning against a carved stone balustrade overhanging the dizzying vertical drop to the Euphrates river below, explaining with animated expressions.",
        "video_prompt": (
            "0-3s: Mia leans against the stone railing, hair catching the wind as she gestures downward over the dizzying vertical drop.\n"
            "3-7s: She looks straight into the camera lens with an insightful smile, saying \"The word 'Hanging' is a Greek mistranslation of 'Kremastos'—it means overhanging terraces, not hanging from ropes!\"\n"
            "7-10s: She turns her head to look out across the vast panorama of Babylon as the sun begins its dramatic descent toward the horizon."
        ),
        "narrator_text": "History fact: 'Hanging' was a Greek mistranslation of 'Kremastos'—it meant overhanging garden terraces, not gardens hanging on ropes!",
    },
    {
        "display_order": 21,
        "name": "Sunset Over Babylon (Hoàng Hôn Rực Lửa Phủ Lên Tháp Etemenanki)",
        "duration": 10.0,
        "character_names": [],
        "prompt": "Epic panoramic landscape at golden hour over the entire city of Babylon, Euphrates river glowing like molten gold, seven-tiered Etemenanki ziggurat casting long dramatic shadows.",
        "video_prompt": (
            "0-3s: The camera glides slowly right across the epic panorama as the blazing orange sun touches the distant desert horizon.\n"
            "3-7s: The golden glow deepens into rich purple and magenta, illuminating the glistening waters of the Euphrates and the towering silhouette of the great ziggurat.\n"
            "7-10s: Evening stars begin to twinkle faintly in the deep violet sky above the eternal city."
        ),
        "narrator_text": "Sunset over 570 BC Babylon. One of the greatest cities the ancient world would ever see.",
    },
    {
        "display_order": 22,
        "name": "Farewell View (Ngồi Lan Can Đá Thả Chân Tạm Biệt)",
        "duration": 10.0,
        "character_names": ["Mia", "Mia Outfit"],
        "prompt": "Cinematic medium shot of Mia sitting on the wide stone balustrade of the highest terrace, legs swinging over the edge, silhouetted against a radiant orange and violet sunset.",
        "video_prompt": (
            "0-3s: Mia sits on the stone balustrade in the sunset breeze, her silhouette glowing warm gold against the horizon.\n"
            "3-7s: She turns her face toward the camera, a warm, heartfelt smile appearing as she says \"From the riverbanks to the top of the world... Babylon, you were unforgettable.\"\n"
            "7-10s: She looks back out over the city one last time, taking a deep, quiet breath of the cool evening desert air."
        ),
        "narrator_text": "From escaping guards in the aqueducts to the quiet atop the world... Babylon, you were truly unforgettable.",
    },
    {
        "display_order": 23,
        "name": "Stone Balustrade Sign-off (Cận Cảnh Kết Nối Với Người Xem)",
        "duration": 10.0,
        "character_names": ["Mia", "Mia Outfit"],
        "prompt": "Close-up selfie vlog in twilight blue hour of Mia holding the phone camera, soft warm glow illuminating her face, distant city torches flickering below.",
        "video_prompt": (
            "0-3s: Mia looks directly into the camera lens in the soft twilight, whispering warmly: \"My recall beacon is charging. Time to jump.\"\n"
            "3-7s: She winks playfully at the viewer, saying \"Subscribe for the next time-travel expedition. See you in the next century!\"\n"
            "7-10s: She raises her hand with a smile and places her palm gently over the camera lens, fading the scene to black as the video ends."
        ),
        "narrator_text": "My beacon is charging. Subscribe for the next time-travel destination. See you in the next century!",
    },
]

conn = sqlite3.connect("flow_agent.db")
cur = conn.cursor()

# Remove any old scenes in this new video if any
cur.execute("DELETE FROM scene WHERE video_id = ?", (video_id,))
conn.commit()

import uuid

inserted = 0
for sc in scenes:
    sid = str(uuid.uuid4())
    cur.execute(
        """
        INSERT INTO scene (
            id, video_id, display_order, prompt, video_prompt,
            character_names, duration, narrator_text
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """,
        (
            sid,
            video_id,
            sc["display_order"],
            sc["prompt"],
            sc["video_prompt"],
            json.dumps(sc["character_names"]),
            sc["duration"],
            sc["narrator_text"],
        ),
    )
    inserted += 1

conn.commit()
conn.close()
print(f"SUCCESS: Inserted {inserted} scenes for Video ID {video_id} into flow_agent.db!")
