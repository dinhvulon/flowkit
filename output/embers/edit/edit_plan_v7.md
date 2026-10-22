# Kế hoạch dựng EMBERS v7

File này dùng làm đầu vào cho bước dựng. Khi dựng, gọi `/video-editing` (Rule 66), kết hợp với `/fk-capcut-edit`, `/fk-cinematic-transitions` và `/fk-sound-design`, rồi làm theo các mục dưới đây.
Cập nhật lần cuối: 20/10/2026, sau khi duyệt RR-10 v6, RR-11 v3, RR-12 v2 và BN-01 v3. Mỗi lần duyệt thêm clip hoặc chốt quyết định âm thanh thì cập nhật file này.

## 0. Nguồn

- **Clip đã duyệt và file của từng clip:** `output/embers/scenes_v7.json`, các mục có `approved: true`. Danh sách ở mục C.
- **Thứ tự cảnh và thời lượng:** `output/embers/paper_edit_v7.md`. Kịch bản gốc ở `output/embers/script_v7.md`.
- **Hook mở đầu (dựng lại kiểu trailer):** `output/embers/hook_recuts_v7.json`.
- **File âm thanh dùng khi dựng:** `output/embers/edit/audio/`.

## Ràng buộc khi dựng (Rule 18, 32, 49, 66, 67)

- **Bản xuất cuối:** chỉ dùng bản 1080p đã xoá logo, `output/embers/1080/*_1080p_clean.mp4`.
  - Clip nào cũng phải upscale từ đúng tài khoản Flow đã sinh ra nó (cột "Acc" ở mục C).
  - Đã upscale + xoá logo (20/10): 17 clip namlt đã duyệt (FL-06 → FL-12, EL-07, MP-01, LH-01, LH-02, RR-10 → RR-14, BN-01). Clip dinhvulon25 chưa upscale.
  - Đã upscale + xoá logo (21/10, acc dinhvulon16): BN-11, BN-13a, BN-13b, ES-05, LH-09, TR-02b, TR-04.
- **Bản nháp:** được dùng bản 720p trong `output/embers/scenes/`.
- **Điểm cắt thoại:** lấy theo mốc thời gian từng từ của Whisper (`tools/review_dialogue.py`). Không cắt mù 1 giây đầu.
- **Âm lượng:** master ở −14 LUFS / −1 dBTP. Không dùng mức `loudnorm -16` mặc định của skill.
- **Lưu file:** EDL, file concat và các bản dựng lưu trong `output/embers/edit/` với tên `edit_v1`, `edit_v2`… Không ghi đè bản đã giao cho user.
- **Không dùng dịch vụ ngoài:** không gọi ElevenLabs, fal.ai hay VideoDB. Giọng thì dùng tiếng gốc của clip hoặc `/fk-gen-narrator`, và phải hỏi user trước.

## A. Lồng tiếng radio (đã chốt)

### A1. RR-04 (Nora nghe điện thoại / radio trong xe)

- **Hình:** RR-04 v8, `scenes/scene_045_RR-04_855e529b_v8.mp4`. Clip này im lặng, khoảng −33 LUFS.
- **File giọng sẵn sàng:** `edit/audio/RR-04_eli_radio.mp3`, dài 6.0s, mono, đã xử lý radio, −16 LUFS. Làm ngày 20/10/2026.
- **Nguồn:** voicemail của Eli trong `scenes/scene_031_EL-06_c50977a5_v3.mp4` (câu thoại, tiếng va chạm, tiếng ngựa hí), lấy đoạn 0–5.5s và đẩy lùi 0.2s.
- **Xử lý radio** (chi tiết ở `scenes_v7.json` → `RR-04.edit_audio_v8`):
  - band-pass 380–3000 Hz, tăng 5 dB ở 1.7 kHz, nén 6:1, soft-clip, bitcrush nhẹ;
  - nền nhiễu trắng: squelch to ở 0–0.2s và 5.7–5.95s, giữa hai đoạn là tiếng rè nhỏ, sau đó im lặng.
- **Whisper:** nghe đủ 100% câu của Eli ở 0.27–4.35s.
- **Cách mix:** đặt mp3 vào từ giây 0 của RR-04 v8. Tiếng gốc v8 gần như im (−33 LUFS) nên giữ nguyên bên dưới, không cần tắt.

### A2. LH-01 (tổng đài báo sơ tán Cedar Flat)

- **File giọng sẵn sàng:** `edit/audio/LH-01_dispatch_radio.mp3`, dài 5.8s, mono, đã xử lý radio, −16 LUFS.
- **Câu thoại:** "All units, Cedar Flat is now mandatory evacuation. Fire is two miles out."
- **Nguồn:** chính clip LH-01 v1 tự đọc câu này (0.0–5.5s), sau đó tách bằng ffmpeg: band-pass 300–3400 Hz, khử nhiễu FFT, nén, bitcrush nhẹ.
  - Đây không phải tách stem bằng AI, nên có thể còn lẫn tiếng lửa trong dải tần radio.
  - Nếu nghe thấy lẫn, cài demucs để tách lại (hỏi user trước).
- **Cách mix:**
  - Tắt tiếng gốc của clip trong 0–5.8s, vì giọng gốc chưa qua radio và sẽ chồng lên bản radio.
  - Đặt mp3 vào từ giây 0.
  - Dưới giọng giữ một lớp nền tiếng lửa/gió, hạ khoảng −6 dB. Lấy nền này từ phần cuối clip (5.6–6s) hoặc từ clip lửa bên cạnh.

### A3. RR-07: KHÔNG lồng

User dặn ngày 20/10/2026: chỉ RR-04 cần lồng radio. RR-07 chỉ giữ tiếng nhiễu radio gốc.

## B. Post-VO trong kịch bản chưa chốt (kiểm tra khi dựng)

Các dòng dưới đây có câu thoại post-VO trong `prompts_v7.json` nhưng chưa có quyết định lồng tiếng.

- **Clip đã duyệt:** nghe lại clip. Như LH-01, có thể model đã tự đọc câu thoại.
- **Clip chưa sinh:** quyết định khi duyệt clip.

Trước khi tạo giọng mới, phải hỏi user.

| Clip | Thời điểm | Người nói | Giọng | Câu thoại |
|---|---|---|---|---|
| RA-07 (đã duyệt) | 0-3s | Dispatch | erinome | "Evacuation warning for Cedar Flat, Ridge Road and Keller Lane. Fire's making a run. All crews report to Division Alpha." |
| FL-02 (đã duyệt) | 0-2s | rookie | alnilam | "You ever had to deploy one of those?" |
| EL-02 (đã duyệt) | 0-5s | Walt | sadaltager | "Eli Hale! Turn around! That road's closed, son! Your sister'll skin us both!" |
| FL-07 (đã duyệt) | 0-2s | rookie | alnilam | "We're lighting more fire?" |
| FL-12 (đã duyệt) | 0-2s | crew | alnilam | "Hey, Hale, you're pink!" |
| EM-01 (đã duyệt) | 0-6s | Walt | sadaltager | "Walt Pruitt. Nora on this channel? Your brother biked up Ridge Road at four." |
| EM-03 (đã duyệt) | 3-7s | Walt | sadaltager | "Keller's place. Had a halter and rope over his shoulder." |
| CH-00 (đã duyệt) | 4-8s | Dispatch | erinome | "Negative, Hale. Air is grounded. No engines past the closure." |
| BN-05 (chưa sinh) | 0-3s | Nora | kore | "Somebody had to sign the papers, Eli! Mom sure didn't!" |
| BN-13a (`scenes/scene_067_BN-13a_e5937af3_hg2.mp4`) | 2.5-3.5s | Nora | kore | "Mom." (dời từ BN-12 đã cắt, 2026-10-21 #21; mặt Nora khuất, chỉ lồng tiếng; _hg2: Eli gào 0.78–2.22s, đặt "Mom." sau 2.3s để không đè) |
| LH-08 (chưa sinh) | 0-2s | crew | alnilam | "Cap, Hale's truck radio is just static." |
| LS-03 (chưa sinh) | 1.5-5s | Nora | kore | "Right here, Eli. Same as always. On top of you." |
| BK-07 (chưa sinh) | 4-8s | Nora | kore | "For a kid on a horse. She got him out. Not herself." |
| DW-03 (chưa sinh) | 0-2s | Ray | algenib | "Nora." |
| DW-05 (chưa sinh) | 2.5-4s | Nora | kore | "Worth it." |
| DW-06 (chưa sinh) | 0-3s | Ray | algenib | "Town held, Hale. We lost two barns and a mile of fence. Not one house. Not one person." |

## C. Clip đã duyệt (53 clip; còn 66 clip chưa sinh hoặc chưa duyệt)

| Clip | File 720p | Độ dài | AI | Acc | Ghi chú dựng |
|---|---|---|---|---|---|
| RA-02 | `scenes/scene_001_RA-02_49c1a6a2.mp4` | 8s | - | dinhvulon25 |  |
| RA-03 | `scenes/scene_002_RA-03_2528b08c.mp4` | 6s | - | dinhvulon25 |  |
| RA-06 | `scenes/scene_005_RA-06_14421c95.mp4` | 4s | - | dinhvulon25 |  |
| RA-07 | `scenes/scene_006_RA-07_f996fd3e.mp4` | 8s | - | dinhvulon25 | Có post-VO trong kịch bản, xem mục B |
| RA-08 | `scenes/scene_007_RA-08_1a7e8514_v3.mp4` | 4s | - | dinhvulon25 |  |
| RA-09 | `scenes/scene_008_RA-09_aeb258ed.mp4` | 4s | - | dinhvulon25 |  |
| FL-01 | `scenes/scene_009_FL-01_b2919f94_v3.mp4` | 8s | - | dinhvulon25 |  |
| FL-02 | `scenes/scene_010_FL-02_99f32c8f_v3.mp4` | 6s | - | dinhvulon25 | Có post-VO trong kịch bản, xem mục B |
| FL-04 | `scenes/scene_011_FL-04_5fd1fc66_v2.mp4` | 6s | - | dinhvulon25 |  |
| EL-01 | `scenes/scene_012_EL-01_a6727dd7.mp4` | 6s | - | dinhvulon25 |  |
| EL-02 | `scenes/scene_013_EL-02_1941e521_v6_8s.mp4` | 6s | - | dinhvulon25 | Có post-VO trong kịch bản, xem mục B |
| FL-05 | `scenes/scene_014_FL-05_4157ec00.mp4` | 4s | - | dinhvulon25 |  |
| FL-06 | `scenes/scene_015_FL-06_075b26da_v2.mp4` | 4s | - | namlt |  |
| FL-07 | `scenes/scene_016_FL-07_c8ec4bc6_v2.mp4` | 6s | - | namlt | Có post-VO trong kịch bản, xem mục B |
| EL-07 | `scenes/scene_017_EL-07_82687128_v3.mp4` | 6s | - | namlt |  |
| FL-08 | `scenes/scene_018_FL-08_948b7239_v2.mp4` | 8s | - | namlt |  |
| FL-10 | `scenes/scene_020_FL-10_1f54cd9e.mp4` | 6s | - | namlt |  |
| FL-11 | `scenes/scene_021_FL-11_9460e14b.mp4` | 4s | - | namlt |  |
| FL-12 | `scenes/scene_022_FL-12_136294a1.mp4` | 6s | - | namlt | Có post-VO trong kịch bản, xem mục B |
| MP-01 | `scenes/scene_023_MP-01_ba45804a.mp4` | 4s | - | namlt |  |
| MP-02 | `scenes/scene_024_MP-02_20b5906a.mp4` | 4s | - | dinhvulon25 |  |
| MP-03 | `scenes/scene_025_MP-03_cc8585de.mp4` | 8s | 8.25 | dinhvulon25 |  |
| MP-04 | `scenes/scene_026_MP-04_d4f60adf_v2.mp4` | 6s | 8.0 | dinhvulon25 |  |
| FL-13 | `scenes/scene_027_FL-13_0e9a4d05.mp4` | 6s | 8.5 | dinhvulon25 |  |
| MP-05 | `scenes/scene_028_MP-05_4f44afa0_v2.mp4` | 6s | 8.25 | dinhvulon25 |  |
| EL-03 | `scenes/scene_029_EL-03_7b51db6b_nopay.mp4` | 6s | 8.35 | dinhvulon25 |  |
| EL-05 | `scenes/scene_030_EL-05_de04a4b9_v2.mp4` | 6s | 8.5 | dinhvulon25 |  |
| EL-06 | `scenes/scene_031_EL-06_c50977a5_v3.mp4` | 6s | 8.0 | dinhvulon25 |  |
| EM-01 | `scenes/scene_032_EM-01_493785b6_v5.mp4` | 6s | 8.4 | dinhvulon25 | Có post-VO trong kịch bản, xem mục B |
| EM-02 | `scenes/scene_033_EM-02_3835fbf3_v3.mp4` | 4s | 8.25 | dinhvulon25 |  |
| EM-03 | `scenes/scene_034_EM-03_808d2300_v2.mp4` | 8s | 8.15 | dinhvulon25 | Có post-VO trong kịch bản, xem mục B |
| CH-00 | `scenes/scene_035_CH-00_ca4a14db_v2.mp4` | 8s | 8.2 | dinhvulon25 | Có post-VO trong kịch bản, xem mục B |
| CH-01 | `scenes/scene_036_CH-01_78bee1b9.mp4` | 8s | 8.4 | dinhvulon25 |  |
| CH-02 | `scenes/scene_037_CH-02_cb02f9b9.mp4` | 4s | 8.25 | dinhvulon25 |  |
| CH-03 | `scenes/scene_038_CH-03_e2543c1f_v2.mp4` | 8s | 8.15 | dinhvulon25 |  |
| CH-04 | `scenes/scene_039_CH-04_1c465109_v6.mp4` | 4s | 7.5 | dinhvulon25 |  |
| CH-05 | `scenes/scene_040_CH-05_213d9d86_v2.mp4` | 6s | 8.5 | dinhvulon25 |  |
| CH-07 | `scenes/scene_041_CH-07_7387b5cb_v2.mp4` | 6s | 8.5 | dinhvulon25 |  |
| CH-09 | `scenes/scene_042_CH-09_bbf4f595.mp4` | 6s | 8.4 | dinhvulon25 |  |
| RR-01 | `scenes/scene_043_RR-01_6d65d48b_v3.mp4` | 8s | 8.5 | dinhvulon25 |  |
| RR-02 | `scenes/scene_044_RR-02_ba32ecf9.mp4` | 4s | 8.3 | dinhvulon25 |  |
| RR-04 | `scenes/scene_045_RR-04_855e529b_v8.mp4` | 8s | 8.08 | dinhvulon25 | Lồng radio (mục A1) |
| RR-06 | `scenes/scene_046_RR-06_cd708a9f_v3.mp4` | 4s | 8.1 | dinhvulon25 |  |
| RR-07 | `scenes/scene_047_RR-07_c85505c5_v2.mp4` | 6s | 7.95 | dinhvulon25 | Không lồng radio |
| RR-08 | `scenes/scene_048_RR-08_545ae5e1_v3.mp4` | 6s | 7.95 | dinhvulon25 | trim first 0.5s (puffy smoke). |
| LH-01 | `scenes/scene_049_LH-01_366868c5.mp4` | 6s | 8.2 | namlt | Lồng Dispatch (mục A2) |
| LH-02 | `scenes/scene_050_LH-02_76ffc9cc_v2.mp4` | 6s | 8.12 | namlt | dùng 0–6s. v2 sinh lại cho gấp gáp (Bài học 102); Whisper đủ 100% chữ, thoại hết ở 4.86s. |
| RR-13 | `scenes/scene_051_RR-13_da00d8ea_v6.mp4` | 8s | 7.25 | namlt | dùng 0–8s, không thoại (chỉ tiếng thở gấp). v6: chạy về phía máy, cây cháy đổ sau lưng, cắt cảnh ở 6s sang đặc tả mặt hoảng sợ (đoạn 6–8s là điểm nhấn, có thể dùng cho hook). Lửa yếu hơn các cảnh kề (trời xám) — chỉnh màu ấm/cam khi dựng cho khớp RR-14/RR-10. Kính đẩy lên mũ, khác RR-14. |
| RR-14 | `scenes/scene_052_RR-14_916b6f45_v4.mp4` | 4s | 7.3 | namlt | dùng 0–4s, không thoại. v4: lửa mạnh đều phía sau (ref Ridge Road Fire); găng tay chỉ vào dấu vết trên sỏi. Dấu vết ra vết gai ngắn rộng (giống gai lốp/đế giày), không phải rãnh mảnh — nếu cần thì cắt ngắn 0.5–3.5s để bớt đoạn tay quét sỏi tung bụi. |
| RR-10 | `scenes/scene_053_RR-10_fba01c21_v6.mp4` | 4s | 8.65 | namlt | dùng 0–4s (giây 0–1 hơi rộng, có thể dùng 1–4s), không thoại. v6: xe nằm nghiêng im ở góc dưới trái sát cột cổng, đầu xe trái — khớp vị trí và hướng xe RR-11 (ref Keller Gate Bike lấy từ frame RR-11). Máy đẩy chậm vào; chiều muộn qua khói, lửa mạnh đều. |
| RR-11 | `scenes/scene_054_RR-11_d8aeb207_v3.mp4` | 6s | 7.67 | namlt | dùng 0–6s. Thoại gốc Nora (kore), gào 2 lần: "Eli! Eli Hale!" 0.2–2.6s, ngậm miệng nghe ngóng 3–4s, "I'm not mad!" ~4.1–5.1s. Đứng ở cổng cạnh xe đạp, khum tay gào, chỉ về chuồng; mặt hoảng. |
| RR-12 | `scenes/scene_055_RR-12_def0c40f_v2.mp4` | 4s | 8.15 | namlt | dùng 0–4s, không thoại (tiếng ngựa hí + thở gấp). v2: Nora quay phắt về chuồng; 0–2s Juniper (ngựa xám) chồm trong khe cửa rồi lùi vào; 2–4s Nora lao tới cửa, cuối clip đứng ở khe cửa, tay chạm ngựa ở ngưỡng (BN-01 mở từ tư thế này). |
| BN-01 | `scenes/scene_056_BN-01_57546ddf_v3.mp4` | 6s | 8.05 | namlt | dùng 0–6s, không thoại (lửa gầm, cửa nghiến ray, ngựa hí). v3 nối thẳng từ khung cuối RR-12 v2 (khung đó làm ref mở đầu): Nora quay lưng, tay trên cổ Juniper ở khe cửa; kéo cửa rộng ra; che mặt lao vào khói. Mối nối: ngựa ở frame 0 sáng hơn và đứng giữa khe cửa hơn so với cuối RR-12 — cắt thẳng, có thể chồng 2–3 frame nếu thấy nhảy. |
| BN-06 | `1080/scene_061_BN-06_a6adad15_1080p_clean.mp4` (720p đã xoá) | 6s | 8.4 | dinhvulon16 | Duyệt 22/10. Không thoại. Cận Nora nhìn xuống rồi nhìn ra, nước mắt rửa vệt muội tới cằm (rõ nhất 2.5–4s). Đỉnh đầu Eli lấp ló ở mép phải dưới — crop nhẹ nếu vướng. |
| BN-11 | `scenes/scene_065_BN-11_19fa5343_hg2.mp4` | 6s | 7.0 | dinhvulon16 | Whisper PASS 3 câu. Lỗi đã chấp nhận: rút khăn ra rồi nhưng vẫn thấy góc khăn đỏ trong túi quần Nora — nếu lộ rõ thì crop nhẹ / cắt sớm; sửa triệt để = start frame mới giấu khăn. |
| BN-13a | `scenes/scene_067_BN-13a_e5937af3_hg2.mp4` | 4s | 8.0 | dinhvulon16 | Eli gào 0.78–2.22s (cờ `? VOICE?` 372 Hz — nghe lại khi dựng). Bước nhảy lò cò chưa rõ. Lồng "Mom." xem mục A. |
| BN-13b | `scenes/scene_068_BN-13b_f044334e_hg2.mp4` | 4s | 7.8 | dinhvulon16 | Không thoại, thở gấp. Mái sập có chùm tia lửa hơi giống pháo hoa; cuối clip chạy lướt qua máy → có thể cắt đuôi ~0.5s. |
| ES-05 | `scenes/scene_073_ES-05_522f7b24_hg2.mp4` | 6s | 8.5 | dinhvulon16 | Không thoại. Ban đêm, ngựa đi cùng suốt clip, khớp start frame; không cần grade. |

## D. Thay đổi dựng từ lượt căng thẳng 2026-10-21 (#21)

- BN-12 và TR-05 đã cắt khỏi kịch bản; không dựng.
- BN-09r (~2s, chỉ dựng, không sinh): cắt lại một đoạn mái/gác cháy từ BN-07 v4, chèn giữa BN-09 và BN-11 để giữ nhịp đồng hồ "mái sắp sập". Chọn đoạn khi BN-07 v4 và BN-09 đã duyệt.
- BN-08 (sửa 21/10, không đòn bẩy/rìu): BN-08a = Nora tay không ấn cây rồi kéo tay Eli, thất bại, ngã ngồi (mở từ khung cuối BN-05; DUYỆT take 8 = scene_063_BN-08a_fca69fca_sf5.mp4, 4s, không thoại). BN-08b = Nora lấy vai đẩy cây lên một gang tay, hét "Eli, pull your legs out! Now!", Eli lôi chân ra, cây rơi xuống rơm trống (mở từ khung cuối BN-08a sf5). Nối thẳng a → b → BN-09; BN-09 mở từ khung cuối BN-08b (không sinh start frame), Nora dìu Eli yếu, vừa dìu vừa hét vào mặt.

- BN-13a + BN-13b bản `_hg2` (thay v8/v1) đã duyệt 2026-10-21: ra cửa chuồng ban đêm, mái sập sau lưng; mũ ref `HALE Helmet Goggles`. Khăn đỏ giờ che kín hai mắt ngựa (ref `Juniper Blindfold`), không còn nằm trên trán — giữ như vậy tới LS-05a (ngựa hất khăn).

Clip đã duyệt có thể chưa dùng hết trong bản dựng. Ví dụ FL-09 đã bỏ. `script_v7.md` vẫn ghi FL-10 là "Whirl!"; khi dựng phải hỏi user.

### Thang giờ (user chọn A, 2026-10-21)
- RR → BN → ES: **chiều tà dưới khói** (khớp các clip đã duyệt RR-07/08/12, BN-01..07). LS → TR: **chập tối dưới khói**. BK: đêm. DW: bình minh.
- **ES-05** bản `_hg2` (thay v4): đã là ban đêm, ánh lửa cam, khớp start frame; ngựa đi cùng suốt clip → không cần grade tối nữa.
- Nguyên nhân: ảnh ref `Ridge Road` chụp ban ngày nên model lấy luôn ánh sáng của ảnh. Câu Light trong prompt nay có thêm "never the plain grey daylight of the location photo".
