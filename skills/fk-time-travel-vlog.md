# fk-time-travel-vlog — Time Travel Vlog Orchestrator (Mọi Thời Kỳ, Mọi Địa Điểm)

Tạo kịch bản và dự án video vlog **DU HÀNH THỜI GIAN / POV VLOG LỊCH SỬ** kiểu *"I Time Traveled to Ancient China in 211 BC"*, *"A Day in Ancient Rome"*, *"POV You Woke Up in 1890 London"* — vlogger hiện đại cầm điện thoại/gậy selfie, rơi vào một thời kỳ lịch sử cụ thể, vừa đi vừa nói chuyện với camera và dân bản địa. Khác với `/fk-vlog-japan` (khóa cứng vào Nhật Bản + thoại tiếng Nhật), skill này dùng cho **bất kỳ thời kỳ/địa điểm nào khác** (La Mã cổ đại, Trung Hoa Tần/Hán, London thời Victoria, Ai Cập cổ đại, Ba Tư, Viking...).

Format này ăn view vì 3 thứ: **góc nhìn người thật** (mọi thứ "quay bằng điện thoại của nhân vật" → người xem thấy mình đang ở đó), **thế giới xa lạ nhưng có thật** (sự thật lịch sử bật ra qua quan sát, không giảng bài), và **đường cong cảm xúc** đi từ đời thường → quyền lực/nguy hiểm → di sản mà người xem hiện đại đã biết tên. Cảnh nào không phục vụ 3 thứ đó thì cắt.

---

## 🎭 VAI TRÒ & MỤC TIÊU

Skill này kết hợp:
1. **Khung kịch bản 7 hồi du hành thời gian** — hook giữa chợ/đường lớn → đời thường → quyền lực → cao trào nguy hiểm → hạ nhịp → di sản → kết, với tỉ lệ % thời lượng cố định (xem bên dưới).
2. **Character Bible khóa nhân vật** — mô tả cố định dán vào mọi entity/scene để giữ mặt, tóc, trang phục nhân vật giống hệt suốt video.
3. **Research Pack** — checklist sự thật lịch sử theo thời kỳ, tránh bịa sự kiện/vật dụng sai niên đại.

Skill này **gọi các skill FlowKit khác** để tự động fact-check và triển khai:
- `/fk-research` — bắt buộc chạy trước khi viết bất kỳ prompt nào, để khóa chính xác niên đại, địa danh, trang phục, ẩm thực.
- `/fk-add-material` — khóa chất liệu ảnh (`material: "realistic"`).
- `/fk-camera-guide` — chuẩn góc máy selfie/POV cho Veo 3 / Omni Flash.
- `/fk-gen-music` — nhạc nền/ambient trải liên tục (xem mục 8).
- `/fk-create-project`, `/fk-switch-project`, `/fk-upload-ref`, `/fk-pipeline`, `/fk-youtube-seo`, `/fk-thumbnail` — triển khai và chạy pipeline (xem phần 🛠️ bên dưới).

Khung kịch bản, tỉ lệ shot và nhịp beat dưới đây được rút ra từ phân tích khung-hình thật của một video cùng format đã thành công — chi tiết đầy đủ ở `.agents/skills/time-travel-vlog/references/reference-analysis.md` (tóm tắt lại ở mục "📊 Bằng chứng thực nghiệm" bên dưới). **Đọc file gốc trước khi lệch khỏi khung mặc định.**

Kết quả đầu ra tương thích 100% với pipeline của FlowKit:
- **Project API**: `POST /api/projects` (với `material: "realistic"`, entities nhân vật + bối cảnh + đạo cụ từ Character Bible)
- **Scene API**: `POST /api/scenes` — mỗi **beat** (~15s, xem mục "Bằng chứng thực nghiệm") = 1–2 scene FlowKit (mỗi scene 8s) ghép bằng `chain_type: CONTINUATION`; `prompt` cho Frame 0 + `video_prompt` chia sub-clip `0-3s`, `3-6s`, `6-8s`
- **TTS Engine**: Tạo giọng đọc qua OmniVoice (`POST /api/videos/{vid}/narrate`) nếu dùng lồng tiếng thay vì khẩu hình native

---

## 📐 NGUYÊN TẮC CỐT LÕI (BẮT BUỘC TUÂN THỦ)

### 0. Đầu vào — tối đa 1 lượt hỏi, còn lại dùng mặc định và ghi rõ giả định

| Thông số | Mặc định |
|---|---|
| Thời kỳ + địa điểm + năm cụ thể | **bắt buộc** — cấm chung chung ("La Mã cổ đại"), phải ghi rõ ví dụ `Rome, 79 AD` / `Xianyang, Qin dynasty China, 211 BC` |
| Độ dài | Long-form ~10 phút ≈ 35–40 beat × ~15s (mỗi beat = 1–2 scene FlowKit 8s nối `CONTINUATION`); Shorts 40–48s ≈ 3–4 beat |
| Ngôn ngữ thoại | English mặc định; dân bản địa nói tiếng địa phương/cổ nếu cần kịch tính, có phụ đề trong `narrator_text` |
| Nhân vật | Vlogger ngoại quốc ngoại hình nổi bật, **mặc trang phục đúng thời kỳ ngay từ clip đầu tiên** — không có cảnh "vừa rơi xuống" mặc đồ hiện đại (xem mục 2) |
| Tỉ lệ khung | VERTICAL 9:16 (Shorts) hoặc HORIZONTAL 16:9 (long-form) |
| Material | `realistic` (bắt buộc, xem `/fk-add-material`) |

Chỉ học format; không sao chép tên, ngoại hình hay lời thoại nhân vật của kênh gốc mà user đưa làm ví dụ.

### 1. Khung "Time Capsule" — Phải chính xác tới năm
- **CẤM** dùng từ chung chung ("thời phong kiến", "cổ đại") — AI sẽ trộn lẫn nhiều thời kỳ/trang phục du lịch hiện đại.
- **BẮT BUỘC** chỉ định rõ thành phố + năm trong mọi `description`/`prompt`: `Rome, 79 AD` / `Xianyang, Qin dynasty China, 211 BC` / `London, 1890`.
- Chi tiết lịch sử phải qua `/fk-research` trước — vật dụng/món ăn xuất hiện sai niên đại (vd: ớt, khoai tây ở châu Á/châu Âu trước thế kỷ 16) là lỗi thường gặp nhất.

### 2. Character Bible — khóa nhân vật xuyên suốt (dán nguyên văn vào entity `description`)
Gồm: mặt (tuổi, dáng mặt, mắt, tàn nhang/nốt ruồi), tóc (màu, kiểu búi, trâm/phụ kiện), trang phục thời kỳ (kiểu áo, màu, cổ áo, thắt lưng — **KHÔNG nhuộm màu/vải công nghiệp hiện đại**), thiết bị (gậy selfie ngắn + điện thoại góc siêu rộng 0.5x, tay cầm máy lọt khung), giọng (`voice_description`: tông, tốc độ, thì thầm khi sợ).

Điểm then chốt (kiểm chứng từ video mẫu — xem "Bằng chứng thực nghiệm"): nhân vật **mặc đồ thời kỳ ngay từ khung hình đầu tiên**, KHÔNG có cảnh mặc đồ hiện đại rồi đổi đồ. Yếu tố gây tò mò/"người lạ" nằm hoàn toàn ở **ngoại hình** (tóc màu nổi, người ngoại quốc) chứ không nằm ở quần áo — dân bản địa nhìn tò mò nhưng nhân vật vẫn "hòa nhập" về trang phục. Cách này cho phép nhân vật đi khắp nơi mà không bị lộ ngay, để dành căng thẳng cho cao trào.

Mặc đồ hiện đại + cảnh "vừa rơi xuống"/đổi đồ (kiểu `/fk-vlog-japan`) là một **biến thể phong cách tùy chọn**, không phải mặc định — chỉ dùng khi user yêu cầu rõ hiệu ứng hài "lạc loài". Mặc định của skill này là bỏ thẳng vào thế giới từ giây 0, không có cảnh du hành/đổi đồ nào cả.

### 3. Strict Ethnicity Lock & Period Lock
- Mọi người xuất hiện trong khung (người đi đường, người bán hàng, lính canh, quý tộc) phải **đúng chủng tộc bản địa của thời kỳ/địa điểm đó** — nghiên cứu qua `/fk-research` trước khi viết `description`.
- **PERIOD LOCK**: cấm rập khuôn điện ảnh sai (vd: mũ sừng Viking), cấm vật liệu/kiến trúc/trang phục lệch niên đại. Ánh sáng dùng đuốc/đèn dầu, tránh nguồn sáng không đúng thời đại.
- Hình phạt/chiến tranh chỉ ám chỉ, không mô tả máu me — vừa đúng lịch sử vừa tránh bị Veo từ chối (`UNSAFE_GENERATION`) và YouTube hạn chế quảng cáo. Xem bảng từ ngữ an toàn trong `fk-create-project.md`.

### 4. Research Pack — 10–15 beat sự thật thật (điền trước khi viết scene)
Ưu tiên khi chọn beat:
- Chi tiết thị giác **trái với hình dung phổ biến** (vd: tượng binh mã từng được sơn màu rực rỡ) — khoảnh khắc "wow" người xem đem đi bình luận/chia sẻ.
- Chi tiết cho POV xúc giác: cầm, nếm, sờ, đong (hạt kê, thẻ tre, giáp, kiếm, tiền xu).
- Chợ & tiền tệ, đồ ăn thường ngày, luật lệ & hình phạt (beat căng nhất), nghề nghiệp/lao dịch, tín ngưỡng, vệ sinh (beat hài hiệu quả), vị trí phụ nữ trong xã hội (tạo xung đột nếu vlogger là nữ).
- Sự kiện/công trình người xem đã biết tên để làm điểm đến cuối (Colosseum, Vạn Lý Trường Thành, Big Ben...).

Không chắc → cho nhân vật nói dạng suy đoán: "I think...", "historians say...", "apparently...".

### 5. Cấu trúc kịch bản 7 hồi theo % thời lượng

| % thời lượng | Hồi | Nội dung |
|---|---|---|
| 0–5% | Hook | Giữa chợ/đường lớn, câu đầu nói rõ đang ở đâu, năm nào, và lời hứa của video. Vào thẳng thế giới từ giây 0 — khung đầu là chuyển động mạnh sát ống kính (bánh xe, ngựa) rồi mở ra nhân vật giữa đám đông. |
| 5–40% | Đời thường | Chợ, đồ ăn (1 cảnh máy dựng cố định ngồi ăn), nghề thủ công, hành chính — mỗi beat 1 sự thật mới |
| 40–55% | Quyền lực | Quân đội, công trường, lính canh — tăng quy mô và căng thẳng |
| 55–70% | Cao trào nguy hiểm | Một sự kiện lớn (vua đi qua, lễ, hành quyết được ám chỉ) → bị để ý → trốn/chạy/cưỡi ngựa thoát |
| 70–75% | Hạ nhịp | Đi nhờ xe, trò chuyện với người tốt bụng, cảnh đồng quê |
| 75–95% | Di sản | Điểm đến người xem đã biết tên, reveal dần: nhìn từ xa → xưởng làm → chạm tay → toàn cảnh khổng lồ |
| 95–100% | Kết | Máy dựng cố định, ngồi tĩnh lúc hoàng hôn, nói suy nghĩ; mồi tập sau |

Shorts: hook (1) → 2–3 beat đời thường/wow (2–4) → nguy hiểm hoặc reveal (5) → câu kết cliffhanger (6).

**Quy tắc thoại trong `video_prompt` (sub-clip 8s chuẩn FlowKit)**
- Chia `video_prompt` theo `0-3s: ... 3-6s: ... 6-8s: ...`, để 1–2s không thoại ở đầu/cuối clip cho chuyển cảnh (khớp mối nối với scene kế).
- Một người nói/clip. Dân bản địa nói → vlogger im lặng phản ứng (mắt mở to, môi mím).
- Giọng vlog thật: câu ngắn, cảm thán, thì thầm, gọi người xem. Sự thật lịch sử nói qua quan sát, không giảng bài.
- Mỗi beat có một thứ mới: nơi mới, người mới, thông tin mới hoặc nguy hiểm mới.

### 6. Storyboard & tỉ lệ loại shot
Tỉ lệ loại shot nên giữ gần đúng vì chính tỉ lệ này tạo cảm giác "máy của nhân vật":
- **~65%** selfie góc siêu rộng (front camera 24–28mm), cánh tay/gậy lọt khung, vừa đi vừa nói.
- **~15%** POV mắt nhân vật, thấy tay cô tương tác với đồ vật/người (không thấy mặt — dùng cho beat xúc giác).
- **~10%** sau gáy / qua vai — chủ yếu để làm chuyển cảnh (xem mục 7).
- **~5%** máy dựng cố định (ăn uống, kết).
- **~5%** toàn cảnh hoành tráng nhưng **vẫn từ vị trí nhân vật đứng** (phone giơ cao), không drone/flycam trừ khi dùng làm establishing shot đầu/cuối video (2 slot cố định, giống `/fk-vlog-japan`).

### 7. Chuyển cảnh — dùng `chain_type` + `transition_prompt` của FlowKit thay CapCut thủ công
FlowKit tự lo việc nối clip qua `chain_type: ROOT|CONTINUATION` + `transition_prompt` (xem `fk-create-project.md`) — không cần Extend/Frames-to-Video/CapCut thủ công như quy trình gốc. Vẫn áp dụng nguyên tắc giấu mối nối vào `prompt`/`video_prompt`:
- **Foreground wipe** ⭐ dùng nhiều nhất: cuối scene A một vật lớn lướt sát ống kính che gần kín khung (súc gỗ, tấm ván, bánh xe, người đi ngang) → scene B mở với vật đó rời khung, lộ nơi mới. Hướng di chuyển phải khớp giữa A và B.
- **Look-away / back-of-head**: nhân vật quay đầu nhìn thứ gì đó, camera thấy sau gáy → scene B mở từ sau gáy, nhân vật quay lại, bối cảnh đã đổi.
- **Selfie flip (reveal)**: nhân vật nói "you guys… look at this" và xoay điện thoại → scene B là POV toàn cảnh hoành tráng, tay nhân vật hơi lọt khung. Dùng cho các beat "di sản".
- **Time-skip**: cùng góc/địa điểm, ánh sáng đổi (trưa → hoàng hôn → đuốc), nhân vật đổi trạng thái (mệt, lấm bụi) — thể hiện hoàn toàn bằng hình ảnh, **không dùng title card chữ** kiểu "3 HOURS LATER" (xem mục 8).
- **Jump cut khi đi bộ**: cùng nhân vật, cùng góc selfie, cùng hướng đi — không cần xử lý gì thêm, đúng chất vlog thật.
- 2 slot flycam/toàn cảnh câm cố định (không thoại, chỉ nhạc cụ truyền thống + âm thanh môi trường): ngay sau Hook và ở Coda kết thúc.

### 8. Không chữ trên màn hình, nhạc/ambient trải liên tục
Video mẫu thành công **không có bất kỳ chữ nào trên màn hình** — không title card chương, không "3 HOURS LATER", không phụ đề cứng. Mọi thông tin (địa điểm, thời gian, chuyển cảnh) truyền qua lời thoại + hình ảnh. Âm thanh (nhạc nền + ambient) **trải liên tục suốt video, gần như không có khoảng lặng** — khi lồng nhạc qua `/fk-gen-music` hoặc mix cuối ở `/fk-concat`, hạ nhạc nhỏ dưới thoại thay vì tắt hẳn giữa các scene.

---

## 📊 BẰNG CHỨNG THỰC NGHIỆM (Reference Video Analysis)

Khung kịch bản và tỉ lệ shot ở trên không phải suy đoán — được rút ra từ phân tích khung-hình thật của video *"I Time Traveled to Ancient China in 211 BC! (Vlog)"* (10:40, ~38 shot). Toàn bộ chi tiết nằm ở `.agents/skills/time-travel-vlog/references/reference-analysis.md` — **đọc file này trước khi viết kịch bản mới**, đặc biệt nếu định lệch khỏi khung mặc định ở trên.

**Số liệu chính:**
- ~38 shot / 10:40 → trung bình ~17s, trung vị ~15s. Rất nhiều mối nối cách nhau đúng ~15s → mỗi beat ≈ 1 clip 8s + Extend, hoặc 2 clip 8s nối liền mạch (khớp với ghi chú "1–2 scene FlowKit/beat" ở mục 0 và 7).
- 1 cao trào nguy hiểm duy nhất ở ~60% video (đoàn xe hoàng đế đi qua → bị lính để ý → chạy trốn), sau đó hạ nhịp rồi dồn vào reveal — đúng tỉ lệ 55–70% ở bảng cấu trúc mục 5.
- Không có cảnh "du hành" mở đầu — vào thẳng thế giới từ giây 0 bằng một vật chuyển động mạnh sát ống kính (bánh xe bò).
- Kết bằng khoảnh khắc tĩnh, phản tư (ngồi dưới gốc cây lúc hoàng hôn) — không có cảnh "quay về".

**Dòng thời gian rút gọn (minh họa tỉ lệ, không sao chép nguyên văn):**

| % video | Beat | Loại |
|---|---|---|
| 0% | Bánh xe bò sát ống kính → giữa chợ, trẻ con, lính cầm giáo | Hook vào thẳng |
| 4–9% | Đường lớn, công trường cung điện, súc gỗ khiêng ngang (wipe) | Định hướng + quy mô |
| 12–29% | POV đường bùn, quan lại viết thẻ tre, chợ rau, ăn cháo, đong hạt bằng đấu chuẩn, xưởng nhuộm | Đời thường (mỗi beat 1 sự thật) |
| ~47% | Quay gáy → đại quân đang tập trận (Reveal lớn #1) | Quyền lực |
| ~57–68% | Đoàn xe hoàng đế đi qua, dân quỳ rạp → nấp sau cột → chạy trốn qua ngõ → cưỡi ngựa thoát ra cổng thành | Cao trào nguy hiểm |
| ~70% | Đi nhờ xe bò với bà nông dân thân thiện | Hạ nhịp |
| ~74–92% | Công trường lăng mộ xa xa, xưởng gốm, tượng binh mã sơn màu rực rỡ (chi tiết ít người biết), chạm giáp/kiếm đồng, hố tượng nhìn từ trên cao | Di sản (reveal dần) |
| ~94–100% | Đi dọc hàng tượng, ngồi dưới gốc cây lúc hoàng hôn nói suy nghĩ | Đỉnh cảm xúc → Kết trầm |

Chỉ học tỉ lệ/nhịp; không sao chép tên, ngoại hình hay lời thoại nhân vật của video gốc.

---

## 🛠️ CÁCH TRIỂN KHAI TRONG FLOWKIT

### Bước 0: Kiểm Tra Kết Nối & Pre-Flight (Bắt Buộc)
Trước khi bắt đầu, đảm bảo server Python và Chrome Extension trên tab `flow.google.com` đã kết nối:
```bash
curl -s http://127.0.0.1:8100/health
# Bắt buộc trả về: {"extension_connected": true}
```

---

### Bước 1: Nghiên cứu Dữ Kiện & Khóa Mỹ Thuật
1. **Fact-check lịch sử qua `/fk-research`** (bắt buộc, trước khi viết bất kỳ prompt nào):
   ```bash
   /fk-research "Ancient Rome 79 AD daily life market food dress Pompeii"
   # hoặc: /fk-research "Qin dynasty China 211 BC Xianyang market commoners soldiers"
   # hoặc: /fk-research "Victorian London 1890 daily life market fog gaslight"
   ```
   Xác minh chính xác niên đại, địa danh, trang phục, ẩm thực, luật lệ — tránh để AI sáng tác sai lệch (đặc biệt vật dụng/món ăn lệch niên đại).
2. **Khóa chất liệu mỹ thuật qua [`/fk-add-material`](file:///c:/flowkit/skills/fk-add-material.md)**:
   - Dự án BẮT BUỘC có trường `"material": "realistic"`.
   - Hệ thống Image Material sẽ tự động áp bộ quy chuẩn: *Photorealistic RAW photograph, Canon EOS R5, 35mm lens, natural available light* và chèn negative prompt chống trôi thành anime/3D render.
3. **Quy chuẩn góc máy qua [`/fk-camera-guide`](file:///c:/flowkit/skills/fk-camera-guide.md)**:
   - Áp dụng camera selfie trước 24–28mm, nhịp walking gait nhấp nhô, và tỉ lệ shot ở mục 6 phía trên.

---

### Bước 2: Dựng Dự Án Trong FlowKit (Character Bible + Storyboard → API)
Khác với `/fk-vlog-japan` (có sẵn script kịch bản mẫu đóng gói), skill này không có script cố định vì mỗi thời kỳ/địa điểm khác nhau — dùng thẳng `/fk-create-project` với Character Bible (Bước 2 phần Nguyên Tắc Cốt Lõi) và bảng storyboard (Bước 5 & 6) vừa lập:

```bash
curl -X POST http://127.0.0.1:8100/api/projects \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Rome 79 AD - Time Travel Vlog",
    "story": "<tóm tắt 7 hồi từ storyboard>",
    "material": "realistic",
    "characters": [
      {"name": "Vlogger", "entity_type": "character", "description": "<Character Bible: mặt, tóc, trang phục thời kỳ, gậy selfie>", "voice_description": "<tông giọng>"},
      {"name": "Forum Market", "entity_type": "location", "description": "<bối cảnh từ research pack>"},
      {"name": "Selfie Stick", "entity_type": "visual_asset", "description": "<mô tả đạo cụ>"}
    ]
  }'
```
Sau đó tạo video (`POST /api/videos`) và từng scene (`POST /api/scenes`) theo đúng thứ tự storyboard — mỗi beat (~15s) dựng thành 1–2 scene 8s nối bằng `chain_type: CONTINUATION` (beat mới/đổi nhân vật-địa điểm thì bắt đầu `ROOT`) + `transition_prompt` theo mục 7. Tham khảo chi tiết định dạng `prompt`/`video_prompt`/`character_names` trong [`/fk-create-project`](file:///c:/flowkit/skills/fk-create-project.md).

---

### Bước 2.5: Xác Định & Đặt Dự Án Hoạt Động (Set Active Project)
```bash
# Kiểm tra dự án đang active:
curl -s http://127.0.0.1:8100/api/active-project

# Chuyển đổi dự án nếu cần:
/fk-switch-project <PROJECT_ID>
```

---

### Bước 3: Tải Ảnh Chân Dung Thật (Tùy Chọn)
Nếu muốn sử dụng khuôn mặt thật của bạn làm Vlogger thay vì mặt AI:
```bash
/fk-upload-ref "C:/photos/my_face.jpg" --entity "Vlogger"
```

---

### Bước 4: Chạy Toàn Bộ Pipeline Tự Động (`/fk-pipeline`)
Chạy trọn gói chỉ với một câu lệnh:
```bash
/fk-pipeline --tts --concat
```
Hệ thống sẽ tự động thực hiện tuần tự:
1. **Refs**: Lấy ảnh mặt thật đã nạp (nếu có, bỏ qua sinh AI) và sinh bối cảnh/đạo cụ còn thiếu.
2. **Videos**: Sinh từng clip video 8s theo `prompt`/`video_prompt`/`transition_prompt` đã dựng ở Bước 2.
3. **TTS**: Tạo giọng đọc tự nhiên nếu dùng lồng tiếng thay vì khẩu hình native trong video.
4. **Concat**: Ghép toàn bộ clip + âm thanh thành video hoàn chỉnh `output/<slug>/<slug>_final.mp4`.
5. **Auto SEO (`/fk-youtube-seo`)**: Tự động sinh tiêu đề hook kiểu `"I Time Traveled to ___ in ___! (Vlog)"`, mô tả 4 phần, bộ tag 3 tầng và timestamps chapters.
6. **Auto Thumbnails (`/fk-thumbnail`)**: Tự động sinh 4 biến thể thumbnail (mặt nhân vật sốc + công trình/sự kiện nổi tiếng nhất của thời kỳ) chuẩn tỷ lệ 9:16 (Shorts) hoặc 16:9 (Long-form).
