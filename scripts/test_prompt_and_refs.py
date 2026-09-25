import sys
sys.path.insert(0, ".")
import asyncio
import json
from agent.db import crud
from agent.sdk.services.operations import _build_video_prompt, _r2v_duration

async def main():
    video_id = "71909a60-29f7-460e-807c-ed48b8a12ad1"
    project_id = "6224591f-b884-42f2-8f57-613bc86d66fb"
    scenes = await crud.list_scenes(video_id)
    scene = scenes[0]
    
    prompt = await _build_video_prompt(scene.get("video_prompt"), scene, project_id)
    print("--- Video Prompt for Scene 1 ---")
    print(prompt)
    print("\n--- Duration ---")
    print(_r2v_duration(scene.get("duration")))

    # Test ref resolution
    prefix = "horizontal"
    char_names_raw = scene.get("character_names")
    if isinstance(char_names_raw, str):
        char_names_raw = json.loads(char_names_raw)
    
    project_entities = await crud.get_project_characters(project_id)
    from agent.sdk.services.operations import _char_matches
    
    ref_ids = []
    seen = set()
    # 1. Character
    for c in project_entities:
        if _char_matches(c, set(char_names_raw)) and c.get("entity_type") == "character":
            mid = c.get("media_id")
            if mid and mid not in seen:
                ref_ids.append(mid)
                seen.add(mid)
    # 2. Scene start frame
    start_id = scene.get(f"{prefix}_image_media_id")
    if start_id and start_id not in seen:
        ref_ids.append(start_id)
        seen.add(start_id)

    print("\n--- References (Pinhole Ingredients) for Scene 1 ---")
    print(f"Total refs: {len(ref_ids)}")
    for i, r in enumerate(ref_ids):
        print(f"Ref {i+1}: {r}")

asyncio.run(main())
