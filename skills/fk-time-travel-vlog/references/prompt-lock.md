# 🔒 PROMPT LOCK — khung `video_prompt` + checklist trước khi lưu

Đọc ở **Bước 5** của `SKILL.md`, chạy lại ở Bước 8 khi review. Thay mục 10b cũ.

> User yêu cầu: các bài học ở `production-lessons.md` (mục 11 cũ) phải được **khóa vào lúc viết prompt**, không chỉ nằm trong danh sách bài học. Mọi `video_prompt` (POST hoặc PATCH) phải dựng theo khung dưới đây và **qua đủ checklist** trước khi lưu. Clip nào không qua checklist thì sửa prompt trước, không gửi sinh.

**A. Thứ tự khối trong `video_prompt` (không đảo, không bỏ khối):**

1. **Style + góc máy** — chọn đúng 1 trong 3 loại, không trộn trong cùng clip (Rule 42):
   - *Selfie:* `"The lens sits at the end of <V>'s outstretched right arm, completely outside the visible frame and never seen; her right arm stays extended toward the lens for the entire clip, and she never reaches toward, touches, covers, taps, or points at the lens. Only her left hand is free."`
   - *POV:* `"The view is <V>'s own eyes; all recording gear is completely outside the visible frame, and her hands stay out of frame for the whole clip."` (chỉ viết "her hands enter the frame" khi sub-clip **thật sự** có thao tác tay — Bài học 50).
   - *Máy dựng cố định:* `"Static footage from a fixed viewpoint resting on <vật cụ thể>; the frame does not move; nobody touches the viewpoint. Both of <V>'s hands are free."` — dùng khi hành động cần **hai tay** (Bài học 50).
2. **`Setting:`** — địa điểm + năm + **mặt đất/thời tiết** (tuyết, băng) + **giờ & ánh sáng khớp clip trước và sau** + vật liệu thời kỳ. Nội thất luôn có câu khóa bếp: `"an open fire in a shallow sunken hearth ringed with stones in the earth floor; no fireplace, no chimney, no brick or built wall, no grate, no metal objects."` (Bài học 53, Scene 15/27/28/53).
3. **`Everything is already in place from the very first frame:`** — liệt kê **mọi người, sinh vật, đạo cụ** sẽ xuất hiện trong clip, vị trí và khoảng cách của từng thứ ở giây 0, kèm `"stays in that same spot; never appears suddenly, never vanishes"`. Ghi **số lượng** (`"exactly one spear / one cup"`) và **tay nào cầm**. (Bài học 48)
4. **`Shot:`** — bố cục khung (ai ở 1/3 nào, thấy tới đâu trên người).
5. **`[ID-LOCK]`** theo Rule 46 / Bài học 60 (mặt + tóc từ `<V>`, dáng + quần áo từ `<V> Body` đã mặc outfit, kèm `BODY LOCK` & `OUTFIT LOCK`; mẫu ở `character-bible.md` mục 5) + câu khóa mũ (Bài học 52 điểm 2b) + câu `"From the very first frame to the last, <V> is fully dressed in the complete outfit: ... No part of the outfit appears, disappears or changes."`
6. **Miệng nhân vật phụ** khi họ hiện mặt: không có thoại → khóa miệng `"<Local>'s lips stay closed for the entire clip; ... The only moving mouth in the frame is <V>'s."` (Bài học 49). Có thoại ngôn ngữ không hiểu được → ghi rõ sub-clip họ nói, giọng (`deep, gravelly male voice — guttural non-English sounds, no recognizable words`) và `<V> stays silent while he speaks` (`character-bible.md` mục 4).
7. **`0-3s / 3-6s / 6-8s`** — mỗi đoạn: hành động có **nguyên nhân vật lý** + nhắc lại 1 chi tiết outfit (cổ lông / cổ V đan dây / thắt lưng) + thoại.
8. **Câu kết:** `"Pure front-facing selfie view; the shot never switches to a third-person view. Only <V> speaks English; nobody speaks over anyone else. No subtitles or text appear in the frame. Real amateur footage, not a 3D render."` + với POV/cảnh rộng: `"The image is clean footage only: no on-screen interface, no recording indicator, no battery icon, no zoom label, no names, no text or symbols."`
9. **`Audio:`** cuối cùng.

**B. Checklist — đọc lại từng `video_prompt` trước khi lưu (mỗi dòng phải trả lời "có"):**

| # | Kiểm tra | Bài học |
|---|---|---|
| 1 | Chỉ 1 loại góc máy; selfie thì cánh tay phải giữ máy suốt clip, mọi thao tác chỉ bằng **tay trái** | 41, 42, 50 |
| 2 | Hành động cần **2 tay** (trượt, chống tay, kẹp tay vào nách, ôm vật nặng) → đã chuyển sang POV hoặc máy dựng cố định | 50, Scene 27/45 |
| 3 | Mọi người/vật/sinh vật trong sub-clip đều đã có mặt trong khối "already in place" với vị trí + khoảng cách ở giây 0 | 48, Scene 2/14/39/73 |
| 4 | Không giao hành động cho người không có trong khung; chuyển đồ vật tả từng bước tay (đưa → đỡ bằng tay nào → tay kia buông) | 48, Scene 14/15 |
| 5 | Không nhắc tên món đồ trên người (mũ, găng, khăn) trong sub-clip nếu không muốn nhân vật thao tác với nó; mũ đã khóa "luôn để xuống" | 52, Scene 21/62 |
| 6 | Đạo cụ chức năng (găng, áo) tả **động tác mặc/xỏ trước**, buộc dây sau, khoe ngang ngực | 45, 46 |
| 7 | Người bản địa hiện mặt + vlogger có thoại → selfie qua vai; người bản địa không thoại thì khóa miệng, có thoại thì ở sub-clip riêng, ngôn ngữ không hiểu được, giọng ghi rõ; POV thoại ngoài khung chỉ khi không thấy mặt người | 49, character-bible §4, Scene 13/53 |
| 8 | Ngã/trượt/va chạm có **nguyên nhân vật lý** và **máy chịu hậu quả** (rung, chúi, văng); không ngã khi không gấp | 51, Scene 1/45 |
| 9 | Vật nặng (tấm da cửa, đá) chỉ chuyển động khi có tay tác động, không giao cho "gió" | 50, Scene 9 |
| 10 | Hai sinh vật cùng lông/màu không chạm nhau (vòi–voi con…); câu `"each animal is a separate body; they never overlap or merge"` | Scene 36 |
| 11 | Sinh vật tuyệt chủng tả đặc điểm loài + loại trừ loài giống (`"not an African elephant"`, `"never horses or bison"`) | 53, Scene 38/48 |
| 12 | `Setting:` có năm, địa điểm, tuyết/băng, ánh sáng khớp clip liền trước/sau; nội thất có câu khóa bếp trũng | 53, Scene 15/27/28/48 |
| 13 | Clip nối hành động mở bằng đúng trạng thái cuối clip trước (vị trí, tư thế, ánh sáng, mối nguy) và **không đi trước** clip sau về thời gian | 44, 51, Scene 43/70 |
| 14 | Muốn nhân vật nhìn thấy thứ ở phía sau → thứ đó đã nằm trong khung từ giây 0 (không đổi phông khi quay đầu) | 42, Scene 70 |
| 15 | Tối đa 3 ref cho cảnh có vlogger: `<V>` + `<V> Body` (đã mặc outfit của tập) + 1 ref bối cảnh/sinh vật; ref sinh vật đang đe dọa phải có trong cảnh đó; không có entity `<V> Outfit` | 47, 51, 60, Rule 46 |
| 16 | Không có từ `phone`, `smartphone`, `camera` (đạo cụ), `selfie stick`, `device`, `screen`, `gimbal`; không dùng dòng `Negative:` | 40, memory |
| 17 | Không còn câu mẫu thừa bị lặp (`only her bare empty hand enters...`, `Wearing the exact outfit from reference image`) ở clip không dùng tay | 50, Scene 67 |
| 18 | **Nhịp gửi request:** **mọi request tới Flow** (sinh ảnh/video, upscale, upload ảnh ref, tạo project, poll trạng thái, đọc media) cách nhau **ngẫu nhiên 45–60s** — server đã khóa sẵn (`FLOW_GENERATION_MIN/MAX_INTERVAL_S`); script tự gửi thì dùng `random.uniform(45, 60)`, dừng ngay khi gặp `UNUSUAL_ACTIVITY` hoặc `QUOTA`. Video: mỗi lần 1 video, chờ video trước xong rồi ~30s sau mới gửi tiếp (user chốt 2026-10-07) | 54 |
| 19 | **Khóa tóc cụ thể theo ảnh ref:** vị trí cột tóc (`tied at the crown of her head, not low at the nape`), mái (`wispy curtain bangs parted in the middle that cover the edges of her forehead and frame both cheeks`), `never slicked back`; có gió thì ghi `wind only makes the ponytail swing, the bangs stay over her forehead` — không viết tóc bị gió `whip` | 55 |
| 20 | **Cảnh POV có tay vlogger** (cầm, chạm, xỏ, đỡ đồ) → `character_names` phải có `<V>` + `<V> Body` (đã mặc outfit) để bàn tay, cổ tay áo đúng của nhân vật chính (user chốt 04/10/2026, cập nhật theo Rule 46) | Scene 45/53, 60 |
| 21 | **Đạo cụ cầm tay của nhân vật phụ** (giáo, gậy, cốc) → tạo ref riêng `<Tên> <Đạo cụ>` (vd `Torak Spear`) bằng **EDIT từ ảnh ref gốc** của nhân vật (giữ mặt + trang phục), sheet 16:9 3 góc, đạo cụ cầm sẵn trong tay; xóa logo → upload lại → dùng thay ref nhân vật trong cảnh đó | Scene 29 |

**C. Sau khi sinh — rà lỗi theo cùng checklist** khi review (`/fk-review-video` + user): trích ~16 frame/clip, đối chiếu từng dòng B; lỗi mới chưa có trong bảng → ghi bài học mới vào `production-lessons.md` **và** thêm 1 dòng vào bảng B.
