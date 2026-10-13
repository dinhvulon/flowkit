# FLOWKIT — PROJECT HANDOFF DOCUMENT

**Dự án**: Hell Creek 66 Ma (Kỷ Phấn Trắng — Ngày Thiên Thạch Rơi)  
**Ngày cập nhật**: 13/10/2026 (Phiên làm việc chiều)  
**Mục đích**: Tài liệu bàn giao chi tiết để tiếp tục chạy và sản xuất dự án trên máy khác mà không bị thất thoát dữ liệu, bài học hay cấu hình.

---

## 1. TỔNG QUAN HỆ THỐNG & ĐỊNH DANH DỰ ÁN

| Thông số                  | Giá trị                                                                 |
| ------------------------- | ----------------------------------------------------------------------- |
| **Tên dự án**             | `Hell Creek 66 Ma`                                                      |
| **Project ID**            | `21513736-f0db-422c-954c-4c20dffd29a3`                                  |
| **Active Video ID**       | `bff25f18-b35d-41c8-811a-4f0a52184380` (Act 1: 18 scenes)               |
| **Base URL Backend**      | `http://127.0.0.1:8100` (`python -m agent.main`)                        |
| **Database**              | `flow_agent.db` (SQLite WAL checkpointed, committed vào Git)            |
| **Material áp dụng**      | `cretaceous_vlog` / `realistic` (đã bổ sung trong `agent/materials.py`) |
| **Thư mục output chính**  | `output/hell_creek_66_ma/` (đã dọn sạch media rác)                      |
| **Master Prompt Package** | `output/hell_creek_66_ma/prompts_act1_v2.json`                          |
| **Reference Prompts**     | `output/hell_creek_66_ma/references.json`                               |

---

## 2. TRẠNG THÁI HIỆN TẠI (CURRENT STATE)

1. **Bộ Media đã được dọn sạch rác**:
   - Toàn bộ media cũ (video 720p, 1080p, start frames cũ, file tạm) trong `output/hell_creek_66_ma/` đã được xóa sạch để giải phóng dung lượng và sẵn sàng sản xuất lại từ đầu theo quy chuẩn mới.
   - Thư mục chỉ lưu đúng 2 file cấu hình cốt lõi:
     - `prompts_act1_v2.json`: Chứa đầy đủ 10 Reference Prompts + 18 Scene Prompts của Act 1.
     - `references.json`: Chứa 10 Reference Prompts riêng biệt.
2. **Database SQLite đã được checkpoint**:
   - Toàn bộ prompt của `character` và `scene` trong `flow_agent.db` đã đồng bộ 100% với file JSON.
   - Chế độ WAL đã được chạy `PRAGMA wal_checkpoint(TRUNCATE)`, file `flow_agent.db-wal` đạt 0 byte, đảm bảo mọi dữ liệu đã nằm trọn vẹn trong `flow_agent.db` và đã commit vào Git.
3. **Queue sạch sẽ**:
   - Đã flush toàn bộ request `PENDING` rác, không bị kẹt worker khi khởi động backend trên máy mới.

---

## 3. TOÀN BỘ BÀI HỌC VÀ QUY TẮC MỚI (CHIỀU 13/10/2026)

Tất cả các bài học dưới đây đã được lưu trữ và đồng bộ vào `setup.py`, `CLAUDE.md`, `AGENTS.md`, `.agents/rules/claude_rules.md`, `skills/fk-character-design/SKILL.md`, và `skills/fk-time-travel-vlog/references/`:

### Rule 57 / Bài học 73: Đặc tả chất liệu sinh học khủng long & Triệt tiêu CGI

- **Giải phẫu hóa thạch thực tế**: Dựa trên mẫu da hóa thạch _Lane_ Triceratops (BHI-6200): vảy đa giác dạng lát gạch (`basement polygonal scales`), gai nón sừng 5–12cm (`conical tubercles/osteoderms`), yếm cổ nếp gấp đẫm bùn đỏ khô nứt nẻ.
- **Tập tính thị uy thực tế**: Thú ăn cỏ khổng lồ không cắn xé như quái vật phim kinh dị mà lao chéo 3/4 $\to$ trượt cày đất phanh lại $\to$ giậm chân nện đất thị uy $\to$ quay đầu bỏ đi.
- **Triệt tiêu 3D CGI**: CẤM 100% da nhẵn bóng, sáp bóng, mô hình nhựa, ánh sáng studio phẳng. Bắt buộc dùng ánh nắng xiên vòm lá (`dappled canopy sunlight`).

### Rule 58 / Bài học 74: Bắt buộc dùng Turnaround Sheet 16:9 cho Thực thể sống

- **Cấm ảnh đơn 1 góc (Single Photograph)** cho nhân vật và sinh vật chủ chốt.
- **Creature Turnaround Sheet 16:9 (3 Panel)**:
  - Panel 1: 3/4 góc Trái (thấy rõ sừng trái gãy cụt còn 30cm lộ lõi keratin phong hóa + sẹo diềm cổ).
  - Panel 2: 3/4 góc Phải (thấy rõ sừng phải lành lặn dài 100cm nhọn hoắt).
  - Panel 3: Cận cảnh chính diện sọ (khóa đối xứng/bất đối xứng, giác đấu, mắt hổ phách slit pupils).
- **Anti-Smoke Lock**: Cấm tuyệt đối luồng khói trắng xóa đặc quánh như ống khói tàu hỏa; chỉ dùng hơi sương ngưng tụ mờ nhẹ (`subtle faint mist`).

### Rule 59 / Bài học 75: Xác thú phân hủy sinh học & Triệt tiêu vết lốp xe / God Rays

- **Xác thú phân hủy thực tế**: Xác Edmontosaurus 7 tấn chìm lún 30cm vào bùn phù sa ướt, sườn ố vàng dính thịt rữa & gân nhờn bám sụn, vết cắn T. rex dập tủy, ruồi muỗi bu quanh; CẤM xương trắng khô thạch cao như bảo tàng.
- **Bảo toàn đường mòn tiền sử**: CẤM từ `trail` đơn độc làm AI vẽ vệt bánh xe tải 4x4 và gỗ xẻ hiện đại. Bắt buộc dùng `animal-trampled game corridor cutting into primeval rainforest, STRICTLY NO vehicle tracks, NO tire ruts, NO sawn logs`.
- **Triệt tiêu God Rays**: Xóa sạch các tia nắng volumetric beams thần thoại làm cảnh giả trân.

### Rule 60 / Bài học 76: Khóa chặt 1:1 khuôn mặt bằng Mệnh lệnh sắt đá & Ngũ quan

- **Dùng đúng ảnh Ref hiện có**: Tái sử dụng nguyên vẹn ảnh Ref Nora (`media_id: 553d94da-0545-471e-a503-b45855b87f92`), không cắt nhỏ hay tạo ảnh mới.
- **Mệnh lệnh 1:1 bắt buộc**: Mọi prompt có Nora bắt buộc mở đầu bằng:  
  `"Nora's face is an exact 1:1 identical match to the attached Nora reference image. Perfectly preserve her exact facial likeness from the reference photo without changes."`
- **Đặc tả hình học ngũ quan (Facial Geometry DNA Lock)**: Mặt trái xoan mềm mại (`youthful soft feminine heart-shaped face`), cằm thon tròn (`delicate rounded chin`), má bầu bĩnh, sống mũi nhỏ thẳng, đặc biệt là **bờ môi dày mọng hình trái tim (`distinctively FULL PLUMP PILLOWY LIPS with defined Cupid's bow and pouty lower lip`)**.
- **Khối phủ định đối kháng**: `STRICTLY FORBIDDEN: strictly NO square jaw, NO long rectangular face, NO thin lips, NO hollow cheeks, NO aged appearance (must look 22-23), NO facial distortion, NO face drift.`
- **Khóa tay trống không (Empty Hand Lock)**: Người xem nhìn qua ống kính camera; tay tự do của Nora trống không tự nhiên; CẤM 100% từ `phone`, `smartphone`, `device` để chống lỗi AI tự vẽ điện thoại ngoài đời lơ lửng trên tay.

---

## 4. DANH SÁCH 10 REFERENCE ENTITIES ĐÃ KHÓA TRÊN FLOWKIT

Toàn bộ 10 entity này đã có sẵn trong dự án với Media ID UUID sạch watermark:

| Entity Name               | Loại         | UUID Media ID                          | Mô tả tóm tắt                                                                                                                                    |
| ------------------------- | ------------ | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Bò Đực**                | creature     | `cab5ec79-af18-4d26-9e5e-278a8b0595bf` | Triceratops Bull 8.5 tấn, Turnaround Sheet 16:9 (3 panel: sừng trái gãy 30cm, sừng phải dài 100cm, sọ cận cảnh, vảy Lane BHI-6200, anti-smoke).  |
| **Con Non**               | creature     | `9311fac7-6e45-4e67-9205-6ae818a13299` | Triceratops con 2 tuổi, Turnaround Sheet 16:9 (3 panel: frill mềm, sừng nhú 10cm, vảy mịn).                                                      |
| **Edmontosaurus Carcass** | visual_asset | `4883a5b5-4610-40c0-acec-fc50f49454e1` | Xác hadrosaur 12m chìm lún 30cm trong bùn mép nước, sườn ố vàng dính gân cơ, vết cắn T. rex dập tủy.                                             |
| **Hell Creek Bank**       | location     | `8652b9b3-9c05-459d-a99b-d59fd6a0df6c` | Bờ sông Hell Creek 66 Ma, lòng sông bùn đỏ, rễ cọ Sabalites và dương xỉ rủ, sương sớm.                                                           |
| **Hell Creek Trail**      | location     | `97133e49-4bbc-43d4-bc84-e6adcf56299a` | Hành lang thú dẫm đạp trong rừng cận nhiệt đới, đất sét đỏ lún dấu chân, cấm 100% vệt lốp xe.                                                    |
| **Hell Creek Waterhole**  | location     | `b3584e8d-534c-4d5e-8ba1-c9e96b2eb522` | Bãi nước bùn đỏ Hell Creek, dấu chân 3 ngón, cỏ tháp bút và lau sậy cổ đại.                                                                      |
| **Nora**                  | character    | `553d94da-0545-471e-a503-b45855b87f92` | Mặt Nora 16:9: 22 tuổi, mặt trái xoan mềm, má bầu, môi mọng Cupid's bow, tóc đuôi ngựa vàng mật ong.                                             |
| **Nora Body**             | character    | `d32e92ec-e9a3-4a1e-84b2-03d6d02860b3` | Body Nora đã mặc outfit thời kỳ: áo tunic vải lanh màu olive-tan cổ V đan dây, đai da, quần bó, ủng cao cổ.                                      |
| **Nora Hand**             | character    | `24a1ffae-63ba-4ef3-9201-9f9b5d720c02` | Turnaround Sheet 16:9 cẳng tay & bàn tay nữ thon gọn, xắn tay áo khớp outfit, móng tự nhiên không sơn (dùng cho các shot POV tương tác nhặt đồ). |
| **T. rex**                | creature     | `763f69eb-a83a-4467-b50a-e5fa0061e897` | Khủng long bạo chúa T. rex Hell Creek.                                                                                                           |

---

## 5. HƯỚNG DẪN TỪNG BƯỚC ĐỂ TIẾP TỤC TRÊN MÁY KHÁC

### Bước 1: Kéo Repo và Kiểm tra Môi trường

```bash
git clone <repo-url> flowkit
cd flowkit
git checkout main
git status
```

_Đảm bảo working tree sạch sẽ, commit mới nhất là `10fce83`._

### Bước 2: Đồng bộ AI Tool Configs

Chạy lệnh setup để đồng bộ luật và kỹ năng cho công cụ AI bạn sử dụng (Claude Code, Antigravity, hoặc Codex):

```bash
python setup.py sync
```

_Lệnh này sẽ tự động cập nhật `.claude/commands/`, `AGENTS.md`, `.agents/skills/`, và `.agents/rules/claude_rules.md`._

### Bước 3: Khởi động Backend Flowkit & Kết nối Chrome Extension

1. Mở terminal chạy backend:
   ```bash
   python -m agent.main
   ```
   _(Backend chạy tại `http://127.0.0.1:8100`)_
2. Mở trình duyệt Google Chrome:
   - Cài đặt / nạp unpacked extension `extension/` vào Chrome.
   - Đăng nhập vào tài khoản Google Flow (Labs / FX).
   - Kiểm tra kết nối qua trình duyệt hoặc terminal:
     ```bash
     curl -s http://127.0.0.1:8100/health
     # Phải trả về: {"extension_connected": true}
     ```

### Bước 4: Kiểm tra Dự án & Nạp Prompt vào Bộ nhớ

Kiểm tra dự án Hell Creek 66 Ma đã có sẵn trong database:

```bash
curl -s http://127.0.0.1:8100/api/projects/21513736-f0db-422c-954c-4c20dffd29a3
```

Hai file master prompt sẵn sàng nằm tại:

- `output/hell_creek_66_ma/prompts_act1_v2.json`
- `output/hell_creek_66_ma/references.json`

---

## 6. QUY TRÌNH TIẾP TỤC SẢN XUẤT ACT 1 (PIPELINE EXECUTION)

Tiến hành sản xuất theo quy trình 2 tầng chuẩn mực (Rule 27 & Rule 29):

### Giai đoạn A: Sinh Start Frame tĩnh cho 18 Cảnh (Frame 0 Anchor)

> **LƯU Ý QUAN TRỌNG (Rule 29)**: Trước khi gửi lệnh sinh ảnh, BÁO CÁO số lượng cảnh cần sinh (18 ảnh) và HỎI Ý KIẾN USER XÁC NHẬN!

1. **Gửi lệnh sinh ảnh**:
   - Sử dụng `POST /api/requests/batch` với `type: "GENERATE_IMAGE"` và các `image_prompt` đã khóa trong `prompts_act1_v2.json`.
   - Server tự động pacing 45–60s mỗi request theo Rule 10 để chống lỗi unusual activity.
2. **Quy trình Clean-Before-Video-Gen (Rule 28)**:
   - Tải ảnh về: `output/hell_creek_66_ma/images/scene_{idx}.jpg`.
   - Chạy xóa watermark: `python tools/remove_watermark_from_image.py "output/hell_creek_66_ma/images/scene_{idx}.jpg"`.
   - Upload ảnh sạch lên Flow: `POST /api/flow/upload-image` để nhận Media ID UUID sạch.
   - Gán UUID sạch này vào `horizontal_image_media_id` của từng Scene.
3. **Cổng Duyệt Ảnh Bắt Buộc (Rule 22 & 25 — Stop & Review Gate)**:
   - Mở giao diện duyệt ảnh: `output/hell_creek_66_ma/review_images.html`.
   - **DỪNG LẠI CHỜ USER DUYỆT 100% START FRAMES!**
   - Chỉ khi User duyệt ảnh nào đạt, ảnh đó mới được đưa vào sinh video. Ảnh nào chưa đạt thì resubmit bằng `REGENERATE_IMAGE`.

### Giai đoạn B: Sinh Video 720p (Omni Flash R2V Ingredients Workflow)

1. **Sau khi User duyệt Start Frames**:
   - Gửi batch `GENERATE_VIDEO_REFS` (RPC `MZZa6b`):
     - Start Frame sạch làm Frame 0 Anchor.
     - Reference Ingredients gồm `character_names` (ví dụ: `["Nora", "Nora Body"]` hoặc `["Bò Đực"]`).
     - Voice model: Slot 7 pinned `laomedeia` (Rule 24).
2. **Tải video 720p thô & Chưa xóa logo (Rule 18 & 32)**:
   - Tải về: `output/hell_creek_66_ma/scenes/scene_{idx}.mp4`.
   - **TUYỆT ĐỐI CHƯA CẦN XÓA LOGO Ở BƯỚC NÀY** để tránh tốn CPU/GPU.
   - Mở Review Board (`python tools/review_server.py 8200` tại `http://localhost:8200`) để User duyệt từng clip 720p thô.

### Giai đoạn C: Upscale 1080p, Xóa logo & Concat cuối cùng

1. **Upscale có chọn lọc (Rule 18)**:
   - CHỈ những cảnh User đã duyệt PASS mới gửi lệnh Upscale: `POST /api/requests/batch` (`type: "UPSCALE_VIDEO"`, RPC `p0UkFb`).
   - Tải video 1080p về: `output/hell_creek_66_ma/1080/scene_{idx}_1080p.mp4`.
2. **Xóa logo trên bản 1080p**:
   - Chạy `remove_watermark_video` trực tiếp trên file 1080p:
     `output/hell_creek_66_ma/1080/scene_{idx}_1080p_clean.mp4`.
3. **Ghép nối phim hoàn chỉnh (Concat)**:
   - Dùng `tools/concat_videos.py` hoặc ffmpeg để nối toàn bộ các clip 1080p clean đã duyệt thành phim hoàn chỉnh kèm TTS/Audio mastering.

---

## 7. CÁC QUY TẮC CẦN GHI NHỚ KHI VIẾT CODE / SCRIPT

1. **Rule 4 (Scratch Directory Only)**:
   - TUYỆT ĐỐI KHÔNG tạo script tạm thời (`test_*.py`, `check_*.py`, `debug_*.py`) trong thư mục gốc repo hoặc `scripts/`.
   - BẮT BUỘC lưu script tạm trong thư mục scratch của cuộc hội thoại:
     `<appDataDir>/brain/<conversation-id>/scratch/` hoặc chạy inline one-liner: `python -c "..."`.
2. **Rule 21 (Flush Pending Queue)**:
   - Nếu worker bị kẹt do request cũ, chạy lệnh dọn dẹp:
     ```bash
     python -c "import sqlite3; conn = sqlite3.connect('flow_agent.db'); conn.execute(\"UPDATE request SET status='FAILED' WHERE status='PENDING'\"); conn.commit()"
     ```
3. **Rule 29 (Confirm Before Spend)**:
   - Luôn hỏi rõ ràng và chờ sự đồng ý của User trước bất kỳ lệnh sinh media nào tiêu tốn credit Flow.

---

**Tài liệu này được tạo tự động và đồng bộ với commit Git `10fce83`. Mọi AI Agent tiếp quản dự án này trên máy mới chỉ cần đọc tài liệu này là có thể tiếp tục công việc một cách hoàn hảo.**
