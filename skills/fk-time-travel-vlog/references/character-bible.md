# Character Bible — khóa nhân vật, giọng và bộ ref

Đọc ở **Bước 2** của `SKILL.md`. Mục này thay mục 2 / 2b cũ.

## 1. `CHARACTER_LOCK` — khóa ngoại hình

Một khối cố định, **dán nguyên văn vào entity `description` của `<Vlogger>` và KHÔNG sửa giữa các clip**. Video mẫu giữ mặt nhân vật giống hệt suốt 10 phút — đây là điều kiện sống còn của độ chân thực.

Gồm: mặt (tuổi, dáng mặt, mắt, tàn nhang/nốt ruồi), tóc (màu, kiểu buộc, vị trí cột tóc, mái — Bài học 55), trang phục thời kỳ (kiểu áo, màu, cổ áo, thắt lưng — **không nhuộm màu/vải công nghiệp hiện đại**), giọng (`voice_description`).

**Không mô tả thiết bị quay** (điện thoại, gậy selfie, màn hình) trong `CHARACTER_LOCK` hay bất cứ đâu đi vào prompt — nhắc tới thiết bị, kể cả câu phủ định, làm model vẽ thiết bị ra (Bài học 23, 33; CLAUDE.md Rule 30). Góc máy chỉ tả bằng câu khung ở `prompt-lock.md` khối 1.

Mẫu (thay giá trị, tên do bạn đặt, rồi đóng băng):
```
CHARACTER_LOCK:
Nora, a 26-year-old Western woman with a heart-shaped face, hazel-green eyes, dense freckles across nose and cheeks,
bright copper-red hair in a high bun held by a dark wooden hairpin, a few loose strands at the temples,
wearing an era-appropriate [dark indigo cross-collar hemp robe with a white inner collar and a plain dark sash].
Voice: Laomedeia — upbeat, mid-high pitched, energetic expressive conversational female voice, fast confident vlog delivery with dry humor, rises into real cracking screams when in danger, drops to a fast whisper when hiding.
```
Tên trong `CHARACTER_LOCK`, tên entity và tên người nói trong `video_prompt` phải **trùng nhau tuyệt đối** (mẫu gốc từng lệch Nora/Mia — đừng lặp lại).

Nhân vật **mặc đồ của thời kỳ ngay từ clip đầu** để "trà trộn"; yếu tố gây tò mò là ngoại hình khác biệt (tóc màu nổi, người ngoại quốc). Không có cảnh "vừa rơi xuống" mặc đồ hiện đại, trừ khi user yêu cầu rõ phong cách hài "lạc loài".

## 2. `VOICE_LOCK` — khóa tính cách (góp ý của user, 2026-10-01)

`CHARACTER_LOCK` khóa ngoại hình và chất giọng; cách nói (vlogger là ai, nói nhanh hay chậm, đùa kiểu gì, sợ gì, không bao giờ nói gì) khóa bằng `VOICE_LOCK` theo `voice-bible.md` mục 1. Ghi `VOICE_LOCK` vào `script.md` ngay dưới `CHARACTER_LOCK`, không sửa giữa các clip. `VOICE_LOCK` **không** dán vào entity `description` hay `video_prompt`; nó là luật để viết thoại, thứ đi vào prompt là câu thoại và tag cách diễn đạt.

## 3. Giọng — Laomedeia, 1 giọng mỗi clip

- Vlogger nữ: `voice_description` theo chuẩn **Laomedeia** (Google Gemini-TTS, khối mẫu ở trên). Slot 7 của Omni Flash `MZZa6b` mặc định `[["laomedeia"]]`.
- Thoại nhúng thẳng trong sub-clip: `0-3s / 3-6s / 6-8s` (clip 10s: `6-10s`), dạng `Nora says (tag cách nói): "..."` để `abra_r2v` tự sinh khẩu hình native.
- Slot 7 chỉ gửi **một** voice id, lấy từ entity **đầu tiên theo thứ tự DB** có `voice_description` → **chỉ vlogger khai báo voice**. Gửi 2 giọng làm clip thất bại (test 2026-10-05).

## 4. Nhân vật phụ nói ngôn ngữ không hiểu được (user chốt 2026-10-05)

Thay cả kiểu "người bản địa câm, môi khép" lẫn kiểu "Translator POV" cũ (vlogger dịch lại lời họ). Chi tiết ở `story-engine.md` mục 13.

- Nhân vật phụ **được nói**, bằng tiếng cổ / tiếng bịa người xem không hiểu. Không bao giờ nói tiếng Anh, không phụ đề, không khai báo `voice_description`.
- **Agent tự chọn giọng** cho mỗi nhân vật phụ có thoại từ danh sách 30 giọng ở `voice-bible.md` mục 0b (theo giới, tuổi, vai; không trùng id; cách vlogger ít nhất 1 bậc cao độ), ghi vào cột `Voice` của bảng nhân vật trong `script.md`, rồi đổi id thành câu mô tả giọng cố định trong prompt.
- `video_prompt` ghi rõ **ai nói, giọng gì, ở sub-clip nào**, không nói chồng: `3-5s: The Leader speaks in a deep, gravelly male voice — short guttural non-English sounds, no recognizable words; Nora stays silent.` → `5-8s: Nora says (hushed): "..."`.
- Vlogger phản ứng với **giọng điệu**, **không dịch nội dung** (`"No idea what he said. But that wasn't a question."`). Có thể lặp lại câu của nhân vật phụ về sau với nghĩa khác (callback).
- Test 1 clip có nhân vật phụ nói trước khi gen hàng loạt; nếu giọng vlogger phát ra từ miệng họ thì clip đó quay về môi khép, chỉ cử chỉ (Bài học 49).
- Bố cục (Rule 42): **100% selfie qua vai** (vlogger 1/3 tiền cảnh, người bản địa 2/3 hậu cảnh, tương tác bằng ánh mắt và quay đầu) **hoặc cặp shot kép** (Shot A 100% POV → cắt sang Shot B 100% selfie). Cấm lia máy 180° giữa cam trước và cam sau trong 1 shot.

## 5. Bộ ref của vlogger: Mặt + Body đã mặc outfit (Rule 46, user lock 2026-10-05)

- Vlogger có đúng **2 ref**: `<Vlogger>` (mặt & tóc) và `<Vlogger> Body` (body đã mặc hoàn chỉnh trang phục). **Không tạo entity `<Vlogger> Outfit`.**
- Ảnh `<Vlogger> Body` = `EDIT_CHARACTER_IMAGE` với `source_media_id` = Body trần gốc (EDIT 1 lần từ gốc, không chain): giữ 3 panel chính diện / 3/4 / sau lưng, khung cắt vai không lộ mặt, đúng dáng; chỉ thay quần áo. Không ma-nơ-canh, không crop. Xóa watermark (Rule 28) → upload lại → gán làm media_id của `<Vlogger> Body`.
- Mọi video: `character_names` = `["<Vlogger>", "<Vlogger> Body", <tối đa 1 ref bối cảnh/đạo cụ>]` (tối đa 3 ref/clip, Bài học 4). Cảnh POV có tay vlogger cũng dùng đúng bộ này.
- **Phụ kiện rời** (bao tay, mũ, khăn) mà cảnh sau có thao tác đeo/tháo: ảnh Body **không** đính kèm chúng (để tay trần); đưa vào bằng prompt hành động (Bài học 46, Rule 45).
- **Cổng duyệt bắt buộc:** trước bất kỳ lệnh sinh video nào, xuất ảnh Body đã mặc trang phục (đã xóa logo) cho user xem và **chờ user duyệt dáng & trang phục**.
- Khối `[ID-LOCK]` trong mọi `video_prompt`: *"her face and hair from the <Vlogger> face sheet, and her build and clothing from the <Vlogger> Body sheet (which shows her full body dressed in this handmade outfit)"*, kèm `BODY LOCK` & `OUTFIT LOCK` (Bài học 60, `prompt-lock.md` khối 5).
