# Bài học sản xuất thực tế — góp ý của user

Đọc ở **Bước 5** của `SKILL.md` trước khi viết `video_prompt`, và khi review clip lỗi. Đây là mục 11 cũ của skill, giữ nguyên số thứ tự bài học để các tham chiếu "Bài học N" cũ vẫn đúng.

**Thứ tự ưu tiên:** CLAUDE.md > bài học có số lớn hơn / ngày mới hơn > bài học cũ. Các bài học đã bị thay được đánh dấu `[ĐÃ THAY]` ngay đầu dòng; giữ lại làm bằng chứng, không làm theo. Các chỗ ghi "mục N" trong file này trỏ tới số mục của skill cũ — tra bảng "Bản đồ mục cũ" trong `SKILL.md`.

**Thêm bài học mới:** mỗi lỗi gen lặp lại ghi thành MỘT bài học đánh số tiếp theo (root-cause, câu prompt sửa, bằng chứng: clip nào, bản nào) **và** thêm 1 dòng vào checklist B của `prompt-lock.md`.

Rút ra từ dự án `output/atlantis-9600bc/` (2026-09-27). Khi mâu thuẫn với phần khác của skill, **mục này thắng**.

**Quy trình**
1. **Xác nhận trước mỗi bước sinh** (ảnh ref, video, clip thử, sinh lại): nói rõ sinh gì, bao nhiêu, rồi chờ user đồng ý. Xong mỗi bước thì **dừng và đưa kết quả cho user xem** (kèm link file, bảng ghép ảnh hoặc khung hình). Không tự sinh lại khi lỗi.
2. **Chạy thử clip khó nhất trước, 1 clip**, rồi **1 clip bình thường làm mốc**, trước khi gửi cả loạt. Lỗi thường có hệ thống; sửa ở vài clip đầu rẻ hơn nhiều so với sửa cả loạt.
3. **Ảnh ref phải được user xem trước khi dùng.** Ghép bảng ảnh và đưa đường dẫn file để user tự xem.

**Ảnh ref (R2V)**
4. Mỗi clip **tối đa 3 ref**; worker chỉ lấy entity `character` và `visual_asset`. Công trình hay bối cảnh cần giữ nhất quán (thành phố, tường thành, đền) phải khai báo là `visual_asset`.
5. **Clip nào có thành phố hay bối cảnh lớn thì phải kèm ảnh ref của chính bối cảnh đó** (ví dụ ảnh toàn cảnh thành phố). Chỉ tả bằng chữ thì model tự vẽ một thành phố khác.
6. **Mọi ảnh ref đều sinh ngang 16:9** (góp ý của user, 2026-10-01), kể cả nhân vật (sheet các góc đặt cạnh nhau). FlowKit đã sinh 16:9 cho mọi loại entity. Entity `location` **không** được worker đưa vào R2V, nên mọi bối cảnh cần giữ nhất quán phải khai báo `visual_asset`. Worker lấy `visual_asset` trước `character`, nên tổng `character_names` của mỗi clip phải ≤3 và luôn có vlogger, nếu không vlogger bị loại khỏi ref.
7. Ảnh ref không được có người, tay, đồ vật hay trang phục hiện đại lọt vào (găng tay, ủng, người mặc áo thun), không có kiến trúc lệch thời kỳ (mái vòm, tháp nhọn, lâu đài trung cổ), và không có dải màu trơn quanh ảnh.

**Viết `video_prompt`**
8. **Ràng buộc là câu khẳng định**, không dùng dòng `Negative:` (xem mục 9).
9. **Điện thoại là máy quay, nhưng KHÔNG viết chữ `phone` trong prompt (bài 33):** chỉ tả góc nhìn (`The lens sits at the end of her outstretched arm…` / `The view is her own eyes`) và tay trống (`her free hand is empty`). Không viết `she holds the phone up`, `the phone is the camera` hay `no phone`; nhắc tới đồ vật, kể cả câu phủ định, đều làm model vẽ nó ra. Với POV, cho tay nhân vật bận việc khác (bám mép thuyền, cầm đồ vật).
10. **Shot selfie không dùng vật lướt qua ống kính** (xà gỗ, ngựa…): ở góc selfie, vật phải chen vào khoảng khoảng 60 cm giữa gậy selfie và mặt nên trông như "bay" đến, và model hay xóa luôn nhân vật (user duyệt: không thực tế). Selfie chuyển cảnh bằng **swing/whip pan** (nhân vật xoay gậy lia máy nhanh sang cảnh mới, nhòe chuyển động nửa giây cuối; clip sau mở giữa cú lia rồi dừng lại trên nhân vật ở chỗ mới) hoặc **jump cut**. Foreground wipe chỉ dùng cho shot POV.
11. **Chống hình kiểu 3D ở cảnh thần thoại hoặc thảm họa** (model chỉ biết những cảnh này qua phim và game):
    - mở prompt bằng khối "footage thật": `raw unedited amateur video, looks like real footage posted online, not a movie`, rung tay, auto-exposure, nhiễu nén, giọt nước trên ống kính, ánh sáng bệt;
    - tả bằng vật liệu có thật (ví dụ "tường ốp tấm đồng đỏ cũ, xỉn màu" thay vì "orichalcum phát sáng"); tên thần thoại chỉ để trong lời thoại;
    - giảm độ hoành tráng: cảnh ở xa, bị mưa hoặc sương che, khung lệch;
    - nhưng **vẫn phải kèm ảnh ref bối cảnh** (quy tắc 5), nếu không sẽ mất nhận diện (ví dụ Atlantis thành làng chài Anh).

**Kỹ thuật FlowKit**
12. `POST /api/scenes` không nhận `duration`; phải `PATCH {"duration": 8}` (thiếu thì âm thầm ra clip 10s).
13. Mỗi clip chỉ có 1 giọng, lấy từ entity **đầu tiên theo thứ tự DB** có `voice_description`. **Chỉ nhân vật chính khai báo voice**; khai báo cho nhân vật phụ thì giọng họ sẽ đè lên thoại của nhân vật chính.
14. Sinh lại một scene R2V đã COMPLETED: PATCH `horizontal_video_status: PENDING` rồi gửi `GENERATE_VIDEO_REFS` (không có `REGENERATE_VIDEO_REFS`).
15. Ảnh do Flow sinh luôn có logo ✦ ở góc dưới phải (tâm khoảng `(W-98, H-97)`). Xóa bằng `tools/remove_watermark_from_image.py` (đã sửa ngưỡng ngày 2026-09-27), rồi **mở ảnh ra kiểm tra**. Ảnh không phải do Flow sinh (ví dụ bảng ảnh ghép của user) thì tool có thể đoán sai vị trí.
16. Google chặn sinh tự động (`UNUSUAL_ACTIVITY`) → làm theo Bước 4.9. Đổi tài khoản Google thì phải tạo project mới (project và media thuộc tài khoản đã tạo ra chúng).

19. **Không có gì tự hiện ra giữa clip:** thứ được "reveal" (thành phố, tường thành, tượng…) phải **có mặt từ khung hình đầu**, chỉ lộ ra nhờ nhân vật dịch sang bên hoặc máy xoay tới, và đứng yên một chỗ. Viết rõ vị trí của nó ở giây 0 (ví dụ `to the right of her head, far across the water, the city is already visible on the horizon`) và thêm câu `nothing pops into view`. Nếu tả nó ở mốc thời gian sau, model sẽ cho nó xuất hiện ở mốc đó (lỗi S31 Atlantis).

20. **Ghi rõ hướng và tốc độ của mọi thứ đang di chuyển** (thuyền, xe, ngựa, người chạy): đi về đâu, nhanh cỡ nào, và hệ quả trong khung hình (ví dụ `the boat moves only at slow rowing speed and away from the city, so the city stays the same size or slowly shrinks and never gets closer`). Tả cả chuyển động vật lý thật (thuyền nhấp nhô và lắc theo sóng, không lướt đi; người chèo ngồi quay mặt về phía đuôi thuyền). Bỏ trống thì model chọn kiểu kịch tính và sai vật lý (lỗi S31 Atlantis: thuyền chèo lao về phía thành phố như thuyền máy).

21. **Bảng vật lý phải được user duyệt trước khi viết Clip JSON** (mục Định dạng output, bước 5b): mỗi clip ghi máy đặt ở đâu và nhìn về đâu, có gì trong khung ở giây 0, mọi vật di chuyển (hướng, tốc độ, hệ quả trong khung), chuyển động vật lý thật, và ai hoặc cái gì rời khung bằng cách nào. Nội dung bảng được viết thành câu trong `video_prompt` (quy tắc 19, 20). Đây là chỗ bắt lỗi vật lý rẻ nhất: sửa trên giấy, không tốn credit.

22. **[ĐÃ THAY bởi bài học 60 / Rule 46 — trang phục mặc lên `<Vlogger> Body`, không tách entity Outfit]** **Trang phục khóa bằng panel toàn thân trong ảnh sheet nhân vật** (góp ý của user, 2026-10-01; thay bài học S31 Atlantis): ảnh ref vlogger là một sheet 16:9 có mặt rõ, góc 3/4 và toàn thân mặc trang phục (xem mục 2). Chỉ tách entity `<Vlogger> Outfit` riêng khi trang phục vẫn bị đổi giữa các clip.

23. **Tuyệt đối CẤM từ khóa `selfie-stick` và mô tả cầm điện thoại (bài học S11, S17, S20 Atlantis):**
    - Từ khóa `selfie-stick` hay `smartphone selfie` làm AI vẽ thêm 1 chiếc gậy selfie trong tay, hoặc vẽ 1 chiếc điện thoại/màn hình điện thoại bay lơ lửng trước ống kính (hiện tượng quay màn hình điện thoại).
    - **Chuẩn thay thế:** Dùng `Handheld front-camera vlog footage, ultra-wide 0.5x lens, slight wide-angle barrel distortion`. Tả cánh tay: `Mia holds the camera at arm's length with her right arm extended toward the bottom-right corner of the frame.`
    - **Khóa câu khẳng định bắt buộc:** `The lens sits at the end of Mia's outstretched right arm, looking back at her; her right hand is beyond the frame edge and her other hand is empty, so the frame contains only Mia and the scene behind her.` (không nhắc tới thiết bị, xem bài 33)

24. **100% First-Person POV không vẽ thiết bị hay thao tác sai vật lý (bài học S12, S16, S34 Atlantis):**
    - Khi quay POV (nhúng tay thử nước, bước qua cầu, nhìn xuống mặt nước): Người xem nhìn thẳng qua mắt vlogger. Vlogger đứng hoàn toàn sau camera, hai tay giữ máy ở tầm ngực.
    - Chỉ có **1 bàn tay không** (trống trơn, không cầm gì) vươn vào mép dưới khung hình để tương tác (chạm nước, nhặt đá, chỉ tay).
    - CẤM mô tả "cầm gậy rồi thả ra rồi cầm điện thoại" hoặc vẽ bàn tay cầm điện thoại khác; cấm để điện thoại nổi lơ lửng trên mặt nước. Khóa câu: `The view is Mia's own eyes; Mia's face and body never appear, and only her bare empty hand enters the lower frame.` (không nhắc tới thiết bị, xem bài 33)

25. **Vật lý cầm máy khi chạy tháo chạy và nhảy — Running & Action Leap Physics (bài học S27, S30 Atlantis):**
    - **Khi chạy trốn (S27):** Vlogger vlogging cuộc tháo chạy của mình thì **PHẢI LUÔN NẮM CHẶT CAMERA QUAY MẶT MÌNH**. Cấm để AI cho nhân vật buông tay, vứt điện thoại hay chạy xa khỏi camera. Tả: `Mia clutches the camera firmly in her right hand at arm's length pointed continuously at her face; she NEVER drops, releases, or lets go of the camera. The camera shakes violently with her sprint.`
    - **Khi nhảy (S30):** Vlogger một tay nắm chặt máy nhảy xuống thuyền; camera trải qua một cú giật nảy giật dọc cực kỳ thực tế khi tiếp đất trên sàn thuyền gỗ. Cấm buông máy/gậy trước khi nhảy.

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

33. **ĐIỆN THOẠI HIỆN RA LẶP ĐI LẶP LẠI — KHÔNG ĐƯỢC NHẮC TỚI THIẾT BỊ TRONG PROMPT (bài học H1/H2 Ice Age 16,000 BC, sau 4 lượt gen hỏng liên tiếp):**
    - **Root-cause:** model video **không hiểu phủ định**. Câu "no phone, no phone screen, no device…" thực chất là gọi tên đồ vật nhiều lần, nên model càng vẽ ra nó. Bản lock `PHONE INVISIBILITY RULE (CRITICAL)` từng ghi ở đây là **SAI**: prompt H1 khi đó chứa `phone` 8 lần, `screen` 4, `device` 3, `smartphone` 3, và kết quả vẫn có điện thoại. Ngoài ra, mọi `style.*` cũ đều mở đầu bằng "Handheld smartphone footage… natural smartphone perspective".
    - **Luật bắt buộc:** trong `style`, `lock`, `general`, `physics`, `bg`, `shot`, `frame0` TUYỆT ĐỐI KHÔNG có các từ `phone`, `smartphone`, `device`, `screen` (theo nghĩa thiết bị), `gadget`, `selfie stick`, `tripod` (đồ vật). Chỉ tả **góc nhìn** và **tay đang trống**:
      - `selfie`/`run`: *"The lens sits at the end of Nora's outstretched right arm, about 60 cm in front of her face, looking back at her; her right shoulder and upper arm reach toward the bottom-right corner and leave the frame there, so her right hand is never in view."* + *"Her left hand is empty, and nothing is held up in front of her or near her face."*
      - `pov`: *"The view is Nora's own eyes, and only the world in front of her fills the frame; the view simply moves as she moves."* (câu khẳng định; không viết "no face, no body, no person" vì phủ định vẫn gọi tên đối tượng, xem bài 37)
      - `tripod`: *"Static locked-off footage from a fixed viewpoint resting on a ledge… nothing that holds or supports the view is visible."*
      - thay "natural smartphone perspective" bằng **"natural wide-angle handheld perspective"**.
    - **Kiểm tra trước khi gen:** sau khi render, grep prompt; phải ra 0 kết quả cho `\b(phone|smartphone|device|gadget|selfie stick)\b`.
    - **Tay giữ camera không được đánh khi chạy (lỗi H1, góc selfie bị gãy ở giây 2.5):** nếu prompt vừa nói "right arm extended toward the lens" vừa nói "arms swinging hard" thì model buộc phải chọn một. Nó cho cả 2 tay đánh, và góc quay biến thành camera người ngoài quay theo. Với shot `run`, luôn viết **"her left arm pumps hard while her right arm stays extended toward the lens for the entire clip"**, không bao giờ viết "arms swing" (số nhiều).
    - **Tốc độ chạy trong tuyết sâu:** để cảnh trông KHẨN CẤP và NHANH, tả `legs pumping as fast as physically possible, her left arm pumping hard, the view bouncing violently with each stride, face locked in wide-eyed terror`. Tránh "short heavy strides" vì model sẽ gen thành đi bộ.
    - **Kẻ đuổi không được bắt kịp:** ghi rõ khoảng cách cố định, ví dụ *"The mammoth stays about twenty metres behind Nora for the whole clip; she never draws level with Nora."* Nếu chỉ ghi "never catches up" thì khung cuối mammoth vẫn chạy ngang hàng.
    - **Biểu cảm:** Với cảnh trốn chạy, phải khóa cứng `wide-eyed terror, mouth open in a gasp or scream, no smile whatsoever, brow furrowed hard` — nếu chỉ tả "terrified" mà không chi tiết, model hay gen mặt cười kiểu excited.

34. **[LEGACY & BÀI HỌC GỐC] BỘ REF CHO VLOGGER: Mặt + Body (bài học H1/H2 Ice Age 16,000 BC; từ 05/10/2026 cập nhật theo Rule 46 & Bài học 60):**
    - **Root-cause #1 (lỗi nặng nhất): `character_names` phải là TÊN entity, không phải UUID.** Server so khớp theo `name`/`slug` (`_char_matches` trong `agent/sdk/services/operations.py`). Nếu lưu UUID thì không khớp entity nào → server rơi vào nhánh dự phòng và chỉ gửi **1 ref duy nhất** (entity đầu tiên của project). Mọi lock outfit/body đều vô hiệu. Luôn PATCH `character_names: ["Nora", "Nora Body", ...]` (bài học 60) và đọc lại scene để kiểm tra.
    - **Root-cause #2: giới hạn ref r2v.** `_R2V_MAX_REFS` đã nâng từ 3 lên 7 (giới hạn Omni Flash). Thứ tự ưu tiên: `visual_asset` trước, rồi `character`; entity `location` KHÔNG được gửi làm ref (chỉ mô tả bằng prompt). Một scene có tối đa 7 ref visual_asset + character.
    - **Root-cause #3: không có entity body/outfit riêng** → model tự suy diễn quần áo theo bối cảnh (tuyết → áo parka nâu) và tự đổi dáng người.
    - **Bộ 2 entity chuẩn cho vlogger (Rule 46 & Bài học 60 — TUYỆT ĐỐI KHÔNG TẠO ENTITY OUTFIT RIÊNG):**
      | Entity | Nguồn ảnh | Chứa gì |
      |---|---|---|
      | `<Vlogger>` | Ảnh mặt user cung cấp (Ice Age: `uploads/nora_main.jpg`) — upload thẳng, KHÔNG gen lại | Chỉ khuôn mặt, tóc, khuyên tai |
      | `<Vlogger> Body` | **`EDIT_CHARACTER_IMAGE` từ ảnh body trần nguồn (`source_media_id` = media_id của Body trần chuẩn)** để "mặc trang phục" lên body: giữ nguyên 3 panel (chính diện, 3/4, sau lưng), tư thế, tỉ lệ giải phẫu (ngực đầy, eo thon, hông nở, chân dài), khung cắt vai/dưới cằm không lộ mặt, và nền studio. **Đây chính là Body đã mặc hoàn chỉnh trang phục, đóng vai trò là `<Vlogger> Body` duy nhất.** | Body đã mặc outfit: dáng người + trang phục |
    - **Vì sao body KHÔNG có mặt:** nếu ảnh body có mặt, model nhận 2 khuôn mặt khác nhau (ảnh mặt + ảnh body) và trộn lẫn → mặt trôi. Body sheet chỉ được mang thông tin dáng người và trang phục.
    - **Quy trình khi setup project (Rule 46 & Bài học 60):**
      1. Xóa logo ảnh mặt → upload → PATCH `media_id` của `<Vlogger>`.
      2. Lấy ảnh Body trần của user (ví dụ `uploads/nora_body_v3_clean.jpg`) làm nguồn (`source_media_id`), chạy `EDIT_CHARACTER_IMAGE` với prompt mô tả trang phục vừa vặn form-fitting để "mặc đồ" lên body. Tải về, kiểm tra không lộ mặt, giữ đúng dáng ngực/eo/hông/chân, xóa logo SynthID, upload lại lấy UUID sạch và gán trực tiếp làm `media_id` cho entity `<Vlogger> Body`.
      3. **Duyệt Body đã mặc đồ**: Xuất ảnh `<Vlogger> Body` sạch logo cho user duyệt trước khi gen video.
      4. Trong `clips.json` / scene: mọi clip có `<Vlogger>` chỉ gắn **2 ref nhân vật** `["<Vlogger>", "<Vlogger> Body", ...]`. **TUYỆT ĐỐI KHÔNG tạo entity Outfit riêng và KHÔNG gửi ảnh Body trần/gym vào video** (Rule 46 & 47).
      5. `common.identity` nêu rõ vai trò từng ảnh: *"her face and hair from the Nora face sheet, and her build and clothing from the Nora Body sheet."*
    - **LUẬT CỨNG cho shot POV (`pov`, `pov_hand`, `wide`): KHÔNG gắn `<Vlogger>`, `<Vlogger> Body` vào `refs`/`character_names`.** Bằng chứng: H2 hỏng 3 lần liên tiếp theo cùng một kiểu. Prompt nói Nora ở sau camera, nhưng ảnh ref chứa mặt Nora. Model ưu tiên ảnh hơn chữ nên vẽ Nora vào khung. Vì prompt POV không có khối identity/outfit, model tự chọn áo parka sẫm, rồi diễn giải "holding it firmly" thành cầm điện thoại thấy rõ màn hình. POV chỉ gắn ref của thứ cần thấy trong khung (động vật, đồ vật, người địa phương). Với `pov_hand`, tả tay áo bằng chữ trong lock (*"her bare empty hand… coming out of a cream suede sleeve with a thick white fox-fur cuff"*).
    - **Outfit lock trong `common.identity`:** Cập nhật `common.identity` trong `clips.json` để mô tả chi tiết màu sắc, chất liệu, phụ kiện của trang phục. Phải nêu rõ "NOT dark, NOT brown, NOT a parka" để ngăn model suy diễn.
    - **Outfit lock trong `video_prompt`:** Thêm `OUTFIT LOCK (CRITICAL)` vào mỗi `video_prompt` của cảnh có vlogger, nêu rõ màu chủ đạo (ví dụ: "WHITE/CREAM reindeer suede dress, NOT dark/brown coat").
    - **Lưu ý mannequin:** KHÔNG gen outfit trên mannequin (phom người thon thẳng, không có tay chân thật → các góc mâu thuẫn, mất tay áo/legging; Neanderthal ep 2 v1/v2 hỏng). Trang phục luôn EDIT trực tiếp lên Body sheet của user (Rule 46 & Bài học 60).
    - **[LEGACY — chỉ project Ice Age cũ] Lệnh crop Nora Outfit ref** (project mới dùng bài học 60):
      ```bash
      ffmpeg -y -i "output/<slug>/refs/nora_clean.jpg" \
        -vf "crop=iw*2/3:ih:iw/3:0" \
        "output/<slug>/refs/nora_outfit_crop.jpg"
      # Kết quả: panel 3/4 + full-body từ nora_clean.jpg, không có face close-up
      # Upload rồi dùng làm media_id của entity "Nora Outfit"
      ```

    **[ICE AGE PROJECT — LEGACY, project mới theo bài học 60] Nora — bộ 3 ref đã khóa:**
    - `Nora` ← `uploads/nora_main.jpg` (sheet mặt 4 góc, đã xóa logo → `refs/nora_main_clean.jpg`). Đây là ảnh nhân vật chính thức; KHÔNG dùng `nora_clean.jpg` làm ảnh mặt nữa.
    - `Nora Body` ← `refs/nora_body_v3_clean.jpg` (EDIT_CHARACTER_IMAGE từ nora_main + `uploads/nora_base_body_prompt.json` v3: khung cắt ngang vai, áo tank + quần bike ôm sát để thấy eo nhỏ, chân thon, ngực đầy; không có mặt).
    - `Nora Outfit` ← `refs/nora_outfit_crop.jpg` (crop từ `nora_clean.jpg`).
    - `refs` của mọi clip có Nora: `["Nora", "Nora Body", "Nora Outfit", ...]`.
    - **common.identity lock (dùng trong tất cả cảnh Nora xuất hiện):**
      ```
      Nora looks exactly like her three reference images: her face from the Nora face sheet
      (honey-blonde high ponytail with curtain bangs, grey-green eyes), her tall curvy hourglass build
      from the Nora Body sheet, and her clothing from the Nora Outfit sheet.
      OUTFIT LOCK (CRITICAL -- match the Nora Outfit reference image exactly):
      she wears a fitted WHITE/CREAM reindeer suede jacket-dress (mid-thigh length),
      deep plunging V neckline laced with thin leather ties and ivory beads along the edges,
      large white arctic-fox fur collar/hood framing the neckline,
      long sleeves with thick white fur cuffs,
      wide tan leather belt at waist sewn with rows of drilled ivory/bone teeth,
      the body of the dress is CREAM/OFF-WHITE suede -- NOT dark, NOT brown, NOT a parka.
      Light beige-white hide leggings (NOT dark/black).
      Knee-high suede cream boots with white fur cuff trim at the top.
      Small white fur mittens on a braided cord hanging at her sides.
      Every scene featuring Nora must show this exact costume.
      ```
    - **Inline OUTFIT LOCK cho video_prompt (thêm sau "No one else in the shot."):**
      ```
      OUTFIT LOCK (CRITICAL -- match Nora Outfit reference exactly):
      Nora wears a fitted WHITE/CREAM reindeer suede jacket-dress (mid-thigh length),
      deep V neckline laced with leather ties and ivory beads, large white arctic-fox fur collar,
      long sleeves with thick white fur cuffs, wide tan leather belt with bone teeth at waist,
      light beige-white hide leggings (NOT dark/black leggings),
      knee-high cream suede boots with white fur cuff trim,
      small white fur mittens on braided cord.
      This outfit is WHITE/CREAM throughout -- NOT a dark coat, NOT a brown parka, NOT modern clothing.
      ```

35. **CHẠY MÀ KHUNG HÌNH KHÔNG RUNG (bài học H1 Ice Age 16,000 BC bản v4 — người chạy hết sức nhưng mặt Nora và đường chân trời đứng yên như quay bằng gimbal):**
    - **Root-cause:** prompt chỉ ghi chung chung "the view bounces vertically with each footfall" một lần ở phần style. Model video mặc định ổn định hình (stabilize), nên một câu trừu tượng như vậy bị lờ đi. Chỉ chân và tay chuyển động, còn khung hình thì không.
    - **Fix: tả hiệu ứng rung NHÌN THẤY ĐƯỢC trên khung hình, có biên độ cụ thể, và nhắc lại trong TỪNG đoạn thời gian:**
      - Style `run` (bản đã sửa theo bài 36): *"Raw unstabilized footage: because the lens is in Nora's own outstretched right hand, every stride she takes jolts the whole frame — her face jumps up and down by about a tenth of the frame height and the horizon behind her tilts a few degrees left and right, with a brief motion blur on each footfall, while her face always stays in the frame."*
      - Mỗi segment `0-3s / 3-6s / 6-8s` của shot chạy phải có một cụm rung riêng, **gắn vào tay vlogger**, ví dụ *"her outstretched arm jolting the frame hard on every stride"*, *"the horizon swinging left and right with each footfall"*.
      - Không dùng các từ làm model ổn định hình: `smooth`, `steady`, `stable`, `cinematic tracking`.
    - **Mức rung theo hành động** (rung phải khớp nhịp chân): đi bộ → nảy nhẹ, chân trời nghiêng ≤2°. Chạy bộ → mặt nhảy ~5% chiều cao khung. Chạy thục mạng hoặc vấp → mặt nhảy ~10%, chân trời nghiêng 3–5°, nhòe chuyển động mỗi bước. Trượt, ngã → khung xoay mạnh. Với shot selfie, mặt vlogger luôn nằm trong khung; không tả "khung trôi khỏi mặt rồi giật về" (xem bài 36).
    - **Review:** khi xem contact sheet, so vị trí mặt và đường chân trời giữa các khung liền nhau. Nếu gần như không đổi trong lúc nhân vật đang chạy thì trừ điểm Motion Quality và sửa prompt theo mẫu trên.

36. **TẢ RUNG NHƯ MỘT CAMERA ĐỘC LẬP LÀM MẤT GÓC SELFIE (bài học H1 Ice Age v5 — v4 giữ selfie đủ 8 giây, v5 thành người ngoài chạy giật lùi quay theo, cả hai tay Nora đều đánh):**
    - **Root-cause:** thay đổi duy nhất giữa v4 và v5 là câu rung *"the framing drifts off her face and snaps back"* cùng cụm *"the framing lurching and snapping back"* trong từng segment. Câu này mô tả khung hình có chuyển động riêng, tách khỏi cơ thể Nora, nên model hiểu là có một người quay riêng và dựng thành tracking shot. (Mới có một mẫu so sánh, nhưng đây là thay đổi duy nhất.)
    - **Fix:** mọi mô tả rung trong shot selfie/run phải nêu **nguyên nhân là tay của chính vlogger**: *"because the lens is in Nora's own outstretched right hand, every stride she takes jolts the whole frame … while her face always stays in the frame"*. Segment dùng *"her outstretched arm jolting the frame"*, không dùng "the framing lurches / drifts / snaps back".
    - **Kiểm tra trước khi gen:** grep prompt shot `run`/`selfie`; không được có `framing (drifts|lurch|snaps)`.

37. **SHOT POV TẢ HÀNH ĐỘNG CỦA NGƯỜI QUAY → MODEL VẼ NGƯỜI ĐÓ TỪ BÊN NGOÀI (bài học H2 Ice Age v5 — cuối clip thấy một người mặc đồ sẫm lăn xuống dốc ở góc người thứ ba):**
    - **Root-cause:** segment ghi *"the camera pitches down sharply as Nora slides over the lip"*. "Nora slides" là hành động cơ thể có chủ ngữ là người, nên model dựng hình người đó trượt. Prompt POV không gắn ref Nora, nên model tự bịa ra một người mặc đồ sẫm.
    - **Fix:** trong shot `pov`/`wide`, chủ ngữ chỉ được là **góc nhìn hoặc khung hình** ("the view tips forward and drops over the lip, sliding fast down the snowy slope, snow spraying across the frame"), không bao giờ là "Nora …". Riêng `pov_hand` được tả bàn tay ("Nora's bare hand lifts…") vì tay có trong khung.
    - **Không dùng phủ định để chặn người** ("no person is seen", "no face, no body"): phủ định vẫn gọi tên đối tượng (cùng cơ chế với bài 33). Viết câu khẳng định: *"only snow, sky and the slope fill the frame"*, *"only the world in front of her fills the frame"*.
    - Đã sửa cùng lỗi ở S30 (cũng "Nora slides over the lip") và S49 ("whips back down toward Nora" trong shot wide → "toward the firelit camp").
    - **Kiểm tra trước khi gen:** với clip `pov`/`wide`, grep segment; không được có `\bNora\b` ngoài "Nora says".

38. **SHOT POV BỊ NGƯỜI LẠ CHIẾM KHUNG — "OVER THE SHOULDER" VÀ "FROM BEHIND THE CAMERA" (bài học H2 Ice Age v6 — 2.5 giây đầu quay qua vai một phụ nữ lạ tóc nâu tết, áo parka sẫm, không phải Nora):**
    - **Root-cause:** trường `shot` ghi *"first looking back over the shoulder"*. Với model video, "over the shoulder" là thuật ngữ góc máy chuẩn: quay qua vai một người đang đứng trong khung. Model dựng đúng nghĩa đen. Vì cảnh POV không gắn ref vlogger, model bịa ra một người lạ. Thêm nữa, lời thoại gắn dạng *"Nora says from behind the camera"* ngầm báo có một người quay đứng sau máy, càng kéo model vẽ người. Đoạn cuối *"sliding fast down the slope"* là hành động của cơ thể, nên vẫn ra một người lăn.
    - **Fix:**
      - Không dùng thuật ngữ góc máy có người trong đó (`over the shoulder`, `OTS`, `two-shot`, `behind her`) cho shot POV. Viết theo chuyển động của góc nhìn: *"the view swings round to face backward toward the mammoth, then swings forward to the riverbank edge"*.
      - Lời thoại POV/wide gắn dạng **`Nora's off-screen voice says, …:`**, không dùng "from behind the camera".
      - Rơi hoặc trượt trong POV thì tả mặt đất lao về phía ống kính: *"the view tips forward over the lip and the snowy slope rushes up toward the lens, snow spraying across the frame until it turns white"*. Không dùng "sliding", "tumbling", "falling" (động từ của cơ thể).
    - **Kiểm tra trước khi gen:** clip `pov`/`wide` không được có `over the shoulder|from behind the camera|\b(sliding|tumbling|falling)\b` trong `shot` và segment.
    - **Trạng thái:** fix đã áp vào `clips.json` nhưng chưa gen kiểm chứng (hết credit ngày 2026-10-02). Gen xong phải ghi kết quả vào đây.

39. **NHẢY HOẶC TIẾP ĐẤT TRONG SHOT SELFIE DỄ BỊ BUÔNG MÁY → CHUYỂN GÓC THỨ BA (bài học H2 Ice Age 16,000 BC bản v7):**
    - **Root-cause:** Khi mô tả nhân vật nhảy hoặc trượt qua gờ dốc ("Nora reaches the edge and leaps, sliding feet-first..."), model video AI (Omni Flash / Veo) ưu tiên mô tả hành động cơ thể tiếp đất tự nhiên (người nhảy phải vung hai tay giữ thăng bằng), dẫn đến việc model "buông điện thoại", lùi camera ra ngoài thành góc người thứ 3 (third-person spectator wide shot) hoặc vẽ Nora chạy ra xa máy.
    - **Fix:**
      - **Khóa cứng cánh tay và máy quay (Permanent Arm & Camera Lock):** Trong shot selfie có động tác nhảy/rơi/trượt, bắt buộc tả rõ cánh tay vlogger luôn duỗi thẳng và nắm chặt máy hướng về mặt mình: *"Nora plunges downward over the icy lip, her right arm remaining permanently extended gripping the camera tightly aimed directly back at her screaming face; she NEVER drops, releases, or lets go of the camera, and the view NEVER switches to third-person or spectator angle."*
      - **Tả chuyển động khung hình và tuyết thay vì tả chuyển động toàn thân:** Khung hình rung giật dọc theo quán tính cú rơi (`view jerks violently downward with the sudden drop`), tuyết bắn mù mịt xung quanh bờ vực, nhưng khuôn mặt vlogger luôn neo chặt ở trung tâm khung hình selfie.
    - **Kiểm tra trước khi gen:** Trong shot selfie có hành động nhảy/rơi/trượt (`leap`, `slide`, `jump`, `fall`): Bắt buộc phải có mệnh đề khẳng định: `her [right/left] arm remains extended pointing the camera at her face, NEVER drops or lets go of the camera, view never switches to third-person`.
    - **Bằng chứng thực nghiệm:** H2 bản v8 (media `665ccebc-ec01-406a-88cd-55aaefc9643b`) giữ góc selfie 100% từ 0s đến 6s, Nora vừa trượt dốc tuyết vừa la hét trực tiếp vào ống kính, cánh tay vươn dài giữ chắc máy, hoàn toàn không chuyển góc thứ 3.

40. **BODY DRIFT KHI DÙNG VÁY MANNEQUIN VÀ THỨ TỰ TRUYỀN REF TRONG R2V INGREDIENTS (bài học H1/H2 Ice Age 16,000 BC bản v7):**
    - **Root-cause:**
      1. Ảnh Outfit tạo trên manocanh (mannequin display) có phom người thon gọn, thẳng đuột tiêu chuẩn. Khi đưa vào R2V ingredients cùng với ảnh Body đồng hồ cát, model video AI có xu hướng bị phom dáng mảnh khảnh của manocanh làm lấn át (body drift), khiến nhân vật trong video bị phẳng ngực và mất đường cong eo-hông dù prompt có ghi "hourglass build".
      2. Thứ tự ref gửi lên server: Nếu entity Outfit được gửi trước entity Body, model sẽ dựng phom áo trước khi gán tỉ lệ cơ thể.
    - **Fix (từ 05/10/2026 thay bằng Rule 46 & bài học 60: outfit EDIT trực tiếp lên Body, <Vlogger> Body chính là Body đã mặc trang phục, video chỉ nhận `["<Vlogger>", "<Vlogger> Body"]` → không còn mannequin và không có entity Outfit riêng lẻ; các ý dưới chỉ là tài liệu tham khảo cho project cũ):**
      - **Bảo toàn thứ tự truyền Ref theo chuỗi nhận diện:** Server (`agent/sdk/services/operations.py`) bảo toàn thứ tự entities trong `character_names`: `[Face] -> [Body]` (ví dụ: `["Nora", "Nora Body"]`). Model cố định nhận diện khuôn mặt trước, sau đó áp vóc dáng và trang phục từ Body sheet.
      - **Manocanh không đầu (Headless Mannequin):** Ảnh trang phục manocanh BẮT BUỘC là manocanh không đầu trên nền studio trung tính, chụp 3 góc (chính diện, 3/4, sau lưng); tuyệt đối không có tóc giả hay mặt người giả để tránh xung đột nhận diện khuôn mặt.
      - **Khóa tương phản giải phẫu cơ thể (Negative Contrast Constraints) trong Prompt:** Trong `common.identity` và `video_prompt`, phải có cụm từ tương phản đối kháng mạnh mẽ ép model tuân thủ ảnh Body: *"BODY LOCK (CRITICAL): Nora has a voluptuous hourglass figure with a large full heavy natural bust, tiny narrow waist, and wide curvaceous hips matching Nora Body reference; she is NOT skinny, NOT slender, NOT petite, NOT flat-chested, and her deep neckline proudly showcases her cleavage."*
    - **Bằng chứng thực nghiệm:** H1 (media `81b3bf5f`) và H2 (media `665ccebc`) bản v8 thể hiện chuẩn xác vóc dáng đồng hồ cát nóng bỏng với vòng 1 đầy đặn và váy slip dress lụa trắng xẻ ngực sâu trùng khớp hoàn toàn với ảnh `thumbnail_v2_2k_clean.jpg` và `nora_body_v3_clean.jpg`.

41. **LOCK BODY, TÔN DÁNG VÒNG 1 (PUSH-UP CLEAVAGE), CHÂN DÀI SIÊU MẪU & QUY TẮC VIẾT PROMPT (bài học H1/H2 Ice Age 16,000 BC bản v9):**
    - **Hiện tượng & Root-causes khiến vòng 1 trông nhỏ và chân bị ngắn trong video:**
      1. *Ảnh Body Ref bị nén thể thao:* Người mẫu trong ảnh Body thường mặc áo tank top thể thao bó sát (compression tank), khiến mô ngực bị nén phẳng chặt vào lồng ngực (cỡ C-cup thể thao tự nhiên) và tỉ lệ thân/chân 1:1, không có gọng đẩy ngực (push-up) hay khe ngực sâu như trong ảnh thumbnail.
      2. *Động tác chạy mở rộng lồng ngực:* Khi vlogger chạy thục mạng một tay vươn cầm máy và một tay vung ra sau, lồng ngực mở rộng kéo dạt hai bầu ngực sang hai bên nách, không thể chụm lại tạo khe ngực sâu như lúc đứng yên khoanh tay (trong ảnh thumbnail).
      3. *Hiệu ứng co ngắn phối cảnh góc rộng (Foreshortening) của ống kính 0.5x:* Khi cầm máy ngang mặt chúc xuống, phần đầu/mặt ở gần ống kính nhất sẽ bị phóng to (magnified), trong khi phần hông/đùi/chân ở xa trục camera sẽ bị hút nhỏ và co ngắn lại (foreshortening). Người chạy chúi thân trên về phía trước càng làm chân bị lùi sâu vào hậu cảnh.
      4. *Vị trí khối BODY LOCK bị chôn vùi cuối prompt (Attention Decay):* Trong prompt dài 5.000–6.000 ký tự, nếu để khối BODY LOCK ở vị trí thứ 8 sau 3.500 ký tự (sau style, setting, timed segments, physics...), model AI bị phân tán sự chú ý và ưu tiên mô phỏng chuyển động trước khi áp hình thể nhân vật.
    - **Bộ giải pháp chuẩn khi viết Prompt (BẮT BUỘC ÁP DỤNG MỌI CẢNH):**
      - **1. Kiến trúc Prompt đưa Body Lock lên SỚM (Early Conditioning):**
        Đưa khối `Identity & Body Lock` lên vị trí **ngay sau `Shot:`**, TRƯỚC các phân đoạn hành động `0-3s`, `3-6s`. Cấu trúc chuẩn: `[Style] -> [Setting & Light] -> [Shot] -> [Identity & Body Lock (Face + Body + Outfit)] -> [Timed Segments] -> [Background] -> [Physics] -> [Lock] -> [General] -> [Audio]`. Model AI sẽ định hình lưới giải phẫu và trang phục trước khi render động tác.
      - **2. Cụm từ khóa đấm lực vòng 1 (Push-up Cleavage Punch):**
        TUYỆT ĐỐI CẤM các từ gây xệ hoặc phẳng ngực (`low-hanging bust`, `natural bust compression`). BẮT BUỘC dùng cụm khẳng định đối kháng cực mạnh:
        *"BODY LOCK (CRITICAL): [Character] has an exceptionally large, full, voluminous heavy bust pushed up with prominent deep cleavage valley spilling out of the plunging V-neckline (dramatic push-up cleavage effect, huge voluptuous cleavage), a dramatically tiny narrow cinched waist, and wide curvaceous hips; she is distinctly voluptuous, curvy, and busty -- NOT flat-chested, NOT small-busted, NOT skinny, NOT slender."*
      - **3. Cụm từ khóa chân dài & chiều cao siêu mẫu (Statuesque Legs Punch):**
        CẤM dùng "thick thighs" đơn độc làm chân trông ngắn và mập. Bổ sung thông số chuẩn:
        *"STATURE & LEGS: [Character] is a tall, statuesque woman (178 cm / 5'10" tall) with exceptionally long, slender model legs and high hip placement, an elongated tall athletic silhouette -- NOT short, NOT stubby, NOT stocky."*
      - **4. Quang học góc máy tôn dáng (Optical Angle — Low-Angle Chest Level):**
        Trong `style.run` và `style.selfie`, điều chỉnh vị trí đặt máy:
        *"The lens sits at the end of [Character]'s outstretched right arm, held at chest/mid-torso level angled slightly upward looking back at [Character]; this dynamic angle captures her face, her plunging low-cut cleavage, tiny waist, and long slender legs, emphasizing her tall statuesque height."*
        Góc máy từ ngực/bụng hất nhẹ lên loại bỏ hiện tượng to đầu - ngắn chân, khoe trọn khe ngực và kéo dài đôi chân.
      - **5. Nhúng đặc điểm thể hình trực tiếp vào chuyển động (Action-Segment Reinforcement):**
        Trong từng phân đoạn `0-3s`, `3-6s`, lặp lại trực tiếp:
        *"...her tall statuesque frame and long slender legs pumping powerfully through the snow; her exceptionally large, voluptuous full bust bounces with dramatic push-up cleavage prominently spilling out of the deep plunging neckline of her snug white silk slip dress; her tiny cinched waist and wide curvy hips accentuated..."*
    - **Bằng chứng thực nghiệm:** H1 (`2f001786`) và H2 (`287f5bf5`) bản v9: góc máy hất nhẹ lên khoe trọn đôi chân dài miên man đang sải bước trong tuyết, khe ngực sâu push-up căng đầy bốc lửa trong chiếc váy lụa trắng xẻ sâu, điểm số AI Review Scorecard đạt 95.5 và 97.0 / 100.

42. **BỘ TỨ NGUYÊN LÝ VẬT LÝ SINH TỒN & ĐIỂM MÙ QUANG HỌC POV VLOG (bài học H2 Ice Age 16,000 BC bản v10):**
    
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

    #### 3. Nguyên lý Động học Camera & Điểm mù Quang học (Optical Viewpoint)
    - **Hiện tượng "Điện thoại ma" (Ghost Phone) dưới góc nhìn vật lý AI:**
      - Khi trong prompt xuất hiện từ `phone`, `smartphone`, `screen`, `device`, `selfie stick` (ngay cả trong câu cấm *"she never drops the phone"*), model AI hiểu rằng có một vật thể vật lý 3D mang tên "chiếc điện thoại" cần xuất hiện trong khung hình. Thế là nó vẽ chiếc iPhone trên tay Nora và tự động đặt một camera thứ ba lùi ra xa để quay cảnh đó!
    - **Vật lý quang học chân thực của POV Vlog:**
      - Bản thân người xem đang nhìn **XUYÊN QUA ỐNG KÍNH MÁY QUAY**.
      - Cánh tay phải giơ ra giữ ống kính, nghĩa là **thân máy và bàn tay cầm máy nằm ở PHÍA SAU MẶT PHẲNG TIÊU CỰ (Behind the focal plane / Off-screen)**, quang học tự nhiên không thể nào chụp được chính cái máy đang quay nó!
      - **Đặc tả đúng kỹ thuật:**
        `Handheld front-lens vlog footage, ultra-wide 0.5x lens, natural wide-angle handheld perspective. The lens sits at the end of [Character]'s outstretched right arm, held at chest level angled slightly upward; the camera lens itself and her right gripping hand are completely outside the visible frame and never seen; her free left hand is completely empty and flails naturally for balance.`
      - **TUYỆT ĐỐI CẤM 100% các từ:** `phone`, `smartphone`, `screen`, `device`, `selfie stick` trong toàn bộ prompt.
    - **Động học chấn động (Kinematic Shockwave):**
      - Khi thân người đập xuống tuyết và trượt dốc, cánh tay có khớp vai và cơ bắp chịu chấn động gián tiếp: khung hình phải rung giật cực mạnh chúc xuống mặt tuyết (`rotational jolt & downward shockwave`), tuyết bột bắn tung tóe dính vào mặt kính thấu kính (`powder snow coats the lens glass`) làm mờ nhòe tự nhiên (whiteout transition).

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

43. **LỖI "VẬT THỂ HÓA MÁY ẢNH" & XUNG ĐỘT GÓC NHÌN NGƯỜI THỨ BA (Camera Prop Glitch & Third-Person POV Conflict — Bài học Scene 04 Ice Age 16,000 BC):**
    
    #### 1. Hiện tượng lỗi thực tế
    - Trong Scene 04 của Ice Age 16,000 BC, ở giây thứ 1, AI vẽ Nora đứng quay lưng lại, trên tay cầm một chiếc **máy ảnh compact kỹ thuật số có màn hình LCD** chĩa vào thợ săn Torak. Đến giây thứ 5 khi cô xoay tay lại để selfie, chiếc máy ảnh biến dạng thành một **ống kính máy ảnh rời (DSLR Lens)** to đùng trên tay Nora giơ ra trước mặt khán giả.
    
    #### 2. Root Cause (Nguyên nhân gốc rễ)
    - **Xung đột góc nhìn chết người (Third-Person vs POV):**
      - Prompt mô tả: *"Handheld vlog footage that starts from Nora's raised hand just behind her head and then turns around to face her... Shot: From just behind Nora's head, then turning around to a selfie."*
      - Khi camera đặt ở phía sau đầu / sau lưng vlogger nhìn tới (`from just behind Nora's head`), đây là **GÓC NHÌN NGƯỜI THỨ BA (Third-person spectator)**. Khán giả đứng ngoài nhìn thấy toàn bộ lưng và cánh tay của Nora.
      - AI model lập luận logic: *"Người xem đang đứng sau lưng quay cảnh Nora và Torak, vậy vật thể mà tay Nora đang giơ lên là cái gì?"* ➔ AI bắt buộc phải vật thể hóa thành một **chiếc máy ảnh kỹ thuật số (Compact Camera / LCD screen)** trong tay nhân vật!
    - **Lỗi ngữ nghĩa từ "Camera" như một Đạo cụ (Prop):**
      - Mặc dù đã cấm `phone/smartphone`, prompt lại dùng từ `camera` tới 5 lần như tân ngữ của hành động: *"starts from Nora's raised hand... Nora slowly brings the camera around... she never lets go of the camera..."*.
      - Trong góc nhìn người thứ ba, AI hiểu "the camera" là một **đạo cụ vật lý (prop)** cầm tay chứ không phải ống kính của chính người xem. Khi Nora xoay tay lại, AI tiếp tục giữ góc nhìn người xem ở ngoài và vẽ một **ống kính máy ảnh rời (DSLR Lens)** trong tay Nora!
    - **AI Video không thể tự "chui vào mắt" vlogger:**
      - AI diffusion model không thể chuyển đổi mượt mà giữa camera thứ 3 (sau lưng) và camera thứ 1 (POV cầm tay) trong cùng một chuỗi khung hình liên tục mà không sinh ra thiết bị quay thứ hai.

    #### 3. Quy tắc & Giải pháp Khắc phục Triệt để
    - **1. TUYỆT ĐỐI CẤM các shot quay từ sau đầu / sau lưng vlogger rồi xoay ra trước mặt:**
      - CẤM: `from just behind her head`, `from behind her back`, `over her shoulder from behind then turning`.
    - **2. Kỹ thuật Đơn góc nhìn thuần khiết (Single-Perspective Vlog Purity — THAY THẾ Whip Pan 180°):**
      - *Lưu ý quan trọng (Đã lỗi thời):* Cú lia máy Whip Pan 180° trong 1 clip trước đây từng được thử nghiệm để loại bỏ đạo cụ máy ảnh ma, nhưng đã bị bãi bỏ vì gây cảm giác phi lý (quay cam trước lật cam sau thì mù màn hình, camera bay như có người thứ ba; xem chi tiết Bài học 44).
      - **Giải pháp chuẩn:** Khi vlogger muốn tương tác với đối tượng phía sau hoặc cảnh vật:
        - **Bản đề xuất 100% Selfie Tự Nhiên (Over-the-Shoulder Selfie Interaction):** Toàn bộ shot 8s–10s giữ 100% cam trước Selfie 0.5x. Vlogger ở 1/3 tiền cảnh, đối tượng ở 2/3 hậu cảnh. Tương tác qua ánh mắt và quay đầu, camera luôn cố định vào vlogger, loại bỏ hoàn toàn cảm giác xoay lật giả tạo.
        - **Hoặc Cặp Shot Kép (Two Separate Shots):** Shot 1 (100% POV Cam sau) nhìn qua mắt vlogger ➔ Cắt cảnh (Cut) sang Shot 2 (100% Selfie Cam trước) vlogger nói chuyện. Không xoay 180° trong cùng 1 clip.
    - **3. Không bao giờ mô tả nhân vật "cầm/xoay the camera" như một vật thể:**
      - Thay câu *"she brings the camera around"* bằng *"she pivots her extended arm back toward herself"*.
      - Điểm nhìn người xem chính là thấu kính (`The viewer looks directly through the camera lens`).
    - **4. Tự động kiểm tra qua Prompt Self-Linter:**
      - Linter BẮT BUỘC quét và chặn các cụm từ: `behind (her|his|their) head`, `behind (her|his|their) back`, và cảnh báo hành động cầm nắm `camera` làm đạo cụ.

44. **LỖI LẬT XOAY CAMERA 180° GIỮA CAM TRƯỚC & CAM SAU TRONG CÙNG MỘT SHOT (The 180° Camera Flip Fallacy & Single-Perspective Vlog Purity — Bài học Scene 04 Ice Age 16,000 BC bản v2):**
    
    #### 1. Hiện tượng lỗi thực tế
    - Dù đã loại bỏ được chiếc máy ảnh/ống kính ma bằng kỹ thuật Whip Pan 180° (Two-Phase POV), nhưng khi xem video thực tế, người xem lập tức cảm thấy **vô lý, giả tạo và phi logic** khi camera đang quay góc nhìn thứ nhất (cam sau nhìn Torak ở 0-3s) rồi đột ngột xoay lật 180° chuyển sang góc selfie (cam trước ở 4-10s) trong cùng một shot 10 giây.
    
    #### 2. Root Cause (Nguyên nhân gốc rễ)
    - **Nghịch lý công thái học điện thoại (Smartphone Ergonomics Fallacy):**
      - Trong thực tế, khi cầm điện thoại quay vlog:
        - Nếu bạn đang quay cam sau (quay người khác/cảnh vật), rồi lật ngược điện thoại 180° lại để tự quay mình, thì màn hình điện thoại sẽ quay ra phía trước! Người quay bị hoàn toàn mù màn hình, không thể nhìn thấy khung hình, biểu cảm hay kiểm tra người đứng sau lưng.
        - Nếu dùng tính năng chuyển cam trên màn hình (flip camera button), ứng dụng luôn tạo ra một cú **CẮT CẢNH (Cut shot)**, chứ không bao giờ lia xoay vật lý 180° trong không gian.
    - **Nghịch lý động học không gian (Spatial Kinematics & Fake Cameraman Feel):**
      - Ở 3 giây đầu, điểm nhìn camera nằm ở ngang tầm mắt người quay (cam sau). Đến giây thứ 5, camera bỗng nhiên nằm ở trước mặt vlogger cách 60cm nhìn ngược lại.
      - Cú xoay này đòi hỏi camera phải tự bay một vòng quỹ đạo bán kính lớn trong không khí, tạo cảm giác như **có một người quay phim thứ ba (cameraman cầm gimbal/flycam)** chạy vòng quanh vlogger, phá hủy hoàn toàn cảm giác "vlogger đơn độc tự cầm máy sinh tồn".
    - **Gãy mạch thị giác (Visual Continuity Breakdown):**
      - Scene 03 là góc Selfie cam trước. Scene 05 là góc Selfie cam trước. Việc Scene 04 bị chèn một đoạn cam sau rồi xoay lật làm vỡ nhịp điệu thị giác và tính nhất quán của chuỗi vlog.
    
    #### 3. Quy tắc Vàng: Đơn góc nhìn thuần khiết & Selfie qua vai (Single-Perspective Vlog Purity & Over-the-Shoulder Vlog Composition)
    - **Quy tắc tuyệt đối: 1 SHOT = 1 GÓC NHÌN DUY NHẤT (Single Perspective per Shot):**
      - Mỗi shot 8s–10s chỉ được chọn MỘT trong hai góc nhìn:
        - Hoặc là **100% Selfie (Cam trước 0.5x)** từ đầu đến cuối clip.
        - Hoặc là **100% First-Person POV (Cam sau)** từ đầu đến cuối clip.
      - **TUYỆT ĐỐI CẤM** xoay lật 180° giữa cam trước và cam sau trong cùng một shot (`whip pan 180-degree ... turning to face`, `pivoting the viewpoint back`).
    - **Kỹ thuật Vlog Selfie qua vai (Over-the-Shoulder Selfie Interaction):**
      - Khi vlogger muốn giao tiếp hoặc phản ứng với một nhân vật phụ / sinh vật xuất hiện:
        1. **Bố cục 1/3 tiền cảnh (Vlogger in Foreground 1/3):** Vlogger cầm máy ở góc selfie 0.5x (bên trái hoặc bên phải), chiếm 1/3 khung hình. Tay cầm máy nằm ngoài điểm mù (`outside the visible frame`).
        2. **Nhân vật phụ ở 2/3 hậu cảnh (Subject in Background 2/3):** Nhân vật phụ (như Torak, thổ dân, quái thú) xuất hiện ở 2/3 khung hình còn lại, nhìn thấy rõ hành động bước tới, cử chỉ hoặc hiệu lệnh săn bắn ngay phía sau vai vlogger.
        3. **Tương tác đa chiều bằng ánh mắt & quay đầu (Gaze & Head Turns, NOT Camera Flips):**
           - Vlogger nói trực tiếp với khán giả qua ống kính: *"Okay, that's Torak. My name for him."*
           - Vlogger khẽ quay đầu hoặc liếc mắt ra sau kiểm tra đối tượng khi đối tượng hành động (giơ tay dừng, giơ giáo): *"Hand flat, palm down, probably means stay. I stay."*
           - Vlogger quay lại nhìn thẳng vào camera thể hiện cảm xúc chân thật (lo lắng, cười gượng, thì thầm): *"A stranger walking into a winter camp? I'd spear me too."*
        ➔ Camera luôn neo cố định vào vlogger, chuyển động chỉ là rung lắc bước chân tự nhiên (`subtle hand shake / footfall bounce`), tạo cảm giác chân thực 100% như vlog YouTube/TikTok đời thực!
    
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

47. **OUTFIT DRIFT, SAI KIỂU TÓC & CÔNG THỨC KHÓA NHẬN DIỆN VỚI ẢNH MANNEQUIN TRONG R2V (Omni Flash / Veo 3 — Bài học Scene 00 H1 Ice Age 16,000 BC bản Test 1-4):**
    
    #### 1. Hiện tượng lỗi thực tế qua các vòng Test
    - **Test 1**: Mô tả sơ sài/thiếu chuẩn xác khiến vlogger biến thành mặc váy ngắn hiện đại (mini dress) lộ đùi trần giữa bão tuyết, kèm theo chiếc máy ảnh DSLR trên gimbal xuất hiện góc phải khung hình.
    - **Test 2**: Dù đã loại sạch từ khoá camera để hết máy ảnh ma, nhưng do **xoá trắng mô tả trang phục và tóc trong prompt** (chỉ để câu logic trơ trọi `"wearing the exact outfit from reference image"`), kết hợp việc gửi kèm ref `Nora Body` (ảnh mặc đồ gym: áo tank top sát nách và quần đùi đen lộ da thịt trần). Kết quả: Vlogger biến thành người tiền sử cởi trần mặc áo da thú thô màu nâu rách rưới, tóc nâu bù xù xoã tự do, mất sạch kiểu tóc đuôi ngựa vàng và mất đầm trắng may đo!
    - **Test 3**: Đổi sang dùng ảnh crop nhân vật `nora_outfit_crop_clean.jpg`. Đã khóa được màu trắng và tóc đuôi ngựa, nhưng thiếu mất cổ áo mũ trùm lông cáo tuyết dày bản lớn và đai răng xương đặc trưng của trang phục ma-nơ-canh `nora_outfit_clean.jpg`.
    - **Test 4 (Chuẩn xác 100%)**: Dùng đúng ảnh ma-nơ-canh 3 góc `nora_outfit_clean.jpg`, loại bỏ hoàn toàn `Nora Body`, và viết khối `IDENTITY & OUTFIT LOCK` neo chính xác từng chi tiết (mũ trùm lông cổ vai to bản, dây đan ngực chéo, thắt lưng nẹp răng xương, bo viền lông cổ tay, tóc đuôi ngựa vàng cột cao có mái bay). ➔ Kết quả: Đạt chuẩn 100% cả tóc lẫn outfit.

    #### 2. Root Cause (Nguyên nhân gốc rễ)
    1. **Nhiễm da thịt trần từ ảnh Body gym (`Body Latent Contamination`):**
       - Khi đưa entity `<Vlogger> Body` (vốn mặc đồ tập gym ngắn áo tank top + quần đùi lộ da tay chân) vào cùng danh sách `character_names` với `<Vlogger> Outfit` trong bối cảnh mùa đông/tiền sử, model R2V bị nhiễm latent tay chân trần từ ảnh body. Khi kết hợp với bối cảnh "Ice Age 16,000 BC", AI tự động biến thành áo da thú cộc tay cởi trần kiểu người tiền sử generic!
    2. **Cái bẫy "Xoá sạch mô tả outfit" (`The Empty Prompt Trap`):**
       - Diffusion model hoạt động bằng cơ chế liên kết chéo (Cross-Attention) giữa text embeddings và image latents. Nó KHÔNG hiểu câu lệnh trỏ logic thuần tuý: `"wearing the exact outfit from reference image"`.
       - Nếu trong prompt không có các từ neo thị giác (`honey-blonde hair tied in a high wavy ponytail with curtain bangs`, `cream-white reindeer suede dress`, `fluffy white fur hood and collar`, `criss-cross leather ties`), thì các từ khoá bối cảnh thời kỳ (`Ice Age 16,000 BC mammoth steppe`) sẽ chiếm 100% trọng số attention, ép nhân vật ra kiểu tóc bù xù xoã ngang vai và áo da thú cởi trần nguyên thủy.
    3. **Hiện tượng loãng trọng số Ma-nơ-canh (`Mannequin Attention Dilution`):**
       - Ảnh ma-nơ-canh không đầu trên nền trung tính rất tốt để AI học cấu trúc 3D của trang phục, NHƯNG nếu có quá nhiều ref (ví dụ 5 ref gồm cả Body, Location, Creature) hoặc thiếu text anchor, model sẽ bỏ qua ma-nơ-canh vì nó không phải là con người.
       - Khi tinh gọn ref còn đúng 3 ref cốt lõi `[<Vlogger>, <Vlogger> Outfit, Creature]` và có text anchor mạnh mẽ, model ánh xạ chính xác 100% bộ đầm từ ma-nơ-canh lên thân hình vlogger!

    #### 3. Quy tắc Vàng: Công thức Khóa Nhận diện Tóc & Outfit chuẩn 100%
    1. **Bộ Reference tối ưu (Tối đa 3 Ref cho cảnh Vlogger):**
       - Khóa chuẩn: `[<Vlogger>, <Vlogger> Outfit, <Creature/Asset>]`.
       - **BẮT BUỘC LOẠI BỎ `<Vlogger> Body`** đối với mọi cảnh nhân vật mặc trang phục mùa đông/may đo dài tay kín đáo. Từ 05/10/2026 (bài học 60): **Body trần/gym** không bao giờ gửi vào video; trang phục nào cũng được mặc lên Body bằng EDIT và chính ảnh đã mặc đó là `<Vlogger> Body` gửi vào video.
       - **[ĐÃ THAY bởi bài học 60]** Entity `<Vlogger> Outfit` chỉ còn ở project Ice Age cũ. Project mới: ảnh 3 góc đã mặc outfit (EDIT từ Body, xóa watermark) gán thẳng làm `<Vlogger> Body`, không có entity Outfit.
    2. **Khối cấu trúc Prompt `IDENTITY & OUTFIT LOCK` bắt buộc (Đưa lên vị trí SỚM ngay sau `Shot:` trước `0-3s`):**
       ```text
       IDENTITY & OUTFIT LOCK (CRITICAL -- match reference images exactly):
       [Character] has [hair color] hair tied in a [exact hairstyle, e.g. high wavy ponytail with curtain bangs framing her face], [eye color] eyes, and fair skin with natural pink flush. Her high blonde ponytail bounces energetically with each running stride.
       [Character] wears the exact outfit from the [Character] Outfit reference ([outfit_ref_name]): a tailored cream-white reindeer suede dress with a large fluffy white arctic-fox fur hood and collar framing a plunging laced V-neckline, long sleeves with thick white fur cuffs, a wide tan belt sewn with vertical bone teeth at her waist, thick white fur trim at the mid-thigh hem, cream hide leggings, and knee-high boots with white fur cuff trim.
       This outfit is WHITE/CREAM throughout -- NOT dark, NOT brown, NOT a caveman fur pelt, NOT sleeveless, NOT bare legs, NOT loose unkempt hair, NOT modern clothing.
       ```
    3. **Gia cố chi tiết trong từng phân đoạn hành động (Action Sub-clips):**
       - Phân đoạn `0-3s`: Nhắc lại chuyển động tóc và tay áo (`her blonde high ponytail bouncing with her desperate survival momentum; her cream suede sleeves with thick white fur cuffs pump powerfully in rhythm; her wide tooth-studded belt and fur collar flutter in the freezing wind`).
       - Phân đoạn `3-6s`: Nhắc lại tà váy và bo lông (`her white fur-trimmed dress and fur cuffs flutter in the freezing wind`).
    4. **Duy trì không vết tích thiết bị quay (No Ghost Devices):**
       - Tuân thủ Bài học 40, 42: hoàn toàn không xuất hiện từ `phone`, `smartphone`, `screen`, `device`, `gimbal`, `selfie stick`. Dùng góc nhìn `Handheld front-facing running vlog POV footage, ultra-wide 0.5x view, natural wide-angle perspective`.
    5. **Bằng chứng thực nghiệm:**
       - Scene 00 H1 Ice Age 16,000 BC bản Test 4 (`bfb7ba56-a131-45ae-8612-d2c5fa4528c1`) thể hiện chuẩn xác 100% bộ đầm may đo da tuần lộc trắng kem với cổ áo mũ trùm lông cáo tuyết dày to bản, đan dây ngực chéo, đai răng xương, bo lông gấu áo, kiểu tóc đuôi ngựa vàng cột cao có mái bay, động tác chạy nổ tuyết chân thực, không có thiết bị ma.

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
    - **Hiện tượng:** Scene 13 là POV của Nora, thoại viết `Nora's off-screen voice says`, gương mặt duy nhất trong khung là Alva → Alva mở miệng "nói" suốt clip bằng giọng Laomedeia. Vi phạm luật "chỉ vlogger nói".
    - **Root cause:** Omni Flash chỉ có 1 giọng (Slot 7) và luôn cố gắn khẩu hình vào **một cái miệng nhìn thấy được**. Khi miệng vlogger không có trong khung, nó gắn vào người bản địa duy nhất đang hiện mặt. Câu `Only Nora speaks` không đủ để khóa miệng người kia.
    - **Quy tắc:**
      1. Beat có thoại + người bản địa hiện mặt → **dùng Selfie Qua Vai** (Rule 42, mục 2b): vlogger 1/3 tiền cảnh nói bằng chính miệng mình, người bản địa 2/3 hậu cảnh; thêm `Nora`, `Nora Body` vào `character_names` (giữ tối đa 3 ref theo Bài học 47 & Rule 46).
      2. Clip người bản địa **không có thoại**: thêm câu khóa `"<Local>'s lips stay closed for the entire clip; she never speaks or mouths words, and communicates only by frowning, shaking her head and hand gestures. The only moving mouth in the frame is Nora's."` (Cập nhật 2026-10-05: người bản địa **được** nói ngôn ngữ không hiểu được ở sub-clip riêng, mục 2b; khi đó không dùng câu khóa này mà ghi rõ ai nói, lúc nào, giọng gì.)
      3. POV thoại ngoài khung chỉ an toàn khi trong khung **không có mặt người** (tay, đồ vật, phong cảnh) hoặc người bản địa quay lưng / ở rất xa.
    - **Rà soát:** sau khi gen, lọc mọi scene có `off-screen voice` + người bản địa trong `character_names` rồi kiểm tra miệng (Part 2: 13 lỗi rõ; 53, 31 nghi ngờ).

50. **HÀNH ĐỘNG HAI TAY KHI ĐANG CẦM MÁY & ĐƯỜNG ĐI CỦA GÓC NHÌN QUA CỬA (Two-Hand Action While Filming — Bài học Scene 09, 11 Ice Age 16,000 BC Part 2, user review 03/10/2026):**
    - **Hiện tượng:** Scene 11 Nora vén tấm da cửa bằng **cả hai tay** trong khi góc nhìn đã nằm sẵn bên trong lều nhìn ra — không thể vừa tự quay vừa có máy ở trong trước. Cuối clip `swings her outstretched arm` sinh ra bàn tay vung về phía ống kính. Scene 09 tấm da cửa tự vén lên cứng đờ "do gió" trong khi tóc và cỏ đứng yên.
    - **Root cause:** Prompt không phân vai hai tay (tay nào giữ góc quay, tay nào làm việc) và không mô tả góc nhìn đi qua cửa thế nào. Vật nặng (tấm da cửa) được giao cho "gió" thay vì cho một bàn tay.
    - **Quy tắc:**
      1. Mọi shot selfie ghi rõ: `"her right arm stays extended toward the lens for the entire clip ... Only her left hand is free."` Mọi thao tác (vén cửa, cầm cốc, kéo mũ) tả là `"using only her free left hand"`.
      2. Đi qua cửa trong selfie: cánh tay giữ máy dẫn trước → `"the viewpoint passes through the doorway first, facing back at Nora, and she follows it inside"`.
      3. Vật nặng chỉ chuyển động khi có lực: `"It is thick and weighted; it stays completely still unless a hand moves it."` Không dùng "sways in the wind / lifts slightly" cho tấm da cửa.
      4. Chuyển cảnh swing dùng **cả góc nhìn lia** (`"the whole view whips quickly to the left in a heavy motion blur; no hand comes into the frame"`), không dùng "swings her arm".

51. **NGÃ KHÔNG CÓ NHÂN QUẢ & GÓC QUAY ĐỨNG YÊN KHI NGÃ (Fall Without Cause — Bài học Scene 01 Ice Age 16,000 BC Part 2, user review 03/10/2026):**
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
    - **Chỉ đạo cốt lõi của User (05/10/2026):** Khi tạo ảnh trang phục mặc lên body, nó KHÔNG PHẢI là outfit riêng lẻ nữa. Nó chính là **Body đã mặc trang phục** và đóng vai trò trực tiếp là **`<Vlogger> Body`** duy nhất. Không tạo entity `<Vlogger> Outfit` riêng gây phân mảnh và thừa thãi. Downstream video R2V chỉ nhận: `["<Vlogger>", "<Vlogger> Body", ...]`.
    - **Bằng chứng:** Outfit gen trên mannequin hỏng (v1/v2: giày hiện đại, cụt tay, mất legging, làm phẳng ngực). Khi dùng `EDIT_CHARACTER_IMAGE` từ ảnh Body trần của user (`uploads/nora_body_v3_clean.jpg`) với prompt tôn dáng (ôm sát, nâng ngực nhô cao, eo thon, chân dài) → sinh ra ảnh 3 góc khớp nhau tuyệt đối, chuẩn trang phục cổ đại và giữ nguyên vóc dáng đồng hồ cát.
    - **Quy tắc 1 — tạo ref `<Vlogger> Body`:** Dùng ảnh Body trần nguồn của user làm `source_media_id`, chạy `EDIT_CHARACTER_IMAGE` để "mặc trang phục" lên body: giữ nguyên 3 panel (chính diện, 3/4, sau lưng), tư thế, tỉ lệ giải phẫu (ngực đầy, eo thon, hông nở, chân dài), khung cắt vai không lộ mặt, và nền studio. Sau khi sinh xong: tải về, xóa sạch watermark SynthID bằng `python tools/remove_watermark_from_image.py`, upload lại lấy UUID sạch và gán trực tiếp làm `media_id` cho entity `<Vlogger> Body`.
    - **Quy tắc 2 — ref cho video downstream:** Mọi clip có vlogger gắn `character_names`/`refs` = `["<Vlogger>", "<Vlogger> Body", ...]`. **TUYỆT ĐỐI KHÔNG tạo entity Outfit riêng và KHÔNG gửi ảnh Body trần/gym vào video** (tránh nhiễm da thịt trần, Rule 47).
    - **Câu identity:** *"Nora looks exactly like her two reference images: her face and hair from the Nora face sheet, and her build and clothing from the Nora Body sheet."* Vẫn giữ `OUTFIT LOCK` + `BODY LOCK` bằng chữ trong prompt (Rule 47).
    - **Cổng duyệt bắt buộc (Rule 46):** Bắt buộc trình ảnh `<Vlogger> Body` sạch logo cho user xem và duyệt phom dáng & trang phục trước khi gửi bất kỳ lệnh sinh video nào.

61. **PHÂN BIỆT RẠCH RÒI SELFIE VLOGGER VS POV ĐI SĂN / HÀNH ĐỘNG CẬN CHIẾN & TỶ LỆ GÓC MÁY VÀNG (Bài học Neanderthal 51ka, Scene 20–36, user review 08/10/2026):**
    - **Hiện tượng & Root Cause:** 
      1. Hiểu nhầm luật "phone is the camera" và bài học 25/39/50 (cánh tay vươn dài giữ máy) thành việc ép 100% mọi cảnh vlogger phải giơ tay selfie quay mặt mình. Kết quả: vlogger vừa đi săn vừa giơ tay quay mặt mình nói chuyện, biểu cảm đơ cứng, không thể di chuyển tự nhiên, biến cuộc đi săn thành buổi livestream lố bịch, phản sinh tồn.
      2. Áp dụng máy móc Rule 49 (thoại 18–22 từ) vào lúc áp sát con thú lớn, khiến nhân vật lải nhải khi đang cách bò mộng 3 mét.
    - **Quy tắc:**
      1. **Tỷ lệ Góc Máy Vàng (Golden Camera Ratio — Rule 42):** 
         - **60%–70% First-Person POV qua mắt vlogger (Cam sau):** Toàn bộ hành động rình rập, săn bắn, di chuyển, chiến đấu, chế tác công cụ, quan sát đồng đội và cảnh quan.
         - **20%–30% Front-Camera Selfie & Over-the-Shoulder (Cam trước 0.5x):** Dành riêng cho lúc an toàn, mở đầu/kết thúc tập, tâm sự với khán giả, hoặc phản ứng sốc/hú vía sau khi vượt qua hiểm nguy.
         - **10% Ground / Fixed Cam:** Camera tựa đá/mặt đất khi cần 2 tay rảnh hoàn toàn.
         - **CẤM TUYỆT ĐỐI 3 cảnh selfie liên tiếp.**
      2. **Khóa Im Lặng Khi Rình Mồi / Cận Chiến (Sonic Isolation — Rule 49 & 50):** 
         - Khi áp sát mục tiêu, phục kích, hoặc giao chiến sinh tử: BẮT BUỘC dùng First-Person POV và áp dụng **Sonic Isolation** (`Strictly NO spoken dialogue. Her mouth stays firmly closed in dead silence`). 
         - Âm thanh là Foley cơ học: tiếng thở nén qua mũi, tiếng tim đập, tiếng cành cây gãy, tiếng dã thú thở phì phò. Lời dẫn/suy nghĩ nội tâm nếu có chỉ đưa vào voiceover/subtitles hậu kỳ, miệng nhân vật KHÔNG được mấp máy.
      3. **Cánh tay khóa máy chỉ áp dụng cho shot Selfie:** Các bài học 25, 39, 50 về cánh tay duỗi thẳng giữ máy chỉ kích hoạt khi shot đó ĐÃ ĐƯỢC CHỌN là góc Selfie. Khi là shot First-Person POV, hai tay vlogger tự do tham gia hành động (cầm giáo, bò trườn, bám đá).


**Nội dung**
17. **[ĐÃ THAY bởi Rule 46 / bài học 60]** Vlogger mặc đồ hiện đại theo ảnh ref là chấp nhận được. Hiện tại: vlogger mặc trang phục thời kỳ ngay từ clip đầu qua `<Vlogger> Body` đã mặc outfit; đồ hiện đại chỉ khi user yêu cầu phong cách "lạc loài".
18. User có thể yêu cầu **cảnh mở đầu FPV điện ảnh** (từ không gian lao xuống toàn cảnh thành phố, không có vlogger), là ngoại lệ của luật "mọi shot quay bằng điện thoại". Clip đó dùng ảnh ref toàn cảnh, giữ yên 2–3 giây cuối, và clip sau mở bằng vật lướt qua ống kính để che cú cắt.
