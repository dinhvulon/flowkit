# Channel branding — TimeTravelJapanAI

Cách sinh: `POST /api/projects/{pid}/generate-thumbnail` với `character_names: ["Nora"]`, nên mặt lấy từ ảnh ref của Nora.

Endpoint này tự chèn phần mở đầu prompt của material project vào trước prompt. Material hiện là `phone_vlog`, phần mở đầu là "ultra-wide 0.5x front camera…", sẽ làm méo chân dung. Vì vậy trước khi sinh 2 ảnh này cần PATCH tạm material project → `realistic`, sinh xong đổi lại `phone_vlog`.

## 1. Avatar (PORTRAIT → cắt vuông 800×800)

YouTube hiển thị avatar dạng hình tròn, nhỏ tới 48px. Vì vậy mặt phải nằm giữa, chiếm khoảng 60% khung, nền đơn giản.

```
Studio beauty portrait of the woman from the reference image: use only her face, face shape, grey-green eyes, freckles, pink flush, honey-blonde high wavy ponytail with long curtain bangs and small gold hoop earrings; she is NOT wearing the fur parka. Head-and-shoulders framing, face centered in the frame and filling most of it, slight three-quarter turn, warm confident smile, looking straight into the lens. She wears an elegant fitted evening dress in deep emerald satin with a deep V neckline showing some cleavage and bare shoulders, thin straps. Soft warm studio key light, gentle rim light on her hair, smooth dark teal background with a faint golden glow behind her head. 85mm lens, shallow depth of field, photorealistic, real skin texture. No text, no logo, no watermark.
```

Hậu kỳ: cắt vuông quanh mặt rồi scale về 800×800 (`ffmpeg -vf "crop=iw:iw:0:(ih-iw)/3,scale=800:800"`).

## 2. Ảnh bìa (LANDSCAPE → 2560×1440)

Vùng YouTube hiển thị trên mọi thiết bị là **1546×423 ở chính giữa**, tức khoảng 60% chiều ngang × 29% chiều cao. Nora và chữ phải nằm gọn trong vùng này, phần ngoài chỉ là nền (TV thấy toàn bộ, điện thoại bị cắt hai bên).

Bước 1. AI sinh nền và nhân vật, **không có chữ**:

```
Wide cinematic 16:9 YouTube channel banner background. In the exact center, small in the frame, the woman from the reference image (same face, honey-blonde ponytail with curtain bangs) seen from the waist up, occupying only the central quarter of the image height, warm smile, wearing the same elegant emerald satin dress with a deep V neckline. Behind her a large softly glowing golden circular time-portal ring. The background fades from a snowy Ice Age mammoth steppe at dusk on the left to a Japanese street with cherry blossoms and paper lanterns at night on the right, both soft and out of focus. Dark, rich, cinematic colors, everything important kept in the center, edges calm and empty. Photorealistic. No text, no letters, no logo, no watermark.
```

Bước 2. Chèn chữ bằng ffmpeg ở giữa, đè lên trước Nora, ngang ngực để không che mặt. Làm vậy để chữ đúng chính tả và nằm chắc trong vùng an toàn (AI hay viết sai chữ dài như "TimeTravelJapanAI"):

```bash
ffmpeg -y -i banner_raw.png -vf "scale=2560:1440,drawtext=fontfile='C\:/Windows/Fonts/segoeuib.ttf':text='TimeTravelJapanAI':fontsize=96:fontcolor=white:borderw=4:bordercolor=black@0.6:shadowx=3:shadowy=3:x=(w-text_w)/2:y=(h-text_h)/2+70" banner_2560x1440.png
```

Kiểm tra: chữ cao khoảng 96px (nhỏ, gọn) và toàn bộ Nora cùng chữ nằm trong khung 1546×423 ở giữa.
