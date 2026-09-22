# fk-vlog-guide — Master Guide & Interactive Hub for Historical POV Vlogs

Cẩm nang điều phối trọn gói quy trình sản xuất Video Vlog Du Hành Lịch Sử / POV Time Travel từ A đến Z, kèm bảng lựa chọn (Options Menu) cho từng giai đoạn từ nghiên cứu, kịch bản, nạp mặt thật, chạy pipeline đến xuất bản YouTube.

---

## 🧭 BẢNG ĐIỀU PHỐI QUY TRÌNH (PRODUCTION HUB)

Khi bạn muốn sản xuất một tập vlog mới, hãy thực hiện tuần tự qua các giai đoạn sau:

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ 0. THIẾT LẬP MÔI TRƯỜNG & KẾT NỐI (Pre-Flight)  ➔ /health: true             │
│ 1. NGHIÊN CỨU DỮ KIỆN (Fact-Check)              ➔ /fk-research              │
│ 2. TẠO KỊCH BẢN & SET ACTIVE PROJECT            ➔ /fk-vlog-japan            │
│ 3. NẠP ẢNH MẶT THẬT (Tùy chọn)                  ➔ /fk-upload-ref            │
│ 4. CHẠY PIPELINE TỰ ĐỘNG (All-in-One)           ➔ /fk-pipeline              │
│ 5. XEM LẠI & ĐĂNG TẢI YOUTUBE                   ➔ /fk-youtube-upload        │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ GIAI ĐOẠN 0: THIẾT LẬP TỪ ĐẦU ĐẾN CHẠY DỰ ÁN (SETUP & PRE-FLIGHT)

Hệ thống FlowKit hoạt động theo cơ chế cầu nối 3 lớp:
```text
┌──────────────────┐     WebSocket      ┌──────────────────────┐     RPC Web     ┌──────────────────┐
│  Python Agent    │◄──────────────────►│  Chrome Extension     │───────────────►│  flow.google.com │
│  (FastAPI :8100) │    localhost:9222  │  (MV3 Extension)     │                 │  (Tab đang mở)   │
└──────────────────┘                    └──────────────────────┘                 └──────────────────┘
```
> **Tại sao cần trình duyệt thật?** Google Flow ký mỗi lệnh sinh ảnh/video bằng token phiên `at`, cookie Google và mã giải reCAPTCHA chỉ sinh được trên tab web thật. Script Python không thể chạy ngầm headless mà cần gửi lệnh qua Chrome Extension trên tab đang mở.

### 5 Bước Chuẩn Bị & Khởi Chạy (Pre-Flight Checklist)

#### Bước 0.1: Cài Chrome Extension vào trình duyệt
1. Mở Google Chrome, gõ địa chỉ: `chrome://extensions`
2. Bật công tắc **Chế độ dành cho nhà phát triển (Developer mode)** ở góc trên bên phải.
3. Bấm **Tải tiện ích đã giải nén (Load unpacked)**.
4. Chọn thư mục `extension/` của dự án (`c:\flowkit\extension`). Icon **Flow Kit** sẽ xuất hiện trên thanh công cụ.

#### Bước 0.2: Đăng nhập Google Flow & Luôn giữ tab mở
1. Mở tab mới trên Chrome và truy cập: **https://flow.google.com/**
2. Đăng nhập tài khoản Google của bạn.
3. **Quy tắc vàng:** Luôn **giữ tab `flow.google.com` này mở** trong suốt quá trình tạo video.

#### Bước 0.3: Lấy mã `FLOW_PROJECT_ID`
1. Trên giao diện `flow.google.com`, bấm mở một Project có sẵn (hoặc tạo mới).
2. Nhìn lên URL trình duyệt: `https://flow.google.com/project/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`
3. Copy chuỗi mã UUID ở cuối URL và gán vào terminal:
   - **Windows PowerShell:**
     ```powershell
     $env:FLOW_PROJECT_ID="chuỗi-uuid-vừa-copy"
     ```
   - **macOS / Linux / Git Bash:**
     ```bash
     export FLOW_PROJECT_ID="chuỗi-uuid-vừa-copy"
     ```

#### Bước 0.4: Khởi động Server Python (FastAPI cổng 8100)
Tại thư mục gốc dự án (`c:\flowkit`):
- **Windows PowerShell:**
  ```powershell
  .\venv\Scripts\Activate.ps1
  python -m agent.main
  ```
- **macOS / Linux / Git Bash:**
  ```bash
  source venv/bin/activate
  python -m agent.main
  ```
> [!NOTE]
> **Xử lý sự cố cổng 8100:** Nếu terminal báo lỗi `address already in use` hoặc tự tắt ngay, nghĩa là Server FlowKit **đang chạy ngầm sẵn từ trước** rồi! Bạn không cần bật lại mà chỉ cần mở tab terminal khác để thao tác.

#### Bước 0.5: Kiểm tra kết nối Health Check (Bắt Buộc)
Mở một cửa sổ terminal mới và chạy:
- **Windows PowerShell:**
  ```powershell
  curl.exe -s http://127.0.0.1:8100/health
  # (Lưu ý: Bắt buộc thêm đuôi .exe vì trong PowerShell từ "curl" là bí danh của Invoke-WebRequest)
  ```
- **macOS / Linux / Git Bash:**
  ```bash
  curl -s http://127.0.0.1:8100/health
  ```
**Kết quả bắt buộc phải có:**
```json
{"status": "ok", "extension_connected": true}
```
Khi thấy `"extension_connected": true`, toàn bộ hệ thống cầu nối đã thông suốt và sẵn sàng chạy các bước kịch bản bên dưới!

---

## 📌 CHI TIẾT TỪNG BƯỚC SẢN XUẤT VLOG (WORKFLOW)

### BƯỚC 1: Nghiên Cứu Dữ Kiện Lịch Sử (`/fk-research`)

Xác minh thực tế để kịch bản không bị AI "ảo giác" hoặc sáng tác sai niên đại:

```bash
# Ví dụ chọn đề tài:
/fk-research "Heian-kyo daily life 1000 AD commoners food market dress"
/fk-research "Kamakura period 1274 AD samurai defense mongol invasion"
/fk-research "Edo period 1657 AD great fire of meireki machiya"
```

> [!TIP]
> Kết quả nghiên cứu sẽ được lưu vào `.omc/research/<topic>.md`. Các chi tiết về trang phục, giá cả hàng hóa, món ăn sẽ được nhúng thẳng vào câu thoại của Vlogger.

---

### BƯỚC 2: Khóa Mỹ Thuật & Tạo Kịch Bản (`/fk-vlog-japan`)

1. **Khóa chất liệu mỹ thuật qua [`/fk-add-material`](file:///c:/flowkit/skills/fk-add-material.md)**:
   - Luôn nạp `material: "realistic"` vào dự án. Hệ thống sẽ tự động chèn tiền tố _Photorealistic RAW photograph, natural available light_ vào toàn bộ ảnh nhân vật và phân cảnh, đồng thời áp negative prompt chống trôi thành anime/3D.
   - Kiểm tra các material có sẵn:
     ```bash
     curl -s http://127.0.0.1:8100/api/materials
     ```
2. **Quy chuẩn góc máy Veo 3 ([`/fk-camera-guide`](file:///c:/flowkit/skills/fk-camera-guide.md))**:
   - Cầm camera selfie trước góc rộng 24–28mm.
   - Khẩu độ Pan-Focus f/8–f/11 (nét sâu từ mặt vlogger đến cảnh chợ phía sau, zero bokeh).
   - Kỹ thuật **vừa đi vừa quay (Walking POV)**: camera nảy nhẹ theo bước chân, tạo hiệu ứng trôi cảnh 3D parallax sống động.
3. **Tạo kịch bản vào FlowKit**:
   - Gọi **[`/fk-vlog-japan`](file:///c:/flowkit/skills/fk-vlog-japan.md)** để sinh trọn gói kịch bản 10–12 phân cảnh với thoại tiếng Nhật đàm thoại chuẩn `dialog-japan`.
   - Hoặc chạy nhanh script kịch bản có sẵn:
     ```bash
     python scripts/create_kamakura_1274.py   # Kịch bản Vịnh Hakata 1274
     # hoặc
     python scripts/create_kyoto_heian_1000.py # Kịch bản Kyoto Heian 1000
     ```

---

### BƯỚC 2.5: Xác Định & Đặt Dự Án Hoạt Động (Set Active Project)

Khi bạn vừa chạy xong script tạo dự án, FlowKit có cơ chế nhận diện tự động:
1. **Tự Động Kích Hoạt (Auto-Active / Fallback)**:
   - Hệ thống tự động ưu tiên dự án mới tạo gần đây nhất (`fallback_most_recent`). Bạn có thể chạy ngay các lệnh ở Bước 3 & 4 mà không cần gõ kèm `project_id`.
2. **Kiểm Tra Dự Án Đang Hoạt Động**:
   ```bash
   curl -s http://127.0.0.1:8100/api/active-project
   # Hoặc xem bảng trạng thái: /fk-status
   ```
3. **Chuyển Đổi / Đặt Đích Danh Dự Án (`/fk-switch-project`)**:
   Nếu trong FlowKit đang có nhiều dự án và bạn muốn chỉ định rõ ràng dự án cần thao tác:
   ```bash
   /fk-switch-project <PROJECT_ID>
   ```
   *Mẹo*: Bạn cũng có thể truyền trực tiếp `<PROJECT_ID>` vào các lệnh pipeline:
   ```bash
   /fk-pipeline <PROJECT_ID> --r2v --tts --concat
   /fk-upload-ref "C:/photos/my_face.jpg" --project <PROJECT_ID> --entity "Vlogger"
   ```

---

### BƯỚC 3: Nạp Ảnh Mặt Thật Của Bạn (`/fk-upload-ref`)

Nếu bạn muốn đóng vai Vlogger chính trong chuyến du hành thay vì để AI tự tạo mặt:

```bash
/fk-upload-ref "C:/photos/my_face.jpg" --entity "Vlogger"
```

- **Tự động khóa nhận diện**: Ảnh thật được đẩy lên Google Flow và gán mã UUID `media_id` vào nhân vật.
- **Bảo toàn 100%**: AI sẽ bỏ qua việc vẽ mặt ảo và dùng chính ảnh này làm khuôn mẫu cho tất cả các góc quay.

---

### BƯỚC 4: Chạy Trọn Gói Pipeline (`/fk-pipeline`)

Chỉ với một câu lệnh duy nhất, hệ thống tự động làm hết mọi khâu nặng nhọc:

```bash
/fk-pipeline --r2v --tts --concat
```

**Các giai đoạn tự động chạy ngầm:**

1. **Model R2V (`abra_r2v_8s`)**: Nạp thẳng ảnh tham chiếu mặt thật vào Google Flow để sinh 10 clip video 8s mà không cần qua bước tạo ảnh tĩnh Start Frame.
2. **Khẩu hình Veo 3 Lip-Sync**: Tự động render cử động môi nhân vật nói chuyện tiếng Nhật tự nhiên theo câu thoại đặt trong ngoặc kép.
3. **Lồng tiếng TTS Studio**: Tạo giọng đọc tiếng Nhật đàm thoại chuẩn nhịp phách mora.
4. **Ghép nối video (Concat)**: Ghép 10 clip và lồng âm thanh hoàn chỉnh ra file `output/<slug>/<slug>_final.mp4`.
5. **Tự động sinh YouTube SEO (`/fk-youtube-seo`)**: Tạo tiêu đề hook, mô tả 4 phần chuẩn SEO, bộ tag 3 tầng và timestamps chapters vào file `youtube_metadata.json` & `.md`.
6. **Tự động tạo 4 Thumbnail (`/fk-thumbnail`)**: Sinh 4 ảnh thumbnail ấn tượng chuẩn tỷ lệ (9:16 Shorts hoặc 16:9 Long-form) lưu vào `output/<slug>/thumbnails/`.

---

### BƯỚC 5: Bảng Lựa Chọn Xuất Bản YouTube (`/fk-youtube-upload`)

Sau khi pipeline hoàn tất, bạn kiểm tra thư mục `output/<slug>/` và tiến hành xuất bản theo các tùy chọn dưới đây:

#### Bảng Tùy Chọn Upload (Options Menu):

| Tùy chọn                                 | Lệnh thực hiện                          | Ý nghĩa                                                                                                                                     |
| :--------------------------------------- | :-------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------ |
| **1. Duyệt trước an toàn (Recommended)** | `/fk-youtube-upload --privacy unlisted` | Đăng video ở chế độ **Không công khai (Unlisted)** để bạn xem thử chất lượng và kiểm tra bản quyền trên YouTube Studio trước khi công khai. |
| **2. Đăng công khai ngay**               | `/fk-youtube-upload --privacy public`   | Đăng video công khai (Public) lập tức tới người xem.                                                                                        |
| **3. Chọn ảnh Thumbnail**                | `/fk-youtube-upload --thumbnail 2`      | Chọn biến thể thumbnail yêu thích (từ 1 đến 4 trong thư mục `thumbnails/`) làm ảnh đại diện chính.                                          |
| **4. Hẹn giờ đăng tải (Schedule)**       | `/fk-youtube-upload --schedule "19:00"` | Hẹn giờ đăng vào khung giờ vàng (12:00 trưa hoặc 19:00 tối).                                                                                |
| **5. Xem trước không upload (Dry-run)**  | `/fk-youtube-upload --dry-run`          | In toàn bộ thông tin (Tiêu đề, mô tả, tags, đường dẫn video, thumbnail) ra màn hình để kiểm tra trước.                                      |

---

## 🎯 DANH SÁCH CÂU LỆNH TẮT ĐỂ COPY NHANH

```bash
# Toàn bộ quy trình rút gọn từ A-Z:

# 0. Kiểm tra kết nối Chrome Extension & Server:
curl.exe -s http://127.0.0.1:8100/health

# 1. Nghiên cứu tư liệu lịch sử:
/fk-research "Kamakura period 1274 AD samurai defense mongol invasion"

# 2. Khởi tạo dự án & 10 phân cảnh:
python scripts/create_kamakura_1274.py

# 3. Nạp ảnh mặt thật (tùy chọn):
/fk-upload-ref "C:/photos/my_face.jpg" --entity "Vlogger"

# 4. Chạy toàn bộ pipeline tự động (R2V + TTS + Concat + SEO + Thumbnails):
/fk-pipeline --r2v --tts --concat

# 5. Xuất bản YouTube:
/fk-youtube-upload --privacy unlisted --thumbnail 1
```
