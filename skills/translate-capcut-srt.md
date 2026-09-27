# translate-capcut-srt — Dịch phụ đề CapCut Desktop

Trích xuất Auto Captions từ CapCut Desktop project và dịch sang ngôn ngữ khác.

## Cách dùng

```bash
# Trích xuất phụ đề từ project CapCut
python tools/capcut_extract_srt.py "<Project Name>" -o "transcript-capcut/<Project Name>.srt"
```

Hoặc qua MCP:
```python
extract_capcut_srt(project_name="<Project Name>")
```

Sau khi có file `.srt`, agent dịch giữ nguyên timestamp `HH:MM:SS,mmm` và lưu thành:
`transcript-capcut/<Project Name>_<lang>.srt` (ví dụ `_vi.srt`, `_en.srt`).
