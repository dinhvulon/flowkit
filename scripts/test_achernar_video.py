import urllib.request, json, time, os

project_id = '6224591f-b884-42f2-8f57-613bc86d66fb'
scene_id = '5fc05aeb-c42e-4721-828f-7dcd560a9104' # Scene 01

prompt = (
    '0-3s: A massive wooden cart wheel rolls past inches from the lens in a heavy wipe, '
    'revealing Mia standing near the dusty Euphrates riverbank. '
    '3-6s: Mia extends her selfie stick, looks directly into the lens with wide sparkling eyes and says '
    '"You guys... welcome to Babylon, 570 BC! And right behind me is the legendary Hanging Gardens!" '
    '6-10s: She points excitedly toward the colossal green terraces as desert palm fronds sway gently in the warm breeze. '
    'Character voices: Mia: Achernar — soft, higher-pitched, natural expressive conversational female voice, casual vlog tone, breathy when amazed, hushed whisper when nervous.. '
    'Audio: no background music. Keep character dialogue and natural ambient sounds. '
    'Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.'
)

payload = {
    'project_id': project_id,
    'scene_id': scene_id,
    'reference_media_ids': [
        '3904fece-f12e-47ef-9018-361f1a74f315', # Mia character ref
        '894e8d96-d6b1-4070-ba81-d358341ec5a4'  # Scene 01 approved start frame
    ],
    'prompt': prompt,
    'model_family': 'omni_flash',
    'duration_s': 10,
    'aspect_ratio': 'VIDEO_ASPECT_RATIO_LANDSCAPE',
    'resolution': '720p'
}

print("Submitting test with full Achernar voice conditioning & dialogue...")
req = urllib.request.Request(
    'http://127.0.0.1:8100/api/flow/generate-video-refs',
    data=json.dumps(payload).encode('utf-8'),
    headers={'Content-Type': 'application/json'}
)

try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        res = json.loads(resp.read())
        print("Submit response:", json.dumps(res, indent=2))
        op_name = res['operations'][0]['operation']['name']
except Exception as e:
    print("Submit error:", e)
    exit(1)

print(f"Polling operation: {op_name}...")
poll_payload = {
    'project_id': project_id,
    'operations': [{'operation': {'name': op_name}}]
}
headers = {'Content-Type': 'application/json'}

video_url = None
for i in range(12):
    time.sleep(3)
    p_req = urllib.request.Request('http://127.0.0.1:8100/api/flow/check-status', data=json.dumps(poll_payload).encode('utf-8'), headers=headers)
    p_resp = json.loads(urllib.request.urlopen(p_req).read())
    op = p_resp['operations'][0]
    st = op.get('status')
    meta = op.get('operation', {}).get('metadata', {})
    print(f"Poll {i+1}: {st}")
    if st == 'MEDIA_GENERATION_STATUS_SUCCESSFUL':
        video_url = meta.get('fifeUrl')
        video_media_id = meta.get('video', {}).get('mediaId')
        print(f"SUCCESS! mediaId: {video_media_id}")
        print(f"URL: {video_url}")
        break

if video_url:
    dest = os.path.abspath('output/time_travel_vlog_hanging_gardens_of_babylon_570_bc/scenes/scene_01_achernar_voice_10s.mp4')
    h = {'User-Agent': 'Mozilla/5.0'}
    dl_req = urllib.request.Request(video_url, headers=h)
    with urllib.request.urlopen(dl_req, timeout=30) as d_resp:
        data = d_resp.read()
        with open(dest, 'wb') as f:
            f.write(data)
    print(f"Downloaded video to {dest} ({len(data)/(1024*1024):.2f} MB)")
