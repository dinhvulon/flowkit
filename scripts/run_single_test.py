import urllib.request, json, time, os, subprocess

project_id = '6224591f-b884-42f2-8f57-613bc86d66fb'
scene_id = '5fc05aeb-c42e-4721-828f-7dcd560a9104'

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
        '3904fece-f12e-47ef-9018-361f1a74f315', # Mia face
        '894e8d96-d6b1-4070-ba81-d358341ec5a4'  # Scene 01 start frame
    ],
    'prompt': prompt,
    'model_family': 'omni_flash',
    'duration_s': 10,
    'aspect_ratio': 'VIDEO_ASPECT_RATIO_LANDSCAPE',
    'resolution': '720p',
    'voice_id': 'achernar' # <--- Slot 7 Native Voice ID
}

print("1. Submitting generation request with abra_r2v_10s + Pinhole Ingredients + Slot 7 Voice ID ('achernar')...", flush=True)
req = urllib.request.Request(
    'http://127.0.0.1:8100/api/flow/generate-video-refs',
    data=json.dumps(payload).encode('utf-8'),
    headers={'Content-Type': 'application/json'}
)

with urllib.request.urlopen(req, timeout=30) as resp:
    res = json.loads(resp.read())
    op_name = res['operations'][0]['operation']['name']
    print(f"Submitted successfully! Operation ID: {op_name}", flush=True)

print(f"2. Polling operation {op_name}...", flush=True)
poll_payload = {
    'project_id': project_id,
    'operations': [{'operation': {'name': op_name}}]
}
headers = {'Content-Type': 'application/json'}

video_media_id = None
video_url = None

for i in range(25):
    time.sleep(3)
    p_req = urllib.request.Request('http://127.0.0.1:8100/api/flow/check-status', data=json.dumps(poll_payload).encode('utf-8'), headers=headers)
    p_resp = json.loads(urllib.request.urlopen(p_req).read())
    op = p_resp['operations'][0]
    st = op.get('status')
    meta = op.get('operation', {}).get('metadata', {})
    mid = meta.get('video', {}).get('mediaId')
    print(f"  Poll {i+1}: status={st} | mediaId={mid}", flush=True)
    if st == 'MEDIA_GENERATION_STATUS_SUCCESSFUL':
        video_media_id = mid
        video_url = meta.get('fifeUrl')
        break

if not video_media_id:
    print("Generation timed out or failed.", flush=True)
    exit(1)

# If fifeUrl is not directly in metadata, fetch via /api/flow/media/{media_id}
if not video_url:
    print(f"Fetching video URL for mediaId {video_media_id}...", flush=True)
    m_req = urllib.request.Request(f'http://127.0.0.1:8100/api/flow/media/{video_media_id}')
    m_resp = json.loads(urllib.request.urlopen(m_req).read())
    video_url = m_resp.get('video', {}).get('fifeUrl')

print(f"Video URL obtained: {video_url}", flush=True)

dest = os.path.abspath('output/time_travel_vlog_hanging_gardens_of_babylon_570_bc/scenes/test_slot7_achernar_10s.mp4')
print(f"3. Downloading to {dest}...", flush=True)
h = {'User-Agent': 'Mozilla/5.0'}
dl_req = urllib.request.Request(video_url, headers=h)
with urllib.request.urlopen(dl_req, timeout=40) as d_resp:
    data = d_resp.read()
    with open(dest, 'wb') as f:
        f.write(data)

size_mb = len(data) / (1024 * 1024)
print(f"SUCCESS! Downloaded {dest} ({size_mb:.2f} MB)", flush=True)

# Copy to artifact folder
artifact_dest = r'C:\Users\Administrator\.gemini\antigravity-ide\brain\e22150ce-4262-4e3c-8619-a7731a7f7c3a\test_slot7_achernar_10s.mp4'
import shutil
shutil.copy2(dest, artifact_dest)
print(f"Copied to artifact: {artifact_dest}", flush=True)
