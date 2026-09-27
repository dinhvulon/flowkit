# /translate-capcut-srt

Trích xuất Auto Captions từ CapCut Desktop project và dịch sang ngôn ngữ khác.

## Cách dùng

`/translate-capcut-srt [Project Name] -> [Target Language]`

Ví dụ:
- `/translate-capcut-srt 0426 -> Tiếng Anh`
- `/translate-capcut-srt SharkyEp3 -> Tiếng Việt`

## Hướng dẫn thực hiện

Khi người dùng chạy lệnh này, bạn hãy:
1. Đọc và làm theo hướng dẫn trong skill `skills/translate-capcut-srt.md` hoặc `.claude/skills/translate-capcut-srt/SKILL.md`.
2. Trích xuất SRT bằng lệnh:
   ```bash
   python tools/capcut_extract_srt.py "$ARGUMENTS"
   ```
   (Hoặc dùng MCP tool `extract_capcut_srt` nếu có).
3. Đọc nội dung file SRT, dịch sang ngôn ngữ yêu cầu:
   - **BẮT BUỘC GIỮ NGUYÊN**: số thứ tự index, timestamp `HH:MM:SS,mmm --> HH:MM:SS,mmm`, dòng trống.
   - Chỉ dịch phần text nội dung.
4. Lưu file dịch vào `transcript-capcut/<Project>_<lang>.srt`.
5. Thông báo hoàn tất và hướng dẫn người dùng kéo thả file `.srt` vào Media bin của CapCut.

Arguments: $ARGUMENTS
