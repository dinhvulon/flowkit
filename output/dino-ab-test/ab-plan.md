# Dino A/B test — luật chuyển động mới vs skill cũ (HEAD)

- Project: Neanderthal 51ka v6 `b9910e52-78cb-40c1-aff1-68b0c3a19f64`
- Video: `e67f1d20-a0b8-4ab4-83a5-f250184be7bf` (HORIZONTAL)
- Scene A (skill hiện tại): `50dacb2b-64e9-4c54-926a-7f8256d361d6` — `prompt_A.json`
- Scene B (skill HEAD): `c35629c2-ccf7-4a51-94c2-fca333cc938d` — `prompt_B.json`
- Giống nhau: thoại 24 từ, 10s, ref `Nora` + `Nora Body`, bối cảnh, mô tả khủng long, audio, ràng buộc.

## Khác nhau (biến được test)

| Luật | A | B |
|---|---|---|
| Dòng 42 điểm tựa | gối phải ấn đất, bốt trái đặt phẳng, cẳng tay trái tựa thân gỗ "for the whole clip"; mỗi bước chân khủng long đặt + in dấu | chỉ "kneels behind the log", tay trái đặt trên gỗ |
| Dòng 43 frame 0 trước hành động | khủng long đầu ngẩng, mỏ khép, chưa ăn, lá dương xỉ còn nguyên | chỉ ghi vị trí |
| §8 Reveal vs Pop in | "steps out from behind the fern clump (reveal)" | "pops out ... with a crisp elastic rebound (pop in)" |
| Dòng 44 chừa 0.5s | xé lá xong trước ~9.5s, 0.5s cuối giữ yên nhai | ngẩng đầu nhìn ống kính đúng lúc hết clip |

## Chấm khi review (mỗi clip, 4 fps)

1. Nora có lơ lửng / trượt / đổi tư thế quỳ không (dòng 42)
2. Khủng long có mọc ra / nảy bật / biến dạng khi bước ra khỏi lùm dương xỉ không (§8)
3. Giây 0 đúng trạng thái chưa ăn không; có lá bị xé sẵn không (dòng 43)
4. Động tác cuối bị cắt ngang hay xong trọn (dòng 44)
5. Chân khủng long trượt / trôi; Nora nói hết câu; thoại khớp miệng
6. Điểm tổng theo rubric 6 tiêu chí (ngưỡng giữ ≥ 9)

## Kết quả (1 mẫu mỗi bản, 2026-10-11)

| Tiêu chí | A (skill mới) | B (skill HEAD) |
|---|---|---|
| Frame 0: khủng long sau bụi dương xỉ, chưa ăn | Đạt | **Trượt**: đứng ngoài trống từ giây 0 |
| Bước ra khỏi bụi (reveal / pop in) | Đạt, bước ra tự nhiên, không nảy bật | Không xảy ra (đã ở ngoài từ đầu) |
| Chân khủng long trượt / trôi | Không | Không |
| Trang phục Nora (quần bó che chân) | Đạt | **Lỗi**: lộ da đùi + đầu gối (lặp lỗi Bài học 78) |
| Tay trái neo trên khúc gỗ | **Không đạt**: tay khua theo lời nói, đặt lên gối | Phần lớn đặt trên gỗ |
| Giật chuyển động | Đầu khủng long quay ngoắt 8.1–8.3s | Không thấy |
| Thoại kết thúc (silencedetect) | ~9.35s | ~9.50s |
| Động tác cuối bị cắt | Không, 0.5s cuối giữ yên nhai | Không, ngẩng nhìn ống kính trọn |
| Màu quần so với ảnh Body (da lộn nâu vàng) | Che kín nhưng nâu sẫm, lệch màu | Bốt + màu đúng nhưng hở đùi |
| Khủng long đúng tuổi "con non", sừng ngắn cong ra sau | Không: to như con trưởng thành, sừng dài chĩa trước | Có: nhỏ hơn, sừng ngắn |
| Điểm ước tính (6 tiêu chí) | ~8.5 | ~7.6 |

Cả hai dưới ngưỡng giữ 9. Một mẫu mỗi bản: chỉ là xu hướng, chưa phải kết luận.

## Clip C — rượt đuổi (skill mới, scene `18e6e4c7-18d4-41c5-a9ec-f6c1028eb73e`)

| Tiêu chí | Kết quả |
|---|---|
| POV ngoái ra sau suốt clip | **Lỗi**: góc nhìn về phía trước, bạo chúa ở phía trước, hai con lao vào nhau |
| Người cưỡi giữ trên lưng thú | **Lỗi**: ~8.1s đầu gối Nora biến mất, khung tách khỏi lưng, Triceratops thành con riêng đi về phía bạo chúa |
| Bạo chúa dừng ở khe cây | **Lỗi**: đi tiếp, áp sát mặt Triceratops 8.5–9s (gần chạm) |
| Tiếng gầm 3.5–5s lúc Nora im | Đạt (3.75–4.75s) |
| Quần cùng màu áo, che kín gối | Đạt |
| Thân cây vào từ cạnh khung | Đạt |
| Cỡ bạo chúa so với Triceratops | Đạt |
| Điểm ước tính | ~6 (không giữ) |

## Clip D — máy cố định nhìn ngang, có ref 2 khủng long (scene `e03cb8e3-987f-4de8-9a3c-aa272e4f73df`)

| Tiêu chí | Kết quả |
|---|---|
| Chất liệu da, khối lượng bạo chúa | Đạt: da mờ đóng bùn, đi nặng, bùn văng ~7.75s |
| Khớp ref (Triceratops con, bạo chúa) | Đạt |
| Trang phục Nora khớp Body | Đạt: quần cùng màu, bốt, tay áo dài; hai tay giữ diềm |
| Tiếng gầm lúc Nora im | Đạt (3.75–4.75s) |
| Triceratops băng qua khung | **Lỗi**: chạy tại chỗ, thân gần như không tiến |
| Khe cây để thoát | **Lỗi**: cây thành hậu cảnh, không có khe trên đường |
| Bạo chúa khựng trước khe | **Lỗi**: tới sát sau lưng Nora, đầu ở trên cô 7–10s (không chạm) |
| Điểm ước tính | ~7 (C ~6) |
