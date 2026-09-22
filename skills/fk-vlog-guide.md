# fk-vlog-guide — Master Guide & Interactive Hub for Historical POV Vlogs

Cẩm nang điều phối trọn gói quy trình sản xuất Video Vlog Du Hành Lịch Sử / POV Time Travel từ A đến Z, kèm bảng lựa chọn (Options Menu) cho từng giai đoạn từ nghiên cứu, kịch bản, nạp mặt thật, chạy pipeline đến xuất bản YouTube.

---

## 🧭 BẢNG ĐIỀU PHỐI QUY TRÌNH (PRODUCTION HUB)

Khi bạn muốn sản xuất một tập vlog mới, hãy thực hiện tuần tự qua 5 bước sau:

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ 1. NGHIÊN CỨU DỮ KIỆN (Fact-Check)      ➔ /fk-research                      │
│ 2. TẠO KỊCH BẢN & KHÓA MỸ THUẬT         ➔ python scripts/create_...py       │
│ 3. NẠP ẢNH MẶT THẬT (Tùy chọn)          ➔ /fk-upload-ref                    │
│ 4. CHẠY PIPELINE TỰ ĐỘNG (All-in-One)   ➔ /fk-pipeline --r2v --tts --concat │
│ 5. XEM LẠI & ĐĂNG TẢI YOUTUBE           ➔ /fk-youtube-upload                │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 📌 CHI TIẾT TỪNG BƯỚC & CÁC LỰA CHỌN (OPTIONS)

### BƯỚC 0: Nghiên Cứu Dữ Kiện Lịch Sử (`/fk-research`)
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

### BƯỚC 1: Khóa Mỹ Thuật & Tạo Kịch Bản
1. **Khóa chất liệu mỹ thuật**: Luôn đặt `material: "realistic"` để giữ hình ảnh và video chân thực như máy ảnh tư liệu đời thực, không bị biến thành anime hay hoạt hình.
2. **Quy chuẩn góc máy Veo 3 ([`/fk-camera-guide`](file:///c:/flowkit/skills/fk-camera-guide.md))**:
   - Cầm camera selfie trước góc rộng 24–28mm.
   - Khẩu độ Pan-Focus f/8–f/11 (nét sâu từ mặt vlogger đến cảnh chợ phía sau, zero bokeh).
   - Kỹ thuật **vừa đi vừa quay (Walking POV)**: camera nảy nhẹ theo bước chân, tạo hiệu ứng trôi cảnh 3D parallax sống động.
3. **Nạp kịch bản vào FlowKit**:
   ```bash
   # Dùng script mẫu Heian 1000 có sẵn:
   python scripts/create_kyoto_heian_1000.py
   ```

---

### BƯỚC 2: Nạp Ảnh Mặt Thật Của Bạn (`/fk-upload-ref`)
Nếu bạn muốn đóng vai Vlogger chính trong chuyến du hành thay vì để AI tự tạo mặt:
```bash
/fk-upload-ref "C:/photos/my_face.jpg" --entity "Vlogger"
```
- **Tự động khóa nhận diện**: Ảnh thật được đẩy lên Google Flow và gán mã UUID `media_id` vào nhân vật.
- **Bảo toàn 100%**: AI sẽ bỏ qua việc vẽ mặt ảo và dùng chính ảnh này làm khuôn mẫu cho tất cả các góc quay.

---

### BƯỚC 3: Chạy Trọn Gói Pipeline (`/fk-pipeline`)
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

### BƯỚC 4: Bảng Lựa Chọn Xuất Bản YouTube (`/fk-youtube-upload`)

Sau khi pipeline hoàn tất, bạn kiểm tra thư mục `output/<slug>/` và tiến hành xuất bản theo các tùy chọn dưới đây:

#### Bảng Tùy Chọn Upload (Options Menu):

| Tùy chọn | Lệnh thực hiện | Ý nghĩa |
| :--- | :--- | :--- |
| **1. Duyệt trước an toàn (Recommended)** | `/fk-youtube-upload --privacy unlisted` | Đăng video ở chế độ **Không công khai (Unlisted)** để bạn xem thử chất lượng và kiểm tra bản quyền trên YouTube Studio trước khi công khai. |
| **2. Đăng công khai ngay** | `/fk-youtube-upload --privacy public` | Đăng video công khai (Public) lập tức tới người xem. |
| **3. Chọn ảnh Thumbnail** | `/fk-youtube-upload --thumbnail 2` | Chọn biến thể thumbnail yêu thích (từ 1 đến 4 trong thư mục `thumbnails/`) làm ảnh đại diện chính. |
| **4. Hẹn giờ đăng tải (Schedule)** | `/fk-youtube-upload --schedule "19:00"` | Hẹn giờ đăng vào khung giờ vàng (12:00 trưa hoặc 19:00 tối). |
| **5. Xem trước không upload (Dry-run)** | `/fk-youtube-upload --dry-run` | In toàn bộ thông tin (Tiêu đề, mô tả, tags, đường dẫn video, thumbnail) ra màn hình để kiểm tra trước. |

---

## 🎯 DANH SÁCH CÂU LỆNH TẮT ĐỂ COPY NHANH

```bash
# Toàn bộ quy trình rút gọn:
/fk-research "Heian-kyo daily life 1000 AD"
python scripts/create_kyoto_heian_1000.py
/fk-upload-ref "C:/photos/my_face.jpg" --entity "Vlogger"
/fk-pipeline --r2v --tts --concat
/fk-youtube-upload --privacy unlisted --thumbnail 1
```
