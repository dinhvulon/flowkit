# /extract-capcut-srt

Liệt kê project CapCut và trích xuất phụ đề Auto Captions thành file .srt chuẩn.

## Cách dùng

`/extract-capcut-srt [Project Name hoặc --list]`

Ví dụ:
- `/extract-capcut-srt --list` (Liệt kê tất cả project và số câu phụ đề)
- `/extract-capcut-srt 0426` (Bóc tách phụ đề project 0426)

## Hướng dẫn thực hiện

1. Nếu đối số là `--list` hoặc rỗng:
   Chạy `python tools/capcut_extract_srt.py --list` và hiển thị danh sách project cho người dùng.
2. Nếu có tên project:
   Chạy `python tools/capcut_extract_srt.py "$ARGUMENTS"` (hoặc MCP `extract_capcut_srt`).
3. Trả về đường dẫn file `.srt` đã xuất kèm 5 dòng preview đầu tiên.

Arguments: $ARGUMENTS
