# Template prompt

Đọc ở **Bước 2** (CHARACTER_LOCK) và **Bước 5** (Clip JSON) của `SKILL.md`. Câu chữ cuối cùng trong `video_prompt` phải theo khung 9 khối của `prompt-lock.md`; file này chỉ là bản thiết kế.

Quy ước chung (Bài học 23, 33, CLAUDE.md Rule 30):
- Không có chữ `phone`, `smartphone`, `camera` (đạo cụ), `selfie stick`, `device`, `screen`, `gimbal` — kể cả câu phủ định.
- Ràng buộc viết thành câu khẳng định trong trường `constraints`, không có trường/dòng `Negative:`.
- Tên vlogger (`Nora` trong mẫu) trùng tuyệt đối giữa `CHARACTER_LOCK`, entity và lời thoại.

## Character Bible (mẫu — thay giá trị, sau đó KHÔNG sửa giữa các clip)
```
CHARACTER_LOCK:
Nora, a 26-year-old Western woman with a heart-shaped face, hazel-green eyes, dense freckles across nose and cheeks,
bright copper-red hair in a high bun held by a dark wooden hairpin, a few loose strands at the temples,
wearing an era-appropriate [dark indigo cross-collar hemp robe with a white inner collar and a plain dark sash].
Voice: Laomedeia — upbeat, mid-high pitched, energetic expressive conversational female voice, fast confident vlog delivery with dry humor, rises into real cracking screams when in danger, drops to a fast whisper when hiding.
```

## Clip JSON (bản thiết kế 1 clip 8s, R2V Omni Flash)
```json
{
  "clip_id": "CH2-05",
  "duration": 8,
  "aspect_ratio": "16:9",
  "refs": ["Nora", "Nora Body", "Xianyang Market"],
  "camera": "The lens sits at the end of Nora's outstretched right arm, completely outside the visible frame and never seen; her right arm stays extended toward the lens for the entire clip. Only her left hand is free.",
  "style": "handheld vlog footage, natural wide-angle handheld perspective, no exaggerated fisheye distortion, natural daylight, subtle hand shake, photorealistic, documentary realism",
  "setting": "Xianyang market street, Qin dynasty China, 211 BC: rammed-earth walls, dark timber stalls with grey tile roofs, dirt road, midday light",
  "in_place": "Merchants in plain hemp robes stand at the stalls on both sides; two laborers carrying one large wooden log wait at the far left edge of the street; soldiers in lamellar armor stand at the far end. Everyone stays in that same spot until they move; nobody appears suddenly or vanishes.",
  "shot": "ultra-wide selfie at arm's length, face on the left third, deep market street behind her",
  "action": "0-3s she walks backward glancing over her shoulder; 3-6s she leans in and speaks in a hushed voice; 6-8s she swings her outstretched arm to the right, the street blurs into a fast whip pan",
  "dialogue": [
    {"t": "0-3s", "speaker": "Nora", "delivery": "hushed, nervous half-laugh", "line": "Okay, don't freak out, but everyone here"},
    {"t": "3-6s", "speaker": "Nora", "delivery": "hushed", "line": "is staring at my bright red hair."},
    {"t": "6-8s", "speaker": "Nora", "delivery": "dry", "line": "And honestly, I'd stare too."}
  ],
  "background_people": "merchants pause and stare at her with suspicion; their lips stay closed",
  "audio": "market chatter in ancient Chinese, clattering wooden carts, distant bronze bell",
  "transition_in": "opens mid whip pan with heavy motion blur moving right, settling on the market street",
  "transition_out": "swing: her arm whips the view right, heavy motion blur fills the frame in the final second",
  "join": "CUT — cắt ở khung nhòe nhất; CH2-06 mở giữa cú lia sang phải",
  "physics": "selfie at arm's length facing her, walking backward at walking pace; frame 0: Nora mid-market, stalls both sides; laborers walk left to right behind her at walking pace",
  "constraints": "Nora stays in frame for the whole clip and never disappears. The locals wear plain Qin-era hemp clothing; everything around is 211 BC China, with no modern buildings or vehicles. Only Nora speaks English; nobody speaks over anyone else. No subtitles or text appear on screen. This looks like real footage, not a movie or a 3D render."
}
```
Thoại 18–22 từ / clip 8s, chia 6–7 / 7–8 / 5–7 từ theo sub-clip (Rule 49). Mẫu trên = 7 + 7 + 5 = 19 từ.

## Clip nhân vật phụ nói (ngôn ngữ không hiểu được)
- Sub-clip riêng cho người nói: `3-5s: The Leader speaks in a deep, gravelly male voice — short guttural non-English sounds, no recognizable words; Nora stays silent and watches him.`
- Vlogger phản ứng với giọng điệu ở sub-clip sau, không dịch nội dung (`character-bible.md` mục 4).
- Người bản địa hiện mặt mà không có thoại → khóa miệng: `"<Local>'s lips stay closed for the entire clip. The only moving mouth in the frame is Nora's."` (Bài học 49).

## Clip POV mắt nhân vật
- `camera`: `"The view is Nora's own eyes; all recording gear is completely outside the visible frame, and her hands stay out of frame for the whole clip."`
- Chỉ khi sub-clip thật sự có thao tác tay: `"her own hands enter the lower frame [scooping millet / touching bronze armor]"` (Bài học 50). Không thấy mặt; thoại của Nora là giọng ngoài khung.

## Clip máy dựng cố định
- `camera`: `"Static footage from a fixed viewpoint resting on <vật cụ thể>; the frame does not move; nobody touches the viewpoint. Both of Nora's hands are free."` — dùng cho cảnh ăn, cảnh kết, và mọi hành động cần hai tay (Bài học 50).

## Clip toàn cảnh hoành tráng
- `camera`: `"The view is Nora's own eyes from where she stands on a high earthen ridge, slow handheld pan over [thousands of soldiers / the pits]; she never appears in the frame."` — không drone, vẫn có rung tay.

## Ảnh khung đầu — chỉ cho shot không có nhân vật
Clip có vlogger **không dùng ảnh start frame** (R2V Ingredients, CLAUDE.md Rule 27). Chỉ shot không người (vũ trụ, drone theo yêu cầu, phong cảnh) mới được tạo ảnh khung đầu, và phải qua quy trình 4 bước xóa logo → upload lại (Rule 28) trước khi đưa vào sinh video.
