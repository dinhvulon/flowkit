# Storyboard, tỉ lệ shot & chuẩn chân thực

Đọc ở **Bước 4** của `SKILL.md`. Mục này thay mục 3, 6, 8, 9 cũ. Câu chữ đưa vào `video_prompt` luôn lấy từ `prompt-lock.md` — bảng dưới chỉ để lập storyboard.

## Ethnicity Lock & Period Lock (mục 3 cũ)

- Mọi người xuất hiện trong khung (người đi đường, người bán hàng, lính canh, quý tộc) phải **trông như người bản địa của thời kỳ/địa điểm đó** để người xem tin, không cần nghiên cứu chính xác.
- **PERIOD LOCK**: cấm rập khuôn điện ảnh sai (vd: mũ sừng Viking), cấm vật liệu/kiến trúc/trang phục lệch niên đại. Ánh sáng dùng mặt trời/đuốc/đèn dầu, tránh nguồn sáng không đúng thời đại.
- Không làm nhục/biếm họa dân tộc, tôn giáo. Hình phạt/chiến tranh chỉ ám chỉ, không mô tả máu me — để tránh bị Veo từ chối (`UNSAFE_GENERATION`) và YouTube hạn chế quảng cáo. Xem bảng từ ngữ an toàn trong `fk-create-project.md`.

## Storyboard & tỉ lệ loại shot (mục 6 cũ)

**Bảng storyboard toàn video (bắt buộc, trước khi viết Clip JSON):**

| # | Hồi | Beat | Loại shot | Hành động | Thoại (ai nói) | Chuyển cảnh vào | Chuyển cảnh ra | Khung cuối |
|---|---|---|---|---|---|---|---|---|

Cột "Khung cuối" mô tả chính xác khung hình cuối clip (vd: "súc gỗ che 90% khung, đi trái→phải") — clip kế tiếp mở từ đúng khung này.

**Bảng vật lý từng clip — BẮT BUỘC user duyệt trước khi viết Clip JSON** (Bài học 21; dùng `AskUserQuestion` hoặc hỏi thẳng trong chat):

| # | Máy đặt ở đâu, nhìn về đâu | Có gì trong khung ở giây 0 | Vật di chuyển: hướng + tốc độ + hệ quả trong khung | Chuyển động vật lý thật | Ai hoặc cái gì rời khung, bằng cách nào |
|---|---|---|---|---|---|
| S31 | Trên thuyền chèo, nhìn về sau qua đuôi thuyền | Sau gáy vlogger bên trái, thành phố ở chân trời bên phải | Thuyền chèo tay đi chậm, rời xa thành phố → thành phố giữ nguyên hoặc nhỏ dần | Thuyền nhấp nhô và lắc theo sóng; người chèo quay mặt về đuôi thuyền | Vlogger dịch sang bên; sóng tạt kín ống kính ở giây cuối |

**Tỉ lệ loại shot** — giữ gần đúng, vì chính tỉ lệ này tạo cảm giác "máy của nhân vật":

| Tỉ lệ | Loại | Mẫu `shot` (từ `prompt-templates.md`) |
|---|---|---|
| ~65% | Selfie góc siêu rộng, cánh tay lọt khung, vừa đi vừa nói | `ultra-wide selfie at arm's length, her extended arm visible at the right edge, face on the left third, deep [street] behind her` |
| ~15% | POV mắt nhân vật, thấy tay cô tương tác với đồ vật/người — không thấy mặt, dùng cho beat xúc giác | `first-person POV from her eye level, her own hands visible in the lower frame [scooping millet / touching bronze armor]` |
| ~10% | Sau gáy / qua vai — chủ yếu để làm chuyển cảnh | `camera behind her head, she turns away to look at [X], the back of her hair bun fills the frame` |
| ~5% | Máy dựng cố định (ăn uống, kết) | `Static footage from a fixed viewpoint resting on the table facing her; the frame does not move; she sits and eats, vendors moving behind` |
| ~5% | Toàn cảnh hoành tráng nhưng **vẫn từ vị trí nhân vật đứng** | `view from where she stands on a high earthen ridge, slow handheld pan over [thousands of soldiers / the pits]; the view is her own eyes, and she never appears in the frame` |

**Không drone, không flycam, không b-roll điện ảnh tách rời** — video mẫu gần như không có shot nào không "quay bằng máy của cô". Chỉ dùng drone khi user yêu cầu rõ.

**Clip dân bản địa nói**: người nói là dân bản địa (`<Name> says in [ancient language]: "..."`), thêm vào hành động `"<Vlogger> listens silently, reacting with wide eyes, lips closed"`.

## Chữ trên màn hình & âm thanh (mục 8 cũ)

**Ngoại lệ (user chốt 2026-10-05):** được chèn đúng 3 loại chữ ở hậu kỳ: năm (`51,000 YEARS AGO`), mission card (`MISSION: MAKE FIRE BEFORE SUNSET`) và countdown (`HOUR 3 — 21 HOURS REMAINING`). Không bao giờ viết chúng vào `video_prompt`. Ngoài 3 loại đó: video mẫu **không có bất kỳ chữ nào trên màn hình** — không title card chương, không "3 HOURS LATER", không phụ đề cứng. Mọi thông tin (địa điểm, thời gian, chuyển cảnh) truyền qua lời thoại + hình ảnh. Phụ đề chỉ là tùy chọn dạng file `.srt` rời, không burn vào hình. Vì vậy **không dùng `/fk-gen-text-overlays`**, và không dùng `/fk-concat-fit-narrator` với text overlay/crossfade.

Âm thanh (nhạc nền + ambient) **trải liên tục suốt video** (nhịp im lặng của `story-engine.md` là im **thoại**, ambient vẫn chạy) — hạ nhạc nhỏ dưới thoại thay vì tắt hẳn giữa các scene; hạ thêm ở cảnh nguy hiểm và cảnh kết (Bước 5).

## Chuẩn chân thực — "mọi thứ quay bằng máy của cô" (mục 9 cũ)

Độ chân thật của format đến từ việc **người xem tin đây là footage điện thoại thật**. Mọi clip phải giữ đủ các yếu tố sau:

- **Style string cố định** (đầu mọi `video_prompt`, ngay sau câu góc máy của `prompt-lock.md` khối 1; theo `/fk-camera-guide` mục quang học smartphone):
  `handheld vlog footage, natural wide-angle handheld perspective, no exaggerated fisheye distortion, natural daylight, subtle hand shake, photorealistic, documentary realism`
- **Dấu vết máy quay chân thực**: góc nhìn tự nhiên, không méo kiểu fisheye (`no exaggerated fisheye distortion`), rung tay nhẹ theo nhịp bước, cánh tay lọt mép khung ở shot selfie, auto-exposure theo nguồn sáng tự nhiên. Không dolly/crane/gimbal mượt kiểu điện ảnh.
- **Người nền phản ứng**: dân bản địa dừng lại nhìn chằm chằm, tò mò hoặc nghi ngờ. Người nền không nói; chỉ người được giao thoại trong sub-clip mới nói (nhân vật phụ nói ngôn ngữ không hiểu được, `character-bible.md` mục 4).
- **Audio môi trường đúng thời kỳ**: tiếng chợ bằng ngôn ngữ cổ/địa phương, bánh xe gỗ lạch cạch, chuông đồng xa — ghi ở dòng `Audio:` cuối prompt.
- **Ràng buộc viết thành câu khẳng định trong thân prompt — KHÔNG dùng dòng `Negative:` liệt kê từ khóa** (góp ý của user: liệt kê từ khóa không có tác dụng, điện thoại vẫn hiện ra). Câu chuẩn, đặt trước dòng `Audio:`:
  `The view comes from her own outstretched arm or her own eyes, and her free hand is empty. <V> stays in frame for the whole clip and never disappears. The locals wear [period clothing]; everything around is [era], with no modern buildings or vehicles. Only <V> speaks English; nobody speaks over anyone else. No subtitles or text appear on screen. This looks like real footage, not a movie or a 3D render.`
- **Material**: `realistic` mặc định áp *Canon EOS R5, 35mm* — kiểu ảnh máy ảnh, lệch với footage điện thoại. Khuyến nghị tạo material tùy chỉnh (giữ ảnh ref chân thực, chỉ đổi scene sang chất điện thoại):
  ```bash
  curl -X POST http://127.0.0.1:8100/api/materials -H "Content-Type: application/json" -d '{
    "id": "phone_vlog",
    "name": "Smartphone Vlog (Photoreal)",
    "style_instruction": "Photorealistic RAW photograph, natural available light, real skin texture, documentary realism.",
    "negative_prompt": "NOT 3D render, NOT anime, NOT illustration, NOT cinematic color grade, NOT studio lighting, NOT lens distortion.",
    "scene_prefix": "Handheld vlog frame, natural daylight, natural wide-angle handheld perspective, no exaggerated fisheye distortion, documentary realism.",
    "lighting": "Natural available light"
  }'
  ```
  Rồi tạo project với `"material": "phone_vlog"`. Nếu user không muốn thêm material → dùng `realistic` và dựa vào style string trong `video_prompt`.
