"""CapCut Desktop Auto Captions → SRT Extractor.

Đọc draft_content.json của CapCut Desktop, trích xuất subtitle
(Auto Captions) và xuất ra file .srt chuẩn.

Cách dùng:
  python tools/capcut_extract_srt.py                      # Liệt kê tất cả project
  python tools/capcut_extract_srt.py "Tên Project"        # Xuất SRT từ project cụ thể
  python tools/capcut_extract_srt.py "Tên Project" -o output.srt   # Chỉ định file output
  python tools/capcut_extract_srt.py --list                # Liệt kê project + số subtitle
"""

import json
import os
import sys
import re
from pathlib import Path

# Configure UTF-8 for Windows console
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


# ── CapCut draft paths ─────────────────────────────────────────────────────────

CAPCUT_DRAFTS_DIR = os.path.expandvars(
    r"%USERPROFILE%\AppData\Local\CapCut\User Data\Projects\com.lveditor.draft"
)

# Jianying (bản Trung Quốc) dùng path khác
JIANYING_DRAFTS_DIR = os.path.expandvars(
    r"%USERPROFILE%\AppData\Local\JianyingPro\User Data\Projects\com.lveditor.draft"
)


def _get_drafts_dir() -> str:
    """Tìm thư mục draft hợp lệ (ưu tiên CapCut, fallback Jianying)."""
    if os.path.isdir(CAPCUT_DRAFTS_DIR):
        return CAPCUT_DRAFTS_DIR
    if os.path.isdir(JIANYING_DRAFTS_DIR):
        return JIANYING_DRAFTS_DIR
    raise FileNotFoundError(
        f"Không tìm thấy thư mục draft CapCut.\n"
        f"  Đã kiểm tra:\n"
        f"    - {CAPCUT_DRAFTS_DIR}\n"
        f"    - {JIANYING_DRAFTS_DIR}\n"
        f"  Hãy chắc chắn CapCut Desktop đã được cài đặt."
    )


# ── Project discovery ──────────────────────────────────────────────────────────

def list_projects(drafts_dir: str = None) -> list[dict]:
    """Liệt kê tất cả project CapCut với thông tin cơ bản."""
    drafts_dir = drafts_dir or _get_drafts_dir()
    projects = []
    for folder in os.listdir(drafts_dir):
        folder_path = os.path.join(drafts_dir, folder)
        if not os.path.isdir(folder_path):
            continue
        meta_path = os.path.join(folder_path, "draft_meta_info.json")
        if not os.path.exists(meta_path):
            continue
        try:
            with open(meta_path, encoding="utf-8") as f:
                meta = json.load(f)
            projects.append({
                "name": meta.get("draft_name", folder),
                "path": folder_path,
                "created": meta.get("tm_draft_create", 0),
                "modified": meta.get("tm_draft_modified", 0),
            })
        except Exception:
            pass
    # Sắp xếp theo thời gian modified mới nhất
    projects.sort(key=lambda p: p["modified"], reverse=True)
    return projects


def find_project(project_name: str, drafts_dir: str = None) -> str | None:
    """Tìm project folder theo tên."""
    drafts_dir = drafts_dir or _get_drafts_dir()
    for folder in os.listdir(drafts_dir):
        folder_path = os.path.join(drafts_dir, folder)
        if not os.path.isdir(folder_path):
            continue
        meta_path = os.path.join(folder_path, "draft_meta_info.json")
        if not os.path.exists(meta_path):
            continue
        try:
            with open(meta_path, encoding="utf-8") as f:
                meta = json.load(f)
            if meta.get("draft_name", "").lower() == project_name.lower():
                return folder_path
        except Exception:
            pass
    return None


# ── SRT time formatting ───────────────────────────────────────────────────────

def us_to_srt_time(microseconds: int) -> str:
    """Chuyển microseconds → SRT timestamp (HH:MM:SS,mmm)."""
    ms = microseconds // 1000
    s, ms = divmod(ms, 1000)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


# ── Text extraction from CapCut materials ──────────────────────────────────────

def _extract_text_from_material(text_material: dict) -> str:
    """Trích xuất text thuần từ material text của CapCut.
    
    CapCut lưu text content theo nhiều format khác nhau tùy phiên bản:
    - Cách 0: field "recognize_text" (Auto Captions)
    - Cách 1: field "content" là JSON string chứa {"text": "..."}
    - Cách 2: field "content" là JSON string chứa {"texts": [{"text": "..."}]}
    - Cách 3: field "text_content" trực tiếp
    """
    # Ưu tiên recognize_text từ Auto Captions
    recognize_text = text_material.get("recognize_text", "")
    if recognize_text and isinstance(recognize_text, str):
        return recognize_text.strip()

    # Thử cách 1 & 2: field "content" (phổ biến nhất)
    content_str = text_material.get("content", "")
    if content_str:
        try:
            content = json.loads(content_str) if isinstance(content_str, str) else content_str
            # Format: {"text": "Hello"}
            if isinstance(content, dict):
                text = content.get("text", "")
                if text:
                    return text.strip()
                # Format: {"texts": [{"text": "Hello"}]}
                texts = content.get("texts", [])
                if texts:
                    return " ".join(t.get("text", "") for t in texts if t.get("text")).strip()
        except (json.JSONDecodeError, TypeError):
            # content_str có thể là plain text
            if isinstance(content_str, str) and content_str.strip():
                return content_str.strip()

    # Thử cách 3: field khác
    for field in ["text_content", "value", "text"]:
        val = text_material.get(field, "")
        if val and isinstance(val, str):
            return val.strip()

    return ""


# ── Main extraction ───────────────────────────────────────────────────────────

def extract_subtitles(project_path: str) -> list[dict]:
    """Trích xuất tất cả subtitle entries từ draft_content.json.
    
    Returns: List of {"index": int, "start_us": int, "end_us": int, "text": str}
    """
    draft_path = os.path.join(project_path, "draft_content.json")
    if not os.path.exists(draft_path):
        raise FileNotFoundError(f"Không tìm thấy draft_content.json tại {project_path}")

    with open(draft_path, encoding="utf-8") as f:
        draft = json.load(f)

    # Build map: material_id → text content
    text_map = {}
    materials = draft.get("materials", {})
    
    # CapCut lưu subtitle text trong materials.texts[]
    for txt in materials.get("texts", []):
        mat_id = txt.get("id", "")
        text = _extract_text_from_material(txt)
        if mat_id and text:
            text_map[mat_id] = text

    # Collect subtitle entries từ text tracks
    entries = []
    for track in draft.get("tracks", []):
        if track.get("type") != "text":
            continue
        for seg in track.get("segments", []):
            mat_id = seg.get("material_id", "")
            tr = seg.get("target_timerange", {})
            start = tr.get("start", 0)
            duration = tr.get("duration", 0)
            text = text_map.get(mat_id, "")
            if text:
                entries.append({
                    "start_us": start,
                    "end_us": start + duration,
                    "text": text,
                })

    # Sort theo thời gian
    entries.sort(key=lambda e: e["start_us"])

    # Đánh index
    for i, entry in enumerate(entries, 1):
        entry["index"] = i

    return entries


def entries_to_srt(entries: list[dict]) -> str:
    """Chuyển entries thành nội dung SRT."""
    lines = []
    for entry in entries:
        lines.append(str(entry["index"]))
        lines.append(
            f"{us_to_srt_time(entry['start_us'])} --> {us_to_srt_time(entry['end_us'])}"
        )
        lines.append(entry["text"])
        lines.append("")  # blank line
    return "\n".join(lines)


def extract_srt(project_name: str, output_path: str = None) -> str:
    """Hàm chính: tìm project → trích subtitle → ghi file SRT.
    
    Returns: đường dẫn file SRT đã ghi.
    """
    project_path = find_project(project_name)
    if not project_path:
        raise FileNotFoundError(
            f"❌ Không tìm thấy project '{project_name}' trong CapCut.\n"
            f"   Chạy: python tools/capcut_extract_srt.py --list  để xem danh sách."
        )

    entries = extract_subtitles(project_path)
    if not entries:
        raise ValueError(
            f"❌ Project '{project_name}' không có subtitle/caption nào.\n"
            f"   Hãy mở CapCut → Text → Auto captions → Create trước."
        )

    srt_content = entries_to_srt(entries)

    # Xác định output path
    if not output_path:
        safe_name = re.sub(r'[^\w\s\-]', '', project_name).strip().replace(' ', '_')
        output_path = os.path.join(project_path, f"{safe_name}.srt")

    # Đảm bảo thư mục cha tồn tại
    parent_dir = os.path.dirname(os.path.abspath(output_path))
    if parent_dir:
        os.makedirs(parent_dir, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(srt_content)

    return output_path


# ── CLI ────────────────────────────────────────────────────────────────────────

def main():
    args = sys.argv[1:]

    # --list: liệt kê tất cả project
    if not args or args[0] == "--list":
        try:
            projects = list_projects()
        except FileNotFoundError as e:
            print(str(e))
            sys.exit(1)

        if not projects:
            print("Khong tim thay project nao trong CapCut Desktop.")
            sys.exit(0)

        print(f"\n[INFO] Tim thay {len(projects)} project CapCut:\n")
        print(f"  {'#':<4} {'Ten Project':<40} {'Subtitle'}")
        print(f"  {'-'*4} {'-'*40} {'-'*10}")

        for i, proj in enumerate(projects, 1):
            try:
                entries = extract_subtitles(proj["path"])
                sub_count = f"{len(entries)} dong"
            except Exception:
                sub_count = "—"
            print(f"  {i:<4} {proj['name']:<40} {sub_count}")

        print(f"\n[INFO] Dung: python tools/capcut_extract_srt.py \"Ten Project\" de xuat SRT\n")
        return

    # Extract SRT
    project_name = args[0]
    output_path = None
    if "-o" in args:
        idx = args.index("-o")
        if idx + 1 < len(args):
            output_path = args[idx + 1]

    try:
        srt_path = extract_srt(project_name, output_path)
        entries = extract_subtitles(find_project(project_name))
        print(f"\n[OK] Xuat thanh cong {len(entries)} dong subtitle!")
        print(f"File: {srt_path}")
        print(f"\n--- Preview (5 dong dau) ---")
        for entry in entries[:5]:
            time_str = f"{us_to_srt_time(entry['start_us'])} -> {us_to_srt_time(entry['end_us'])}"
            print(f"  [{time_str}] {entry['text']}")
        if len(entries) > 5:
            print(f"  ... va {len(entries) - 5} dong nua")
        print()
    except (FileNotFoundError, ValueError) as e:
        print(str(e))
        sys.exit(1)


if __name__ == "__main__":
    main()
