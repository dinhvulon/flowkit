import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

proj_dir = "output/time_travel_vlog_ancient_babylon_570_bc"
seo_path = os.path.join(proj_dir, "youtube_seo.json")

chapters = [
    "00:00 - The Shock Arrival (Euphrates Riverbank 570 BC)",
    "00:08 - The Legend of King Nebuchadnezzar & Queen Amytis",
    "00:16 - Euphrates River Docks & Bitumen Quffa Boats",
    "00:24 - The Massive Mechanical Chain Pump",
    "00:32 - Ancient Waterproofing: Bitumen Pitch & Reeds",
    "00:40 - Walking Beneath the Colossal Vaulted Arches",
    "00:48 - The Hanging Gardens Bazaar: Fresh Pomegranates & Figs",
    "00:56 - Tasting Fresh Figs from the Royal Terraces",
    "01:04 - Limestone Aqueducts & Cascading Streams",
    "01:12 - Trading with Ancient Silver Shekels",
    "01:20 - Sneaking Up to the Restricted Royal Sanctuaries",
    "01:28 - Imperial Guards Spotted!",
    "01:36 - Hiding Behind Bougainvillea Trellises",
    "01:44 - Royal Court Procession & Close Call",
    "01:52 - High-Speed Chase Behind the Ancient Waterfall",
    "02:00 - Catching Breath in the Upper Botanical Nursery",
    "02:08 - Meeting a Kind Babylonian Gardener",
    "02:16 - Sky Oasis: The 80-Foot Floating Paradise",
    "02:24 - Giant Lebanese Cedars Growing on the Rooftop",
    "02:32 - Myth Busted: What 'Hanging' Actually Means",
    "02:40 - Touching the Summit Spring Water",
    "02:48 - 360 Panorama: Ishtar Gate, Ziggurat & Babylon Sunset",
    "02:56 - Sunset Farewell & Time Portal Sign-off"
]

seo_data = {
    "title_options": [
        "I Time Traveled to Ancient Babylon in 570 BC! (POV Vlog)",
        "Inside the 7 Wonders: I Spent a Day in Ancient Babylon (570 BC)",
        "What Life Was REALLY Like in Ancient Babylon 2,500 Years Ago",
        "Exploring the Hanging Gardens of Babylon in 570 BC (First-Person POV)"
    ],
    "description": (
        "What would it look like to walk the streets of ancient Babylon at the very peak of the Neo-Babylonian Empire in 570 BC?\n\n"
        "In this photorealistic cinematic time-travel vlog, Mia journeys 2,500 years back in time under the reign of King Nebuchadnezzar II. "
        "From dodging ox-carts on the dusty Euphrates riverbank to tasting freshly harvested figs in the shaded vaults of the Hanging Gardens, "
        "discover the mind-blowing engineering, hydraulic chain pumps, and royal terraces of the Second Wonder of the Ancient World.\n\n"
        "TIMESTAMPS / CHAPTERS:\n" + "\n".join(chapters) + "\n\n"
        "AI DISCLOSURE:\n"
        "Visuals in this video are rendered using next-generation generative AI simulation (Google Veo / Flow), "
        "reconstructed faithfully from archaeological excavations, cuneiform tablets, and historical Mesopotamian research.\n\n"
        "#babylon #timetravel #hanginggardens #historyvlog #ancienthistory #archaeology #mesopotamia #nebuchadnezzar"
    ),
    "tags": [
        "ancient babylon", "hanging gardens of babylon", "time travel vlog", "babylon 570 bc",
        "mesopotamia", "nebuchadnezzar", "ancient history", "7 wonders of the ancient world",
        "ishtar gate", "etemenanki ziggurat", "euphrates river", "ancient engineering",
        "history documentary", "pov vlog", "veo 3", "google flow"
    ],
    "category_id": "27", # Education / Travel
    "default_language": "en"
}

with open(seo_path, "w", encoding="utf-8") as f:
    json.dump(seo_data, f, indent=2, ensure_ascii=False)

print(f"Generated YouTube SEO metadata: {seo_path}")
