---
name: translate-capcut-srt
description: Trích xuất Auto Captions từ CapCut Desktop project và dịch sang ngôn ngữ khác.
---

# Translate CapCut Subtitles (SRT)

Skill này tự động bóc tách phụ đề (Auto Captions) từ CapCut Desktop project, dịch sang ngôn ngữ đích bằng AI, và xuất file `.srt` chuẩn để import ngược lại CapCut.

## Yêu cầu đầu vào

1. `Project Name`: Tên project CapCut (project phải đã được chạy Auto Captions và đã Lưu trên CapCut Desktop).
2. `Target Language`: Ngôn ngữ cần dịch sang (ví dụ: Tiếng Việt, English, Japanese, v.v.).
3. *(Tùy chọn)* `Style / Tone`: Văn phong dịch (ví dụ: tự nhiên, hài hước, trang trọng, v.v.).

---

## Quy trình thực hiện (Workflow)

Thực hiện tuần tự các bước sau:

### Bước 1: Trích xuất file SRT từ CapCut

Sử dụng script local trong repo:
```bash
python tools/capcut_extract_srt.py "<Project Name>"
```
*(Hoặc chỉ định đường dẫn output: `python tools/capcut_extract_srt.py "<Project Name>" -o "transcript-capcut/<Project Name>.srt"`)*.

> *Lưu ý*: Nếu MCP tool `extract_capcut_srt(project_name="<Project Name>")` có sẵn, agent cũng có thể gọi trực tiếp tool này.

Nếu project chưa có phụ đề hoặc chưa lưu, script sẽ thông báo. Nhắc người dùng mở CapCut Desktop → Text → Auto Captions → Create → Bấm Ctrl+S để lưu project rồi chạy lại.

### Bước 2: Đọc nội dung file SRT gốc

Dùng `view_file` đọc toàn bộ file `.srt` vừa được trích xuất.

### Bước 3: Dịch nội dung phụ đề

Sử dụng năng lực dịch của AI model để dịch sang `Target Language`:
- **QUY TẮC CỐT LÕI (BẮT BUỘC):**
  1. **KHÔNG ĐƯỢC THAY ĐỔI** số thứ tự index (1, 2, 3...).
  2. **GIỮ NGUYÊN 100%** timestamp `HH:MM:SS,mmm --> HH:MM:SS,mmm`.
  3. **GIỮ NGUYÊN** dòng trống ngăn cách giữa các entry.
  4. **CHỈ THAY ĐỔI** phần text nội dung câu thoại.
  5. Đảm bảo câu từ tự nhiên, đúng ngữ cảnh video, dịch mượt mà theo văn phong yêu cầu.

### Bước 4: Lưu file SRT đã dịch

Lưu file phụ đề đã dịch vào thư mục `transcript-capcut/` trong workspace:
- Định dạng tên: `transcript-capcut/<Project Name>_<Mã Ngôn Ngữ>.srt` (ví dụ: `transcript-capcut/SharkyEp3_vi.srt`).
- Dùng tool `write_to_file` để ghi file.

### Bước 5: Báo cáo kết quả và hướng dẫn nhập vào CapCut

Thông báo hoàn tất kèm đường dẫn file:
1. Đường dẫn file gốc (`.srt`) và file dịch (`_vi.srt`, `_en.srt`,...).
2. Hướng dẫn người dùng đưa vào CapCut:
   - Mở project CapCut Desktop.
   - Kéo file `.srt` đã dịch thả vào Media bin (khu tài nguyên).
   - Kéo từ Media bin xuống Timeline để tạo track phụ đề mới.
   - (Tùy chọn) Tắt hoặc xóa track Auto Captions cũ để tránh đè chữ.
