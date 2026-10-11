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
5. **Bắt buộc dùng skill:** `/fk-camera-guide`, `/fk-cinematic-transitions` (+ `references/transitions.md`), `/fk-action-choreography`, `/fk-scriptwriter` + `references/story-engine.md`, `/fk-character-bible`, `/fk-gen-narrator`, `/fk-sound-design`, `/fk-prompt-lock`, `/fk-animation-vocabulary` (thuật ngữ chuyển động chuẩn), và `/fk-improve-animations` (thiết kế gia tốc, nhịp độ & giảm chấn quán tính theo ngân sách thời gian). Ghi rõ skill đã áp cho từng clip trong kịch bản/storyboard.

---

## Rule 57 — Chuẩn hóa từ vựng chuyển động & động học qua `animation-vocabulary` (User Lock 11/10/2026)

Áp dụng cho cả Antigravity (`agy`) và Claude (`claude`):

1. **Bắt buộc dùng skill `animation-vocabulary`**: Khi xây dựng kịch bản, storyboard, và viết `video_prompt` (đặc biệt cho Time-Travel / POV Vlog): BẮT BUỘC phải tra cứu và áp dụng từ vựng chuẩn từ skill `animation-vocabulary` (`skills/animation-vocabulary/SKILL.md` hoặc `/fk-animation-vocabulary`) để miêu tả chính xác động học (motion dynamics), quán tính và tương tác camera.
2. **Cấm từ ngữ chuyển động mơ hồ, chung chung**: TUYỆT ĐỐI CẤM dùng các mô tả mơ hồ như "moves quickly", "shakes violently", "jumps weirdly", "smoothly appears". Thay vào đó, BẮT BUỘC dùng các thuật ngữ chính xác theo vật lý và animation:
   - *Động học & Quán tính*: **Anticipation** (hạ thấp trọng tâm/lấy đà trước khi hành động), **Overshoot** (văng quá đà trước khi nén dừng), **Settle** (triệt tiêu chấn động hồi phục thăng bằng), **Secondary motion** (quán tính chuyển động trễ của tóc đuôi ngựa, vạt áo da thú, lông thú viền cổ).
   - *Xuất hiện, biến mất & Chuyển đổi khung*: **Pop in** (nảy bung xuất hiện nhanh), **Stagger** (chuỗi hành động/nhân vật xuất hiện so le kế tiếp nhau), **Foreground wipe** / **Clip-path sweep** (che quét mở khung hình qua vật cản tiền cảnh), **Slide & Dampen** (trượt dốc có lực ma sát hãm phanh).
   - *Động học Camera Vlog*: **Rubber-banding** (kéo giãn rồi nảy bật đàn hồi trở lại khi camera hay cánh tay đạt cự ly tối đa), **Vertical bounce** (nhấp nhô nhịp nhàng theo bước chạy bộ), **Rotational lag** (độ trễ góc xoay quán tính khi thân người ngoái đầu), **Drift** (trôi góc nhẹ tự nhiên).
3. **Hiệu quả thực tế**: Giúp AI video model (Veo 3 / Omni Flash R2V `abra_r2v`) phân giải chính xác vector lực cơ học, loại bỏ triệt để hiện tượng nhân vật di chuyển trôi nổi (floating/gliding), tay chân biến dạng, hoặc camera chuyển động giật cục phi tự nhiên.

---

## Rule 58 — Thiết kế động lực học khi viết prompt & Giám định chuyển động qua `improve-animations` (User Lock 11/10/2026)

Áp dụng cho cả Antigravity (`agy`) và Claude (`claude`):

1. **BẮT BUỘC DÙNG KHI VIẾT STORYBOARD & PROMPT (Tiền kỳ)**: Khi viết storyboard và `video_prompt`, BẮT BUỘC áp dụng triết lý và tiêu chuẩn của `improve-animations` (`skills/improve-animations/` hoặc `/fk-improve-animations`) để đóng vai trò Cố vấn Động lực học (Motion Architecture Advisor):
   - *Ngân sách thời gian hành động (Duration Budgeting)*: Trong clip 8s, mỗi sub-clip 2–3s (`0-3s`, `3-6s`, `6-8s`) chỉ được bố trí đúng 1 chu kỳ chuyển động chính. Tuyệt đối CẤM nhồi nhét 2–3 hành động dồn dập vào cùng 1 mốc thời gian làm model AI phải tua nhanh khung hình gây giật cục và vỡ giải phẫu.
   - *Đường cong gia tốc & Giảm chấn (Easing & Damping Curves)*: Mọi chuyển động phải thiết kế đủ 3 pha: Khởi phát lấy đà (`Anticipation / Ease-in`), Đỉnh vận tốc (`Peak velocity`), và Hãm phanh triệt tiêu quán tính (`Deceleration / Damping / Settle`). Cấm mô tả chuyển động tuyến tính đều đều từ đầu đến cuối (`linear speed`).
   - *Độ trễ của quán tính thứ cấp (Secondary Motion Timing)*: Tóc, viền lông thú, tà áo và dây thắt lưng luôn có độ trễ quán tính 0.2s–0.3s so với thân người khi dừng.
2. **BẮT BUỘC DÙNG KHI REVIEW VIDEO 720p THÔ & LẬP KẾ HOẠCH SỬA PROMPT**: Khi review video AI 720p thô (`/fk-review-video`), nếu một cảnh bị chấm điểm dưới 7.5 ở Motion Quality (20%) hoặc Temporal Coherence (10%), hoặc xuất hiện dị tật động học, BẮT BUỘC dùng `improve-animations` lập Motion Remediation Plan độc lập theo mẫu chuẩn `PLAN-TEMPLATE.md` với các thông số vật lý chính xác để User duyệt trước khi regen.
3. **BẮT BUỘC DÙNG KHI HẬU KỲ CẮT DỰNG**: Rà soát hướng vector chuyển động (motion vector) giữa 2 cảnh cắt nối (Match-on-action, J-cut) để mắt người xem không bị đứt gãy mạch theo dõi chuyển động.
