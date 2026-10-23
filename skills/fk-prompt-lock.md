---
name: fk-prompt-lock
description: "Lock và chuẩn hóa video prompt FlowKit theo kiến trúc Structured JSON của phim điện ảnh ngôi thứ ba (/fk-film). Bắt buộc kiểm tra qua tools/lint_prompt.py trước khi lưu DB hoặc gửi gen video cho cả Antigravity (agy) và Claude."
---

# 🔒 fk-prompt-lock — Structured JSON Video Prompt Architecture & Linter Gate (Narrative Film)

> **BẮT BUỘC CHO MỌI AGENT (Antigravity `agy` & Claude `claude`):**
> Khi viết hoặc sửa đổi `video_prompt` cho bất kỳ cảnh nào trong FlowKit (`POST /api/scenes`, `PATCH /api/scenes`, hoặc submit batch sinh video), **TUYỆT ĐỐI KHÔNG VIẾT CHUỖI TEXT TỰ DO LỘN XỘN**.
> Bắt buộc viết prompt theo đúng **Kiến Trúc Structured JSON của Phim Điện Ảnh Ngôi Thứ Ba (`/fk-film`)** dưới đây và **chạy qua bộ kiểm tra `python tools/lint_prompt.py` đạt `errors=0` trước khi lưu vào DB hoặc gửi sinh**.

---

## 1. Tại Sao Bắt Buộc Dùng Prompt Cấu Trúc JSON?

1. **Cơ chế Text Encoder của AI Video (Omni Flash R2V `abra_r2v`)**:
   - Khi viết văn bản xuôi dài dòng (unstructured text), model dễ bị **Attention Decay** (bỏ qua các câu lệnh cuối), **Token Drift & Hallucination** (nhân đôi nhân vật, trộn trục 180° giữa các panel Storyboard, biến dạng trang phục hoặc đạo cụ).
2. **Cấu trúc JSON phân cấp (Hierarchical Conditioning)**:
   - Tách biệt rõ ràng các phân vùng nhận thức của AI: `clip_id`, `refs`, `start_frame`, `storyboard`, `camera`, `style`, `setting`, `characters`, `timeline_action`, `speech`, `post_vo`, `dramatic_craft`, `props_lock`, `audio`, `negative_constraints`.

---

## 2. Chuẩn JSON Schema Bắt Buộc Cho Phim Điện Ảnh (`/fk-film`)

Mỗi `video_prompt` phải là một đối tượng JSON hợp lệ chứa đầy đủ các trường sau (xem chi tiết tại [`skills/fk-film/references/prompt-lock.md`](fk-film/references/prompt-lock.md)):

```json
{
  "clip_id": "SC-01",
  "scene_name": "Galleon Entering the Fog Bank",
  "duration": 10,
  "aspect_ratio": "16:9",
  "refs": ["Nora", "Nora Body", "Castor", "Castor Body", "Galleon Deck", "SC-01 Storyboard"],
  "start_frame": {
    "type": "STORYBOARD",
    "source": "SC-01 Storyboard"
  },
  "storyboard": {
    "grid": "2x2",
    "description": "TIME STORYBOARD (CRITICAL): {{media:<uuid>|SC-01 Storyboard.jpg}} is a STORYBOARD OF FOUR MOMENTS IN TIME (Panel 1 Top-Left 0-3s, Panel 2 Top-Right 3-7s, Panel 3 Bottom-Left 7-10s, Panel 4 Bottom-Right end state), NOT a single frame."
  },
  "camera": {
    "viewpoint": "third-person cinematic camera; the camera itself is never seen",
    "shot_size": "OPENING SHOT (second 0): matching the top-left panel (Panel 1) of {{media:<uuid>|SC-01 Storyboard.jpg}} — Extreme Wide Shot (EWS) -> Hard Cut to Medium Shot (MS)",
    "description": "35mm Panavision anamorphic lens, deep focus f/8. At second 3.0, a crisp hard cut matching Panel 2. At second 7.0, a crisp hard cut matching Panel 3."
  },
  "style": "35mm film, cinematic documentary realism, Panavision anamorphic lens, natural organic lighting, subtle film grain, deep focus f/8, photorealistic, tactile textures",
  "setting": "Location: weathered wooden galleon deck matching {{media:<uuid>|Galleon Deck.jpg}} in dense cold grey sea-fog. SPATIAL LOCK: All characters stand firmly INSIDE the vessel on the solid wooden deck planks, NEVER on the exterior ocean side of the railing.",
  "characters": [
    {
      "name": "Nora",
      "visual_lock": "FACE LOCK: Nora's face and hair are an exact 1:1 match to {{media:<uuid>|Nora.jpg}}. BODY AND OUTFIT LOCK: Her build and seafarer costume match {{media:<uuid>|Nora Body.jpg}} with zero outfit variations.",
      "state": "standing at the bow rail, salt spray on her oiled-leather corslet, gaze sharp and resolute"
    }
  ],
  "timeline_action": {
    "0-3s": "Matching Panel 1 (Top-Left) of {{media:<uuid>|SC-01 Storyboard.jpg}}: Extreme wide shot of the weathered wooden galleon slicing through rolling grey sea-fog.",
    "3-7s": "At second 3.0, a crisp hard cut matching Panel 2 (Top-Right): Medium shot of Nora at the bow rail; strictly Nora alone in this shot while Castor is completely off-screen. From the start of the shot, Nora speaks in a firm voice: Nora says (commanding, resolute): \"Drop the mainsail to half! Keep every eye on the fog!\"",
    "7-10s": "At second 7.0, a crisp hard cut matching Panel 3 (Bottom-Left): Medium close-up of Castor gripping the hemp shroud rope on the main deck; strictly Castor alone in this shot while Nora is completely off-screen. Castor says (gritty, urgent): \"Soundings drop fast, Captain! Reefs dead ahead!\""
  },
  "speech": {
    "speaker": ["Nora", "Castor"],
    "voices": {"Nora": "kore", "Castor": "alnilam"},
    "delivery": "firm, urgent seafarer command voices cutting clearly through the ocean wind, lip-synced",
    "dialogue": [
      {"t": "3-7s", "speaker": "Nora", "line": "Drop the mainsail to half! Keep every eye on the fog!"},
      {"t": "7-10s", "speaker": "Castor", "line": "Soundings drop fast, Captain! Reefs dead ahead!"}
    ]
  },
  "post_vo": null,
  "dramatic_craft": {
    "beat": "Commanding caution / warning of imminent reef hazard",
    "value_turn": "+ to - (controlled navigation to sudden navigational peril)",
    "subtext": "Both know these uncharted waters match the cursed coordinates of the Golden Tree.",
    "prop_and_detail": "Taut wet hemp shroud rope vibrating under wind tension"
  },
  "props_lock": "Strictly ONE single continuous wooden railing along the starboard side; taut wet hemp shroud ropes.",
  "audio": "Clear lip-synced dialogue from Nora (kore) and Castor (alnilam) on top; heavy creaking oak hull timbers, snapping canvas sails, and low ocean swell underneath.",
  "negative_constraints": [
    "No subtitles, no captions, no on-frame text, no logos, no watermarks.",
    "The video is full-frame shots only: never a 2x2 grid, never panels, never split screen, never black dividing lines.",
    "Crisp hard cuts at second 3.0 and second 7.0; no camera blending, no crossfades, no 180-degree axis fusion.",
    "Strictly NO duplicate characters, NO multiple Nora, NO multiple Castor, NO cloning; Nora is strictly alone in 3-7s and Castor is strictly alone in 7-10s.",
    "All characters stand firmly INSIDE the wooden deck, NEVER standing on the ocean water outside the hull.",
    "Strictly NO CGI, NO plastic skin, NO 3D render sheen, NO breath smoke, NO white steam plumes, NO volumetric god rays, NO shallow bokeh."
  ]
}
```

---

## 3. Các Quy Tắc Khóa Cứng Trong Prompt Phim Điện Ảnh (Core Film Locks)

1. **Góc máy ngôi thứ ba thuần túy (`Third-Person Cinematic Camera`):**
   - `camera.viewpoint` luôn là `"third-person cinematic camera; the camera itself is never seen"`. Không có thiết bị quay trong khung hình, không ai nhìn thẳng vào ống kính như vlog.
2. **Storyboard 2×2 Crisp Hard Cuts, Chống Phân Thân & Chống Đảo Trục 180° (Rule 69, Rule 74):**
   - Khi các panel trên Storyboard 2×2 khác góc máy hoặc nhân vật, bắt buộc dùng `crisp hard cut` tại đúng mốc giây (góc máy giữa 2 panel cắt cảnh phải lệch nhau `> 45°–90°`, cấm cắt giữa 2 panel trùng góc nhìn dọc cùng 1 lan can gây nhân đôi lan can).
   - Khi một Shot chỉ có 1 nhân vật, bắt buộc ghi `Strictly [Character A] alone in this shot; [Character B] is completely off-screen and never seen` kèm khóa chống phân thân trong `negative_constraints`.
   - Khi nhân vật trên cao chỉ tay phát hiện mục tiêu ở xa (thuyền/sinh vật/đảo), cú máy chỉ tay (`0-2s`/`0-3s`) chỉ quay người chỉ tay trên boong về phía ngoài khung hình (`off-screen target`), sau đó Hard Cut mới lộ mục tiêu. Nhân vật sợ hãi giữ khuôn mặt lộ rõ 100% (`NO hands covering face or cheeks`).
3. **Khóa Nhận Diện 1:1, Trang Phục Thuần Ref & Đồng Bộ Kích Thước Đạo Cụ/Sinh Vật (Rule 46, 60, 64, 74 (4)):**
   - Nhắc mọi ref bằng chip `{{ref:<Tên>}}` / `{{media:<uuid>|<name>}}`. Không tả lại ngũ quan hay quần áo bằng chữ dài dòng.
   - Sinh vật/đạo cụ có ảnh ref (như `Omen Fish`) phải đính vào `refs` ở mọi cảnh có mặt và khóa cứng kích thước/trọng lượng vật lý tuyệt đối (`1.7m–1.9m, 80 kg`).
4. **Chất Liệu Sinh Học Thực Tế, Cấm Khói Thở Trắng & Deep Focus `f/8` (Rule 57, 62):**
   - Khóa `deep focus f/8`, cấm xóa phông bokeh, cấm khói thở trắng (`strictly NO breath smoke, NO white steam plumes`), cấm `volumetric god rays`, cấm CGI.
5. **Chuẩn Số Từ Thoại Rule 49 & Đa Giọng Nói Pinhole (`voice-bible.md`):**
   - `4s`: 0 hoặc 6–8 từ; `6s`: 12–15 từ; `8s`: 18–22 từ; `10s`: 24–28 từ.
   - Mỗi người nói có một Voice ID riêng trong `speech.voices`. Trong vùng nguy hiểm hoặc khi tranh cãi, ngữ điệu phải nhanh, lớn, gắt, dứt khoát.

---

## 4. Cổng Kiểm Tra Linter Bắt Buộc (`tools/lint_prompt.py`)

Trước khi lưu prompt vào database hoặc gửi batch request tới FlowKit, bắt buộc chạy:

```bash
python tools/lint_prompt.py output/<slug>/prompts_act1.json
# Hoặc kiểm tra trực tiếp một Scene đã lưu trong DB:
python tools/lint_prompt.py --scene <scene_id>
```

**Tiêu chuẩn thông qua:** `errors=0` (`0 CRITICAL`, `0 HIGH`). Nếu có bất kỳ lỗi nào, phải sửa ngay trước khi gửi sinh.
