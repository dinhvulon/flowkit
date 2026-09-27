---
name: extract-capcut-srt
description: Liệt kê project CapCut và trích xuất phụ đề Auto Captions thành file .srt chuẩn.
---

# Extract CapCut Subtitles (SRT)

Skill này dùng để liệt kê các project CapCut Desktop trên máy và trích xuất phụ đề Auto Captions thành file `.srt` chuẩn.

## Lệnh CLI chính

```bash
# 1. Liệt kê tất cả project CapCut + số dòng subtitle
python tools/capcut_extract_srt.py --list

# 2. Xuất SRT từ một project cụ thể
python tools/capcut_extract_srt.py "<Project Name>"

# 3. Xuất SRT chỉ định thư mục lưu trữ
python tools/capcut_extract_srt.py "<Project Name>" -o "transcript-capcut/<Project Name>.srt"
```

## Khi dùng qua MCP

Nếu server `flow-capcut-mcp` đang chạy:
```python
extract_capcut_srt(project_name="<Project Name>")
```

## Lưu ý quan trọng

1. Project phải được tạo Auto Captions trong CapCut Desktop trước (`Text` -> `Auto Captions` -> `Create`).
2. Project phải được **LƯU** (`Ctrl+S`) để CapCut ghi dữ liệu xuống `draft_content.json`.
3. Script tự động tìm kiếm trong:
   - CapCut Desktop: `%USERPROFILE%\AppData\Local\CapCut\User Data\Projects\com.lveditor.draft`
   - JianyingPro (bản Trung): `%USERPROFILE%\AppData\Local\JianyingPro\User Data\Projects\com.lveditor.draft`
