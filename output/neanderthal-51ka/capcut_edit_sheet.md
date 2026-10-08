# Bảng dựng — I Survived 24 Hours with Neanderthals (51,000 Years Ago)
16:9 · 1920×1080 · 24 fps · Dự kiến ~10:50 (bảng này: 0:00–2:11.9) · Nhạc: chưa có (`/fk-gen-music` cần `SUNO_API_KEY`)

Nguồn: `output/neanderthal-51ka/1080/scene_XX_*_1080p_clean.mp4`. "Giữ" tính theo giây của file nguồn; timecode trong ngoặc là vị trí trên timeline.
- Clip 01–13: đã có file. Bảng đi theo **hình thật** đã xem từng giây (không theo nhãn `clips.json`, xem mục chốt).
- Clip 18–56 trong intro: **chưa sinh**. Mốc giây lấy từ phân đoạn 0-3s / 3-6s / 6-8s trong `video_prompt`. Khi có file 1080p thì xem lại và dời in/out cho khớp câu thoại.

Chung cho cả đoạn:
- Cắt thẳng, không transition, không bumper.
- Chữ chỉ có card năm / mission card / countdown: Arial Black trắng, viền đen 3, giữa trên ~8% từ mép, ~2.5s, không animation. **Intro không có chữ nào.**
- Lớp Adjustment ấm nhẹ (Temp +6, Contrast +5) phủ cảnh ngày và cảnh trong hang. Không phủ C01 (rừng đêm) và C39–C47 (bão đêm); hai đoạn đó giữ xanh lạnh. Grain rất nhẹ phủ hết.
- Bật Normalize loudness cho mọi clip có thoại.

## Intro (trailer cắt từ cả video) — 0:00–0:57.3

Cách đọc: 4 nhịp tăng dần, bị → bỏ đói → đi săn → bị vây, rồi một nhịp chậm, cuối cùng là câu chốt.
- Mỗi cú cắt dừng **trước khi lộ kết quả**: chưa thấy Thủ Lĩnh tránh bò, chưa thấy linh cẩu bỏ chạy.
- Thoại gốc của từng clip giữ nguyên, nên mỗi mảnh là một câu nói trọn.
- Đổi hình nằm ở chính điểm cắt (mảnh 2–3s), nên cột "Hình đổi ở" chỉ ghi điều xảy ra bên trong mảnh.

| # | Clip | Giữ (in→out) | Dài | Hình đổi ở | Chữ | Âm | Ghi chú |
|---|---|---|---|---|---|---|---|
| 1 | C01 `scene_01_8ae57638` | 1.0→8.0 | 7.0s (0:00.0–0:07.0) | 3.0 cô ngoái lại, linh cẩu lộ ra · 6.0 cành thông quét ngang ống kính | — | Tiếng gốc 100%, **không nhạc** | Hook: giây 0 là mặt hoảng + "HELP!", linh cẩu lộ ở 0:02. Cắt ngay sau cành thông. HANDOFF: phát lại đoạn này sau A4-05 |
| 2 | C05 `scene_05_2ee54029` | 6.0→8.0 | 2.0s (0:07.0–0:09.0) | Hai thợ săn khựng lại, nhìn thẳng vào lùm cây | — | Nhạc vào thẳng ở 0:07.0, −20 dB (không fade) | Câu hỏi thứ hai: họ là ai |
| 3 | C06 `scene_06_25b511a6` | 3.0→5.0 | 2.0s (0:09.0–0:11.0) | Thủ Lĩnh chồm kín khung | — | Tiếng gầm gốc đè nhạc | |
| 4 | C08 `scene_08_17feb126` | 6.0→8.0 | 2.0s (0:11.0–0:13.0) | Nora quay mặt về máy | — | Nhạc −24 · "Help me... please..." | |
| 5 | C18 `A2-06 MEAT-CRISIS` | 1.0→3.5 | 2.5s (0:13.0–0:15.5) | Cái xương lủng lẳng trong hốc trống | — | Nhạc −24 · "Wait. That's it? That's the food?" | Nhịp 2: không đủ ăn |
| 6 | C18 | 6.0→8.0 | 2.0s (0:15.5–0:17.5) | Nora sát ống kính, hơi thở mờ | — | "Storm's coming. I'm the extra mouth." | Jump cut trong cùng clip |
| 7 | C19 `A2-07 HUNT-CALL` | 6.0→8.0 | 2.0s (0:17.5–0:19.5) | Nora siết thắt lưng, bước theo | — | Nhạc lên −20, trống bắt đầu · "Nobody said no. So I'm going." | Nhịp 3: đi săn |
| 8 | C23 `A3-04 STALKING` | 3.0→6.0 | 3.0s (0:19.5–0:22.5) | Con bò vung sừng hất tuyết | — | Nhạc −22 · "That's not a cow. That's a truck." | Câu đùa giữa lúc căng: giữ trọn |
| 9 | C26 `A3-07 ALARM` | 3.0→6.0 | 3.0s (0:22.5–0:25.5) | Con bò ngẩng phắt, nhìn thẳng Nora | — | "No no no. It's looking at me." | |
| 10 | C27 `A3-08 THE-CHARGE` | 1.0→4.0 | 3.0s (0:25.5–0:28.5) | Bò lao, tuyết tung | — | Nhạc dâng −18 · "It's running! It's coming— Chief!" | **Nhanh** |
| 11 | C28 `A3-09 FEINT` | 1.0→2.5 | 1.5s (0:28.5–0:30.0) | Sừng sát ngực Thủ Lĩnh | — | "It's on him—" · riser 1s trước điểm cắt | Cắt trước cú né, không cho thấy kết quả |
| 12 | ĐEN | — | 0.4s (0:30.0–0:30.4) | — | — | Cắt câm cả nhạc lẫn tiếng · hit trầm | |
| 13 | C35 `A3-16 BLOOD-SCENT` | 6.0→8.0 | 2.0s (0:30.4–0:32.4) | Nora ngoái về rặng thông xa | — | Nhạc vào lại −24, chỉ còn drone · "That laughing's getting closer." | Nhịp 4: máu kéo bầy thú về |
| 14 | C39 `A4-02 BLIZZARD` | 3.0→6.0 | 3.0s (0:32.4–0:35.4) | Cửa hang chỉ còn bức tường trắng | — | Gió gốc lớn · "Can't see anything." | |
| 15 | C40 `A4-03 HYENA-CRIES` | 3.0→6.0 | 3.0s (0:35.4–0:38.4) | Nora giật mình, ép sát vách | — | Tiếng cười linh cẩu gốc, tăng +3 dB nếu nhỏ · "It's laughing. Right outside." | |
| 16 | C41 `A4-04 HYENAS-SHADOWS` | 1.0→3.5 | 2.5s (0:38.4–0:40.9) | Bốn đôi mắt sáng trên thềm đá | — | "One, two, three... four." | |
| 17 | C43 `A4-06 SPEAR-WALL` | 1.0→3.0 | 2.0s (0:40.9–0:42.9) | Con đầu đàn bước lên thềm cao | — | Trống dồn | |
| 18 | C44 `A4-07 SNARL` | 3.0→5.0 | 2.0s (0:42.9–0:44.9) | Hai người đàn ông gầm, ưỡn ngực | — | Tiếng gầm gốc đè nhạc | |
| 19 | C46 `A4-09 TORCH-DYING` | 1.0→3.0 | 2.0s (0:44.9–0:46.9) | Linh cẩu lao qua ngưỡng hang | — | "It's jumping at him— look out!" | **Nhanh** |
| 20 | C47 `A4-10 NORA-FIRE` | 1.0→3.0 | 2.0s (0:46.9–0:48.9) | Nora dí cành lửa vào đuốc, lửa bùng | — | Nhạc đỉnh −18 · "Here! Take it— take the fire!" · riser | Cắt trước khi linh cẩu chạy |
| 21 | ĐEN | — | 0.4s (0:48.9–0:49.3) | — | — | Câm · hit trầm | |
| 22 | C55 `A4-18 RED-OCHRE` | 3.0→6.0 | 3.0s (0:49.3–0:52.3) | Vệt son đỏ kéo qua gò má | — | Nhạc chỉ còn 1 nốt kéo dài −26 · "Oh— cold. That's on my face now." | **Chậm.** Hứa hẹn cảm xúc, không nói cô sống hay không |
| 23 | C56 `A4-19 HAND-STENCILS` | 6.0→8.0 | 2.0s (0:52.3–0:54.3) | Bàn tay đỏ nhỏ cạnh bàn tay lớn | — | "My hand. Next to theirs." | |
| 24 | C40 | 6.0→8.0 | 2.0s (0:54.3–0:56.3) | Mặt Nora tái quay về ống kính | — | Nhạc tắt hẳn ở 0:54.3 · thì thầm "They followed the blood. All the way." | Câu chốt: quay lại mối nguy |
| 25 | ĐEN | — | 1.0s (0:56.3–0:57.3) | — | — | Boom trầm nhỏ · J-cut tiếng gió C02 vào ở 0:57.0 | Hết intro |

Nhạc intro là một bài riêng kiểu trailer, có nhịp dồn và 2 chỗ ngắt cho 2 cú ĐEN. Khác bài nền của Act 1.

## Act 1 — 0:57.3–2:11.9   (tổng tới đây: 2:11.9)

C01 đã dùng ở intro nên câu chuyện mở thẳng bằng C02. C05/C06/C08 có 2s từng xuất hiện ở intro; giữ nguyên, người xem nhận ra "đây rồi".

| # | Clip | Giữ (in→out) | Dài | Hình đổi ở | Chữ | Âm | Ghi chú |
|---|---|---|---|---|---|---|---|
| 26 | C02 `scene_02_3fc899f4` | 1.0→6.0 | 5.0s (0:57.3–1:02.3) | FPV chạy liên tục · 4.0 lao qua cửa hang | `51,000 YEARS AGO` 0:57.6–1:00.1 | Gió gốc · nhạc nền Act 1 fade-in 1s, −22 dB | Cửa hang có lửa = nơi an toàn duy nhất |
| 27 | C03 `scene_03_e7a2e9c3` | 1.0→8.0 | 7.0s (1:02.3–1:09.3) | 1.0 trượt chân ngã nước · 3.5 bám rễ cây leo lên · 6.0 punch-in 110% mặt | — | Nhạc −22, hạ −26 quanh "Ten seconds in. Soaked." · tiếng nước gốc | Tiếng nước bắn làm dấu câu |
| 28 | C04 `scene_04_1428bcf0` | 1.0→8.0 | 7.0s (1:09.3–1:16.3) | 3.0 punch-in 112% (khoanh tay, nói) · 6.0 trả về 100% lúc cô liếc sang phải | `HOUR 0 — 24 HOURS REMAINING` 1:09.6–1:12.1 | Nhạc −24, hạ −28 quanh "Wet clothes kill faster than cold." | Cái liếc ở 6.0 nối hướng nhìn sang C05 |
| 29 | C05 `scene_05_2ee54029` | 2.0→8.0 | 6.0s (1:16.3–1:22.3) | Push-in 100→108% suốt clip · 6.0 hai người khựng lại, nhìn thẳng vào lùm cây | — | Nhạc hạ dần xuống −30 · bước chân, tiếng thở nín (gốc) | Không thoại |
| 30 | C06 `scene_06_25b511a6` | 1.0→7.6 | 6.6s (1:22.3–1:28.9) | 1.0 máy giật lùi · 3.0 Thủ Lĩnh chồm vào kín khung · 5.5 punch-in 110% mặt ông | — | Nhạc −30 · tiếng gầm gốc đè lên | **Nhanh.** Cắt ngay khi gầm xong |
| 31 | C07 `scene_07_b24dd212` | 1.0→8.0 | 7.0s (1:28.9–1:35.9) | 3.0 punch-in 115%, dời Position vào bàn tay + đường may · 5.5 về 100% lúc ông đứng dậy · 7.0 ông đi xa | — | Nhạc từ −30 lên −24 ở 5.5 · "They're not killing me... but I'm freezing." 6–8s | Cận đường may = lý do ông tha cô |
| 32 | C08 `scene_08_17feb126` | 1.0→8.0 | 7.0s (1:35.9–1:42.9) | 3.0 Người Mạnh Nhất hạ giáo chắn ngang · 6.0 Nora quay về máy, punch-in 110% | — | Nhạc −24, hạ −28 quanh "Help me... please... It's too cold..." | Lửa trong hang ngay sau lưng người gác |
| 33 | C09 `scene_09_93a7f623` | 2.0→10.0 | 8.0s (1:42.9–1:50.9) | 2.0 Thủ Lĩnh ra khỏi bóng tối · 4.0 tiến sát · 5.5 punch-in 110% lúc giơ hai viên đá · 6.5 nhát đánh ra tia lửa · 9.0 chỉ tay ra thung lũng | `MISSION: MAKE FIRE BEFORE NIGHTFALL` 1:48.4–1:50.9 | Nhạc −26 · tiếng đá gõ ở 6.5 nguồn | Mission card ngay sau nhát đánh mẫu |
| 34 | C10 `scene_10_7fdc42df` | 1.0→8.0 | 7.0s (1:50.9–1:57.9) | 3.0 tia rơi vào rêu, punch-in 112% xuống tổ rêu · 5.0 cô thổi · 6.0 lửa bùng, về 100% thấy hai thợ săn | — | Nhạc −28 lúc gõ đá · 6.0 dâng −20 | **Nhanh** đến 6.0 |
| 35 | C11 `scene_11_4365f996` | 1.0→8.0 | 7.0s (1:57.9–2:04.9) | 4.0 Người Mạnh Nhất thu giáo · 6.0 cô bước vào · 7.0 lưng vào bóng tối (khung che → cắt) | — | Nhạc −22 · J-cut tiếng lửa C12 ở 2:04.4 | Để thở, không zoom |
| 36 | C12 `scene_12_cbf44f9b` | 1.0→8.0 | 7.0s (2:04.9–2:11.9) | Push-in chậm 100→105% · 3.0 Bà Lão thêm que · 5.0 Bà thổi · 6.0 lửa bùng to | — | Nhạc −22 chạy tiếp sang Act 2 | **Chậm.** Act 2 mở bằng C13 |

Kiểm tra luật:
- Không đoạn nào quá 3s không đổi hình. Intro đổi hình mỗi 1.5–3s; Act 1 đổi ≤ 3s.
- Chữ trên hình: 1 card năm, 1 countdown, 1 mission card. Không phụ đề, không end screen.

## Shorts lấy được từ đoạn này

| Short | Nguồn (timecode video dài) | Dài | Hook giây đầu | Reframe (Scale ≈316%) | Kết |
|---|---|---|---|---|---|
| A "Bị săn" | 0:00.0–0:07.0 (C01) + 1:16.3–1:28.9 (C05+C06) | ~20s | Mặt hoảng + "HELP!", linh cẩu lộ ở 0:02 | C01: bám mặt Nora, dời Position sang phải ở 3.0 · C05: bám người cầm giáo · C06: bám mặt Thủ Lĩnh | Cắt ngay tiếng gầm |
| B "Thử thách lửa" | 1:46.9–2:04.9 (C09 từ 6.0 nguồn + C10 + C11) | ~18s | Nhát đánh ra tia lửa | C09: bám tay cầm đá · C10: bám tổ rêu + mặt · C11: bám Nora + mũi giáo | Lưng cô đi vào hang tối |

Không dùng intro làm Short: nó lộ cả video, Short nên là một khoảnh khắc trọn. Khi đăng: gắn Related video tới video dài, ghim link, tiêu đề tiếng Anh.

## Kiểm tra sau khi xuất (khi ghép đủ cả video)

```bash
ffprobe -v error -show_entries format=duration:stream=width,height,r_frame_rate -of default=nw=1 final.mp4
ffmpeg -i final.mp4 -af loudnorm=I=-14:LRA=11:TP=-1.0 -c:v copy -c:a aac -b:a 192k -ar 48000 final_14lufs.mp4
ffmpeg -i final_14lufs.mp4 -af ebur128=peak=true -f null - 2>&1 | tail -12   # dòng "I:" ≈ -14 LUFS
```
- [ ] 1080p, H.264, 24 fps
- [ ] 0:00 có mặt hoảng + tiếng kêu, linh cẩu lộ trước 0:03
- [ ] Intro không lộ kết quả cú bò lao và trận linh cẩu
- [ ] Thoại nghe rõ trên nhạc (tai nghe **và** loa điện thoại)
- [ ] Video dài ≥ 8 phút; −14 LUFS ± 1

## Cần user chốt

1. **Intro dùng 13 clip chưa sinh** (C18–C56). Có 2 cách:
   - Dựng intro sau cùng, khi đã có cả video.
   - Dựng tạm bản ngắn chỉ từ C01–C12 rồi thay sau.
2. **Mission card lùi xuống 1:48, và intro 57s chưa nói tiền đề.** Nghiên cứu mới (skill `pro-recipes.md` §8): một intro 40s toàn highlight không giải thích chỉ giữ 18.5%. Bản hiện tại tới 0:57 người xem vẫn chưa biết đây là năm nào, cô có bao lâu.
   - **Đề xuất mặc định:** rút intro còn ~30s (bỏ mảnh 5–6, 13–14, 17–18, 22–23), mission card về ~1:20.
   - Thêm tiền đề trong 10s đầu bằng card được phép: đưa `51,000 YEARS AGO` lên mảnh 2 (0:07.3–0:09.8) và bỏ card này ở C02. Countdown `HOUR 0` giữ ở C04.
   - Khi có đủ clip: xuất cả 2 bản intro bằng `[Xuất đoạn]` để so; sau khi đăng xem key moment Intro (% ở 0:30).
   - Mốc re-hook: video ~10:50 cần cảnh mạnh quanh 3:00 (rơi vào Act 2, khủng hoảng thịt) và 6:00 (cuộc săn). Kiểm khi lập bảng Act 2–3.
3. **Hai bản scene 09.**
   - Bảng dùng `93a7f623`: có lửa trong hang, Thủ Lĩnh đánh mẫu ra tia lửa.
   - `clips.json` trỏ `132d3863`: hang tối, chỉ thả đá rồi chỉ tay. Nếu dùng bản này, mission card ở 1:49.9–1:52.4.
4. **File 10–13 không khớp nhãn trong `clips.json` / HANDOFF.**
   - Nhãn ghi chuỗi đánh hỏng ferro rod / 4 nhúm rêu.
   - Hình thật: C10 Nora tự ra lửa, C11 được vào hang, C12 thắp bếp với Bà Lão, C13 toàn cảnh hang.
   - Thoại C09–C12 cần nghe lại để đặt mốc hạ nhạc.
5. **Nhiệm vụ xong quá sớm.** Mission card ở 1:48, lửa bùng ở 1:56, không có lần hỏng.
   - (a) Để Act 2 đưa ngay vấn đề mới (thịt cạn / bão tới).
   - (b) Chèn 1–2 lần hỏng trước C10. Cần bản ferro-rod cũ hoặc sinh clip mới (tốn credit, hỏi trước).
