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

## 2. Đóng Gói YouTube — Tiêu Đề `| Full Movie 4K`, Thumbnail Không Chữ & SEO Khai Báo AI (Bước 1.5 & Bước 11 — User Lock 24/10/2026)

- **Chốt Gói Mở Đầu Trước Khi Viết Kịch Bản (Bước 1.5 — `/fk-scriptwriter` §G2, `/fk-thumbnail-guide`, `/fk-youtube-seo`)**:
  - 3 phương án Tiêu đề chuẩn ZOVEN STUDIOS + 4 phương án Thumbnail điện ảnh không chữ + Câu mở đầu 5 giây + Lời hứa 30 giây đã được chốt từ tiền kỳ phải khớp 100% với thành phẩm cuối cùng.
- **Công Thức Tiêu Đề Phim Điện Ảnh (`| Full Movie 4K` — BẮT BUỘC dù video là 1080p)**:
  - Cấu trúc 3 vế ngăn cách bằng dấu `|`:
    `[TÊN PHIM NGẮN VIẾT HOA TOÀN BỘ] | [Câu Hook Cốt Truyện High-Stakes Có 1 Từ Nhấn Mạnh VIẾT HOA] | Full Movie 4K`
  - Ví dụ: `THE WARNING | An Alien Came to Earth to SAVE Us From Her Own People | Full Movie 4K` hoặc `THE GOLDEN CURSE | A Pirate Crew Cut Open a Giant Fish and Found What SANK 50 Ships | Full Movie 4K`.
  - **Mặc dù chất lượng file video xuất ra là 1080p (chưa phải 4K), LUÔN LUÔN giữ hậu tố `| Full Movie 4K` trên tiêu đề.**
- **Mô Tả (Description) Chuẩn Điện Ảnh + BẮT BUỘC Nêu Rõ Phim Được Sản Xuất Bằng AI (`/fk-youtube-seo`)**:
  - Mở đầu Zone 1 bằng 3 đoạn văn ngắn cách dòng giàu kịch tính (Đoạn 1: Bối cảnh nhân vật chính $\to$ Đoạn 2: `"Then, one night, ..."` biến cố ập đến $\to$ Đoạn 3: Phát hiện kỳ dị bên trong & cảnh báo sinh tử).
  - Ngay dưới phần mở đầu phải có dòng **Khai báo sản xuất bằng AI (`🎬 AI PRODUCTION DISCLOSURE` / `🎬 THÔNG TIN SẢN XUẤT AI`)** nêu rõ bộ phim được sản xuất bằng AI (hình ảnh, giọng nói, âm thanh) và toàn bộ nhân vật/sự kiện là hư cấu.
- **Thiết Kế Thumbnail Điện Ảnh 35mm Thuần Khiết — TUYỆT ĐỐI KHÔNG CÓ CHỮ (`/fk-thumbnail-guide`, `/fk-thumbnail`)**:
  - **ZERO TEXT ON THUMBNAIL (`strictly NO text, NO words, NO letters, NO typography, NO titles, NO logos`)**: Không bao giờ đưa bất kỳ chữ viết nào lên ảnh Thumbnail.
  - Bố cục khung hình phim 35mm (ZOVEN STUDIOS style): Nhân vật chính cầm nguồn sáng thực tế (đèn bão, đuốc) chiếu sáng phát hiện kỳ dị hoặc mối nguy hiểm trong bóng tối sương mù xanh lạnh (tương phản ấm – lạnh cực mạnh), xóa sạch watermark bằng `remove_watermark_from_image.py` trước khi resize về `1280x720`.
- **Ngôn ngữ đồng nhất (Rule 20) & Nhãn AI trên YouTube Studio**:
  - Toàn bộ metadata (`/fk-youtube-seo`) khớp 100% với ngôn ngữ thoại của bộ phim.
  - Bật nhãn *"AI use" / "Altered or synthetic content"* khi đăng tải qua `/fk-youtube-upload` / YouTube Studio.

---

## 3. Chiến Lược Phát Hành Đa Kênh & Chẩn Đoán Sau Đăng (`/fk-youtube-analytics`)

1. **Cắt 3–4 YouTube Shorts (9:16, 15–35s) kéo traffic mồi (`/video-editing` + `/fk-capcut-edit`)**:
   - Trích xuất các phân đoạn cao trào nhất từ bộ phim (cảnh phát hiện sinh vật kỳ dị, cảnh vượt cạm bẫy sinh tử, cảnh đối đầu quái thú) sang khung dọc 9:16 có tiêu điểm thông minh (*smart reframe*).
   - Gắn liên kết **Related Video** trong YouTube Studio trỏ trực tiếp về bộ phim dài.
2. **Kiểm toán chỉ số sau 48 giờ và 7 ngày (`/fk-youtube-analytics`)**:
   - Theo dõi 3 chỉ số cốt lõi: **CTR** (mục tiêu $\ge 6\%$), **Giữ chân 30s đầu** (mục tiêu $\ge 65\%$), và **AVD** (thời lượng xem trung bình).
   - Nếu CTR thấp hơn kỳ vọng: áp dụng quy tắc **đổi 1 biến mỗi lần** (thay phương án Thumbnail dự phòng trước, theo dõi 48h rồi mới đổi phương án Tiêu đề).
