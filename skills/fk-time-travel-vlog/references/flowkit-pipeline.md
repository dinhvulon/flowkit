# Triển khai trong FlowKit — R2V Ingredients

Đọc ở **Bước 6–9** của `SKILL.md`. Thay mục 7a, 10 và phần 🛠️ cũ (quy trình start-frame → i2v cũ đã bỏ theo CLAUDE.md Rule 27).

> **Xác nhận trước mỗi bước sinh (Rule 29).** Trước bất kỳ lệnh nào khiến Flow sinh media (ref, video, clip thử, sinh lại, upscale), nói rõ sinh gì, bao nhiêu, rồi chờ user đồng ý. Xong mỗi bước thì DỪNG, đưa kết quả cho user duyệt. Lỗi hoặc điểm review thấp → báo cáo kèm đề xuất sửa, không tự sinh lại.

## 1. Cách nối clip

| Loại shot | Cách nối | Ghi chú |
|---|---|---|
| Có vlogger (mọi selfie / POV có tay / máy dựng) | **Tạo riêng rồi cắt**: 2 scene R2V độc lập. `video_prompt` A kết bằng khung che (swing cho selfie, foreground wipe cho POV); `video_prompt` B mở từ đúng khung che đó. Cắt thẳng tại khung che kín nhất lúc concat | **Mặc định duy nhất.** Cùng tư thế thì thêm match on action: B mở đúng tư thế cuối của A trong 1–2s đầu (Rule 44) |
| Không có nhân vật (vũ trụ, phong cảnh, FPV mở đầu theo yêu cầu — Bài học 18) | Có thể dùng ảnh khung đầu / Omni Flash first+last: `POST /api/flow/generate-video` với `model_family: "omni_flash"` + `start_image_media_id` (+ `end_image_media_id`), 4/6/8/10s, xem `docs/OMNI_FLASH.md` | Ảnh AI phải qua 4 bước xóa logo → upload lại trước khi dùng (Rule 28) |

- **Không dùng `/fk-gen-chain-videos`** (Veo start+end frame) — fail `UNSUPPORTED_ON_BATCH_API`; `FLOW_ALLOW_DEGRADED=1` chỉ biến nó thành i2v thường.
- FlowKit không có Extend. Một beat ~15s = 2 scene 8s nối bằng khung che.

## 2. Clip JSON → scene FlowKit

Clip JSON (mẫu ở `prompt-templates.md`) là bản thiết kế đọc được, lưu trong `output/<slug>/script.md`. Mỗi clip **bắt buộc** có `transition_in`, `transition_out` (câu prompt cụ thể) và `join`.

| Trường Clip JSON | Vào trường FlowKit |
|---|---|
| `refs` | `character_names` của scene = `["<V>", "<V> Body", <1 ref bối cảnh/sinh vật>]` (tối đa 3) |
| `camera` + `style` + `setting` + `in_place` + `shot` + ID-LOCK + `action` + `dialogue` + `background_people` + `transition_in/out` + `constraints` + `audio` | `video_prompt`, dựng đúng thứ tự 9 khối của `prompt-lock.md`; sub-clip `0-3s / 3-6s / 6-8s`; thoại dạng `Nora says (tag): "..."` |
| `setting` (tóm tắt) | `prompt` của scene (mô tả cảnh — R2V không dùng ảnh Frame 0) |
| `dialogue` (ghép 3 sub-clip) | `narrator_text` (PATCH, 18–22 từ) — đồng bộ bằng `/fk-gen-narrator` |
| `duration` | **PATCH** `{"duration": 8}` sau khi tạo scene — POST không nhận, thiếu thì âm thầm ra 10s (Bài học 12) |
| `join` | ghi chú cho bước concat (điểm cắt); `chain_type` = `ROOT` cho mọi scene R2V |
| `bleep_at` (tùy chọn) | không vào FlowKit — ghi chú hậu kỳ (`voice-bible.md` mục 3) |

## 3. Pre-flight & dựng dự án

```bash
curl -s http://127.0.0.1:8100/health          # {"extension_connected": true}
curl -s http://127.0.0.1:8100/api/flow/status # {"transport": "batch", ...}
```
Project mới → flush request PENDING cũ trước (CLAUDE.md Rule 21). Lỗi pipeline bất kỳ → `/fk-doctor` trước khi đoán cách sửa (Rule 31).

```bash
curl -X POST http://127.0.0.1:8100/api/projects -H "Content-Type: application/json" -d '{
  "name": "Rome 79 AD - Time Travel Vlog",
  "story": "<tóm tắt cold open + 5 Act>",
  "material": "phone_vlog",
  "allow_voice": true,
  "characters": [
    {"name": "Nora", "entity_type": "character", "description": "<CHARACTER_LOCK nguyên văn>", "voice_description": "<Laomedeia>"},
    {"name": "Nora Body", "entity_type": "character", "description": "<body sheet 3 góc đã mặc outfit thời kỳ>"},
    {"name": "Forum Market", "entity_type": "visual_asset", "description": "<bối cảnh + thành phố + năm>"}
  ]
}'
```
- `allow_voice: true`: server tự nối hậu tố vào mọi `video_prompt` (kể cả R2V, `_build_video_prompt`). Prompt thiếu dòng `Audio:` mà `allow_voice` tắt thì hậu tố là "no narration, no voiceover" — có thể nuốt giọng vlogger. Server cũng luôn nối `Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands.` nếu prompt chưa có chữ `negative:`; dòng này không nhắc thiết bị nên chấp nhận được, nhưng đừng tự thêm dòng `Negative:` khác.
- Bối cảnh cần giữ nhất quán khai báo `visual_asset` (worker bỏ qua `location` khi chạy R2V — Bài học 6). Chỉ vlogger có `voice_description` (Bài học 13).
- Material `phone_vlog`: tạo theo `shots-and-realism.md` mục chuẩn chân thực, hoặc dùng `realistic`.
- Sau đó: `POST /api/videos` → `POST /api/scenes` theo thứ tự storyboard → PATCH `duration` + `narrator_text` từng scene → `/fk-switch-project <PID>`.
- Dự án nhiều tập (cùng vlogger qua nhiều thời kỳ): dùng `series_manifest` để tái dùng media_id mặt của vlogger thay vì sinh lại — xem mục 7.

## 4. Refs → cổng duyệt

1. **Mặt** `<V>`: `/fk-upload-ref` (mặt thật) hoặc `/fk-gen-refs` (16:9 sheet nhiều góc). Xóa logo → upload lại (Rule 28).
2. **Body đã mặc outfit** `<V> Body`: công thức outfit lock — `EDIT_CHARACTER_IMAGE` từ Body trần gốc (`character-bible.md` §6). Xóa logo → upload lại.
3. **Ref bối cảnh / sinh vật / đạo cụ nhân vật phụ** (Bài học 5, checklist #21).
4. **DỪNG — cổng duyệt:** ghép bảng ảnh, đưa đường dẫn file cho user xem. Kiểm UUID media_id mọi entity (Rule 1, `/fk-fix-uuids` nếu thấy `CAMS...`).

## 5. Sinh video R2V

1. Chạy `prompt-lock.md` checklist B trên từng `video_prompt`.
2. **Clip khó nhất trước, 1 clip**, rồi 1 clip bình thường làm mốc (Bài học 2) — mỗi lần đều hỏi user trước.
3. Cả loạt: một `POST /api/requests/batch` với `type: "GENERATE_VIDEO_REFS"` (Omni Flash `abra_r2v_<duration>s`, RPC `MZZa6b`). Server tự giãn mọi request Flow 45–60s; với video: 1 video một lúc, xong mới gửi tiếp (memory 2026-10-07). Dừng ngay khi gặp `UNUSUAL_ACTIVITY` / `QUOTA`.
4. Theo dõi: `GET /api/requests/batch-status?video_id=<VID>&type=GENERATE_VIDEO_REFS`.
5. Sinh lại 1 scene R2V đã COMPLETED: PATCH `horizontal_video_status: PENDING` rồi gửi lại `GENERATE_VIDEO_REFS` (Bài học 14). Lỗi content filter → đề xuất prompt đã làm sạch, chờ user đồng ý (Rule 17 + 29).

## 6. Review → upscale → xóa logo → concat (Rule 18, 32)

1. Mỗi clip 720p xong → tải ngay về `${OUTDIR}/scenes/scene_{idx}_{sid}.mp4`. **Chưa xóa logo.**
2. `/fk-review-video` (light) trên bản 720p thô: scorecard 6 tiêu chí + lỗi Critical/High/Minor, đối chiếu checklist B của `prompt-lock.md`. Bật Review Board `python tools/review_server.py 8200`.
3. **DỪNG — user duyệt từng clip.** Clip < 7.5 hoặc user chê: sửa `video_prompt` (xung đột với prompt user đã duyệt → đưa danh sách cho user chọn) → sinh lại ở 720p. Tối đa 2 vòng.
4. Chỉ clip đã duyệt: `UPSCALE_VIDEO` (1080p, `p0UkFb`) → `${OUTDIR}/1080/scene_{idx}_{sid}_1080p.mp4` → `remove_watermark_video` → `..._1080p_clean.mp4`.
5. `/fk-concat` cắt thẳng tại khung che (không crossfade, không text overlay); trim `-ss 1` đầu mỗi clip. Chỉ thêm `--tts` nếu user chọn lồng tiếng thay thoại native.

## 7. Dự án nhiều tập — series manifest

Tập mới mang theo **mặt `<V>` + Body trần gốc** của vlogger: mặt qua `scripts/series_manifest.py bootstrap --only "<V>" --flow-project-id …`, Body trần qua `source_media_id`; rồi EDIT ra `<V> Body` mặc outfit của tập theo công thức outfit lock. Chi tiết: `cinematic-toolkit.md` §5 và `character-bible.md` §6. Ref bối cảnh luôn làm mới.

## 8. Dự phòng khi Google chặn sinh tự động → xuất file import thủ công

**Khi nào đề xuất:** lệnh sinh qua FlowKit bị `PUBLIC_ERROR_UNUSUAL_ACTIVITY` (không có `[HIJACK]`) **từ 2 lần chạy thử 1 request trở lên**, dù extension đúng bản, đã xóa cookie, và bấm tay trên giao diện Flow vẫn sinh được. Khi đó dừng gửi request và đề xuất với user xuất kịch bản ra JSON để import vào công cụ tạo thủ công.

```bash
python tools/export_flow_import.py <PROJECT_ID> --main <Vlogger>   --upload "<Vlogger>=C:/path/face_clean.jpg"   --refs-dir output/<slug>/refs --script output/<slug>/script.md   --out output/<slug> --time-capsule "<Địa điểm>, <năm> — <vibe>"
# → output/<slug>/kich-ban-vlog/<project-slug>/<project-slug>.json + base-ref/*.jpg
```

- **Template chuẩn:** `flow-import-template.json` cùng thư mục (node `upload` / `image` / `video`, `promptParts` gồm `text` + `image_ref`, `refImageIds`, `sources`, `voiceId`, `dialog`, `edges`).
- **Ánh xạ R2V:** mỗi node video tham chiếu thẳng các ảnh ref (`image_ref` + `refImageIds`), `sources: []`, `model: abra_r2v_<duration>s`.
- **Entity có ảnh local** (`--upload` hoặc `<slug>_clean.jpg` / `<slug>.jpg` trong `--refs-dir`) thành node `upload`, ảnh copy vào `base-ref/`. Entity chưa có ảnh thành node `image` với prompt lấy từ `description`.
- **Thoại:** lấy chính xác từ Clip JSON trong `script.md`. Clip của vlogger có `voiceId` + `voiceCharId: "char-main"`; clip của dân bản địa có `speaker` riêng.
- Ảnh trong `base-ref/` phải là **bản đã xóa logo**. Chạy lại lệnh sau khi làm sạch ảnh.
- Copy cả thư mục `kich-ban-vlog/` vào thư mục gốc của công cụ import (đường dẫn `file` trong JSON có dạng `kich-ban-vlog/<slug>/base-ref/...`).
