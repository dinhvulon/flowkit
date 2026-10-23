---
name: fk-script-to-prompts
description: "Chuyển thể Kịch Bản (script.md) thành Structured Video Prompt JSON cho phim điện ảnh ngôi thứ ba (/fk-film) trên FlowKit / Omni Flash R2V. Bắt buộc tích hợp 100% bộ Screenwriting Skills (sw-*), bộ Cinematic Subagents (fk-*), Storyboard 2x2 (Rule 69, Rule 74), tự động Self-Review (/fk-review-prompt) và kiểm toán qua tools/lint_prompt.py trước khi xuất file cho user duyệt."
allowed-tools: Read, Bash, Edit, Grep, Glob, Skill, AskUserQuestion
---

# 🎬 fk-script-to-prompts — Script-to-Prompt Converter & Validator (Narrative Film)

> **BẮT BUỘC CHO MỌI AGENT (Antigravity `agy` & Claude `claude`):**
> Khi chuyển thể từ kịch bản phân cảnh (`script.md` / `script_act*.md`) và bảng phân cảnh (`storyboards_act*.json`) sang file Video Prompt JSON (`prompts_act*.json`), **TUYỆT ĐỐI CẤM VIẾT PROMPT AD-HOC TỰ DO HOẶC TỰ Ý CHẾ THOẠI**.
> Agent **BẮT BUỘC** phải vận hành skill này để tích hợp toàn bộ **bộ Screenwriting Skills (`sw-*`)**, **bộ Cinematic Subagents (`fk-*`)**, chạy quy trình **Self-Review (`/fk-review-prompt`) & Linter Auto-Repair (`tools/lint_prompt.py`)**, và chỉ xuất file cuối cùng đạt `errors=0` cho người dùng duyệt.

---

## 1. Danh Mục Các Skill Bắt Buộc Tích Hợp (Skill Registry)

### A. Hệ Thống Screenwriting Skills (`sw-*` — BẮT BUỘC 100%)
1. **`/sw-workflow` (Điều phối kịch bản & SSOT)**: Lấy `story-bible.md` và `script.md` làm chân lý tối thượng (Single Source of Truth).
2. **`/sw-premise-theme`, `/sw-genre-anatomy`, `/sw-story-structure`, `/sw-truby-anatomy`**: Đảm bảo mỗi cảnh phục vụ đúng Premise, Genre Beats và 22 bước cấu trúc hữu cơ.
3. **`/sw-character-conflict`**: Thể hiện rõ mục tiêu (Want vs. Need), ma trận đối kháng và triệu chứng cơ thể hữu hình trong `characters[].state`.
4. **`/sw-scene-craft`**: Điền đầy đủ khối `dramatic_craft` (`beat`, `value_turn`, `subtext`, `prop_and_detail`).
5. **`/sw-dialogue`**:
   - Giữ nguyên văn 100% lời thoại từ `script.md`, khớp cứng số từ theo **Rule 49** (`4s: 0 hoặc 6–8 từ`; `6s: 12–15 từ`; `8s: 18–22 từ`; `10s: 24–28 từ`).
   - Mỗi nhân vật có thoại được gán một Voice ID Pinhole riêng trong `speech.voices` (`skills/fk-film/references/voice-bible.md` §0).
   - Cấm thoại giải thích lộ liễu (*on-the-nose exposition*), cấm từ khóa mua bán/tiền bạc gây ghost op.
6. **`/sw-format-adaptation`**: Chuyển hóa hành động kịch bản thành ngôn ngữ nghe-nhìn điện ảnh 35mm thuần túy.

### B. Hệ Thống Cinematic Subagents (`fk-*` — BẮT BUỘC 100%)
7. **`/fk-storyboard` (Rule 65, Rule 69, Rule 74)**:
   - Cảnh chuyển / mở đầu (Rule 65 Loại 2): Dùng `start_frame.type = "STORYBOARD"`, khối `storyboard` chứa câu khóa `"STORYBOARD OF FOUR MOMENTS IN TIME"` trỏ chip `{{ref:<CLIP> Storyboard}}`.
   - Cảnh nối tiếp trực tiếp cùng góc máy (Rule 65 Loại 1): Dùng `start_frame.type = "PREV_LAST_FRAME"`.
   - **Rule 74**: Chuyển giữa các panel khác góc máy bằng **crisp hard cuts** tại đúng mốc giây (góc máy lệch `> 45°–90°`); cô lập nhân vật xuất hiện một mình (`Strictly [Name] alone in this shot; [Other] is completely off-screen`); khóa `SPATIAL LOCK (INSIDE vs. OUTSIDE)`; cú máy chỉ tay (`Point Shot`) tách rời với cú máy lộ mục tiêu (`Reveal Shot`) qua Hard Cut; nhân vật sợ hãi giữ mặt lộ rõ 100% (`NO hands on face/cheeks`).
8. **`/fk-character-design` & `/fk-character-bible` (Rule 46, 58, 60, 64, 72)**:
   - Đính kèm `<Tên>` + `<Tên> Body` + sinh vật/đạo cụ + bối cảnh + `<CLIP> Storyboard` vào `refs` (tối đa 7).
   - Nhắc mọi ref bằng chip `{{ref:<Entity>}}` ngay trong câu khóa; không tả lại ngũ quan hay quần áo bằng chữ.
   - Khóa cứng kích thước và trọng lượng tuyệt đối cho sinh vật/đạo cụ (`CREATURE & PROP SCALE/MASS LOCK`, Rule 74 (4)).
9. **`/fk-camera-guide`**: Góc máy ngôi thứ ba (`"third-person cinematic camera; the camera itself is never seen"`), ống kính Panavision Anamorphic 35mm, khẩu độ `deep focus f/8` (Rule 62).
10. **`/fk-action-choreography`**: Vũ đạo hành động 3 pha (Chuẩn bị $\to$ Thực thi $\to$ Thu thế), tuân thủ quán tính $p=m\cdot v$, cấm cận chiến giáp lá cà với dã thú khổng lồ.
11. **`/fk-cinematic-transitions`**: Match-on-action, whip pan, foreground wipe, J-cut / L-cut.
12. **`/fk-sound-design`**: Hòa âm 3 lớp (Thoại nổi rõ trên nền + Foley hiện trường + Ambient môi trường).
13. **`/fk-prompt-lock` & `/fk-review-prompt`**: Kiểm toán toàn bộ 15 hạng mục trong Checklist B của `skills/fk-film/references/prompt-lock.md` và chạy `python tools/lint_prompt.py` đạt `errors=0`.

---

## 2. Quy Trình Thực Hiện 5 Bước (5-Step Execution Workflow)

1. **Bước 1 — Đọc SSOT (`story-bible.md`, `script_act*.md`, `storyboards_act*.json`)**:
   - Nắm vững danh sách nhân vật, Voice ID, bảng phân cảnh, thời lượng từng cảnh (`4/6/8/10s`), loại kết nối (`STORYBOARD` vs `PREV_LAST_FRAME`) và 4 panel của từng tấm Storyboard 2×2.
2. **Bước 2 — Tổng Hợp Kỹ Nghệ Điện Ảnh (`sw-*` + `fk-*`)**:
   - Chuyển hóa từng cảnh thành 13 trường chuẩn của `skills/fk-film/references/prompt-lock.md` (Mục A).
   - Áp dụng **Argument Climax Lock** (thoại đối đầu/tranh cãi phải lớn, gắt, cộc) và **Danger-Zone Urgency Lock** (thoại trong vùng nguy hiểm phải gấp gáp, dứt khoát, cơ thể luôn căng và chuyển động).
3. **Bước 3 — Xuất File `prompts_act*.json`**:
   - Lưu mảng JSON hợp lệ, sạch ký tự lỗi encoding.
4. **Bước 4 — Tự Động Kiểm Toán Qua `/fk-review-prompt` & `tools/lint_prompt.py`**:
   ```bash
   python tools/lint_prompt.py output/<slug>/prompts_act1.json
   ```
   - Nếu có bất kỳ lỗi nào, tự động sửa ngay cho đến khi đạt **`errors=0`**.
5. **Bước 5 — Visual Audit Sau Khi Sinh Storyboard 2×2 & Trình Duyệt (Rule 69 (7))**:
   - Ngay khi ảnh Storyboard 2×2 sạch được tạo và upload lấy UUID, đọc trực tiếp 4 panel thực tế trên ảnh để tinh chỉnh `video_prompt` (resolve `{{ref:...}}` thành `{{media:<uuid>|<name>}}`) khớp 100% với thể ảnh thực tế trước khi gửi sinh video.
