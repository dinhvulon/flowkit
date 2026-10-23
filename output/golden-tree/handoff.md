# BÀN GIAO TIẾN ĐỘ DỰ ÁN (PROJECT HANDOFF)
**Tên dự án:** *Pirates of the Golden Tree* (Cướp Biển Cây Vàng)  
**Workspace:** `c:\flowkit`  
**Ngày cập nhật:** 23/10/2026

---

## 1. Vị trí Lưu Trữ Dữ Liệu & Context (SSOT)

Toàn bộ dữ liệu của dự án được lưu trữ độc lập và tự thân trong thư mục dự án `c:\flowkit`:

1. **Cơ sở dữ liệu (Database SQLite):**
   * Đường dẫn: `c:\flowkit\flow_agent.db`
   * Lưu toàn bộ 154 scenes, requests, characters, video URLs, media IDs, status của toàn bộ phim.
   * `project_id`: `1e8932e0-f47e-4799-8677-174d3b219a07`
   * `video_id`: `e9667a26-bce9-48da-b356-64044c06b317`

2. **File Kịch bản & Prompt 5 Hồi (Đã cập nhật Rule 74 Hard Cuts 100%):**
   * Hồi 1 (SC-01 đến SC-30): `output/golden-tree/prompts_act1.json`
   * Hồi 2A (SC-31 đến SC-84): `output/golden-tree/prompts_act2a.json`
   * Điểm giữa (SC-85 đến SC-96): `output/golden-tree/prompts_midpoint.json`
   * Hồi 2B (SC-97 đến SC-122): `output/golden-tree/prompts_act2b.json`
   * Hồi 3 (SC-123 đến SC-154): `output/golden-tree/prompts_act3.json`
   * Toàn bộ 154 prompt đều đã vượt qua `tools/lint_prompt.py` (0 lỗi) và đồng bộ vào `flow_agent.db`.

3. **Tài nguyên Hình ảnh & Video:**
   * Thư mục ảnh tham chiếu & Storyboard: `output/golden-tree/images/`
     * 22 tấm Storyboard sạch logo (`SC-01_storyboard_clean.jpg` ... `SC-30_storyboard_clean.jpg`).
     * Toàn bộ ảnh nhân vật sạch logo: `nora_clean.jpg`, `nora_body_seafarer_clean.jpg`, `castor_clean.jpg`, `heracles_clean.jpg`, `old_fisherman_clean.jpg`, `omen_fish_clean.jpg`, `labyrinth_beast_clean.jpg`, `theron_clean.jpg`, `abyssal_siren_clean.jpg`.
   * Thư mục Video: `output/golden-tree/scenes/`
   * Thư mục Review 24 frames: `output/golden-tree/scenes/review/` (đã trích xuất 24 frames và contact sheet lưới 6×4 của SC-01).

4. **Hệ thống Rule & Skills (Đã sync):**
   * `AGENTS.md` & `CLAUDE.md`: Chứa đầy đủ từ Rule 1 đến Rule 74 (Rule 73: 24-frame review, Rule 74: Hard Cuts & Anti-Cloning Lock).
   * `.agents/skills/`: 52 Antigravity skills.
   * `skills/fk-film/`: Hướng dẫn làm phim, bài học thực tế (`production-lessons.md` - Bài học 80), bảng khóa prompt (`prompt-lock.md`).

5. **Log Phiên Làm Việc (Antigravity Brain Logs):**
   * Thư mục: `C:\Users\Administrator\.gemini\antigravity-ide\brain\e56b0f8e-65d9-4203-9bec-6f6be70e0302\`
   * Toàn bộ transcript lịch sử hội thoại: `.system_generated\logs\transcript.jsonl`

---

## 2. Trạng Thái Hiện Tại Của Dự Án

* **Hồi 1 (Act 1):** Đã tạo xong toàn bộ 22 ảnh Storyboard 2×2 sạch logo và 8 cảnh liên tục.
* **Cảnh SC-01:**
  * Đã sinh video 720p thô lần 1 và phát hiện 2 lỗi qua trích xuất 24 frames: (1) thiếu cú cắt gắt Hard Cut theo Storyboard, (2) lỗi xuất hiện 2 Nora (nhân đôi nhân vật) ở giây số 9.
  * Đã viết lại prompt khóa cứng `Multi-shot sequence with crisp hard cuts` tại giây 3.0 và 7.0, khóa cô lập Nora off-screen trong cú máy Castor, và thêm khối cấm phân thân `anti-cloning lock`.
  * Trạng thái hiện tại của SC-01 trong database: `horizontal_video_status = 'PENDING'` (sẵn sàng sinh lại).

---

## 3. Lệnh Cần Chạy Khi Mở Antigravity / Phiên Mới

1. **Khởi động server FlowKit:**
   ```powershell
   cd c:\flowkit
   python -m agent.main
   ```
   (Server chạy tại `http://127.0.0.1:8100`)

2. **Khởi động Review Board:**
   ```powershell
   cd c:\flowkit
   python tools/review_server.py 8200
   ```
   (Mở trình duyệt: `http://localhost:8200?video_id=e9667a26-bce9-48da-b356-64044c06b317`)

3. **Gửi lệnh sinh lại video SC-01 (khi User duyệt):**
   Submit batch request R2V:
   ```bash
   curl -X POST http://127.0.0.1:8100/api/requests/batch -H "Content-Type: application/json" -d '{"requests": [{"type": "GENERATE_VIDEO_REFS", "scene_id": "4de18786-a007-4dbc-926a-2d76b8030bfd", "project_id": "1e8932e0-f47e-4799-8677-174d3b219a07", "video_id": "e9667a26-bce9-48da-b356-64044c06b317", "orientation": "HORIZONTAL"}]}'
   ```
