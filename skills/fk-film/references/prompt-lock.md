# 🔒 PROMPT LOCK — khung `video_prompt` (phim) + checklist trước khi lưu



Đọc ở **Bước 5** của `SKILL.md`, chạy lại ở Bước 9 khi review. Thay mục 10b cũ.



> User yêu cầu: các bài học ở `production-lessons.md` (mục 11 cũ) phải được **khóa vào lúc viết prompt**, không chỉ nằm trong danh sách bài học. Mọi `video_prompt` (POST hoặc PATCH) phải dựng theo khung dưới đây và **qua đủ checklist** trước khi lưu. Clip nào không qua checklist thì sửa prompt trước, không gửi sinh.



> **Phim vs vlog (2026-10-19):** khung A dưới đây là khung của **phim ngôi thứ ba**. Khung 9 khối cũ của vlog (selfie / POV / máy dựng) và các dòng checklist chỉ áp cho vlog đã chuyển nguyên văn sang [`vlog-archive.md`](vlog-archive.md) §4; dòng checklist cũ giữ số, chỉ còn con trỏ kèm luật tương đương cho phim.



**A. Khung `video_prompt` của phim — Structured JSON (Rule 55; mẫu thật: `output/embers/prompts_v7_act*.json`):**



Thứ tự khóa (không bỏ khóa bắt buộc):



1. **`clip_id`, `scene_name`, `duration`, `aspect_ratio`, `refs`** — `refs` là TÊN entity (≤7), gồm mặt + Body của mọi nhân vật trong khung, sinh vật, bối cảnh (dòng 15).

2. **`camera`** — `viewpoint`: `"third-person cinematic camera; the camera itself is never seen"`; `shot_size`; `description` (ống kính, máy cố định hay di chuyển, bố cục). Máy được phép dolly / track / handheld theo `/fk-camera-guide`; ghi rõ máy có di chuyển hay không để không tự mâu thuẫn (Bài 86).

3. **`style`** — chất phim (`35mm film, cinematic documentary realism, natural film grain …`), không CGI.

4. **`setting`** — địa điểm trỏ ref bối cảnh `{{ref:<Bối cảnh>}}`, mặt đất/thời tiết, **giờ & ánh sáng khớp clip trước và sau**, những gì đứng yên ở hậu cảnh suốt clip.

5. **`characters[]`** — mỗi người/thú: `visual_lock` (câu khóa 1:1 trỏ chip ref, Rule 64; không tả lại mặt/trang phục), `state` (trạng thái ở giây 0: bẩn, ướt, bỏng…).

6. **`timeline_action`** — mốc theo `duration` (4s `0-2s / 2-4s`; 6s `0-2s / 2-4s / 4-6s`; 8s `0-3s / 3-6s / 6-8s`; 10s `0-3s / 3-7s / 7-10s`); mỗi mốc một beat, hành động có **nguyên nhân vật lý**, người nói bắt đầu từ giây 0 (Rule 54). Mọi người/vật xuất hiện phải có mặt từ giây 0 (Bài 48).

7. **`speech`** — `speaker`, `voices` (voice id từng người), `delivery`, `dialogue[]` (mốc, người nói, câu nguyên văn từ `script.md`, số từ theo Rule 49). Clip im lặng ghi rõ không có thoại.

8. **`post_vo`** — lời qua bộ đàm / điện thoại / lời dẫn thêm khi dựng (Bài 99); không viết vào thoại trên hình.

9. **`dramatic_craft`** — `beat`, `value_turn`, `subtext`, `prop_and_detail` (Rule 56).

10. **`audio`** — thoại + foley + ambient; giọng nói nổi trên nền (Bài 81, 101).

11. **`negative_constraints`** — câu cấm viết thành câu hoàn chỉnh (không chữ, không logo, anti-CGI, không khói thở, cơ thể không nhập nhau, đếm đạo cụ…).

12. **`props_lock`** (khi có đạo cụ dễ lỗi: dây, dao, bình…) — Bài 94, 96.



**B. Checklist — đọc lại từng `video_prompt` trước khi lưu (mỗi dòng phải trả lời "có"):**



| # | Kiểm tra | Bài học |

|---|---|---|

| 1 | → chuyển sang [`vlog-archive.md`](vlog-archive.md) §4 (góc máy vlog: selfie/POV/máy dựng). **Phim:** một góc máy ngôi thứ ba mỗi clip (`third-person cinematic camera; the camera itself is never seen`); không trùng cỡ cảnh + góc máy với clip liền trước | Rule 42 (4), prompt EMBERS |

| 2 | → chuyển sang [`vlog-archive.md`](vlog-archive.md) §4 (hành động 2 tay khi vlogger đang cầm máy). Phim không có ràng buộc này | — |

| 3 | Mọi người/vật/sinh vật trong sub-clip đều đã có mặt trong khối "already in place" với vị trí + khoảng cách ở giây 0 | 48, Scene 2/14/39/73 |

| 4 | Không giao hành động cho người không có trong khung; chuyển đồ vật tả từng bước tay (đưa → đỡ bằng tay nào → tay kia buông) | 48, Scene 14/15 |

| 5 | Không nhắc tên món đồ trên người (mũ, găng, khăn) trong sub-clip nếu không muốn nhân vật thao tác với nó; mũ đã khóa "luôn để xuống" | 52, Scene 21/62 |

| 6 | Đạo cụ chức năng (găng, áo) tả **động tác mặc/xỏ trước**, buộc dây sau, khoe ngang ngực | 45, 46 |

| 7 | → chuyển sang [`vlog-archive.md`](vlog-archive.md) §4 (bản vlog: selfie qua vai, người bản địa nói tiếng không hiểu được). **Phim:** nhân vật hiện mặt mà không có thoại thì khóa miệng; mỗi người nói ở nhịp riêng, voice id riêng trong `speech.voices`, không nói chồng; cảnh rình/áp sát/ẩn nấp dùng Sonic Isolation | 49 (ý chung), Rule 49 (4) |

| 8 | Ngã/trượt/va chạm có **nguyên nhân vật lý** và **máy chịu hậu quả** (rung, chúi, văng); không ngã khi không gấp *(phần "máy chịu hậu quả" chỉ áp cho vlog cầm tay)* | 51, Scene 1/45 |

| 9 | Vật nặng (tấm da cửa, đá) chỉ chuyển động khi có tay tác động, không giao cho "gió" | 50, Scene 9 |

| 10 | Hai sinh vật cùng lông/màu không chạm nhau (vòi–voi con…); câu `"each animal is a separate body; they never overlap or merge"` | Scene 36 |

| 11 | Sinh vật tuyệt chủng tả đặc điểm loài + loại trừ loài giống (`"not an African elephant"`, `"never horses or bison"`) | 53, Scene 38/48 |

| 12 | `Setting:` có năm, địa điểm, tuyết/băng, ánh sáng khớp clip liền trước/sau; nội thất có câu khóa bếp trũng | 53, Scene 15/27/28/48 |

| 13 | Clip nối hành động mở bằng đúng trạng thái cuối clip trước (vị trí, tư thế, ánh sáng, mối nguy) và **không đi trước** clip sau về thời gian | 44, 51, Scene 43/70 |

| 14 | Muốn nhân vật nhìn thấy thứ ở phía sau → thứ đó đã nằm trong khung từ giây 0 (không đổi phông khi quay đầu) | 42, Scene 70 |

| 15 | Tối đa 7 ref/clip (giới hạn Omni Flash; luật 3 ref đã bỏ — user 2026-10-14): `<V>` + `<V> Body` (đã mặc outfit của tập) + ref của mọi sinh vật/bối cảnh có trong khung; ref sinh vật đang đe dọa phải có trong cảnh đó; không có entity `<V> Outfit` | 47, 51, 60, Rule 46 |

| 16 | → chuyển sang [`vlog-archive.md`](vlog-archive.md) §4 (từ chỉ thiết bị quay của vlog). **Phim:** không gọi tên vật/thú/lửa/thiết bị mà mình không muốn thấy trong khung, kể cả trong thoại và audio; không dùng dòng `Negative:` dạng văn xuôi (ràng buộc nằm trong `negative_constraints`) | 33 (ý chung), 73, 77, 99 |

| 17 | → chuyển sang [`vlog-archive.md`](vlog-archive.md) §4 (câu mẫu tay trống của vlog bị lặp) | — |

| 18 | **Nhịp gửi request:** **mọi request tới Flow** (sinh ảnh/video, upscale, upload ảnh ref, tạo project, poll trạng thái, đọc media) cách nhau **ngẫu nhiên 45–60s** — server đã khóa sẵn (`FLOW_GENERATION_MIN/MAX_INTERVAL_S`); script tự gửi thì dùng `random.uniform(45, 60)`, dừng ngay khi gặp `UNUSUAL_ACTIVITY` hoặc `QUOTA`. Video: mỗi lần 1 video, chờ video trước xong rồi ~30s sau mới gửi tiếp (user chốt 2026-10-07) | 54 |

| 19 | **Khóa tóc cụ thể theo ảnh ref:** vị trí cột tóc (`tied at the crown of her head, not low at the nape`), mái (`wispy curtain bangs parted in the middle that cover the edges of her forehead and frame both cheeks`), `never slicked back`; có gió thì ghi `wind only makes the ponytail swing, the bangs stay over her forehead` — không viết tóc bị gió `whip` | 55 |

| 20 | **Cảnh POV có tay vlogger** (cầm, chạm, xỏ, đỡ đồ) → `character_names` phải có `<V>` + `<V> Body` (đã mặc outfit) để bàn tay, cổ tay áo đúng của nhân vật chính (user chốt 04/10/2026, cập nhật theo Rule 46) | Scene 45/53, 60 |

| 21 | **Đạo cụ cầm tay của nhân vật phụ** (giáo, gậy, cốc) → tạo ref riêng `<Tên> <Đạo cụ>` (vd `Torak Spear`) bằng **EDIT từ ảnh ref gốc** của nhân vật (giữ mặt + trang phục), sheet 16:9 3 góc, đạo cụ cầm sẵn trong tay; xóa logo → upload lại → dùng thay ref nhân vật trong cảnh đó | Scene 29 |

| 22 | Hành động chia đúng 3 pha (chuẩn bị → **một** đòn theo một hướng → thu thế): dễ thì khớp `0-3s / 3-6s / 6-8s` trong 1 clip 8s, dễ lỗi thì mỗi pha 1 clip 4s (dòng 31); không xoay 360°, không thú lao thẳng vào ống kính, không tả xuyên thịt — chỉ tả quỹ đạo và hậu quả | `cinematic-toolkit.md` §1 |

| 23 | Cảm xúc của vlogger viết bằng triệu chứng cơ thể (thở, mắt, hàm, vai), không bằng tính từ (`terrified`, `sad`); clip có vòng A → chất xúc tác → B | `cinematic-toolkit.md` §2 |

| 24 | → chuyển sang [`vlog-archive.md`](vlog-archive.md) §4 (Rule 50: săn bắn quay POV, cấm selfie). **Phim:** săn bắn/giao chiến/chạy trốn theo 3 pha của `/fk-action-choreography`; cắt thoại khi rình (Sonic Isolation) | `cinematic-toolkit.md` §1 |

| 25 | → chuyển sang [`vlog-archive.md`](vlog-archive.md) §4 (Rule 50: xoay vòng POV → selfie → máy dựng). **Phim:** đổi cỡ cảnh liên tục, không 2 cảnh liền nhau cùng góc máy + cỡ cảnh | Rule 42 (4) |

| 26 | **KHÓA TRANG PHỤC THUẦN ẢNH THAM CHIẾU (Bài học 63):** Tuyệt đối KHÔNG mô tả lại trang phục bằng lời trong prompt (không tự thêm shearling collar, tunic, fur-lined...); chỉ trỏ thẳng ref: `wears the exact historical outfit shown in the <V> Body reference sheet (NO shearling collar, NO extra fur, NO hood, NO outfit variations)` | Bài học 63, Scene 21 |

| 27 | → chuyển sang [`vlog-archive.md`](vlog-archive.md) §4 (BODY LOCK tôn dáng vlogger — trái memory 2026-10-14 "Body lock = normal figure"). **Phim:** dáng người lấy từ ảnh Body, không tả vòng 1 | Bài 63 (quy tắc 3) |

| 28 | → chuyển sang [`vlog-archive.md`](vlog-archive.md) §4 (material `phone_vlog`). **Phim:** material `realistic` / `documentary_footage` hoặc material riêng của phim | — |

| 29 | **KHÓA BỐI CẢNH REF 16:9 DÙNG CHUNG & REVIEW START FRAME (Bài học 69):** Mỗi cụm cảnh cùng không gian (bếp lửa C27-28, bàn thuộc da C30-31, cửa hang C33-36, ổ ngủ C51-54) BẮT BUỘC sinh 1 ảnh ref bối cảnh 16:9 sạch watermark, đưa user duyệt trước, gán vào `reference_media_ids` dùng chung; prompt trỏ trực tiếp: `SETTING: Matches the exact layout shown in the [Setting Reference] image`; khóa đạo cụ đơn nhất (`single tool, never duplicate`), cấm người ngoài rìa đứng thừa | Bài học 69, Scene 27/28/30 |

| 30 | **MỘT TAY — MỘT ĐẠO CỤ — SUỐT CLIP (Bài học 70):** đạo cụ chính nằm ở **một tay từ giây 0 tới giây cuối**, không đặt xuống, không chuyền tay; nhân vật đối diện máy thì ghi kèm vị trí khung (`her right hand, on the left side of the frame`); tối đa 2 trạng thái tay/clip; khoe kết quả bằng tay đang cầm sẵn; `negative_constraints` đếm đạo cụ (`exactly one flake, always in her right hand, never vanishes, never duplicates, never appears on the slab`) | Bài học 70, Scene 29 |

| 31 | **ĐỘ DÀI CLIP THEO ĐỘ KHÓ & PHÂN ĐỊNH CHUỖI 4s VS CHUYỂN CẢNH (Bài học 71):** (1) Cảnh dễ lỗi liền mạch (chạy nhanh, tương tác thú, ngã/rơi máy, sinh vật lớn băng qua khung, VFX, vật vỡ/gãy) đã tách thành **chuỗi 4s** `a/b/c` — mỗi mắt xích 1 hành động, **CẤM TUYỆT ĐỐI CHUYỂN CẢNH / ĐỔI GÓC MÁY trong chuỗi** (giữ nguyên 100% refs + `Setting` + ánh sáng + `camera.viewpoint` + `camera.shot_size`), mở bằng tư thế cuối mắt xích trước; (2) Cảnh phức tạp CÓ CHUYỂN CẢNH / ĐỔI GÓC: **CẤM gom vào chuỗi `a/b/c`**, bắt buộc tách Scene ID riêng biệt (4s/6s) nối bằng kỹ thuật dựng phim; (3) Cảnh dễ không chuyển cảnh mới để 8s/10s; sub-clip và số từ khớp `duration`; `duration` đã PATCH đúng cột `Dur` | Bài học 71, Rule 49 (0) |

| 32 | **TAY POV LẤY TỪ `<V> BODY` (Bài học 95, thay Bài 72):** cảnh POV có thao tác tay đính `<V> Body`, KHÔNG đính `<V> Hand`; câu khóa `her hands and bare forearms are exactly the hands and arms of the woman in {{ref:<V> Body}}` + độ dài tay áo đúng như Body (tay ngắn → `no sleeve, cuff or fabric is anywhere on her forearms`); `negative_constraints` cấm tay nam, cẳng tay lông, tay áo dài/sờn, đồng hồ, móng sơn, thừa ngón | Bài học 95, A1-06 Hell Creek v2 |

| 33 | **ĐẶC TẢ CHẤT LIỆU SINH HỌC KHỦNG LONG & TRIỆT TIÊU CGI (Bài học 73):** Cảnh có khủng long / bò sát khổng lồ BẮT BUỘC tả đủ 3 trụ cột: (1) **Action:** lao chéo 3/4 (cấm đâm chính diện), trượt quán tính $p=m \cdot v$ cày bùn 40cm (cấm phanh ABS), giậm chân thị uy rồi quay đi (cấm cắn xé quái dị); (2) **Material:** da vảy sần sùi osteoderms, nếp gấp da cổ đẫm bùn nứt nẻ, sừng gãy lộ sợi keratin, sẹo rách diềm sọ, lỗ mũi khô ráo sạch sẽ (strictly NO breath vapor, strictly NO smoke or steam), dãi mỏ tự nhiên, mắt hổ phách phản chiếu ánh sáng tự nhiên, cấm tuyệt đối da nhẵn sáp/CGI; (3) **Setting:** móng nén bùn lún 15 kPa hất tung bùn đỏ, sừng quét toác cành gỗ mục, ánh sáng ban mai tán xạ qua vòm lá rậm rạp (*dappled canopy sunlight*) phá vỡ ánh sáng phẳng 3D render | Bài học 73, Scene 14-16 Hell Creek |

| 34 | **KHÓA CHUẨN TURNAROUND SHEET CHO REF SINH VẬT & NHÂN VẬT (Rule 58 & `/fk-character-design`):** Mọi ảnh reference cho sinh vật chủ chốt (Triceratops Bull, T-Rex...) và nhân vật BẮT BUỘC dùng Turnaround Sheet 16:9 chuẩn đa góc (3 panel sinh vật: 3/4 trái, 3/4 phải, cận cảnh đầu sọ; 4 góc nhân vật) khóa 5 tầng DNA anchors (tỷ lệ, xương sọ, biểu bì Rule 57, đạo cụ cố định, cấm lật sừng & cấm khói thở trắng đặc xe lửa). CẤM dùng ảnh đơn 1 góc (Single Photograph) cho sinh vật chủ chốt | Rule 58, Bài học 74, `/fk-character-design` |

| 35 | **XÁC PHÂN HỦY LÚN BÙN 30CM & TRIỆT TIÊU VỆT LỐP XE / GOD RAYS (Rule 59):** (1) Xác thú lớn chìm lún 30cm vào bùn phù sa ướt, sườn ố vàng dính thịt rữa & gân bám sụn, vết cắn T. rex dập tủy, ruồi nhặng bu quanh; CẤM xương trắng khô thạch cao như bảo tàng. (2) Đường mòn động vật giẫm đạp hỗn loạn; CẤM 100% vệt lốp xe ô tô 4x4, thân gỗ xẻ, đường lâm nghiệp. (3) Ánh sáng ban mai tán xạ tự nhiên, ẩm ướt; CẤM god rays volumetric ảo diệu | Rule 59, Bài học 75 |

| 36 | **KHÓA CHẶT 1:1 KHUÔN MẶT BẰNG MỆNH LỆNH SẮT ĐÁ & ĐẶC TẢ NGŨ QUAN (Rule 60):** Dùng đúng ảnh Ref hiện có (không cần cắt mới). Mọi cảnh có mặt Vlogger BẮT BUỘC có khối `FACE & IDENTITY LOCK (CRITICAL)` gồm: (1) Lệnh ép 1:1: `[Name]'s face is an exact 1:1 identical match to the attached [Name] reference image. Perfectly preserve her exact facial likeness from the reference photo without changes`; (2) Đặc tả ngũ quan: mặt trái xoan mềm, cằm thon, má bầu bĩnh, mũi nhỏ thẳng, đặc biệt là bờ môi dày mọng hình trái tim (`FULL PLUMP PILLOWY LIPS with Cupid's bow`); (3) Khối cấm đối kháng: `strictly NO square jaw, NO thin lips, NO aged appearance (must look 22-23)`; (4) Khóa tay tự do trống không cấm ghost phone *(ý (4) "tay tự do trống, cấm ghost phone" chỉ áp cho vlog; phim nhắc chip ref theo dòng 40)* | Rule 60, Bài học 76 |

| 37 | **KHÓA TUYỆT ĐỐI CHỐNG KHÓI THỞ, CHẤT LIỆU DA THÚ PACHYDERM KHÔNG BÓNG NHỰA, VÀ DEEP FOCUS f/8 (Rule 62):** CẤM TUYỆT ĐỐI hơi thở khói trắng/sương mù (zero smoke, zero breath vapor, zero steam); da thú sần sùi thô ráp không phản quang (non-reflective pachyderm hide) như tê giác/voi; cấm tia nắng streaming god rays và đèn viền studio rim light; cảnh trung và selfie bắt buộc deep focus f/8 chống xóa phông bokeh | Rule 62 |



| 38 | **BẮT BUỘC TRUYỀN ID ẢNH REF VLOGGER (`source_media_id`) KHI SINH START FRAME CÓ NHÂN VẬT (Rule 63 & Bài học 78):** Khi sinh ảnh Start Frame cho các cảnh có Vlogger / nhân vật chính, request BẮT BUỘC phải truyền `source_media_id` = UUID của ảnh ref nhân vật (`uploads/nora_main_clean.jpg`) để Google Flow gán trực tiếp thẻ ảnh ref vào canvas (`BASE_IMAGE`), khóa cứng nhận diện 1:1, ngăn Imagen 3 vẽ khuôn mặt ngẫu nhiên từ text | Rule 63, Bài học 78 |

| 39 | **SHEET REF SINH VẬT CÓ DẤU BẤT ĐỐI XỨNG (Bài học 93):** Panel 1/2 tả bằng "đầu chỉ về mép TRÁI/PHẢI của ảnh, sườn nào hướng máy"; panel 3 là cận đầu 3/4 nhìn từ phía có dấu (sừng gãy, vệt má, sẹo), không chính diện thuần; bạo chúa ghi môi kín kiểu kỳ đà, `zero teeth are visible`; review soi chữ/số tự chèn và đạo cụ cố định đúng bên | Bài học 93 |

| 40 | **NHẮC ẢNH REF NGAY TRONG PROMPT (Rule 64):** mọi ảnh ref đính kèm đều được nhắc tại câu khóa bằng `{{ref:<entity>}}` (gửi đi thành `{{media:<uuid>\|<file>}}` = chip ảnh của Flow); mặt/makeup/trang phục KHÔNG tả lại bằng chữ, chỉ "exactly as in {{ref:X}}"; Start Frame có vlogger đính đúng 3 ref [mặt, Body, bối cảnh]; `lint_prompt.py` đạt 0 lỗi mention | Rule 64 |

| 41 | **ĐẠO CỤ CHÍNH GIỐNG HỆT NHAU GIỮA CÁC CLIP CHUYỂN CẢNH (Bài học 94):** đạo cụ xuất hiện ở ≥2 clip (bình, dao, gùi) dùng **một câu tả chuẩn** (hằng số trong `common.py`) nguyên văn ở mọi clip, kể cả clip nhặt / chế tác; không tính từ trái với ref (`bleached`, `white`, `shiny`); clip có đạo cụ đính ref chứa nó (đồ trên sheet Body → đính `<V> Body`) ở cả `image_refs` lẫn `character_names`; clip chuyển trạng thái đạo cụ miễn câu sổ liên tục, tự ghi `At second 0 … by second N …`; đồ đeo ghi độ dài dây + vị trí so với thắt lưng | Bài học 94, A1-06/A1-07 Hell Creek v2 |

| 42 | **MỘT SỢI DÂY LIỀN KHI HAI NGƯỜI CÙNG CẦM (Bài học 96):** clip có dây/dây cương/xích/khăn mà hai nhân vật cùng cầm hoặc giằng co có `props_lock` "exactly ONE … single continuous unbroken …", ghi rõ ai cầm đoạn nào, lúc giật thì "slides out … in one piece" + tay người kia trống, và câu cấm đứt/tách đôi/nhân đôi | Bài học 96, EMBERS RA-02 |

| 43 | **CẢNH SUÝT CHẠM (Bài học 97):** beat "gần chạm rồi rút" ghi khoảng cách (cm) + "a clear gap of air … never touching" + câu cấm chạm/vuốt/vỗ; chia vươn → khựng → rút; máy cố định ghi rõ không di chuyển/không zoom, chỉ chuyển nét; beat 3 nhịp dùng ≥ 6s | Bài học 97, EMBERS RA-03 |

| 44 | **ĐƯỜNG ĐI QUA VẬT CẢN (Bài học 98):** nhân vật di chuyển trong khung có rào/cổng/xe/cột → ghi rõ đi dọc/vòng/qua cửa nào so với vật cản + câu cấm đi xuyên; điểm đến phải có trong Start Frame | Bài học 98, EMBERS RA-05 |

| 45 | **CLIP IM LẶNG KHÔNG CÓ RADIO TRÊN HÌNH (Bài học 99):** câu nói qua bộ đàm/điện thoại để ở `post_vo` (thêm khi dựng), không viết vào prompt; clip im lặng không cho bộ đàm xuất hiện, nhân vật chỉ khựng lại/nghiêng đầu nghe; bắt buộc có radio thì ghi trước là sẽ tắt tiếng gốc khi dựng; Whisper phải PASS (không EXTRA SPEECH) | Bài học 99, EMBERS EM-01 |

| 47 | **CẢNH TRANH CÃI NÓI TO, GẮT, CỘC (Bài học 101):** thoại đối đầu / ra lệnh dưới áp lực ghi rõ "loud and sharp, voice raised over the roar, every word hard, clipped and forceful, each short sentence punched out like an order" ở cả `speech.delivery` lẫn nhịp timeline; bỏ "low / quiet / voice drops / flat"; không trích lại câu thoại ở nhịp khác | Bài học 101, EMBERS CH-03 |

| 48 | **THOẠI TRONG VÙNG NGUY HIỂM PHẢI GẤP (Bài học 102):** clip có thoại khi nguy hiểm đang diễn ra (cháy, bão, rượt đuổi, cứu người, sơ tán) không được có `natural pace` / `runs on from 0s through Ns`; `speech.delivery` ghi "shouted fast and hoarse over the roar, urgent, clipped, no pauses, never calm, never slow"; tách câu theo nhịp và nói xong sớm (vd. hết thoại trước giây 4 của clip 6s); `characters.state` có trạng thái căng bằng thân thể (mồ hôi, hàm nghiến, mắt đảo, không đứng yên); timeline luôn có chuyển động + một biến cố áp lực; câu cấm "never calm or relaxed: no slow talking, no soft voice, no pauses, no standing still, no gentle smile". Nhịp chậm chỉ cho beat lặng có chủ đích | Bài học 102, EMBERS LH-02 |

| 49 | **CẢNH CHÁY RỪNG PHẢI CHÁY ĐỀU, MÁY GẦN (Bài học 103):** `setting` tả cả rừng hai bên cháy đều (thân cây, ngọn, cỏ mép đường, tường lửa liền phía sau, không còn cây xanh), lửa là nguồn sáng chính; `camera` cầm tay cách nhân vật 3–4 m, khung từ gối trở lên, không `WS` / ống kính dài; câu cấm "fire never limited to one or two trees" và "no burning object flies sideways through the air"; vật rơi gần người phải ghi khoảng cách bằng mét kèm "never falls on or touches her" | Bài học 103, EMBERS RR-13 |

| 46 | **THOẠI KHÔNG NÓI CHUYỆN TRẢ TIỀN / MUA BÁN (Bài học 100):** nhân vật trẻ nói với người khác về trả tiền/mua/bán ("buy her back… forty dollars", "Please, I can pay!") bị Flow chặn im lặng (ghost op) dù đã thêm ngữ cảnh con vật; bỏ hẳn ý tiền khỏi thoại và subtext, đưa vào `post_vo`/phụ đề nếu cần; ghost 2 lần cùng clip → soát thoại trước, không gửi lại nguyên văn | Bài học 100, EMBERS EL-03 |



**C. Sau khi sinh — rà lỗi theo cùng checklist** khi review (`/fk-review-video` + user): trích ~16 frame/clip, đối chiếu từng dòng B; lỗi mới chưa có trong bảng → ghi bài học mới vào `production-lessons.md` **và** thêm 1 dòng vào bảng B.

**D. Đọc lại toàn bộ sau mỗi lần sửa (Bài học 86)** — mục này được `/fk-review-prompt` chạy thành một bước có báo cáo: (1) sau khi sửa bất kỳ câu nào, đọc lại **cả** prompt, không chỉ câu vừa sửa; (2) gom các câu theo thuộc tính (tốc độ, hướng đi, máy đứng yên hay di chuyển, ánh sáng, bối cảnh, số lượng đạo cụ) và kiểm hai câu có nói ngược nhau không; (3) chạy hết checklist B; (4) gửi kèm prompt một báo cáo tự đánh giá (dòng nào áp, Đạt / Không đạt, mâu thuẫn đã sửa) trước khi hỏi user duyệt sinh. Linter chỉ bắt `SPEED_CONTRADICTION` và `CAMERA_CONTRADICTION`; mọi mâu thuẫn khác phải tự đọc mà tìm.
