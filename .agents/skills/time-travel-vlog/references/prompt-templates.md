# Template prompt

## Character Bible (mẫu — thay giá trị, sau đó KHÔNG sửa giữa các clip)
```
CHARACTER_LOCK (ví dụ — thay giá trị, sau đó KHÔNG sửa giữa các clip):
Nora, a 26-year-old Western woman with a heart-shaped face, hazel-green eyes, dense freckles across nose and cheeks,
bright copper-red hair in a high bun held by a dark wooden hairpin, a few loose strands at the temples,
wearing an era-appropriate [dark indigo cross-collar hemp robe with a white inner collar and a plain dark sash],
holding a short black selfie stick with a smartphone on ultra-wide 0.5x lens, her arm visible at the frame edge.
Voice: warm, curious American English, breathy when amazed, whispers when scared.
```
## Clip JSON cho Veo 3.1 / Google Flow
```json
{
  "clip_id": "CH2-05",
  "duration": "8s",
  "aspect_ratio": "16:9",
  "style": "handheld smartphone selfie-stick vlog footage, ultra-wide 0.5x front camera, natural daylight, slight lens distortion, subtle hand shake, photorealistic, documentary realism",
  "character": "<dán CHARACTER_LOCK nguyên văn>",
  "setting": "Xianyang market street, Qin dynasty China, 211 BC: rammed-earth walls, dark timber stalls with grey tile roofs, dirt road, merchants in plain hemp robes, soldiers in lamellar armor at the far end",
  "shot": "ultra-wide selfie at arm's length, her extended arm visible at the right edge, face on the left third, deep market street behind her",
  "action": "0-2s she walks backward glancing over her shoulder; 2-6s leans toward the camera and speaks in a hushed voice; 6-8s two laborers carry a large wooden log right across the lens from left to right, almost filling the frame",
  "dialogue": {
    "speaker": "Mia",
    "line": "Okay, don't freak out, but everyone here is staring at my hair.",
    "delivery": "hushed, nervous half-laugh"
  },
  "background_people": "merchants pause and stare at her with suspicion, no one speaks",
  "audio": "market chatter in ancient Chinese, clattering wooden carts, distant bronze bell",
  "transition_in": "opens with a cart wheel sliding out of frame very close to the lens",
  "transition_out": "foreground wipe: log fills the frame in the final second",
  "negative": "no subtitles, no on-screen text, no modern buildings, no cars, no other modern people, no second speaker, no face change, no extra fingers"
}
```

## Clip dân bản địa nói (vlogger im lặng)
- `dialogue.speaker` = người bản địa, `line` bằng tiếng địa phương/cổ (ghi phiên âm đơn giản) hoặc English có accent nếu muốn người xem hiểu.
- Thêm vào action: "Mia listens silently, reacting with wide eyes, lips closed".

## Clip POV mắt nhân vật
- `shot`: "first-person POV from her eye level, her own hands visible in the lower frame [scooping millet / touching bronze armor]" — không thấy mặt — thoại vẫn của nhân vật (giọng off) hoặc của người bản địa trước mặt.

## Clip máy dựng cố định
- `shot`: "smartphone propped on the table facing her, static frame, she sits and eats, vendors moving behind" — dùng cho cảnh ăn và cảnh kết.

## Clip toàn cảnh hoành tráng
- `shot`: "phone held up from where she stands on a high earthen ridge, slow handheld pan over [thousands of soldiers / the pits]" — không drone, vẫn có rung tay.

## Ảnh khung đầu (nếu dùng Frames to Video)
Viết 1 câu prompt ảnh tĩnh từ `character + setting + shot` + tư thế ở giây 0; tạo bằng Imagen/Grok Imagine, giữ cùng ảnh tham chiếu mặt.
