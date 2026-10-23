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
  * Lần 1: Phát hiện 2 lỗi qua trích xuất 24 frames: (1) thiếu cú cắt gắt Hard Cut theo Storyboard, (2) lỗi xuất hiện 2 Nora (nhân đôi nhân vật) ở giây số 9.
  * Lần 2 (`2e9002c4-fd91-4fe5-a336-7a0d8a011a93`): Đã khắc phục 100% lỗi Hard Cut (cắt đúng tại 3.0s và 7.0s) và triệt tiêu 100% lỗi nhân đôi 2 Nora (điểm `0-7.1s` đạt `9.5/10`). Tuy nhiên phát hiện lỗi ở Shot 3 (`7.1s-10.0s`): do prompt gộp `matching Panel 3 and Panel 4` (trong khi Panel 3 và Panel 4 đảo trục 180° Trái/Phải), AI đã ghép vị trí đứng bên trái lan can của Castor ở Panel 3 vào nền cảnh biển bên trái của Panel 4 (khiến Castor đứng phía ngoài mạn tàu).
  * Đã đúc kết **Rule 74(3) / Bài học 80.4 (`Anti-180°-Axis-Fusion` & `Inside-Deck SPATIAL LOCK`)** vào `AGENTS.md`, `CLAUDE.md`, `skills/fk-film/` và cập nhật đồng bộ toàn bộ **154 scenes** trên cả 5 Hồi (`prompts_act1.json` .. `prompts_act3.json`) + `flow_agent.db` (đạt `0 lỗi` qua `tools/lint_prompt.py`).
  * Lần 3 (`b351f00a-187f-406a-86d5-f4cebd0ba2e5`): **ĐẠT 9.72/10 (`excellent` — PASS)**!
    * Shot 1 (`0-3s`, Frames 01–07): EWS tàu hải tặc lướt qua sương mù, đèn lồng đồng vàng ấm phản chiếu mặt nước đen (khớp Panel 1).
    * Hard Cut 1 (`3.0s`, Frame 07 ➔ 08): Cắt gắt sang MS mũi tàu; Nora đứng một mình bên trái trên sàn tàu gỗ, tay đặt lên lan can nhìn sang phải vào màn sương (khớp Panel 2, 100% đúng khuôn mặt & trang phục).
    * Hard Cut 2 (`7.0s`, Frame 17 ➔ 18): Cắt gắt sang MS mạn tàu giữa (khớp Panel 3 Bottom-Left); sàn gỗ ướt + thùng gỗ bên trái, lan can + đèn lồng đồng bên phải, mặt biển sương mù phía ngoài bên phải. Castor bước tới **đứng hoàn toàn BÊN TRONG trên sàn tàu gỗ bên trái**, tay trái đặt lên lan can nhìn ra biển. Triệt tiêu 100% lỗi nhân đôi nhân vật và lỗi gộp trục 180°.
  * Trạng thái hiện tại của SC-01 trong database: `horizontal_video_status = 'COMPLETED'`, `horizontal_video_media_id = 'b351f00a-187f-406a-86d5-f4cebd0ba2e5'`, đã tải về `output/golden-tree/scenes/scene_01_4de18786-a007-4dbc-926a-2d76b8030bfd.mp4` và trích xuất 24 frames (`output/golden-tree/scenes/review/SC-01_contact_sheet_24frames.jpg`).
  * **Đã Upscale 1080p & Xóa Logo `SC-01`:** `output/golden-tree/1080/scene_01_4de18786-a007-4dbc-926a-2d76b8030bfd_1080p_clean.mp4`.
* **Đồng bộ 100% Storyboard Omen Fish (Rule 74(4) — `1.7m–1.9m [1.8m] / 80 kg`):**
  * Đã sinh lại, xóa watermark, upload lấy UUID sạch và thực hiện Visual Audit cho **8 tấm Storyboard**:
    * `SC-02`: `c3ef210a-4aa9-44db-9665-a481f00e70e2` (`SC-02_storyboard_clean.jpg`)
    * `SC-05`: `1000e331-34ca-4a29-8173-3ccc7aabf112` (`SC-05_storyboard_clean.jpg`)
    * `SC-07`: `bfc450b5-8bd1-4290-8ff3-6cb589250caa` (`SC-07_storyboard_clean.jpg`)
    * `SC-08`: `262700dc-0837-484b-b5ae-e5fd27671438` (`SC-08_storyboard_clean.jpg`)
    * `SC-09`: `0f80d0fd-53cd-4826-8ea9-a6cb93b655cc` (`SC-09_storyboard_clean.jpg`)
    * `SC-15`: `e926a2cc-374a-4b49-895d-b21327164eea` (`SC-15_storyboard_clean.jpg`)
    * `SC-16`: `050d1587-7b86-4bde-b5d1-4d499e885be0` (`SC-16_storyboard_clean.jpg`)
    * `SC-17`: `4f556610-4918-42f7-9ea0-d7cc67598c62` (`SC-17_storyboard_clean.jpg`)
* **Cảnh SC-02 (`69d7a32b-d107-41d8-a5c4-e005e73e138c`):**
  * Lần 1 (`862d5eaf-7bc0-4875-8116-a170c1f196ab`, `output/golden-tree/scenes/scene_02_69d7a32b-d107-41d8-a5c4-e005e73e138c.mp4`):
    * **Hình ảnh (24 frames `SC-02_contact_sheet_24frames.jpg`)**: **9.65/10** — Hoàn hảo 3 cú máy (Shot 1 `0-3s` Castor trên boong tàu chỉ tay xuống thuyền thúng bên phải; Hard Cut 1 tại `3.0s` sang Shot 2 `3-6s` Castor + Nora cầm đèn lồng đồng nhìn xuống thuyền; Hard Cut 2 tại `6.0s` sang Shot 3 `6-8s` góc cao nhìn thẳng vào thuyền thúng thấy rõ cá Omen Fish 1.8m/80kg bụng phát sáng xanh ngọc bên trái và Ông Lão Ngư Dân ôm mặt bên phải). Không nhân đôi nhân vật, không gộp trục 180°.
    * **Âm thanh / Thoại (Whisper `tools/review_dialogue.py`)**: Phát hiện 2 vấn đề:
      1. **Giọng nói (`pitch 232 Hz`)**: Do `SC-02` được gửi lúc `character.voice_description` trong DB chưa gán `fenrir`, hệ thống fallback về giọng mặc định `laomedeia` (giọng nữ) cho Castor (độ chính xác từ 100%). Hiện tại DB đã khóa cứng `Castor -> fenrir` (giọng nam trầm) và sắp xếp `character_names[0] = speaker[0]` cho toàn bộ 154 scenes.
      2. **Timing thoại (`0.4s–7.12s` so với kế hoạch `0-6s`)**: Câu thoại 20 từ kéo dài lấn 1.12s qua cú cắt gắt ở giây `6.0s`.
* **Bước tiếp theo:** Chờ User quyết định đối với **SC-02** (Phương án A: Sinh lại `SC-02` với giọng nam `fenrir` + câu thoại rút gọn 14 từ kết thúc trước 6.0s; hoặc Phương án B: Duyệt hình ảnh `SC-02` để upscale 1080p và chuyển sang sinh tiếp **SC-03**).

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
