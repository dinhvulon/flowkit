# Hậu Kỳ Điện Ảnh, Đóng Gói YouTube & Chiến Lược Phát Hành

> **Quy chuẩn `/fk-film`:** Đọc ở **Bước 10–11** của `SKILL.md`. Sau khi toàn bộ các cảnh đã được duyệt, upscale lên 1080p và xóa sạch watermark (`output/<slug>/1080/*_1080p_clean.mp4`), bắt buộc phối hợp bộ skill hậu kỳ và phát hành: **`/video-editing` (Rule 66)**, **`/fk-capcut-edit`**, **`/fk-cinematic-transitions`**, **`/fk-sound-design`**, **`/fk-concat`**, **`/fk-youtube-seo`**, **`/fk-thumbnail-guide`**, **`/fk-thumbnail`**, **`/fk-youtube-upload`**, và **`/fk-youtube-analytics`**.

---

## 1. Dựng Hậu Kỳ & Hòa Âm Điện Ảnh (Bước 10)

1. **Dựng hình & Nhịp cắt (`/video-editing`, `/fk-capcut-edit`, `/fk-cinematic-transitions`)**:
   - Cắt bỏ hoàn toàn khoảng chết (*dead air*) ở đầu và cuối mỗi clip AI.
   - Đảm bảo nhịp thay đổi hình ảnh mỗi **3–5 giây** (kết hợp các cú `crisp hard cut` bên trong từng clip 8s/10s đã thiết kế từ Storyboard 2×2 và các điểm cắt nối cảnh).
   - Áp dụng **J-cut / L-cut** (âm thanh cảnh sau vào sớm `0.3–0.5s` hoặc âm thanh cảnh trước ngân sang cảnh sau) để tạo dòng chảy điện ảnh mượt mà.
   - Xây dựng **Intro Trailer Montage (15–30s đầu)** nếu làm phim dài trên YouTube theo quy chuẩn giữ chân người xem của `/fk-capcut-edit`.
2. **Thiết kế âm thanh & Mastering (`/fk-sound-design`, `/fk-gen-music`)**:
   - Tách bạch 3 lớp âm thanh: (1) Thoại nhân vật (`speech`) cộng hưởng với các câu `post_vo` (nếu có); (2) Foley & Ambient hiện trường (tiếng sóng vỗ, gỗ tàu cọt kẹt, kiếm chạm, đá lở); (3) Nhạc nền giao hưởng/nhạc cụ cổ điển theo thời kỳ (`/fk-gen-music`), tự động hạ âm lượng (*sidechain ducking*) khi có thoại.
   - Chuẩn hóa âm lượng toàn phim đạt chuẩn phát sóng quốc tế **−14 LUFS** và giới hạn đỉnh **−1 dBTP**.
3. **Đồng bộ màu sắc & Chất phim 35mm (`/fk-brand-logo`, `/fk-concat`)**:
   - Phủ lớp color grade và hạt phim (*subtle 35mm film grain*) đồng nhất để xóa nhòa ranh giới màu sắc giữa các clip sinh rời:
     ```bash
     ffmpeg -i final_raw.mp4 -vf "colorbalance=rs=0.03:bs=-0.03,noise=alls=4:allf=t" -c:a copy final_graded.mp4
     ```
   - Xuất file phụ đề `.srt` rời chuẩn xác (không burn hardsub đè lên khung hình điện ảnh trừ khi User yêu cầu).

---

## 2. Đóng Gói YouTube — Tiêu Đề, Thumbnail & SEO (Bước 1.5 & Bước 11)

- **Chốt Gói Mở Đầu Trước Khi Viết Kịch Bản (Bước 1.5 — `/fk-scriptwriter` §G2 & `/fk-thumbnail-guide`)**:
  - 3 phương án Tiêu đề + 4 phương án Thumbnail + Câu mở đầu 5 giây + Lời hứa 30 giây đã được chốt từ tiền kỳ phải khớp 100% với thành phẩm cuối cùng.
- **Ngôn ngữ đồng nhất (Rule 20)**:
  - Toàn bộ metadata (`/fk-youtube-seo`) và chữ trên Thumbnail (`/fk-thumbnail`) phải khớp 100% với ngôn ngữ thoại/kịch bản của bộ phim.
- **Thiết kế Thumbnail Điện Ảnh High-Stakes (`/fk-thumbnail-guide`, `/fk-thumbnail`)**:
  - Bố cục 3 điểm: Biểu cảm nhân vật chính sắc nét trước hiểm nguy khổng lồ (quái thú biển, cổng đá sập, bão lửa) + Tương phản màu sắc mạnh + Text ngắn gọn 2–4 từ gợi sự tò mò tột độ.
  - Xuất bản 16:9 cho video dài và 9:16 cho Shorts.
- **Nhãn nội dung AI trên YouTube Studio**:
  - Bật nhãn *"Altered or synthetic content"* khi đăng tải qua `/fk-youtube-upload` / YouTube Studio.

---

## 3. Chiến Lược Phát Hành Đa Kênh & Chẩn Đoán Sau Đăng (`/fk-youtube-analytics`)

1. **Cắt 3–4 YouTube Shorts (9:16, 15–35s) kéo traffic mồi (`/video-editing` + `/fk-capcut-edit`)**:
   - Trích xuất các phân đoạn cao trào nhất từ bộ phim (cảnh phát hiện sinh vật kỳ dị, cảnh vượt cạm bẫy sinh tử, cảnh đối đầu quái thú) sang khung dọc 9:16 có tiêu điểm thông minh (*smart reframe*).
   - Gắn liên kết **Related Video** trong YouTube Studio trỏ trực tiếp về bộ phim dài.
2. **Kiểm toán chỉ số sau 48 giờ và 7 ngày (`/fk-youtube-analytics`)**:
   - Theo dõi 3 chỉ số cốt lõi: **CTR** (mục tiêu $\ge 6\%$), **Giữ chân 30s đầu** (mục tiêu $\ge 65\%$), và **AVD** (thời lượng xem trung bình).
   - Nếu CTR thấp hơn kỳ vọng: áp dụng quy tắc **đổi 1 biến mỗi lần** (thay phương án Thumbnail dự phòng trước, theo dõi 48h rồi mới đổi phương án Tiêu đề).
