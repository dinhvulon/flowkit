#!/usr/bin/env python3
"""
FlowKit — Script Khởi Tạo Dự Án: Kamakura 1274 (Kháng Chiến Vịnh Hakata POV Vlog)
Tự động nạp kịch bản Vịnh Hakata 1274 với 10 phân cảnh, thoại tiếng Nhật đàm thoại
chuẩn nhịp mora và thiết lập quang học Pan-Focus f/8-f/11 vào FlowKit Local API (cổng 8100).

Sử dụng:
    python scripts/create_kamakura_1274.py
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


def put_json(endpoint: str, data: dict) -> dict:
    url = f"{BASE_URL}{endpoint}"
    req = urllib.request.Request(
        url,
        data=json.dumps(data, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="PUT"
    )
    try:
        with urllib.request.urlopen(req) as res:
            return json.loads(res.read().decode("utf-8"))
    except Exception as e:
        print(f"[-] Cảnh báo: không thể set active project: {e}", file=sys.stderr)
        return {}


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
        "name": "Kamakura 1274 - Mongol Invasion Hakata Bay POV Vlog",
        "story": (
            "Một nữ vlogger hiện đại du hành thời gian về Vịnh Hakata (Kyushu) tháng 11 năm 1274 (Chiến dịch Bun'ei - Kháng chiến chống quân Mông Cổ lần 1). "
            "Rơi xuống bờ biển buốt lạnh giữa lúc hạm đội 900 chiến thuyền Nguyên Mông đen ngòm xuất hiện ngoài khơi, cô thay sang trang phục thường dân vải gai chàm, "
            "chạy dọc phòng tuyến cọc gỗ dã chiến cùng dân làng, cận cảnh mảnh vỡ quả bom sấm sét 'tetsuhau' đầy khói đen, chứng kiến kỵ sĩ samurai uy nghiêm trong "
            "bộ đại giáp Ō-yoroi lụa đỏ phi ngựa giương cung nghênh địch, lắng đọng bên bức tượng Jizo trong rừng thông và chứng kiến trận cuồng phong đầu tiên nổi lên lúc hoàng hôn."
        ),
        "material": "realistic",
        "characters": [
            {
                "name": "Vlogger",
                "entity_type": "character",
                "description": (
                    "Authentic photorealistic portrait of ONE young Japanese woman (22-24 years old), "
                    "natural East Asian features, fair natural warm skin with visible fine pores, soft rounded-oval face, "
                    "long natural dark black-brown hair tied back neatly, very soft natural everyday makeup. "
                    "Wearing authentic Kamakura period Japanese commoner short kosode robe made of coarse handwoven hemp dyed in muted deep indigo (aizome), "
                    "tied with a simple rough hemp cord sash at waist, straw sandals (waraji) on feet. "
                    "TIGHT WAIST-UP FRAMING, front view, eye-level. STRICT ETHNICITY LOCK: 100% native East Asian Japanese. "
                    "NO Caucasian, NO Westerner, NO blonde hair, NO modern kimono styling, NO geisha makeup."
                ),
                "voice_description": (
                    "Young Japanese female travel vlogger (22-24 years old) speaking casual conversational Japanese (話し言葉 / タメ口). "
                    "Authentic in-the-moment reaction, lively, natural breath pauses, warm and expressive vocal delivery."
                )
            },
            {
                "name": "Kamakura Cavalry Samurai",
                "entity_type": "character",
                "description": (
                    "Authentic photorealistic portrait of ONE fierce Kamakura period samurai warrior gokenin (30-35 years old), "
                    "strong weathered East Asian Japanese features, intense determined eyes, short-trimmed neat mustache and beard. "
                    "Wearing authentic heavy Kamakura-era boxy Ō-yoroi armor laced with vibrant scarlet red silk cords (hi-odoshi), "
                    "massive rectangular shoulder guards (ō-sode), iron helmet (kabuto) with pointed kuwagata brass horns. "
                    "Astride a sturdy wooden-saddled Japanese warhorse, holding a massive 2-meter asymmetrical Japanese longbow (wakyū). "
                    "STRICT ETHNICITY LOCK: 100% native East Asian Japanese warrior."
                ),
                "voice_description": (
                    "Deep, commanding resonant voice of a medieval Japanese samurai warrior."
                )
            },
            {
                "name": "Hakata Bay Beach and Fleet",
                "entity_type": "location",
                "description": (
                    "Authentic historical establishing view of Hakata Bay coastline, Kyushu, Japan, November 1274 AD. "
                    "Wide cold grey-sand beach, foaming ocean waves crashing on the wet shore, wind-bent dark coastal pine trees (matsu). "
                    "Far out across the grey churning sea, hundreds of ominous dark Yuan-Mongol expedition fleet warships are silhouetted on the horizon under heavy low dark autumn storm clouds. "
                    "Distant signal smoke columns rising from shoreline watch posts. "
                    "PERIOD LOCK: Kamakura Japan 1274 AD. NO modern ships, NO concrete breakwaters, NO electric poles."
                )
            },
            {
                "name": "Coastal Village Palisades",
                "entity_type": "location",
                "description": (
                    "Authentic historical view of a defensive palisade line in a coastal fishing hamlet along Hakata Bay, Japan, November 1274 AD. "
                    "Crude defensive barricades made of sharpened pine stakes and bundles of bamboo, dirt mounds, earthen drainage ditches. "
                    "Low wooden thatch-roofed fishermen huts, coiled ropes, drying mullet fish racks, straw sacks of rice and millet. "
                    "Distanced smoke of signal fires. Villagers and foot soldiers (ashigaru) in indigo-dyed rough hemp kosode and straw sandals hurrying about with sharpened bamboo spears. "
                    "PERIOD LOCK: Kamakura Japan 1274 AD."
                )
            },
            {
                "name": "Tetsuhau Shrapnel Bomb",
                "entity_type": "visual_asset",
                "description": (
                    "Authentic historical close-up photograph of an exploded Yuan-Mongol 'tetsuhau' explosive bomb remnant resting on wet sand of Hakata Bay, 1274 AD. "
                    "A shattered spherical ceramic and cast-iron shell, jagged cracked edges, heavily scorched with black gunpowder residue, scattering small round river stones and iron shrapnel fragments nearby on the cold wet grey sand. "
                    "Delicate wisp of thin lingering white smoke rising from the cracked casing."
                )
            },
            {
                "name": "Hakozaki Shrine Torii Path",
                "entity_type": "location",
                "description": (
                    "Authentic historical view of the pine grove approach near Hakozaki Hachiman Shrine, Hakata, Japan, November 1274 AD. "
                    "Dense dark green Japanese coastal pine forest with gnarled twisted trunks, ground covered with dry brown pine needles. "
                    "A weathered rustic moss-covered stone torii gate standing along a winding sandy footpath. "
                    "Fallen pine cones, small rustic carved stone Jizo roadside guardian statues. "
                    "Heavy cold autumn sea wind blowing through the pine branches under an overcast slate-grey sky."
                )
            }
        ]
    }

    res_proj = post_json("/api/projects", project_payload)
    project_id = res_proj["id"]
    print(f"[+] Project tạo thành công! ID: {project_id}")
    put_json("/api/active-project", {"project_id": project_id})
    print(f"[+] Đã tự động kích hoạt Project ID {project_id} làm Active Project!")

    print("\n--- BƯỚC 2: TẠO VIDEO CONTAINER ---")
    video_payload = {
        "project_id": project_id,
        "name": "Kamakura 1274 Hakata Bay Vlog - Bun'ei Campaign",
        "description": "POV Smartphone Vlog du hành thời gian về Vịnh Hakata năm 1274 (Kháng chiến chống Mông Cổ)"
    }
    res_vid = post_json("/api/videos", video_payload)
    video_id = res_vid["id"]
    print(f"[+] Video tạo thành công! ID: {video_id}")

    print("\n--- BƯỚC 3: TẠO 10 PHÂN CẢNH (SCENES) ---")
    scenes = [
        # Scene 1: Hook rơi xuống bờ vịnh Hakata (đồ hiện đại)
        {
            "display_order": 0,
            "chain_type": "ROOT",
            "character_names": ["Vlogger", "Hakata Bay Beach and Fleet"],
            "prompt": (
                "Authentic smartphone selfie photograph, vertical 9:16, 28mm wide-angle front camera held at arm's length. "
                "TIGHT WAIST-UP SELFIE FRAMING, looking directly into lens with startled, wide-eyed expression. "
                "PAN-FOCUS (f/8-f/11) - DEEP DEPTH OF FIELD, face and background simultaneously 100% tack-sharp, STRICTLY ZERO BOKEH, ZERO PORTRAIT BLUR. "
                "Cool overcast daylight 6200K, fierce cold coastal wind blowing loose hair strands across her face. "
                "Vlogger wearing modern casual white t-shirt. Standing on the cold grey-sand beach of Hakata Bay in 1274 AD, foaming waves behind her, "
                "hundreds of dark Yuan invasion warships silhouetted on the distant horizon under menacing storm clouds. "
                "Free hand clutching her chest in shock. STRICT ETHNICITY LOCK: 100% East Asian Japanese. NO phone visible."
            ),
            "video_prompt": (
                "0-3s: Handheld smartphone front camera micro-shake. Bitter ocean wind whips her hair across her face. "
                "She turns slightly toward the sea, squinting at the terrifying fleet of warships on the horizon, eyes wide with genuine shock. "
                "3-6s: She whips back to face the camera lens, shivering in her thin white t-shirt, pointing a trembling hand out toward the bay. "
                "6-8s: Speaking in natural, panicked yet lively casual Japanese: \"えっ、寒っ！風、強すぎない？……ちょっと待って、沖に見えるあれ、船？何百隻もあるんだけど…ここ、どこ？\" "
                "Audio: Fierce coastal wind howling, crashing ocean waves, faint ominous wooden war horns in the distance. No background music. Keep natural sound effects."
            ),
            "narrator_text": "えっ、寒っ！風、強すぎない？……ちょっと待って、沖に見えるあれ、船？何百隻もあるんだけど…ここ、どこ？"
        },
        # Scene 2: Flycam toàn cảnh bãi biển & hạm đội chiến thuyền
        {
            "display_order": 1,
            "chain_type": "ROOT",
            "character_names": ["Hakata Bay Beach and Fleet"],
            "prompt": (
                "Authentic photorealistic establishing aerial drone photograph (flycam), 4K, 28mm wide-angle, vertical 9:16. "
                "PAN-FOCUS f/8-f/11 - entire depth tack-sharp, ZERO BOKEH. Dark dramatic late-autumn daylight 6200K. "
                "Low angle skimming just above the wind-tossed crowns of coastal pine trees along Hakata Bay in 1274 AD. "
                "Beyond, the churning dark ocean water stretches out toward hundreds of wooden Yuan dynasty battleships anchored in formation, "
                "banners fluttering in the gale under towering slate-grey storm clouds. "
                "NO vlogger in frame, nobody looking at camera. STRICT ETHNICITY LOCK: 100% native Japanese."
            ),
            "video_prompt": (
                "0-3s: Smooth continuous aerial drone glide soaring rapidly over dark wind-whipped pine trees toward the foaming shoreline. "
                "3-8s: Fluid high-altitude ascent revealing the vast panoramic expanse of Hakata Bay, with hundreds of dark wooden invasion ships dotting the churning sea and dark storm squalls approaching from the horizon. "
                "Audio: Roaring sea gale, crashing heavy surf, distant low resonant boom of war drums. NO dialogue, NO voiceover."
            ),
            "narrator_text": ""
        },
        # Scene 3: Đổi trang phục sang vải gai chàm & định vị thời gian
        {
            "display_order": 2,
            "chain_type": "ROOT",
            "character_names": ["Vlogger", "Coastal Village Palisades"],
            "prompt": (
                "Authentic smartphone selfie photograph, vertical 9:16, 28mm front camera at arm's length. "
                "TIGHT WAIST-UP SELFIE FRAMING. PAN-FOCUS f/8-f/11, DEEP DEPTH OF FIELD, ZERO BOKEH. "
                "Cool overcast daylight 6000K. Vlogger now walking along a coastal dirt lane, wearing authentic Kamakura commoner rough indigo hemp kosode and straw sandals (waraji). "
                "Her free hand wipes windblown sand from her cheek with a grim, determined smile. "
                "Coastal villagers carrying straw-wrapped bundles run past in the background. STRICT ETHNICITY LOCK: 100% native Japanese."
            ),
            "video_prompt": (
                "0-3s: Handheld front camera with rhythmic walking gait oscillation as she walks briskly along the coastal dirt path. "
                "She glances down at her coarse indigo hemp sleeve, brushing off grit before looking straight into the lens. "
                "3-6s: She angles the camera slightly to show fishermen and women hurriedly evacuating behind her. "
                "6-8s: Speaking with an earnest, tense whisper into the lens: \"はい、着替えました。ここは千二百七十四年、博多湾です。……元軍が、本当に攻めてきた。\" "
                "Audio: Sound of hurried footsteps on dirt, straw sandals rustling, coastal wind, shouting voices of villagers. No background music. Keep natural sound effects."
            ),
            "narrator_text": "はい、着替えました。ここは千二百七十四年、博多湾です。……元軍が、本当に攻めてきた。"
        },
        # Scene 4: Chiến lũy & Dân làng chuẩn bị nghênh chiến
        {
            "display_order": 3,
            "chain_type": "CONTINUATION",
            "character_names": ["Vlogger", "Coastal Village Palisades"],
            "prompt": (
                "Authentic smartphone selfie photograph, vertical 9:16, 28mm front camera. TIGHT WAIST-UP SELFIE FRAMING. "
                "PAN-FOCUS f/8-f/11, ZERO BOKEH. Cold daylight. Vlogger in indigo hemp clothes walking alongside crude defensive palisades of sharpened pine stakes. "
                "Behind her, local foot soldiers (ashigaru) and villagers are feverishly sharpening bamboo spears with machetes and stacking heavy straw rice bales. "
                "Her free hand is gesturing toward the defensive barricades. STRICT ETHNICITY LOCK: 100% native Japanese."
            ),
            "video_prompt": (
                "0-3s: Walking POV along the wooden palisade with gentle camera sway matching her footsteps. "
                "She gestures with her open hand toward two villagers violently chopping bamboo into sharp defensive stakes. "
                "3-6s: She turns back to the camera, eyes reflecting the solemn, grave atmosphere around her. "
                "6-8s: Speaking with brisk, focused casual delivery: \"村の人たち、みんな走ってる。竹の槍を削って、米を運んでる。パニックっていうより、覚悟を決めた顔してる。\" "
                "Audio: Thudding of wood axes, chopping bamboo, low determined voices of men working. No background music. Keep natural sound effects."
            ),
            "narrator_text": "村の人たち、みんな走ってる。竹の槍を削って、米を運んでる。パニックっていうより、覚悟を決めた顔してる。"
        },
        # Scene 5: Cận cảnh xúc giác - Mảnh vỡ bom sấm sét Tetsuhau
        {
            "display_order": 4,
            "chain_type": "CONTINUATION",
            "character_names": ["Vlogger", "Tetsuhau Shrapnel Bomb", "Hakata Bay Beach and Fleet"],
            "prompt": (
                "Authentic smartphone selfie photograph, vertical 9:16, 28mm front camera. TIGHT WAIST-UP SELFIE FRAMING. "
                "PAN-FOCUS f/8-f/11, ZERO BOKEH. Cold daylight. Vlogger is crouched low on the damp grey sandy ground near a defensive trench. "
                "Beside her on the sand lies the shattered black-scorched ceramic casing of an exploded tetsuhau bomb. "
                "Her free hand's index finger points down toward the charred bomb fragments. STRICT ETHNICITY LOCK: 100% native Japanese."
            ),
            "video_prompt": (
                "0-3s: She lowers the camera slightly, her fingers hovering inches above the black-scorched ceramic bomb casing on the sand, inspecting the jagged shrapnel with intense curiosity and awe. "
                "3-6s: She brings the camera back up to chest level, eyes wide as she explains the historical weapon. "
                "6-8s: Speaking rapidly in an amazed whisper: \"これ、見て。てつはうの破片。火薬で爆発する爆弾なんだって。馬が音にパニックになって、陣形が崩れたらしい。\" "
                "Audio: Faint crackle of smoldering soot, wind howling across sand dunes, distant hollow boom. No background music. Keep natural sound effects."
            ),
            "narrator_text": "これ、見て。てつはうの破片。火薬で爆発する爆弾なんだって。馬が音にパニックになって、陣形が崩れたらしい。"
        },
        # Scene 6: Kỵ sĩ Samurai giáp Ō-yoroi lụa đỏ phi ngựa xuất trận
        {
            "display_order": 5,
            "chain_type": "CONTINUATION",
            "character_names": ["Vlogger", "Kamakura Cavalry Samurai", "Hakozaki Shrine Torii Path"],
            "prompt": (
                "Authentic smartphone selfie photograph, vertical 9:16, 28mm front camera. TIGHT WAIST-UP SELFIE FRAMING. "
                "PAN-FOCUS f/8-f/11, ZERO BOKEH. Overcast light filtering through coastal pine trees. "
                "Vlogger stands by roadside pine trunk, looking back over her shoulder in awe. "
                "Mid-ground: a Kamakura samurai warrior in majestic scarlet-laced Ō-yoroi armor on a galloping warhorse, holding a massive asymmetrical longbow (wakyū). "
                "Her free hand is raised defensively to shield from flying dirt. STRICT ETHNICITY LOCK: 100% native Japanese."
            ),
            "video_prompt": (
                "0-3s: The ground trembles as a mighty samurai on horseback gallops past along the pine path, red armor cords shining, massive longbow held high. "
                "Vlogger quickly leans back against a pine tree to avoid flying dirt clods, eyes wide in disbelief. "
                "3-6s: She whips the camera around to catch the retreating cavalry warrior before turning back into the lens, breathless. "
                "6-8s: Speaking with rapid, excited breathless wonder: \"うわ、馬！おおよろいの武士だ。赤い糸がすごく鮮やか。……一人で何十人も相手にするつもりなのかな。\" "
                "Audio: Heavy thundering horse hooves on packed dirt, jingling metal plates and armor cords, loud samurai battle yell. No background music."
            ),
            "narrator_text": "うわ、馬！おおよろいの武士だ。赤い糸がすごく鮮やか。……一人で何十人も相手にするつもりなのかな。"
        },
        # Scene 7: Tiếng sấm trận & Đấu pháp mới của quân Nguyên
        {
            "display_order": 6,
            "chain_type": "CONTINUATION",
            "character_names": ["Vlogger", "Hakata Bay Beach and Fleet"],
            "prompt": (
                "Authentic smartphone selfie photograph, vertical 9:16, 28mm front camera. TIGHT WAIST-UP SELFIE FRAMING. "
                "PAN-FOCUS f/8-f/11, ZERO BOKEH. Chilly darkening afternoon light. Vlogger ducking down low behind a sandy coastal ridge. "
                "In the distant background across the beach, black gunpowder smoke billows into the grey sky. "
                "Her free hand is cupped near her ear listening to the unsettling sounds of battle. STRICT ETHNICITY LOCK: 100% native Japanese."
            ),
            "video_prompt": (
                "0-3s: Ducking low behind a coastal sand dune, she flinches as the piercing whistle of a samurai kaburaya arrow shrieks overhead followed by the eerie rattle of Mongol bronze gongs. "
                "3-6s: She turns to the lens, face tense, clutching her collar against the biting sea gale. "
                "6-8s: Whispering urgently and somberly straight into the camera: \"変な太鼓の音が響いてる。日本の戦い方と全然違う。名乗りを上げる前に、毒矢が一斉に飛んでくるんだって。\" "
                "Audio: Piercing whistle of a kaburaya whistling arrow, clashing bronze gongs, distant roar of war cries, heavy gusts of wind. No background music."
            ),
            "narrator_text": "変な太鼓の音が響いてる。日本の戦い方と全然違う。名乗りを上げる前に、毒矢が一斉に飛んでくるんだって。"
        },
        # Scene 8: Phút lắng đọng bên tượng Jizo rặng thông
        {
            "display_order": 7,
            "chain_type": "CONTINUATION",
            "character_names": ["Vlogger", "Hakozaki Shrine Torii Path"],
            "prompt": (
                "Authentic smartphone selfie photograph, vertical 9:16, 28mm front camera. TIGHT WAIST-UP SELFIE FRAMING. "
                "PAN-FOCUS f/8-f/11, ZERO BOKEH. Dim late afternoon light 5600K through dense pine needles. "
                "Vlogger stands beside a small weathered stone Jizo statue covered in soft green moss. "
                "Dry brown pine needles swirling in the chilly wind. "
                "Her free hand gently touches the cold mossy stone head of the Jizo statue. STRICT ETHNICITY LOCK: 100% native Japanese."
            ),
            "video_prompt": (
                "0-3s: Wind rustling heavily through the pine crowns. Her hand rests gently on the weathered stone Jizo statue, her chest heaving as she catches her breath after running, gaze softened with profound emotion. "
                "3-6s: She looks directly into the lens, speaking slowly with deep, heartfelt sincerity. "
                "6-8s: Speaking with contemplative emotion: \"松の林まで逃げてきた。……教科書では一行の事件だけど、ここに生きてる人にとっては、今日が命がけの現実なんだ。\" "
                "Audio: Melancholy wind sighing through dense pine boughs, dry needles rustling on the ground, distant church-like silence. No background music. Keep natural sound effects."
            ),
            "narrator_text": "松の林まで逃げてきた。……教科書では一行の事件だけど、ここに生きてる人にとっては、今日が命がけの現実なんだ。"
        },
        # Scene 9: Hoàng hôn & Gió bão thần phong (Kamikaze) bắt đầu nổi lên
        {
            "display_order": 8,
            "chain_type": "CONTINUATION",
            "character_names": ["Vlogger", "Hakata Bay Beach and Fleet"],
            "prompt": (
                "Authentic smartphone selfie photograph, vertical 9:16, 28mm front camera. TIGHT WAIST-UP SELFIE FRAMING. "
                "PAN-FOCUS f/8-f/11, ZERO BOKEH. Deep dramatic sunset amber-red light 4200K breaking through thick storm clouds over Hakata Bay. "
                "Wild gale-force wind whipping her hair and clothes. In her raised free hand she holds up a small arrowhead fragment found in the sand. "
                "Behind her, giant white-capped ocean breakers crash violently against the shore. STRICT ETHNICITY LOCK: 100% native Japanese."
            ),
            "video_prompt": (
                "0-3s: Blazing amber sunset light cuts across the dark churning bay. Gale-force wind whips her indigo tunic violently as towering waves smash onto the shore. She holds up a small arrow tip to catch the dying sunlight. "
                "3-6s: She turns to the camera, smiling with awe and goosebumps as the storm gathers power. "
                "6-8s: Speaking with goosebumps in a wind-buffeted voice: \"海からの風が、どんどん冷たくなってきた。……今夜、嵐が来る。この風が、歴史を変えるのかな。\" "
                "Audio: Powerful howling sea storm wind, thundering crash of massive surf, fluttering banners. No background music. Keep natural sound effects."
            ),
            "narrator_text": "海からの風が、どんどん冷たくなってきた。……今夜、嵐が来る。この風が、歴史を変えるのかな。"
        },
        # Scene 10: Flycam hoàng hôn bão tố Vịnh Hakata (Câm)
        {
            "display_order": 9,
            "chain_type": "ROOT",
            "character_names": ["Hakata Bay Beach and Fleet"],
            "prompt": (
                "Authentic photorealistic establishing aerial drone photograph (flycam), 4K, 28mm wide-angle, vertical 9:16. "
                "PAN-FOCUS f/8-f/11, ZERO BOKEH. Dramatic twilight 3800K after sunset. "
                "Deep violet and fiery crimson sky above the violent churning waves of Hakata Bay in 1274 AD. "
                "Coastal pine forests bending under ferocious gale winds. "
                "Along the hill ridges, bright orange beacon signal fires flicker against the storm darkness. "
                "NO vlogger in frame. STRICT ETHNICITY LOCK: 100% native Japanese."
            ),
            "video_prompt": (
                "0-3s: Low dramatic aerial glide over violently thrashing pine treetops and frothing white shoreline waves. "
                "3-8s: Soaring high into the darkening tempest sky, revealing the vast silhouette of Hakata Bay, flickering beacon fires along the ridges, and the storm clouds swallowing the horizon. "
                "Audio: Solitary, haunting shakuhachi flute melody swelling, merging with the epic roar of ocean waves and howling storm gale. NO dialogue, NO voiceover."
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
    print("🎉 KHỞI TẠO HOÀN TẤT DỰ ÁN KAMAKURA 1274 (VỊNH HAKATA)!")
    print(f"Project ID : {project_id}")
    print(f"Video ID   : {video_id}")
    print("\nCác bước tiếp theo bạn có thể chạy ngay:")
    print(f"  1. Sinh ảnh mẫu các thực thể :  /fk-gen-refs {project_id}")
    print(f"  2. Nạp mặt thật (tùy chọn)   :  /fk-upload-ref \"C:/photo.jpg\" --entity \"Vlogger\"")
    print(f"  3. Chạy toàn bộ pipeline tự động:")
    print(f"     /fk-pipeline --r2v --tts --concat")
    print("=======================================================")


if __name__ == "__main__":
    main()
