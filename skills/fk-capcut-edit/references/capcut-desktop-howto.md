# CapCut Desktop — đường click cho từng thao tác

Chỉ đọc khi user hỏi một nút / thao tác nằm ở đâu (user dựng thành thạo, giao diện tiếng Anh). Tên menu đổi theo phiên bản; nếu user báo không thấy, hỏi họ đang thấy gì (hoặc xin ảnh chụp màn hình) thay vì đoán tiếp. Một số tính năng có biểu tượng Pro — báo user trước và đưa cách thay thế miễn phí.

## Mục lục
1. Bố cục màn hình
2. Project & nhập clip
3. Cắt, trim, sắp xếp
4. Zoom, punch-in, keyframe
5. Chữ & card
6. Âm thanh
7. Màu & hiệu ứng
8. Phụ đề
9. Xuất video
10. Shorts 9:16
11. Phím tắt

## 1. Bố cục màn hình
- **Trái trên**: thư viện — các tab Media, Audio, Text, Stickers, Effects, Transitions, Captions (bản cũ nằm trong Text), Filters, Adjustment.
- **Giữa trên**: trình phát (Player). Nút **Ratio** ở góc dưới trình phát để đổi tỉ lệ khung.
- **Phải trên**: bảng thuộc tính của thứ đang chọn — Video (Basic / Animation / Speed / Adjust…), Audio, Text.
- **Dưới**: timeline. Track chính ở giữa; kéo thả vào phía trên để tạo track phủ.

## 2. Project & nhập clip
- Trang chủ → **Create project**.
- Media → **Import** (hoặc kéo thả thư mục `1080/` vào ô Media). Chọn nhiều clip → kéo cả cụm xuống timeline; CapCut xếp theo thứ tự đang chọn, nên sắp tên file theo số scene trước (`scene_01…`, `scene_02…`).
- Tỉ lệ: Ratio → **16:9** (long-form) / **9:16** (Shorts).
- Clip đầu tiên kéo vào thường quyết định fps của project; nếu xuất ra fps lệch nguồn, chỉnh lại ở bước xuất (mục 9).

## 3. Cắt, trim, sắp xếp
- **Split** tại đầu phát: `Ctrl+B` (hoặc biểu tượng split trên thanh công cụ timeline).
- **Bỏ phần bên trái / phải đầu phát**: `Q` / `W` (bản cũ có thể không có — dùng Split rồi Delete).
- **Trim**: kéo mép trái/phải clip. Bỏ 1s đầu mỗi clip FlowKit = đặt đầu phát ở 1.0s của clip → `Q`.
- **Xóa và tự dồn khoảng trống**: chọn clip → `Delete` trên track chính (track chính tự dồn; track phủ thì không).
- **CUT ĐEN**: Media → Library (hoặc kho nội bộ) → tìm "black" và kéo clip đen vào; hoặc để trống một đoạn ngắn trên track chính nếu bản CapCut cho phép khoảng trống.
- **Gộp nhóm** (để di chuyển cả Act): chọn nhiều clip → chuột phải → **Create compound clip** (`Alt+G`).

## 4. Zoom, punch-in, keyframe
- **Punch-in**: Split tại mốc 3s/6s → chọn đoạn sau → bảng phải Video → **Basic** → **Scale** = 110–115%. Kéo hình trong trình phát để chỉnh khung (Position).
- **Push-in chậm**: đầu phát ở đầu clip → bấm biểu tượng **hình thoi (keyframe)** cạnh Scale (100%) → đưa đầu phát về cuối clip → đổi Scale thành 105–108% (keyframe thứ hai tự tạo).
- **Bám chủ thể** (dùng nhiều ở Shorts): keyframe ở **Position** tại các điểm chủ thể di chuyển.
- Muốn zoom mượt hơn: chuột phải vào keyframe (hoặc mục Graphs / Curves ở bản mới) → chọn ease in/out.

## 5. Chữ & card
- Text → **Default text** (Add text) → kéo lên track phủ đúng vị trí trong Bảng dựng → gõ nội dung ở bảng phải.
- Style gợi ý cho card năm/mission/countdown: font đậm không chân (Arial Black, Montserrat ExtraBold…), trắng, **Stroke** đen 2–3, Shadow nhẹ, cỡ ~1/18 chiều cao khung, đặt ~8% từ mép trên.
- Làm 1 card chuẩn → chuột phải → **Copy / Paste** cho các card sau để giữ đúng style (hoặc lưu Preset nếu bản CapCut có).
- Animation của chữ: để trống hoặc In/Out rất ngắn (≤ 0.2s). Không chữ bay, không đánh máy.

## 6. Âm thanh
- **Âm lượng**: chọn clip/nhạc → bảng phải Audio → **Volume** (dB). Nhạc dưới thoại: −20 đến −24 dB.
- **Hạ nhạc quanh câu thoại**: keyframe ở Volume (hình thoi) — 4 điểm: bình thường → hạ → giữ → trả lại.
- **Fade**: Fade in / Fade out ngay dưới Volume (nhạc vào/ra 0.5–1s).
- **Normalize loudness**: toggle trong bảng Audio (nếu có) — bật cho clip thoại để các clip đều tiếng nhau.
- **Tách âm khỏi clip** (để làm J-cut/L-cut): chuột phải clip → **Extract audio** / **Separate audio**. Kéo phần âm của clip sau sang trái ~0.5s.
- **Nhạc / SFX**: Audio → **Import** file `/fk-gen-music`, hoặc thư viện Sound effects (gõ "whoosh", "boom", "beep").
- Tắt tiếng gốc cả track: biểu tượng loa ở đầu track.

## 7. Màu & hiệu ứng
- **Lớp màu phủ cả video**: Adjustment → **Custom adjustment** → kéo lên track phủ → kéo dài phủ toàn timeline. Chỉnh ở bảng phải: Temperature +5…+10 (ấm), Contrast +5, Saturation −5…0.
- Sửa riêng clip lệch màu: chọn clip → bảng phải **Adjust**.
- **Grain**: Effects → Video effects → tìm "grain" / "film" / "noise" → kéo lên track phủ, giảm Intensity thấp (≈10–20).
- **Glitch** (chuyển cảnh "điện thoại giật"): Effects → tìm "glitch", độ dài ≤ 0.5s đặt trên điểm cắt.
- Không dùng tab Transitions cho vlog (luật cắt thẳng tại khung che).

## 8. Phụ đề
- Captions (bản cũ: Text → **Auto captions**) → chọn ngôn ngữ nói → **Generate / Create**.
- Sửa chữ: bấm vào từng dòng phụ đề trên timeline hoặc trong danh sách phụ đề ở bảng phải.
- `Ctrl+S` để lưu — `/extract-capcut-srt` đọc phụ đề từ file project đã lưu.
- Trước khi xuất: ẩn track phụ đề (biểu tượng mắt ở đầu track) hoặc bỏ chọn phụ đề trong hộp thoại Export — user không burn phụ đề vào hình, kể cả Shorts. Bản mới có tùy chọn xuất phụ đề ra `.srt` ngay trong hộp thoại Export, dùng được thay cho `/extract-capcut-srt`.

## 9. Xuất video
Nút **Export** góc phải trên:
- Resolution **1080p**, Bit rate **Recommended** (hoặc Higher), Codec **H.264**, Format **mp4**, Frame rate **= nguồn** (FlowKit 24 fps).
- Audio: bật xuất audio, AAC (nhạc trộn sẵn trong CapCut; sau khi xuất chạy lệnh loudnorm −14 LUFS ở SKILL.md mục 5).
- Bỏ chọn phụ đề (mục 8).
- Đặt tên file có ngày: `<slug>_final_2026-10-08.mp4`.

## 10. Shorts 9:16
- Trang chủ → chuột phải project dài → **Duplicate** (bản sao để cắt Shorts; không sửa bản gốc).
- Ratio → **9:16**. Hình 16:9 sẽ thành dải ngang giữa khung → chọn clip → tăng Scale tới khi hết viền đen trên/dưới (thường ~316%, vì khung dọc cao gấp ~3.16 lần dải hình ngang) — rồi kéo Position để giữ chủ thể ở giữa. Scale cao như vậy làm hình mềm hơn; chọn đoạn có chủ thể lớn, rõ.
- **Auto reframe** (bảng phải Video, có thể là Pro) tự bám chủ thể — dùng nếu có, kiểm lại từng đoạn.
- Mỗi Short xuất riêng: kéo vùng xuất bằng cách xóa phần ngoài đoạn cần dùng trong bản sao, hoặc tạo nhiều bản sao.

## 11. Phím tắt hay dùng
| Phím | Việc |
|---|---|
| `Space` | Phát / dừng |
| `Ctrl+B` | Split tại đầu phát |
| `Q` / `W` | Bỏ phần trái / phải đầu phát |
| `Delete` | Xóa clip đang chọn |
| `Ctrl+Z` / `Ctrl+Shift+Z` | Hoàn tác / làm lại |
| `Ctrl+C` / `Ctrl+V` | Copy / dán (cả style chữ) |
| `Alt+G` | Tạo compound clip |
| `Ctrl+S` | Lưu project |
| `Ctrl` + lăn chuột | Zoom timeline |
| `←` / `→` | Lùi / tiến 1 khung hình |

Phím tắt có thể khác theo bản; xem đầy đủ ở menu chính → **Keyboard shortcuts**.
