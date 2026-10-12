# CẨM NANG HƯỚNG DẪN FLOWKIT DÀNH CHO NGƯỜI MỚI (BEGINNER'S GUIDE)
## Quy Trình Sản Xuất Video Vlog Du Hành Lịch Sử / POV Time-Travel Từ A Đến Z

---

## 🌟 1. TỔNG QUAN: FLOWKIT HOẠT ĐỘNG NHƯ THẾ NÀO?

FlowKit là hệ thống tự động hóa toàn diện quy trình sản xuất video điện ảnh AI — đặc biệt chuyên sâu cho thể loại **POV Time-Travel Vlog** (Vlogger hiện đại du hành quá khứ, tự cầm máy sinh tồn giữa các nền văn minh cổ đại hoặc tiền sử).

Toàn bộ quá trình đi qua **2 giai đoạn lớn**:
1. **Giai đoạn Tiền kỳ (Pre-Production):** Đi qua **Kiến trúc 3 tầng tài liệu** (từ Ý tưởng $\to$ `story-bible.md` $\to$ `script.md` $\to$ `prompts_actX.json` + `vn.json`).
2. **Giai đoạn Sản xuất Media (FlowKit Production):** Kết nối Google Flow qua Chrome Extension $\to$ Tạo Reference sạch logo $\to$ Sinh video R2V $\to$ AI Review & Duyệt $\to$ Upscale 1080p $\to$ Concat hoàn thiện.

---

## 🏛️ 2. KIẾN TRÚC TIỀN KỲ 3 TẦNG: STORY-BIBLE VÀ SCRIPT TẠO TỪ ĐÂU?

Rất nhiều người mới thắc mắc: *"`story-bible.md` và `script.md` từ đâu sinh ra? Skill nào làm việc này?"*  
Dưới đây là sơ đồ phân công chuẩn mực của hệ thống:

```text
                     [Ý TƯỞNG CỦA BẠN]
             (Ví dụ: "Rome năm 79 AD", "Hell Creek 66 Ma")
                            │
                            ▼
┌───────────────────────────────────────────────────────────────────────────┐
│ TẦNG 1: story-bible.md  (SSOT Chiến Lược Cốt Truyện)                      │
│ ── Skill điều phối: /sw-workflow                                         │
│ ── Các skill con tham gia:                                                │
│    • /sw-premise-theme: Xây dựng Premise, Theme, Misbelief của Vlogger     │
│    • /sw-story-structure: Khung 5 Act 起承转合, 12 mốc giờ đếm ngược     │
│    • /sw-character-conflict: Want vs Need của Nora, mối quan hệ thế giới  │
│ ── Output: output/<slug>/story-bible.md                                   │
└───────────────────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌───────────────────────────────────────────────────────────────────────────┐
│ TẦNG 2: script.md  (SSOT Phân Cảnh, Storyboard & Đạo Diễn)                │
│ ── Skill điều phối: /sw-scene-craft + /sw-dialogue                        │
│ ── 5 Subagent điện ảnh chuyên trách (BẮT BUỘC theo Rule 50):              │
│    • fk-action-choreography: Rà soát vật lý, tách chuỗi 4s a/b/c cảnh khó │
│    • fk-camera-guide: Chọn góc quay (POV, Selfie, Fixed) theo hành động   │
│    • fk-cinematic-transitions: Thiết kế chuyển cảnh match-on-action, whip │
│    • fk-gen-narrator: Chuẩn hóa số từ thoại Nora theo Rule 49             │
│    • fk-add-material: Cấu hình Material hình ảnh (chuẩn prehistoric/era)  │
│ ── Output: output/<slug>/script.md (Gồm §9 Storyboard & §10 Bảng vật lý) │
└───────────────────────────────────────────────────────────────────────────┘
                            │
                            ⛔ [CỔNG DUYỆT 1]: Bạn duyệt kịch bản script.md
                            │
                            ▼
┌───────────────────────────────────────────────────────────────────────────┐
│ TẦNG 3: prompts_actX.json + vn.json  (Prompt Kỹ Thuật Cho Model AI)      │
│ ── Skill bắt buộc: /fk-script-to-prompts (RULE 56 - KHÓA CỨNG)           │
│ ── Quy trình tự động:                                                     │
│    1. Đọc script.md §9 (giữ nguyên 100% lời thoại gốc, không tự chế)      │
│    2. Đọc script.md §10 (bảng vật lý)                                     │
│    3. Xuất JSON phân cấp 9 khối chuẩn kiến trúc Veo 3 / Omni Flash        │
│    4. Tự động chạy tools/lint_prompt.py kiểm toán cấm ghost phone/device  │
│    5. Tự sửa lỗi (Self-Repair) đến khi đạt 0 lỗi (PROMPT LINT PASSED)     │
│    6. Xuất kèm bản dịch tiếng Việt tự nhiên vn.json                       │
│ ── Output: output/<slug>/prompts_act1.json ... & vn.json                 │
└───────────────────────────────────────────────────────────────────────────┘
                            │
                            ⛔ [CỔNG DUYỆT 2]: Bạn duyệt prompt trước khi gen video
```

## 🎨 2.5 BƯỚC BẮT BUỘC: NGHIÊN CỨU CHẤT LIỆU & SOẠN PROMPT ẢNH REF TRƯỚC KHI GEN
Rất nhiều người mới mắc sai lầm là nhảy thẳng vào bấm sinh ảnh, dẫn đến ảnh AI bị generic, khủng long trông như đồ chơi nhựa CGI hoặc bối cảnh sai lệch thời kỳ.  
**Quy trình chuẩn hóa bắt buộc phải có bước này trước khi bấm nút sinh media:**

```text
┌───────────────────────────────────────────────────────────────────────────┐
│ BƯỚC 2.5: THIẾT KẾ & DUYỆT PROMPT ẢNH REFERENCE                           │
│ 1. /fk-research: Nghiên cứu địa chất, thực vật, giải phẫu sinh vật học    │
│ 2. /fk-add-material: Khóa chất liệu (style_instruction, negative_prompt,  │
│    lighting) để ảnh trông như phim tài liệu thực tế, cấm 100% CGI/3D      │
│ 3. Soạn thảo file ref_prompts.json: Chốt chi tiết từng câu prompt cho:     │
│    • Nora Body: Turnaround Sheet 16:9 đã mặc hoàn chỉnh trang phục         │
│    • Nora Hand (16:9): Cận cảnh cẳng tay & bàn tay vlogger cho shot POV    │
│      tương tác (nhặt đồ, vốc nước, gạt cành) tránh lỗi tay đàn ông (Bài 72)│
│    • Bối cảnh (16:9): Không người, không thước đo (Rule 34)                │
│    • Sinh vật / Đạo cụ (16:9): Chuẩn giải phẫu, da sần, bùn đỏ            │
│ 4. ⛔ [CỔNG DUYỆT PROMPT REF]: Trình danh sách Prompt Ref cho Bạn duyệt!   │
└───────────────────────────────────────────────────────────────────────────┘
```

---

## 🎬 3. GIAI ĐOẠN SẢN XUẤT MEDIA: TỪ PROMPT RA VIDEO HOÀN CHỈNH

Sau khi bạn duyệt danh sách Prompt Reference và Kịch bản, quá trình sản xuất trên Google Flow diễn ra tuần tự:

### Bước 1: Chuẩn bị môi trường (Pre-Flight)
1. **Google Chrome:** Cài Chrome Extension bản `≥ 0.5.2` (tại thư mục `c:\flowkit\extension`), bật *Developer Mode*.
2. **Mở tab Flow:** Truy cập `https://flow.google.com/`, đăng nhập và **luôn giữ tab này mở**.
3. **Khởi động Server Python:** Mở terminal PowerShell tại `c:\flowkit`:
   ```powershell
   .\venv\Scripts\Activate.ps1
   python -m agent.main
   ```
   *(Server chạy tại cổng `http://127.0.0.1:8100`).*

### Bước 2: Sinh Ảnh Reference & Tẩy Watermark AI (Rule 28, 33, 46)
- Gửi các prompt trong `ref_prompts.json` lên Flow để sinh ảnh 16:9.
- **Quy trình tẩy watermark bắt buộc (Rule 28):** Mọi ảnh AI sinh ra từ Flow đều có logo chìm. Agent sẽ:
  `Tải ảnh về máy` $\to$ `Chạy tools/remove_watermark_from_image.py` $\to$ `Upload ngược lên Flow lấy UUID sạch`.
- Bạn mở gallery ảnh để duyệt start frame & entity ref trước khi sinh video.

### Bước 3: Sinh Video R2V Omni Flash (`abra_r2v`)
- Tuyệt đối **không sinh Start Frame** rồi chạy `i2v` (làm đơ mặt và méo người).
- Sử dụng trực tiếp `GENERATE_VIDEO_REFS` với model `abra_r2v_<duration>s`.
- Tích hợp sẵn khẩu hình tự nhiên theo giọng **Laomedeia** (Slot 7).

### Bước 4: AI Review & Duyệt Video trên Review Board (Rule 18, 32)
- Khi video 720p sinh xong, Agent tải về máy nhưng **chưa xóa logo vội** (tiết kiệm tài nguyên).
- Chạy tự động `/fk-review-video` chấm điểm theo 6 tiêu chuẩn cốt lõi (nhận diện nhân vật, bám sát prompt, vật lý chuyển động...).
- Khởi động Review Board:
  ```powershell
  python tools/review_server.py 8200
  ```
- Bạn mở trình duyệt vào `http://127.0.0.1:8200` để xem trực quan từng clip.

### Bước 5: Upscale 1080p, Tẩy Logo Video & Concat Hoàn Chỉnh
- Chỉ những clip **bạn đã duyệt thông qua**: Gửi lệnh Upscale 1080p (`veo_3_1_upsampler_1080p`).
- Chạy công cụ xóa watermark trên file 1080p: sinh ra file `scene_XXX_1080p_clean.mp4`.
- Concat toàn bộ clip, lồng âm thanh foley/nhạc nền ducking theo chuẩn YouTube (-14 LUFS).

---

## 🚀 4. HƯỚNG DẪN BẮT ĐẦU NHANH CHO NGƯỜI MỚI (QUICKSTART)

### Cách 1: Bắt đầu một tập Vlog mới bằng 1 câu lệnh duy nhất
Bạn chỉ cần nhắn cho AI:
> *"Làm tập time travel vlog: Thành Rome năm 79 AD (trước khi núi lửa Vesuvius phun trào)"*

**AI sẽ tự động làm gì?**
1. Tự kích hoạt `/fk-time-travel-vlog`.
2. Tự gọi bộ skill `sw-*` tạo `output/rome-79ad/story-bible.md` (Tầng 1).
3. Tự phối hợp 5 subagents điện ảnh tạo `output/rome-79ad/script.md` (Tầng 2).
4. Dừng lại báo cáo bạn để duyệt kịch bản trước khi làm tiếp!

---

### Cách 2: Làm từng bước có kiểm soát (Step-by-Step)

| Bước | Bạn gõ / yêu cầu | AI sẽ thực hiện |
|---|---|---|
| **1. Ý tưởng & Bible** | `Tạo story-bible cho tập Ai Cập cổ đại năm 2500 BC xây Kim Tự Tháp` | Gọi `/sw-workflow` viết `story-bible.md` (Premise, 5 Act, 12 mốc giờ). |
| **2. Viết Kịch Bản** | `Viết script.md chi tiết cho tập này` | Gọi 5 Subagent điện ảnh viết §9 Storyboard và §10 Bảng vật lý. |
| **3. Chuyển thành Prompt** | `Dùng skill /fk-script-to-prompts chuyển Act 1 sang JSON prompt` | Chuyển kịch bản thành `prompts_act1.json`, tự chạy `lint_prompt.py` self-repair 0 lỗi. |
| **4. Kiểm tra Prompt** | `Chạy kiểm tra prompt file prompts_act1.json` | Chạy lệnh `python tools/lint_prompt.py --file ...` báo cáo kết quả. |
| **5. Chuẩn bị Dự Án** | `Tạo FlowKit project cho tập này` | Tạo project và scenes trên FlowKit server. |
| **6. Tạo Ảnh Nhân Vật** | `Tạo bộ ref cho Nora và bối cảnh` | Sinh ảnh, xóa logo, upload lấy UUID sạch. |
| **7. Sinh Video** | `Sinh video cho Act 1` | Hỏi xác nhận credit $\to$ Sinh video R2V Omni Flash. |
| **8. Xem Review** | `Mở Review Board xem video` | Chạy `python tools/review_server.py 8200`. |

---

## ❓ 5. BẢNG GIẢI ĐÁP CÁC LỖI THƯỜNG GẶP (FAQ & TROUBLESHOOTING)

### 1. Tại sao AI vẽ ra chiếc điện thoại / gậy selfie bay lơ lửng?
- **Nguyên nhân:** Trong prompt có chữ `phone`, `smartphone`, `device`, `screen` hoặc `phone_vlog` (kể cả câu cấm "no phone").
- **Cách xử lý:** Hệ thống đã có **Rule 35, 40** và tool `tools/lint_prompt.py`. Linter sẽ chặn đứng 100% các từ này và ép dùng ràng buộc quang học rảnh tay: *"The camera lens and viewpoint are completely outside the visible frame; both hands are empty."*

### 2. Lỗi `PUBLIC_ERROR_UNUSUAL_ACTIVITY` hoặc `[HIJACK]` trên server Flow là gì?
- **Nguyên nhân:** Gửi request quá dồn dập hoặc Chrome Extension chưa cập nhật lên bản `0.5.2`.
- **Cách xử lý:**
  1. Kiểm tra Chrome Extension tại `chrome://extensions` đã nạp bản `0.5.2` chưa (bấm nút Reload xoay tròn).
  2. F5 lại tab `https://flow.google.com/`.
  3. Server FlowKit đã tự động giãn cách mỗi request từ **45–60 giây** (Rule 10) để tránh bị Google chặn.

### 3. Tại sao không sinh ảnh Start Frame rồi bấm tạo video?
- **Nguyên nhân:** Sinh start frame rồi chạy i2v khiến AI cố định điểm ảnh ban đầu, khi nhân vật chuyển động sẽ bị méo mặt, co giật cơ thể và đơ chuyển động.
- **Cách xử lý chuẩn (Rule 27):** Dùng trực tiếp **Omni Flash Ingredients (`abra_r2v`)**, chỉ truyền ảnh Mặt + ảnh Body đã mặc outfit vào để model tự diễn xuất mượt mà.

### 4. Muốn xem lại các bài học sản xuất thực tế thì xem ở đâu?
- Toàn bộ 71+ bài học xương máu được tổng hợp tại:
  `skills/fk-time-travel-vlog/references/production-lessons.md`
- Checklist cấu trúc câu chữ prompt tại:
  `skills/fk-time-travel-vlog/references/prompt-lock.md`
