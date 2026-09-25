import os

artifact_path = r"C:/Users/Administrator/.gemini/antigravity-ide/brain/e22150ce-4262-4e3c-8619-a7731a7f7c3a/clean_scene_images_gallery.md"
brain_images_dir = "C:/Users/Administrator/.gemini/antigravity-ide/brain/e22150ce-4262-4e3c-8619-a7731a7f7c3a/images"

scenes_info = [
    {
        "idx": 1,
        "title": "The Shock Arrival (Bờ sông Euphrates & Cỗ xe bò lướt sát ống kính)",
        "mid": "44d1a433-a291-4592-ad4c-79ca28c870d6",
        "fixed": False,
        "note": "",
        "dialogue": 'Mia: "You guys... welcome to Babylon, 570 BC! And right behind me is the legendary Hanging Gardens!"'
    },
    {
        "idx": 2,
        "title": "Story of King & Queen (Vừa đi vừa kể chuyện Vua Nebuchadnezzar & Hoàng Hậu Amytis)",
        "mid": "8030c158-0b53-4d44-9cb7-5231a90437c4",
        "fixed": False,
        "note": "",
        "dialogue": 'Mia: "King Nebuchadnezzar built this entire mountain of green for Queen Amytis because she missed the forested hills of Media."'
    },
    {
        "idx": 3,
        "title": "Euphrates Quffa Boats (POV sông Euphrates & người chèo thuyền thúng quffa chở đất, cây non)",
        "mid": "5df99f7d-c059-4d9f-b346-ad8f7f111e05",
        "fixed": True,
        "note": "✓ ĐÃ SỬA: Đã có người chèo thuyền Babylon cơ bắp đứng chèo thuyền quffa tròn bằng gỗ mun; loại bỏ thuyền trôi dạt vô chủ.",
        "dialogue": 'Mia: "Every single drop of water and every basket of rich soil feeding those rooftop trees starts right here from this river."'
    },
    {
        "idx": 4,
        "title": "Ancient Chain Pump (Ngước nhìn guồng nước / bơm xích khổng lồ nâng nước sông)",
        "mid": "a02f1377-9b8e-4b4a-ab16-a0d81cb30627",
        "fixed": False,
        "note": "",
        "dialogue": 'Mia: "Look at this mechanical chain pump! 2,500 years ago, lifting thousands of gallons into the desert sky every hour!"'
    },
    {
        "idx": 5,
        "title": "Waterproof Secret (POV xúc giác: Sờ lớp hắc ín bitum & chiếu cói chống thấm)",
        "mid": "8dc0de50-f4ce-45c4-aa5a-76dfb25c0482",
        "fixed": False,
        "note": "",
        "dialogue": 'Mia: "Feel this texture. Natural tar and reeds waterproofing the stone so water does not flood the royal palace chambers below."'
    },
    {
        "idx": 6,
        "title": "The Colossal Vaults (Đi dưới vòm gạch nung khổng lồ đỡ ngọn núi cây)",
        "mid": "1f03ae6c-013c-4b81-ab5e-65e03a0e93cc",
        "fixed": False,
        "note": "",
        "dialogue": 'Mia: "These arches are holding up hundreds of thousands of tons of wet earth, palm trees, and mountain water right above my head."'
    },
    {
        "idx": 7,
        "title": "Garden Bazaar (Dạo chợ nông sản dưới bóng râm vườn treo, lựu đỏ & vả tươi)",
        "mid": "7edbc83a-7303-40a5-bb1e-f4d47ea74aed",
        "fixed": False,
        "note": "",
        "dialogue": 'Mia: "The smell here is heaven... sweet mountain figs, fresh dates, and freshly harvested royal pomegranates."'
    },
    {
        "idx": 8,
        "title": "Table Prop-up Dining #1 (Gác máy lên bàn: Ngồi ăn quả vả tươi hái tại vườn)",
        "mid": "d0a7863a-d7ed-4838-8a03-2a82a96279a1",
        "fixed": True,
        "note": "✓ ĐÃ SỬA: Loại bỏ hoàn toàn điện thoại di động trên bàn ăn; khung máy gác tĩnh candid nhìn Mia thưởng thức quả sung tươi.",
        "dialogue": 'Mia: "Honestly, tasting a fig picked directly from the Hanging Gardens of Babylon? This is absolute bucket-list perfection."'
    },
    {
        "idx": 9,
        "title": "Gravity-Fed Aqueducts (Đi dọc kênh dẫn nước bậc thang đá vôi trong vắt)",
        "mid": "821272fe-ba26-48dc-b8eb-f34a8ddec8de",
        "fixed": False,
        "note": "",
        "dialogue": 'Mia: "Total engineering genius. Gravity channels carrying cold water to thousands of exotic plants on every tier."'
    },
    {
        "idx": 10,
        "title": "Ancient Trade: Silver Shekels (POV xúc giác: Cân cuộn dây bạc shekel đổi hoa thơm)",
        "mid": "4bb5bf2b-9a7d-4702-9a0a-93b5bdbd1551",
        "fixed": True,
        "note": "✓ ĐÃ SỬA: POV bàn tay nữ thanh mảnh của Mia cầm cuộn dây bạc shekel đổi hương liệu núi; loại bỏ tay thô ráp của đàn ông.",
        "dialogue": 'Mia: "No minted coins here in 570 BC... just little curls of silver wire called shekels, weighed by hand to trade for rare mountain spices."'
    },
    {
        "idx": 11,
        "title": "Ascending Royal Terraces (Leo thang đá lên tầng cấm của hoàng gia)",
        "mid": "cda9d05d-0621-44bf-831a-adf141be21c0",
        "fixed": False,
        "note": "",
        "dialogue": 'Mia: "We are climbing into the private royal terraces... commoners definitely are not allowed up here."'
    },
    {
        "idx": 12,
        "title": "Reveal #1: Imperial Guards (Quay gáy 180 độ: Duy nhất 1 Mia nấp nhìn lính ngự lâm)",
        "mid": "9bbe453b-64c6-42a0-9279-030c58cece38",
        "fixed": True,
        "note": "✓ ĐÃ SỬA: Đã sửa lỗi nhân bản 2 cô gái. Khung hình chỉ có DUY NHẤT 1 nhân vật nữ Mia nấp sau cột đá nhìn 2 lính tuần.",
        "dialogue": 'Mia: "Look at this grand terrace... an explosion of royal flowers! But wait... armed imperial guards are patrolling right ahead!"'
    },
    {
        "idx": 13,
        "title": "Hidden in Flowers (Nấp sau giàn hoa giấy tím, lính tuần qua)",
        "mid": "8a81ef0f-fee4-4572-9c45-7a68dbff2813",
        "fixed": False,
        "note": "",
        "dialogue": 'Mia: "Shh... bronze spears and heavy leather shields... do not look this way, please do not turn around..."'
    },
    {
        "idx": 14,
        "title": "Royal Procession (Đoàn ngự giá hoàng gia đi qua & bị lính phát hiện)",
        "mid": "9e3ff0a8-8f5a-457c-acc8-4a72cff9187c",
        "fixed": False,
        "note": "",
        "dialogue": 'Mia: "Wait... someone in embroidered silk... is that Queen Amytis?! Oh no, they saw me! Run!"'
    },
    {
        "idx": 15,
        "title": "Chase Behind Waterfall (Rượt đuổi nghẹt thở sau màn thác nước cổ)",
        "mid": "8d811b69-f8e8-4a44-8e65-ed5aebc17e0c",
        "fixed": True,
        "note": "✓ ĐÃ SỬA: Mia chạy trốn sau màn thác nước với 2 TAY HOÀN TOÀN TỰ DO; không còn cầm đèn lồng vô lý.",
        "dialogue": 'Mia: "Running for my life behind a 2,500-year-old waterfall... completely terrifying but insane!"'
    },
    {
        "idx": 16,
        "title": "The Upper Nursery (Chốt then cửa gỗ thoát hiểm vào vườn ươm trên cao)",
        "mid": "525d91d1-0cae-4269-91f3-c205a140d5d9",
        "fixed": True,
        "note": "✓ ĐÃ SỬA: Đã sửa lỗi gen; Mia kéo chốt then cửa gỗ tuyết tùng vào vườn ươm, dựa tường thở phào, 2 tay tự do.",
        "dialogue": 'Mia: "Okay... we lost them. The guards just thundered down toward the lower barracks. We are safe in the upper nursery."'
    },
    {
        "idx": 17,
        "title": "The Kind Gardener (Gặp ông lão làm vườn hiền lành chỉ đường lên đỉnh)",
        "mid": "484b0477-4504-4bce-aa7c-8aa4d4bf53a7",
        "fixed": False,
        "note": "",
        "dialogue": 'Mia: "He did not shout. He just smiled, offered me water, and pointed toward the summit stairs."'
    },
    {
        "idx": 18,
        "title": "Reveal #2: Sky Oasis (Tầng thác nước ngoạn mục & hồ ngọc bích lơ lửng giữa trời)",
        "mid": "f140dbb3-2f8c-4aa1-843c-3ff4c07159b2",
        "fixed": False,
        "note": "",
        "dialogue": 'Mia: "Oh... my... god. Are you seeing this?! An emerald oasis suspended four stories directly in the open sky!"'
    },
    {
        "idx": 19,
        "title": "Lebanese Cedar Giant (Gốc cây tuyết tùng Lebanon khổng lồ bén rễ trên mái tháp)",
        "mid": "d1d9b2b8-148f-4f3b-99f4-fb8a643c8be5",
        "fixed": False,
        "note": "",
        "dialogue": 'Mia: "A full Lebanese cedar tree... growing out of a rooftop balcony. How did they even keep these roots alive?!"'
    },
    {
        "idx": 20,
        "title": "Myth Busted: Overhanging (Giải mã bí mật: Vườn nhô ra trên không chứ không treo)",
        "mid": "d80029a7-063a-48a9-ac8c-b2aa8eb06a98",
        "fixed": True,
        "note": "✓ ĐÃ SỬA: Góc máy vlog siêu rộng 0.5x hướng về Mia; 2 tay hoàn toàn tự do, không cầm điện thoại bên tay phải.",
        "dialogue": 'Mia: "Historical myth busted: the gardens were not \'hanging\' on ropes! The Greek term \'kremastos\' means \'overhanging\' - just like these dramatic terraces jutting out over the city!"'
    },
    {
        "idx": 21,
        "title": "Summit Spring Water (POV xúc giác: Vốc dòng nước nguồn mát lạnh đỉnh tháp)",
        "mid": "809e102e-4725-4f27-afcb-86dec6e7f66a",
        "fixed": False,
        "note": "",
        "dialogue": 'Mia: "Ice cold mountain water at the very summit! In the middle of the blazing Mesopotamian desert!"'
    },
    {
        "idx": 22,
        "title": "Reveal #3: Crown of Ancient World (Toàn cảnh đỉnh: Cổng Ishtar xanh biếc & Ziggurat 90m)",
        "mid": "2fa4e853-47ac-4f08-81b8-daa1292be483",
        "fixed": False,
        "note": "",
        "dialogue": 'Mia: "There it is: the golden Euphrates, the legendary blue Ishtar Gate, and the 90-meter Etemenanki ziggurat... ancient Babylon in all its glory."'
    },
    {
        "idx": 23,
        "title": "Stone Balustrade Sign-off #2 (Gác máy thành đá: Hoàng hôn tím vàng & lời tạm biệt)",
        "mid": "6ea6314d-fbc7-4ec7-8ef5-38f6e40154ee",
        "fixed": True,
        "note": "✓ ĐÃ SỬA: Máy quay gác tĩnh trên lan can đá đối diện; Mia ngồi thư thái hai tay thả lỏng tự nhiên, không cầm điện thoại selfie.",
        "dialogue": 'Mia: "A wonder built entirely out of love for a queen who longed for home. Ancient Babylon in 570 BC is unforgettable. Where should we travel next?"'
    }
]

md_lines = [
    "# Review Board: 23 Khung Ảnh Đầu Đã Sửa Lỗi & Tẩy Logo (Clean Start Frames)",
    "> **Dự án**: Time Travel Vlog — Ancient Babylon (570 BC)  ",
    "> **Project ID**: `ac50c619-1b31-4847-95d6-5379d02554c7`  ",
    "> **Video ID**: `dc2afa55-8a7f-42c3-bf8c-a13f580b6830`  ",
    "> **Trang Phục Đồng Bộ Toàn Phim**: Entity `Mia Outfit` (`media_id: 9a988664-2828-4ae2-a1a8-e7f5812d3631`)  ",
    "> **Interactive Review Board Trực Tuyến**: [http://localhost:8200/review_images.html](http://localhost:8200/review_images.html)  ",
    "> **File HTML Cục Bộ**: [review_images.html](file:///C:/flowkit/output/time_travel_vlog_ancient_babylon_570_bc/review_images.html)  ",
    "",
    "---",
    "",
    "## 👗 Khóa Trang Phục Đồng Bộ Cho Mia (Locked Outfit Reference)",
    "Để đảm bảo Mia mặc cùng 1 bộ trang phục linen xếp nếp cổ đại Babylon viền chỉ vàng thắt lưng đồng xuyên suốt tất cả 23 cảnh:",
    "- **Entity Name**: `Mia Outfit`",
    "- **Locked Media ID**: `9a988664-2828-4ae2-a1a8-e7f5812d3631`",
    f"![Mia Outfit Reference](C:/Users/Administrator/.gemini/antigravity-ide/brain/e22150ce-4262-4e3c-8619-a7731a7f7c3a/mia_outfit_ref_1790324365310.jpg)",
    "",
    "---",
    "",
    "## 🎬 Chi Tiết 23 Khung Ảnh Đầu Đã Cập Nhật (Đặc Biệt 8 Cảnh Vừa Sửa Lỗi)",
    ""
]

for s in scenes_info:
    badge = " [✓ ĐÃ SỬA THEO YÊU CẦU]" if s['fixed'] else ""
    md_lines.append(f"### Cảnh {s['idx']:02d} — {s['title']}{badge}")
    md_lines.append(f"- **Clean Media ID**: `{s['mid']}`")
    if s['note']:
        md_lines.append(f"- **Chi tiết sửa lỗi**: {s['note']}")
    md_lines.append(f"- **Thoại**: *{s['dialogue']}*")
    md_lines.append("")
    md_lines.append(f"![Cảnh {s['idx']:02d}: {s['title']}](C:/Users/Administrator/.gemini/antigravity-ide/brain/e22150ce-4262-4e3c-8619-a7731a7f7c3a/images/scene_{s['idx']:02d}.jpg)")
    md_lines.append("")
    md_lines.append("---")
    md_lines.append("")

with open(artifact_path, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

print(f"Updated gallery artifact at: {artifact_path}")
