import sqlite3
import re
import json

conn = sqlite3.connect('flow_agent.db')
VIDEO_ID = '34f6179f-4ce9-4c66-830d-0ba70d7eb76e'

scenes = conn.execute('SELECT id, display_order, video_prompt, prompt FROM scene WHERE video_id = ? ORDER BY display_order ASC', (VIDEO_ID,)).fetchall()

def sanitize_text(text: str) -> str:
    if not text:
        return text
    t = text
    # 1. Phrases with phone
    t = re.sub(r'\bnever drops(, releases, or lets go of)? the phone\b', 'never drops\\1 the camera', t, flags=re.I)
    t = re.sub(r'\braw unstabilized smartphone footage\b', 'raw unstabilized handheld footage', t, flags=re.I)
    t = re.sub(r'\bsmartphone footage\b', 'handheld camera footage', t, flags=re.I)
    t = re.sub(r'\bnatural smartphone perspective\b', 'natural wide-angle handheld perspective', t, flags=re.I)
    t = re.sub(r'\bsmartphone propped on\b', 'camera propped on', t, flags=re.I)
    t = re.sub(r'\bsmartphone\b', 'camera', t, flags=re.I)
    t = re.sub(r'\bphone\b', 'camera', t, flags=re.I)
    t = re.sub(r'\bselfie[- ]?stick\b', "arm's length", t, flags=re.I)
    
    # 2. Screen
    t = re.sub(r'\boff-screen\b', 'outside the visible frame', t, flags=re.I)
    t = re.sub(r'\bon[- ]screen\b', 'in the frame', t, flags=re.I)
    t = re.sub(r'\bappear(s)? on screen\b', 'appear\\1 in the frame', t, flags=re.I)
    t = re.sub(r'\b(phone|camera|tv) screen\b', 'display', t, flags=re.I)
    
    # 3. Device
    t = re.sub(r'\bghost devices?\b', 'unwanted objects', t, flags=re.I)
    t = re.sub(r'\bdevice\b', 'camera', t, flags=re.I)
    
    return t

updated_count = 0
for sc in scenes:
    sid, order, vp, p = sc[0], sc[1], sc[2] or '', sc[3] or ''
    new_vp = sanitize_text(vp)
    new_p = sanitize_text(p)
    if new_vp != vp or new_p != p:
        conn.execute('UPDATE scene SET video_prompt = ?, prompt = ? WHERE id = ?', (new_vp, new_p, sid))
        updated_count += 1

conn.commit()
print(f'Sanitized {updated_count} / {len(scenes)} scenes in DB!')

# Also update clips.json
try:
    with open('output/ice_age_16_000_bc_survival_vlog/clips.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    for c in data.get('clips', []):
        if 'video_prompt' in c:
            c['video_prompt'] = sanitize_text(c['video_prompt'])
        if 'prompt' in c:
            c['prompt'] = sanitize_text(c['prompt'])
    with open('output/ice_age_16_000_bc_survival_vlog/clips.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print('Sanitized clips.json cleanly!')
except Exception as e:
    print('Error updating clips.json:', e)
