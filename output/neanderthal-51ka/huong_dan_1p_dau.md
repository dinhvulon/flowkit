# Hướng dẫn dựng phút đầu — neanderthal-51ka (CapCut Desktop)

Bản này dựng được **ngay hôm nay** bằng clip đã có trong `1080/` (C01–C10). Nó khác phần "Intro trailer" trong `capcut_edit_sheet.md`, vốn cần 13 clip chưa sinh.

Vì sao bản này mở đầu tốt:
- Cold open → CUT ĐEN → card năm → mission card ở **0:54**, trước mốc 1:00.
- Người xem biết "khi nào, ở đâu" ở 0:06 (card năm) và cái giá ở 0:15–0:20 ("Ten seconds in. Soaked." + countdown 24 giờ).
- Mốc **0:30**, chỗ YouTube đo key moment Intro, rơi đúng lúc Thủ Lĩnh chồm vào mặt Nora.

Cách đọc giờ:
- "nguồn 6.5" = giây 6.5 của file clip gốc.
- "TL 0:05.5" = vị trí trên timeline.
- Tên trong ngoặc vuông là công thức ở `skills/fk-capcut-edit/references/pro-recipes.md`.

---

## Bước 0 — Chuẩn bị (5 phút)

1. CapCut → **Create project**. Bảng phải (khi chưa chọn gì) → **Ratio 16:9**.
2. Media → **Import**:
   - Thư mục `output/neanderthal-51ka/1080/`: lấy `scene_01` … `scene_10`. Scene 09 lấy bản **`93a7f623`**.
   - File `output/neanderthal-51ka/assets/black_2s_1080p24.mp4`: clip đen 2s, 24 fps, mình đã tạo sẵn cho các cú CUT ĐEN.
3. Bật **nam châm (Magnet)** trên thanh công cụ timeline.
4. Kéo lần lượt vào track chính: C01, black, C02, C03, C04, C05, C06, C07, C08, C09, C10.
5. Phóng to timeline bằng `Ctrl` + lăn chuột cho tới khi thấy từng khung hình. `←` / `→` đi 1 khung; 24 khung = 1 giây.

**Cách cắt đúng giây nguồn:**
- Bấm vào clip, đưa đầu phát về đúng mép trái clip (nam châm sẽ hít vào).
- Đi tới số giây cần cắt: nhìn đồng hồ trên Player, hoặc bấm `→` đủ số khung (1.0s = 24 lần).
- `Q` bỏ phần bên trái đầu phát, `W` bỏ phần bên phải.
- Mọi clip đều bỏ 1.0s đầu (giây đầu AI hay giật).

> Ghi chú: muốn khỏi cắt 1.0s đầu 10 lần, mình có thể cắt sẵn bằng ffmpeg ra thư mục `1080_trim/`. Khi đó mọi mốc "nguồn" dưới đây trừ đi 1.0.

---

## Bước 1 — Khung timeline

| # | Clip | Giữ (nguồn) | TL | Mối nối ra (xem Bước 2) |
|---|---|---|---|---|
| 1 | C01 | 1.0 → 6.5 | 0:00.0–0:05.5 | **N1** Smash cut to black |
| 2 | Đen | 0.6s | 0:05.5–0:06.1 | **N2** J-cut gió |
| 3 | C02 | 1.0 → 4.5 (1×) + 4.5 → 5.75 (2×) | 0:06.1–0:10.2 | **N3** Speed ramp + whoosh |
| 4 | C03 | 1.0 → 8.0 | 0:10.2–0:17.2 | **N4** Đổi cỡ cảnh + L-cut tiếng nước |
| 5 | C04 | 1.0 → ~6.4 (khung cắt ở N5) | 0:17.2–~0:22.6 | **N5** Cut on look |
| 6 | C05 | 2.0 → 8.0 | ~0:22.6–0:28.6 | **N6** Im lặng trước cú đánh |
| 7 | C06 | 1.0 → 7.6 | 0:28.6–0:35.2 | **N7** Cắt ngay sau tiếng gầm |
| 8 | C07 | 1.0 → 8.0 | 0:35.2–0:42.2 | **N8** Match hướng chuyển động |
| 9 | C08 | 1.0 → 8.0 | 0:42.2–0:49.2 | **N9** Đổi góc sau câu thoại + J-cut |
| 10 | C09 | 2.0 → ~9.6 (khung cắt ở N10) | 0:49.2–~0:56.8 | **N10** Cut on point |
| 11 | C10 | 1.0 → … | ~0:56.8 → | (tia lửa ~0:57.6, lửa bùng ~1:01.8) |

Mốc TL sau C04 lệch vài khung tùy khung bạn chọn ở N5 và N10. Chỉ cần thứ tự đúng.

---

## Bước 2 — 10 mối nối, làm từng cái

Luật chung cho cả 10 mối nối:
- **Không mở tab Transitions.** Vlog giả làm footage điện thoại thật, nên mọi chuyển cảnh là cắt thẳng. Cảm giác "chuyển cảnh" đến từ ba thứ: chuyển động trong hình, âm thanh, và chọn đúng khung để cắt.
- Cắt **trong lúc đang chuyển động**, không cắt sau khi chuyển động đã dừng.
- Whoosh chỉ đi với cú cắt có chuyển động. Cắt tĩnh mà gắn whoosh nghe như video template.

### N1 — C01 → Đen: Smash cut to black

Cô đang chạy, linh cẩu sát sau lưng, và hình tắt phụt. Người xem bị bỏ lửng: đó là cái móc của cả video.
1. Tìm khung **cành thông che nhiều nhất bên phải**, khoảng nguồn **6.3–6.5**. Dò từng khung bằng `←` / `→` [Frame].
2. Đầu phát ở khung đó → `W` (bỏ phần sau).
3. Clip đen nằm ngay sau. Kéo mép phải clip đen về **0.6s** (14–15 khung).
4. SFX: Audio → **Sound effects** → tìm `impact` hoặc `boom` (chọn tiếng trầm, ngắn).
   - Kéo xuống track âm, **mép trái đúng khung đầu clip đen**.
   - Volume −8 dB, Fade out 0.3s.
5. Kiểm tra: tiếng thở và tiếng chân của C01 phải **tắt cụt** đúng điểm cắt, không fade. Sự im lặng đột ngột chính là cú đánh.

### N2 — Đen → C02: J-cut tiếng gió

Âm thanh cảnh sau đến trước hình, nên não người xem "vào" thung lũng trước khi mắt thấy.
1. Chuột phải C02 → **Separate audio** (bản cũ: Extract audio).
2. Kéo mép trái track âm của C02 sang trái **0.3s**, chồng lên cuối clip đen. Kéo được vì còn 1.0s đã cắt ở đầu clip.
3. Âm đoạn đó: **Fade in 0.3s**.
4. Card `51,000 YEARS AGO`: xem Bước 4.

### N3 — C02 → C03: Speed ramp vào cửa hang + whoosh

Flycam lao vào hang và tăng tốc ở cuối. Viền đá nhòe mạnh che mối nối, rồi C03 mở bằng tiếng nước bắn.
1. Đầu phát ở nguồn **4.5** của C02 → `Ctrl+B`.
2. Chọn đoạn sau → bảng phải **Speed** → **Normal** → **2.0x**. Đoạn này còn ~0.63s.
   - Muốn tăng tốc mượt hơn: Speed → **Curve** → **Custom**, kéo 2 điểm cuối lên ~2.5x. Tốc độ sẽ dồn dần thay vì nhảy bậc.
   - Clip không có người nên tăng tốc an toàn [Ramp]. **Không làm chậm** clip có mặt người.
3. Cắt ở khung **viền đá nhòe nhất**, khoảng nguồn 5.5–5.75. Không đi tới hết clip vì khung cuối đã chậm lại.
4. Thêm whoosh: Sound effects → `whoosh`. Đặt sao cho **chỗ to nhất của whoosh rơi đúng điểm cắt**, tức đầu whoosh vào sớm ~0.2s. Volume −10 dB.
5. Kiểm tra: tiếng nước bắn đầu C03 phải nối liền ngay sau whoosh, giống một chuỗi âm.

### N4 — C03 → C04: Đổi cỡ cảnh + L-cut tiếng nước

Selfie cận chuyển sang máy đặt cố định, thấy cả người đang run. Đổi cỡ cảnh rõ rệt đã là chuyển cảnh, không cần gì thêm.
1. Cắt C03 ngay **sau chữ "Soaked."**, để thêm 4–6 khung cho câu nói thở ra hết.
2. L-cut: Separate audio của C03 → kéo mép phải track âm dài thêm **0.5s** sang C04, Fade out 0.5s. Tiếng nước kéo qua nên cảnh mới không bị "trống".
3. Không whoosh, vì đây là cắt tĩnh.

### N5 — C04 → C05: Cut on look

Nora liếc sang một bên, rồi cắt sang thứ cô đang nhìn: hai thợ săn qua lùm cây. Người xem tự hiểu "cô thấy họ".
1. Trong C04, dò từng khung quanh nguồn **6.0** để tìm khung **đầu cô bắt đầu quay**.
2. Đi thêm **4–6 khung** → `W`. Cắt khi đầu quay được nửa chừng, không đợi quay xong.
3. Kiểm tra câu "Wet clothes kill faster than cold." đã nói xong trước điểm cắt.
4. Không SFX. Tiếng gió và tiếng chân C05 vào thẳng.

### N6 — C05 → C06: Im lặng trước cú đánh

Hai người khựng lại và nhìn thẳng vào ống kính, rồi C06 nổ ra.
1. C05 giữ tới nguồn **8.0**, để cái nhìn thẳng kéo dài ~2s (căng).
2. 0.4s cuối C05: Separate audio → **Fade out 0.4s** cho tiếng nền. Khi có nhạc, cũng keyframe nhạc tụt xuống mức thấp nhất ở đúng 0.4s này.
3. Đầu C06: SFX `impact` trầm, đặt ngay khung đầu, Volume −10 dB. Tiếng gốc C06 để 100%.
4. Mốc này rơi ~TL 0:28.6. Ngay sau đó, ở 0:30, là cú chồm. Đây là chỗ giữ người qua mốc 30s.

### N7 — C06 → C07: Cắt ngay sau tiếng gầm

1. C06 cắt ở nguồn **~7.6**, ngay khi tiếng gầm dứt. Không để khoảng lặng sau gầm.
2. C07 mở bằng bàn tay ông chạm tay áo cô. Nhịp đột ngột chuyển từ sợ sang tò mò, và chính sự tương phản đó là chuyển cảnh.

### N8 — C07 → C08: Match hướng chuyển động

1. Cuối C07 Thủ Lĩnh **đi xa khỏi máy**. Cắt khi ông đang giữa bước chân, khoảng nguồn 7.5–8.0. Kiểm tra câu "…but I'm freezing." đã xong.
2. C08 mở bằng Nora cũng **đi xa khỏi máy**, hướng về cửa hang. Hai chuyển động cùng chiều nên mắt người xem trượt qua mối nối như một hành trình liền.

### N9 — C08 → C09: Đổi góc sau câu thoại + J-cut

1. Cắt C08 sau "…It's too cold…", để thêm ~6 khung cho tiếng thở.
2. Separate audio của C09 → kéo mép trái track âm sớm **0.3s**: tiếng bước chân hoặc tiếng gầm trong hang vào trước hình.

### N10 — C09 → C10: Cut on point

Thủ Lĩnh chỉ tay xuống, rồi cắt thẳng vào thứ ông chỉ: hai viên đá và tổ rêu trước gối Nora.
1. Cuối C09, tìm khung **cánh tay duỗi hết**, khoảng nguồn 9.3–9.6. Đi thêm 2–3 khung → `W`.
2. C10 mở trên tay Nora và đá; tiếng đá gõ vào gần như ngay. Không whoosh.

---

## Bước 3 — Đổi hình bên trong clip

| Clip | Mốc (nguồn) | Làm |
|---|---|---|
| C01 | — | Để nguyên. Clip chạy rung sẵn; zoom thêm sẽ rối |
| C03 | 6.0 | `[Punch]` 110% + `[Gióng mắt]` khi nói "Ten seconds in. Soaked." |
| C04 | 3.0 | `[Punch]` 112% (khoanh tay, nói) + `[Gióng mắt]` |
| C05 | cả clip | `[Push]` 100 → 108% (keyframe Scale đầu và cuối clip) |
| C06 | 5.5 | `[Punch]` 110% vào mặt Thủ Lĩnh |
| C07 | 3.0 / 5.5 | `[Punch]` 115%, Position dời vào bàn tay + đường may → 5.5 trả 100% |
| C08 | 6.0 | `[Punch]` 110% lúc Nora quay về máy |
| C09 | 5.5 | `[Zoom-CO]` 100 → 110% lúc ông giơ hai viên đá |

**`[Punch]` làm như sau:**
1. Đầu phát ở mốc → `Ctrl+B`.
2. Chọn đoạn sau → bảng phải **Video → Basic → Scale** = 110%.
3. Kéo hình trong Player cho mắt nhân vật nằm đúng đường gióng: menu Player → bật ruler / guides, rồi kéo một đường ngang ở tầm mắt **trước** khi zoom.

**`[Zoom-CO]` làm như sau:**
1. Đầu phát ở mốc → bấm hình thoi cạnh Scale để đặt keyframe ở 100%.
2. Đi tới ~20 khung → Scale 110% (keyframe 2 tự tạo).
3. Chuột phải keyframe 2 → chọn đường cong **Cubic Out**.

---

## Bước 4 — 3 card chữ

| Card | TL | Nằm trên |
|---|---|---|
| `51,000 YEARS AGO` | 0:06.3–0:08.8 | C02 flycam |
| `HOUR 0 — 24 HOURS REMAINING` | 0:17.5–0:20.0 | C04 |
| `MISSION: MAKE FIRE BEFORE NIGHTFALL` | 0:54.2–0:56.7 (C09 nguồn ~7.0, ngay sau nhát đá ra tia lửa) | C09 |

1. Text → **Add text** → kéo lên track phủ đúng mốc.
2. Kiểu chữ:
   - Font **Arial Black**, trắng, **Stroke** đen độ dày 3.
   - Cỡ ~1/18 chiều cao khung.
   - Căn giữa, cách mép trên ~8%.
3. **Không** dùng Animation.
4. Làm xong card 1 → **Save preset** [Preset chữ] → card 2 và 3 chọn preset đó.
5. Không phụ đề, không chữ nào khác.

---

## Bước 5 — Âm thanh

- Chọn mọi clip có thoại (C01, C03, C04, C07, C08) → bảng Audio → bật **Normalize loudness**.
- Mức trên đồng hồ dB:
  - Thoại đỉnh −6 đến −12.
  - SFX nhỏ hơn thoại. Ngoại lệ: cú `impact` ở N1 và N6 được nổi.
- **Nhạc chưa có** (Suno chưa có key). Khi có nhạc:
  - 0:00–0:06.1 không nhạc.
  - Nhạc vào ở C02 với Fade in 1s, −22 dB.
  - Từ C05 hạ dần về −30 dB; tụt hẳn ở 0.4s cuối C05 (N6).
  - Lên lại −24 dB ở C07 nguồn 5.5.
  - `[Duck]` −4 dB quanh từng câu thoại.

---

## Bước 6 — Xuất thử và xem trên điện thoại

1. Đặt `I` ở 0:00 và `O` ở ~1:05 → **Export** chỉ vùng này [Xuất đoạn]: 1080p, H.264, **24 fps**.
2. Xem trên điện thoại, **một lần có tiếng và một lần tắt tiếng**, kiểm từng điểm:
   - [ ] 0:00–0:02: mặt hoảng và linh cẩu lộ ra trước 0:03.
   - [ ] N1: tiếng tắt cụt đúng lúc hình tắt. Không lọt 1 khung C01 nào sau màn đen.
   - [ ] N3: không thấy khung đứng yên trước khi cắt.
   - [ ] N5 và N10: thấy rõ "cô nhìn → thấy họ", "ông chỉ → thấy đá".
   - [ ] Không có khung đen hay khung nháy 1 khung ở bất kỳ mối nối nào (dò từng khung quanh mỗi điểm cắt).
   - [ ] Mission card hiện trước 1:00 và đọc kịp.
3. Mối nối nào "giật" thì dời điểm cắt ±2–4 khung, đừng thêm hiệu ứng.

Sau khi đăng 48h: Studio → video → **Analytics → Engagement → Key moments → Intro**, xem % còn lại ở 0:30. So với video trước của kênh.
