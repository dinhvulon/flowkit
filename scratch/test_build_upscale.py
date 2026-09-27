import json
import uuid
import sys
sys.path.append('c:/flowkit')

from agent.services import flow_batch as fb

def build_test_upscale_req(media_id, project_id, aspect=fb.VIDEO_ASPECT_LANDSCAPE):
    op_id = "dd5c57a1-9a6a-4624-8f1d-cf0c3918e32a"
    client_uuid1 = "94788D86-C7D2-4C9C-B2E1-FA3BBD99B4A9"
    client_uuid2 = "8D5A4E7F-4373-44DD-A734-D911A9C60831"
    
    aspect_val = 2 if aspect in (fb.VIDEO_ASPECT_LANDSCAPE, "HORIZONTAL", "VIDEO_ASPECT_RATIO_LANDSCAPE", 2) else 1
    
    # 32 slots:
    item = [None] * 32
    item[0] = [None, op_id]
    item[2] = aspect_val
    item[4] = [None, media_id, None, None, client_uuid1]
    item[6] = 2
    item[31] = "veo_3_1_upsampler_1080p"
    
    envelope = fb.build_envelope("p0UkFb", [
        [item],
        fb._context(project_id),
        [client_uuid2]
    ])
    return envelope

env = build_test_upscale_req("26d8b4c7-449c-4e30-834b-f4e7f3fd4e72", "aae54cfc-ea42-4c63-8f9d-440b0b9ddd86")
print("Constructed envelope:")
print(env[:300])

parsed = fb.parse_envelope(f")]}}'\\n\\n123\\n{env}\\n")
print("\nParsed ok! Number of results:", len(parsed))
