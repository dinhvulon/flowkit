#!/usr/bin/env python3
"""
FlowKit — Script Khởi Tạo Dự Án: Heian-kyō 1000 (Kyoto Heian Vlog)
Tự động nạp kịch bản Heian 1000 với đầy đủ 10 phân cảnh, thoại tiếng Nhật đàm thoại
và thiết lập quang học Pan-Focus vào FlowKit Local API (cổng 8100).

Sử dụng:
    python scripts/create_kyoto_heian_1000.py
"""

import json
import os
import sys
import urllib.request
import urllib.error

BASE_URL = os.environ.get("FLOWKIT_API_URL", "http://127.0.0.1:8100")


def post_json(endpoint: str, data: dict) -> dict:
    url = f"{BASE_URL}{endpoint}"
    req = urllib.request.Request(
        url,
        data=json.dumps(data, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(req) as res:
            return json.loads(res.read().decode("utf-8"))
    except urllib.error.URLError as e:
        print(f"[-] Lỗi gọi API {endpoint}: {e}", file=sys.stderr)
        if hasattr(e, "read"):
            print(f"    Chi tiết: {e.read().decode('utf-8')}", file=sys.stderr)
        sys.exit(1)


def check_health():
    url = f"{BASE_URL}/health"
    try:
        with urllib.request.urlopen(url) as res:
            data = json.loads(res.read().decode("utf-8"))
            print(f"[+] FlowKit Server đang chạy: {data}")
    except Exception as e:
        print(f"[-] Không thể kết nối tới FlowKit Server tại {BASE_URL}. Vui lòng chạy: python -m agent.main", file=sys.stderr)
        sys.exit(1)


def main():
    check_health()

    print("\n--- BƯỚC 1: TẠO PROJECT & THỰC THỂ (ENTITIES) ---")
    project_payload = {
        "name": "Heian-kyō 1000 - Kyoto Time Travel Vlog",
        "story": (
            "Một nữ vlogger hiện đại du hành thời gian về Heian-kyō (Kyoto) năm 1000, đúng thời Thiên hoàng Ichijō. "
            "Cô mặc đồ thường dân bằng vải gai, xem việc trao đổi hàng đổi hàng (vải lấy gạo), nếm thử món cơm phơi khô, "
            "nép mình né xe bò quý tộc trên đại lộ Suzaku, lặng người trước những tấm bia gỗ bên sông Kamo, chiêm ngưỡng "
            "cột son đỏ Daidairi và đổi chiếc dây buộc tóc hiện đại lấy chiếc lược gỗ làm kỷ niệm trước khi hoàng hôn buông xuống."
        ),
        "material": "realistic",
        "characters": [
            {
                "name": "Vlogger",
                "entity_type": "character",
                "description": (
                    "Authentic photorealistic portrait of ONE young Japanese woman (22-24 years old), "
                    "natural East Asian features, fair natural warm skin with visible fine pores, soft rounded-oval face, "
                    "long natural dark black-brown hair tied loosely, very soft natural everyday makeup (thin eyeliner, sheer lip tint). "
                    "Wearing an authentic middle Heian period Japanese commoner kosode robe made of coarse undyed hemp in natural pale oatmeal tone, "
                    "narrow flat indigo woven cord sash tied simply at the waist, mid-calf length, natural rustic weave. "
                    "TIGHT WAIST-UP FRAMING, front view, eye-level. STRICT ETHNICITY LOCK: 100% native East Asian Japanese. "
                    "NO Caucasian, NO Westerner, NO blonde hair, NO modern kimono styling, NO geisha makeup."
                ),
                "voice_description": (
                    "Young Japanese female travel vlogger (22-24 years old) speaking casual conversational Japanese (話し言葉 / タメ口). "
                    "Lively, authentic in-the-moment reaction, natural breath pauses, warm and expressive vocal delivery."
                )
            },
            {
                "name": "East Market Higashinoichi",
                "entity_type": "location",
                "description": (
                    "Authentic historical establishing view of Higashi-no-ichi east market in Heian-kyo, Japan, year 1000 CE. "
                    "Packed-earth muddy market lane with shallow drainage ditches, footprints and wooden handcart ruts. "
                    "Low open-air stalls of rough unpainted cedar posts and overhanging board-and-thatch roofs spaced apart. "
                    "Reed mats displaying bolts of undyed coarse hemp cloth, straw-tied rice sacks, dried fish, earthenware bowls. "
                    "Cool soft morning daylight 6000K, thin drifting cooking smoke. "
                    "Townspeople and traders all in plain undyed hemp garments. Wooded Higashiyama hills in far background. "
                    "PERIOD LOCK: Middle Heian Japan circa 1000 CE. NO stone paving, NO Edo machiya townhouses, NO red tourist lanterns, NO concrete."
                )
            },
            {
                "name": "Suzaku Avenue and Palace",
                "entity_type": "location",
                "description": (
                    "Authentic historical view of Suzaku-oji central ceremonial avenue and Daidairi palace enclosure in Heian-kyo, Japan, year 1000 CE. "
                    "Vast 80-meter-wide bare packed-earth avenue stretching north to south under an open overcast sky. "
                    "Willow trees and earthen drainage ditches lining both edges, low earthen walls enclosing official compounds in distance. "
                    "In the palace enclosure, massive round timber pillars coated in faded, chalky, weathered red-ochre lacquer. "
                    "Across the courtyard rises the great Daigokuden audience hall on a raised earthen-stone foundation with dark grey ceramic tile hip-and-gable roof. "
                    "PERIOD LOCK: Middle Heian 1000 CE. NO stone-paved plaza, NO bright freshly painted red shrine, NO concrete."
                )
            },
            {
                "name": "Kamo Riverbank",
                "entity_type": "location",
                "description": (
                    "Authentic historical landscape of the Kamo river on the eastern edge of Heian-kyo, Japan, year 1000 CE. "
                    "Wide open pale riverbed with loose white-grey cobbles and gravel bars, shallow clear water braiding through slow channels. "
                    "Untended wild banks covered in tall dry susuki pampas grass and leaning bare willows. "
                    "A few weathered, rain-silvered wooden memorial grave tablets lean simply in the dry grass at the water's edge. "
                    "Muted late-afternoon natural daylight transitioning to soft amber sunset, Higashiyama hills rising softly in the east. "
                    "PERIOD LOCK: Middle Heian 1000 CE. NO concrete embankment, NO stone revetments, NO bridges, NO modern monuments."
                )
            },
            {
                "name": "Boxwood Comb",
                "entity_type": "visual_asset",
                "description": (
                    "A small authentic middle Heian-period Japanese wooden comb (tsuge no kushi) made of pale fine-grained boxwood, "
                    "semi-circular traditional arch shape with hand-carved fine teeth, smooth gentle hand-polished natural wood sheen, "
                    "slight honest antique wear, resting on a rustic reed mat. Macro product view, crisp studio texture."
                )
            }
        ]
    }

    project = post_json("/api/projects", project_payload)
    project_id = project["id"]
    print(f"[+] Project tạo thành công! ID: {project_id}")

    print("\n--- BƯỚC 2: TẠO VIDEO TRONG PROJECT ---")
    video_payload = {
        "project_id": project_id,
        "title": "Heian 1000 Episode 1 - Mot Ngay Lam Thuong Dan Kyoto"
    }
    video = post_json("/api/videos", video_payload)
    video_id = video["id"]
    print(f"[+] Video tạo thành công! ID: {video_id}")

    print("\n--- BƯỚC 3: TẠO 10 PHÂN CẢNH (SCENES) ---")
    scenes = [
        # Scene 1: Hook rơi xuống chợ Đông (đồ hiện đại)
        {
            "display_order": 0,
            "chain_type": "ROOT",
            "character_names": ["Vlogger", "East Market Higashinoichi"],
            "prompt": (
                "Authentic smartphone selfie photograph, vertical 9:16, 28mm wide-angle front camera held at arm's length. "
                "TIGHT WAIST-UP SELFIE FRAMING, looking directly into lens with stunned expression. "
                "PAN-FOCUS (f/8-f/11) - DEEP DEPTH OF FIELD, face and background simultaneously 100% tack-sharp, STRICTLY ZERO BOKEH, ZERO PORTRAIT BLUR. "
                "Cool morning daylight 6000K, thin cooking smoke. Vlogger wearing modern white t-shirt. Standing in Higashi-no-ichi market lane of Heian-kyo 1000 AD, "
                "packed-earth muddy ground, rough cedar stalls with thatch roofs, porters in undyed hemp cloth. Free hand raised in open-palm helpless gesture. "
                "STRICT ETHNICITY LOCK: 100% East Asian Japanese. NO phone visible in frame."
            ),
            "video_prompt": (
                "0-3s: Handheld front camera with natural micro-shake. Still in modern clothes, she turns slightly, nose wrinkling at the pungent smell of wet earth, smoke, and dried fish, eyes widening in disbelief. Market porters carrying rice sacks move behind her. "
                "3-6s: She looks straight into the lens, lifting her free hand helplessly toward the market stalls behind her. "
                "6-8s: She speaks in natural casual Japanese, bewildered yet lively: \"えっ、ちょっと待って。においが…においがすごい。道は土だし、車の音もゼロ。しかも、なんか寒い。ここ、どこ？\" "
                "Audio: ambient street noise, chatter of market traders, wooden carts on dirt. No background music. Keep natural sound effects."
            ),
            "narrator_text": "えっ、ちょっと待って。においが…においがすごい。道は土だし、車の音もゼロ。しかも、なんか寒い。ここ、どこ？"
        },
        # Scene 2: Flycam toàn cảnh chợ Đông
        {
            "display_order": 1,
            "chain_type": "ROOT",
            "character_names": ["East Market Higashinoichi"],
            "prompt": (
                "Authentic photorealistic establishing aerial drone photograph (flycam), 4K, 28mm wide-angle, vertical 9:16. "
                "PAN-FOCUS f/8-f/11 - entire depth tack-sharp, ZERO BOKEH. Cool morning light 6000K. "
                "Low angle skimming just above the dark thatch roofs of Higashi-no-ichi market in Heian-kyo 1000 AD. "
                "Beyond, the straight earthen street grid stretches to the distant faded red palace gate and wooded Higashiyama hills. "
                "NO vlogger in frame, nobody looking at camera. STRICT ETHNICITY LOCK: 100% native Japanese."
            ),
            "video_prompt": (
                "0-3s: Smooth continuous aerial drone glide soaring slowly above dark thatch roofs and cloth drying racks of the market lane. "
                "3-8s: Buttery-smooth acceleration rising steadily upward into a panoramic view of the wide earthen avenues, low wooden roofs, and distant northern palace gates under an overcast sky. "
                "Audio: Gentle, sparse traditional koto and bamboo flute melody with natural morning wind. NO dialogue, NO voiceover."
            ),
            "narrator_text": ""
        },
        # Scene 3: Định vị & tuyên bố nhiệm vụ (đã đổi đồ)
        {
            "display_order": 2,
            "chain_type": "ROOT",
            "character_names": ["Vlogger", "East Market Higashinoichi"],
            "prompt": (
                "Authentic smartphone selfie photograph, vertical 9:16, 28mm front camera at arm's length. "
                "TIGHT WAIST-UP SELFIE FRAMING. PAN-FOCUS f/8-f/11, DEEP DEPTH OF FIELD, ZERO BOKEH. Cool daylight 6000K. "
                "Vlogger now wearing authentic Heian commoner hemp kosode robe. Her free hand is lightly tugging her own coarse hemp sleeve at the elbow with a wry smile. "
                "Standing in packed-earth market lane, traders bargaining animatedly behind her. STRICT ETHNICITY LOCK: 100% native Japanese."
            ),
            "video_prompt": (
                "0-3s: Handheld smartphone front camera micro-shake. She tugs her coarse hemp sleeve with a self-deprecating grin, glancing down at her clothes before looking back up into the lens. "
                "3-6s: She pans the phone slightly to show the lively cedar market stalls and moving shoppers in undyed hemp. "
                "6-8s: Speaking casually into the lens with a calm, amused tone: \"はい、着替えました。ここは平安京、西暦千年です。貴族じゃなくて、庶民の暮らしを見に行きます。\" "
                "Audio: Ambient market bustle, footsteps on dirt, gentle chatter. No background music. Keep natural sound effects."
            ),
            "narrator_text": "はい、着替えました。ここは平安京、西暦千年です。貴族じゃなくて、庶民の暮らしを見に行きます。"
        },
        # Scene 4: Chợ & kinh tế - Đổi vải lấy gạo (chạm tay vào lược)
        {
            "display_order": 3,
            "chain_type": "CONTINUATION",
            "character_names": ["Vlogger", "East Market Higashinoichi", "Boxwood Comb"],
            "prompt": (
                "Authentic smartphone selfie photograph, vertical 9:16, 28mm front camera. TIGHT WAIST-UP SELFIE FRAMING. "
                "PAN-FOCUS f/8-f/11, ZERO BOKEH. Standing close to an open cloth stall. On the reed mat beside her lie rolls of coarse hemp cloth and a row of small boxwood combs. "
                "Her free hand rests on the mat with fingertips touching one boxwood comb. Mid-ground: a kneeling trader pushes hemp cloth across to a farmer putting down a straw rice sack. "
                "STRICT ETHNICITY LOCK: 100% native Japanese."
            ),
            "video_prompt": (
                "0-3s: Her free hand slides fingertips slowly across a small boxwood comb on the mat with a longing look, then points toward the merchant and customer. The merchant vigorously pushes cloth forward while taking a straw bale of rice. "
                "3-6s: She turns back to the camera, eyes wide with genuine excitement, gesturing with her open hand toward the barter exchange. "
                "6-8s: Speaking with rapid, excited casual inflection: \"見て、今の。布と米、そのまま交換してる。銭より、米や布で払うことも多いんだって。顔見て決めてる。\" "
                "Audio: Rustle of straw sacks, merchant laughing and bargaining. No background music. Keep natural sound effects."
            ),
            "narrator_text": "見て、今の。布と米、そのまま交換してる。銭より、米や布で払うことも多いんだって。顔見て決めてる。"
        },
        # Scene 5: Ăn thử cơm phơi khô (hoshi-ii)
        {
            "display_order": 4,
            "chain_type": "CONTINUATION",
            "character_names": ["Vlogger", "East Market Higashinoichi"],
            "prompt": (
                "Authentic smartphone selfie photograph, vertical 9:16, 28mm front camera. TIGHT WAIST-UP SELFIE FRAMING. "
                "PAN-FOCUS f/8-f/11, ZERO BOKEH. Cool morning light. Vlogger in hemp kosode. "
                "Her free hand holds a small woven straw packet of dried rice (hoshi-ii) at chest height. In front of a rustic food stall with unglazed clay dishes. "
                "Behind her, a food vendor grins while wiping his hands on his apron. STRICT ETHNICITY LOCK: 100% native Japanese."
            ),
            "video_prompt": (
                "0-3s: She brings the dried rice packet closer to inspect it, takes a small crunchy bite, chewing thoughtfully with eyebrows raised at the hard, salty texture. "
                "3-6s: She nods with honest surprise, showing the small straw packet to the camera lens. "
                "6-8s: Speaking with cheerful curiosity: \"これ、乾かしたごはん。めちゃくちゃ硬いけど、かめば甘い。しょうゆはあるけど、今のとは別物なんだって。\" "
                "Audio: Crunchy chewing sound effect, cheerful market laughter nearby. No background music. Keep natural sound effects."
            ),
            "narrator_text": "これ、乾かしたごはん。めちゃくちゃ硬いけど、かめば甘い。しょうゆはあるけど、今のとは別物なんだって。"
        },
        # Scene 6: Xe bò quý tộc đi qua đại lộ Suzaku
        {
            "display_order": 5,
            "chain_type": "CONTINUATION",
            "character_names": ["Vlogger", "Suzaku Avenue and Palace"],
            "prompt": (
                "Authentic smartphone selfie photograph, vertical 9:16, 28mm front camera. TIGHT WAIST-UP SELFIE FRAMING. "
                "PAN-FOCUS f/8-f/11, ZERO BOKEH. Standing by roadside willow trees on the vast 80-meter-wide packed-earth Suzaku avenue. "
                "A black lacquered ox carriage with lowered bamboo blinds rolls past in the mid-ground. Townspeople nearby have stopped and bowed their heads. "
                "Her free hand is raised low in a cautious wait gesture. STRICT ETHNICITY LOCK: 100% native Japanese."
            ),
            "video_prompt": (
                "0-3s: Wide outdoor perspective. A black ox slowly pulls the heavy lacquered carriage across the avenue, wooden wheels creaking. Vlogger quickly steps back toward the willow tree, glancing sideways with caution and bowing slightly. "
                "3-6s: She brings the camera close to her face, keeping her head low and eyes cautious. "
                "6-8s: Whispering in hushed, tense tones straight into the lens: \"ぎっしゃが来た。牛車。みんな、道を空けて下向いてる。……誰も中を見ようとしない。\" "
                "Audio: Heavy slow clopping of ox hooves, low creaking of wooden wheels, silence of the crowd. No background music."
            ),
            "narrator_text": "ぎっしゃが来た。牛車。みんな、道を空けて下向いてる。……誰も中を見ようとしない。"
        },
        # Scene 7: Beat lắng bên bờ sông Kamo
        {
            "display_order": 6,
            "chain_type": "CONTINUATION",
            "character_names": ["Vlogger", "Kamo Riverbank"],
            "prompt": (
                "Authentic smartphone selfie photograph, vertical 9:16, 28mm front camera. TIGHT WAIST-UP SELFIE FRAMING. "
                "PAN-FOCUS f/8-f/11, ZERO BOKEH. Soft grey late-afternoon daylight 5800K. Standing on the wide gravel bed of Kamo river. "
                "Shallow clear braided water, wild susuki grass. Off to one side, simple weathered wooden grave tablets lean unevenly in the grass. "
                "An old woman places a bundle of reeds in silence. Her free hand hangs still at her side. STRICT ETHNICITY LOCK: 100% native Japanese."
            ),
            "video_prompt": (
                "0-3s: River breeze blowing wild susuki pampas grass. She turns slowly to glance at the weathered wooden tablets standing by the gravel bank, eyes softened with quiet contemplation. "
                "3-6s: She turns back to the camera, speaking slowly with a gentle, subdued, reflective voice. "
                "6-8s: Speaking with heartfelt sincerity: \"川のそばに、木の札が立ってる。誰かを、とむらってるのかな。名前を呼ぶ人がいる限り、その人は消えないんだと思う。\" "
                "Audio: Soft flowing water, rustling dry grass in the river wind. No background music. Keep natural sound effects."
            ),
            "narrator_text": "川のそばに、木の札が立ってる。誰かを、とむらってるのかな。名前を呼ぶ人がいる限り、その人は消えないんだと思う。"
        },
        # Scene 8: Cột son đỏ cổng Suzaku & Đại điện Daigokuden
        {
            "display_order": 7,
            "chain_type": "CONTINUATION",
            "character_names": ["Vlogger", "Suzaku Avenue and Palace"],
            "prompt": (
                "Authentic smartphone selfie photograph, vertical 9:16, 28mm front camera. TIGHT WAIST-UP SELFIE FRAMING. "
                "PAN-FOCUS f/8-f/11, ZERO BOKEH. Cool daylight. Standing inside Daidairi palace enclosure beside a massive round timber pillar coated in weathered, faded red-ochre lacquer. "
                "Across the open court stands the great Daigokuden audience hall on a raised earthen-stone foundation with broad timber steps. "
                "Her free hand is laid flat against the aged red pillar. STRICT ETHNICITY LOCK: 100% native Japanese."
            ),
            "video_prompt": (
                "0-3s: Her palm slides gently across the weathered chalky red lacquer of the giant pillar, feeling the wood grain beneath her fingers. She gazes up at the vast dark grey ceramic roof of Daigokuden. "
                "3-6s: She turns to the lens, face filled with solemn historical reverence. "
                "6-8s: Speaking in a low, reverent voice: \"この朱色、本物。だいごくでん、まだ建ってる。……百七十七年後に焼けて、その後は再建されないんだ。\" "
                "Audio: Open courtyard breeze, distant deep bell tone, muffled footsteps of distant courtiers. No background music."
            ),
            "narrator_text": "この朱色、本物。だいごくでん、まだ建ってる。……百七十七年後に焼けて、その後は再建されないんだ。"
        },
        # Scene 9: Chiếc lược kỷ niệm lúc hoàng hôn
        {
            "display_order": 8,
            "chain_type": "CONTINUATION",
            "character_names": ["Vlogger", "Kamo Riverbank", "Boxwood Comb"],
            "prompt": (
                "Authentic smartphone selfie photograph, vertical 9:16, 28mm front camera. TIGHT WAIST-UP SELFIE FRAMING. "
                "PAN-FOCUS f/8-f/11, ZERO BOKEH. Low warm sunset amber light 4600K across Kamo river gravel. Higashiyama hills turning deep blue. "
                "Vlogger smiling warmly. In her raised free hand she holds up the small pale boxwood comb from Scene 4, turned to catch the evening light. "
                "Behind her, villagers walk home across the shallows. STRICT ETHNICITY LOCK: 100% native Japanese."
            ),
            "video_prompt": (
                "0-3s: Low golden sunset light glinting across the Kamo river. She raises the boxwood comb into the light, smiling fondly at it before tucking it safely into her kosode sash. "
                "3-6s: She looks warmly into the camera lens, giving a slight, grateful nod to the viewers. "
                "6-8s: Speaking warmly and tenderly with a peaceful smile: \"あのくし、ヘアゴムと交換してもらえた。千年後の世界に、これだけ持って帰ります。平安京、いい街でした。\" "
                "Audio: Gentle evening water flow, distant cicadas or crickets, peaceful river breeze. No background music."
            ),
            "narrator_text": "あのくし、ヘアゴムと交換してもらえた。千年後の世界に、これだけ持って帰ります。平安京、いい街でした。"
        },
        # Scene 10: Coda Flycam hoàng hôn sông Kamo
        {
            "display_order": 9,
            "chain_type": "ROOT",
            "character_names": ["Kamo Riverbank"],
            "prompt": (
                "Authentic photorealistic establishing aerial drone photograph (flycam), 4K, 28mm wide-angle, vertical 9:16. "
                "PAN-FOCUS f/8-f/11, ZERO BOKEH. Low sunset light 4600K skimming just above dry susuki grass and pale gravel bars of Kamo river. "
                "The shallow braided channels reflect amber light. Behind, the grid of Heian-kyo stretches west toward the dark silhouette of the mountains. "
                "NO vlogger in frame. STRICT ETHNICITY LOCK: 100% native Japanese."
            ),
            "video_prompt": (
                "0-3s: Smooth fluid aerial glide soaring low over the glowing water channels and golden susuki plumes of Kamo river. "
                "3-8s: Stepping into a high, majestic climb as the capital slips into dusk, hearth smoke rising from small wooden houses under the glowing evening sky. "
                "Audio: Solitary, gentle koto melody fading slowly into quiet evening river wind. NO dialogue, NO voiceover."
            ),
            "narrator_text": ""
        }
    ]

    for sc in scenes:
        sc_payload = {
            "video_id": video_id,
            "display_order": sc["display_order"],
            "prompt": sc["prompt"],
            "video_prompt": sc["video_prompt"],
            "character_names": sc["character_names"],
            "chain_type": sc["chain_type"],
            "narrator_text": sc["narrator_text"]
        }
        res_scene = post_json("/api/scenes", sc_payload)
        print(f"  [+] Scene {sc['display_order'] + 1}/10 tạo thành công (ID: {res_scene['id']})")

    print("\n=======================================================")
    print("🎉 KHỞI TẠO HOÀN TẤT DỰ ÁN KYOTO HEIAN 1000!")
    print(f"Project ID : {project_id}")
    print(f"Video ID   : {video_id}")
    print("\nCác bước tiếp theo bạn có thể chạy ngay:")
    print(f"  1. Sinh ảnh mẫu các thực thể :  /fk-gen-refs {project_id}")
    print(f"  2. Sinh ảnh Frame 0 các cảnh :  /fk-gen-images {project_id} {video_id}")
    print(f"  3. Sinh 10 đoạn video 8s     :  /fk-gen-videos {project_id} {video_id}")
    print(f"  4. Lồng tiếng TTS tiếng Nhật :  /fk-gen-narrator {video_id}")
    print(f"  5. Ghép video hoàn chỉnh     :  /fk-concat-fit-narrator {video_id}")
    print("=======================================================")


if __name__ == "__main__":
    main()
