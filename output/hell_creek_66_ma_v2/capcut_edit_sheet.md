# Bảng dựng CapCut Desktop — Hell Creek 66 Ma (v2) · Act 1
16:9 · 1920×1080 · **24 fps** · Thời lượng Act 1: **1:46.5** (độc lập) / **1:54.1** (kèm Cold Open) · Nhạc: Ambient Cinematic Dinosaur / Cretaceous Soundscape

> **Thông số kỹ thuật dự án (Lựa chọn đã chốt):**
> - **Khung hình & Tốc độ:** 16:9 ngang, 1920×1080, **24 fps** (bằng đúng fps gốc FlowKit, **không** đổi sang 30 fps tránh giật nhịp).
> - **Quy tắc cắt AI (Rule 49):** Các clip độc lập đặt điểm `in = 1.0s` để loại bỏ 1s khựng khung của mô hình AI. **Ngoại lệ:** Chuỗi va chạm nối frame `A1-12a, 12b, 12c` áp dụng Rule 65 (`PREV_LAST_FRAME`) giữ nguyên `in = 0.0s` để bảo toàn đà lao và phanh trượt!
> - **Phụ đề:** **Không burn phụ đề vào hình**. File `.srt` rời được quản lý riêng qua skill `/extract-capcut-srt`.
> - **Thẻ chữ:** Chỉ dùng thẻ năm, thẻ đếm ngược `HOUR X` và thẻ nhiệm vụ (Mission Card). Chữ đậm không chân, trắng viền đen, đặt giữa trên ~8% từ mép trên, hiển thị 2.5s.
> - **Âm thanh:** Thoại đỉnh −6 đến −12 dB (bật Normalize loudness trong CapCut); Nhạc nền −20 đến −24 dB dưới thoại; SFX đỉnh −18 đến −12 dB. Xuất file xong chuẩn hóa về **−14 LUFS / −1 dBTP** bằng ffmpeg loudnorm.
> - **Phím tắt CapCut Desktop (mặc định):** `Ctrl+B` (Split), `Q` (Ripple delete trái), `W` (Ripple delete phải), `Ctrl + lăn chuột` (Phóng to timeline), `←` / `→` (Đi từng khung hình).

---

## Phần 1: Phút đầu (Cold Open & Trailer Hook) — 0:00 – 1:00

*Mục tiêu retention:* Giữ chân người xem ở 30 giây đầu tiên (chỉ số **Intro** trong YouTube Studio). Đặt khoảnh khắc nguy hiểm / câu hỏi lớn nhất trước, giải thích sau. Tuyệt đối không chào hỏi, không logo mở màn, không xin subscribe.

| # | Clip ID | File nguồn local | Mốc cắt (in ➔ out) | Dài | TC Act 1 Standalone | TC Full Master | Hình đổi ở (Công thức Pro) | Chữ trên hình | Âm thanh (dB & Công thức) | Kiểu chuyển cảnh & Thao tác dựng |
|---|---|---|---|---|---|---|---|---|---|---|
| **0** | **CO** | `scene_MASTER` *(Dời mốc khi có file Act 4)* | 1.0 ➔ 8.0s | 7.0s | — | **0:00.0 ➔ 0:07.0** | 3.5s `[Zoom-CO]` 115% vào bùn và hạt thủy tinh li ti rơi | — | Thoại: −8 dB (`"¡Abajo, abajo, el aire está quemando!"`). Nhạc: dồn dập −16 dB. SFX: hạt thủy tinh lộp độp | **Cold Open**. Đoạn cao trào Act 4 gieo trước. Cắt cụt (Hard cut) ở 7.0s |
| **—** | **ĐEN** | Track phụ / Color solid đen | — | 0.6s | — | **0:07.0 ➔ 0:07.6** | — | — | Âm tắt lịm đột ngột. **SFX hit/boom trầm** (−8 dB, `[Fade]` out 0.3s) | **Smash cut to black**. Cắt cụt âm tạo khoảng lặng sốc |
| **1** | **EST-01** | `scene_000_EST-01_533b18b6_clean.mp4` | 1.0 ➔ 6.0s | 5.0s | **0:00.0 ➔ 0:05.0** | **0:07.6 ➔ 0:12.6** | `[Push]` Keyframe Scale 100% ➔ 106% lướt vào thung lũng | `66,000,000 YEARS AGO · HELL CREEK, MONTANA` (hiện 0.5 ➔ 3.0s của clip) | Không thoại. Nhạc ambient trầm hùng vào từ −22 dB (`[Fade]` in 1.0s). SFX: gió rít sớm, tiếng nước chảy | **J-cut**: Tiếng gió vào trước 0.3s. Toàn cảnh bình minh rạng đông (L0) thiết lập thế giới |
| **2** | **A1-01** | `scene_001_A1-01_ba9e7dd0_clean.mp4` | 1.0 ➔ 6.0s | 5.0s | **0:05.0 ➔ 0:10.0** | **0:12.6 ➔ 0:17.6** | 3.0s `[Punch]` 112% vào lưng sần cá sấu đang trôi sát | — | Sonic Isolation: Nora thở gấp qua mũi, nước bì bõm. Nhạc chìm xuống −24 dB | **Cắt thẳng (Match on direction)**. Lội nước ngang đùi, 2 dải lưng cá sấu Borealosuchus bơi tới |
| **3** | **A1-02** | `scene_002_A1-02_d4ffd8d5_clean.mp4` | 1.0 ➔ 8.0s | 7.0s | **0:10.0 ➔ 0:17.0** | **0:17.6 ➔ 0:24.6** | 4.0s `[Punch]` 112% + `[Gióng mắt]` khi nói punchline "paciencia" | `HOUR 0 — 12 HOURS REMAINING` (hiện 0.5 ➔ 3.0s của clip) | Thoại: đỉnh −8 dB (`"Okey. Ya salí... Lo que tenían era paciencia."`). Nhạc: −22 dB `[Duck]` dưới thoại | **Cut on look**. Nora quỳ trên sỏi ướt sũng. Bắt đầu đếm ngược 12 giờ trước thảm họa |
| **4** | **A1-04** | `scene_004_A1-04_6e65ed64_clean.mp4` | 1.0 ➔ 8.0s | 7.0s | **0:17.0 ➔ 0:24.0** | **0:24.6 ➔ 0:31.6** | 3.5s `[Zoom-CO]` 115% gia tốc vào bàn tay đặt trong vết răng | — | Thoại: đỉnh −8 dB (`"Miren el tamaño... Estoy parada en su cocina."`). SFX: ruồi bu, gió luồn xương | **Đổi cỡ cảnh (Macro ECU)**. Bàn tay lọt thỏm trong vết cắn T. rex. Gieo mối nguy T-Rex bằng hình |
| **5** | **A1-05** | `scene_005_A1-05_8b049391_clean.mp4` | 1.0 ➔ 8.0s | 7.0s | **0:24.0 ➔ 0:31.0** | **0:31.6 ➔ 0:38.6** | 3.5s `[Push]` Scale 100% ➔ 106% tăng dần cảm xúc cô độc | — | Thoại: đỉnh −8 dB (`"En doce horas ese cielo se incendia. Yo nada más vine a ver."`). Nhạc hạ −24 dB câu chốt | **Đổi cỡ cảnh (Selfie MS)**. Câu thoại cốt lõi xác lập niềm tin sai lầm: "Tôi chỉ đến xem thôi" |
| **6** | **A1-06** | `scene_006_A1-06_03c3325e_clean.mp4` | 1.0 ➔ 10.0s | 9.0s | **0:31.0 ➔ 0:40.0** | **0:38.6 ➔ 0:47.6** | **3.0s** `[Punch]` 112% (nhấn chìm mai rùa); **6.0s** `[Zoom-CO]` 115% (lia lên hốc khô bờ xa) | — | Thoại: đỉnh −7 dB (`"Caparazón de tortuga... Hay un hueco seco allá. Cocodrilos justo abajo."`) | **Cắt thẳng (POV MS)**. Gieo bình mai rùa (sẽ vỡ ở Act 3) + gieo hốc khô sinh tồn (payoff Act 4) |
| **7** | **A1-07** | `scene_007_A1-07_dd501c45_clean.mp4` | 1.0 ➔ 8.0s | 7.0s | **0:40.0 ➔ 0:47.0** | **0:47.6 ➔ 0:54.6** | 3.5s `[Punch]` 110% vào chi tiết nút buộc sợi cọ | — | Thoại: đỉnh −8 dB (`"Fibra de palma torcida... Si este nudo se suelta..."`). Nhạc nền duy trì −22 dB | **Đổi cỡ cảnh (Fixed MS)**. Kê máy trên gỗ trôi, buộc mai rùa vào hông trái. Gieo chi tiết nút sẽ đứt |
| **8** | **A1-08** | `scene_008_A1-08_f2fbb6e2_clean.mp4` | 1.0 ➔ 8.0s | 7.0s | **0:47.0 ➔ 0:54.0** | **0:54.6 ➔ 01:01.6** | 3.5s `[Push]` Scale 100% ➔ 107% lia vào miệng hành lang thú | — | Thoại: đỉnh −8 dB (`"Este bosque es un muro sólido... Y algo muy grande lo abrió."`). SFX: cành gãy xa | **Cut on look**. Lia từ bìa rừng sang hành lang thú bùn xám bị giẫm nát. Đặt câu hỏi: "Cái gì to mở lối?" |

---

## Phần 2: Timeline chi tiết toàn bộ Act 1 (0:54.0 – 1:46.5 Standalone / 01:01.6 – 01:54.1 Master)

*Tiến triển nhanh (Fast Pacing):* Hành lang thú ➔ Phát hiện dấu chân khổng lồ ➔ Chạm trán đàn Triceratops ➔ Bò Đực dọa húc (Chuỗi va chạm 3 mắt xích liên tục `PREV_LAST_FRAME`) ➔ Thoát chết & Thiết lập Mission Card ngồi chờ.

| # | Clip ID | File nguồn local | Mốc cắt (in ➔ out) | Dài | TC Act 1 Standalone | TC Full Master | Hình đổi ở (Công thức Pro) | Chữ trên hình | Âm thanh (dB & Công thức) | Kiểu chuyển cảnh & Thao tác dựng |
|---|---|---|---|---|---|---|---|---|---|---|
| **9** | **A1-09** | `scene_009_A1-09_e8a7080e_clean.mp4` | 1.0 ➔ 8.0s | 7.0s | **0:54.0 ➔ 01:01.0** | **01:01.6 ➔ 01:08.6** | 3.5s `[Zoom-CO]` 115% gia tốc vào mũi giày so vết chân | — | Thoại: đỉnh −8 dB (`"Huella redonda... Lo que la hizo está cerca."`). SFX: nước đục sóng sánh | **Đổi cỡ cảnh (Macro ECU)**. Dấu chân khổng lồ rộng hơn vai, nước đục còn rung. Cảnh báo mối nguy cận kề |
| **10** | **A1-10** | `scene_010_A1-10_5e72915f_clean.mp4` | 1.0 ➔ 8.0s | 7.0s | **01:01.0 ➔ 01:08.0** | **01:08.6 ➔ 01:15.6** | 4.0s `[Punch]` 112% vào 3 con Triceratops đang ăn | — | Thoại: thì thầm −9 dB (`"Ahí. Son tres, con cuernos... Grande quiere decir seguro, ojalá."`). Nhạc: −23 dB | **Cut on look (OTS MS)**. Nora nấp sau bụi lá thì thầm, đàn 3 con ở hậu cảnh. Gieo nghi ngờ: "Hy vọng thế" |
| **11** | **A1-S1** | `scene_011_A1-S1_1e61b7d2_clean.mp4` | 1.0 ➔ 8.0s | 7.0s | **01:08.0 ➔ 01:15.0** | **01:15.6 ➔ 01:22.6** | 3.5s `[Punch]` 112% + `[Gióng mắt]` khi Nora cười chốt | — | Thoại: đỉnh −8 dB tự tin (`"Okey, son enormes, pero solo comen plantas... Nada más miren."`) | **Đổi cỡ cảnh (Selfie MCU)**. Nora chủ quan bước ra khỏi bụi rậm. Điểm rơi tâm lý trước cú sốc |
| **12** | **A1-11** | `scene_012_A1-11_56d05221_clean.mp4` | 1.0 ➔ 6.0s | 5.0s | **01:15.0 ➔ 01:20.0** | **01:22.6 ➔ 01:27.6** | 3.0s `[Zoom-CO]` 115% vào mắt & sừng gãy Bò Đực | — | Sonic Isolation hoàn toàn: không thoại, tiếng nhai dừng bặt, tiếng thở phì mũi nặng trịch. Nhạc tắt lịm về 0 | **Match on action (POV WS)**. Bước ra trảng cỏ; Bò Đực ngẩng đầu chậm, diềm cổ ửng đỏ. Im lặng trước bão tố |
| **13** | **A1-12a**| `scene_013_A1-12a_e18bf361_clean.mp4` | **0.0 ➔ 3.5s** *(Rule 65)* | 3.5s | **01:20.0 ➔ 01:23.5** | **01:27.6 ➔ 01:31.1** | Không zoom. Chuyển động thực của Bò Đực lao tới choán nửa khung hình | `HOUR 1 — 11 HOURS REMAINING` (hiện 0.2 ➔ 2.2s của clip) | Không thoại. SFX: bước chân rầm rập rung chuyển đất, tiếng gầm gừ đục ngầu cực đại (−6 dB). Không nhạc | **Hard cut (Chuỗi 4s 1/3 - Lao)**. Giữ nguyên frame 0.0s nối 100% với A1-11. Bò Đực hạ sừng lao 3 bước vũ bão! |
| **14** | **A1-12b**| `scene_014_A1-12b_6ef6dca6_clean.mp4` | **0.0 ➔ 3.5s** *(Rule 65)* | 3.5s | **01:23.5 ➔ 01:27.0** | **01:31.1 ➔ 01:34.6** | Không zoom. Bùn đất tung văng thẳng vào ống kính máy quay | — | Không thoại. SFX: tiếng chân cào bùn phanh trượt khét lẹt, tiếng thở khè dữ dội (−6 dB) | **Hard cut (Chuỗi 4s 2/3 - Phanh)**. Khớp 100% frame cuối 12a. Bò Đực phanh dẫm bùn cách 6m dằn mặt! |
| **15** | **A1-12c**| `scene_015_A1-12c_4b674781_clean.mp4` | **0.0 ➔ 3.5s** *(Rule 65)* | 3.5s | **01:27.0 ➔ 01:30.5** | **01:34.6 ➔ 01:38.1** | Khung hình rung chấn mạnh lật ngửa lên tán lá non | — | Thoại: Tiếng thét vỡ giọng của Nora trong lúc ngã (`"¡Aaaagh!"` đỉnh −6 dB). SFX: cành lá gãy rôm rốp | **Hard cut (Chuỗi 4s 3/3 - Ngã)**. Khớp 100% frame cuối 12b. Máy ngã bật ngửa vào bụi rậm, lật lên tán lá non |
| **16** | **A1-13** | `scene_016_A1-13_a841469a_clean.mp4` | 1.0 ➔ 8.0s | 7.0s | **01:30.5 ➔ 01:37.5** | **01:38.1 ➔ 01:45.1** | 3.5s `[Punch]` 112% + `[Gióng mắt]` khi Nora thốt lên "Híjole" | — | Thoại: đỉnh −8 dB (`"Se detuvo a seis metros... Okey, mensaje recibido, grandote. Híjole."`). Nhạc vào nhẹ −24 dB | **Cắt thẳng khớp ráng lá (Selfie MCU)**. Nora nằm thở dốc trong bụi, lá vắt ngang má, dry humor giải tỏa |
| **17** | **A1-14** | `scene_017_A1-14_00a04296_clean.mp4` | 1.0 ➔ 10.0s | 9.0s | **01:37.5 ➔ 01:46.5** | **01:45.1 ➔ 01:54.1** | **3.5s** `[Punch]` 110% (biểu cảm kiên nhẫn); **7.0s** `[Push]` 100% ➔ 105% nhấn mạnh quyết tâm "Y espero" | `MISSION: EARN ACCEPTANCE — DO NOT MOVE` (hiện 6.0 ➔ 8.5s của clip) | Thoại: đỉnh −8 dB (`"Entonces no puedo entrar ahí... Me siento acá en la orilla... Y espero."`). Nhạc: −22 dB | **Đổi cỡ cảnh (Fixed OTS Vlog 3/4)**. Nora ngồi bệt tựa gốc cây kiên nhẫn, đàn ở hậu cảnh. Đóng Act 1 |

---

## Phần 3: Kế hoạch cắt 4 Video Shorts (9:16) từ Footage Act 1

*Chiến lược 4 (Kéo Traffic):* Tận dụng các pha cao trào để đăng Shorts YouTube nhằm thu hút tệp khán giả đam mê khủng long và sinh tồn. Tất cả các clip dọc đều được crop từ bản 16:9 gốc trong CapCut Desktop (Menu Modify ➔ Ratio: 9:16, Scale ~316%).

### Short 1: "Cú dọa húc của Quái thú 10 tấn" (The 10-Ton Charge)
- **Mục tiêu:** Viral triệu view nhờ cú lao nghẹt thở và cú phanh trượt bùn chuẩn vật lý.
- **Nguồn footage:** `A1-11` (2s cuối: 4.0 ➔ 6.0s) + `A1-12a` (3.5s) + `A1-12b` (3.5s) + `A1-12c` (3.5s) + `A1-13` (3.5s đầu: 1.0 ➔ 4.5s).
- **Tổng thời lượng:** **16.0 giây**.
- **Hook giây đầu:** 0:00 mở ngay giữa cú ngẩng đầu diềm ửng đỏ và tiếng bước chân dậm đất lao tới (`A1-12a`).
- **Reframe 9:16 trong CapCut:**
  - Scale: **316%**.
  - `Position X`: Canh giữa trúng đầu và chiếc sừng trái gãy cụt của Bò Đực.
  - Ở đoạn ngã (`A1-12c ➔ A1-13`): Dời `Position Y` hơi chúc xuống để ôm trọn biểu cảm thở dốc của Nora trong bụi rậm.
- **Điểm kết (Loop):** Câu thoại chốt của Nora: *"Okey, mensaje recibido, grandote"* ➔ Cắt cụt (Hard cut) nối vòng tròn lại cú lao giây đầu (`[Loop]`).

### Short 2: "Rơi vào bẫy cá sấu 66 triệu năm trước" (Trapped with Ancient Crocodiles)
- **Mục tiêu:** Kích thích sự tò mò và thót tim ở giây đầu tiên.
- **Nguồn footage:** `A1-01` (1.0 ➔ 5.0s: 4.0s) + `A1-02` (1.0 ➔ 8.0s: 7.0s).
- **Tổng thời lượng:** **11.0 giây**.
- **Hook giây đầu:** Bàn chân lội nước bùn, hai dải vảy lưng cá sấu Borealosuchus bơi xé nước áp sát.
- **Reframe 9:16 trong CapCut:**
  - Scale: **316%**.
  - Clip 1: Canh giữa vào hai con cá sấu.
  - Clip 2: Pan sang khuôn mặt ướt sũng của Nora đang ngồi thở phào trên bãi sỏi.
- **Điểm kết:** Nora cười trừ nói câu punchline: *"Lo que tenían era paciencia"* (Thứ chúng có... là sự kiên nhẫn!).

### Short 3: "Đặt tay vào vết răng T-Rex" (Inside a T-Rex Bite Mark)
- **Mục tiêu:** Thể hiện độ chân thực khoa học và quy mô khổng lồ của kẻ săn mồi đỉnh chóp.
- **Nguồn footage:** `A1-04` (1.0 ➔ 8.0s: 7.0s) + `A1-05` (1.0 ➔ 5.0s: 4.0s).
- **Tổng thời lượng:** **11.0 giây**.
- **Hook giây đầu:** Bàn tay Nora lọt thỏm hoàn toàn vào rãnh răng cưa trên xương chậu khủng long.
- **Reframe 9:16 trong CapCut:**
  - Scale: **316%**.
  - Khóa chặt `Position` vào lòng bàn tay và rãnh răng sâu hoắm.
- **Điểm kết:** Chuyển sang Nora đứng nhìn bao quát bãi sỏi: *"Estoy parada en su cocina"* (Tôi đang đứng ngay trong nhà bếp của nó).

### Short 4: "Mẹo sinh tồn: Bình nước mai rùa" (Turtle Shell Canteen Hack)
- **Mục tiêu:** Nội dung "mẹo sinh tồn kỳ lạ" giữ chân người xem cực tốt.
- **Nguồn footage:** `A1-06` (1.0 ➔ 7.0s: 6.0s) + `A1-07` (1.0 ➔ 8.0s: 7.0s).
- **Tổng thời lượng:** **13.0 giây**.
- **Hook giây đầu:** Nhặt mai rùa khô rỗng, ấn chìm xuống mép nước trong vắt để nước tràn vào đầy ắp.
- **Reframe 9:16 trong CapCut:**
  - Scale: **316%**.
  - Canh bám vào đôi bàn tay thao tác luồn dây sợi cọ buộc vào đai ngực.
- **Điểm kết:** Câu cảnh báo hài hước: *"Si este nudo se suelta, me toca beber del charco de cocodrilos"* (Nếu nút này đứt, tôi sẽ phải uống chung vũng với cá sấu!).

---

## Phần 4: Quy trình thao tác nhanh trong CapCut Desktop (Step-by-Step)

1. **Chuẩn bị Dự án:**
   - Mở CapCut Desktop ➔ **New project** ➔ Đặt tên: `Hell_Creek_Act1`.
   - Chọn tỷ lệ khung hình (dưới màn hình Preview): **16:9** (hoặc 9:16 khi làm Shorts).
   - Menu trên cùng: **Menu ➔ Settings ➔ Edit** ➔ Đặt **Frame Rate: 24 fps**.
2. **Kéo thả Footage vào Timeline:**
   - Import toàn bộ 17 files video sạch từ thư mục: `output/hell_creek_66_ma_v2/scenes/` (các file có đuôi `_clean.mp4`).
   - Sắp xếp thứ tự các clip trên track chính (Main Track) đúng theo thứ tự bảng ở Phần 2 (`EST-01` ➔ `A1-14`).
   - Bật nút **Magnet (Nam châm)** trên thanh công cụ timeline (`[Nam châm]`) để các clip tự hít chặt vào nhau, không bị khe hở đen 1 khung hình.
3. **Cắt gọt (Trimming) chính xác từng khung:**
   - Dùng phím `Ctrl + lăn chuột` để phóng to timeline (`[Frame]`).
   - Với các clip độc lập: Di chuyển đầu phát đến `00:01:00` (giây 1.0) ➔ bấm phím `Q` để gọt bỏ 1s đầu bị giật. Di chuyển đến mốc `out` ➔ bấm phím `W` để gọt phần đuôi thừa.
   - **Lưu ý chuỗi `A1-12a, 12b, 12c`:** Tuyệt đối **KHÔNG** bấm `Q` ở đầu clip! Giữ nguyên từ `00:00:00` để các khung hình nối khớp 100% không bị nhảy vị trí.
4. **Áp dụng Đổi hình (Zoom & Punch-in):**
   - Tìm đến mốc giây ghi trong cột "Hình đổi ở":
     - Nếu là `[Punch]`: Đặt đầu phát ➔ bấm `Ctrl+B` để chia clip ➔ chọn nửa clip sau ➔ ở bảng **Video ➔ Basic**, kéo **Scale lên 110% – 112%**. Bật đường gióng mắt (`[Gióng mắt]`) để chỉnh lại `Position Y` sao cho tầm mắt nhân vật giữ nguyên vị trí.
     - Nếu là `[Push]`: Đặt đầu phát ở đầu clip ➔ bấm icon Keyframe bên cạnh Scale (100%) ➔ di chuyển đầu phát đến cuối clip ➔ kéo Scale lên 106%.
     - Nếu là `[Zoom-CO]`: Đặt Keyframe 1 ở Scale 100% ➔ bấm `Shift + →` 2 lần (~20 khung hình) ➔ đặt Keyframe 2 ở Scale 115% ➔ chuột phải vào Keyframe 2 trên timeline chọn đường cong **Cubic Out**.
5. **Chèn Thẻ chữ (Cards):**
   - Vào tab **Text ➔ Add text ➔ Default text**.
   - Chọn font: **Montserrat / Arial / Helvetica** (In hoa, Bold, màu trắng).
   - Bật mục **Stroke (Viền):** Chọn màu đen, độ dày (Thickness) ~25.
   - Kéo vị trí chữ lên giữa trên (~8% từ mép trên màn hình).
   - Cắt độ dài thanh chữ đúng **2.5 giây**.
   - Bấm **Save as preset** (`[Preset chữ]`) để các thẻ sau chỉ cần kéo ra và gõ lại nội dung.
6. **Cân chỉnh Âm thanh (Audio Mixing):**
   - Chọn tất cả các clip video trên timeline ➔ ở bảng **Audio ➔ Basic**, tích chọn **Normalize loudness** (CapCut sẽ tự động cân bằng âm lượng các đoạn thoại về mức chuẩn).
   - Đoạn có thoại: Kéo slider Volume của track nhạc nền xuống mức **−20 dB đến −24 dB**.
   - Ở các câu chốt kịch tính (A1-05, A1-11, A1-12a): Thêm 4 keyframe âm lượng trên track nhạc nền để hạ nhạc (`[Duck]`) hoặc kéo về −∞ dB (`[Fade]`) trước khi Bò Đực lao tới.

---

## Phần 5: Checklist kiểm tra sau khi xuất file (Export Quality Gate)

- [ ] **Tốc độ khung hình (FPS):** Xuất đúng **24 fps**, độ phân giải **1080p (1920×1080)**, định dạng **MP4 (H.264)**, Bitrate Recommended/Higher.
- [ ] **Kiểm tra 30 giây đầu:** Mở đầu cuốn hút với mối nguy cá sấu và câu đố vết cắn T. rex; không có logo thừa, không chào hỏi lan man.
- [ ] **Nhịp đổi hình:** Không có đoạn nào hình đứng yên quá 5 giây; các cú zoom (`[Punch]`, `[Push]`) đều phục vụ cảm xúc nhân vật và bối cảnh.
- [ ] **Chuỗi va chạm `A1-12a/b/c`:** Kiểm tra bằng phím `←` / `→` từng khung hình xem Bò Đực có bị nhảy vị trí hay biến dạng sừng hay không (nhờ Rule 65 nối frame, chuyển động phải mượt như một cú máy quay liền mạch).
- [ ] **Thoại và Nhạc:** Lời thoại tiếng Tây Ban Nha của Nora nghe rõ ràng, tự nhiên trên nền nhạc và âm thanh rạch suối; không bị tiếng nhạc đè lấp.
- [ ] **Chuẩn hóa Âm lượng YouTube (−14 LUFS):**
  Sau khi xuất file `final_act1.mp4`, mở Terminal chạy lệnh ffmpeg sau để chuẩn hóa độ lớn âm thanh theo chuẩn YouTube:
  ```bash
  ffmpeg -i final_act1.mp4 -af loudnorm=I=-14:LRA=11:TP=-1.0 -c:v copy -c:a aac -b:a 192k -ar 48000 final_act1_14lufs.mp4
  ```
  Kiểm tra lại độ lớn bằng lệnh:
  ```bash
  ffmpeg -i final_act1_14lufs.mp4 -af ebur128=peak=true -f null - 2>&1 | tail -12
  ```
  *(Dòng `I:` hiển thị xấp xỉ `-14.0 LUFS` và `Peak` không vượt quá `-1.0 dB` là đạt chuẩn 100%)*.
