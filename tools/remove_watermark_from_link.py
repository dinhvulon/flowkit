"""
Xóa watermark từ video LOCAL trên máy — chỉ cần dán đường dẫn file, script tự xóa logo.

Cách dùng:
---------
1) Chạy tương tác (không cần nhớ cú pháp):
    python tools/remove_watermark_from_link.py

   Script sẽ hỏi lần lượt:
     Dán đường dẫn video (Enter để dừng):

   Dán 1 đường dẫn (hoặc kéo-thả file .mp4 vào cửa sổ terminal) -> Enter
   -> nó xóa watermark -> in ra đường dẫn file kết quả.
   Dán tiếp file khác nếu có nhiều video, hoặc bấm Enter (để trống) để dừng.

2) Chạy nhanh với 1 hoặc nhiều file truyền thẳng trên dòng lệnh:
    python tools/remove_watermark_from_link.py "C:\\path\\video1.mp4" "C:\\path\\video2.mp4"

3) Xử lý cả một thư mục (mọi file .mp4 trong đó):
    python tools/remove_watermark_from_link.py --dir "C:\\path\\to\\folder"

Kết quả:
-------
Với mỗi video gốc <ten>.mp4, script tạo file mới:
  <ten>_clean.mp4   <- bản đã xóa watermark, dùng file này

File gốc được giữ nguyên, không bị ghi đè.
"""

import argparse
import glob
import os
import sys

# Configure UTF-8 for Windows console
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# Ensure flowkit root and tools dir are in sys.path
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_TOOLS = os.path.dirname(os.path.abspath(__file__))
for _p in (_ROOT, _TOOLS):
    if _p not in sys.path:
        sys.path.insert(0, _p)

try:
    from agent.services.watermark import remove_watermark_video
except ImportError:
    try:
        from watermark import remove_watermark_video
    except ImportError:
        from omniflash.watermark import remove_watermark_video


def _clean_path_arg(raw: str) -> str:
    """Bỏ dấu ngoặc kép nếu người dùng kéo-thả file (Windows tự bọc "..." quanh path)."""
    return raw.strip().strip('"').strip("'")


def process_one_file(path: str) -> str | None:
    path = _clean_path_arg(path)
    if not path:
        return None

    if not os.path.isfile(path):
        print(f"  [LỖI] Không tìm thấy file: {path}")
        return None

    if path.lower().endswith("_clean.mp4"):
        print(f"  [BỎ QUA] File này đã là bản clean rồi: {path}")
        return None

    try:
        print("  -> Đang xóa watermark...")
        cleaned = remove_watermark_video(path)
        print(f"  [OK] Xong: {cleaned}")
        return cleaned
    except Exception as e:
        print(f"  [LỖI] Không xóa được watermark: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(description="Xóa watermark khỏi video local (đường dẫn hoặc cả thư mục).")
    parser.add_argument("paths", nargs="*", help="Danh sách đường dẫn video (bỏ trống để nhập tương tác)")
    parser.add_argument("--dir", help="Xử lý mọi file .mp4 trong thư mục này (bỏ qua các file _clean.mp4)")
    args = parser.parse_args()

    paths = list(args.paths)

    if args.dir:
        folder = os.path.abspath(args.dir)
        found = sorted(glob.glob(os.path.join(folder, "*.mp4")))
        found = [p for p in found if not p.lower().endswith("_clean.mp4")]
        if not found:
            print(f"Không tìm thấy file .mp4 nào (chưa có _clean) trong: {folder}")
            return
        paths.extend(found)

    if not paths:
        print("Dán đường dẫn video (hoặc kéo-thả file vào đây), mỗi lần 1 file.")
        print("Bấm Enter (để trống) khi xong.\n")
        while True:
            p = input("Dán đường dẫn video (Enter để dừng): ")
            p = _clean_path_arg(p)
            if not p:
                break
            paths.append(p)

    if not paths:
        print("Không có file nào được nhập. Thoát.")
        return

    results = []
    for i, p in enumerate(paths, 1):
        print(f"\n=== [{i}/{len(paths)}] {p} ===")
        result = process_one_file(p)
        if result:
            results.append(result)

    print(f"\nHoàn tất: {len(results)}/{len(paths)} video đã xóa watermark thành công.")
    for r in results:
        print(f"  - {r}")


if __name__ == "__main__":
    main()
