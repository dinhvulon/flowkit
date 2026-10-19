# Quy tắc Khóa Prompt Video: Bắt buộc cấu trúc JSON & Chạy Linter (Prompt Lock Rule)

> **QUY TẮC BẮT BUỘC CHO MỌI AGENT KHI VIẾT HOẶC SỬA PROMPT VIDEO TRONG FLOWKIT:**
> Áp dụng cho cả Antigravity (`agy`) và Claude (`claude`).

Khi tạo mới hoặc cập nhật bất kỳ `video_prompt` nào (`POST /api/scenes`, `PATCH /api/scenes`, hoặc submit lệnh sinh video qua batch API):

### 1. BẮT BUỘC DÙNG CẤU TRÚC STRUCTURED JSON
Tuyệt đối không viết prompt dạng văn bản tự do, lộn xộn hoặc chèn ký tự đặc biệt gây lỗi tokenization (như em-dash `\u2014`). Mọi prompt phải tuân thủ chuẩn của skill `/fk-prompt-lock` và chứa các khối JSON sau:
- `camera`: Loại góc máy, vị trí, bố cục khung hình (tuân thủ Tỷ lệ Góc Máy Vàng: 60-70% POV, 20-30% OTS/Selfie, 10% Fixed; khóa điểm mù quang học ngoài khung hình).
- `setting`: Địa điểm, thời kỳ, các vật liệu có sẵn từ giây 0, khớp 100% Setting Reference.
- `characters`: Danh sách nhân vật có `visual_lock` khớp ảnh ref (Face + Dressed Body), khóa `wears the exact historical outfit shown in the [Character] Body reference sheet`, cấm tả lại trang phục lan man, cấm tả ngực/khe ngực làm méo áo.
- `timeline_action`: Chia 3 mốc thời gian rõ ràng: `0-3s`, `3-6s`, `6-8s`. Nói ngay từ giây 0 (`Immediate Frame-0 Delivery`).
- `speech`: Khóa thoại 23–25 từ theo giọng Laomedeia (hoặc Sonic Isolation nếu là cảnh rình săn/ẩn nấp).
- `negative_constraints`: Danh sách câu phủ định đối kháng (cấm phone, smartphone, screen, device, selfie-stick, gimbal, camera chạm tay, chuyển góc 3rd-person).

### 2. BẮT BUỘC CHẠY PROMPT LINTER TRƯỚC KHI LƯU VÀ SINH
Trước khi lưu prompt vào database (`flow_agent.db`) hoặc gửi bất kỳ request sinh video nào (`GENERATE_VIDEO_REFS`), Agent **BẮT BUỘC PHẢI CHẠY LỆNH KIỂM TRA**:
```bash
python tools/lint_prompt.py --test-json
# Hoặc kiểm tra file prompt:
python tools/lint_prompt.py --file <path_to_prompt.json>
# Hoặc kiểm tra scene đã lưu:
python tools/lint_prompt.py --scene <scene_id>
```
Nếu có bất kỳ lỗi nào (`CRITICAL` hoặc `HIGH`): **CẤM GỬI LỆNH SINH VIDEO**. Agent phải sửa prompt đạt 0 lỗi mới được tiếp tục!

---

## Rule 56 — Prompt càng chi tiết càng tốt & Bắt buộc dùng skill làm phim (User Lock 10/10/2026)

Áp dụng cho cả Antigravity (`agy`) và Claude (`claude`):

1. **Không giới hạn độ dài prompt.** Tả từng cử chỉ, từng chuyển động theo mốc thời gian: mỗi bàn tay cầm gì/làm gì, ánh mắt, tư thế, trọng tâm, hơi thở, hướng di chuyển trong khung, vị trí đồ vật từ frame 0 và trạng thái cuối clip. Chỗ trống = AI tự bịa lỗi.
2. **Sửa lỗi bằng cách tả thêm, không cắt bớt.** Chỉ bỏ yếu tố khi hỏng lặp lại nhiều lần và phải báo user.
3. **Nhân vật phụ luôn "sống"**, kể cả hậu cảnh (thở, đọng khói hơi thở, đổi trọng tâm, chớp mắt, quay đầu theo hành động, siết đồ đang cầm); thú vật đánh hơi, bước, vẫy tai. Không ai đứng đơ như tượng.
4. **Khối vật lý 5 tầng** (`/fk-camera-guide`) trong mọi prompt: chuyển động chính · lực & ma sát · chuyển động phụ · môi trường · phản ứng máy quay.
5. **Bắt buộc dùng skill:** `/fk-camera-guide`, `/fk-cinematic-transitions` (+ `references/transitions.md`), `/fk-action-choreography`, `/fk-scriptwriter` + `references/story-engine.md`, `/fk-character-bible`, `/fk-gen-narrator`, `/fk-sound-design`, và `/fk-prompt-lock`; từ vựng chuyển động và nhịp động học theo `skills/fk-film/references/cinematic-toolkit.md` §8–9 (Rule 57–58). Ghi rõ skill đã áp cho từng clip trong kịch bản/storyboard.

---

## Rule 57 — Từ vựng chuyển động chuẩn (User Lock 11/10/2026)

Áp dụng cho cả Antigravity (`agy`) và Claude (`claude`):

1. Mọi chuyển động của nhân vật và khung hình viết bằng hành động vật lý cụ thể, kèm thuật ngữ trong ngoặc: **Anticipation**, **Overshoot**, **Settle**, **Secondary motion**, **Stagger**, **Reveal**, **Slide & Dampen**, **Rubber-banding**, **Vertical bounce**, **Rotational lag**, **Drift**.
2. CẤM từ mơ hồ: "moves quickly", "shakes violently", "jumps weirdly", "smoothly appears", "pops in". Vật/người lộ ra phải đi từ sau vật che có sẵn từ giây 0.
3. Bảng tra: `skills/fk-film/references/cinematic-toolkit.md` §8.

---

## Rule 58 — Nhịp động học, điểm tựa & sửa lỗi chuyển động (User Lock 11/10/2026)

Áp dụng cho cả Antigravity (`agy`) và Claude (`claude`):

1. **Tiền kỳ (storyboard & prompt)**: mỗi mốc `timeline_action` đúng 1 beat chính (8s: `0-3s / 3-6s / 6-8s`; 10s: `0-3s / 3-7s / 7-10s`); mỗi động tác đủ 3 pha lấy đà → đỉnh vận tốc → hồi thăng bằng; tóc, lông, tà áo trễ 0.2–0.3s; người ngồi/quỳ/ngả/dựa ghi rõ điểm tựa; frame 0 là tư thế trước hành động đầu tiên; chừa 0.5s cuối.
2. **Review 720p**: clip dưới ngưỡng giữ, Motion Quality / Temporal Coherence < 7.5, hoặc có lỗi chuyển động nhìn thấy → Motion Fix Plan (giây + frame lỗi, khối prompt cũ và mới nguyên văn, chỉ đổi khối liên quan) → lint → PATCH → hỏi user trước khi regen.
3. **Hậu kỳ**: rà hướng chuyển động và tư thế giữa 2 clip cắt nối (match on action, J-cut).
4. Chi tiết: `cinematic-toolkit.md` §9 + checklist B dòng 40–45 trong `references/prompt-lock.md`.
