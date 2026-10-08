---
name: fk-capcut-edit
description: Lập Bảng dựng CapCut cho mọi loại video YouTube (vlog FlowKit, video tự quay, nấu ăn, review…) để tăng watch time và sớm đủ điều kiện bật kiếm tiền (1000 sub / 4000 giờ xem) — kế hoạch từng clip theo giây: giữ đoạn nào, cắt ở đâu, punch-in/zoom, B-roll, chữ trên hình, nhạc, SFX, phút đầu kiểu trailer, đổi hình mỗi 3–5s, chuẩn −14 LUFS, và kế hoạch cắt Shorts 9:16 từ video dài. Dùng skill này mỗi khi user nhắc tới CapCut, "edit video", "dựng video", "hậu kỳ", "cắt ghép", "bảng dựng", "watch time", "giữ chân người xem", "retention", "người xem thoát sớm", "cắt Shorts từ video dài", hoặc vừa có bản 1080p clean từ FlowKit và hỏi bước tiếp theo — kể cả khi user không nói chữ "CapCut".
---

# fk-capcut-edit — Bảng dựng CapCut để tăng watch time

User dựng thành thạo trong CapCut Desktop (giao diện tiếng Anh). Việc của Claude là đưa ra **Bảng dựng**: kế hoạch cụ thể tới từng giây để user mở song song và làm theo — không dẫn từng cú click, không dừng chờ sau mỗi thao tác. Thao tác nào cần kỹ thuật riêng thì gọi **tên công thức** trong ngoặc vuông (`[Zoom-CO]`, `[Gióng mắt]`, `[Beat]`…) từ `references/pro-recipes.md`; đọc file đó trước khi lập bảng. Chỉ khi user hỏi "nút X ở đâu" mới mở `references/capcut-desktop-howto.md` (đường dẫn tính từ `skills/fk-capcut-edit/`). Mỗi mối nối trong bảng ghi **tên kiểu chuyển cảnh**; cách làm từng kiểu trong CapCut nằm ở `references/transitions-capcut.md`.

**Chế độ hướng dẫn chi tiết** — khi user xin "hướng dẫn chi tiết", "làm từng bước", "chuyển cảnh làm sao": viết thêm file hướng dẫn từng bước cho đoạn đó (vd. `output/<slug>/huong_dan_1p_dau.md`). File này gồm: chuẩn bị project, khung timeline có mốc nguồn và mốc TL, từng mối nối kèm khung cắt + thao tác CapCut + SFX + cách tự kiểm tra, rồi tới zoom, card chữ, âm thanh, xuất thử. Mẫu: `output/neanderthal-51ka/huong_dan_1p_dau.md`.

Nền tảng: 5 chiến lược của video *"Cách đạt 1000 Sub và 4000 Giờ xem"* (kênh Hồ Mạnh Thắng Official). Bảng dựng xử lý chiến lược 2 (watch time) và 4 (Shorts kéo view). Chiến lược 1 (thumbnail, SEO), 3 (chủ đề cố định) và 5 (lịch đăng, playlist) nằm ngoài phần dựng — xem bảng cuối file.

## Lựa chọn user đã chốt (2026-10-08)

| Chủ đề | Chốt |
|---|---|
| Phạm vi | Mọi loại video. Luật vlog FlowKit chỉ áp khi đó là POV / time-travel vlog |
| Phụ đề | **Không burn phụ đề** vào hình — cả video dài lẫn Shorts. Video dài có thể kèm `.srt` rời nếu user muốn (`/extract-capcut-srt`) |
| End screen | **Không chừa đoạn cuối cho end screen**. Video kết thúc theo đúng nhịp truyện (vlog: CUT ĐEN là hết) |
| Nhạc | Trộn hết trong CapCut (âm lượng, hạ nhạc dưới thoại); sau khi xuất chỉ chạy ffmpeg chuẩn hóa về −14 LUFS |
| Shorts | Cắt từ video dài 16:9, reframe sang 9:16 trong CapCut (không sinh clip dọc riêng) |
| Cách hướng dẫn | Mặc định: Bảng dựng + tên công thức (`references/pro-recipes.md`), không dẫn từng click. User xin chi tiết (2026-10-08) → chế độ hướng dẫn chi tiết ở trên |
| Phím tắt | Mặc định CapCut (`Ctrl+B`, `Q`/`W`…), không đổi keymap |

## Thứ tự ưu tiên khi các nguồn mâu thuẫn

1. `CLAUDE.md`, memory của user, và bảng "Lựa chọn user đã chốt" ở trên.
2. Với POV / time-travel vlog: luật hậu kỳ của `/fk-time-travel-vlog` (`references/post-and-publish.md` §1, `story-engine.md` §1, §5, §9, §11, §13b, `transitions.md`) — không crossfade, không bumper, chữ trên hình chỉ năm / mission card / countdown.
3. Skill này.

## Vì sao dựng quyết định watch time

YouTube đưa video cho ~100 người đầu. Nếu họ thoát sau vài giây, tỷ lệ giữ chân thấp và hệ thống ngừng đề xuất. Bảng dựng nhắm 3 việc:

- **Phút đầu giữ người ở lại** — như trailer phim: khoảnh khắc mạnh nhất / câu hỏi lớn nhất trước, giải thích sau. Nhưng trailer phải cho biết chuyện gì đang xảy ra: một intro 40s toàn highlight mà không có tiền đề chỉ giữ được 18.5%. Thước đo là key moment **Intro** trong Studio (% còn xem ở 0:30).
- **50% đầu được đầu tư nặng nhất** (công thức MrBeast) — ai xem hết nửa đầu thường xem tiếp. Video dài nên ≥ 8 phút (mốc chèn quảng cáo giữa video), và 4–5 phút đầu là nơi dồn công.
- **Mắt luôn có thứ mới** — đổi góc, đổi cỡ cảnh, B-roll hoặc zoom mỗi 3–5s; nhưng xen nhịp chậm ở khoảnh khắc cảm xúc để video không mệt. Editor của Ryan Trahan thấy chính việc *chậm lại* ở nhịp nhân vật làm retention tăng.
- **Kéo lại người xem ở ~3:00 và ~6:00, kết đột ngột** — memo MrBeast: đặt một cảnh mạnh ở hai mốc này, không báo hiệu sắp hết video.

Nguồn và độ tin cậy của từng con số: `references/pro-recipes.md` §8. Điều không có nguồn gốc (vd. "intro ≤ 25s") không đưa vào luật.

## Quy trình

### 1. Gom đầu vào

**Dự án FlowKit** (có `output/<slug>/`) — tự tìm, không hỏi:

| Cần | Ở đâu |
|---|---|
| Clip đã duyệt | `output/<slug>/1080/scene_XX_*_1080p_clean.mp4` (thiếu thì `scenes/` bản 720p) |
| Thứ tự, thoại, Act | `script.md`, `clips.json` |
| Nhịp dựng | bảng **Nhịp dựng** trong `script.md` (clip Chậm / Nhanh, nhịp cao trào) |
| Card chữ | mốc năm, mission card, countdown trong `script.md` |
| Nhạc | file từ `/fk-gen-music` (nếu có) |

Clip 8s của FlowKit có ~1s đầu bị giật (Rule 49) → mặc định giữ từ giây 1.0 trừ khi đã trim.

**Video khác** — hỏi user đúng 1 lượt những gì chưa biết: thư mục footage (hoặc danh sách cảnh + thời lượng), chủ đề kênh, độ dài mong muốn, khoảnh khắc mạnh nhất của video. Nếu user chỉ mô tả bằng lời (chưa có file), lập Bảng dựng theo cảnh mô tả, ghi rõ giả định.

Có file → đo thông số trước khi lập bảng:
```bash
ffprobe -v error -show_entries format=duration:stream=width,height,r_frame_rate -of default=nw=1 <clip>
```
(Clip FlowKit thường 1920×1080, 24 fps.)

### 2. Lập Bảng dựng

Dự án FlowKit → ghi `output/<slug>/capcut_edit_sheet.md`; video khác → thư mục footage của user (hoặc scratch nếu chưa có). Gửi bảng cho user; user sửa thì cập nhật file.

Mẫu:

```markdown
# Bảng dựng — <tên video>
16:9 · 1920×1080 · 24 fps · Dự kiến 9:40 · Nhạc: music_main.mp3

## Phút đầu (trailer) — 0:00–1:00
| # | Clip | Giữ (in→out) | Dài | Hình đổi ở | Chữ | Âm | Ghi chú |
|---|---|---|---|---|---|---|---|
| 1 | C01 | 1.0→7.6 | 6.6s | 3.0 punch-in 112% | — | không nhạc | Cold open, cắt ĐEN ở 7.6 |
| 2 | ĐEN | — | 0.6s | — | — | SFX boom nhẹ | |
| 3 | C02 | 1.0→8.0 | 7.0s | push-in 100→106% | `51,000 YEARS AGO` 0.3→2.8s | nhạc vào −22 dB | |

## Act 1 — 1:00–2:40   (tổng tới đây: 2:40)
...

## Kế hoạch Shorts
| Short | Nguồn (timecode video dài) | Dài | Hook giây đầu | Reframe | Kết |

## Kiểm tra sau khi xuất
```

Luật lập bảng:
- **2s đầu đã có mối nguy / câu hỏi / khoảnh khắc mạnh nhất.** Không logo, không chào hỏi, không xin sub trong phút đầu.
- **Phút đầu dựng như trailer.** Vlog FlowKit: cold open → CUT ĐEN → card năm → … → mission card trước ~1:00. Video khác: kết quả đẹp nhất / khoảnh khắc gây tò mò nhất trước (món ăn hoàn thành, cú twist, kết quả thử nghiệm), cắt trước khi lộ hết, rồi mới vào phần "làm thế nào".
- **Tiền đề + cái giá trong ~10s đầu.** Người xem phải biết *ai, ở đâu, sắp mất gì*, bằng một câu thoại hoặc card được phép (vlog: card năm, countdown). Một chuỗi highlight không lời giải thích thì tụt.
- **Intro montage cắt từ cả video** (khi user muốn trailer dài hơn cold open):
  - Mảnh 2–3s từ các khoảnh khắc mạnh nhất, theo thứ tự leo thang của truyện; mỗi mảnh là một câu thoại gốc trọn vẹn.
  - Cắt **trước khi lộ kết quả** (chưa thấy ai thắng, ai sống).
  - Ngắt giữa các nhịp bằng CUT ĐEN 0.4s + hit trầm; kết bằng câu thì thầm quay về mối nguy, rồi `[J-cut]` sang cảnh mở truyện.
  - Đổi lấy: mission card bị lùi. Ghi rõ mốc mới; mặc định ~30s để mission card về ~1:20. Bản ~60s chỉ khi user chọn, và lập 2 bản cho user so số Intro ở 0:30.
  - Clip chưa sinh thì lấy mốc từ phân đoạn `0-3s / 3-6s / 6-8s` của `video_prompt`, ghi "dời lại khi có file".
- **Phút 1–3 đi nhanh** (memo MrBeast lấy chính video sinh tồn làm ví dụ: gói nhiều ngày trong 3 phút đầu). Không dừng lâu ở giải thích hay chuẩn bị.
- **Re-hook ở ~3:00 và ~6:00**: đánh dấu trong cột Ghi chú cảnh mạnh rơi vào hai mốc này; nếu không có, đề xuất đổi thứ tự hoặc rút đoạn trước nó.
- **Cột "Hình đổi ở" không trống quá 5s liên tục** trong 50% đầu video (nửa sau nới tới ~8s).
- **Mỗi 15–20s phải có thứ mới**: thông tin, vấn đề, thất bại, nguy hiểm hoặc nhịp cảm xúc. Đoạn nào trượt luật này ở nửa đầu → đề xuất cắt, rút ngắn hoặc đẩy cảnh mạnh hơn lên trước, ghi lý do trong cột Ghi chú.
- **Nhịp nhanh / chậm xen kẽ.** Cảnh hành động, chuỗi thử–hỏng: cắt ngay khi hành động xong (thường giữ 4–6s, ngắn dần). Cảnh cảm xúc, im lặng, cảnh cuối: giữ đủ, không zoom. Cao trào: dài → ngắn → ngắn → ngắn → payoff → dài.
- **Kết đột ngột** ở nhịp truyện cuối, không câu "cảm ơn đã xem", không báo trước sắp hết.
- **Tổng thời lượng sau mỗi Act / chương**; cảnh báo nếu video dài < 8 phút.

### 3. Công cụ đổi hình (ghi vào cột "Hình đổi ở")

Theo thứ tự ưu tiên (tên trong ngoặc vuông là công thức ở `references/pro-recipes.md`):
1. **Cắt thẳng sang clip mới** tại khung che (vật lướt qua ống kính, quay gáy, whip pan) — kèm SFX whoosh nhẹ.
2. **`[Punch]`**: split tại mốc 3s hoặc 6s (với clip FlowKit trùng ranh giới `0-3s / 3-6s / 6-8s`), đoạn sau Scale 110–115%. Trên mặt người luôn kèm `[Gióng mắt]`. Zoom có gia tốc vào khoảnh khắc phát hiện: `[Zoom-CO]`.
3. **`[Push]`**: keyframe Scale 100% → 105–108% suốt clip — cảnh căng, lời thú nhận, phát hiện.
4. **B-roll / cutaway** trên track phủ 1.5–3s (tay, vật, cảnh rộng) trong khi tiếng clip chính vẫn chạy.
5. **Jump cut** khi đi bộ hoặc nói dài — bỏ khoảng chết thật, không cắt hơi thở giữa các từ.
6. **`[Ramp]`** tăng tốc đoạn đi đường / làm việc. Không làm chậm clip AI có mặt hoặc tay.

Mỗi zoom phải có lý do (câu chốt, phát hiện, cảm xúc); zoom chỉ để "có chuyển động" làm video rối.

Giới hạn: Scale tối đa ~120% trên nguồn 1080p (quá mức này hình mềm, lộ lỗi AI); zoom không được cắt mất mặt, tay đang cầm vật hoặc chủ thể chính. Video không phải vlog được dùng thêm transition ngắn (≤ 0.3s) ở chỗ đổi chương, nhưng cắt thẳng vẫn là mặc định.

### 4. Chữ trên hình

- **Vlog FlowKit**: chỉ năm, mission card, countdown `HOUR X — Y HOURS REMAINING` (~7 mốc cho 9–10 phút, đặt ngay trước/sau nấc leo thang).
- **Video khác**: tiêu đề chương ngắn, chữ nhấn mạnh từ khóa / con số — tối đa 1 dòng chữ trên hình tại một thời điểm.
- Style mặc định: chữ đậm không chân, trắng, viền đen, giữa trên ~8% từ mép, hiện ~2.5s (đủ đọc, không chớp qua), không hiệu ứng bay. Làm 1 card rồi `[Preset chữ]`. Ghi nội dung + timecode chính xác vào cột Chữ.
- Không burn phụ đề (lựa chọn đã chốt).

### 5. Âm thanh (trộn trong CapCut)

Ghi vào cột Âm (mức đồng hồ dB và công thức `[Fade]`, `[Duck]`, `[Beat]`: `references/pro-recipes.md` §4):
- **Thoại**: đỉnh −6 đến −12 dB.
- **Nhạc**: −20 đến −24 dB khi có thoại (nguồn khác nói hạ 15–20 dB dưới thoại; cả hai đều được); đoạn không thoại như intro, montage lên −15 đến −18 dB; hạ thêm hoặc tắt ở cảnh căng đỉnh điểm và cảnh cuối; không tắt hẳn giữa một cảnh. Câu thoại quan trọng → keyframe hạ nhạc quanh câu đó.
- **SFX**: whoosh ở cú cắt khung che, boom nhẹ ở CUT ĐEN, bíp ~0.3s nếu có chửi thề (vlog: mốc `bleep_at`). SFX nhỏ hơn thoại.
- **`[J-cut]`**: tiếng clip sau vào sớm ~0.5s trước hình (chỉ khi 0.5s đó không có thoại).
- Bật **Normalize loudness** cho các clip thoại để clip đều tiếng nhau.
- **`[Beat]`** chỉ cho intro trailer, montage, Shorts. Đoạn kể chuyện cắt theo câu nói, không theo nhạc.

Sau khi xuất, chuẩn hóa về −14 LUFS / −1 dBTP (YouTube hạ video to hơn mức này, video nhỏ hơn thì nghe yếu hơn video khác):
```bash
ffmpeg -i final.mp4 -af loudnorm=I=-14:LRA=11:TP=-1.0 -c:v copy -c:a aac -b:a 192k -ar 48000 final_14lufs.mp4
```

### 6. Màu đồng nhất

Một lớp Adjustment phủ cả timeline (hơi ấm, tương phản nhẹ; vlog thêm grain rất nhẹ để giống một máy quay), rồi chỉnh riêng clip lệch. Ghi clip nào cần chỉnh riêng vào cột Ghi chú. Gợi ý thử trên 10s trước khi áp cả video.

### 7. Kế hoạch Shorts (chiến lược 4)

Shorts được đề xuất mạnh tới người lạ không cần SEO — dùng làm mồi kéo người sang video dài.

- **3–4 Short, mỗi cái 15–45s, một ý duy nhất**, lấy từ khoảnh khắc mạnh nhất. Vlog sinh tồn: món ăn lạ, rượt đuổi / nguy hiểm, mẹo sinh tồn kỳ lạ (`post-and-publish.md` §3). Video khác: kết quả gây bất ngờ, mẹo hay nhất, khoảnh khắc hài / kịch tính nhất.
- **Nguồn 16:9 → 9:16**: crop mất ~70% bề ngang, nên chọn đoạn có chủ thể lớn, nằm gần giữa khung. Ghi vào cột Reframe: Scale (≈316% để lấp khung dọc) + chủ thể cần bám (mặt, tay, mối nguy) và mốc giây phải dời Position.
- **Giây đầu = giữa hành động**, coi như thumbnail của Short (người ta vuốt đi trong 1s); không dẫn nhập; đổi hình nhanh hơn video dài (2–3s).
- Shorts được tới 3 phút và YouTube nói không có độ dài ưu tiên; giữ 15–45s vì một ý duy nhất hiếm khi cần hơn.
- **Không phụ đề burn** (lựa chọn đã chốt) → chọn đoạn mà hình tự kể được chuyện, không phụ thuộc vào việc nghe rõ thoại.
- **Kết** ở khoảnh khắc chưa có kết quả hoặc `[Loop]` nối vòng về giây đầu (view tính cả lượt xem lại).
- Nhắc user khi đăng: gắn **Related video** trỏ tới video dài, ghim bình luận có link video dài; ngôn ngữ tiêu đề khớp ngôn ngữ thoại (CLAUDE.md Rule 20).

### 8. Kiểm tra sau khi xuất

Đặt cuối Bảng dựng:
```bash
ffprobe -v error -show_entries format=duration:stream=width,height,r_frame_rate -of default=nw=1 final.mp4
ffmpeg -i final_14lufs.mp4 -af ebur128=peak=true -f null - 2>&1 | tail -12   # dòng "I:" ≈ -14 LUFS
```
- [ ] Xuất 1080p, H.264, **fps bằng nguồn** (FlowKit 24 → xuất 24; mẹo "xuất 30 fps" chỉ đúng khi quay 30, đổi 24 → 30 làm chuyển động giật). Xuất thử intro bằng `[Xuất đoạn]`, xem trên điện thoại trước
- [ ] 2s đầu có mối nguy / câu hỏi; phút đầu không logo, không chào hỏi
- [ ] Nửa đầu: không đoạn > 5s hình đứng yên, không đoạn 20s không có gì mới
- [ ] Thoại rõ trên nhạc (nghe bằng tai nghe **và** loa điện thoại)
- [ ] Chữ đúng chính tả, đúng loại cho phép; không có phụ đề burn
- [ ] Tiền đề + cái giá rõ trong ~10s đầu; có cảnh mạnh quanh 3:00 và 6:00; kết đột ngột
- [ ] Video dài ≥ 8 phút; −14 LUFS ± 1
- [ ] Sau khi đăng 48h: xem key moment **Intro** (% ở 0:30) và chỗ dip trên biểu đồ retention; dip trùng cảnh nào thì ghi vào bảng dựng video sau

## Những thứ ngoài phần dựng

| Việc | Dùng |
|---|---|
| Thumbnail (chiến lược 1) | `/fk-thumbnail`, `/fk-thumbnail-guide` — biểu cảm mặt rõ, cảm xúc mạnh |
| Tiêu đề, mô tả, tag SEO (chiến lược 1) | `/fk-youtube-seo` (vlog: không timestamp, theo memory) |
| Chủ đề cố định (chiến lược 3), lịch đăng + playlist (chiến lược 5) | `skills/fk-time-travel-vlog/references/post-and-publish.md` §3–4. Playlist sắp trong YouTube Studio, không cần chèn vào video |
| Ghép tự động bằng ffmpeg không qua CapCut | `/fk-concat` |
| Nhạc | `/fk-gen-music` |
| Phụ đề `.srt` rời | `/extract-capcut-srt`, `/translate-capcut-srt` |
| Upload | `/fk-youtube-upload` (bật nhãn "Altered or synthetic content" bằng tay với video AI) |

Khi user hỏi chiến lược kênh chung: đăng đều (vd. 1 video/tuần) tốt hơn đăng dồn rồi bỏ; mốc 50–100 video tăng mạnh cơ hội được đề xuất; giữ một chủ đề để YouTube và nhà quảng cáo định dạng được kênh.
