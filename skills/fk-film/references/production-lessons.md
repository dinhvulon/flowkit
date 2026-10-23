# Bài học sản xuất thực tế — góp ý của user

Đọc ở **Bước 5** của `SKILL.md` trước khi viết `video_prompt`, và khi review clip lỗi. Đây là mục 11 cũ của skill, giữ nguyên số thứ tự bài học để các tham chiếu "Bài học N" cũ vẫn đúng.

**Thứ tự ưu tiên:** CLAUDE.md > bài học có số lớn hơn / ngày mới hơn > bài học cũ. Các bài học đã bị thay được đánh dấu `[ĐÃ THAY]` ngay đầu dòng; giữ lại làm bằng chứng, không làm theo.

**Phim vs vlog (2026-10-19):** skill này giờ là skill làm **phim kể chuyện ngôi thứ ba** (`/fk-film`). Bài học chỉ đúng cho POV / selfie vlog đã chuyển sang [`vlog-archive.md`](vlog-archive.md); chỗ cũ chỉ còn một dòng `→ chuyển sang vlog-archive.md` để giữ số thứ tự. Bài học trộn cả hai có dòng *(Phạm vi: …)* ngay dưới tiêu đề, ghi phần nào chỉ áp cho vlog. Trong các bài còn lại, chữ "vlogger" đọc là "nhân vật chính", `<V>` là tên nhân vật.

---

## §1. LUẬT HIỆN HÀNH (PHIM) — đọc mục này là đủ để viết prompt

> Bảng tra nhanh cho phim (cập nhật 2026-10-19). Bảng §1 cũ của bản vlog (2026-10-12) lưu nguyên văn ở `vlog-archive.md` §2. File dưới §2 là **kho lịch sử bài học**; khi nghi ngờ, bảng này thắng. Mỗi khi chốt luật mới, sửa bảng này **trước**, rồi mới ghi bài học mới vào §2.

| Chủ đề | Luật hiện hành (phim) | Nguồn |
|---|---|---|
| **Góc nhìn** | Máy điện ảnh **ngôi thứ ba**: `third-person cinematic camera; the camera itself is never seen`, người xem vô hình. Không selfie, không POV điện thoại, không nhân vật nói với ống kính. Cỡ cảnh và cách đặt máy chọn theo nhịp kịch (`/fk-camera-guide`); cấm 2 clip liền nhau trùng cỡ cảnh + góc máy | prompt EMBERS v7, Rule 42 (4) |
| **Prompt** | Structured JSON: `camera`, `style`, `setting`, `characters`, `timeline_action`, `speech`, `post_vo`, `dramatic_craft`, `audio`, `negative_constraints` (+ `props_lock` khi cần). Viết qua `/fk-script-to-prompts`, lint bằng `tools/lint_prompt.py` (0 Critical/High) | Rule 55, 56 |
| **Độ dài clip** | **Không cố định.** Dễ lỗi → chuỗi 4s cùng bối cảnh (1 hành động/clip, khớp tư thế đầu-cuối). Dễ, không chuyển cảnh → 8s; long take / master / cảnh cuối → 10s; lưng chừng → 6s. **PATCH `duration`** sau khi POST scene | Rule 49 (0) + Bài 71, 12 |
| **Số từ thoại theo độ dài** | **4s** 0 hoặc 6–8 · **6s** 12–15 · **8s** 18–22 · **10s** 24–28 (memory: thoại 23–25 từ → clip 10s). Thiếu → dead air; thừa → cụt âm. Nói **ngay từ giây 0.0**. Mặt người nói phải thấy được khi nói | Rule 49, 54 + Bài 65, 81 |
| **Giọng** | Mỗi nhân vật có thoại một voice id riêng (danh sách 30 giọng ở `voice-bible.md` §0), ghi `speech.voices`; Slot 7 mang nhiều giọng theo thứ tự nói. Không mặc định Laomedeia (đó là giọng vlogger, Rule 24) | prompt EMBERS, Bài 13 |
| **Im lặng khi rình / ẩn nấp** | Cảnh áp sát thú, phục kích, ẩn nấp: **0 từ trên hình**, miệng khóa (`Sonic Isolation`). Lời trong đầu → `post_vo` | Rule 49 (4) |
| **Thoại ngoài hình** | Câu qua bộ đàm / điện thoại / lời dẫn → `post_vo`, thêm khi dựng. Clip im lặng không để bộ đàm hiện trên hình | Bài 99 |
| **Cảnh tranh cãi** | Nói **to, gắt, cộc** ở cả `speech.delivery` lẫn nhịp timeline; bỏ `low / quiet / voice drops / flat` | Bài 101 |
| **Thoại trong vùng nguy hiểm** | Đang cháy / bão / rượt / cứu người: **hét nhanh, khàn, không ngắt**, tách câu theo nhịp và nói xong sớm; cấm `natural pace`; thân thể căng + luôn chuyển động + một biến cố áp lực; câu cấm "never calm… no slow talking… no standing still". Nhịp chậm chỉ cho beat lặng có chủ đích | Bài 102 |
| **Cảnh cháy rừng** | Tả **cả rừng hai bên cháy đều** (thân, ngọn, cỏ mép đường, tường lửa phía sau), lửa là nguồn sáng chính; máy cầm tay **cách nhân vật 3–4 m, khung từ gối**; cấm "chỉ một hai cây cháy", cấm vật cháy bay ngang; vật rơi gần người ghi khoảng cách bằng mét + "never touches her" | Bài 103 |
| **Thoại bị chặn im lặng** | Không để nhân vật nói chuyện trả tiền / mua bán (ghost op). Ý đó đưa vào `post_vo` / phụ đề | Bài 100 |
| **Nghe thoại khi review** | Mọi lần review chạy `tools/review_dialogue.py` (Whisper) trước khi chấm điểm | Rule 67 |
| **Bộ ref nhân vật** | `<Tên>` (mặt) + `<Tên> Body <trạng thái trang phục>` (đã mặc đồ, EDIT 1 lần từ Body gốc). Không có entity Outfit riêng. Tối đa 7 ref/clip; gửi ref cho mọi thứ cần giữ nhất quán có trong khung; `character_names` là TÊN entity | Rule 46 + Bài 60, 88, 34 (ý chung) |
| **Khóa mặt & trang phục** | Nhắc chip ref ngay trong câu khóa (`{{ref:<Tên>}}`, Rule 64); không tả lại mặt / makeup / trang phục bằng chữ. Phần trang phục dễ bị model "sáng tạo" (tay áo, quần khi ngồi, gấu áo) chốt bằng câu khóa trỏ về ref | Rule 52 (2), 64 + Bài 63, 74, 78 |
| **Vật ở giây 0** | Mọi người/sinh vật/đạo cụ nằm trong khối `Everything is already in place from the very first frame`, ghi vị trí + khoảng cách + số lượng + tay nào cầm | Bài 48, 69 |
| **Gọi tên là hiện ra** | Model không hiểu phủ định: không gọi tên vật/thú/lửa/thiết bị mà mình không muốn thấy, kể cả trong thoại và audio | Bài 33 (ý chung), 73, 77, 99 |
| **Chất liệu / bột** | Có sẵn trên bề mặt từ Frame 0; chạm trực tiếp. Cấm hứng bụi/bột rơi giữa không trung | Rule 53 + Bài 64 |
| **Đạo cụ** | Một tay — một đạo cụ — suốt clip; không buông/đặt xuống giữa chừng; đạo cụ đơn nhất; một câu tả chuẩn cho đạo cụ xuất hiện ở ≥2 clip; dây hai người cùng cầm là **một sợi liền** | Bài 68, 69, 70, 94, 96 |
| **Vật cản & khoảng cách** | Ghi đường đi so với rào/cổng/xe; cảnh "suýt chạm" ghi khoảng cách bằng cm + câu cấm chạm | Bài 97, 98 |
| **Cận chiến** | **Cấm** đánh đấm/vật lộn cận chiến người vs thú lớn | Rule 51 (1) + Bài 62 (quy tắc 1) |
| **Miệng nhân vật phụ** | Không thoại → khóa miệng. Có thoại → nhịp riêng, voice id riêng, không nói chồng | Bài 49 (ý chung) |
| **Bối cảnh** | Ảnh ref bối cảnh 16:9 dùng chung cho mọi clip cùng địa điểm; sổ liên tục bối cảnh chạy một chiều | Bài 69, `shots-and-realism.md` |
| **Lửa, khói, chất liệu (anti-CGI)** | `35mm film`, documentary realism, không CGI; không khói thở / hơi nước trắng; bếp than là lớp than đỏ, nguồn sáng ghi rõ chỗ; không god rays | Rule 57, 59, 61, 62 + Bài 73, 75 |
| **Ánh sáng & da người** | Ánh sáng tự nhiên; chống glamour (không beauty glow, da thật); deep focus khi cần thấy bối cảnh | Rule 61, 62 (3) + Bài 77 (mục 1, 2) |
| **Start Frame** | Cảnh nối tiếp trực tiếp → cắt Last Frame clip trước (`PREV_LAST_FRAME`); chuyển cảnh → `GENERATE_IMAGE` có `source_media_id`, tẩy logo, user duyệt. Riêng EMBERS: refs-only r2v, không start frame (memory 2026-10-18) | Rule 63, 65 + Bài 79 |
| **Cắt cảnh Storyboard & Chống phân thân** | Storyboard 2×2 đổi góc/người ➔ BẮT BUỘC chỉ định Hard Cut dứt khoát ('crisp hard cut at second X.0 matching Panel N'); cú máy quay nhân vật B thì nhân vật A ghi rõ 'strictly off-screen and never seen'; 'negative_constraints' cấm nhân đôi/phân thân ('strictly NO duplicate characters, strictly NO multiple [Name], strictly [Other] alone in shot Y, no cloning') | Rule 74, Bài 80 |
| **Xác phân hủy / đường mòn tiền sử** | Theo Rule 59 khi phim có bối cảnh tiền sử | Rule 59 + Bài 75 |

**Kỹ thuật bổ sung từ `skills/character-scene-design-skills-main/`** (repo tham chiếu, đọc khi cần — xem con trỏ trong `character-bible.md` §7 và `shots-and-realism.md`):
- *Proportion lock → W0 turnaround contract* (`skills/character-design/SKILL.md`) — khóa tỉ lệ hình thể **trước** khi sinh sheet; chống body drift mạnh hơn nhồi tính từ vào prompt.
- *Permanent prop geometry* (cùng file) — tả đạo cụ bằng hình học + nêu rõ **nó KHÔNG phải cái gì**.
- *Scene continuity ledger* (`.agents/skills/scene-design/SKILL.md`) — tách base scene khỏi per-segment scene state để truyền trạng thái qua từng clip.

---

## §2. Kho bài học (lịch sử đầy đủ, 1–71)

Giữ nguyên số thứ tự để các tham chiếu "Bài học N" cũ vẫn đúng. Bài nào đã bị §1 thay thì §1 thắng.

**Thêm bài học mới:** mỗi lỗi gen lặp lại ghi thành MỘT bài học đánh số tiếp theo (root-cause, câu prompt sửa, bằng chứng: clip nào, bản nào) **và** thêm 1 dòng vào checklist B của `prompt-lock.md`.

Rút ra từ dự án `output/atlantis-9600bc/` (2026-09-27). Khi mâu thuẫn với phần khác của skill, **mục này thắng**.

**Quy trình**
1. **Xác nhận trước mỗi bước sinh** (ảnh ref, video, clip thử, sinh lại): nói rõ sinh gì, bao nhiêu, rồi chờ user đồng ý. Xong mỗi bước thì **dừng và đưa kết quả cho user xem** (kèm link file, bảng ghép ảnh hoặc khung hình). Không tự sinh lại khi lỗi.
2. **Chạy thử clip khó nhất trước, 1 clip**, rồi **1 clip bình thường làm mốc**, trước khi gửi cả loạt. Lỗi thường có hệ thống; sửa ở vài clip đầu rẻ hơn nhiều so với sửa cả loạt.
3. **Ảnh ref phải được user xem trước khi dùng.** Ghép bảng ảnh và đưa đường dẫn file để user tự xem.

**Ảnh ref (R2V)**
4. **[ĐÃ THAY bởi Bài học 88]** ~~Mỗi clip tối đa 3 ref; worker chỉ lấy entity `character` và `visual_asset`.~~ Hiện tại: tối đa 7 ref (Omni Flash); khi scene có `character_names`, server chọn ref theo tên, mọi loại entity (kể cả `creature`); chỉ nhánh dự phòng (scene không ghi tên) mới lọc `character`/`visual_asset`. Công trình hay bối cảnh cần giữ nhất quán (thành phố, tường thành, đền) phải khai báo là `visual_asset`.
5. **Clip nào có thành phố hay bối cảnh lớn thì phải kèm ảnh ref của chính bối cảnh đó** (ví dụ ảnh toàn cảnh thành phố). Chỉ tả bằng chữ thì model tự vẽ một thành phố khác.
6. **Mọi ảnh ref đều sinh ngang 16:9** (góp ý của user, 2026-10-01), kể cả nhân vật (sheet các góc đặt cạnh nhau). FlowKit đã sinh 16:9 cho mọi loại entity. Entity `location` **không** được worker đưa vào R2V, nên mọi bối cảnh cần giữ nhất quán phải khai báo `visual_asset`. Worker lấy `visual_asset` trước `character`, nên tổng `character_names` của mỗi clip phải ≤3 và luôn có vlogger, nếu không vlogger bị loại khỏi ref.
7. Ảnh ref không được có người, tay, đồ vật hay trang phục hiện đại lọt vào (găng tay, ủng, người mặc áo thun), không có kiến trúc lệch thời kỳ (mái vòm, tháp nhọn, lâu đài trung cổ), và không có dải màu trơn quanh ảnh.

**Viết `video_prompt`**
8. **Ràng buộc là câu khẳng định**, không dùng dòng `Negative:` (xem mục 9).
9. → chuyển sang [`vlog-archive.md`](vlog-archive.md) (chỉ áp cho POV vlog: điện thoại là máy quay, không viết chữ `phone`).
10. → chuyển sang [`vlog-archive.md`](vlog-archive.md) (shot selfie không dùng vật lướt qua ống kính).
11. **Chống hình kiểu 3D ở cảnh thần thoại hoặc thảm họa** (model chỉ biết những cảnh này qua phim và game):
    - mở prompt bằng khối "footage thật": `raw unedited amateur video, looks like real footage posted online, not a movie`, rung tay, auto-exposure, nhiễu nén, giọt nước trên ống kính, ánh sáng bệt;
    - tả bằng vật liệu có thật (ví dụ "tường ốp tấm đồng đỏ cũ, xỉn màu" thay vì "orichalcum phát sáng"); tên thần thoại chỉ để trong lời thoại;
    - giảm độ hoành tráng: cảnh ở xa, bị mưa hoặc sương che, khung lệch;
    - nhưng **vẫn phải kèm ảnh ref bối cảnh** (quy tắc 5), nếu không sẽ mất nhận diện (ví dụ Atlantis thành làng chài Anh).

**Kỹ thuật FlowKit**
12. `POST /api/scenes` không nhận `duration`; phải `PATCH {"duration": <4|6|8|10>}` theo cột `Dur` của storyboard (thiếu thì âm thầm ra clip 10s).
13. Mỗi clip chỉ có 1 giọng, lấy từ entity **đầu tiên theo thứ tự DB** có `voice_description`. **Chỉ nhân vật chính khai báo voice**; khai báo cho nhân vật phụ thì giọng họ sẽ đè lên thoại của nhân vật chính. *(Phim nhiều người nói: mỗi nhân vật có voice id riêng trong `speech.voices`, Slot 7 mang nhiều giọng theo thứ tự nói (prompt EMBERS, `voice-bible.md` §0). Câu "chỉ nhân vật chính khai báo voice" là luật của vlog một giọng.)*
14. Sinh lại một scene R2V đã COMPLETED: PATCH `horizontal_video_status: PENDING` rồi gửi `GENERATE_VIDEO_REFS` (không có `REGENERATE_VIDEO_REFS`).
15. Ảnh do Flow sinh luôn có logo ✦ ở góc dưới phải (tâm khoảng `(W-98, H-97)`). Xóa bằng `tools/remove_watermark_from_image.py` (đã sửa ngưỡng ngày 2026-09-27), rồi **mở ảnh ra kiểm tra**. Ảnh không phải do Flow sinh (ví dụ bảng ảnh ghép của user) thì tool có thể đoán sai vị trí.
16. Google chặn sinh tự động (`UNUSUAL_ACTIVITY`) → làm theo Bước 4.9. Đổi tài khoản Google thì phải tạo project mới (project và media thuộc tài khoản đã tạo ra chúng).

19. **Không có gì tự hiện ra giữa clip:** thứ được "reveal" (thành phố, tường thành, tượng…) phải **có mặt từ khung hình đầu**, chỉ lộ ra nhờ nhân vật dịch sang bên hoặc máy xoay tới, và đứng yên một chỗ. Viết rõ vị trí của nó ở giây 0 (ví dụ `to the right of her head, far across the water, the city is already visible on the horizon`) và thêm câu `nothing pops into view`. Nếu tả nó ở mốc thời gian sau, model sẽ cho nó xuất hiện ở mốc đó (lỗi S31 Atlantis).

20. **Ghi rõ hướng và tốc độ của mọi thứ đang di chuyển** (thuyền, xe, ngựa, người chạy): đi về đâu, nhanh cỡ nào, và hệ quả trong khung hình (ví dụ `the boat moves only at slow rowing speed and away from the city, so the city stays the same size or slowly shrinks and never gets closer`). Tả cả chuyển động vật lý thật (thuyền nhấp nhô và lắc theo sóng, không lướt đi; người chèo ngồi quay mặt về phía đuôi thuyền). Bỏ trống thì model chọn kiểu kịch tính và sai vật lý (lỗi S31 Atlantis: thuyền chèo lao về phía thành phố như thuyền máy).

21. **Bảng vật lý phải được user duyệt trước khi viết Clip JSON** (mục Định dạng output, bước 5b): mỗi clip ghi máy đặt ở đâu và nhìn về đâu, có gì trong khung ở giây 0, mọi vật di chuyển (hướng, tốc độ, hệ quả trong khung), chuyển động vật lý thật, và ai hoặc cái gì rời khung bằng cách nào. Nội dung bảng được viết thành câu trong `video_prompt` (quy tắc 19, 20). Đây là chỗ bắt lỗi vật lý rẻ nhất: sửa trên giấy, không tốn credit.

22. → chuyển sang [`vlog-archive.md`](vlog-archive.md) ([ĐÃ THAY] sheet nhân vật vlogger khóa trang phục).

23. → chuyển sang [`vlog-archive.md`](vlog-archive.md) (cấm `selfie-stick`, câu khóa cánh tay selfie).

24. → chuyển sang [`vlog-archive.md`](vlog-archive.md) (100% First-Person POV của vlogger, bàn tay trống).

25. → chuyển sang [`vlog-archive.md`](vlog-archive.md) (vlogger giữ máy khi chạy và nhảy).

26. **Khóa cố định nền đất cho cảnh trên cạn (bài học S11 Atlantis):**
    - Với các cảnh đứng trên bờ đá, suối khoáng, thềm gạch: Bắt buộc ghi rõ `Mia stands firmly on a solid stone terrace/ground; zero vehicle or boat motion; background structures remain completely static`. Tránh mô tả chung chung về nước chảy khiến AI làm nền trôi bồng bềnh như đang trên thuyền hay cầu di chuyển theo thuyền.

27. **Cơ học truyền lực & Điểm neo vững chắc (Force Transmission & Structural Ground Anchoring) (bài học S28–S30 Ice Age 20,000 BC):**
    - **CẤM để cơ thể người (chân, tay, vai) làm điểm tì chống chịu lực trực tiếp** từ động vật khổng lồ hoặc vật cản nặng hàng tấn (`human boot → spear → mammoth`). Động lượng $p = m \times v$ sẽ nghiền nát hoặc hất văng người.
    - **Đường truyền lực đúng:** `Incoming force → Weapon/Object → Timber barrier/Brace → Frozen Ground/Boulders`. Giáo cắm vào rãnh ngang của dầm gỗ chắn nặng (`heavy timber brace`), tựa vào súc gỗ ngang neo giữa các tảng đá đóng băng.
    - **Chiến thuật thực tế:** Người tiền sử không "chặn đứng" con voi bằng sức người; họ dùng **khe hẹp + mặt băng trơn + chướng ngại vật kiên cố** để ép động vật mất bám, trượt ngang và bẻ hướng tháo lui (`deflection, not direct stop`).

28. **Động lực học Megafauna & Quán tính chuyển động thứ cấp (Megafauna Biomechanics & Heavy Inertia) (bài học S20, S22, S25, S27, S29 Ice Age):**
    - Động vật lớn (voi ma mút, tê giác lông mượt, khủng long) có **quán tính thân hình cực lớn (`heavy body inertia`)**: chân nén tuyết/đất trước khi thân chuyển động; tai, vòi, lông dài có độ trễ chuyển động thứ cấp (`delayed secondary motion`).
    - **CẤM phanh khựng lại cách mũi giáo vài bước như ô tô có ABS** (`skidding to a halt just feet away`). Trên mặt băng/bùn: chân trước mất bám (`loses traction on glazed surface`), thân hình lảo đảo chao đảo cố lấy lại thăng bằng (`lurching sideways to regain balance`), trượt ngang và bẻ hướng.
    - **Không tả thú "vung ngà như kiếm" (`brandishing tusks`)**, mà là hất đầu tự vệ (`tossing its head defensively, tusks naturally sweeping through snow/brush`). Khi kiếm ăn, ngà chỉ thi thoảng ủi tuyết cạn (`occasionally pushing through shallow snow`).
    - **Phân tầng giải phẫu lông:** Lớp lông ngoài cứng dài (`long coarse guard hairs in uneven strands`) phủ trên lớp lông tơ ngắn dày cách nhiệt (`dense shorter woolly undercoat`).

29. **Vật lý chất liệu, Biến dạng & Nhiệt động học (Material Deformation & Thermodynamic Realism) (bài học S6, S8, S11, S14, S15, S38, S39, S41 Ice Age):**
    - **Nhiệt truyền dần, không tức thì:** Thả đá nung đỏ vào túi nước không làm nước sôi bùng nổ tức thì (`instant violent boil`), mà gây sủi bọt cục bộ quanh viên đá (`rapid localized bubbling around the submerged stone`) và hơi nước bốc lên tăng dần theo đối lưu nhiệt.
    - **Biến dạng vật liệu:** Da thú cong nhẹ dưới áp lực mũi kim khâu (`hide flexes slightly around needle`); đập xương tạo các vết nứt lan tỏa từ điểm va chạm (`cracks radiate from impact point`) rồi mảng yếu mới vỡ toác bốc khói; màng da trống rung nảy rõ rệt theo từng nhịp gõ (`drum membrane visibly flexes with each strike`).
    - **Vân đá tự nhiên:** Lưỡi dao/giáo đá lửa có vân gãy hình vỏ sò tự nhiên (`conchoidal fracture patterns`), tránh tả "như thủy tinh" làm AI vẽ thành kính. Tượng ngà có độ bóng satin mờ với vết ghè đá lửa và bề mặt hơi gồ ghề (`subtle satin sheen, microscopic tool marks and uneven surface`).
    - **Khí động học:** Hơi thở trong −35°C tan biến nhanh trong không khí lạnh (`dense short-lived breath vapor that dissipates rapidly`), không đọng thành khói; khói bốc theo đối lưu nhiệt và bị gió lạnh làm xáo trộn; tàn lửa bay theo luồng khí nóng rồi nguội dần và tắt.

30. **Cử động nhân vật & Quang học Smartphone chân thực (Character Action & Dynamic Smartphone Optics) (bài học S18, S26, S27, S33, S37, toàn bộ 45 cảnh):**
    - *(Phạm vi: ý "Quang học Smartphone" và "Động học camera chuyển động" chỉ áp cho POV vlog, xem [`vlog-archive.md`](vlog-archive.md); ý di chuyển trong tuyết sâu, không chạy lùi khi tháo chạy, cân bằng sáng áp cho phim.)*
    - **Di chuyển trong tuyết sâu:** Người chạy trong tuyết ngập đầu gối không thể lướt nhanh, mà sải bước nặng nhọc với bước chân rút ngắn (`struggles through knee-deep powder with shortened, heavy strides, boots sinking deep`). Dấu chân nén tuyết sâu với gờ tuyết đùn cao xung quanh mép (`raised rim of displaced snow`).
    - **Không chạy lùi khi tháo chạy:** Vừa chạy tới vừa xoay người ngoái nhìn (`runs forward while twisting upper body and looking back over shoulder`), tránh chạy lùi trên địa hình nguy hiểm.
    - **Quang học Smartphone:** Bỏ câu lệnh cứng nhắc "zero lens distortion", chuyển sang `natural wide-angle handheld perspective, no exaggerated fisheye distortion` (không dùng chữ `smartphone`, xem bài 33).
    - **Động học camera chuyển động:** Khi nhân vật chạy hoặc vận động mạnh, bắt buộc tả: `handheld smartphone footage with natural vertical bounce synchronized to each footfall, slight rotational lag when turning, and realistic motion blur`.
    - **Cân bằng sáng:** Cực quang hay ánh trăng không chiếu sáng rực như đèn neon, mà chỉ tạo ánh xanh nhạt tinh tế trên tuyết và chóp mái, lửa trại/đuốc vẫn là nguồn sáng chính.

31. **Mô hình Prompt 5 Tầng (5-Layer Physical Prompt Architecture):**
    - Mọi cảnh hành động đều tuân thủ 5 tầng:
      - **Layer 1 (Primary Motion):** Hành động chính của chủ thể.
      - **Layer 2 (Force & Traction):** Lực tiếp xúc, ma sát và độ nén bề mặt.
      - **Layer 3 (Secondary Motion & Inertia):** Quán tính thân hình, độ trễ chuyển động của tóc, lông thú, quần áo, tai/vòi.
      - **Layer 4 (Environment/Material Response):** Biến dạng vật liệu, gãy vỡ, đối lưu khói lửa, mảnh vỡ văng tung tóe.
      - **Layer 5 (Camera Dynamic Response):** Độ nảy dọc theo bước chân, độ trễ xoay góc, nhòe chuyển động tự nhiên.

32. **Tính liên tục của Đạo cụ & Vật lý giữa các cảnh (Physical & Prop Continuity):**
    - Khi các cảnh nối tiếp nhau (ví dụ: gắp đá nung S10 → đun nước S11 → uống nước ấm S12), kích thước viên đá, màu sắc than hồng, túi nước và nhiệt độ phải đồng nhất xuyên suốt chuỗi cảnh.

33. → chuyển sang [`vlog-archive.md`](vlog-archive.md) (điện thoại hiện ra lặp lại). Ý chung vẫn áp cho phim: model không hiểu phủ định, gọi tên một vật (kể cả để cấm) là mời nó vào khung (Bài 73, 77, 99); kẻ đuổi ghi khoảng cách cố định bằng câu khẳng định; biểu cảm sợ hãi khóa bằng chi tiết mặt (`wide-eyed terror, mouth open, no smile`).

34. → chuyển sang [`vlog-archive.md`](vlog-archive.md) (bộ ref vlogger Ice Age, legacy). Ý chung vẫn áp cho phim: `character_names` phải là TÊN entity, không phải UUID; lưu UUID thì server rơi vào nhánh dự phòng và chỉ gửi 1 ref.

35. → chuyển sang [`vlog-archive.md`](vlog-archive.md) (rung khung hình khi vlogger tự cầm máy chạy).

36. → chuyển sang [`vlog-archive.md`](vlog-archive.md) (tả rung như camera độc lập làm mất góc selfie).

37. → chuyển sang [`vlog-archive.md`](vlog-archive.md) (chủ ngữ trong shot POV của vlogger).

38. → chuyển sang [`vlog-archive.md`](vlog-archive.md) (POV của vlogger bị người lạ chiếm khung vì `over the shoulder`).

39. → chuyển sang [`vlog-archive.md`](vlog-archive.md) (selfie nhảy/tiếp đất làm buông máy).

40. → chuyển sang [`vlog-archive.md`](vlog-archive.md) (body drift do ma-nơ-canh, thứ tự ref vlogger — legacy).

41. → chuyển sang [`vlog-archive.md`](vlog-archive.md) (BODY LOCK tôn vòng 1 / chân dài cho vlogger — trái memory 2026-10-14 "Body lock = normal figure").

42. **BỘ TỨ NGUYÊN LÝ VẬT LÝ SINH TỒN & ĐIỂM MÙ QUANG HỌC POV VLOG (bài học H2 Ice Age 16,000 BC bản v10):**
    - *(Phạm vi: mục 1, 2, 4 (động lượng, trọng tải trên sườn dốc, biến dạng tuyết) áp cho phim; mục 3 đã chuyển sang [`vlog-archive.md`](vlog-archive.md); mục 5 (chạy linter sau khi viết prompt) áp cho mọi dự án, riêng ý "đặt BODY LOCK sớm sau `Shot:`" là khung văn xuôi cũ của vlog.)*
    
    #### 1. Nguyên lý Động lượng & Quán tính cơ học ($p = m \cdot v$)
    - **Lỗi AI thường gặp ("Nhìn giả như AI"):**
      - Khi prompt mô tả: *"Nora lao mình nhảy xuống bờ sông trong khi tay vẫn giơ máy quay"*, AI sẽ hiểu theo kiểu phim hoạt hình hoặc video game: nhân vật bay lơ lửng giữa không trung (anti-gravity), cơ thể đơ cứng, không có trọng lực.
    - **Vật lý con người thực tế:**
      - Nora có khối lượng $m \approx 55\text{ kg}$, đang chạy nước rút với vận tốc $v \approx 6\text{ m/s}$ ➔ Động lượng $p = m \cdot v$ cực lớn.
      - Khi gót giày vấp phải rãnh băng (hệ số ma sát $\mu \to 0$): Chân dừng/trượt đột ngột, nhưng phần thân trên mang toàn bộ quán tính lao về phía trước.
      - Trọng tâm cơ thể (Center of Mass) vượt khỏi chân đế. Con người không thể bay, mà bắt buộc phải trải qua chuỗi phản xạ sinh học:
        1. *Loạng choạng quán tính:* Chân bước vội 1–2 bước ngắn trong tuyệt vọng để cứu thăng bằng.
        2. *Mất mômen xoắn:* Cánh tay tự do quơ loạn xạ trong không khí để tìm thăng bằng.
        3. *Sụp đổ trọng lực:* Lực hấp dẫn $F_g = mg$ kéo sụp cơ thể, ngã đập mạnh hông và đầu gối xuống mặt băng tuyết với xung lực nén lún rõ rệt.

    #### 2. Nguyên lý Tương phản Trọng tải trên Sườn dốc ($m_{\text{voi}} \gg m_{\text{người}}$)
    - **Tại sao ngã trên mặt đất bằng phẳng là sai logic vật lý & sinh tồn?**
      - Nếu ngã trên thảo nguyên bằng phẳng ngay trước mũi voi ma mút: Con voi 6 tấn với đà chạy khủng khiếp sẽ giẫm bẹp vlogger trong 0.5 giây! Cảnh quay trở nên hoàn toàn vô lý.
    - **Vật lý địa hình sườn dốc bờ sông băng ($\theta \approx 45^\circ - 60^\circ$):**
      - Bờ dốc sông băng là một mặt phẳng nghiêng có tuyết dày. Thành phần trọng lực dọc theo sườn dốc $F = mg\sin\theta$ thắng lực ma sát trượt của tuyết $F_{\text{friction}} = \mu mg\cos\theta$, biến cú ngã thành cú trượt cày dốc tuyết (Kinetic Slope Slide).
    - **Sự tương phản trọng lượng quyết định sinh tử:**
      - *Nora (55 kg):* Nhẹ, trượt cày trên lớp tuyết xốp dày xuống đáy thung lũng sông băng an toàn giống như vận động viên trượt tuyết (lớp tuyết đóng vai trò đệm giảm chấn hấp thụ động năng).
      - *Voi ma mút (6.000 kg — gấp hơn 100 lần):* Khối lượng quá khủng khiếp khiến nó không thể lao xuống sườn dốc băng tuyết trơn trượt vì sẽ gây sạt lở tuyết, gãy chân hoặc lăn đè bẹp chính nó!
      - ➔ **Chính định luật vật lý về trọng tải đã giải thích tại sao Nora sống sót và tại sao con voi ma mút bắt buộc phải phanh khựng lại trên đỉnh mép dốc!**

    #### 3. → chuyển sang [`vlog-archive.md`](vlog-archive.md) (điểm mù quang học POV vlog & "điện thoại ma").

    #### 4. Nguyên lý Biến dạng Vật liệu & Triệt tiêu Động năng (Energy Dissipation)
    - **Tuyết Kỷ Băng Hà không phải là mặt sàn bê tông cứng:**
      - *Nứt nén bề mặt (Crust Fracture):* Khi gót chân vấp và thân người đập xuống, lớp váng băng mỏng trên bề mặt nứt vỡ rạn chân chim.
      - *Bụi tuyết khí dung (Aerosolized Powder Snow):* Lực va chạm nén không khí, hất tung lớp tuyết bột xốp bên dưới thành đám mây bụi trắng xóa quanh người.
      - *Rãnh ma sát (Frictional Furrow):* Cơ thể cày một vệt lõm sâu trên sườn dốc, ma sát tuyết triệt tiêu dần toàn bộ động năng $\frac{1}{2}mv^2 \to Q$ cho đến khi người dừng hẳn lại ở bãi tuyết chân dốc.

    #### 5. Quy trình BẮT BUỘC: Prompt Self-Linter (Tự kiểm tra prompt sau khi viết xong)
    - Sau khi soạn thảo bất kỳ prompt nào (trước khi lưu DB, `clips.json` hoặc gửi API gen media), Agent BẮT BUỘC phải chạy công cụ kiểm tra tự động (`python tools/lint_prompt.py`):
      1. Quét regex cấm `\b(phone|smartphone|screen|device|selfie[- ]?stick)\b`. Nếu có, lập tức loại bỏ.
      2. Kiểm tra câu điểm mù quang học (`off-screen`, `outside the visible frame`).
      3. Kiểm tra vị trí `BODY LOCK` (phải đặt SỚM ngay sau `Shot:` trước `0-3s`).
    - **Bằng chứng thực nghiệm:** H2 Ice Age 16,000 BC bản v10 loại bỏ 100% từ "phone", camera giữ góc POV selfie hoàn hảo, tuyết phủ mặt kính chuyển cảnh mượt mà, không còn bất kỳ chiếc điện thoại ma nào xuất hiện trong khung hình.

43. → chuyển sang [`vlog-archive.md`](vlog-archive.md) (vật thể hóa máy ảnh khi quay từ sau đầu vlogger rồi xoay ra selfie). Ý chung vẫn áp cho phim: chữ `camera` làm tân ngữ của hành động (`brings the camera around`) bị hiểu là đạo cụ cầm tay; chỉ tả máy trong khối `camera`, không cho nhân vật cầm hay xoay nó.

44. → chuyển sang [`vlog-archive.md`](vlog-archive.md) (lật camera 180° giữa cam trước và cam sau trong một shot).

45. **LỖI GÃY MẠCH TƯ THẾ ĐẦU KHI CẮT NỐI HAI SHOT & KỸ THUẬT KHỚP ĐỘNG TÁC (The Inter-Scene Posture Snap & Head-Turn Match Continuity — Bài học Scene 03 -> Scene 04 Ice Age 16,000 BC):**
    
    #### 1. Hiện tượng lỗi thực tế
    - Scene 03 kết thúc ở 5-6s: Nora quay ngoắt đầu sang phải nhìn lều xương voi Mezhyrich (`At 5s she turns her head to look back at the camp, so the back of her head and ponytail fill half the frame`).
    - Nhưng Scene 04 mở đầu ở 0-3s: Prompt lại mô tả ngay Nora cầm máy nhìn thẳng vào ống kính camera thì thầm (`Nora holds the camera firmly in front-facing selfie at arm's length; she glances directly into the lens whispering nervously`).
    - **Hậu quả**: Khi nối Scene 03 và Scene 04, đầu của Nora bị giật 90 độ ngay lập tức từ quay gáy sang nhìn chính diện (Spatial Snap / Disorienting Jump Cut). Khán giả cảm thấy video bị sượng, đứt gãy mạch chuyển động và mất tính liên tục.
    
    #### 2. Root Cause (Nguyên nhân gốc rễ)
    - Do mỗi clip AI diffusion sinh độc lập, AI không có bộ nhớ tư thế khung hình cuối của clip trước. Nếu prompt của clip B không neo rõ tư thế mở đầu khớp với tư thế kết thúc của clip A, AI sẽ tự động sinh nhân vật ở tư thế cơ bản (đứng thẳng nhìn vào camera).
    - Cắt giữa 2 shot cùng cự ly (Medium Close-Up Selfie) mà tư thế đầu bị nhảy đột ngột là vi phạm quy tắc 30 độ trong dựng phim.
    
    #### 3. Quy tắc Vàng: Khớp Động Tác Liền Mạch (Match on Action / Head-Turn Continuity)
    - **Quy tắc bắt buộc khi nối 2 shot liền kề:**
      1. **Neo tư thế mở đầu ở 0-1s / 0-2s**: Clip B BẮT BUỘC phải mở đầu ở đúng tư thế kết thúc của Clip A (`0-2s: Matching the previous scene's ending, the clip opens with [Character]'s head turned looking back over her shoulder toward [Object]...`).
      2. **Thực hiện động tác chuyển đổi in-camera**: Trong chính 1-2 giây đầu của Clip B, mô tả nhân vật phát hiện đối tượng hoặc nghe thấy tiếng động, sau đó mới xoay mặt lại nhìn vào ống kính camera (`Seeing him emerge, her eyes widen and she smoothly turns her head back around to face directly into the camera lens`).
      3. **Tác dụng kỳ diệu**: Mối nối giữa Clip A và Clip B trở thành một cú cắt **Match on Action**. Khán giả nhìn thấy động tác quay đầu diễn ra mượt mà và tự nhiên, hoàn toàn triệt tiêu cảm giác giật hình (jump cut) của AI!

46. **LỖI VƯƠN TAY CHẠM ỐNG KÍNH VLOG & TƯƠNG TÁC ĐẠO CỤ TRANG PHỤC (Hand Reaching Camera Lens & Functional Prop Dressing Continuity — Bài học Scene 07 Ice Age 16,000 BC):**
    - *(Phạm vi: mục 3.1 "Khóa cấm chạm thấu kính" và động tác khoe đồ ngang ngực với camera chỉ áp cho vlog; mục 3.2 "tả hành động chức năng trước" áp cho phim (Rule 45 (2)).)*
    
    #### 1. Hiện tượng lỗi thực tế
    - Trong Scene 07, vlogger Nora trong lúc quay vlog selfie lại đưa cánh tay vươn thẳng tới sát ống kính camera/màn hình làm chắn khung hình và tạo tư thế cầm máy bất thường (đang quay lại đưa tay lên camera/màn hình).
    - Đồng thời, nhân vật phụ Alva chỉ cầm sợi dây buộc lòng thòng kéo kéo quanh cổ tay Nora mà không thực sự xỏ/đeo chiếc găng tay lông thú (fur mitten) vào bàn tay đang lạnh cóng của Nora, tạo cảm giác vô nghĩa và sai lệch chức năng sinh tồn (cột dây như dắt thú thay vì mang găng giữ ấm).

    #### 2. Root Cause (Nguyên nhân gốc rễ)
    - **Lỗi thiếu ràng buộc điểm mù cho bàn tay tự do:** Prompt chỉ cấm chung chung về camera nhưng thiếu câu lệnh khẳng định cấm vlogger vươn tay chạm/che thấu kính (`she never reaches toward, touches, covers, or points at the camera lens`). Khi nhân vật chuyển động, AI model hay cho tay vươn về phía trước theo quán tính tự nhiên, vô tình chạm vào mặt phẳng thấu kính.
    - **Lỗi mô tả đạo cụ gián tiếp (Indirect Prop Description Fallacy):** Prompt mô tả *"Alva takes the hide cord at Nora's left wrist and tugs it twice; the mitten swinging on its cord..."*. AI hiểu đúng nghĩa đen là Alva chỉ giật sợi dây thừng và chiếc găng tay đung đưa tự do ngoài không khí, chứ không nhận thức được mục đích thực tế: Alva đang mặc đồ ấm cho Nora!

    #### 3. Quy tắc Vàng: Khóa Cứng Ống Kính & Tả Hành Động Chức Năng Đạo Cụ
    - **1. Khóa cấm chạm thấu kính (Camera Touch Prohibition):**
      - Trong mọi shot vlog selfie, bắt buộc bổ sung mệnh đề khẳng định:
        `"The lens sits at the end of [Character]'s outstretched arm... completely outside the visible frame and never seen; she NEVER reaches toward, touches, covers, taps, or points at the camera lens."`
      - Bàn tay tự do chỉ hoạt động ở khu vực cơ thể (ngang ngực, bụng, hông) hoặc tương tác trực tiếp với đạo cụ/nhân vật khác, tuyệt đối không vươn về phía mặt phẳng thấu kính.
    - **2. Tả hành động chức năng trước, đạo cụ phụ sau (Functional Dressing Action First):**
      - Khi một nhân vật phụ mặc đồ, đeo găng, khoác áo choàng hay trao trang phục cho vlogger:
        - **Hành động chức năng chính:** Phải mô tả trực tiếp hành động đưa đồ vào cơ thể: *"Alva attentively holds the thick fur mitten and gently slips and slides it directly onto Nora's cold bare left hand, pulling the warm fur mitten fully over all her fingers."*
        - **Cố định phụ kiện:** Sau khi đã xỏ găng/mặc đồ xong, mới mô tả thao tác khóa dây: *"Alva fastens and snugs the soft hide wrist-cord tied around Nora's left wrist so the mitten cannot slip off."*
        - **Phản ứng tương tác tự nhiên:** Vlogger giơ bàn tay đã mặc đồ lên ngang ngực (giữ khoảng cách an toàn với camera) để khoe với người xem: *"Nora lifts her left hand—now wearing the thick fur mitten—up to chest level to display the warm mitten clearly to the camera, flexing her mittened fingers."*

47. → chuyển sang [`vlog-archive.md`](vlog-archive.md) (outfit drift với ảnh ma-nơ-canh, entity Outfit riêng — legacy).

48. **ĐỒ VẬT / NGƯỜI TỰ HIỆN RA GIỮA CLIP (Object & Person Pop-in — Bài học Scene 02, 14, 15 Ice Age 16,000 BC Part 2, user review 03/10/2026):**
    - **Hiện tượng:** Scene 02 Torak đột ngột "biến ra" ở cửa lều lúc ~4.5s. Scene 14 hòn đá + kẹp gạc lơ lửng ở frame đầu rồi tay mới xuất hiện chụp lấy; tấm da đựng nước trống rồi nước tự có. Scene 15 Nora tự nhiên cầm một cái cốc thứ hai trong khi Alva vẫn cầm cốc của mình (cuối clip Nora cầm 2 cốc).
    - **Root cause:** Prompt chỉ nhắc người/vật ở sub-clip mà nó **được dùng tới** (Torak chỉ có ở `6-8s`; viên đá chỉ có ở hành động "lowers it"), không nói nó **ở đâu từ frame đầu**. Model phải chèn nó vào giữa chừng. Prompt còn giao hành động cho người không có trong khung (Scene 14: "Alva grips the stone" trong shot POV không có Alva) hoặc tả hành động không dựng nổi ("sips from the cup in Alva's hand") → model tự đẻ thêm đạo cụ.
    - **Quy tắc:**
      1. Mọi người và đạo cụ xuất hiện trong clip phải được **đặt chỗ ngay trong đoạn Setting/Props, trước `0-3s`**: `"Everything is already in place from the very first frame: the hide basin is already full of water, the cobble already sits in the embers, Nora's own hands already hold the tongs."` / `"Torak is already part of the scene from the very first frame ... He stays in that same spot; he never appears suddenly and never vanishes."`
      2. Đếm số lượng đạo cụ: `"There is only ever one cup in the scene."`
      3. Chuyển giao đồ vật phải tả từng bước tay: người A đưa → người B đỡ bằng tay nào → tay A buông ra và để trống. Không tả "uống từ tay người khác".
      4. Câu chốt: `"Every object moves only when a hand moves it; nothing appears, vanishes or floats on its own."`
      5. Hành động trong shot POV chỉ giao cho **tay của chính vlogger** hoặc người đang hiện rõ trong khung.

49. **NHÂN VẬT PHỤ MẤP MÁY MIỆNG TRONG SHOT POV THOẠI NGOÀI KHUNG (Off-screen Voice Lip Transfer — Bài học Scene 13 Ice Age 16,000 BC Part 2, user review 03/10/2026):**
    - *(Phạm vi: cách sửa "Selfie Qua Vai" ở quy tắc 1 chỉ áp cho vlog. Ý chung áp cho phim: giọng luôn bám vào một cái miệng nhìn thấy được, nên người không có thoại phải khóa miệng, còn người có thoại phải hiện mặt ở đúng nhịp mình nói.)*
    - **Hiện tượng:** Scene 13 là POV của Nora, thoại viết `Nora's off-screen voice says`, gương mặt duy nhất trong khung là Alva → Alva mở miệng "nói" suốt clip bằng giọng Laomedeia. Vi phạm luật "chỉ vlogger nói".
    - **Root cause:** Omni Flash chỉ có 1 giọng (Slot 7) và luôn cố gắn khẩu hình vào **một cái miệng nhìn thấy được**. Khi miệng vlogger không có trong khung, nó gắn vào người bản địa duy nhất đang hiện mặt. Câu `Only Nora speaks` không đủ để khóa miệng người kia.
    - **Quy tắc:**
      1. Beat có thoại + người bản địa hiện mặt → **dùng Selfie Qua Vai** (Rule 42, mục 2b): vlogger 1/3 tiền cảnh nói bằng chính miệng mình, người bản địa 2/3 hậu cảnh; thêm `Nora`, `Nora Body` vào `character_names` (tối đa 7 ref theo Bài học 88 & Rule 46).
      2. Clip người bản địa **không có thoại**: thêm câu khóa `"<Local>'s lips stay closed for the entire clip; she never speaks or mouths words, and communicates only by frowning, shaking her head and hand gestures. The only moving mouth in the frame is Nora's."` (Cập nhật 2026-10-05: người bản địa **được** nói ngôn ngữ không hiểu được ở sub-clip riêng, mục 2b; khi đó không dùng câu khóa này mà ghi rõ ai nói, lúc nào, giọng gì.)
      3. POV thoại ngoài khung chỉ an toàn khi trong khung **không có mặt người** (tay, đồ vật, phong cảnh) hoặc người bản địa quay lưng / ở rất xa.
    - **Rà soát:** sau khi gen, lọc mọi scene có `off-screen voice` + người bản địa trong `character_names` rồi kiểm tra miệng (Part 2: 13 lỗi rõ; 53, 31 nghi ngờ).

50. → chuyển sang [`vlog-archive.md`](vlog-archive.md) (thao tác hai tay khi vlogger đang tự cầm máy). Ý chung vẫn áp cho phim: vật nặng (tấm da cửa, cánh cửa, rèm) chỉ chuyển động khi có tay tác động, không giao cho "gió" (checklist B dòng 9).

51. **NGÃ KHÔNG CÓ NHÂN QUẢ & GÓC QUAY ĐỨNG YÊN KHI NGÃ (Fall Without Cause — Bài học Scene 01 Ice Age 16,000 BC Part 2, user review 03/10/2026):**
    - *(Phạm vi: "máy phải chịu hậu quả" và "văng máy khỏi tay" ở quy tắc 2–3 chỉ áp cho vlog cầm tay; quy tắc 1 và "ngã phải có nguyên nhân vật lý" áp cho phim.)*
    - **Hiện tượng:** Clip nối ngay sau cảnh voi rượt nhưng Nora chỉ ngồi phịch xuống tuyết như chơi, không voi, không gấp gáp, khung hình ổn định, mặt luôn ở giữa; ánh sáng đổi từ hoàng hôn vàng sang trời xám; cuối clip cười tươi.
    - **Root cause:** Prompt chọn động tác an toàn "seated glissade" + khóa `viewpoint remains locked on her face` → cú ngã không có lực và không ảnh hưởng gì tới máy. Bỏ ref sinh vật đang rượt (`Woolly Mammoth`) và dùng ref bối cảnh trời xám → mất truy đuổi và lệch ánh sáng so với clip trước.
    - **Quy tắc:**
      1. Clip nối hành động phải mở bằng **đúng trạng thái cuối clip trước** (Rule 44): vẫn chạy, vẫn thấy mối nguy, cùng ánh sáng — giữ ref của mối nguy.
      2. Ngã phải có **nguyên nhân vật lý** (ủng sụt qua lớp băng ở mép dốc, vấp gờ tuyết) và **máy phải chịu hậu quả**: khung rung loạn, chúi xuống, hoặc văng khỏi tay lộn vòng rồi cắm tuyết.
      3. Theo yêu cầu user, cú **văng máy → lộn vòng → nằm trên tuyết → tuyết phủ kín thành màn trắng** là ngoại lệ hợp lệ của luật "máy khóa trong tay" — chỉ tả `"the view is flung out of her grip, spinning"`, không gọi tên thiết bị; vlogger vẫn lướt qua khung (không biến mất); màn trắng cuối clip nối thẳng vào clip sau.

52. **NHẮC TỚI MỘT MÓN TRÊN NGƯỜI LÀ MODEL SẼ THAO TÁC VỚI NÓ (Mentioned Garment Gets Used — Bài học Scene 21 Ice Age 16,000 BC Part 2, user review 03/10/2026):**
    - **Hiện tượng:** Prompt chỉ viết *"Alva glances over at Nora's fox-fur hood"* → Nora tự vòng tay ra sau kéo mũ trùm lên đầu, động tác thừa và vô lý. Cùng clip: giá phơi da có móc treo áo bằng gỗ kiểu hiện đại, hàng trăm tấm da như kho hàng.
    - **Root cause:** Bất kỳ món đồ nào được gọi tên trong sub-clip hành động (mũ, găng, khăn) đều bị model hiểu là đạo cụ cần dùng tới. "Drying racks of pelts" không có ràng buộc vật liệu nên model lấy hình ảnh cửa hàng da hiện đại.
    - **Quy tắc:**
      1. Chỉ gọi tên món đồ trên người trong sub-clip khi **thật sự** muốn nhân vật thao tác với nó. Muốn nó đứng yên thì khóa bằng câu khẳng định: `"Nora's fur hood stays down, resting on her shoulders, for the entire clip; she never touches it or pulls it up."`
      2. Phản ứng của nhân vật phụ gắn với **câu thoại / hành động**, không gắn với trang phục.
      2b. **Mũ trùm mặc định KHÔNG đội, từ đầu đến cuối video** (user chốt 03/10/2026, Scene 62 mũ tự trùm lên rồi tự tụt xuống dù prompt không nhắc tới mũ — ảnh ref outfit có mũ lông to nên model tự quyết). Mọi `video_prompt` có vlogger phải có câu khóa ngay trước `0-3s:` — `"Nora's fur hood stays down, resting on her shoulders behind her neck, for the entire clip; it is never up over her head, and she never touches it or pulls it up."` Không viết động tác kéo/gạt/cởi mũ trong bất kỳ sub-clip nào.
      3. Giá phơi, kệ, khung: ghi rõ số lượng và vật liệu thời kỳ (`"six or seven pelts stretched on frames of lashed bones and branches tied with sinew; no hangers, no hooks, no metal, no rails"`).

53. **GIAO DIỆN CAMERA HIỆN TRÊN HÌNH & PROMPT THIẾU SETTING (Camera HUD Overlay & Missing Setting — Bài học Scene 48 Ice Age 16,000 BC Part 2, user review 03/10/2026):**
    - **Hiện tượng:** Clip có chữ `REC`, biểu tượng pin, nhãn `0.5x | NORA` đè lên hình; bối cảnh thành đồng cỏ khô kiểu savan, không có tuyết; voi ma mút thành voi châu Phi tai to lông thưa.
    - **Root cause:** Dòng `Setting:` quá sơ sài (`"Lower river terrace looking up at the bluff rim, golden sunset"`) — không có năm/địa điểm, không nhắc **tuyết** → model tự chọn bối cảnh theo ảnh ref `Mammoth Steppe` (cỏ khô) và ánh "golden" thành savan. Cụm `0.5x view` + tên vlogger khiến model vẽ cả giao diện app camera.
    - **Quy tắc:**
      1. Mọi prompt (kể cả POV ngắn) bắt buộc có `Setting:` ghi địa điểm + năm + **mặt đất (tuyết phủ dày)** + giờ/ánh sáng khớp clip trước và sau.
      2. Thêm câu: `"The image is clean footage only: there is no on-screen interface, no recording indicator, no battery icon, no zoom label, no names, and no text or symbols of any kind over the picture."`
      3. Sinh vật tuyệt chủng phải tả đặc điểm loài + loại trừ loài gần giống: `"a woolly mammoth: long shaggy dark-brown hair, high domed head, small rounded ears hidden in the fur, long curved tusks; not an African elephant, no large flapping ears."`
      4. Với clip nối tiếp, ghi rõ vị trí người quay so với clip trước (Nora đã trượt xuống → `"the view stays at the bottom of the slope looking up"`).

54. **NHỊP GỬI REQUEST & BỊ GOOGLE CHẶN (Request Pacing — Ice Age 16,000 BC Part 2/3, user chốt 03/10/2026):**
    - **Hiện tượng:** Upscale nhịp 30s bị `PUBLIC_ERROR_UNUSUAL_ACTIVITY` sau 3 request; 25–35s sau 13; 40–60s sau ~20. Tài khoản mới tạo project + upload 13 ảnh ref liền trong ~1 phút → request sinh video **đầu tiên** bị chặn ngay. Mỗi phiên cookie chạy được khoảng 15–20 request liên tục.
    - **Root cause:** Server chỉ giãn 3s giữa các lệnh sinh và **không giãn upload ảnh / tạo project / poll**, nên request dồn thành burst. Tài khoản mới bị chặn ngay request sinh đầu tiên 2 lần liên tiếp (04/10) dù lệnh tạo đã giãn 30–45s → user chốt giãn **mọi** request.
    - **Quy tắc (đã khóa trong code `agent/config.py` + `agent/services/flow_client.py`):**
      1. **Mọi request tới Flow** — sinh ảnh/video, upscale, **upload ảnh**, **tạo project**, **poll trạng thái**, đọc media — cách nhau **ngẫu nhiên 45–60s** (user chốt 04/10/2026, thay cho mức 30–45s chỉ áp cho lệnh tạo). `VIDEO_POLL_TIMEOUT` nâng lên 900s cho vừa nhịp poll chậm.
      2. Gặp `UNUSUAL_ACTIVITY` → dừng gửi, báo user xóa cookie `google.com` + đăng nhập lại `flow.google.com`, rồi gửi thử **1 request** trước khi chạy tiếp.
      3. Gặp `PUBLIC_ERROR_USER_QUOTA_REACHED` → dừng hẳn; chờ quota reset hoặc đổi tài khoản (tạo project mới, upload lại ref, clone scene — prompt giữ nguyên).
      4. Sau khoảng 15 request liên tục, chủ động đề xuất user xóa cookie trước khi bị chặn.
      5. **`PUBLIC_ERROR_UNUSUAL_ACTIVITY_TOO_MUCH_TRAFFIC`** (mã `8` = `RESOURCE_EXHAUSTED`, cùng mã với hết quota) = **giới hạn lưu lượng của tài khoản**, không phải do nhiều job song song: Part 5 (04/10/2026) gặp lỗi này cả khi 3 clip đang render lẫn khi **không có job nào đang chạy** và đã nghỉ 5 phút. Xử lý: dừng, chờ 30–60 phút rồi thử **1 cảnh khác** (cả 2 lần đều rơi vào cùng 1 cảnh — loại trừ khả năng do prompt); vẫn lỗi → chờ lâu hơn/ngày mai hoặc đổi tài khoản. Vẫn nên chạy video tuần tự 1 job cho an toàn.

55. **SAI KIỂU TÓC KHI CÓ GIÓ — MẤT MÁI, ĐUÔI NGỰA TỤT THẤP (Hair Drift in Wind — Bài học Scene 25 Ice Age 16,000 BC Part 5, user review 04/10/2026):**
    - **Hiện tượng:** Ref là đuôi ngựa cột cao trên đỉnh đầu + mái thưa rẽ giữa ôm trán/má; clip ra đuôi ngựa thấp sau gáy, tóc vuốt ngược, **mất mái**, nhiều lọn xõa.
    - **Root cause:** Khối khóa chỉ có cụm ngắn `high wavy ponytail with curtain bangs`; sub-clip lại viết `her ponytail ... whip sideways in the gale` → gió mạnh được hiểu là hất tung mái và kéo tóc ra sau.
    - **Quy tắc:** Trong `IDENTITY & OUTFIT LOCK` tả tóc theo **vị trí cụ thể**: `"hair pulled up into a high wavy ponytail tied at the crown of her head (not low at the nape), with wispy curtain bangs parted in the middle that cover the edges of her forehead and frame both cheeks, plus a few loose face-framing strands at the temples; her hair is never slicked back."` + câu trước `0-3s:`: `"Her curtain bangs stay over her forehead and her ponytail stays tied high at the crown for the entire clip; wind only makes the ponytail swing, it never pulls the hair back or loose."` Cảnh có gió chỉ viết đuôi ngựa `swings`, không viết `whips`.

56. **COLD OPEN VÀ PAYOFF CẮT TỪ MỘT MASTER TAKE (One Master for Hook + Payoff — Neanderthal 51ka script v3 → v4, user review 05/10/2026):**
    - **Hiện tượng (dự báo khi review script):** Cold open C01 và payoff C56 sinh thành 2 clip riêng → nhân vật, ánh sáng, vị trí linh cẩu, nhúm mồi sẽ lệch nhau; người xem thấy "đoạn phát lại" không phải cùng một khoảnh khắc.
    - **Quy tắc:** Sinh **một** clip 10s FIXED CAM (`duration: 10`) chứa trọn khoảnh khắc: 0–2s mối nguy trong khung → hỏng → hỏng → thành công một phần → kết quả. Cold open dùng đoạn đầu tới trước kết quả → CUT ĐEN; payoff dùng 4–5s cuối. Ghi bảng giây của master trong script. Đây là clip khó nhất → sinh **đầu tiên** (Bài học 2). Clip đứng trước payoff kết bằng hướng nhìn khớp đầu đoạn phát lại (Rule 44).

57. **KHÓA VẬT LÝ QUY TRÌNH THỦ CÔNG (Process Physics Lock — Neanderthal 51ka, user review 05/10/2026):**
    - **Root cause dự báo:** Model mặc định cho "mưa tia lửa" và lửa bùng ngay khi đánh đá; vật chứa than tự cháy; người xem từng làm thật thấy giả ngay.
    - **Quy tắc:** Viết một câu khóa cho mỗi quy trình trong mục *Khóa vật lý* của script, dán nguyên vào mọi clip có quy trình đó:
      - Tạo lửa: `She strikes the pyrite in a fast glancing stroke down along the flat face of the flint biface, lengthwise. Only a few tiny, short-lived orange sparks jump from the point of contact and fall onto the dry moss. The moss first shows one small red glowing spot and a thin wisp of smoke; she lowers her face close and blows gently; only after several seconds does a small flame appear. There is no shower of sparks and no instant flame.`
      - Mang than: `A small loosely rolled bundle of bark holds one glowing ember buried in dry moss, with an opening at one end for air. The bark does not burn; only faint warmth and a thin thread of smoke rise from it.`
      - Hướng đánh (sửa 2026-10-05 theo Sorensen et al. 2018, *Sci. Rep.*): vết đập trên biface Neanderthal nằm ở **mặt phẳng/lồi**, song song trục dài. Không tả "cạnh sắc, góc dốc". Pyrite cho tia ngắn và yếu, không bắt được cỏ khô thường; cần mồi rất dễ bắt (bột khoáng MnO₂ hạ ngưỡng cháy, nấm mồi). Nhân vật thất bại với rêu trần là đúng vật lý.
    - Đạo cụ cổ phải tả đúng vật thật (pyrite là cục khoáng màu đồng thau, không phải que mồi thép; biface là đá ghè hai mặt không cán). Không dùng từ gây hiểu nhầm (`black powder` → `dark mineral powder`).

58. **KHÓA SỐ NGƯỜI & DẤU NHẬN DIỆN CHO NGƯỜI PHỤ KHÔNG TÊN (Head-Count Lock & Identity Anchors — Neanderthal 51ka, user review 05/10/2026):**
    - **Root cause dự báo:** Cảnh đêm đông người, model thêm/bớt người giữa các clip; thoại "Eight of us" mâu thuẫn với hình. Người phụ không có ref thì mặt đổi qua từng clip.
    - **Quy tắc:** (1) Cảnh nhóm ghi nguyên câu `Exactly seven Neanderthals and Nora are present; there are no other people anywhere in the frame.` (2) Mỗi người phụ không tên xuất hiện nhiều lần được gán **một dấu nhận diện dễ thấy** (sẹo trên lông mày trái, tóc dài buộc dây da, râu rậm mũi bè, tóc cắt sát, tấm da sói khoác một vai), ghi bảng trong script và dán vào prompt mỗi khi họ có mặt. Không cần ref riêng, không thoại riêng.

59. **TẢ ÁNH SÁNG BẰNG CẢM GIÁC, KHÔNG VỊ TRÍ MẶT TRỜI (Qualitative Light — Neanderthal 51ka, user review 05/10/2026):**
    - **Root cause dự báo:** Prompt kiểu "sun one hand above the ridge" làm model vẽ mặt trời đúng chỗ đó, dễ lệch hướng/độ cao giữa các clip liền nhau và mâu thuẫn với countdown.
    - **Quy tắc:** Dùng `long shadows, low winter sunlight, daylight fading fast` / `dusk` / `moonlight`. Chỉ đưa mặt trời vào khung khi đó là chủ thể của shot (bình minh cuối tập).

60. **BODY ĐÃ MẶC TRANG PHỤC LÀM <VLOGGER> BODY; VIDEO NHẬN MẶT + BODY, KHÔNG CẦN NHẬN OUTFIT RIÊNG (Dressed-Body as Vlogger Body — Neanderthal 51ka, user lock 05/10/2026; thay thế hoàn toàn entity Outfit riêng theo Rule 46 & 47):**
    - *(Phim: áp cho mọi nhân vật chính có ref: `<Tên>` (mặt) + `<Tên> Body <trạng thái trang phục>` (ví dụ EMBERS `Nora Body Ranch`); chữ "vlogger" ở đây đọc là "nhân vật chính".)*
    - **Chỉ đạo cốt lõi của User (05/10/2026):** Khi tạo ảnh trang phục mặc lên body, nó KHÔNG PHẢI là outfit riêng lẻ nữa. Nó chính là **Body đã mặc trang phục** và đóng vai trò trực tiếp là **`<Vlogger> Body`** duy nhất. Không tạo entity `<Vlogger> Outfit` riêng gây phân mảnh và thừa thãi. Downstream video R2V chỉ nhận: `["<Vlogger>", "<Vlogger> Body", ...]`.
    - **Bằng chứng:** Outfit gen trên mannequin hỏng (v1/v2: giày hiện đại, cụt tay, mất legging, làm phẳng ngực). Khi dùng `EDIT_CHARACTER_IMAGE` từ ảnh Body trần của user (`uploads/nora_body_v3_clean.jpg`) với prompt tôn dáng (ôm sát, nâng ngực nhô cao, eo thon, chân dài) → sinh ra ảnh 3 góc khớp nhau tuyệt đối, chuẩn trang phục cổ đại và giữ nguyên vóc dáng đồng hồ cát.
    - **Quy tắc 1 — tạo ref `<Vlogger> Body`:** Dùng ảnh Body trần nguồn của user làm `source_media_id`, chạy `EDIT_CHARACTER_IMAGE` để "mặc trang phục" lên body: giữ nguyên 3 panel (chính diện, 3/4, sau lưng), tư thế, tỉ lệ giải phẫu (ngực đầy, eo thon, hông nở, chân dài), khung cắt vai không lộ mặt, và nền studio. Sau khi sinh xong: tải về, xóa sạch watermark SynthID bằng `python tools/remove_watermark_from_image.py`, upload lại lấy UUID sạch và gán trực tiếp làm `media_id` cho entity `<Vlogger> Body`.
    - **Quy tắc 2 — ref cho video downstream:** Mọi clip có vlogger gắn `character_names`/`refs` = `["<Vlogger>", "<Vlogger> Body", ...]`. **TUYỆT ĐỐI KHÔNG tạo entity Outfit riêng và KHÔNG gửi ảnh Body trần/gym vào video** (tránh nhiễm da thịt trần, Rule 47).
    - **Câu identity:** *"Nora looks exactly like her two reference images: her face and hair from the Nora face sheet, and her build and clothing from the Nora Body sheet."* Vẫn giữ `OUTFIT LOCK` + `BODY LOCK` bằng chữ trong prompt (Rule 47).
    - **Cổng duyệt bắt buộc (Rule 46):** Bắt buộc trình ảnh `<Vlogger> Body` sạch logo cho user xem và duyệt phom dáng & trang phục trước khi gửi bất kỳ lệnh sinh video nào.

61. → chuyển sang [`vlog-archive.md`](vlog-archive.md) (selfie vs POV khi đi săn). Ý chung vẫn áp cho phim: rình, áp sát, ẩn nấp → Sonic Isolation, 0 từ trên hình (Rule 49 (4)).
62. **BỎ HẲN GIÁP LÁ CÀ / VA CHẠM THỂ XÁC VỚI THÚ LỚN; QUY TẮC PHỐI HỢP GÓC MÁY VLOG CHÂN THỰC (TỰ QUAY + TRẢI NGHIỆM 2 TAY TRONG KHUNG HÌNH) (User Lock 08/10/2026):** *(phần "thoại 23–25 từ" đã bị BỎ — số từ chuẩn là 18–22 theo Rule 49, user lock 2026-10-12)*
    - *(Phạm vi: quy tắc 1 (cấm giáp lá cà với thú lớn) áp cho phim; quy tắc 2–4 (phone-vlog trải nghiệm, phối hợp góc máy vlog, thoại Laomedeia) chỉ áp cho vlog; quy tắc 5 là luật riêng của tập Neanderthal.)*
    - **Hiện tượng & Root Cause:** 
      1. Bắt Veo 3 / Omni Flash R2V làm cảnh hành động cận chiến phức tạp đa thực thể (Scene 26–30 Neanderthal: 2 người đâm giáo, bò rừng 1 tấn húc tảng đá, vật lộn gục ngã) làm AI quá tải cơ học tiếp xúc (contact physics) ➔ vũ khí cong queo biến dạng hòa vào thịt, quái thú trượt lướt mất trọng lực, người bị vỡ giải phẫu.
      2. Góc quay selfie một tay vươn dài gượng gạo vừa dễ gây dị tật cánh tay/méo mặt khi xoay người, vừa làm hẹp góc nhìn và che khuất không gian giao lưu. Tuy nhiên, nếu biến thành 100% First-Person POV vô hình thì vlogger biến mất hoàn toàn, mất đi bản sắc và tính kết nối của người dẫn chương trình vlog!
      3. Thoại dưới 15 từ làm nhịp video bị thưa, thiếu năng lượng vlog thực tế.
    - **Quy tắc đúc kết:**
      1. **Dừng 100% cảnh đánh đấm/vật lộn đối kháng:** AI video hiện nay không xử lý được võ thuật và va chạm thể xác phức tạp. Tuyệt đối không viết cảnh cận chiến giáp lá cà người vs thú lớn.
      2. **Chuyển sang Phone-Vlog Trải Nghiệm Giao Lưu & Sinh Tồn Kỳ Thú:** 
         - Kịch bản tập trung vào **Nora đến trải nghiệm giao lưu văn hóa & cơ chế sinh tồn kỳ thú** (học hỏi công thức thành công của các kênh triệu view như Medieval Sisters nhưng giữ vững bản sắc vlog): Kỹ thuật đẽo đá Mousterian sắc như dao mổ, may đo kín khít bằng chỉ gân hươu, đun sôi nước bằng đá nung trong âu da, bột khoáng xúc tác MnO2, dấu bàn tay đất son đỏ.
      3. **Quy tắc Phối hợp Góc Máy Vlog Chân Thực (Bỏ selfie 1 tay vươn dài):** 
         - **Lúc cần có Nora (Self-Vlog / Tự quay)**: Nora cầm máy tự nhiên ngang ngực/cổ quay mặt mình, nói trực tiếp vào ống kính dẫn dắt câu chuyện và chia sẻ cảm xúc; không tả cánh tay vươn dài.
         - **Lúc Nora thao tác 2 tay & Cảnh rộng (In-Frame Host Experience)**: Máy quay đặt trên tảng đá/chạc cây hoặc góc máy trung/toàn (Tripod/Rock-mounted medium/wide shot), Nora xuất hiện rõ ràng trong khung hình (Full/Medium Nora in frame), thoải mái dùng cả hai tay trải nghiệm cơ chế sinh tồn (nếm súp tủy xương, ngồi sưởi ấm bên đống lửa, đẽo đá, may đồ), vừa thao tác vừa quay mặt về phía camera vừa nói/giải thích kiểu người dẫn chương trình thực tế.
         - **Cận cảnh chi tiết (POV Close-Up)**: Camera quay cận cảnh đồ vật/hiện tượng (đá nung sủi bọt, mũi khâu gân) khi cần khán giả soi chi tiết vi mô.
      4. **Chuẩn Thoại Dồn Dập Mới: 23 – 25 từ trong clip 8s:** 
         - Nora nói nhanh, tự nhiên và tràn đầy năng lượng qua giọng Laomedeia, tạo cảm giác vlogger đang livestream thực tế với nhịp adrenaline cao. Số từ theo Rule 49: **18–22 từ / clip 8s** (dưới 18 → dead air; trên 22 → cụt âm ở giây thứ 8).
      5. **Khóa Chuẩn Bối Cảnh Địa Lý/Thời Kỳ (Strictly No Snow):** 
         - Tôn trọng bối cảnh gốc của thời kỳ (MIS 3 liên băng Dordogne là rừng thông ôn đới, đất mùn rêu xanh, tuyệt đối không tự ý chèn tuyết/bão mùa đông).

63. **CẤM TRIỆT ĐỂ TỪ KHÓA 'PHONE/SMARTPHONE/PHONE_VLOG/DEVICE/SCREEN' (GHOST DEVICE MATERIALIZATION), KHÓA TRANG PHỤC THUẦN ẢNH THAM CHIẾU (PURE DRESSED-BODY REF LOCK) & CHỐNG TEO TÓP BODY DO GÓC QUAY (WAIST-UP BODY DRIFT PREVENTION) (User Lock 08/10/2026):**
    - *(Phạm vi: quy tắc 1 (từ khóa thiết bị, material `prehistoric_vlog`) chỉ áp cho vlog; quy tắc 2 (khóa trang phục thuần ref) và quy tắc 3 (không tả vòng 1, khóa dáng theo ref) áp cho phim.)*
    - **Hiện tượng & Root Cause:**
      1. **Vật thể hóa điện thoại (Ghost Device Materialization - Bài học Scene 24):** Khi đưa chữ `phone` hoặc `phone_vlog` vào project material hoặc prompt header/body, diffusion model sẽ hiểu nhầm token text và tự động vẽ (vật thể hóa) một chiếc smartphone vật lý 3D ngoài đời thật lơ lửng hoặc cầm trên tay nhân vật trong bối cảnh tiền sử/cổ đại.
      2. **Loạn trang phục do tự tả bằng lời (Outfit Drift - Bài học Scene 21):** Khi `<Vlogger> Body` đã là ảnh body mặc hoàn chỉnh trang phục (Rule 46/60), nếu prompt tự mô tả lại bằng lời các chi tiết như `shearling collar`, `tunic`, `fur-lined`, model AI sẽ bị xung đột giữa token văn bản và latent của ảnh tham chiếu ➔ tự ý vẽ thêm chi tiết lạ (như Cảnh 21 tự mọc thêm cổ lông cừu trắng kỳ quái che mất áo da lộn cổ V đan dây của Nora Body v8).
      3. **Teo tóp vóc dáng do góc quay & tư thế (Body Drift - Bài học Scene 23 cũ):** Quay góc toàn/xa khi nhân vật cúi gập người khiến phối cảnh ép phẳng vòng 1 và làm mất hoàn toàn eo, biến vóc dáng đồng hồ cát thành dáng phẳng lì, thô kệch.
    - **Quy tắc đúc kết:**
      1. **Cấm 100% từ khóa thiết bị trong Prompt & Material:**
         - TUYỆT ĐỐI CẤM 100% các từ `phone`, `smartphone`, `phone_vlog`, `device`, `screen`, `gimbal` trong cả Material và Prompt (kể cả câu cấm "no phone").
         - Material của project dùng: `prehistoric_vlog` (với bối cảnh tiền sử) hoặc `realistic` / `documentary_footage`. Tuyệt đối không dùng token chứa chữ `phone`.
         - Khóa góc nhìn quang học thuần khiết: `"The camera lens and viewpoint are completely outside the visible frame and never seen; both hands are empty."`
      2. **Khóa trang phục thuần ảnh tham chiếu — CẤM tự mô tả lại bằng lời:**
         - Tuyệt đối KHÔNG mô tả lại trang phục bằng lời trong prompt khi đã có `<Vlogger> Body`.
         - Chỉ dùng câu khóa trỏ thẳng vào reference sheet đã duyệt: `"[Character] wears the exact historical outfit shown in the [Character] Body reference sheet (NO shearling collar, NO extra fur, NO hood, NO outfit variations)."`
      3. **Khóa vóc dáng & trang phục thuần tham chiếu (Chống hỏng áo quần do tập trung vào ngực — User Lock 08/10/2026):**
         - **CẤM TRIỆT ĐỂ mô tả ngực to, khe ngực sâu, khoét cổ sâu (`voluminous heavy bust`, `deep cleavage`, `plunging V-neckline`)**: Việc nhồi nhét các từ khóa phóng đại vòng 1 làm AI diffusion model ép xẻ sâu cổ áo quá đà, làm rách nát, biến dạng và hỏng phom dáng trang phục cổ đại trong ảnh reference.
         - **Giữ đúng body & outfit thuần tham chiếu**: Chỉ cần khóa vóc dáng thể thao đồng hồ cát và bộ trang phục da lộn may đo theo đúng 100% ảnh reference sheet (`Nora Body`):
           `"BODY & OUTFIT LOCK (CRITICAL): Nora matches her reference images exactly: her face and hair from the Nora face sheet, and her athletic, curvaceous hourglass build and tailored clothing from the Nora Body sheet. Nora wears the complete historical outfit from the Nora Body reference: form-fitting smoked golden-tan deer suede tunic with laced V-neckline, wide dark corset belt, fitted trousers, and knee-high boots (strictly NO shearling collar, NO extra fur, NO hood, NO outfit variations). From the very first frame to the last, Nora is fully dressed in the complete outfit. No part of the outfit appears, disappears or changes."`

64. **CẤM MÔ TẢ HỨNG BỤI / BỘT RƠI GIỮA KHÔNG TRUNG; BẮT BUỘC ĐẠO CỤ & BỘT NẰM SẴN TRÊN BỀ MẶT TỪ FRAME 0 (Particle Catching & Latent Color Spawning Glitch — Bài học Scene 22 Neanderthal 51ka, User review 08/10/2026):**
    - **Hiện tượng & Root Cause:** Prompt yêu cầu Thủ Lĩnh cạo bột khoáng rơi xuống và Nora xòe hai tay hứng lấy rồi xoa ngón tay. AI video diffusion model (Veo 3 / Omni Flash R2V) **hoàn toàn không có cơ học mô phỏng hạt bụi rơi tự do và truyền chất giữa hai thực thể**. Kết quả: Thủ Lĩnh cạo đá riêng ở dưới, tay Nora xòe ra giữa không trung không có gì rơi vào, rồi AI đột ngột "hóa phép" (spawn) biến màu đỏ thẫm đè lên lòng bàn tay và làm ngón tay biến dạng kỳ quái (lỗi tự biến đổi tay không có bột).
    - **Quy tắc giải pháp (Direct Surface Contact & Frame 0 Material Presence):**
      1. **Bột/Chất liệu phải có mặt sẵn trên bề mặt từ Frame 0:** Mọi chất liệu (bột đất son đỏ, tro bếp, nước, đất sét) BẮT BUỘC phải nằm sẵn trên một bề mặt vật lý cố định (tảng đá phẳng, khay đá, vỏ cây, âu da) ngay từ giây đầu tiên (`from frame 0, a natural mound of fine crimson red ochre powder already rests on the flat limestone rock`). Tuyệt đối không mô tả bột rơi lơ lửng rồi hứng lấy.
      2. **Tiếp xúc trực tiếp (Direct Touch):** Nhân vật dùng đầu ngón tay chủ động chạm/quệt trực tiếp vào lớp bột có sẵn trên tảng đá (`Nora touches her index finger directly into the crimson pigment on the flat stone, picking up a pinch of red powder`).
      3. **Chuỗi nhân quả rõ ràng:** Ngón tay chạm vào bột ➔ dính bột đỏ ➔ đưa lên ngang ngực miết nhẹ giữa hai ngón tay và khoe với camera. Khử hoàn toàn hiện tượng bàn tay tự đổi màu ma thuật.

65. **NÓI NGAY TỪ GIÂY 0, PHÂN BỔ THOẠI ĐỀU 3 MỐC THỜI GIAN (Immediate Frame-0 Speech Delivery — Chống nuốt chữ / hết giờ khi thoại 22–24 từ — Bài học Scene 21, User review 08/10/2026):**
    - **Hiện tượng & Root Cause:** Prompt mô tả `0-3s: Nora mỉm cười đi về phía trước...` mà không quy định bắt đầu nói ngay từ giây 0, khiến AI cho nhân vật im lặng (dead air) suốt 2–3 giây đầu. Khi câu thoại dài 22–24 từ, AI chỉ còn 4–5 giây cuối để phát âm, dẫn đến việc vlogger nói không kịp, khẩu hình bị dồn cụt hoặc bị ngắt âm ở giây thứ 8.
    - **Quy tắc giải pháp:**
      1. **Bắt buộc nói ngay từ giây 0:** Tại mốc `0-3s`, BẮT BUỘC ghi rõ: `"From the very first frame at second 0, Nora begins speaking immediately, excitedly, and fluently into the lens..."`
      2. **Nhúng thoại chia đều 3 mốc (0-3s, 3-6s, 6-8s):** Chia câu thoại 22–24 từ thành 3 cụm gắn trực tiếp vào từng mốc thời gian để AI dàn trải khẩu hình từ đầu tới cuối clip 8s.
      3. **Khóa trong SPEECH & LIP LOCK:** `"From second 0 through second 7.5s, Nora speaks continuously without dead air at the beginning; she starts speaking immediately from frame 0."`

66. → chuyển sang [`vlog-archive.md`](vlog-archive.md) (tay vlogger trong POV, ref `<Vlogger> Back`, tỷ lệ góc máy vlog).

67. → chuyển sang [`vlog-archive.md`](vlog-archive.md) (POV tự thân vs quay người khác trong vlog).

68. **BẢO TOÀN ĐẠO CỤ VẬT LÝ, CẤM THAO TÁC BUÔNG/ĐẶT ĐỒ XUỐNG ĐẤT & CẤM XOAY NGƯỜI 180° KHI VÁC ĐỒ NẶNG (Prop Continuity, Anti-Vanishing, No Drop-Off & Steady Posture Lock — Bài học Scene 33, 36, 37 Neanderthal 51ka, User review 09/10/2026):**
    - **Hiện tượng & Root Cause:**
      1. **Lỗi biến mất đạo cụ khi quay người 180° (Vanishing Prop on Turning - Bài học Cảnh 33):** Khi nhân vật đang vác một thân cây thông lớn trên vai bước đi, nếu prompt yêu cầu nhân vật quay người lại đối diện camera, không gian tiềm ẩn (latent space) của diffusion model không thể xử lý vật thể dài bị che khuất và xoay chiều trong không gian 3D, dẫn đến AI "giải quyết" bằng cách xóa sổ luôn thân cây, làm hai tay nhân vật bỗng chốc trống không kỳ quái.
      2. **Lỗi biến hình mọc thêm đạo cụ / cành lá (Prop Spawning / Morphing - Bài học Cảnh 36):** Nhân vật khiêng một thân gỗ tròn nhẵn, nhưng prompt lại mô tả thêm *"chèn cành thông dày và phiến đá"*, khiến AI bị nhiễu loạn token và "mọc thêm" các cành lá thông um tùm hoặc biến khúc gỗ thành bụi cây rậm rạp giữa chừng.
      3. **Lỗi đặt đồ vật xuống đất bị bốc hơi biến mất (Disappearing Object on Release - Bài học Cảnh 37):** Khi mô tả nhân vật ôm bó củi rồi *"đặt bó củi xuống đất cạnh bếp lửa"*, AI video diffusion model **hoàn toàn không có engine vật lý va chạm và chuyển giao vật thể**. Ngay khi hai bàn tay buông ra, các điểm ảnh của bó củi bị hòa tan (dissolve) vào mặt sàn đá và biến mất không dấu vết.
    - **Quy tắc giải pháp:**
      1. **Giữ hướng chuyển động đồng nhất khi mang vác (Steady Forward Progression):**
         - Khi nhân vật vác thân cây/khúc gỗ/vũ khí lớn, **CẤM TUYỆT ĐỐI** yêu cầu nhân vật xoay người 180° hay đổi hướng đột ngột.
         - Cả hai nhân vật cùng giữ vững hướng bước đi về phía trước (tiến về cửa hang) từ giây 0 đến giây 8, giữ nguyên thân gỗ vững chắc trên vai suốt toàn bộ clip (`steady forward walking, the heavy pine log remains firmly anchored on his shoulder from frame 0 through frame 8; NO turning around, NO dropping or vanishing of the log`).
      2. **Bảo toàn một trạng thái đạo cụ duy nhất từ Frame 0 (Single Static Prop Identity):**
         - Nếu là thân gỗ tròn (`timber log`), chỉ mô tả DUY NHẤT một thân gỗ tròn thô ráp được hai người hạ thẳng xuống đất chèn ngang ngưỡng cửa. Tuyệt đối không mô tả thêm cành nhánh, tán lá thông rậm rạp làm AI biến hình đạo cụ (`strictly ONE single heavy pine timber log without branches or foliage; NO foliage spawning, NO morphing`).
      3. **Đạo cụ nằm sẵn cố định trên mặt đất từ Frame 0 — CẤM tả động tác đặt xuống đất:**
         - Đối với các cảnh tập kết đồ vật (như đống củi, khay đá, rổ thức ăn): Đạo cụ **PHẢI NẰM CỐ ĐỊNH TRÊN MẶT ĐẤT CẠNH BẾP TỪ FRAME 0** (`from frame 0, a neat stack of dry split pine firewood already rests on the limestone floor beside the hearth`).
         - Nhân vật ngồi cạnh chỉ cần thao tác hơ tay sưởi ấm hoặc cầm 1 que củi cho vào bếp; **TUYỆT ĐỐI KHÔNG** mô tả động tác ôm cả bó đồ rồi đặt buông xuống đất để tránh lỗi tan biến điểm ảnh.

69. **KHÓA BỐI CẢNH BẰNG ẢNH REF 16:9 DÙNG CHUNG & DUYỆT START FRAME BỐI CẢNH TRƯỚC KHI SINH R2V; KHÓA ĐẠO CỤ ĐƠN NHẤT & CẤM NGƯỜI NGOÀI RÌA (Shared 16:9 Setting Ref Lock, Start-Frame Review Gate, Single-Prop Identity & Zero-Bystander Lock — Bài học Scene 27, 28, 30 Neanderthal 51ka, User review 09/10/2026):**
    - **Hiện tượng & Root Cause:**
      1. **Lệch bối cảnh giữa các cảnh liên tiếp (Scene 27 vs Scene 28):** Cùng một không gian bếp lửa trung tâm hang Pech de l'Azé và chỉ cách nhau 3 giây trong kịch bản. Cảnh 27 quay OTS thấy bếp lửa bên trái quây bằng đá nhỏ, nền đá sỏi phẳng, Thủ Lĩnh cởi trần vắt da. Sang cảnh 28, bếp lửa tự nhiên nhảy ra chính giữa, quây bằng những hòn đá cuội to tròn nhẵn thín, Thủ Lĩnh quỳ bên trái mặc áo lông thú dày kín mít, dưới đất xuất hiện thớt đá và tấm da hươu đốm to. Vì R2V chỉ truyền Face và Body của nhân vật mà KHÔNG có ảnh reference bối cảnh (`Setting Reference`), AI đã tự tưởng tượng (hallucinate) ra 2 bếp lửa và 2 bố cục hang hoàn toàn khác nhau!
      2. **Lỗi người ngoài rìa biến mất (Vanishing Bystander - Bài học Scene 30):** Ở giây 0-1, AI tự ý vẽ thêm nửa thân dưới của một người đàn ông đứng ở rìa phải sau lưng Nora (`standing bystander`). Nhưng do prompt không quy định người này và không khóa thời gian, đến giây 5-8 AI tự động xóa sổ người này biến mất không dấu vết.
      3. **Lỗi cục đá kê xuất hiện & cành cây lơ lửng (Floating Props & Morphing Base - Bài học Scene 30):** Bàn kê da không có cấu trúc vật lý neo cố định từ đầu nên AI tự đẻ một tảng đá xám kê dưới khúc gỗ và làm cành cây phía sau trôi nổi lơ lửng mất gốc.
      4. **Lỗi phân mảnh đạo cụ 1 thành 2 (Tool Duplication / Forking Glitch - Bài học Scene 30):** Prompt mô tả bà lão cầm xương lissoir rồi miết lên da, nhưng AI không hiểu sự kế thừa chuyển động, tự "đẻ" thêm một thanh xương thứ hai nằm sẵn trên da ở giây 5-8, khiến bà lão một tay cầm xương cạo, một tay đè lên thanh xương thứ hai!
      5. **Thiếu bước Review Bối cảnh:** Quy trình R2V trước đây bỏ qua việc sinh start frame ảnh, dẫn đến việc User hoàn toàn không được nhìn và duyệt trước không gian, góc đặt máy, bếp lửa và đạo cụ trước khi AI sinh video.
    - **Quy tắc giải pháp:**
      1. **Mỗi cụm bối cảnh (Setting Sequence) BẮT BUỘC phải tạo 1 ảnh Reference Bối cảnh 16:9 (Setting / Scene Start-Frame Ref):**
         - Trước khi sinh video cho bất kỳ phân đoạn nào (như Cụm Bếp lửa ghè đá Cảnh 27-28, Cụm Bàn thuộc da Lissoir Cảnh 30-31, Cụm Ngưỡng cửa hang rào gỗ Cảnh 33-36, Cụm Ổ ngủ cành thông Cảnh 51-54, Cụm Thềm đá ban mai Cảnh 60-67): BẮT BUỘC phải sinh 1 ảnh bối cảnh 16:9 chuẩn (hoặc start frame góc máy tĩnh không người hoặc đúng bố cục người/vật).
         - Quy trình 4 bước chuẩn sạch watermark:
           1. Gen ảnh bối cảnh 16:9.
           2. Tẩy logo watermark & SynthID (`python tools/remove_watermark_from_image.py`).
           3. Upload lên Flow lấy `media_id` UUID sạch (`POST /api/flow/upload-image`).
           4. Đưa lên Review Board (`:8200` / file ảnh) cho User xem và duyệt bối cảnh/bố cục trước.
      2. **Đưa vào R2V Ingredients làm Shared Reference:**
         - UUID ảnh bối cảnh sạch được gán vào `reference_media_ids` của tất cả các cảnh thuộc cùng cụm bối cảnh đó.
         - Ví dụ: Cảnh 27 và 28 cùng nhận `reference_media_ids = [Nora_Face, Nora_Body, Leader_Face, Hearth_Setting_UUID]`. Cảnh 30 và 31 cùng nhận `[Nora_Face, Nora_Body, OldWoman_Face, Leatherwork_Bench_UUID]`.
      3. **Khóa Bối cảnh trong Video Prompt:**
         - Khối `SETTING` trong prompt BẮT BUỘC phải trỏ trực tiếp và khóa chặt theo ảnh ref bối cảnh:
           `SETTING: Matches the exact cave hearth / workspace layout, rock formation, and prop placement shown in the [Setting Reference] image. From the very first frame to the last, all background rocks, embers, and ground textures remain completely consistent.`
      4. **Khóa Đạo cụ Đơn nhất & Khóa Người ngoài rìa (Scene 30 Fixes):**
         - `Strictly ONE single curved deer rib bone tool (lissoir) only; NEVER duplicate, NEVER spawn a second bone, NO extra tools on the pelt.`
         - `The wooden log bench and ground support remain rock-solid and static from frame 0; NO stone block appears under the log; background sticks firmly touch the stone floor and NEVER float.`
         - `Strictly NO bystanders, NO extra people standing in the background or framing edges; only Nora and the Elder Woman are present in the scene.`

70. **KHÓA TAY CẦM ĐẠO CỤ CỐ ĐỊNH SUỐT CLIP — DAO ĐÁ NHẢY TAY / BIẾN MẤT RỒI TỰ HIỆN (One Hand, One Prop, Whole Clip — Bài học Scene 29 Neanderthal 51ka, User review 09/10/2026, lỗi NẶNG):**
    - **Hiện tượng:** Máy dựng cố định, Nora quỳ sau phiến đá thử phiến dao đá cắt gân hươu (10s). Prompt ghi "tay phải cầm dao, tay trái đè gân" nhưng giây 0 dao nằm ở **tay trái**; giây ~3.5 dao **nhảy sang tay phải** không có động tác chuyền; giây ~7.5 dao rời tay phải đặt xuống bàn rồi **tự dịch sang dưới tay trái**, còn đoạn gân lại hiện ở tay phải. User đánh giá: tay chân biến hóa, dao biến mất rồi tự xuất hiện — lỗi nặng, không dùng được.
    - **Root cause:**
      1. **Nhầm trái/phải khi nhân vật đối diện máy:** "her right hand" của nhân vật nằm ở **bên trái khung hình**; model hay lật gương nên khởi đầu sai tay, rồi tự "sửa" giữa clip bằng cách teleport đạo cụ.
      2. **Quá nhiều thao tác tay trong 1 clip:** cầm dao + đè gân + cắt + đặt dao xuống + nhấc gân lên khoe = 5 lần đổi trạng thái tay. Mỗi lần đặt/nhấc là một cơ hội để đạo cụ đổi tay hoặc biến mất.
      3. **"Đặt đạo cụ xuống rồi cầm thứ khác"** khiến model mất dấu vật đang nằm trên bàn và vẽ lại nó ở chỗ khác.
    - **Quy tắc giải pháp:**
      1. **Một tay — một đạo cụ — suốt clip:** đạo cụ chính (dao, búa, xương) ở **một tay duy nhất từ giây 0 đến giây cuối**, không bao giờ đặt xuống, không chuyền tay: `"the flake stays in her right hand from the first frame to the last; it never leaves that hand, never changes hands, and is never put down"`.
      2. **Ghi kèm vị trí trong khung khi nhân vật đối diện máy:** `"her right hand, on the left side of the frame"` / `"her left hand, on the right side of the frame"`.
      3. **Tối đa 2 trạng thái tay mỗi clip** (vd: chuẩn bị → cắt). Phần "khoe kết quả" làm bằng chính tay đang cầm sẵn (tay đè gân nhấc đầu gân đã cắt lên), không đặt dao để lấy vật khác.
      4. **Đếm đạo cụ trong `negative_constraints`:** `"exactly one flake in the whole clip, always in her right hand; it never vanishes, never duplicates, never appears on the slab"`.
      6. **Khóa theo BÊN KHUNG HÌNH, không chỉ theo tay (Scene 41, 10/10/2026):** nhân vật đối diện máy cầm 2 đạo cụ → model hay lật trái/phải ngay từ frame 0 rồi đổi tay giữa clip. Ghi ở MỌI mốc thời gian: `"the bone is on the RIGHT side of the frame in her left hand"`, `"the stick stays on the LEFT side of the frame"`, và `negative_constraints`: `"the two objects never swap sides and never pass between hands"`; ghi kích thước đạo cụ (`"a short stick about the length of a hand, never a long staff"`). Đã thử: lần 2 đạt 9.
      5. **Đạo cụ phụ nhỏ trong tay nhân vật phụ (que, cành) hay tự xuất hiện/biến mất (Scene 32, 10/10/2026, 2 lần liền):** khi model muốn nhân vật cầm đạo cụ chính (giáo) bằng 2 tay, đạo cụ phụ ở tay kia sẽ hiện ra giữa clip rồi biến mất — khóa câu chữ không cứu được. Cách sửa: **bỏ hẳn đạo cụ phụ**, viết lại hành động chỉ với 1 đạo cụ cầm 2 tay (nhúng thẳng khớp mũi giáo vào khay nhựa thay vì dùng que phết).

71. **SELFIE VỪA ĐI VỪA NÓI: HẬU CẢNH NHẢY CÓC & TÓC BUNG (Continuous-Take Lock — Bài học Scene 34 Neanderthal 51ka, 10/10/2026):**
    - *(Phim: luật hậu cảnh cố định + `one continuous take` áp cho mọi shot máy đi theo nhân vật, không chỉ selfie.)*
    - **Hiện tượng:** Selfie Nora vừa leo dốc vừa nói, 10s. Giây ~2.7 hậu cảnh đổi phắt từ sườn đá có cửa hang sang bầu trời + thung lũng như bị cắt cảnh; đuôi ngựa bung, tóc xõa bay tứ tung vì prompt viết "loose strands blown back by the wind" và "a strong gust pushes her hair back".
    - **Quy tắc:** (1) Khung selfie di chuyển phải ghi rõ hậu cảnh cố định từ giây 0 tới cuối + `"one continuous take with no cut and no change of background"`; (2) không tả gió thổi tóc, chỉ `"the ponytail swings, the bangs stay over her forehead"` (khớp checklist 19); (3) `negative_constraints` có `"the ponytail never comes undone; her hair is never loose"`.

72. **ĐEO VÒNG CỔ / DÂY QUA ĐẦU PHẢI ĐÚNG VẬT LÝ (Necklace-Over-Head Physics — Bài học Scene 44 Neanderthal 51ka, user review 10/10/2026):**
    - **Hiện tượng:** Bà lão "quàng" vòng dây móng đại bàng cho Nora; trong clip sợi dây tự nằm vào cổ mà không hề đi qua đỉnh đầu, Nora không cúi đầu — user: "đeo dây mà không lồng vào cổ, không cúi xuống lồng vào, sai vật lý".
    - **Nguyên nhân:** prompt chỉ viết "lowers the loop over Nora's head and lets go" — quá tắt, model nhảy thẳng tới trạng thái cuối (dây đã ở cổ).
    - **Quy tắc:** tả từng bước vật lý: (1) vòng dây **rộng, căng mở bằng 2 tay, nâng cao trên đỉnh đầu** từ frame 0; (2) người được đeo **cúi đầu, cằm xuống**; (3) vòng dây hạ **qua đỉnh đầu và qua búi/đuôi tóc**, trượt xuống gáy; (4) **chỉ sau đó** mới buông tay, mặt dây rơi xuống ngực; (5) người được đeo ngẩng đầu lên. `negative_constraints`: `"the loop always passes over the top of her head and ponytail before it reaches her neck; the cord never passes through her head, face or hair"`. Áp dụng cho mọi hành động mặc/đeo qua đầu (vòng cổ, áo chui đầu, mũ trùm).

73. **TỪ GỢI LỬA TRONG PROMPT LÀM MODEL TỰ VẼ LỬA (Fire-Word Leak — Bài học Scene 50 Neanderthal 51ka, 10/10/2026, 7 lần gen):**
    - **Hiện tượng:** Cảnh POV cửa hang ban đêm, cấm lửa rõ ràng trong `negative_constraints`, nhưng 6 lần liền model vẫn vẽ lửa nhỏ lập lòe sau khúc gỗ/tường đá. Lần 6 hết lửa nhưng ra 2 cục sáng rơi như sao chổi (do tả "puffs/gusts of snow").
    - **Nguyên nhân:** mô tả hình và thoại chứa chữ gợi lửa: thoại `"No fire means death"`, `firelight`, `embers`, `warm orange glow from the hearth`. Model bám vào các chữ này mạnh hơn câu cấm.
    - **Quy tắc:** cảnh không được có lửa thì **xóa mọi chữ fire / firelight / ember / hearth / orange glow / torch khỏi thoại, setting, motion, physical_realism, audio** — chỉ để lại trong câu cấm. Ánh sáng tả bằng "cold blue moonlight". Tuyết tả là "sparse tiny individual snowflakes, smaller than a grain of rice", không dùng "puffs/gusts of snow". Vật dễ "gọi" lửa (khúc gỗ đặt ngang cửa) cũng nên bỏ khỏi khung nếu không cần cho truyện.

74. **CÂU VẬT LÝ CHUNG "HIDE FRINGES" LÀM TRANG PHỤC VLOGGER MỌC TUA RUA (Generic-Realism Outfit Leak — Bài học Scene 70 Neanderthal 51ka, 11/10/2026):**
    - **Hiện tượng:** Clip 70 (Nora đặt pyrite lên tảng rêu rồi đi xa) chuyển động sạch, nhưng tay áo và gấu áo có tua rua, thắt lưng bản nhỏ, bốt trơn — khác ảnh `Nora Body` (gấu trơn, thắt lưng da bản to, bốt dây đan chéo). Review 8.5 → gen lại.
    - **Nguyên nhân:** khối `physical_realism.secondary_motion` dùng chung cho mọi clip có câu `fur trims and hide fringes swing with movement`. Clip chỉ có Nora nên model gắn "fringes" vào áo của cô.
    - **Quy tắc:** câu chuyển động phụ về lông/viền da chỉ được gắn vào **trang phục của NPC** (`the clan's fur cloaks sway`), không viết chung chung. Với vlogger thì ghi rõ áo giữ đúng ảnh Body: `smooth plain hems, wide dark belt, criss-cross laced boots (no fringe, no tassels on her)`, và thêm `NO fringe, NO tassels` vào câu khóa trang phục. Đây là các câu cấm và trỏ về ảnh ref, không phải tả lại trang phục (Rule 52).

75. **BẾP NƯỚNG TRONG HANG RA ĐỐNG LỬA CỦI + ĐUỐC TƯỜNG (Coal-Bed & No-Torch Lock — Bài học Scene 39 Neanderthal 51ka, 11/10/2026):**
    - **Hiện tượng:** prompt tả "glowing embers and low flames" với 3 khúc xương nằm trên than. Model vẽ đống lửa củi cháy cao, xương không thấy đâu, còn tường hang có đuốc cắm giá kiểu trung cổ. Review 7.0.
    - **Nguyên nhân:** chữ "flames", "firelight on walls" và câu chung "firelight or moonlight flickers" kéo model về hình ảnh lửa trại quen thuộc. Tường hang không được tả gì, nên model treo đuốc lên.
    - **Quy tắc:** bếp nướng phải tả là **lớp than đỏ đã cháy hết củi** (`wide flat bed of glowing red coals… no logs, no tall flames, only tiny flickers no taller than a finger`). Vật nướng phải ghi kích thước, vị trí và hướng (`three long pale split bones, each as long as a forearm, lying flat across the top of the coals in plain view`). Tường ghi rõ `bare… lit only from below… nothing mounted, hung or burning on the walls`, kèm câu cấm `no torches, no sconces, no candles, no lamps; the only light source is the coal bed`.
    - **Bổ sung (Scene 46, 11/10/2026):** câu cấm đuốc thôi chưa đủ. Nếu setting tả `warm flickering firelight on the walls` mà không nói ánh sáng đến từ đâu, model vẫn gắn đuốc lên tường làm nguồn sáng. Luôn ghi rõ nguồn sáng và vị trí: `the only light is a soft warm glow from a low hearth on the floor just outside the frame on the right`, tường thì `bare natural rock… nothing mounted, hung or burning on them`.

76. **NPC NGỒI CẠNH VLOGGER BỊ BIẾN THÀNH BẢN SAO CỦA VLOGGER (NPC Clone Lock — Bài học Scene 49 Neanderthal 51ka, 11/10/2026):**
    - **Hiện tượng:** cảnh tĩnh, Nora ngồi giữa, bà cụ ngồi sát bên cùng tư thế nhắm mắt ngân nga. Model vẽ bà cụ thành một cô gái trẻ tóc vàng giống hệt Nora. Đầu mọi người còn có khói trắng lơ lửng. Review 6.0.
    - **Nguyên nhân:** khóa nhận diện NPC chỉ ghi `matches the Old Woman reference image exactly`. Khi NPC ngồi sát và làm cùng động tác với vlogger, ảnh ref của Nora lấn át. Khói đến từ câu `breath fogging in the cold air` trong khối "NPC sống" và chữ `with vapor` trong phần chuyển động, dù đang ở trong hang.
    - **Quy tắc:** NPC đứng hoặc ngồi sát vlogger phải có khóa nhận diện kèm vài nét nhận dạng chính để phân biệt (tuổi, màu tóc, nếp nhăn, gờ mày), cộng câu cấm `Nora is the only young blonde woman in the frame… nobody is a copy of Nora`. Khối "NPC sống" dùng `slow quiet breathing`, không dùng chữ hơi thở đọng khói. Cảnh trong hang ghi thêm `the air inside the cave is clear`.

77. **TÊN CON VẬT TRONG THOẠI LÀM CON VẬT HIỆN RA (Creature-Word Leak — Bài học Scene 56 Neanderthal 51ka, 11/10/2026):**
    - **Hiện tượng:** cảnh POV nhìn bức tường chắn cửa hang, thú "chỉ được nghe thấy". Đã có câu cấm `no animals visible anywhere`, nhưng một con linh cẩu vẫn thò đầu qua mép tường từ giây 3. Khúc gỗ đầu cưa phẳng, tường xếp như gạch xây. Review 7.0.
    - **Nguyên nhân:** giống bài học 73: thoại `"A cave hyena whooping…"` và âm thanh `hyena whoops` gọi con vật vào khung mạnh hơn câu cấm. Khoảng trống phía trên tường để mở nên model đặt con vật vào đó.
    - **Quy tắc:** con vật chỉ được nghe thì **không gọi tên nó** trong thoại, segments, audio, motion; dùng `something is whooping`, `distant eerie whooping calls`. Khoảng trống trong khung ghi `shows only black sky… nothing ever appears in that gap`. Tường chắn tả `rough irregular natural chunks… never neat rectangular blocks`, khúc gỗ tả `jagged, splintered broken ends, never sawn flat`.

78. **VLOGGER NGỒI THÌ MẤT QUẦN BÓ, LỘ ĐẦU GỐI TRẦN (Covered-Legs Lock — Bài học Scene 46 Neanderthal 51ka, 11/10/2026):**
    - **Hiện tượng:** Nora ngồi bó gối trong hang, tay đặt lên đầu gối. Áo, thắt lưng, vòng cổ đều đúng, nhưng đầu gối và cẳng chân lộ da trần, mất quần bó da lộn của ảnh `Nora Body`. Review 8.5.
    - **Nguyên nhân:** ảnh Body chụp đứng thẳng nên khi ngồi model phải tự đoán phần chân. Câu khóa trang phục chỉ nói áo, thắt lưng, bốt, không nói quần.
    - **Quy tắc:** câu khóa trang phục vlogger phải có `tan suede leggings that cover her legs completely from hips to boots… no bare skin on her thighs, knees or shins at any moment, even when she sits or kneels`.
    - **Bổ sung (Scene 46 lần 4, 11/10/2026):** sau khi khóa chân, model lại cắt tay áo thành áo không tay (lỗi áo ba lỗ của Rule 50). Câu khóa trang phục phải chốt đủ cả bốn phần: tay áo `long tunic sleeves that reach all the way to her wrists (never sleeveless, never a tank top, never bare shoulders or upper arms)`, thắt lưng, quần bó, bốt. Bỏ sót phần nào, model sẽ "sáng tạo" đúng phần đó.

79. **BÀN TAY TRỐNG VỪA BUÔNG XUỐNG THÌ MỌC THÊM ĐẠO CỤ (Empty-Hand Mirror Spawn — Bài học Scene 46 POV, 11/10/2026):**
    - **Hiện tượng:** người thợ săn cầm 1 khúc xương ở tay phải, tay trái đặt trên đỉnh cột thạch nhũ. Đến giây 7–10 prompt cho tay trái rời cột buông xuống. Đúng lúc đó tay trái mọc thêm khúc xương thứ hai giống hệt. Clip 46 trước đó cũng hai lần bị xương thừa.
    - **Nguyên nhân:** khi hai tay cùng buông thõng hai bên, model có xu hướng làm hai tay đối xứng, nên sao chép đạo cụ sang tay trống.
    - **Quy tắc:** bàn tay trống phải được **neo vào một chỗ cố định suốt clip** (đặt trên đá, trên đùi, nắm vạt áo), ghi `never lets go, never drops to his side, never holds anything`. Tránh để hai tay cùng buông thõng hai bên ở cuối clip khi một tay đang cầm đồ.

80. **ĐIỂM TỰA, FRAME 0 TRƯỚC HÀNH ĐỘNG, CHỪA NHỊP CUỐI, SỬA ĐÚNG KHỐI (Body Support & Pre-Action Frame — tiếp thu từ skill `yyl-video-prompt`, 11/10/2026):**
    - **Nguồn:** bài học thực chiến của skill `yyl-video-prompt` (ttfake92-lab/skills, đo trên Seedance 2.5). Không phải lỗi từ clip của dự án; chỉ lấy những điểm không trái luật FlowKit. Không lấy luật "chỉ viết điều quan trọng nhất" (trái Rule 56) và cách viết "ai cầm điện thoại quay" (trái Rule 52).
    - **Điểm tựa:** nhân vật ngả 45° mà không ghi vật đỡ → model cho người lơ lửng; ghi "lưng tựa vào tay vịn, tay vịn lún xuống" và câu khóa "suốt clip lưng tựa X" ở đầu prompt thì hết lỗi.
    - **Frame 0:** muốn giây 2–3 bắt chéo chân mà frame 0 không tả hai chân khép → model vẽ sai tư thế; tả frame 0 là trạng thái **trước** hành động thì đúng.
    - **Nhịp cuối:** model chạy gần đúng theo giây, sai số ~0.5s, nhịp cuối hay trễ → không đặt động tác chốt vào 0.5s cuối. Trên Omni Flash R2V chưa đo; khớp với kinh nghiệm thoại 23–25 từ phải xong trước ~9s ở clip 10s.
    - **Sửa prompt:** nói rõ sai gì, đổi thành gì, phần còn lại giữ nguyên → mặt và bối cảnh không chạy.
    - **Quy tắc:** dòng 42–45 checklist B (`prompt-lock.md`), `cinematic-toolkit.md` §9.

81. **THOẠI SẠCH DẤU DIỄN XUẤT, MẶT TRONG KHUNG KHI NÓI, ÂM THANH ≤ 5, TỪ LÀM ĐƠ HÌNH (Dialogue & Anti-Freeze Grammar — tiếp thu từ skill `video-prompt` của mikefluff/skills, 11/10/2026):**
    - *(Phim: ý "từ vựng camera dolly/orbit/crane trái Rule 42" chỉ đúng với vlog; phim được dùng từ vựng máy điện ảnh theo `/fk-camera-guide`.)*
    - **Nguồn:** skill `video-prompt` (mikefluff/skills), phần Veo 3.1 + `beat-structure.md` + `audio-prompting.md`. Không phải lỗi từ clip của dự án; chỉ lấy điểm không trái luật FlowKit.
    - **Dấu câu trong ngoặc kép:** `...`, chữ VIẾT HOA, kéo dài chữ trong câu thoại bị model bỏ qua hoặc đọc thành khựng/im lặng. Ngữ điệu đặt trước ngoặc (`Nora says (hushed, excited): "..."`). Test khủng long B: câu `"Okay, don't move... a baby Triceratops"` có khoảng im 0.75s ngay sau mấy chữ đầu — khớp với lỗi này (1 mẫu, chưa chứng minh).
    - **Mặt phải thấy khi nói:** khẩu hình chỉ khớp khi miệng trong khung. Test B: 0–1s Nora quay lưng về ống kính trong lúc đã bắt đầu nói.
    - **Âm thanh:** quá 5 yếu tố (thoại + nền + SFX) hoặc SFX lớn đè lên câu thoại thì thoại bị chìm; model không tự giảm âm nền khi có thoại nên phải viết sẵn `low under her voice`.
    - **Từ làm đơ hình:** `subtle smile`, `looks at`, `reacts`, `makes a gesture`… khiến model vẽ một tư thế rồi giữ nguyên. Thay bằng bộ phận + chuyển động + mốc; động tác đứng yên của NPC/thú viết dạng lặp `never fully stops`.
    - **Không lấy (trái luật đã chốt):** "không đặt thoại ở beat đầu" (trái Rule 54 — nói từ giây 0); từ vựng camera dolly/orbit/crane (trái Rule 42, góc máy vlog); "camera ghi cuối prompt" và khung `Beat 1/2/3` (trái Rule 55 — JSON); "không tả lại trang phục khi có ref" ở mức tuyệt đối (Bài học 78: phải chốt đủ 4 phần trang phục, nếu không model tự chế đúng phần bị bỏ sót); `--execute` gọi thẳng Gemini API (bỏ qua Flow, nhịp 45–60s và Rule 29).
    - **Quy tắc:** dòng 46–51 checklist B (`prompt-lock.md`), bảng cụm từ cấm ở `cinematic-toolkit.md` §8, `voice-bible.md` §2.

82. **TEST A/B KHỦNG LONG — TAY NEO BỊ BỎ KHI NÓI, THÚ QUAY ĐẦU NGOẮT, SAI CỠ CON NON, QUẦN LỆCH MÀU (Bài học clip test Hell Creek 66 Ma, 11/10/2026):**
    - **Bối cảnh:** 1 clip 10s, Nora quỳ sau khúc gỗ rêu, Triceratops con bước ra khỏi bụi dương xỉ và ăn lá. Bản A theo skill mới (dòng 42–45), bản B theo skill cũ. A ~8.5, B ~7.6 (`output/dino-ab-test/ab-plan.md`).
    - **Tay neo bị bỏ (A):** prompt ghi cẳng tay trái tựa khúc gỗ "for the whole clip", nhưng Nora nói hăng nên khua tay suốt. → Câu neo tay phải có `even while she talks, she never lifts it to gesture`.
    - **Thú quay đầu ngoắt (A, 8.1–8.3s):** đang cúi ăn, đầu quay từ chính diện sang nghiêng trong ~0.2s, nhòe chuyển động. → Mọi cú quay/ngẩng đầu của thú lớn ghi `slowly, over about one second, no sudden snap`.
    - **Sai cỡ (A):** "juvenile, about as tall as a pony" vẫn ra con to như trưởng thành, sừng dài chĩa trước (B ra đúng con non hơn). → Ghi cỡ so với vật trong khung (`its back is no higher than the top of the mossy log`).
    - **Quần lệch màu (A):** câu khóa có "tan suede leggings" nhưng ra quần nâu sẫm. → Ghi `golden-tan suede leggings, the same color as the tunic`.
    - **Lặp lỗi Bài học 78 (B):** hở đùi + đầu gối dù câu khóa chân giống hệt A — nhắc rằng câu khóa giảm xác suất chứ không xóa lỗi; review vẫn phải cắt cận chân ở cảnh ngồi/quỳ.
    - **Frame 0 (dòng 43) có dấu hiệu hiệu quả:** chỉ A giữ khủng long sau bụi ở giây 0 rồi bước ra; B đặt nó ngoài trống từ đầu.
    - **Quy tắc:** dòng 38 (màu quần), 52–54 checklist B (`prompt-lock.md`).

83. **POV NGOÁI SAU TRÊN LƯNG KHỦNG LONG BỊ ĐẢO CHIỀU, NGƯỜI CƯỠI BIẾN MẤT CUỐI CLIP (Bài học clip test rượt đuổi C — Hell Creek, 11/10/2026):**
    - **Bối cảnh:** 1 clip 10s viết theo skill mới (dòng 42–54): POV Nora cưỡi Triceratops con, ngoái nhìn ra sau suốt clip, bạo chúa đuổi phía sau, Triceratops ngoặt phải chui qua khe hai thân cây, bạo chúa quá to nên khựng lại ở khe. Điểm ~6/10 (`output/dino-ab-test/ab-plan.md`).
    - **Đảo chiều (cả clip):** model vẽ góc nhìn về phía trước qua diềm cổ Triceratops, nên bạo chúa ở phía trước và hai con lao vào nhau. Người cưỡi nhìn về trước là mặc định quá mạnh; câu `looking back over the hips` bị bỏ qua.
    - **Tách khỏi lưng thú (8.1s):** đầu gối Nora biến mất, khung hình rời khỏi lưng Triceratops; Triceratops thành con riêng đi về phía bạo chúa và áp sát mặt nó ở 8.5–9s (gần chạm, trái Rule 51). Bạo chúa không dừng ở khe như prompt.
    - **Phần đạt:** quần cùng màu áo, che kín gối (dòng 38 mới); tiếng gầm 3.75–4.75s đúng khung 3.5–5s lúc Nora im (dòng 49); thân cây trượt vào từ cạnh khung, không mọc ra; bạo chúa to hơn hẳn Triceratops (dòng 54).
    - **Quy tắc:** dòng 55–56 checklist B (`prompt-lock.md`).

84. **KHỦNG LONG TẢ BẰNG CHỮ RA ĐỒ CHƠI, SAI TUỔI, BIẾN HÌNH → BẮT BUỘC REF SHEET TỪ RESEARCH + MATERIAL (Creature Ref Lock — user lock 11/10/2026):**
    - **Hiện tượng:** các clip test A, B, C tả khủng long chỉ bằng chữ. Kết quả: chuyển động "như đồ chơi", không có khối lượng, chất liệu da kém; Triceratops ở A ra con trưởng thành sừng dài, ở C biến thành con nhỏ khác cuối clip. User: "không có tính vật lý, chuyển động tệ như đồ chơi, chất liệu không tốt — phải có ảnh ref 2 con khủng long chi tiết, ảnh character đàng hoàng các chi tiết vóc dáng", và "cần chạy fk-research và fk material để nghiên cứu khủng long tạo ảnh ref lại".
    - **Nguyên nhân:** không có ảnh ref thì model tự bịa hình dạng ở mỗi clip; prompt tả bằng chữ không đủ neo vóc dáng, da và cỡ. Thêm nữa server mặc định gắn "ONE single image only" vào prompt ảnh ref khi project có `story`, trái Rule 5.
    - **Quy tắc:** (1) mọi sinh vật trong khung có entity `creature` + sheet 16:9 (toàn thân nghiêng ⅔ | 3/4 trước | cận đầu và da); (2) chạy `/fk-research` trước để lấy cỡ theo tuổi, sừng/diềm, tư thế chân, da, miệng, dáng đi và tốc độ thật (ví dụ bạo chúa chỉ đi nhanh ~18–27 km/h, luôn một chân chạm đất — `.omc/research/hell_creek_dinosaurs_research.md`); (3) `/fk-add-material` tạo material chống đồ chơi/CGI (đã có `prehistoric_wildlife`) và chép text material vào `image_prompt`; (4) xóa logo → upload lại → user duyệt; (5) dữ kiện dáng đi/tốc độ từ research cũng vào `video_prompt`. Checklist B dòng 57; CLAUDE.md Rule 5.

85. **MÁY CỐ ĐỊNH NHÌN NGANG: THÚ CHẠY TẠI CHỖ, LỐI THOÁT BỊ VẼ THÀNH HẬU CẢNH (Bài học clip test D — Hell Creek, 11/10/2026):**
    - **Bối cảnh:** clip D viết lại theo time-vlog + research + 2 ref sheet khủng long (Triceratops v1, bạo chúa v2) + `Nora Body`. Máy dựng cố định nhìn ngang; Triceratops chở Nora phi qua khe hai thân cây, bạo chúa đi nhanh đuổi theo rồi khựng lại trước khe. Điểm ~7/10.
    - **Đạt nhờ ref + research:** da mờ, đóng bùn, không còn vẻ nhựa; bạo chúa đi nặng nề, bùn văng ở bước chân (~7.75s), gầm đúng 3.75–4.75s; Triceratops đúng con non sừng ngắn như ref; trang phục Nora khớp ảnh Body (quần da lộn cùng màu, bốt, tay áo dài), hai tay giữ diềm cổ, mặt thấy được.
    - **Lỗi 1 — chạy tại chỗ:** Triceratops đạp chân suốt 10s nhưng thân gần như không tiến, cuối clip áp vào một thân cây. Model giữ chủ thể ở giữa khung khi prompt chỉ ghi "phi từ trái sang phải".
    - **Lỗi 2 — lối thoát mất:** "hai thân cây đứng gần nhau bên phải đường" bị vẽ thành cây hậu cảnh, không có khe trên đường chạy; bạo chúa đi thẳng tới sát sau lưng Nora (đầu lơ lửng phía trên cô ở 7–10s) thay vì khựng lại trước khe. Không chạm, nhưng sai logic thoát thân.
    - **Quy tắc:** dòng 58–59 checklist B (`prompt-lock.md`).

86. **PROMPT TỰ MÂU THUẪN VÌ SỬA TỪNG CÂU, KHÔNG ĐỌC LẠI TOÀN BỘ (Self-Contradiction After Partial Edits — user hỏi 11/10/2026):**
    - **Hiện tượng:** prompt D sau khi cập nhật theo research ghi bạo chúa "heavy fast walk, never a run", nhưng còn sót "running along the same path", "keeps running", "runs from left to right" và "between the conifers" (bối cảnh đã đổi sang cây lá rộng). Đồng thời khung "does not move / never moves" nhưng `camera_response` lại "shakes slightly with each footfall". Bản có lỗi chữ "running" đã được gửi sinh; clip ra chạy tại chỗ (Bài học 85).
    - **Nguyên nhân:** sửa bằng cách thay đúng những câu đang nhớ, không đọc lại toàn bộ prompt; linter chỉ dò chuỗi cấm nên không bắt được hai câu nói ngược nhau; checklist B làm bằng tay và không có bước bắt buộc báo cáo, nên bị bỏ qua.
    - **Quy tắc:** mục D của `prompt-lock.md` (đọc lại toàn bộ sau mỗi lần sửa, gom câu theo thuộc tính, chạy hết checklist B, báo cáo tự đánh giá kèm prompt); linter có thêm `SPEED_CONTRADICTION` và `CAMERA_CONTRADICTION` (MEDIUM).

87. → chuyển sang [`vlog-archive.md`](vlog-archive.md) (máy dựng cố định phi lý với vlog cầm tay). Phim: máy cố định hay bám theo chọn theo nhịp kịch của cảnh.

88. **TỐI ĐA 7 REF (GIỚI HẠN OMNI FLASH), KHÔNG PHẢI 3 (user 11/10/2026):**
    - **Bối cảnh:** cảnh rượt đuổi E1 cần Nora (mặt), Nora Body, Triceratops con và bạo chúa = 4 ref; luật cũ "tối đa 3 ref" (Bài học 4, 47) buộc phải bỏ ref mặt dù checklist dòng 20 bắt POV có tay phải gửi mặt + Body. User: "dùng tối đa 7 ref chứ, Omni Flash chứ".
    - **Sự thật kỹ thuật:** Omni Flash nhận tối đa 7 ảnh ref (`OMNI_FLASH_MAX_REFERENCE_IMAGES = 7`, `agent/services/omni_flash.py`; server `_R2V_MAX_REFS = 7`). Khi scene có `character_names`, server lấy ref theo tên, mọi loại entity kể cả `creature`. Giới hạn 3 là luật kinh nghiệm từ test Ice Age thời còn ảnh ma-nơ-canh trang phục, không phải giới hạn API.
    - **Quy tắc:** gửi ref cho mọi thứ cần giữ nhất quán có trong khung, tối đa 7: thấy bất kỳ phần nào của vlogger → mặt + Body; mỗi sinh vật → ref của nó; bối cảnh cần giữ → `visual_asset`. Không gửi ref của thứ không có trong khung. Từ 5 ref trở lên soi kỹ trang phục khi review; nếu trang phục trôi lặp lại thì ghi bài học mới. Checklist B dòng 15.

89. **TEST E1 (POV CƯỠI TRICERATOPS, BẠO CHÚA CHẠY SONG SONG, 4 REF) — POV GIỮ ĐƯỢC LƯNG THÚ, NHƯNG KHOẢNG CÁCH SỐ KHÔNG GIỮ ĐƯỢC VÀ CÓ ĐỐM LÓA (11/10/2026):**
    - **Đạt:** khung ở trên lưng Triceratops và hai tay neo trên diềm cổ tới frame cuối (sửa được lỗi tách lưng của Bài học 83 nhờ câu khóa dòng 56); tay áo da lộn nâu vàng đúng, bàn tay đủ ngón; không hề lộ mặt Nora dù có ref mặt (4 ref); bạo chúa đúng ref, đi nặng, có mặt từ giây 0 ở mép trái, gầm khoảng 3.75–4.75s.
    - **Lỗi 1:** prompt ghi "never comes closer than about ten meters" nhưng từ 5s bạo chúa áp sát còn ~3–4 m ở mép trái khung (không chạm). Con số khoảng cách bị bỏ qua.
    - **Lỗi 2:** đốm lóa tròn màu hồng trôi qua khung ở 2.75–7s (khi trên thân cây, khi trên cổ bạo chúa) — lóa ống kính do câu "hazy sunlight slants in".
    - **Nhẹ:** Triceratops chạy chậm hơn "phi" và khung nảy ít hơn mô tả.
    - **Quy tắc:** dòng 61–62 checklist B.

90. **RỪNG TRÔNG GIẢ VÌ TẢ QUÁ ĐẸP + POV QUÁ MƯỢT (user 11/10/2026: "video không chân thực, cây cối nhìn giả giả, prompt không cần POV, quay theo đường chạy"):**
    - **Nguyên nhân:** prompt tả "tall straight dawn redwood trunks", "hazy sunlight slants in", "hazy sunbeams" → model vẽ rừng kiểu game: cây đều và cách đều, đường sạch, tia nắng có khối (dấu hiệu CGI), kéo theo đốm lóa. Không có chi tiết rừng thật (cây gãy, dây leo, rêu, lá rụng, bụi rối) và không có đặc tính máy quay thật (nhòe, nét trễ, sáng tối đổi, nhiễu, tiền cảnh lướt sát). POV E1 lại quá mượt.
    - **Quy tắc:** dòng 63 checklist B. Cảnh rượt đuổi: theo lựa chọn của user, quay máy chạy bám theo đường chạy (ngoại lệ điện ảnh, dòng 60).

91. **TEST F (MÁY BÁM THEO ĐƯỜNG CHẠY, RỪNG THẬT): RỪNG ĐÃ THẬT, NHƯNG BẠO CHÚA ĐUỔI KỊP RỒI XOAY NGOẮT 180° (11/10/2026):**
    - **Đạt:** rừng lộn xộn, trời âm u, không tia nắng/lóa (dòng 63 có tác dụng rõ — hết vẻ game); máy bám ngang, nền trôi, thấy tốc độ (không còn chạy tại chỗ); nước suối bắn thật; trang phục Nora đủ 4 phần, hai tay giữ diềm, ngoái lại thấy mặt; gầm ~3.75–4.75s.
    - **Lỗi:** từ ~6s bạo chúa đuổi kịp, chạy song song, đầu ngang tầm Nora; ~7.3–8.0s nó xoay ngoắt 180° trong < 0.5s, đuôi quét ngang qua lưng Triceratops (gần chạm, trái Rule 51); cú "trượt chân ở bờ bùn rồi tụt lại" không xảy ra.
    - **Vận hành:** lần sinh trước đó bị Flow nhận rồi bỏ ngầm (không có media trong project sau 17 phút), lần gửi lại bị `UNUSUAL_ACTIVITY`; sau khi user xóa cookie, lần thứ ba xong trong 6.7 phút (chậm hơn bình thường ~2.7 phút). Khi một request chậm hơn ~2 lần bình thường, kiểm `GET /api/flow/debug-listing/<operation_id>?project_id=<pid>` thay vì chờ hết 15 phút.
    - **Quy tắc:** dòng 64 checklist B.

92. **TEST F2 (BẠO CHÚA GIỮ Ở XA): 9 GIÂY ĐẦU ĐẠT, GIÂY CUỐI MỌC CON BẠO CHÚA THỨ HAI; CƯỠI THÚ LÀM HỞ ĐÙI (11/10/2026):**
    - **Đạt:** bạo chúa ở xa phía sau suốt 0–9s đúng dòng 64 (không đuổi kịp, không xoay người); rừng thật, lá tiền cảnh lướt sát ống kính ~6.75–7.75s tạo chiều sâu; gầm ~3.75–4.75s; Nora ngoái lại thấy mặt.
    - **Lỗi 1 (nặng):** 9.25–10s một con bạo chúa thứ hai, to và nhòe, lao vào từ mép phải tiền cảnh, che cả Nora, trong khi con thứ nhất vẫn ở xa. Khi ref sinh vật bị giữ nhỏ cả clip, model "dùng" ref đó bằng một bản sao lớn ở cuối.
    - **Lỗi 2:** lộ dải da đùi giữa vạt áo và cổ bốt khi Nora ngồi dạng chân cưỡi thú — câu khóa chân kín (dòng 38) không đủ cho tư thế cưỡi.
    - **Quy tắc:** dòng 65 checklist B; dòng 38 thêm tư thế cưỡi: `even while riding astride with her knees apart, golden-tan suede leggings cover her thighs completely up to the tunic hem`.

93. **SHEET REF SINH VẬT: PANEL CHÍNH DIỆN LẬT GƯƠNG DẤU BẤT ĐỐI XỨNG, 2 PANEL CÙNG HƯỚNG, LỘ RĂNG, TỰ CHÈN SỐ (Hell Creek v2, 14/10/2026):**
    - **Hiện tượng (3 vòng sinh 14 ref):** (1) Prompt "Panel 1 LEFT three-quarter / Panel 2 RIGHT three-quarter" → model vẽ cả 2 panel cùng hướng (BD, TR, CG vòng 1). (2) Panel 3 chính diện: dấu bất đối xứng (sừng gãy TRÁI của Bò Đực, vệt má PHẢI của Con Non) bị đặt sai bên hoặc nhân đôi ra cả 2 má — kể cả khi ghi rõ "bên phải ảnh = bên trái con vật" (vòng 2). (3) T. rex "lips cover the teeth" vẫn lộ hàm răng. (4) Panel 3 kiểu 3/4 có lúc kèm chữ số "2" tự chèn. (5) EDIT mặc outfit lên Body trần làm ngực nhỏ đi, sinh lại có thể đổi bên bình đeo hông.
    - **Quy tắc:** (a) Tả hướng bằng **đầu chỉ về mép nào của ảnh** + **sườn nào hướng máy**: `Panel 1 (left third) … head pointing toward the LEFT edge of the image, so its LEFT flank faces the camera; Panel 2 (middle third) … mirrored, head toward the RIGHT edge`. (b) Sinh vật có dấu bất đối xứng: panel 3 **không dùng chính diện thuần** mà là `close-up of the head seen from the front-<bên có dấu>, looking slightly past that side of the camera, so the <dấu> is nearest the camera` (Rule 58 chấp nhận biến thể này cho sinh vật bất đối xứng). Sinh vật đối xứng giữ chính diện. (c) Bạo chúa môi kín: `mouth firmly shut like an iguana's or a monitor lizard's: thick scaly lips seal the jaws in one smooth continuous lip line … zero teeth are visible anywhere` + negative `NOT any visible tooth`. (d) Review ref: soi chữ/số tự chèn trong khung; nền phẳng thì tẩy cục bộ bằng mảng nền lân cận (không chép qua vạch chia panel), không cần sinh lại. (e) Mỗi lần EDIT lại Body: so bình/đạo cụ cố định đúng bên với bản đã duyệt trước khi thay; giữ bản cũ nếu bản mới đổi bên. (f) Khi 3 vòng vẫn không sửa được (Infernodrakon cánh xòe như vây, đuôi Edmontosaurus bị cắt mép panel) → dừng, báo user, ghi giới hạn vào `video_prompt` của clip dùng ref đó.
    - **Đổi kèm:** `prompt-lock.md` checklist B dòng 39.

94. **ĐẠO CỤ CHÍNH TRÔI HÌNH GIỮA 2 CLIP CHUYỂN CẢNH — MAI RÙA A1-06 ≠ A1-07 (Canonical Prop Look — Hell Creek v2, 15/10/2026):**
    - **Hiện tượng:** A1-06 (nhặt mai rùa trên sỏi, vốc nước) và A1-07 (buộc mai rùa làm bình đeo hông) ra hai cái mai khác hẳn nhau: A1-06 mai trắng bạc như vỏ sò, A1-07 mai nâu sẫm có vảy; dây buộc dài thõng tới gối, khác bình trên sheet `Nora Body`.
    - **Vì sao Rule 65 không cứu được:** hai clip là **chuyển cảnh** (đổi góc, đổi việc), mỗi clip có Start Frame `GENERATE_IMAGE` riêng. Last Frame chỉ khóa liên tục *trong chuỗi*; giữa các chuyển cảnh, đạo cụ chỉ giống nhau nếu **chữ + ref** giống nhau.
    - **Nguyên nhân (4 cái, đều do prompt):** (1) A1-06 tả mai `sun-bleached clean` → mâu thuẫn với bình nâu sẫm trên sheet Body. (2) `image_refs` của A1-06 thiếu `Nora Body` — ảnh duy nhất cho thấy cái mai thật. (3) Sổ liên tục (`nora_state`) chèn câu "bình đã đeo ở hông trái" vào A1-07 — đúng clip đang buộc bình — nên prompt tự mâu thuẫn (Bài 86). (4) Không ghi độ dài dây / vị trí so với thắt lưng.
    - **Quy tắc:**
      1. **Một câu tả chuẩn cho mỗi đạo cụ chính** (`SHELL_LOOK`, `KNIFE_LOOK`…) — hằng số trong `common.py`, dùng nguyên văn ở **mọi** clip có đạo cụ đó, kể cả clip trước khi nó thành đồ đeo (lúc nhặt, lúc chế tác). Câu gồm: kích thước, hình dáng, màu mặt ngoài / mặt trong, hoa văn, trỏ thẳng `the same … as in {{ref:<V> Body}}`, và nó KHÔNG phải cái gì (`never white, never bleached, never a seashell`).
      2. **Không tính từ trái với ref:** cấm `bleached`, `clean`, `new`, `shiny`, `white` … khi đạo cụ trên ref có màu khác. Muốn tả "cũ, rỗng" thì tả trạng thái (`long empty`), không đổi màu.
      3. **Clip có đạo cụ phải đính ref chứa đạo cụ đó** — cả `image_refs` (Start Frame) lẫn `character_names` (video). Đạo cụ nằm trên sheet Body → clip đó đính `<V> Body` dù Nora chỉ hiện tay.
      4. **Clip chuyển trạng thái đạo cụ** (nhặt → buộc, nguyên → vỡ, đeo → mất) được **miễn câu trạng thái của sổ liên tục**; clip tự ghi `At second 0 … by second N …` để không có hai câu trạng thái cãi nhau.
      5. **Đồ đeo ghi hình học gắn:** dây dài bao nhiêu (`a hand's width of cord`), nằm đâu so với thắt lưng, bên nào, `never dangling down at knee height`.
      6. **Review Start Frame:** đặt ảnh 2 clip liền kề có cùng đạo cụ cạnh nhau và cạnh sheet Body trước khi duyệt.
    - **Đổi kèm:** `prompt-lock.md` checklist B dòng 41; `SKILL.md` §QC hàng Q2 + "Lỗi hay gặp".

95. **TAY POV LẤY TỪ `<V> BODY`, KHÔNG TỪ SHEET `<V> HAND` RIÊNG — THAY BÀI 72 (user 15/10/2026):**
    - **Hiện tượng:** Start Frame A1-06 (POV, hai tay nhặt mai rùa) đính `Nora Hand` (sheet chỉ có bàn tay trần trên nền xám) ra cẳng tay đàn ông nhiều lông, móng bẩn, kèm ống tay áo dài sờn mép — trong khi outfit là áo lanh **tay ngắn**.
    - **Nguyên nhân:** sheet Hand không có cẳng tay lẫn tay áo, nên model tự bịa phần còn lại; câu `the edge of a short sleeve shows at the side of the frame` lại mời model vẽ vải lên cẳng tay.
    - **Quy tắc:** clip POV có tay đính `<V> Body` (không đính `<V> Hand`) và trỏ: `her hands and bare forearms are exactly the hands and arms of the woman in {{ref:<V> Body}}: slender, smooth, hairless … her sleeves are short and end above the elbow, so no sleeve, cuff or fabric is anywhere on her forearms`. Negative thêm `NO hairy forearms, NO long or frayed sleeve on the forearm`. Outfit tay dài thì tả cổ tay áo đúng như trên Body, vẫn trỏ Body.
    - **Không sinh lại sheet Hand từ Body:** đã thử (15/10) — EDIT từ cả sheet Body bị `UNSAFE_GENERATION` 2 lần (panel trước có cổ áo khoét sâu); crop panel lưng thì qua nhưng ra sheet có tay áo trôi lơ lửng. User chốt: chỉ đính Body và nhắc tay trong prompt là đủ.
    - **Đổi kèm:** `SKILL.md` hàng "Bộ ref vlogger"; `prompt-lock.md` checklist B dòng 32.

96. **DÂY DẮT NGỰA BỊ ĐỨT LÀM HAI KHÚC, MỖI NGƯỜI CẦM MỘT KHÚC (Single Continuous Rope Lock — EMBERS RA-02, 18/10/2026):** Hai nhân vật cùng giành một sợi dây/dây cương/dây thừng trong cùng khung hình → model vẽ dây đứt giữa chừng hoặc nhân thành 2 sợi, mỗi người cầm một khúc. User: lỗi = sinh lại (không cắt). **Cách sửa:** thêm khối `props_lock` "exactly ONE lead rope, a single continuous unbroken rope clipped to the halter; A grips it near the halter, B holds the free end"; ở mốc giành dây ghi "grabs the same rope … both hold one single unbroken rope"; ở mốc giật ghi "the whole rope slides out of A's fingers in one piece … A's hands are now empty"; thêm câu cấm "never breaks, never snaps, never splits into two pieces, never duplicates; nobody holds a separate piece of rope". Áp cho mọi đạo cụ dài mềm hai người cùng cầm (dây, xích, khăn, dây cương). **Lần 2 vẫn hỏng** (dây chỉ nối tay-với-tay, không gắn dây cương, thừa một khúc chạm đất) → **đổi cách diễn: chỉ MỘT người cầm dây**, người kia túm dây cương/quai má hoặc vai; giữ nguyên thoại và ý cảnh.

97. **CẢNH "SUÝT CHẠM" BỊ MODEL DIỄN THÀNH CHẠM HẲN (Near-Touch Lock — EMBERS RA-03, 18/10/2026):** prompt "hand stopping just short of the muzzle, then pulling back" → tay vuốt luôn mõm ngựa, mất ý cảnh; máy "static tripod" vẫn lùi ra. **Cách sửa:** ghi khoảng cách cụ thể ("fingertips stop about 10 cm short … a clear gap of air … never touching"), chia 3 nhịp (vươn tới → khựng một nhịp, ngón co lại → rút ra khỏi khung), câu cấm "never touches, strokes, pats or rests on …"; máy ghi "locked-off, never moves, never zooms, never pulls back; only the focus shifts". Clip 4s quá ngắn cho beat 3 nhịp này → dùng 6s (user).

98. **NHÂN VẬT ĐI XUYÊN HÀNG RÀO (Obstacle Path Lock — EMBERS RA-05, 18/10/2026):** prompt chỉ ghi "walks away / walks toward the trailer" trong khi khung hình có hàng rào chắn giữa → model cho nhân vật đi xuyên qua thanh rào. **Cách sửa:** khi có vật cản trong khung (rào, cổng, xe, cột, bàn), ghi rõ đường đi so với vật cản ("walks toward frame-left along the outside of the fence, parallel to it, staying on the open gravel") + câu cấm "never touches, climbs or walks through the fence; the rails stay solid and unbroken". Hướng đi phải khớp những gì Start Frame cho thấy (không gọi tên vật không có trong khung).

99. **CÓ RADIO TRÊN HÌNH THÌ CLIP IM LẶNG VẪN BỊ LỒNG TIẾNG (Radio Ghost Speech — EMBERS EM-01, 19/10/2026):** cảnh im lặng có bộ đàm trên ngực nhân vật ("the radio crackles; he turns his head to it") → Omni tự cho nhân vật nhấc radio lên miệng và lồng một câu điều phối bịa ra (v1 "I've had to treat", v2 tiếng lẩm bẩm, v3 "All units be advised, we have a missing firefighter… Eli is not answering his radio", sai cả cốt truyện). Đã thử cấm bằng câu ("radio stays clipped, he never touches it, lips pressed shut", audio "no voices, no words at all") nhưng v3 vẫn hỏng. Whisper bắt được cả 3 lần (EXTRA SPEECH / SPEECH IN A SILENT CLIP), còn khung hình nhìn bình thường. **Cách sửa:** câu thoại phát qua radio là `post_vo`, thêm ở khâu dựng. Trong clip im lặng, **không để bộ đàm xuất hiện trên hình**: nhân vật chỉ khựng lại, nghiêng đầu như vừa nghe thấy gì. Nếu bắt buộc phải có radio, chấp nhận tắt hoặc thay tiếng gốc của clip khi dựng và ghi rõ điều đó vào `review_note`.

100. **KIỂM GHOST BẰNG `debug-listing` CŨNG LÀ REQUEST TỚI FLOW (Listing Reads Count — EMBERS EL-03, 19/10/2026):** script chờ clip gọi `GET /api/flow/debug-listing/<op>` mỗi 45s suốt 40 phút, trong lúc EL-03 bị ghost op. Mỗi lần gọi là một RPC đọc media của project (`RPC_PROJECT_MEDIA`) gửi tới Flow. Ngay sau đó, lần gửi kế tiếp dính `PUBLIC_ERROR_UNUSUAL_ACTIVITY`. **Cách làm:** mỗi clip chỉ kiểm ghost **2 lần** (khoảng phút 3 và phút 12). Quá 12 phút mà op không có trong project thì kết luận ghost: đặt request về FAILED với `retry_count=99` rồi mới gửi lại. Clip Omni r2v bình thường xong trong khoảng 1,5–2 phút, nên quá 5 phút là dấu hiệu ghost. Cùng một clip ghost 2 lần thì nghi bộ lọc an toàn im lặng chặn nội dung prompt: kiểm ảnh ref bằng `GET /api/flow/debug-project-media` (cả 18 ref EMBERS đều có), rồi soát câu thoại tìm cụm dễ bị hiểu sai. Ví dụ EL-03: "I'm here to buy her back! I've got forty dollars!" không có ngữ cảnh con ngựa nên ghost 3 lần, kể cả khi đã thêm ngữ cảnh. Gửi lại bằng câu không mua bán. **Kết luận sau 9 lần gửi (19/10/2026):** thủ phạm là **bất kỳ ý trả tiền nào trong thoại**. Câu "Please, I can pay!" vẫn ghost thêm 5 lần, dù đã lần lượt bỏ dây thừng, xe đạp, lửa, đổi bộ ref và chuyển sang project có ảnh ref mang tên. Chỉ khi đổi thoại thành "I came for Juniper! Is anyone here?" thì clip mới sinh được ngay. Một nhân vật trẻ đứng một mình, nói với một người đàn ông chuyện trả tiền hay mua bán, rất dễ bị Flow chặn im lặng như một lời gạ gẫm. Ý mua hay chuộc lại, nếu cần, đưa vào `post_vo` hoặc phụ đề khi dựng.

101. **CẢNH TRANH CÃI BỊ NÓI BÌNH BÌNH, NHỎ NHẸ (Argument Delivery Lock — EMBERS CH-03, 19/10/2026):** prompt ghi "speaking low and hard", "his voice drops" → Omni đọc câu đối đầu nhỏ nhẹ, đều đều; user: "cần to tiếng kiểu ngăn ngản chứ, không bình bình… những đoạn tranh cãi cần như vậy". **Cách sửa:** mọi câu cãi nhau / chặn đường / ra lệnh dưới áp lực ghi rõ ở `speech.delivery` và nhịp timeline: "loud and sharp, voice raised over the roar of the fire, every word hard, clipped and forceful, each short sentence punched out like an order"; nhịp giữa "stays loud and hard, jaw clenched, leaning toward her"; `audio` để giọng nói nổi trên tiếng lửa. Bỏ "low / quiet / voice drops / flat" trừ khi kịch bản muốn giọng thì thầm đe dọa. Không trích lại câu thoại trong ngoặc kép ở nhịp khác (model có thể nói hai lần).
    - **Tái phạm EMBERS BN-04 v1 (20/10/2026):** prompt chỉ ghi "loud and bitter" / "loud and sharp" / "loud and clipped" rải rác từng nhịp, không có khối khoá đầy đủ → Omni vẫn đọc như nói chuyện thường; user: "cãi nhau mà giọng bình thường vậy phải hét gắt lên chứ". **Một chữ "loud" là không đủ.** Bắt buộc cả bốn chỗ: (1) `speech.delivery` = "a furious argument shouted at full volume over the roar …: voices raised to a yell, every word hard, clipped and forceful, each short sentence punched out like an order, fast and hoarse, no pauses between lines, never calm, never slow, never a normal speaking voice"; (2) mỗi nhịp có thoại dùng động từ **yells** (không dùng "says") + "at the top of his/her voice" / "yells straight back … right after his line with no pause"; (3) `characters.state` có thân thể căng (mồ hôi chảy qua bồ hóng, hàm nghiến, gân cổ nổi, hét bằng cả lồng ngực); (4) câu cấm "Every line is yelled hard and fast at full volume: never a normal talking voice, never calm or relaxed, no soft voice, no slow talking, no pauses, no gentle look."

102. **ĐANG CHỮA CHÁY MÀ NÓI CHẬM, MẶT BÌNH THẢN (Danger-Zone Urgency Lock — EMBERS LH-02, 20/10/2026):** LH-02 v1 (Ray giao nhiệm vụ giữ trường học khi lửa đang tới) bị user trả: "đang chữa cháy sao biểu cảm bình tĩnh vậy, nói chậm vậy… cần review prompt những cảnh gây cấn chứ không nhàm chán". **Gốc lỗi:** mẫu chung của `prompts_v7.json` ghi mọi câu thoại là *"The line runs on from 0s through 6s, spoken at a natural pace"*: kéo 12 từ ra 6s nên Omni đọc chậm. Thêm vào đó, nhân vật chỉ "đứng, quay đầu" nên mặt bình thản. Lỗi này không chỉ ở cảnh cãi nhau (Bài 101) mà ở **mọi clip có thoại trong vùng nguy hiểm**.
    **Cách sửa (LH-02 v2 đạt 8.12):**
    - `speech.delivery`: `"shouted fast and hoarse over the fire roar: an urgent, clipped command voice, no pauses, never calm, never slow"`.
    - Tách câu thoại theo nhịp (`0-2s` câu 1, `2-4s` câu 2) và ghi `"His whole line is finished by second 4"`. Bỏ `natural pace` và `runs on from 0s through 6s`.
    - `characters.state`: trạng thái căng thẳng bằng thân thể, ví dụ `"sweat running through the soot; jaw clenched, eyes darting between the fire and his crew, shouting with his whole chest; he never stands still"`. Đây là biểu cảm, không phải tả ngũ quan (Rule 60).
    - Timeline luôn có chuyển động và áp lực: nhân vật sải bước, vung tay chỉ; nhóm làm việc hết tốc lực phía sau; gió hất tàn lửa; một đám cháy nhỏ bùng lên ở nhịp cuối để nhân vật phản ứng.
    - `audio`: `"loud wildfire roar, hot wind gusts, … <name> shouting over it all"`.
    - Câu cấm: `"<name> is never calm or relaxed: no slow talking, no soft voice, no pauses between words, no standing still, no gentle smile."`
    - Máy quay cầm tay, rung theo gió, đi theo nhân vật.
    **Phạm vi:** áp cho mọi clip có thoại trong lúc nguy hiểm đang diễn ra (cháy, bão, rượt đuổi, cứu người, sơ tán). **Giữ nhịp chậm có chủ đích** chỉ cho beat lặng: hậu quả, nghỉ, tha thứ, câu một từ kiểu "Mom.", thì thầm khi ẩn nấp. **Hệ quả Whisper:** giọng hét làm cao độ tăng (LH-02 v2: 327–372 Hz với giọng nam) nên sẽ bật cờ `? VOICE?`; báo user nghe lại, không tự đánh trượt.

103. **CẢNH CHÁY RỪNG CHỈ CÓ VÀI CÂY CHÁY, MÁY QUAY XA (Whole-Forest Burn & Close Camera Lock — EMBERS RR-13, 20/10/2026):** clip RR-13 (Nora chạy qua rừng cháy, cành cây rơi suýt trúng) mất 3 lần sinh mới đạt.
    - **v1 (7.25):** cành cây rơi đè lên lưng Nora, trong khi prompt chỉ ghi "a few steps ahead". Cảnh ra ban ngày dù prompt ghi "night".
    - **v2 (7.45):** user trả: "cảnh cháy cần cháy đều, góc máy gần hơn chứ cháy có 1 cây vậy". **Gốc lỗi:** prompt chỉ tả lửa ở ngọn cây ("crown fire leaps from treetop to treetop") và dùng máy xa, ống kính dài. Kết quả là vài đốm lửa lẻ trên nền rừng xanh, trời xám. Model còn vẽ một khúc cây cháy bay ngang kéo vệt khói như cây đuốc.
    - **Cách sửa (v3 đạt 7.85):**
      - `setting`: `"The whole forest on both sides of the road is burning evenly: flames climbing every pine trunk and roaring in every crown, burning undergrowth and pine needles along both edges of the road, a continuous wall of fire in the background in every direction; no unburned trees in sight. Light: the fire is the main light…"`.
      - `camera`: máy cầm tay chạy song song, **cách nhân vật 3–4 mét, khung từ gối trở lên**, lửa lấp kín hậu cảnh. Không dùng `WS` hay ống kính dài cho cảnh "nhân vật giữa đám cháy".
      - Câu cấm: `"The fire is never limited to one or two trees: the whole forest … burns evenly for the whole clip; no grey daylight, no green unburned trees."` và `"No burning object ever flies sideways through the air; … the only falling object is the one limb, dropping straight down."`
      - Vật rơi gần người: ghi khoảng cách bằng mét và câu `"Nothing ever falls on her or touches her"`.
    - **Còn lệch ở v3, chấp nhận được:** kính bảo hộ đeo ở cổ, cô chạy về phía máy thay vì từ trái sang phải, ánh sáng vẫn hơi mờ khói. Đêm thật vẫn khó ra khi dùng ref bối cảnh ban ngày; cần đêm thì phải có ref bối cảnh ban đêm.
    - **Áp cho MỌI cảnh có cháy, kể cả cảnh vắng người / cảnh đạo cụ (RR-10, 20/10/2026):** prompt RR-10 đầu tiên chỉ có "hàng cây sau chuồng cháy" và trời hoàng hôn. User dừng lại trước khi sinh: "cảnh cần cháy mạnh hơn", "cháy đều rừng lửa". Cách viết đúng: cả rừng quanh địa điểm cháy đều mọi hướng, từ thân lên ngọn, lửa cao bằng cây; có lửa ở cự ly gần (cỏ, hàng rào cháy cách đạo cụ 3–4 m); lửa là nguồn sáng chính; mưa tàn lửa dày. Kèm câu cấm: `"The fire is strong and everywhere for the whole clip, never a few small flames or one burning tree, never grey daylight."`
    - **Chữ không thắng ref bối cảnh ban ngày — cần ref bối cảnh đang cháy (RR-13 v5 / RR-14 v4, 20/10/2026):** chỉ thêm chữ "lửa mạnh" thì RR-14 v3 và RR-13 v4 vẫn ra rừng mờ khói ban ngày, vì ref Ridge Road ban ngày kéo ảnh về. Khi tạo ref `Ridge Road Fire` bằng EDIT từ ref ban ngày và dùng thay ref cũ, cả hai clip ra lửa mạnh đều cả rừng, trời cam. Mỗi địa điểm có cảnh cháy cần một ref "đang cháy" riêng. Ref EDIT có thể dính vệt lốp mờ trên đường, nên kèm câu cấm vệt lốp. Lửa mạnh không sửa được lỗi hành động: ở v5 cành cây vẫn rơi trúng người, dù prompt ghi rơi 4 m phía trước.
    - **Ref "đang cháy" phải cùng giờ trong ngày với các clip kề bên (RR-10 v3 / RR-11 v3, 20/10/2026):** ref `Keller Barn Fire` đầu tiên có trời đen cam. Clip không người RR-10 v2 chép nguyên ánh sáng đó nên ra tối như chạng vạng. Clip có Nora RR-11 v2 lại kéo về ánh sáng ban ngày như RR-13/14. Kết quả là hai cảnh liền nhau lệch ánh sáng (user: "sai nguyên lý"). Cách sửa: EDIT lại ref, giữ nguyên bố cục và lửa, chỉ đổi giờ trong ngày cho khớp các clip đã duyệt kề bên (chiều muộn, trời hổ phách nhạt qua khói, mặt trời là một đĩa cam mờ). Trước khi tạo ref cháy, đặt một khung của clip đã duyệt ngay trước cạnh ref để so ánh sáng. Prompt clip cũng không được ghi "never daylight / never grey daylight" khi chuỗi đang ở ban ngày; thay bằng câu khóa "same smoke-filtered late-afternoon light as the previous shots; never dusk, never night".
- **Đạo cụ không người chạm thì nằm im (RR-10 v4, 20/10/2026):** prompt cũ cho "bánh trước xe đạp còn quay" để gợi Eli vừa rời đi. User: "bánh xe không tự quay không tự chuyển động. xe nằm yên". Model còn làm bánh nhấc lên và xe dựng dậy (v3). Không viết chuyển động cho vật vô tri khi không có lực tác động trong khung (người, gió mạnh, va chạm). Kèm câu khóa "completely still for the whole clip … only the fire, smoke, embers and the camera move". Lưu ý: chữ "lying on its side, both wheels resting on the ground" ở góc máy sát đất ra xe đứng thẳng trên 2 bánh. Muốn thấy xe nằm thì dùng góc cao chếch xuống.
- **Vị trí đạo cụ giữa 2 cảnh kề nhau phải khóa bằng ảnh ref, không bằng chữ (RR-10 v6, 20/10/2026):** RR-10 v5 khóa hướng xe bằng chữ (đầu xe trái) nhưng model tự đặt xe giữa sân, còn RR-11 đã duyệt để xe sát cột cổng. User: "cần gen ảnh ref chỗ xe với nhà này thì nó mới liên tục được". Cách làm: cắt frame của cảnh kề đã duyệt có thấy rõ đạo cụ, tẩy logo, upload, rồi EDIT_CHARACTER_IMAGE xóa nhân vật ("Remove the woman… keep everything else exactly in position"). Kết quả là một location ref mới (ví dụ "Keller Gate Bike"). Cảnh cần khớp dùng ref này thay ref địa điểm chung, prompt ghi "the same camera position and framing as {{ref}}" và "lying in exactly the spot it lies in the reference". v6 khớp cả vị trí lẫn hướng xe ngay lần đầu (8.65).
- **Cảnh liên tục bắt buộc có ảnh ref bối cảnh riêng của đúng chỗ đó (user 20/10/2026: "các cảnh liên tục thì cần có ảnh ref bối cảnh đó"):** áp dụng khi nhiều clip liền nhau quay cùng một chỗ (cổng chuồng, cửa chuồng, khúc đường…). Ref địa điểm chung (vd. "Keller Barn Fire") không đủ: model tự dựng lại kiến trúc, cửa, hàng rào và chỗ đặt đạo cụ mỗi lần một kiểu. Trước khi sinh clip kế tiếp:
  1. Lấy frame thấy rõ bối cảnh từ clip đã duyệt gần nhất ở chỗ đó.
  2. Tẩy logo, upload, rồi EDIT_CHARACTER_IMAGE xóa người và thú (giữ nguyên vị trí mọi thứ còn lại).
  3. Lưu thành location ref mang tên đúng chỗ (vd. "Keller Gate Bike", "Keller Barn Door").
  4. Mọi clip tiếp theo ở chỗ đó dùng ref này thay ref chung.
  Chỉ một clip quay ở chỗ đó thì ref chung là đủ.

71. **ĐỘ DÀI CLIP LINH HOẠT THEO ĐỘ KHÓ — CẢNH DỄ LỖI SINH CHUỖI 4s CÙNG BỐI CẢNH, CẢNH DỄ GIỮ 8s/10s (Variable Duration & 4s Chain — User Lock 12/10/2026):**
    - **Hiện tượng:** Skill cũ mặc định mọi clip 8s. Clip hành động 8–10s nhồi 3–5 thay đổi trạng thái (thú lao tới → dừng → máy rơi → lật lên tán cây) nên càng về cuối clip càng trôi: thú đổi dáng, tay/đạo cụ teleport (Bài 70), vật hiện/biến (Bài 48). Một chỗ hỏng ở giây 6 bắt sinh lại cả clip 8s.
    - **Quy tắc:**
      1. **Chọn `duration` theo độ khó, không theo mặc định.** Dễ lỗi (chuyển động nhanh, tương tác thú, ngã / rơi máy, sinh vật lớn đi ngang khung, VFX chớp sáng / mưa kính / sóng chấn động, vật đổi trạng thái: vỡ, đứt, đổ) → **4s**. Dễ và không chuyển cảnh (selfie nói chuyện, fixed cam, lia chậm, phong cảnh) → **8s**; long take, master take, cảnh cuối im lặng → **10s**; lưng chừng → **6s**.
      2. **Chuỗi 4s = một cảnh liền, cắt thành nhiều mắt xích (CẤM CHUYỂN CẢNH).** Đặt ID `A1-12a / b / c`. Mỗi mắt xích **chỉ một hành động** (một pha của `fk-action-choreography`).
         - **RÀNG BUỘC THÉP TRONG CHUỖI 4s:** Giữ nguyên 100%: bộ ref (tối đa 7), câu `Setting` + trạng thái ánh sáng, và **vị trí máy + góc máy + cỡ cảnh**. **TUYỆT ĐỐI CẤM CHUYỂN CẢNH / ĐỔI GÓC NHÌN GIỮA CÁC MẮT XÍCH**. Mắt xích sau mở **đúng tư thế / vị trí** mắt xích trước kết thúc (Rule 44), viết thẳng vào khối `Everything is already in place from the very first frame` (`"the bull is already standing six metres away, head low, from the very first frame"`).
         - **CẢNH PHỨC TẠP CÓ CHUYỂN CẢNH / ĐỔI GÓC:** Nếu phân đoạn đòi hỏi đổi góc nhìn (ví dụ: góc 1 thấy dã thú lao tới → góc 2 cận cảnh khuôn mặt hét → góc 3 thấy chân trượt bùn), **TUYỆT ĐỐI CẤM GOM VÀO CHUỖI `a/b/c`**. Phải tách thành các **Scene ID riêng biệt** (độ dài 4s hoặc 6s), kết nối bằng kỹ thuật dựng phim (Cut / Match on Action / Whip-pan / Khung che/Wipe).
      3. **Thoại theo bảng Rule 49 (0):** 4s = 0 từ (hành động) hoặc 6–8 từ chia `0-2s / 2-4s`. Chuỗi hành động thường 0 từ (thở dốc, Foley); câu nói dồn vào mắt xích cuối hoặc clip 8s kế tiếp.
      4. **Dựng:** 4s trim `-ss 0.5` → 3.5s dùng được; cắt thẳng giữa các mắt xích (match on action), không crossfade. Runtime tính theo thời lượng dùng được, không theo số clip × 8.
      5. **Sinh lại theo mắt xích:** mắt xích nào rớt review thì chỉ sinh lại mắt xích đó; mắt xích kế tiếp vẫn dùng được vì điểm nối đã khóa bằng chữ.
    - **Đổi kèm:** CLAUDE.md Rule 11 + Rule 49 (0); `SKILL.md` hàng "Độ dài clip"; §1 bảng tra nhanh.

72. → chuyển sang [`vlog-archive.md`](vlog-archive.md) (bản 2: sheet `<Vlogger> Hand` cho POV vlog; đã thay bởi Bài 95).

73. **ĐẶC TẢ CHẤT LIỆU SINH HỌC KHỦNG LONG, TẬP TÍNH THỊ UY & TRIỆT TIÊU CGI (Prehistoric Reptilian Megafauna Material Lock, Territorial Behavior & Anti-CGI Realism — Bài học Chuỗi Khủng Long Bò Đực A1-12 Hell Creek 66 Ma, User Review 13/10/2026, Rule 57):**
    - **Hiện tượng & Nguyên nhân gốc rễ (Root Cause):**
      1. **Khủng long bị "giả trân" như tượng sáp hoặc đồ chơi 3D (CGI / Plastic Toy Glitch):** Khi mô tả khủng long hoặc bò sát khổng lồ, nếu prompt chỉ ghi chung chung tên loài (`Triceratops`, `T. rex`, `realistic`) mà thiếu các đặc tả sinh học sâu, AI video diffusion model (Veo 3, Flow, Sora) có xu hướng sinh ra một bề mặt da nhẵn thín, bóng loáng như nhựa dẻo, mắt đen vô hồn, ánh sáng phẳng lỳ như mô hình bảo tàng rẻ tiền hoặc game 3D đời cũ.
      2. **Nhầm lẫn tập tính sinh thái (Thú ăn cỏ vs Thú săn mồi):** Khủng long ăn cỏ khổng lồ (Triceratops, Sauropod) tấn công do **bảo vệ lãnh thổ và đàn con**, KHÔNG PHẢI ĐỂ ĂN THỊT. Do đó, chúng không lao vào cắn xé như quái vật phim kinh dị, mà thực hiện chuỗi hành vi: **Dọa xông (mock charge) $\to$ Trượt cày đất phanh lại thị uy $\to$ Giậm chân gầm khè khẳng định ranh giới $\to$ Quay đầu bỏ đi khi đối phương nằm im phục tùng**. Việc prompt cũ bỏ quên khủng long ở pha 3 để quay lá cây là sai lệch kịch bản nghiêm trọng.
      3. **Vật thể người xâm lấn (Ghost Hands):** Khi camera POV ngã ngửa vào bụi cây mà không khóa chủ thể khủng long, AI sẽ tự động vẽ thêm 2 bàn tay game FPS thò ra lơ lửng đỡ đất.
    - **Quy tắc giải pháp chuẩn hóa cho 3 trụ cột: Action, Material, Setting:**
      1. **TRỤ CỘT 1 — ACTION (Vũ đạo & Tập tính động vật):**
         - **Góc lao an toàn:** Thú khổng lồ BẮT BUỘC lao theo góc chéo 3/4 (`diagonal trajectory`), TUYỆT ĐỐI CẤM lao thẳng chính diện đâm vào ống kính (gây méo tỷ lệ sọ và chảy xệ chi tiết mặt).
         - **Quán tính $p = m \cdot v$ & Phanh cày đất:** Không phanh đứng khựng kiểu xe hơi ABS; chân trước găm móng guốc cày nát 2 rãnh bùn đỏ sâu 40cm, thân sau 9 tấn trượt văng nghiêng 30 độ do mất ma sát rồi mới khựng lại ở cự ly 5–6 mét.
         - **Pha kết thúc thị uy (The Domination Stomp):** Thú khổng lồ KHÔNG biến mất khỏi khung hình. Nó đứng sừng sững chiếm trọn khung hình ở góc nhìn thấp (low-angle), giậm chân nện đất, cào bùn thị uy, rồi quay thân mình 9 tấn lừng lững bước đi trong tiếng rung chuyển mặt đất. Cắt sang cảnh sau vlogger thở phào nhẹ nhõm.
      2. **TRỤ CỘT 2 — MATERIAL (Chất liệu sinh học & Triệt tiêu CGI):**
         - **Da vảy sần sùi không đều:** BẮT BUỘC dùng cụm: `rugged pebbled reptilian hide covered in irregular osteoderms and thick keratinized tubercles`. CẤM các từ gợi ý bề mặt nhẵn bóng.
         - **Nếp gấp da & Bùn đất nứt nẻ:** `thick folded skin around neck dewlap, flanks and joints caked in dried, cracked Cretaceous red mud`.
         - **Sừng & Sẹo chiến tích:** `scarred bony neck frill with deep healed predator bite marks; splintered jagged horn tip revealing weathered fibrous keratin core`.
         - **Nhiệt động học & Dịch tiết sinh học:** `nostrils flare violently blasting twin plumes of dense, hot breath vapor billowing in humid morning air; faint natural frothy saliva at corners of razor-sharp keratin beak`.
         - **Mắt sinh vật sống:** `feral amber eyes with narrow vertical slit pupils reflecting natural forest light; living breathing animal, NO smooth plastic CGI texture, NO cartoonish 3D render`.
      3. **TRỤ CỘT 3 — SETTING (Bối cảnh & Tương tác vật lý môi trường):**
         - **Nền đất & Độ biến dạng:** Nền đất bùn đỏ phù sa Hell Creek (`churned iron-rich wet red clay`); móng guốc giậm với áp lực 15 kPa làm lún sâu, xé toác đất bùn và hất tung các tảng đất lẫn rễ cây dương xỉ.
         - **Thực vật gãy vỡ:** Sừng quét làm gãy toác thân cây cọ mục (`shatters rotting palm stump, showering wood splinters and damp peat across foreground`).
         - **Ánh sáng tự nhiên phá vỡ CGI:** Ánh nắng ban mai xuyên qua tán lá cọ *Sabalites* và cây lá kim cổ đại (`dappled jungle canopy sunlight with broken shadows rippling across scaly hide`), tạo khối sáng tối gồ ghề tự nhiên, xóa sạch ánh sáng phẳng của mô hình 3D.

74. **MANDATORY CREATURE & CHARACTER TURNAROUND SHEET VIA `/fk-character-design` (Khóa cứng Sheet 16:9 Đa Góc & 5 Lớp DNA Anchor — Bài học Lỗi Lật Sừng & Khói Thở Con Bò Đực Hell Creek, User review 13/10/2026, Rule 58):**
    - **Hiện tượng & Root Cause:**
      1. **Lỗi Lật Sừng (Horn Flip) & Dị tật biến mất:** Khi sinh ảnh reference bằng ảnh đơn 1 góc chụp (Single Photograph, ví dụ chỉ thấy sườn trái), AI không có góc nhìn đối diện. Khi camera chuyển sang sườn phải hoặc góc quay khác trong video, AI bị "nhầm gương" (mirror glitch), tự lật sừng gãy sang bên phải, hoặc biến sừng gãy thành sừng dài lành lặn nguyên vẹn.
      2. **Lỗi Khói Thở như đầu máy xe lửa (Train Smoke Glitch):** Do thiếu Anti-Smoke Lock và mô tả nhiệt động học quá đà, AI sinh ra luồng khói trắng xóa đặc quánh phụt ra từ mũi như ống khói tàu hỏa, che khuất toàn bộ mặt khủng long và trông cực kỳ giả trân.
    - **Quy tắc giải pháp bắt buộc (Rule 58):**
      1. **Bắt buộc kích hoạt `/fk-character-design` cho mọi Reference thực thể sống:** CẢ Claude VÀ Antigravity BẮT BUỘC kích hoạt `/fk-character-design` để thiết kế Character/Creature Turnaround Sheet 16:9 trước khi sinh bất kỳ ảnh reference nào. Tuyệt đối cấm ảnh đơn 1 góc cho nhân vật và sinh vật chủ chốt.
      2. **Chuẩn Creature Turnaround Sheet 16:9 (3 panel trong 1 ảnh 16:9):**
         - Panel 1 (3/4 Trái): Thể hiện rõ toàn bộ cấu trúc thân thể và đặc điểm bên trái (sừng trái gãy cụt còn 30cm lộ lõi keratin thô ráp phong hóa).
         - Panel 2 (3/4 Phải): Thể hiện rõ góc đối diện và đặc điểm bất đối xứng (sừng phải dài 1m nhọn hoắt nguyên vẹn).
         - Panel 3 (Cận cảnh sọ chính diện): Khóa giác đấu đầu sọ, sừng, hàm mỏ, mắt hổ phách, nếp nhăn diềm sọ, vảy biểu bì lát gạch (Rule 57).
      3. **Khóa 5 Tầng DNA Anchor:** Proportion Lock, Bone & Face Structure Layer, Skin/Epidermis vi mô Rule 57, Permanent Prop/Geometry, và Forbidden Drift & Anti-Smoke Lock (`NO train-engine white smoke plumes; breath vapor is subtle faint mist only`).
75. **KHÓA CHẤT LIỆU XÁC ĐỘNG VẬT PHÂN HỦY SINH HỌC, BẢO TOÀN ĐƯỜNG MÒN NGUYÊN SINH (TRIỆT TIÊU VỆT LỐP XE / CƯA XẺ HIỆN ĐẠI), XÓA GOD RAYS, VÀ KHÓA NHẬN DIỆN KHUÔN MẶT CHỐNG PROMPT ĐÈ (Biological Carcass Decomposition Material, Prehistoric Trail Integrity & Anti-Tire-Track Lock, Anti-God-Rays, Face Lock against Text-Prompt Drift — Bài học Act 1 Hell Creek 66 Ma, User Review 13/10/2026, Rule 59):**
    - **Hiện tượng & Root Cause:**
      1. **Xác động vật giả trân như mô hình bảo tàng (Fake Plastic/Plaster Skeleton):** Prompt cũ tả "khung xương trắng xám cong trên bãi sỏi", thiếu độ chìm lún và thịt thối, khiến AI vẽ ra bộ xương thạch cao trắng bóc, khô cong, nằm hờ hững trên sỏi như mô hình đồ chơi nhựa trong bảo tàng.
      2. **Rừng Kỷ Phấn Trắng bị dính vệt lốp xe tải 4x4 & gỗ xẻ hiện đại (Truck Tire Ruts & Lumber Glitch):** Do dùng từ khóa `mud trail` hay `trail`, AI diffusion model tự liên tưởng tới đường mòn lâm nghiệp nông thôn và vẽ ra 2 vệt bánh xe tải song song sâu hoắm trong bùn kèm thân cây bị cưa xẻ đặt gọn gàng 2 bên đường ở thời điểm 66 triệu năm trước.
      3. **Tia nắng thần thoại CGI (God Rays Glitch):** Prompt dùng các từ ngữ ánh sáng hoa mỹ khiến khung hình bị phủ các luồng sáng volumetric beams như đồ họa Avatar/Disney, lòng sông thu hẹp như mương cảnh quan hồ cá.
      4. **Lỗi khuôn mặt nhân vật chính bị Text Prompt ghi đè (Face Drift by Text Override):** Mặc dù ảnh ref `ref_nora_face.jpg` là cô gái tóc vàng mật ong (*honey-blonde*), da trắng mịn không tàn nhang, nhưng trong DB và prompt lại ghi `auburn hair escaping bun with dirt smudges` hoặc `copper-red hair, freckles`. AI diffusion model ưu tiên chữ hơn ảnh ref, biến nhân vật thành cô gái tóc đỏ cam tàn nhang búi tóc củ tỏi lệch 100% so với ref!
    - **Quy tắc giải pháp bắt buộc (Rule 59):**
      1. **Chất liệu Xác Phân Hủy Sinh Học Thực Tế (`fk-add-material` & `cretaceous_vlog`):**
         - Trọng lượng & Lún bùn: Xác thú lớn (Edmontosaurus 12m, 7 tấn) BẮT BUỘC chìm lún sâu 20–30cm vào bùn phù sa ướt và sét đỏ mép nước (`heavily sunken 30cm into wet river silt and alluvial mud`), tạo gờ đùn bùn đất quanh thân xác.
         - Thịt cơ & Gân rữa bám xương: Khung sườn ố vàng vì nắng gió; cơ thịt đỏ thẫm đông kết và gân nhờn bám chặt vào xương sườn và sụn (`dark coagulated reddish-brown muscle tissue and glistening tendons adhering to costal bone and cartilage`); nội tạng phân hủy trong khoang ngực; da vảy sừng rách tả tơi mép mỡ quăn dính bùn và máu đông khô. CẤM TUYỆT ĐỐI xương thạch cao trắng khô như tượng sáp hoặc mô hình bảo tàng (`NOT a museum diorama, NOT wax figure, NOT dry clean bones`).
         - Vết cắn thú săn mồi: Vết cắn của T. rex hình chữ U sâu hoắm trên xương bả vai/hông phải thấy rõ tủy xương bị dập nát (`scalloped bite gouges with crushed marrow`).
         - Côn trùng: Bầy ruồi nhặng và muỗi cổ đại bu quanh kẽ thịt thối.
      2. **Triệt Tiêu 100% Vệt Lốp Xe & Đường Lâm Nghiệp:**
         - CẤM dùng từ `trail`, `dirt road`, `country road` đơn độc.
         - BẮT BUỘC dùng: `wide, chaotic animal-trampled game corridor cutting into primeval rainforest; deeply churned red clay mud filled with massive rounded ceratopsian foot depressions, crushed fern fronds, mud wallows; STRICTLY NO vehicle tracks, STRICTLY NO parallel tire ruts, STRICTLY NO modern dirt road, STRICTLY NO sawn lumber logs`.
      3. **Ánh Sáng Tự Nhiên & Triệt Tiêu Tia Nắng Thần Thoại:**
         - CẤM `god rays`, `volumetric beams`, `magical sunbeams`.
         - BẮT BUỘC dùng: `flat natural morning overcast daylight, humid river mist in distance, natural dappled canopy sunlight`. Mai rùa nằm nửa chìm trong bùn sỏi ướt sát mép nước (`half-embedded in wet river silt and pebbles with thin specular reflections`).
      4. **Khóa Khuôn Mặt Tuyệt Đối Chống Text Prompt Ghi Đè:**
         - Text prompt trong scene BẮT BUỘC phải đồng bộ 100% với ảnh ref `ref_face`.
         - BẮT BUỘC dùng: `matching Nora face reference: young 23-year-old woman with honey-blonde hair in high wavy ponytail with wispy curtain bangs framing forehead, fair smooth creamy skin (strictly NO red hair, NO auburn hair, NO messy bun, NO freckles), hazel-green eyes`.

76. **[ĐÃ THAY 19/10/2026 bởi Rule 60 mới + Rule 64: KHÔNG tả ngũ quan bằng chữ, chỉ một câu khóa trỏ vào chip ảnh ref — user: "không tả ngũ quan". Nội dung dưới chỉ để tham khảo lịch sử.]** **KHÓA CHẶT 1:1 KHUÔN MẶT BẰNG MỆNH LỆNH SẮT ĐÁ VÀ ĐẶC TẢ HÌNH HỌC NGŨ QUAN — DÙNG ĐÚNG ẢNH REF HIỆN CÓ (Ironclad 1:1 Face Lock via Mandatory Reference Command & Facial Geometry DNA — Bài học Khắc Phục Lệch Mặt Cảnh 01, 04, 15 Hell Creek 66 Ma, User Review 13/10/2026, Rule 60):**
    - **Hiện tượng & Nguyên nhân gốc rễ (Root Cause):**
      1. **Gương mặt bị trôi dạt và biến dạng nặng nề dù đã có ảnh Reference:** Khi sinh Start Frame hoặc hình ảnh có nhân vật chính (Nora), mặc dù đã gắn ảnh Reference `<Vlogger>` trong DB, kết quả khuôn mặt vẫn bị lệch nghiêm trọng:
         - Cảnh 04 mặt vuông dài già nua như phụ nữ 35 tuổi, xương hàm bạnh nam tính, má hóp.
         - Cảnh 15 môi mỏng dính, miệng há to hốc hác méo mó.
         - Cảnh 01 mắt lồi, gò má lệch.
      2. **Vì sao có ảnh Ref mà AI vẫn vẽ sai mặt?**
         - *Prompt thiếu mệnh lệnh ép 1:1:* Prompt cũ chỉ ghi mô tả chung chung (`matching Nora face reference: young 23-year-old woman with honey-blonde hair...`). Diffusion model hiểu đây chỉ là "cảm hứng/gợi ý phong cách", không phải lệnh bắt buộc.
         - *Thiếu đặc tả hình học khung xương & ngũ quan (Facial Geometry DNA):* Không mô tả dáng mặt (trái xoan mềm mại / heart-shaped vs mặt vuông), cằm thon, má bầu bĩnh, và đặc biệt là **bờ môi dày mọng hình trái tim (`distinctively full plump pillowy lips with defined Cupid's bow`)** - đặc trưng nhận diện lớn nhất của ảnh gốc. Khi text không có từ khóa này, AI tự do vẽ môi mỏng và cằm vuông.
         - *Thiếu khối phủ định cấm biến dạng (Negative Identity Constraints):* Không cấm mặt vuông (`strictly NO square jaw`), cấm mặt già (`NO aged appearance`), cấm môi mỏng (`NO thin lips`).
    - **Quy tắc giải pháp bắt buộc (Rule 60):**
      1. **DÙNG ĐÚNG ẢNH REFERENCE HIỆN CÓ — KHÔNG CẦN CẮT MỚI:** Đã có ảnh Reference của nhân vật trong dự án thì tái sử dụng nguyên vẹn, không cần cắt hay tạo ảnh mới làm phân mảnh media.
      2. **Khóa Mệnh Lệnh Sắt Đá 1:1 (Mandatory 1:1 Reference Command):** BẮT BUỘC mở đầu khối nhận diện bằng câu lệnh khẳng định trực tiếp:
         `"Nora's face is an exact 1:1 identical match to the attached Nora reference image. Perfectly preserve her exact facial likeness from the reference photo without changes."`
      3. **Đặc Tả Hình Học Khung Xương & Ngũ Quan (Facial Geometry DNA Lock):** Bắt buộc nêu rõ các thông số hình học:
         `"youthful 22-year-old soft feminine heart-shaped face, delicate rounded chin, soft cheeks, petite straight nose, distinctively FULL PLUMP PILLOWY LIPS with defined Cupid's bow, large hazel-green almond eyes, and honey-blonde hair in high wavy ponytail with wispy curtain bangs softly framing forehead and temples."`
      4. **Khối Phủ Định Triệt Tiêu Trôi Dạt (Anti-Drift Negative Constraints):** Bắt buộc chèn câu cấm tuyệt đối:
         `"STRICTLY FORBIDDEN: strictly NO square jaw, NO long rectangular face, NO thin lips, NO hollow cheeks, NO aged appearance (must look 22-23), NO facial distortion, NO face drift."`

77. **KHÓA ÁNH SÁNG TỰ NHIÊN, TRIỆT TIÊU GLAMOUR BIAS & CẤM CÁNH TAY SELFIE VƯƠN DÀI (Natural Lighting, Anti-Glamour Raw Realism & Zero Stretched Selfie Arm Lock — Bài học ảnh Start Frame Hell Creek 66 Ma, User Review 13/10/2026, Rule 61):**
    - *(Phạm vi: mục 3 "Cấm cánh tay selfie vươn dài" chỉ áp cho vlog; mục 1, 2, 4 (ánh sáng tự nhiên, chống glamour, chất liệu sinh học) áp cho phim.)*
    - **Hiện tượng & Nguyên nhân gốc rễ (Root Cause):**
      1. **Ảnh bị hiệu ứng "Cosplay / 3D Render Unreal Engine / Filter Instagram":** Mặc dù prompt mô tả chi tiết, ảnh gen ra nhìn như người mẫu chụp ảnh cosplay studio với đèn hắt sáng và da búp bê sáp, không ra chất sinh tồn Kỷ Phấn Trắng trần trụi.
      2. **Xung đột Glamour Bias (Làm đẹp giả trân):** Các từ ngữ như `fair smooth creamy skin`, `beauty glow`, `luminous eyes` kích hoạt bộ lọc chân dung thương mại của Imagen 3, làm mờ lỗ chân lông, khử sạch bụi bẩn và nếp nhăn tự nhiên.
      3. **Cánh tay selfie vươn dài biến dạng (Stretched Arm Glitch):** Prompt mô tả `her right arm extends holding camera at chest level` khiến AI vẽ cánh tay dài ngoằng, to tướng thò vào mép ảnh như cây gậy selfie tàng hình, gây mất tự nhiên và méo giải phẫu.
      4. **Khủng long bị biến thành mô hình nhựa / tượng sáp 3D:** Thiếu ánh sáng ban mai tán xạ thực tế và vảy sần phong hóa cặn bùn, khiến Triceratops nhìn như tượng đặt trong công viên.
    - **Quy tắc giải pháp bắt buộc (Rule 61):**
      1. **Ánh Sáng Tự Nhiên 100% (Natural Ambient & Dappled Daylight):**
         - Đầm lầy/sông nước: `flat natural morning overcast daylight, cool humid river mist diffusing soft ambient daylight, realistic moisture reflections on wet gravel and silt; strictly NO volumetric god rays, strictly NO artificial rim lights`.
         - Rừng rậm: `natural dappled canopy sunlight filtering through giant tree ferns and conifers, organic deep micro-shadows breaking flat CGI render`.
      2. **Triệt Tiêu Bẫy Làm Đẹp (Zero Beauty Filter / Raw Survival Texture):**
         - CẤM: `fair smooth creamy skin`, `beauty glow`, `flawless porcelain skin`.
         - BẮT BUỘC: `authentic unretouched outdoor skin texture, fine pores, natural perspiration sheen, light mud and dirt smudges on cheek and jawline, natural wind-blown stray hair strands, zero makeup, zero cosmetics, raw 35mm wildlife forensic documentary realism`.
      3. **Cấm Cánh Tay Selfie Vươn Dài (Zero Stretched Arm Lock):**
         - Điểm nhìn người xem chính là thấu kính camera. CẤM vẽ cánh tay vươn ra cầm máy.
         - BẮT BUỘC: `The camera viewpoint and gripping arm are completely outside the visible frame and never seen; both hands are empty and natural (or resting on ground/prop)`.
         - Ưu tiên góc First-Person POV (cam sau) và Góc máy cố định tựa đá/gốc cây (In-frame experience) theo Rule 42 & Rule 51.
      4. **Chất Liệu Sinh Học Sống Động Cho Khủng Long:**
         - `tactile organic epidermis, irregular polygonal basement scales, prominent conical keratin tubercles, weathered hairline fissures on horns, matte dried alluvial clay caked into crevices, natural breath vapor misting from nostrils`.

78. **BẮT BUỘC TRUYỀN ID ẢNH REF VLOGGER (`source_media_id`) KHI SINH START FRAME CÓ NHÂN VẬT — CHỐNG LỆCH MẶT & MẤT NEO REF TRÊN GOOGLE FLOW (Mandatory Vlogger Ref ID / source_media_id Injection in Scene Start Frames — Bài học Khắc Phục Lệch Mặt Cảnh Có Nora Hell Creek 66 Ma, User Review 14/10/2026, Rule 63):**
    - **Hiện tượng & Nguyên nhân gốc rễ (Root Cause):**
      1. **Ảnh Start Frame trên Google Flow không có ảnh ref đính kèm & mặt bị lệch hoàn toàn:** Khi kiểm tra trên giao diện `flow.google.com`, các ảnh Start Frame được sinh ra hoàn toàn KHÔNG CÓ chip ảnh reference của Nora đính kèm, dẫn đến việc Imagen 3 vẽ khuôn mặt ngẫu nhiên từ mô tả chữ (Cảnh 2, 3 cằm/môi khác nhau; Cảnh 6 bị biến thành tóc nâu và người khác).
      2. **Vì sao Google Flow không gắn ảnh ref?**
         - Khi submit batch `GENERATE_IMAGE`, hệ thống chỉ gửi request dạng Text-to-Image thuần túy mà **KHÔNG truyền `source_media_id` (chứa UUID của ảnh ref nhân vật)**.
         - Khi không có `source_media_id`, Google Flow không có `BASE_IMAGE` làm neo gốc. Backend Imagen 3 của Flow bỏ qua danh sách tham chiếu phụ và tạo ảnh hoàn toàn từ con số 0 (Text-to-Image).
      3. **Hậu quả xung đột trong Video R2V:** Nếu Start Frame Frame 0 mang khuôn mặt lạ đưa vào `GENERATE_VIDEO_REFS`, video model sẽ bị xung đột giữa Frame 0 (mặt người lạ) và Ingredients tham chiếu (mặt Nora thật), gây méo mó, biến dạng hoặc trôi dạt nhận diện.
    - **Quy tắc giải pháp bắt buộc (Rule 63):**
      1. **BẮT BUỘC truyền `source_media_id` cho cảnh có nhân vật:** Mọi request sinh ảnh Start Frame cho cảnh có Vlogger / nhân vật chính BẮT BUỘC phải truyền `source_media_id` = UUID của ảnh ref nhân vật chính (`1fb0ffe9-c60c-434b-a962-93a23fd17571` cho Nora) qua `EDIT_IMAGE` hoặc `GENERATE_IMAGE` có `source_media_id`.
      2. **Hiệu ứng trên Google Flow:** Khi có `source_media_id`, FlowKit đưa ID vào `base_media_id` / `target_asset`. Trên `flow.google.com`, Flow gán trực tiếp thẻ ảnh ref của nhân vật vào khung làm việc làm ảnh nguồn, khóa cứng 1:1 nhận diện ngũ quan, không bao giờ bị vẽ mặt ngẫu nhiên.
      3. **Cảnh không người (Phong cảnh, Khủng long, B-roll):** Tiếp tục dùng `GENERATE_IMAGE` thuần túy không cần `source_media_id`.

79. **QUY TẮC BẤT DI BẤT DỊCH: CẢNH LIÊN TỤC CẮT LAST FRAME LÀM START FRAME — CẤM SINH ẢNH MỚI; CHỈ CHUYỂN CẢNH MỚI SINH START FRAME (Continuous Scene Chains vs. Scene Transitions Start Frame Protocol — User Lock 15/10/2026, Rule 65):**
    - **Hiện tượng & Nguyên nhân gốc rễ (Root Cause):**
      1. **Vỡ giải phẫu & nhảy bối cảnh giữa các cảnh liên tiếp:** Khi một hành động kéo dài qua nhiều clip (ví dụ chuỗi rượt đuổi, trượt chân ngã, va chạm quái thú như `A1-12a` ➔ `A1-12b` ➔ `A1-12c`), nếu cố tình sinh ảnh Start Frame tĩnh mới bằng Text-to-Image AI (`GENERATE_IMAGE`) cho từng mắt xích:
         - AI model không thể tái tạo 100% tư thế cơ thể, hướng ngã, vị trí bùn đất và cành cây ở mili-giây giao nhau giữa 2 clip.
         - Kết quả: Nhân vật bị "dịch chuyển tức thời" (teleport), vỡ khớp xương, đổi dáng áo hoặc khung cảnh bị nhảy giật cục làm hỏng hoàn toàn trải nghiệm điện ảnh chân thực.
      2. **Giải pháp chuẩn xác từ thực địa:** Cắt frame cuối cùng của video trước đó làm frame mở đầu cho video kế tiếp loại bỏ hoàn toàn 100% sai lệch giải phẫu và ánh sáng.
    - **Quy tắc giải pháp bất di bất dịch (Rule 65):**
      1. **Phân loại 2 nhóm cảnh rõ ràng:**
         - **Cảnh liên tục (Chain Action / Motion sequence / Cùng góc nhìn tiếp nối):** CẤM TUYỆT ĐỐI sinh Start Frame bằng `GENERATE_IMAGE`. BẮT BUỘC dùng `PREV_LAST_FRAME`: trích xuất khung hình cuối cùng (`ffmpeg -sseof -0.08 -i prev.mp4 -frames:v 1`), xóa sạch logo và SynthID qua `tools/remove_watermark_from_image.py`, upload lên Flowkit lấy `media_id` UUID gán làm Start Frame (`horizontal_image_media_id`). Clip sau tự động đợi clip trước xong mới trích xuất và sinh video.
         - **Chuyển cảnh (Scene Transitions / Đổi góc POV <-> Selfie / Cutaway / Đổi bối cảnh / Đổi thời gian):** Giữ nguyên quy trình chuẩn — tạo ảnh Frame 0 độc lập bằng `GENERATE_IMAGE` (có `source_media_id` cho cảnh có người theo Rule 63), tẩy logo, mở Review Board (`review_images.html`) dừng lại chờ User duyệt.
      2. **Mở rộng 16/10/2026 — không chỉ chuỗi `a/b/c`:** Mọi clip nối tiếp trực tiếp clip trước đều là cảnh liên tục, dù ID không có hậu tố. Phép thử 4 yếu tố: **cùng địa điểm + cùng khoảnh khắc + cùng vị trí/góc máy + cùng cỡ cảnh**, không có cú cắt ➔ `PREV_LAST_FRAME`. Đổi một yếu tố bất kỳ ➔ chuyển cảnh ➔ `GENERATE_IMAGE`. Bộ code `common.py` của Hell Creek v2 chỉ đánh `PREV_LAST_FRAME` khi clip mang cờ `sf="P"` (chuỗi `a/b/c`). Kiểm lại Act 2 theo phép thử 4 yếu tố (16/10/2026) thì mọi cặp clip khác đều đổi góc máy hoặc cỡ cảnh, nên phân loại cũ vẫn đúng. Nhưng phải xét từng cặp, không suy ra từ hậu tố ID.
      3. **Ghi lý do & thứ tự:** `/fk-script-to-prompts` phân loại từng clip và ghi lý do vào `start_frame.note`. Clip liên tục chỉ sinh sau khi clip trước xong và được duyệt; clip trước bị regen thì cắt lại Last Frame và regen clip sau. Start Frame cắt từ video đã duyệt không cần qua Review Board ảnh, nhưng vẫn phải tẩy watermark (Rule 28).

80. **CẮT CẢNH THEO STORYBOARD (CRISP HARD CUTS) & KHÓA CHỐNG PHÂN THÂN NHÂN VẬT (ANTI-CLONING / CHARACTER CONTAMINATION LOCK) TRONG PURE R2V (User Lock 23/10/2026, Rule 74 — Bài học Lỗi 2 Nora Xuất Hiện Cùng Lúc Ở Giây Số 9 SC-01 Pirates of the Golden Tree):**
    - **Hiện tượng & Nguyên nhân gốc rễ (Root Cause):**
      1. **Không cắt cảnh theo Storyboard (Missing Hard Cuts):**
         - Tấm Storyboard 2×2 thể hiện 4 panel là 4 cú máy riêng biệt (Panel 1: EWS tàu bên ngoài ➔ Panel 2: MS Captain Nora một mình ở mũi tàu ➔ Panel 3 & 4: MS/MCU Castor một mình ở boong giữa).
         - Nhưng prompt video cũ lại mô tả: `[EWS] Slow tracking dolly shot on 35mm Cooke S4 prime lens...` và không có chỉ thị cắt cảnh dứt khoát. Model video Veo 3 / Omni Flash hiểu lầm đây là một cú máy tracking liên tục duy nhất, cố gắng di chuyển camera nối liền từ Nora sang Castor mà không cắt chuyển cảnh theo Storyboard.
      2. **Xuất hiện 2 nhân vật giống hệt nhau (Duplicate Clone Glitch — 2 Nora ở giây 9):**
         - Ở phân đoạn 7-10s, khi Castor sải bước trên boong giữa, do danh sách tham chiếu (`character_names`) đính kèm cả Nora, và prompt không khai báo Nora đã ra khỏi khung hình (`off-screen`), không gian tiềm ẩn (latent space) của mô hình bị "nhiễm nhân vật" (*latent character contamination*).
         - Kết quả: Khi Castor bước tới (khung 21-24 trên contact sheet 24 frames), mô hình giữ Nora bản gốc ở hậu cảnh cạnh đèn bão, đồng thời sinh thêm **một bản sao thứ 2 của Nora** xuất hiện lù lù ở tiền cảnh bên trái che khuất Castor!
    - **Quy tắc giải pháp bắt buộc (Rule 74):**
      1. **BẮT BUỘC chỉ định Hard Cut dứt khoát theo từng Panel Storyboard**:
         - Trong `camera.description`: Chỉ định rõ chuỗi đa shot: `Multi-shot sequence with crisp hard cuts: Shot 1 (0-3s, EWS) -> Hard Cut at 3.0s -> Shot 2 (3-7s, MS) -> Hard Cut at 7.0s -> Shot 3 (7-10s, MS to MCU)`.
         - Trong `timeline_action`: Mọi điểm chuyển panel giữa các góc nhìn khác nhau BẮT BUỘC mở đầu bằng câu lệnh cắt cứng: `At second 3.0, a crisp hard cut matching Panel 2 (Top-Right) of {{media:...}}...` và `At second 7.0, a crisp hard cut matching Panel 3 and Panel 4 (Bottom-Left to Bottom-Right) of {{media:...}}...`.
      2. **Khóa cô lập nhân vật & Off-Screen Lock**:
         - Khi một cú máy chỉ quay nhân vật B, BẮT BUỘC ghi rõ: `Strictly [Character B] alone in this shot; [Character A] is completely off-screen and never appears`.
      3. **Khối phủ định chống phân thân (Anti-Cloning Negative Constraints)**:
         - BẮT BUỘC thêm vào `negative_constraints`: `strictly NO duplicate characters, strictly NO multiple [Name], only one [Name] in shot X, strictly [Other] alone in shot Y, [Name] never appears in the [shot Y], no ghost figures, no cloning; crisp hard cuts at second X.0 and second Y.0, no camera blending, no crossfades.`
      4. **Chống trộn trục 180° giữa 2 Panel (`Anti-180°-Axis-Fusion`) & Khóa không gian Trong/Ngoài lan can (`Inside-Deck Spatial Lock` — Bài học SC-01 v2 Pirates of the Golden Tree, 23/10/2026)**:
         - **Hiện tượng & Root Cause:** Trong `SC-01_storyboard_clean.jpg`, Panel 3 (Bottom-Left) có sàn tàu/thùng gỗ/cầu thang ở **bên TRÁI** và biển ở **bên PHẢI** (Castor đứng bên trái vịn lan can nhìn sang phải). Trong khi đó Panel 4 (Bottom-Right) đảo góc máy 180° nên biển ở **bên TRÁI** và sàn tàu/cầu thang ở **bên PHẢI**. Khi prompt của Shot 3 (`7-10s`) viết gộp `matching Panel 3 and Panel 4 (Bottom-Left to Bottom-Right)`, Omni Flash R2V đã trộn vị trí đứng bên TRÁI lan can của Castor ở Panel 3 vào nền cảnh biển bên TRÁI / sàn tàu bên PHẢI của Panel 4 ➔ biến thành Castor đứng dưới mặt nước biển phía ngoài mạn tàu vịn vào lan can nhìn vào trong tàu!
         - **Quy tắc giải pháp bắt buộc:**
           - **Mỗi Shot chỉ neo bố cục không gian theo MỘT Panel duy nhất:** CẤM viết gộp `matching Panel 3 and Panel 4` trong cùng một cú máy không cắt cảnh. Shot 3 (`7-10s` hoặc `6-8s`) chỉ neo cứng bố cục không gian theo `Panel 3 (Bottom-Left)` từ đầu đến cuối Shot 3 (không đảo trục 180° sang nền cảnh ngược chiều của Panel 4).
           - **Khóa `SPATIAL LOCK (INSIDE vs. OUTSIDE)`:** Mọi cảnh trên tàu thuyền, lan can, gờ đá BẮT BUỘC ghi rõ bên nào (`LEFT` hay `RIGHT`) là sàn gỗ bên trong tàu, bên nào là mặt nước biển bên ngoài, kèm câu khóa: `SPATIAL LOCK: All characters stand firmly INSIDE the vessel on the solid wooden deck planks, NEVER standing on the exterior ocean/water side of the timber railing; no 180-degree axis fusion between panels.`

**Nội dung**
17. → chuyển sang [`vlog-archive.md`](vlog-archive.md) ([ĐÃ THAY] vlogger mặc đồ hiện đại).
18. → chuyển sang [`vlog-archive.md`](vlog-archive.md) (cảnh FPV mở đầu là ngoại lệ của luật "mọi shot quay bằng điện thoại").



