# Chuyển cảnh trong CapCut Desktop

Mỗi mối nối trong Bảng dựng ghi tên một kiểu bên dưới. Phần này nói cách làm kiểu đó trong CapCut (giao diện tiếng Anh, phím mặc định).

Mục lục: 1. Luật chung · 2. Kiểu dùng được cho vlog POV · 3. Video thường: tab Transitions · 4. Chọn kiểu nào

## 1. Luật chung — cú cắt "vô hình"

- **Cắt trong lúc đang chuyển động**: đầu đang quay, tay đang vung, máy đang lia. Mắt bám theo chuyển động nên không thấy mối nối. Cắt khi mọi thứ đã đứng yên thì mối nối lộ ra.
- **Chọn khung bằng `←` / `→`** (1 khung = 1/24s). Lệch 2–4 khung là khác biệt giữa mượt và giật. Sửa mối nối bằng cách dời khung cắt, không thêm hiệu ứng.
- **Âm thanh dẫn hình**: J-cut (âm cảnh sau vào trước) và L-cut (âm cảnh trước kéo qua) làm mối nối trôi hơn bất kỳ hiệu ứng hình nào.
- **Whoosh chỉ đi với cú cắt có chuyển động.** Cắt tĩnh gắn whoosh nghe như template. Chỗ to nhất của whoosh đặt đúng khung cắt (đầu whoosh vào sớm ~0.2s), −10 dB.
- Giữ mắt nhân vật cùng một vị trí khung qua mối nối [Gióng mắt].
- **Vlog POV (FlowKit)**: không mở tab Transitions, không crossfade, không dip-to-black. Ngoại lệ là CUT ĐEN ở cold open và kết. Glitch chỉ khi user yêu cầu (`fk-time-travel-vlog/references/transitions.md`).

## 2. Kiểu dùng được cho vlog POV

| Kiểu | Khi nào | Làm trong CapCut |
|---|---|---|
| **Smash cut to black** | Cold open, đỉnh căng nhất → bỏ lửng | Cắt ở khung bị che nhiều nhất (cành, tay, bụi). Sau đó clip đen 0.4–0.8s (`assets/black_2s_1080p24.mp4` hoặc Media → Library → tìm "black"). Âm clip trước **tắt cụt**, không fade. SFX `impact`/`boom` trầm ở khung đầu màn đen, −8 dB, Fade out 0.3s |
| **J-cut** | Vào cảnh mới, nhất là sau màn đen | Chuột phải clip sau → **Separate audio** → kéo mép trái track âm sang trái 0.2–0.5s (cần phần đầu đã trim, vd. 1.0s Rule 49) → Fade in 0.2–0.3s |
| **L-cut** | Tiếng nền cảnh trước nên kéo dài (nước, gió, đám đông) | Separate audio của clip trước → kéo mép phải track âm dài thêm 0.3–0.8s sang clip sau → Fade out bằng độ dài đó |
| **Speed ramp in** | Flycam hoặc cảnh không người lao về một điểm | Đầu phát ở chỗ bắt đầu tăng tốc → `Ctrl+B` → đoạn sau: **Speed → Normal** 1.5–2.5×, hoặc **Speed → Curve → Custom** kéo điểm cuối lên. Cắt ở khung nhòe nhất, không đợi khung cuối. Thêm whoosh. Không làm chậm clip AI có mặt hoặc tay người |
| **Whip / swing** | Selfie lia nhanh sang hướng khác, máy vung | Cắt ở khung nhòe nhất của cú lia, clip sau mở cũng đang nhòe (cắt bỏ phần đầu cho tới khung nhòe). Whoosh. Không lật cam trước/sau trong 1 shot (Rule 42); giữa 2 shot thì được |
| **Cut on look** | Nhân vật nhìn sang → cảnh sau là thứ họ thấy | Tìm khung đầu bắt đầu quay đầu → thêm 4–6 khung → `W`. Không SFX |
| **Cut on point / gesture** | Ai đó chỉ hoặc đưa vật → cảnh sau là vật đó | Khung tay duỗi hết + 2–3 khung → `W` |
| **Match on action / hướng** | Cùng một chuyển động hoặc hướng đi ở 2 clip | Cắt giữa bước chân / giữa động tác ở clip A; clip B mở cùng pha động tác. Kiểm tra cùng chiều trái–phải (Rule 44) |
| **Foreground wipe** | Vật che kín ống kính (cây, người đi ngang, tay) | Cắt ở khung che kín nhất; clip sau mở trên khung đang che (nếu có) hoặc cắt thẳng |
| **Đổi cỡ cảnh** | Cùng không gian, rộng ↔ cận | Cắt thẳng sau câu thoại + 4–6 khung. Đổi cỡ phải rõ (cận → toàn), lệch ít trông như lỗi jump |
| **Jump cut** | Cắt bớt trong cùng một shot nói chuyện | `Ctrl+B` 2 chỗ → xóa giữa → đoạn sau [Punch] 110% để che bước nhảy |
| **Silence → hit** | Trước cú dọa / cú đánh | 0.3–0.5s cuối clip trước: Fade out tiếng nền, keyframe nhạc tụt sâu. Clip sau: `impact` ở khung đầu, tiếng gốc 100% |
| **Time-skip** | Nhảy thời gian trong ngày | Cắt thẳng + card countdown (nếu có). Không dissolve |

## 3. Video thường (không phải vlog POV): tab Transitions

Được dùng nhưng tiết chế:
1. Thanh trên → **Transitions** → tìm `blur`, `zoom`, `whip`, `pull in`, `slide`.
2. Kéo thả vào giữa 2 clip trên timeline.
3. Bảng phải → **Duration ≤ 0.3s**. Dài hơn sẽ trông như slideshow.
4. Muốn áp cho mọi mối nối: **Apply to all**. Đừng làm vậy; chỉ dùng ở mối nối đổi phần hoặc đổi địa điểm, còn lại cắt thẳng.
5. Tránh 3D cube, page turn, các kiểu "lật trang". Kênh nhỏ dùng các kiểu này trông nghiệp dư.

Transition kéo dài clip cần phần thừa ở 2 đầu. Nếu CapCut báo thiếu, trim mỗi clip 0.3s.

## 4. Chọn kiểu nào — thứ tự thử

1. Có chuyển động sẵn trong hình (quay đầu, chỉ, lia, che)? → kiểu tương ứng ở §2.
2. Không có, nhưng âm thanh nối được? → J-cut hoặc L-cut.
3. Cùng không gian? → đổi cỡ cảnh hoặc jump cut + [Punch].
4. Đổi không khí đột ngột (sợ → tò mò, ồn → lặng)? → cắt thẳng. Sự tương phản tự là chuyển cảnh.
5. Video thường, đổi phần → tab Transitions ≤ 0.3s.
