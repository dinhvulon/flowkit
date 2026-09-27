import json
import urllib.request
import sys
sys.path.append('c:/flowkit')
from agent.services import flow_batch as fb

# S00 details:
# media_id = d78e4811-f44c-4789-a33f-aeea9da11172
# op_id = 22037bb6-a593-4fec-b6bb-19565dadc9b2
# project_id = aae54cfc-ea42-4c63-8f9d-440b0b9ddd86

media_id = "d78e4811-f44c-4789-a33f-aeea9da11172"
op_id = "22037bb6-a593-4fec-b6bb-19565dadc9b2"
project_id = "aae54cfc-ea42-4c63-8f9d-440b0b9ddd86"

item = [None] * 32
item[0] = [None, media_id]
item[2] = 2
item[4] = [None, op_id, None, None, fb._client_uuid()]
item[6] = 2
item[31] = "veo_3_1_upsampler_1080p"

envelope = fb.build_envelope(fb.RPC_UPSCALE_VIDEO, [
    [item],
    fb._context(project_id),
    [fb._client_uuid()]
])

print("Envelope created successfully.")
print(envelope[:300])
