# fk-upload-ref — Upload Custom Reference Image for Character/Entity

Tải ảnh chân dung thật hoặc ảnh trang phục/đạo cụ từ máy tính lên Google Flow và tự động gán làm ảnh Reference chính (`media_id` UUID) cho nhân vật trong dự án trước khi chạy pipeline.

Khi nhân vật đã có `media_id` từ ảnh bạn tải lên:
- `/fk-gen-refs` sẽ **bỏ qua không sinh mặt nhân vật bằng AI** (giữ nguyên 100% ảnh thật của bạn).
- `/fk-pipeline` (chuẩn I2V) sẽ tự động lấy ảnh này làm `imageInputs` reference để mọi góc quay đều mang khuôn mặt của bạn.
- `/fk-pipeline --r2v` (R2V trực tiếp) sẽ đưa thẳng ảnh tham chiếu này vào model `abra_r2v_8s` để sinh video mà không cần qua bước tạo Start Frame, tiết kiệm thời gian và giữ trọn nét gốc.

---

## Cách Dùng

```bash
/fk-upload-ref <file_path> [--project <project_id>] [--entity <entity_name_or_id>]
```

**Ví dụ:**
```bash
# Upload ảnh chân dung của bạn làm mặt Vlogger cho dự án đang hoạt động
/fk-upload-ref "C:/Users/Administrator/Pictures/my_face.jpg" --entity "Vlogger"

# Chỉ định rõ project_id
/fk-upload-ref "C:/photos/face.png" --project d666c67a-6fb5-4d06-9c71-58ac28b8a938 --entity "Vlogger"
```

---

## Các Bước Thực Hiện Chi Tiết

### Bước 1: Kiểm Tra Trạng Thái Kết Nối
```bash
curl -s http://127.0.0.1:8100/health
# Bắt buộc trả về: {"extension_connected": true}
```

### Bước 2: Xác Định Project và Entity
Nếu không truyền `--project`, lấy project đang hoạt động gần nhất:
```bash
PID=$(curl -s http://127.0.0.1:8100/api/projects | python -c "import sys, json; projs = json.load(sys.stdin); print(projs[-1]['id'])")
```

Tìm entity (ví dụ "Vlogger"):
```bash
curl -s "http://127.0.0.1:8100/api/projects/$PID/characters"
# Lấy ID của nhân vật có name trùng khớp (hoặc tạo mới nếu chưa có)
```

### Bước 3: Upload File Lên Google Flow
```bash
curl -s -X POST http://127.0.0.1:8100/api/flow/upload-image \
  -H "Content-Type: application/json" \
  -d '{
    "file_path": "<FILE_PATH>",
    "project_id": "<PID>"
  }'
```
Kết quả trả về chứa:
```json
{
  "media_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

### Bước 4: Gán UUID media_id Vào Entity
```bash
curl -s -X PATCH "http://127.0.0.1:8100/api/characters/<ENTITY_ID>" \
  -H "Content-Type: application/json" \
  -d '{"media_id": "<MEDIA_ID>"}'
```

### Bước 5: Xác Nhận & Sẵn Sàng Chạy Pipeline
Kiểm tra lại entity:
```bash
curl -s "http://127.0.0.1:8100/api/characters/<ENTITY_ID>"
```
In kết quả cho người dùng:
```text
✅ Đã nạp thành công ảnh tham chiếu cho [<Entity Name>]!
  - File nguồn: <file_path>
  - Media ID: <media_id>
  - Trạng thái: Sẵn sàng cho /fk-pipeline (AI sẽ giữ nguyên khuôn mặt thật này làm Reference xuyên suốt tất cả phân cảnh).
```
