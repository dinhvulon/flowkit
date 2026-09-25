# fk-remove-watermark — Remove Watermark & Disrupt SynthID from Images and Videos

Xóa watermark (Gemini / Google Flow sparkle logo) và gỡ bỏ mã nhận diện SynthID trên ảnh hoặc video local bằng thuật toán Reverse Alpha Blending & cv2.inpaint.

Usage:
- Interactive: `python tools/remove_watermark_from_image.py` hoặc `python tools/remove_watermark_from_link.py`
- Command line (1 hoặc nhiều file):
  - Ảnh: `python tools/remove_watermark_from_image.py "<path_to_image>"`
  - Video: `python tools/remove_watermark_from_link.py "<path_to_video>"`
- Xử lý cả thư mục:
  - Ảnh: `python tools/remove_watermark_from_image.py --dir "<path_to_folder>"`
  - Video: `python tools/remove_watermark_from_link.py --dir "<path_to_folder>"`

## Cơ chế hoạt động

1. **Ảnh (Image):**
   - Định dạng hỗ trợ: `.jpg`, `.jpeg`, `.png`, `.webp`.
   - Sử dụng multi-variant template matching (gồm ảnh gốc, CLAHE-enhanced, inverted) để định vị watermark chính xác.
   - Dùng `cv2.inpaint` (thuật toán `INPAINT_TELEA`) trên mặt nạ logo sparkle đã làm dày viền 1px, trả lại pixel nền tự nhiên.
   - Kết quả lưu thành `<ten>_clean.<ext>`, giữ nguyên ảnh gốc.

2. **Video:**
   - Định dạng hỗ trợ: `.mp4`.
   - Đọc luồng raw video `YUV420p` qua `ffmpeg`.
   - **Xóa logo:** Giải hợp ảnh *Reverse Alpha Blending* `original = (observed - α·logo)/(1-α)` trên kênh sáng Y và phục hồi màu trên U/V. Viền nét cao vá bằng inpaint láng giềng.
   - **Phá tín hiệu SynthID:** Thêm nhiễu Gaussian tần số cao cực nhẹ và Gaussian blur bán kính 0.5px trên kênh Y để phá hủy steganography neural pattern mà không suy giảm độ nét.
   - Kết quả lưu thành `<ten>_clean.mp4`, giữ nguyên video gốc.

## Python API Usage

Bạn có thể import trực tiếp trong bất kỳ module hoặc script nào:

```python
from agent.services.watermark import remove_watermark_image, remove_watermark_video

# Xóa watermark trên ảnh
clean_img_path = remove_watermark_image("path/to/frame.png", "path/to/frame_clean.png")

# Xóa watermark trên video
clean_vid_path = remove_watermark_video("path/to/scene_001.mp4", "path/to/scene_001_clean.mp4")
```
