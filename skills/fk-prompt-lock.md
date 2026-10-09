---
name: fk-prompt-lock
description: "Lock và chuẩn hóa video prompt FlowKit theo kiến trúc Structured JSON. Bắt buộc kiểm tra qua tools/lint_prompt.py trước khi lưu DB hoặc gửi gen video cho cả Antigravity (agy) và Claude."
---

# 🔒 fk-prompt-lock — Structured JSON Video Prompt Architecture & Linter Gate

> **BẮT BUỘC CHO MỌI AGENT (Antigravity `agy` & Claude `claude`):**
> Khi viết hoặc sửa đổi `video_prompt` cho bất kỳ cảnh nào trong FlowKit (`POST /api/scenes`, `PATCH /api/scenes`, hoặc submit batch sinh video), **TUYỆT ĐỐI KHÔNG VIẾT CHUỖI TEXT TỰ DO LỘN XỘN**.
> Bắt buộc phải viết prompt theo đúng **Kiến Trúc Structured JSON** dưới đây và **chạy qua bộ kiểm tra `python tools/lint_prompt.py` trước khi lưu vào DB hoặc gửi sinh**.

---

## 1. Tại Sao Bắt Buộc Dùng Prompt Cấu Trúc JSON?

1. **Cơ chế Text Encoder của AI Video (Veo 3 & Omni Flash R2V `abra_r2v`)**:
   - Model video dùng LLM (Gemini / T5-XXL) để mã hóa prompt trước khi đưa vào mạng Diffusion.
   - Khi viết văn bản xuôi dài dòng (unstructured text):
     - Dễ bị **Attention Decay**: Các câu lệnh quan trọng ở cuối bị model bỏ qua.
     - Dễ bị **Token Drift & Hallucination**: AI nhầm lẫn giữa mô tả người quay với bối cảnh, tự ý vẽ thêm màn hình điện thoại (Ghost Device), tự động co rút cơ thể hoặc biến dạng quần áo.
     - Dễ bị **Encoding Corruption**: Tránh hoàn toàn lỗi character encoding (như lỗi bị chèn hàng loạt ký tự gạch ngang em-dash `\u2014` làm nát token).
2. **Cấu trúc JSON phân cấp (Hierarchical Conditioning)**:
   - Tách biệt rõ ràng 6 phân vùng nhận thức của AI: `camera`, `setting`, `characters`, `timeline_action`, `speech`, `negative_constraints`.
   - Kết quả thực nghiệm Scene 27: Prompt JSON đạt điểm review AI **9.25/10**, triệt tiêu 100% lỗi biến dạng nhân vật, giữ đúng 100% nhận diện khuôn mặt và trang phục từ ảnh tham chiếu.

---

## 2. Chuẩn JSON Schema Bắt Buộc

Mỗi `video_prompt` phải là một chuỗi JSON hợp lệ chứa các trường sau:

```json
{
  "camera": {
    "type": "over-the-shoulder handheld tracking shot | first-person pov | static fixed viewpoint",
    "position": "mô tả vị trí đặt máy (ngang ngực/bụng trên, hơi hất nhẹ lên)",
    "framing": "bố cục khung hình (nhân vật chiếm 1/3 góc nào, hậu cảnh 2/3)"
  },
  "setting": {
    "location": "địa điểm và thời kỳ cụ thể (khớp 100% Setting Reference)",
    "elements": [
      "danh sách vật thể và chất liệu có sẵn từ giây 0",
      "không dùng kim loại hoặc vật dụng sai thời kỳ"
    ]
  },
  "characters": [
    {
      "name": "Nora",
      "visual_lock": "matches Nora face and Nora Body reference images exactly",
      "outfit": "wears the exact historical outfit shown in Nora Body reference sheet (NO extra fur, NO variations)",
      "action": "hành vi bao quát"
    },
    {
      "name": "Nhân vật phụ (nếu có)",
      "visual_lock": "matches [Character] reference image",
      "outfit": "mô tả trang phục đơn giản theo ref",
      "position": "vị trí cụ thể"
    }
  ],
  "timeline_action": {
    "0-3s": "Hành động mở đầu từ frame 0 + tương tác vật lý + nhân vật bắt đầu nói ngay từ giây 0 (Immediate Delivery)",
    "3-6s": "Hành động chính + thao tác bề mặt trực tiếp + đoạn thoại tiếp nối",
    "6-8s": "Thu thế / cảm xúc chốt cảnh + câu thoại kết thúc"
  },
  "speech": {
    "speaker": "Nora",
    "voice_profile": "Laomedeia conversational energetic vlog delivery",
    "dialogue": "Toàn bộ câu thoại dài từ 23 đến 25 từ (hoặc Sonic Isolation nếu đang rình săn/ẩn nấp)"
  },
  "negative_constraints": [
    "the camera lens itself and her gripping hand are completely outside the visible frame and never seen",
    "both hands are empty unless directly handling a specified prop",
    "no phone, no smartphone, no screen, no device, no selfie stick, no gimbal",
    "no 3rd-person spectator switch, pure single perspective throughout",
    "no subtitles, no text on screen, no watermark",
    "no morphing or vanishing characters"
  ]
}
```

---

## 3. Các Quy Tắc Cốt Lõi Khóa Vào Prompt (Core Locks)

### A. Khóa Góc Máy Quang Học & Tỷ Lệ Góc Máy Vàng (Rule 41, 42)
- **Tỷ lệ**: 60%–70% First-Person POV (cam sau qua mắt vlogger), 20%–30% Over-The-Shoulder / Selfie (cam trước 0.5x), 10% Máy dựng cố định.
- **CẤM 100%**:
  - Cấm lia máy xoay lật 180° giữa trước và sau trong 1 shot.
  - Cấm shot quay từ sau lưng/sau đầu rồi xoay ra trước mặt.
  - Cấm 3 cảnh selfie liên tiếp.
- **Khóa điểm mù quang học**: Thấu kính camera và tay cầm máy luôn nằm ngoài khung hình (`completely outside the visible frame and never seen`). Bàn tay tự do luôn trống (`empty hand`).

### B. Khóa Nhận Diện & Trang Phục Thuần Tham Chiếu (Rule 46, 52)
- `<Vlogger> Body` **bắt buộc là ảnh Body đã mặc hoàn chỉnh trang phục**.
- **CẤM tự mô tả lại trang phục bằng lời dài dòng**: Không tự ý bịa thêm `shearling collar`, `tunic`, `fur-lined`, v.v. Chỉ trỏ thẳng vào ảnh ref đã duyệt:
  `"wears the exact historical outfit shown in the [Character] Body reference sheet (NO shearling collar, NO extra fur, NO hood, NO outfit variations)"`.
- **CẤM tả ngực to/khe ngực khoét sâu**: Chỉ cần khóa vóc dáng và trang phục theo ảnh reference đã duyệt.

### C. Khóa Động Học Tiếp Xúc & Chống Bụi Lơ Lửng (Rule 51, 53)
- **CẤM 100% đánh đấm, giáp lá cà, vật lộn với dã thú**.
- **CẤM mô tả hứng bụi/bột rơi giữa không trung**: Mọi chất liệu (bột son, tro, đất sét) phải có sẵn trên bề mặt tảng đá/âu da từ Frame 0. Nhân vật quệt ngón tay trực tiếp vào bề mặt có sẵn đó.

### D. Khóa Thoại 23–25 Từ & Nói Ngay Từ Giây 0 (Rule 51, 54)
- **Độ dài thoại**: Chuẩn dồn dập 23–25 từ / clip 8s (không quá 26 từ) tạo cảm giác adrenaline vlog thực tế.
- **Nói ngay từ giây 0**: Trong mốc `0-3s` phải ghi rõ nhân vật bắt đầu nói ngay từ giây đầu tiên (`From the very first frame at second 0, Nora speaks immediately...`), tránh lỗi im lặng đầu clip dẫn đến bị cụt âm cuối clip.
- **Ngoại lệ Sonic Isolation**: Khi rình săn, áp sát thú dữ, ẩn nấp: miệng ngậm chặt tuyệt đối, không có lời thoại (`Strictly NO spoken dialogue. Her mouth stays firmly closed; she holds her breath in dead silence`).

---

## 4. Các Mẫu Template Chuẩn (Ready-to-Use Templates)

### Template 1: Over-the-Shoulder / Self-Vlog Interaction (20%–30% Tỷ Lệ)
Dùng khi vlogger dẫn dắt câu chuyện hoặc giao lưu với người bản địa:

```json
{
  "camera": {
    "type": "over-the-shoulder handheld tracking shot",
    "position": "chest level behind Nora's right shoulder looking toward the native craftsman",
    "framing": "Nora right foreground occupying one third, native craftsman center midground beside hearth occupying two thirds"
  },
  "setting": {
    "location": "Pech de l'Aze limestone cave hearth workspace",
    "elements": [
      "circular stone hearth with glowing red-orange oak embers",
      "dried red deer pelt pad on flat cave stone floor",
      "faceted black flint core resting on pelt pad",
      "natural cave wall in soft firelight, strictly no snow"
    ]
  },
  "characters": [
    {
      "name": "Nora",
      "visual_lock": "matches Nora face and Nora Body reference sheets exactly",
      "outfit": "wears the exact historical outfit shown in Nora Body reference sheet (NO extra fur, NO variations)",
      "action": "observes the craftsman intently while speaking excitedly into the lens"
    },
    {
      "name": "Neanderthal Chief",
      "visual_lock": "matches Leader reference image",
      "outfit": "draped untailored deer pelts with bare muscular shoulders",
      "position": "seated cross-legged on deer pelt pad beside hearth"
    }
  ],
  "timeline_action": {
    "0-3s": "From frame 0, Nora speaks immediately into the lens while turning her eyes to watch the Chief turn the black flint core on the pad.",
    "3-6s": "Chief raises quartzite hammerstone hovering precisely above flint platform as Nora points her left index finger toward his technique.",
    "6-8s": "Chief locks his posture preparing strike; Nora turns her face back to lens whispering her final enthusiastic reaction."
  },
  "speech": {
    "speaker": "Nora",
    "voice_profile": "Laomedeia conversational energetic vlog delivery",
    "dialogue": "Look at how he angles that core! Neanderthals were master engineers who shaped flint with micro-precision thousands of years before history began!"
  },
  "negative_constraints": [
    "the camera lens itself and her gripping right hand are completely outside the visible frame and never seen",
    "free left hand never reaches toward, touches, covers, or taps the camera lens",
    "no phone, no smartphone, no screen, no device, no selfie stick, no gimbal",
    "no modern tools or clothing, no subtitles, no watermark"
  ]
}
```

---

### Template 2: First-Person POV Action / Crafting / Stealth (60%–70% Tỷ Lệ)
Dùng khi quan sát cận cảnh hoặc rình săn (Sonic Isolation):

```json
{
  "camera": {
    "type": "first-person pov shot",
    "position": "view is Nora's direct eye-level looking downward forward",
    "framing": "hands and tools centered in lower frame, working surface occupying midground"
  },
  "setting": {
    "location": "limestone ledge overlooking dense temperate pine forest",
    "elements": [
      "mossy limestone boulder in foreground",
      "frost-free damp moss and pine needles, strictly no snow",
      "tall evergreen canopy under overcast grey sky"
    ]
  },
  "characters": [
    {
      "name": "Nora",
      "visual_lock": "matches Nora Body reference sheet; golden deer suede sleeve visible at bottom edge when hands enter",
      "action": "crouches silently behind boulder tracking distant herd"
    }
  ],
  "timeline_action": {
    "0-3s": "Camera peeks carefully over top edge of mossy boulder; Nora's left deer-suede sleeve rests on stone; strictly dead silence.",
    "3-6s": "A massive Steppe Bison grazes 30 meters away among pine trunks; camera pans slowly tracking its heavy breathing.",
    "6-8s": "Nora slowly pulls back behind boulder cover; hand leaves the rock smoothly; heavy tense breathing through nostrils only."
  },
  "speech": {
    "speaker": "Nora",
    "voice_profile": "Sonic Isolation",
    "dialogue": "Strictly NO spoken dialogue. Her mouth stays firmly closed; she holds her breath in dead silence. Tense breathing and wind audio only."
  },
  "negative_constraints": [
    "recording viewpoint is completely unattached and off-screen",
    "both hands remain off-screen except specified left sleeve touch",
    "strictly no spoken dialogue, no mouth movement",
    "no melee combat, no charging animal",
    "no phone, no device, no on-screen display, no subtitles"
  ]
}
```

---

### Template 3: In-Frame Host Experience / Dual-Handed Fixed View (10% Tỷ Lệ)
Dùng khi máy quay đặt trên tảng đá/mặt đất để Nora dùng cả 2 tay trải nghiệm sinh tồn:

```json
{
  "camera": {
    "type": "static rock-mounted medium shot",
    "position": "fixed firmly at waist height on flat limestone ledge three meters away",
    "framing": "Nora fully centered in midground, hearth and tools clearly visible on left"
  },
  "setting": {
    "location": "Pech de l'Aze cave interior hearth bench",
    "elements": [
      "flat work slab with red ochre powder resting on surface from frame 0",
      "birch bark bowl holding water",
      "warm firelight casting soft shadows on limestone walls"
    ]
  },
  "characters": [
    {
      "name": "Nora",
      "visual_lock": "matches Nora face and Nora Body reference sheets exactly",
      "outfit": "wears the exact historical outfit shown in Nora Body reference sheet",
      "action": "seated comfortably using both hands freely to demonstrate ochre pigment"
    }
  ],
  "timeline_action": {
    "0-3s": "From frame 0, Nora speaks directly to the fixed camera while dipping both index fingers directly into red ochre resting on slab.",
    "3-6s": "She rubs the dry crimson pigment between her palms, raising both hands chest-high to show the vibrant mineral coating.",
    "6-8s": "She beams with excitement, gesturing warmly with open ochre-stained palms as she finishes her enthusiastic explanation."
  },
  "speech": {
    "speaker": "Nora",
    "voice_profile": "Laomedeia conversational energetic vlog delivery",
    "dialogue": "This pure red mineral pigment was their ritual paint! Look how intense the crimson is when crushed against wet cave limestone slabs!"
  },
  "negative_constraints": [
    "viewpoint does not move, tilt, or zoom; completely stationary rock-mounted shot",
    "nobody touches or holds the camera viewpoint; both of Nora's hands are free",
    "no phone, no smartphone, no tripod legs visible in shot",
    "no mid-air floating particles; pigment is touched directly from stone surface",
    "no extra clothing variations, no modern items, no text on screen"
  ]
}
```

---

## 5. Cổng Kiểm Tra Bắt Buộc (Mandatory Linter Gate)

Trước khi lưu prompt vào database hoặc gửi batch request tới FlowKit:

```bash
# 1. Kiểm tra nhanh cú pháp JSON & các quy tắc bằng CLI:
python tools/lint_prompt.py --test-json

# 2. Kiểm tra file prompt cụ thể trước khi lưu:
python tools/lint_prompt.py --file path/to/prompt.json

# 3. Hoặc kiểm tra trực tiếp một Scene đã lưu trong DB:
python tools/lint_prompt.py --scene <scene_id>
```

**Tiêu chuẩn thông qua (Gate Acceptance Criteria)**:
- `0 CRITICAL` issues.
- `0 HIGH` issues.
- Nếu phát hiện `GHOST_DEVICE`, `CAMERA_TOUCH_GLITCH`, hoặc `JSON_SCHEMA_MISSING_KEY`: **BẮT BUỘC SỬA LẠI PROMPT NGAY LẬP TỨC TRƯỚC KHI GỬI GEN**.
