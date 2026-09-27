# fk-vlog-guide — Master Guide & Interactive Hub for Historical POV Vlogs

Cẩm nang điều phối trọn gói quy trình sản xuất Video Vlog Du Hành Lịch Sử / POV Time Travel từ A đến Z, kèm bảng lựa chọn (Options Menu) cho từng giai đoạn từ nghiên cứu, kịch bản, nạp mặt thật, chạy pipeline đến xuất bản YouTube.

---

## 🧭 BẢNG ĐIỀU PHỐI QUY TRÌNH (PRODUCTION HUB)

Khi bạn muốn sản xuất một tập vlog mới, hãy thực hiện tuần tự qua các giai đoạn sau:

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ 0. THIẾT LẬP MÔI TRƯỜNG & UI WEB (Pre-Flight)   ➔ /health: true & :5173     │
│ 1. NGHIÊN CỨU DỮ KIỆN (Fact-Check)              ➔ /fk-research              │
│ 2. TẠO KỊCH BẢN & SET ACTIVE PROJECT            ➔ /fk-time-travel-vlog      │
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

#### Bước 0.1: Cài / cập nhật Chrome Extension (bản ≥ 0.5.2)
1. Mở Google Chrome, gõ địa chỉ: `chrome://extensions`
2. Bật công tắc **Chế độ dành cho nhà phát triển (Developer mode)** ở góc trên bên phải.
3. Lần đầu: bấm **Tải tiện ích đã giải nén (Load unpacked)** → chọn thư mục `extension/` của dự án (`c:\flowkit\extension`). Icon **Flow Kit** sẽ xuất hiện trên thanh công cụ.
4. **Đã cài rồi mà vừa pull code mới:** bấm **↻ Reload** trên thẻ Flow Kit (Chrome không tự nạp lại), rồi kiểm tra thẻ ghi **phiên bản 0.5.2 trở lên**.

> [!IMPORTANT]
> Extension dưới 0.5.2 lấy mã reCAPTCHA theo cách cũ mà Flow đã từ chối — mọi lệnh tạo ảnh/video đều trả `PUBLIC_ERROR_UNUSUAL_ACTIVITY`. Gặp lỗi này, kiểm tra phiên bản extension trước tiên.
>
> **Vì sao cần 0.5.2 (bản upstream, commit `083fed7`, 2026-09-25):**
> - Từ khoảng cuối tháng 9/2026, trang Flow nhận ra extension can thiệp vào reCAPTCHA và đánh dấu token là `extension_hijack_detected`. Với extension cũ, mọi request vì thế đều bị từ chối. Bản 0.5.2 xử lý được việc này và nạp script theo cách tương thích với chính sách bảo mật (Trusted Types CSP) mới của trang.
> - **Hai loại lỗi phía agent:** lỗi có tiền tố `[HIJACK]` là do cơ chế nhận diện extension; agent tạm dừng **30s** và không tính vào số lần thử lại. Lỗi `UNUSUAL_ACTIVITY` **không có** `[HIJACK]` nghĩa là Google chặn phiên, tài khoản hoặc mạng; agent tạm dừng **120s** (xử lý như ở Bước 0.4).
> - Endpoint `POST /api/flow/clear-hijack` xóa thời gian chờ 30s của lỗi `[HIJACK]` bằng tay. **Chỉ dùng sau khi đã sửa nguyên nhân** (reload extension, F5 tab Flow); không dùng để gửi lại dồn dập.
> - **Rủi ro:** cách này đi ngược cơ chế Google dùng để phát hiện tự động hóa trên Flow. Tài khoản có thể bị gắn cờ hoặc hạn chế nếu bị phát hiện, và Flow có thể đổi cơ chế bất cứ lúc nào khiến bản 0.5.2 hỏng. Sau mỗi lần pull upstream, kiểm tra lại số phiên bản.

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
- `FLOW_ALLOW_DEGRADED="1"`: **chỉ nhận đúng `1`** — `"true"` bị coi là tắt. Cho phép Veo chaining (start+end frame) và Veo r2v hạ xuống i2v thường (từ ảnh ref đầu tiên) thay vì báo `UNSUPPORTED_ON_BATCH_API`. r2v thật (nhiều ref) chạy qua Omni Flash `abra_r2v_<N>s`: `/api/flow/generate-video-omni` hoặc `model_family=omni_flash`. Bước r2v trong `/fk-pipeline` (request `GENERATE_VIDEO_REFS`) cũng chạy qua Omni Flash. `N` lấy từ trường `duration` của scene (4/6/8/10), scene thiếu `duration` (tạo scene qua `POST /api/scenes` không nhận trường này) sẽ **âm thầm sinh clip 10s**, nên phải `PATCH /api/scenes/<id>` với `{"duration": 8}`.

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
> **UNUSUAL_ACTIVITY:** FlowKit tự dừng gửi 120s (trả 429) và không tự thử lại request đó. Đừng gửi dồn lại — kiểm tra extension ≥ 0.5.2 rồi gửi lại thủ công.
> **Extension đã đúng bản mà vẫn bị** (lỗi xảy ra ngay request đầu tiên, không phải do gửi dồn) thì phiên, tài khoản hoặc mạng đang bị Google gắn cờ. Thử sinh 1 ảnh trực tiếp trên giao diện `flow.google.com`. Nếu giao diện cũng bị chặn, đổi mạng (tắt VPN) hoặc đợi 1–6 giờ. Nếu giao diện sinh được, xóa cookie `google.com` + `labs.google`, đăng nhập lại, rồi chạy thử 1 request trước khi gửi cả batch.

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
{"status": "ok", "extension_connected": true, "ws": {"extension_versions": ["0.5.2"], ...}}
```
Khi thấy `"extension_connected": true` và `extension_versions` từ `0.5.2` trở lên, toàn bộ hệ thống cầu nối đã thông suốt và sẵn sàng chạy các bước kịch bản bên dưới!

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

### BƯỚC 2: Khóa Mỹ Thuật & Tạo Kịch Bản (`/fk-time-travel-vlog`)

1. **Khóa chất liệu mỹ thuật qua [`/fk-add-material`](file:///c:/flowkit/skills/fk-add-material.md)**:
   - **Khuyên dùng material tùy chỉnh `phone_vlog`** (JSON tạo material có ở mục 9 của `/fk-time-travel-vlog`). Material này giữ ảnh ref chân thực nhưng cho scene chất footage điện thoại.
   - `realistic` chỉ là phương án dự phòng: nó áp phong cách máy ảnh *Canon EOS R5, 35mm*, lệch với cảm giác "quay bằng điện thoại của nhân vật".
   - Kiểm tra các material có sẵn:
     ```bash
     curl -s http://127.0.0.1:8100/api/materials
     ```
2. **Quy chuẩn góc máy ([`/fk-camera-guide`](file:///c:/flowkit/skills/fk-camera-guide.md)), đã lọc cho format vlog điện thoại**:
   - Camera trước **góc siêu rộng 0.5x** trên gậy selfie; cánh tay hoặc gậy lọt mép khung, ống kính méo nhẹ, rung tay theo nhịp bước.
   - Tỉ lệ shot: ~65% selfie · ~15% POV thấy tay nhân vật · ~10% sau gáy · ~5% máy dựng trên bàn · ~5% toàn cảnh quay từ chỗ nhân vật đứng.
   - **Cấm** dolly, crane, gimbal glide, drone, arc shot, slow motion và bokeh điện ảnh.
   - `video_prompt` dài 100–150 từ, chia mốc `0-2s / 2-6s / 6-8s`; câu máy quay tách riêng; cuối prompt có `Audio:` / `SFX:` / `Negative:` (negative chỉ liệt kê từ khóa, không viết "no …").
   - Thoại viết dạng `Mia says: …` **không có ngoặc kép** để Veo không sinh phụ đề. Mỗi clip 8s chứa 12–18 từ và chỉ một người nói.
3. **Tạo kịch bản**:
   - Gọi **[`/fk-time-travel-vlog`](file:///c:/flowkit/skills/fk-time-travel-vlog.md)** kèm file research. Độ dài mặc định: bản dài ~10 phút ≈ 38–42 beat (76–84 scene 8s); Shorts 4–6 beat. Có thể đặt độ dài khác (ví dụ dự án Atlantis có 35 scene).
   - Kịch bản ghi vào `output/<slug>/script.md`. Clip JSON được viết theo từng hồi và **duyệt từng hồi**; chỉ dựng project FlowKit (`/fk-create-project`) sau khi duyệt toàn bộ kịch bản.

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
   /fk-pipeline <PROJECT_ID> --r2v --concat
   /fk-upload-ref "C:/photos/my_face.jpg" --project <PROJECT_ID> --entity "Vlogger"
   ```

---

### BƯỚC 3: Nạp Ảnh Mặt Thật Của Bạn (`/fk-upload-ref`)

Nếu bạn muốn đóng vai Vlogger chính trong chuyến du hành thay vì để AI tự tạo mặt:

```bash
/fk-upload-ref "C:/photos/my_face.jpg" --entity "Vlogger"
```

- **Tự động khóa nhận diện**: Ảnh thật được đẩy lên Google Flow và gán mã UUID `media_id` vào nhân vật.
- AI không vẽ mặt ảo mà dùng chính ảnh này làm khuôn mẫu cho mọi góc quay. Nên dùng **bảng nhiều góc** (chính diện, 3/4, nghiêng, sau gáy): góc sau gáy giúp các cảnh chuyển bằng quay gáy.
- **Ảnh có logo ✦ (Gemini/Flow)?** Chạy `python tools/remove_watermark_from_image.py "<ảnh>"` rồi **mở ảnh `_clean` ra kiểm tra**. Với ảnh bảng nhiều góc, tool có thể không tìm được logo (log báo `Multi-variant match low … using formula position`), vá nhầm chỗ khác và bỏ sót logo.

#### Quy tắc ref của R2V (kiểm chứng trong `agent/sdk/services/operations.py`)
| Quy tắc | Hệ quả khi viết kịch bản |
|---|---|
| Mỗi scene dùng **tối đa 3 ref**: entity `character` trước, sau đó đến `visual_asset` | `character_names` của scene chỉ nên có 1–3 tên, nhân vật chính đứng đầu |
| Entity `location` **bị bỏ qua** (chỉ dùng khi scene không có ref nào khác) | Công trình hoặc bối cảnh cần giữ nhất quán thì khai báo là `visual_asset` |
| Scene thiếu `duration` sẽ **mặc định 10s** (không báo lỗi); `POST /api/scenes` không nhận trường này | Tạo scene xong thì `PATCH` thêm `{"duration": 8}` |
| Mỗi clip chỉ có **1 giọng**, lấy từ **từ đầu tiên** của `voice_description` của entity **đầu tiên (theo thứ tự trong DB, không phải thứ tự trong `character_names`)** có khai báo voice | Viết `voice_description` bắt đầu bằng tên voice, ví dụ `Achernar — soft, …`. **Chỉ nhân vật chính có `voice_description`**, nếu không giọng nhân vật phụ sẽ đè lên thoại của nhân vật chính |

---

### BƯỚC 4: Chạy Trọn Gói Pipeline (`/fk-pipeline`)

Chỉ với một câu lệnh duy nhất, hệ thống tự động làm hết mọi khâu nặng nhọc:

```bash
/fk-pipeline --r2v --concat          # mặc định: thoại native trong video
/fk-pipeline --r2v --tts --concat    # chỉ khi muốn lồng tiếng narrator thay cho thoại native
```

> [!IMPORTANT]
> Format time-travel vlog dùng **thoại native**: vlogger nói với camera ngay trong video. Đừng thêm `--tts` mặc định, vì giọng narrator sẽ đè lên thoại có sẵn. Cũng không dùng text overlay hay crossfade khi concat.

**Các giai đoạn tự động chạy ngầm:**

1. **Model R2V (`abra_r2v_<duration>s`)**: dùng thẳng ảnh ref (nhân vật + visual asset, tối đa 3) để sinh video, không cần ảnh tĩnh Start Frame.
2. **Khẩu hình native**: Omni Flash tự sinh giọng và khẩu hình từ dòng `Mia says: …` trong `video_prompt`, với voice lấy từ `voice_description` (ví dụ Achernar).
3. **Lồng tiếng TTS** *(chỉ khi có `--tts`)*: sinh narration riêng.
4. **Xóa watermark từng clip**: tải về `scenes/`, chạy `remove_watermark_video`, rồi **mở ra kiểm tra** trước khi dùng.
5. **Ghép nối video (Concat)**: cắt thẳng tại khung che, xuất `output/<slug>/<slug>_final.mp4`.
6. **Tự động sinh YouTube SEO (`/fk-youtube-seo`)**: tiêu đề hook, mô tả, bộ tag, timestamps chapters vào `youtube_metadata.json` và `.md`.
7. **Tự động tạo 4 Thumbnail (`/fk-thumbnail`)**: ảnh đúng tỷ lệ (9:16 Shorts hoặc 16:9 long-form) lưu vào `output/<slug>/thumbnails/`.

> [!TIP]
> **Chạy thử trước 1–2 scene rủi ro** (thảm họa, chiến tranh, nghi lễ, hình phạt) trước khi gửi cả loạt. Đây là những scene dễ bị `UNSAFE_GENERATION` nhất. Chỉ ám chỉ bạo lực, và thêm `blood, gore, injured people, dead bodies` vào negative.

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

# 2. Viết kịch bản (duyệt từng hồi) rồi dựng project + scene:
/fk-time-travel-vlog .omc/research/<topic>.md     # → output/<slug>/script.md
/fk-create-project                                # sau khi đã duyệt toàn bộ kịch bản

# 3. Nạp ảnh mặt thật (tùy chọn) — xóa logo trước và mở ảnh ra kiểm tra:
python tools/remove_watermark_from_image.py "C:/photos/my_face.jpg"
/fk-upload-ref "C:/photos/my_face_clean.jpg" --entity "Vlogger"

# 4. Chạy pipeline (R2V + Concat + SEO + Thumbnails; thêm --tts chỉ khi lồng tiếng):
/fk-pipeline --r2v --concat

# 4.5. Mở bảng kiểm duyệt storyboard / video:
/fk-review-board                      # Hoặc: python tools/review_server.py -> Mở http://localhost:8200

# 5. Xuất bản YouTube:
/fk-youtube-upload --privacy unlisted --thumbnail 1
```
