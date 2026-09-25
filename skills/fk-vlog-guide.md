# fk-vlog-guide — Master Guide & Interactive Hub for Historical POV Vlogs

Cẩm nang điều phối trọn gói quy trình sản xuất Video Vlog Du Hành Lịch Sử / POV Time Travel từ A đến Z, kèm bảng lựa chọn (Options Menu) cho từng giai đoạn từ nghiên cứu, kịch bản, nạp mặt thật, chạy pipeline đến xuất bản YouTube.

---

## 🧭 BẢNG ĐIỀU PHỐI QUY TRÌNH (PRODUCTION HUB)

Khi bạn muốn sản xuất một tập vlog mới, hãy thực hiện tuần tự qua các giai đoạn sau:

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ 0. THIẾT LẬP MÔI TRƯỜNG & UI WEB (Pre-Flight)   ➔ /health: true & :5173     │
│ 1. NGHIÊN CỨU DỮ KIỆN (Fact-Check)              ➔ /fk-research              │
│ 2. TẠO KỊCH BẢN & SET ACTIVE PROJECT            ➔ /fk-vlog-japan            │
│ 3. NẠP ẢNH MẶT THẬT (Tùy chọn)                  ➔ /fk-upload-ref            │
│ 4. CHẠY PIPELINE TỰ ĐỘNG (All-in-One)           ➔ /fk-pipeline              │
│ 4.5. KIỂM DUYỆT VIDEO (Review Board)            ➔ /fk-review-board (:8200)  │
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

### 6 Bước Chuẩn Bị & Khởi Chạy (Pre-Flight Checklist)

#### Bước 0.1: Cài / cập nhật Chrome Extension (bản ≥ 0.3.4)
1. Mở Google Chrome, gõ địa chỉ: `chrome://extensions`
2. Bật công tắc **Chế độ dành cho nhà phát triển (Developer mode)** ở góc trên bên phải.
3. Lần đầu: bấm **Tải tiện ích đã giải nén (Load unpacked)** → chọn thư mục `extension/` của dự án (`c:\flowkit\extension`). Icon **Flow Kit** sẽ xuất hiện trên thanh công cụ.
4. **Đã cài rồi mà vừa pull code mới:** bấm **↻ Reload** trên thẻ Flow Kit (Chrome không tự nạp lại), rồi kiểm tra thẻ ghi **phiên bản 0.3.4 trở lên**.

> [!IMPORTANT]
> Extension dưới 0.3.4 lấy mã reCAPTCHA theo cách cũ mà Flow đã từ chối — mọi lệnh tạo ảnh/video đều trả `PUBLIC_ERROR_UNUSUAL_ACTIVITY`. Gặp lỗi này, kiểm tra phiên bản extension trước tiên.

#### Bước 0.2: Đăng nhập Google Flow & Luôn giữ tab mở
1. Mở tab mới trên Chrome và truy cập: **https://flow.google.com/**
2. Đăng nhập tài khoản Google của bạn. Nếu vừa reload extension ở Bước 0.1, **F5 tab này**.
3. **Quy tắc vàng:** Luôn **giữ tab `flow.google.com` này mở** trong suốt quá trình tạo video.

#### Bước 0.3: (Tuỳ chọn) Lấy mã `FLOW_PROJECT_ID`
**Không bắt buộc nữa** — bỏ qua bước này là bình thường. `/fk-create-project` (`POST /api/projects`) tự tạo một project Flow mới, và các lệnh `/api/flow/*` không truyền `project_id` dùng một *session project* tự tạo.

Chỉ làm bước này khi muốn dùng lại một project Flow có sẵn:
1. Trên giao diện `flow.google.com`, bấm mở Project đó.
2. Nhìn lên URL trình duyệt: `https://flow.google.com/project/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`
3. Copy chuỗi mã UUID ở cuối URL. Chuỗi này dùng ở Bước 0.4.

#### Bước 0.4: Set biến môi trường rồi khởi động Server Python (FastAPI cổng 8100)
Server chỉ đọc biến môi trường **một lần lúc khởi động**. Vì vậy phải set **trước** khi chạy server, và **trong cùng một cửa sổ terminal** (`$env:` / `export` chỉ có hiệu lực trong terminal đó). Chạy đúng thứ tự sau tại thư mục gốc dự án (`c:\flowkit`):
- **Windows PowerShell:**
  ```powershell
  .\venv\Scripts\python.exe -m pip install -r requirements.txt   # mỗi lần pull code mới
  $env:FLOW_PROJECT_ID="uuid-copy-từ-URL-flow"                    # tuỳ chọn — bỏ dòng này nếu không làm Bước 0.3
  $env:FLOW_ALLOW_DEGRADED="1"
  .\venv\Scripts\Activate.ps1
  python -m agent.main
  ```
- **macOS / Linux / Git Bash:**
  ```bash
  venv/bin/python -m pip install -r requirements.txt   # mỗi lần pull code mới
  export FLOW_PROJECT_ID="uuid-copy-từ-URL-flow"      # tuỳ chọn — bỏ dòng này nếu không làm Bước 0.3
  export FLOW_ALLOW_DEGRADED="1"
  source venv/bin/activate
  python -m agent.main
  ```
- `FLOW_PROJECT_ID` (tuỳ chọn): uuid project Flow lấy ở Bước 0.3, dùng làm project mặc định cho các lệnh nội bộ cũ. Muốn một project FlowKit gắn vào project Flow có sẵn thì truyền `flow_project_id` khi tạo project.
- `FLOW_ALLOW_DEGRADED="1"`: **chỉ nhận đúng `1`** — `"true"` bị coi là tắt. Cho phép Veo chaining (start+end frame) và Veo r2v hạ xuống i2v thường (từ ảnh ref đầu tiên) thay vì báo `UNSUPPORTED_ON_BATCH_API`. r2v thật (nhiều ref) chạy qua Omni Flash `abra_r2v_<N>s`: `/api/flow/generate-video-omni` hoặc `model_family=omni_flash`. *(Lưu ý: bước r2v trong `/fk-pipeline` — request `GENERATE_VIDEO_REFS` — chưa được nối lại vào Omni sau lần merge upstream, nên hiện chưa chạy được.)*

Kiểm tra server đã nhận đúng cấu hình:
```powershell
curl.exe -s http://127.0.0.1:8100/api/flow/status
# "allow_degraded": true              — nếu false là chưa set FLOW_ALLOW_DEGRADED="1" trước khi chạy server
# "flow_project_id": "<uuid>" hoặc null — null là bình thường nếu bỏ qua Bước 0.3
# "generation_throttle": {"cooldown_active": false, ...}
```

> [!NOTE]
> **Đổi project / đổi biến môi trường / pull code mới:** set lại `$env:` khi server đang chạy **không có tác dụng**. Phải tắt server (`Ctrl+C`), set lại biến, rồi chạy lại `python -m agent.main`.
>
> **Lỗi cổng 8100:** Nếu terminal báo `address already in use` hoặc tự tắt ngay, nghĩa là đã có một server FlowKit chạy ngầm từ trước. Kiểm tra `curl.exe -s http://127.0.0.1:8100/api/flow/status`. Nếu `allow_degraded` / `flow_project_id` đã đúng thì dùng tiếp server đó. Nếu sai, tắt server cũ rồi làm lại bước này.
>
> **UNUSUAL_ACTIVITY:** FlowKit tự dừng gửi 120s (trả 429) và không tự thử lại request đó. Đừng gửi dồn lại — kiểm tra extension ≥ 0.3.4 rồi gửi lại thủ công.

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
{"status": "ok", "extension_connected": true, "ws": {"extension_versions": ["0.3.4"], ...}}
```
Khi thấy `"extension_connected": true` và `extension_versions` từ `0.3.4` trở lên, toàn bộ hệ thống cầu nối đã thông suốt và sẵn sàng chạy các bước kịch bản bên dưới!

#### Bước 0.6: Mở Web Dashboard Trực Quan (Khuyên Dùng)
Để theo dõi trực quan danh sách dự án, tiến độ sinh video, thư viện Gallery ảnh/video và logs hệ thống theo thời gian thực thay vì chỉ nhìn terminal:
1. Mở một terminal mới:
   ```bash
   cd c:\flowkit\dashboard
   npm install        # Chỉ cần chạy lần đầu tiên
   npm run dev
   ```
2. Mở trình duyệt truy cập:
   👉 **http://localhost:5173**
*(Dashboard tự động kết nối và đồng bộ hai chiều với Server Python cổng 8100).*

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

### BƯỚC 4.5: Kiểm Duyệt Video Trực Quan Với Scene Review Board (`/fk-review-board`)

Trước khi xuất bản hoặc khi muốn kiểm tra kỹ chất lượng video từng cảnh (xem cử động, nét mặt nhân vật, chuyển cảnh), bạn sử dụng **Scene Review Board**:

- **Cách 1: Dùng lệnh nhanh**
  ```bash
  /fk-review-board
  ```
- **Cách 2: Chạy trực tiếp qua Python** *(Lưu ý: Chạy từ thư mục gốc `c:\flowkit`, không đứng ở thư mục `dashboard/`)*
  ```bash
  python tools/review_server.py
  ```
  Sau đó mở trình duyệt:
  👉 **http://localhost:8200?video_id=<ID_VIDEO>**

**Các tính năng nổi bật trên Review Board:**
1. **Xem video inline theo chuỗi cảnh (Scene Chains)**: Bấm phát từng video clip trực tiếp trên giao diện storyboard trực quan.
2. **Gắn nhãn phân loại (Tagging)**:
   - **`OK`**: Cảnh hoàn hảo, giữ nguyên để nối video cuối.
   - **`Regen Video`**: Cử động nhân vật bị méo hoặc lỗi chuyển động $\rightarrow$ Yêu cầu sinh lại video.
   - **`Regen Image`**: Ảnh tĩnh ban đầu bị sai chi tiết $\rightarrow$ Yêu cầu vẽ lại ảnh.
   - **`Edit`**: Cần chỉnh sửa câu lệnh prompt.
3. **Ghi chú & Tự động sửa lỗi**: Gõ phản hồi trực tiếp cho từng cảnh và bấm **Export Feedback** (`tools/review_feedback.json`) để Agent tự động tạo lại các cảnh lỗi mà không cần gõ lệnh thủ công.

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

# 0. Kiểm tra kết nối & Khởi động Web Dashboard:
curl.exe -s http://127.0.0.1:8100/health
cd dashboard && npm run dev           # Mở http://localhost:5173

# 1. Nghiên cứu tư liệu lịch sử:
/fk-research "Kamakura period 1274 AD samurai defense mongol invasion"

# 2. Khởi tạo dự án & 10 phân cảnh:
python scripts/create_kamakura_1274.py

# 3. Nạp ảnh mặt thật (tùy chọn):
/fk-upload-ref "C:/photos/my_face.jpg" --entity "Vlogger"

# 4. Chạy toàn bộ pipeline tự động (R2V + TTS + Concat + SEO + Thumbnails):
/fk-pipeline --r2v --tts --concat

# 4.5. Mở bảng kiểm duyệt storyboard / video:
/fk-review-board                      # Hoặc: python tools/review_server.py -> Mở http://localhost:8200

# 5. Xuất bản YouTube:
/fk-youtube-upload --privacy unlisted --thumbnail 1
```
