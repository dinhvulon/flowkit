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
