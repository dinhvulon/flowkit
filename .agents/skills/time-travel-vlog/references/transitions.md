# Thư viện chuyển cảnh in-camera cho Time Travel Vlog

Nguyên tắc: mỗi chuyển cảnh = 2 clip được prompt khớp nhau. Clip A kết bằng một khung "che" (vật thể, gáy, nhòe), clip B mở từ đúng khung che đó. CapCut chỉ cắt thẳng tại khung che kín nhất.

## Cách nối 2 clip trong Google Flow (ghi rõ cách nào cho từng mối nối trong storyboard)
1. **Extend** — kéo dài clip A, prompt phần nối là "vật lướt qua / quay gáy → lộ ra nơi mới". Mượt nhất; hợp khi bối cảnh mới ở gần (cùng phố, cùng xưởng).
2. **Frames to Video** — xuất khung cuối clip A làm khung đầu clip B:
   `ffmpeg -sseof -0.1 -i A.mp4 -frames:v 1 A_last.png`
   Hợp khi cần đổi hẳn bối cảnh mà vẫn liền mạch.
3. **Tạo riêng rồi cắt** — 2 clip độc lập, mô tả khung đầu của B thật cụ thể; cắt tại khung che kín nhất. Nhanh nhất, mắt người không kịp thấy mối nối.

## Luật giấu mối nối (áp dụng cho mọi kỹ thuật)
- 1–2 giây cuối clip A và đầu clip B **không có thoại** — tránh cắt ngang câu.
- Giữ nguyên ánh sáng/giờ trong ngày giữa A và B; muốn đổi giờ thì dùng jump cut công khai.
- Hướng chuyển động ở A và B phải cùng chiều (trái→phải thì B cũng rời khung sang phải).
- Đầu clip B giữ vật che thêm ~3–5 khung hình trước khi mở ra — mắt đọc thành một chuyển động liên tục.
- J-cut: đưa âm thanh môi trường của B vào sớm ~0.5s trước điểm cắt; SFX "vút" nhẹ khi vật lướt qua.

## Ưu tiên theo video mẫu (dùng cho ~80% mối nối)

### A. Foreground wipe — vật thể lướt sát ống kính ⭐ dùng nhiều nhất
- Clip A kết: một vật lớn đi ngang sát ống kính che gần kín khung (súc gỗ phu khuân, tấm ván, bánh xe bò, thân ngựa, người đi ngang).
- Clip B mở: cùng loại vật đang rời khỏi khung, lộ ra nơi mới.
- Prompt A: "in the last 1.5 seconds two laborers carry a large wooden log right across the lens from left to right, almost filling the frame"
- Prompt B: "opens with a wooden log sliding out of frame to the right very close to the lens, revealing [new place]"
- Hướng di chuyển phải khớp giữa A và B.

### B. Look-away / back-of-head — quay gáy
- Clip A kết: nhân vật quay đầu nhìn thứ gì đó, camera thấy sau gáy/búi tóc chiếm khung.
- Clip B mở: từ sau gáy, nhân vật quay lại, bối cảnh đã là nơi khác (video mẫu dùng để reveal đại quân).
- Prompt A: "she turns her head away from the camera to look behind her, the back of her hair bun fills the frame"
- Prompt B: "opens on the back of her head, she turns around to face the camera revealing [new place] behind her"

### C. Swing / lia theo chuyển động
- Clip A kết: camera lia nhanh theo ngựa/xe đang chạy qua, nhòe chuyển động.
- Clip B mở: từ nhòe dừng lại ở cảnh mới.
- Prompt A: "a horse gallops past very close, the camera whips right following it, heavy motion blur fills the frame"
- Prompt B: "begins mid whip pan with heavy motion blur moving right, settling on [new place]"
- CapCut: cắt ở khung nhòe nhất, thêm SFX swish.

### D. Selfie → POV
- Nhân vật nói "look at this", clip sau là POV mắt nhân vật với tay cô lọt khung. Dùng cho beat xúc giác (đồ ăn, thẻ tre, tượng, kiếm).
- Prompt A: "she leans toward the camera, whispers 'look at this', and points past the lens"
- Prompt B: "first-person POV from her eye level, her own hands visible in the lower frame reaching for [object]"
- Không cần khung che — câu thoại + cử chỉ chỉ tay đã dẫn mắt người xem.

### E. Jump cut khi đi bộ
- Cùng nhân vật, cùng góc selfie, cùng hướng đi, bối cảnh ở clip B đã tiến lên. Cắt thẳng, không xử lý gì thêm — đúng chất vlog.

---
## Kỹ thuật bổ sung (dùng tiết chế)
Mỗi kỹ thuật gồm: khi nào dùng · khung cuối clip A · khung đầu clip B · câu prompt · xử lý CapCut.

## 1. Hand-over-lens (tay che ống kính)
- Dùng: chuyển địa điểm trong cùng thành phố; nhân vật "đi tiếp".
- A kết: lòng bàn tay nhân vật tiến sát, che kín ống kính, màn hình tối.
- B mở: bàn tay rút khỏi ống kính để lộ địa điểm mới.
- Prompt A (cuối): "in the final second she raises her palm toward the lens until it fully covers the camera, frame goes dark"
- Prompt B (đầu): "opens with a palm covering the lens, the hand pulls away to reveal [new place]"
- CapCut: cắt tại khung tối nhất, whoosh nhẹ.

## 2. Whip pan
- Dùng: "trong khi đó ở bên kia…", đổi chủ thể nhanh, nhịp chương năng lượng cao.
- A kết: camera quăng mạnh sang phải, nhòe chuyển động toàn khung.
- B mở: nhòe chuyển động từ trái, dừng lại ở cảnh mới.
- Prompt: "ends with a fast whip pan to the right, heavy motion blur" / "begins mid whip pan from the left with motion blur, settling on…"
- CapCut: cắt ở khung nhòe nhất; SFX swish. Hướng quăng phải khớp nhau.

## 3. Walk-through (xuyên cửa / màn / đám đông)
- Dùng: vào trong nhà, cung điện, quán; tạo cảm giác không gian liền mạch.
- A kết: nhân vật bước qua màn vải/cổng tối, camera ngập bóng tối hoặc vải.
- B mở: từ bóng tối/vải bước ra nội thất.
- Biến thể: người đi ngang sát ống kính (crowd wipe), cột gỗ, xe ngựa chạy qua.

## 4. Selfie flip (lật camera)
- Dùng: từ phản ứng của nhân vật → thứ nhân vật đang thấy (reveal). Đây là "chữ ký" của format.
- A: selfie, nhân vật nói "you guys… look at this", bắt đầu xoay điện thoại.
- B: POV camera sau, cảnh tượng lớn (Vạn Lý Trường Thành đang xây, đội quân), tay nhân vật hơi lọt khung.
- CapCut: cắt giữa cú xoay, thêm 2–3 khung motion blur.

## 5. Match cut (khớp hình)
- Dùng: nhảy thời gian/địa điểm có ý nghĩa; đẹp cho b-roll.
- Ví dụ: đồng tiền trong tay → mặt trời tròn trên thành; bát cháo khói bốc lên → khói lò rèn.
- Yêu cầu: vật thể cùng vị trí, cùng kích thước trong khung ở A (cuối) và B (đầu).

## 6. Time-skip (nhảy giờ)
- Dùng: "3 hours later…", "the next morning".
- Cùng góc/địa điểm, ánh sáng đổi (trưa → hoàng hôn → đuốc), nhân vật đổi trạng thái (mệt, lấm bụi).
- CapCut: jump cut + title "3 HOURS LATER" kiểu vlog, SFX tick.

## 7. Dust / smoke / light wipe
- Dùng: cảnh chiến trường, công trường, lò gốm; và **cú du hành thời gian**.
- A kết: bụi/khói/chớp sáng phủ kín khung. B mở: bụi tan ra.
- Du hành: A (hiện đại) ánh sáng trắng nuốt khung + điện thoại nhiễu sóng → B (cổ đại) sáng trắng tan, nhân vật nằm trên đất.

## 8. Phone glitch
- Dùng: nhắc người xem nhân vật đến từ tương lai; chuyển chương; cảnh "pin yếu".
- A kết: màn hình giật, sọc nhiễu. B mở: ổn định lại ở cảnh mới. Tốt nhất thêm bằng hiệu ứng CapCut (glitch) thay vì bắt Veo tạo.

## 9. Jump cut (cắt nhảy)
- Dùng: trong cùng phân đoạn — đúng chất vlog thật, không cần che.
- Giữ cùng bối cảnh, nhân vật hơi đổi vị trí/biểu cảm. Đừng cố làm mượt mọi thứ; vlog thật có jump cut.

## Bảng chọn nhanh
| Tình huống | Ưu tiên |
|---|---|
| Đi sang chỗ mới gần đó | Hand-over-lens, walk-through |
| Reveal cảnh hoành tráng | Selfie flip |
| Đổi chương | Whip pan, dust wipe, glitch |
| Nhảy giờ | Time-skip |
| Cảnh nghệ thuật / b-roll | Match cut |
| Trong một đoạn nói chuyện | Jump cut |
| Du hành thời gian | Light/dust wipe + glitch |
