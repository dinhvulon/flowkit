# extract-capcut-srt — Bóc tách phụ đề CapCut Desktop

Liệt kê project CapCut và trích xuất phụ đề Auto Captions thành file `.srt` chuẩn.

## Cách dùng

```bash
# Liệt kê project
python tools/capcut_extract_srt.py --list

# Xuất SRT
python tools/capcut_extract_srt.py "<Project Name>"
```

Hoặc qua MCP:
```python
extract_capcut_srt(project_name="<Project Name>")
```
