# Script — Hell Creek 66 Ma (v2)

- **Slug:** `hell_creek_66_ma_v2`
- **Vlogger:** Nora (mặt `uploads/nora_main_clean.jpg` · Body đã mặc outfit sinh mới bằng 1 lần EDIT)
- **Bối cảnh:** Đồng bằng sông Hell Creek (~55°N), mùa xuân, ngày va chạm Chicxulub — 66 triệu năm trước
- **Định dạng:** 16:9 HORIZONTAL, thoại **tiếng Tây Ban Nha Mỹ Latinh (es-419, giọng Mexico City)** — đổi từ tiếng Anh ngày 2026-10-14 (bản tiếng Anh: `dialogue_en_backup.json`); prompt vẫn tiếng Anh, chỉ thoại trong ngoặc kép là tiếng Tây Ban Nha; giọng Laomedeia
- **Model:** Omni Flash R2V (`GENERATE_VIDEO_REFS` → `abra_r2v_<N>s`, RPC `MZZa6b`); mọi clip có Start Frame (E/G/P), tối đa 7 ref
- **Toán clip:** 112 lần sinh = 43×4s · 22×6s · 42×8s · 5×10s
- **Độ dài clip:** theo Rule 49 — chuỗi 4s cho cảnh dễ lỗi liền mạch; 8s cho cảnh trò chuyện; 10s cho long take
- **Thời lượng:** ≈ 10:01 (601.5s dùng được sau trim)
- **Nghiên cứu:** `.omc/research/hell_creek_66ma_v2_research.md` · **Bible:** `story-bible.md`

## Changelog

| Bản | Ngày | Thay đổi |
|---|---|---|
| v1 | 2026-10 | `output/hell_creek_66_ma` (bản cũ) |
| v2 | 2026-10-14 | Viết lại theo `/fk-time-travel-vlog` mới nhất; nghiên cứu lại (bùn xám nâu, cây lá rộng, ôn đới ấm, hạt thủy tinh 1 mm, vòm sáng dưới chân trời, seiche, T. rex đi nhanh, Infernodrakon); khóa ánh sáng tự nhiên theo giờ L0–LD; sửa khóa mặt (vàng mật ong, 22–23, không tàn nhang, không trang sức); Start Frame E/G/P + ≤7 ref; 112 lần sinh |
| v2.1 | 2026-10-14 | Theo duyệt của user: bỏ vòm sáng và chấm sáng trên trời — tín hiệu duy nhất là đàn thú phản ứng (A3-Q2 cài, A4-03 trả); kết mới: Nora đứng dậy đi theo Con Non (A5-07, A5-09); Body đã mặc outfit sinh mới bằng 1 lần EDIT; Nora Hand sinh lại |

## Khai báo chữ trên màn hình

Ba loại chữ, **tất cả làm ở hậu kỳ** (CapCut), không bao giờ sinh trong video:
1. Thẻ năm (EST-01): "66,000,000 YEARS AGO · HELL CREEK".
2. Thẻ đếm ngược C1–C8.
3. Phụ đề thoại (Vietsub / English).

Mọi `video_prompt` và `image_prompt` có câu: **"No subtitles, captions, labels, icons or text of any kind appear anywhere in the frame."**

| Thẻ | Clip | Chữ |
|---|---|---|
| C1 | A1-02 | HOUR 0 |
| C2 | A1-12a | HOUR 1 |
| C3 | A2-10 | HOUR 4 |
| C4 | A3-02 | HOUR 6 |
| C5 | A3-06b | HOUR 8 |
| C6 | A3-W1 | HOUR 10 |
| C7 | A3-Q1 | HOUR 11 |
| C8 | A4-03a | HOUR 12 |

---

## §1 GIẢ ĐỊNH

1. Nora xuất hiện ở bờ suối lúc rạng sáng, ướt sũng, không có đường về. Không giải thích cơ chế xuyên không.
2. Hư cấu được phép (Rule 14 ngoại lệ), nhưng bối cảnh, thứ tự tai họa và hành vi thú bám nghiên cứu.
3. Va chạm ở hướng SSE cách ~3.050 km. Quả cầu lửa nằm dưới đường chân trời (độ cong ~700 km). Phim **không** cho thấy dấu hiệu nào trên trời trước sóng địa chấn: tín hiệu duy nhất là đàn thú — Con Cái Già ngẩng nhìn SSE (A3-Q2, cài), cả đàn im bặt và quay về một hướng (A4-03, trả). Thú phản ứng với rung động người chưa cảm thấy là chuyện có ghi nhận; thời điểm ở đây là hư cấu được phép.
4. Thứ tự: sóng P (T+6') → S (T+10') → Rayleigh (T+13') → hạt thủy tinh ~1 mm (15–60') → seiche (sông chảy ngược) → bụi mịn → trời tối. Không sóng thần, không gió nổ trong phim.
5. Act 5 nén còn T+~2h (thực tế tối dần ở T+4–5h) — nén có chủ ý.
6. Nora không đánh nhau với thú (Rule 51). Thú không nói; Nora là người duy nhất có thoại.

## §2 CHARACTER BIBLE

### 2.1 CHARACTER_LOCK (dán vào mọi clip có Nora)

```
FACE LOCK: Nora's face is exactly the face in {{ref:Nora}}, kept 1:1 as it is in that image, including her makeup and hairstyle, in every frame. Do not redraw, restyle, retouch, age or change anything about her face. MAKEUP LOCK: keep her makeup exactly as in {{ref:Nora}}, unchanged in every frame.
```

User 2026-10-14: **không mô tả lại nhân vật** (bỏ khối ngũ quan DNA, "zero makeup", "no freckles"…). Giữ nguyên khuôn mặt **và makeup** như ảnh tham chiếu; trong prompt ảnh nhắc thẳng ảnh ref ngay tại câu khóa (`{{ref:Nora}}` → chip ảnh của Flow).

Giọng (chỉ Nora có `voice_description`): **Laomedeia** — upbeat, mid-high, energetic conversational female voice, fast confident vlog delivery with dry humor; rises into real cracking screams in danger; drops to a fast whisper when hiding.

### 2.2 BODY LOCK

```
BODY LOCK: Nora's build and proportions match the Nora Body reference sheet exactly: a tall young woman (178 cm) with natural, normal proportions. Her body shape never changes from frame to frame.
```

User 2026-10-14: hình thể bình thường, **không** thêm mô tả ngực to / đồng hồ cát — ảnh Nora Body đã sinh là tham chiếu duy nhất (thay khối cũ và Rule 52 §3 / prompt-lock B27 cho dự án này).

### 2.3 OUTFIT LOCK

```
OUTFIT LOCK: Nora wears the exact field outfit shown in the Nora Body reference sheet (NO fur, NO hood, NO shearling collar, NO cloak, NO modern logo, NO outfit variations). From the very first frame to the last, Nora is fully dressed in the complete outfit. No part of the outfit appears, disappears or changes.
```

Từ **A3-07** trở đi thêm: `The turtle-shell flask is gone; only a short snapped plant-fibre cord end hangs at her left hip.`
Trang phục **không bao giờ** được tả lại bằng lời (Rule 52) — chỉ trỏ vào ref.

### 2.4 ID-LOCK

```
[ID-LOCK] Nora keeps her face and hair from the Nora face sheet, and her build and clothing from the Nora Body sheet (which shows her full body dressed in this field outfit). Her face, hair colour, hairline, eye colour and body proportions are identical in every frame and never drift.
```

### 2.5 Tài sản ref (16:9, chi tiết prompt trong `ref_prompts.json`)

| Mã | Entity | Loại | Việc cần làm |
|---|---|---|---|
| N | Nora | mặt | UPLOAD `uploads/nora_main_clean.jpg` (ảnh có hoa tai + dây chuyền → mọi prompt có câu no-jewelry) |
| NB | Nora Body | body đã mặc outfit | SINH MỚI: upload `uploads/nora_body_v3_clean.jpg` (Body trần) → 1 lần `EDIT_CHARACTER_IMAGE` mặc outfit (prompt trong `outfit.json`) → xóa logo → upload lại |
| NH | Nora Hand | tay | SINH LẠI (bản cũ 26 tuổi, tàn nhang) |
| BD | Bò Đực | creature sheet 3 panel | SINH |
| CG | Con Cái Già | creature sheet | SINH (mới) |
| CN | Con Non | creature sheet | SINH |
| TR | T. rex | creature sheet | SINH |
| AR | Acheroraptor | creature sheet | SINH |
| ED | Edmontosaurus | creature sheet | SINH |
| BS | Borealosuchus | creature sheet | SINH |
| IN | Infernodrakon | creature sheet | SINH |
| CA | Edmontosaurus Carcass | đạo cụ/địa điểm | SINH (ảnh đơn, không người) |
| LB | Hell Creek Bank | địa điểm | SINH |
| LC | Hell Creek Game Corridor | địa điểm | SINH |
| LW | Hell Creek Waterhole | địa điểm | SINH |

**Chính sách ref mỗi clip:** Nora trong khung → N + NB; tay trong khung → + NH; mỗi con thú chỉ khi có trong khung; đúng 1 ref địa điểm; mọi mắt xích chuỗi 4s giữ y nguyên bộ ref của mắt xích a. Nhiều nhất 6 ref (A4-08).

### 2.6 Sinh vật

| Tên nội bộ | Loài | Dấu nhận diện | Vai trò kịch | Tiếng |
|---|---|---|---|---|
| Bò Đực | Triceratops horridus ♂ | Sừng mày **trái** gãy cụt ~30 cm lộ lõi keratin, sừng phải ~1 m; sẹo nhạt nửa **trái** diềm | Đầu đàn, dọa húc, chết ở A5-05 | Gầm trầm, phì mũi |
| Con Cái Già | Triceratops horridus ♀ | Diềm bạc màu xám be, mép mẻ nhiều chỗ, lưng võng, sừng mòn ~70 cm | "Ra-đa", mở chỗ cho Nora, báo động trước va chạm (A3-Q2, A4-03) | Rền trầm ngắn |
| Con Non | Triceratops ~2 tuổi, 3 m | Sừng nụ ~10 cm, vệt trăng khuyết nhạt má **phải** | Tò mò → cứu Nora → Nora đi theo nó ở cảnh cuối | Kêu chiếp cao |
| T. rex | Tyrannosaurus rex | Sẹo dọc bên **trái** mõm, ruồi bu | Đe dọa; chỉ đi nhanh | Thở rền, không gầm |
| Acheroraptor | Dromaeosaurid | Vuốt liềm giơ cao | Rình rìa đàn | Lách cách, rít |
| Edmontosaurus | Edmontosaurus annectens | Mào thịt dọc lưng → gai đuôi, móng guốc | Đàn giẫm đạp | Kèn mũi |
| Borealosuchus | Cá sấu | Hai hàng vảy sống lưng | Chờ dưới hõm bờ | Gừ họng |
| Infernodrakon | Azhdarchid | Đi bằng khớp cánh | Bối cảnh, cất cánh xa | Im |

**Khóa không gộp:** Ba con Triceratops không bao giờ trộn dấu nhận diện; sừng gãy luôn ở bên trái Bò Đực, không bao giờ lành, không đổi bên.
**Q2:** Hình học bình mai rùa — 22 cm, treo bên hông **trái** bằng dây sợi thực vật xoắn; vỡ ở A3-06b.

## §3 MATERIAL — `cretaceous_documentary`

Định nghĩa đầy đủ trong `ref_prompts.json` → `material`.

**scene_prefix:**
> Raw handheld field documentary footage, Hell Creek river floodplain in spring 66 million years ago: small broadleaf trees with sycamore-, magnolia- and laurel-like leaves, a few fan palms and tall dawn redwoods at wet sites, horsetails at the water's edge, leaf litter and moss on grey-brown silt. Natural light only, true colours, deep focus, fine film grain, not a 3D render.

**Câu ánh sáng chung:**
> Natural sun and sky only, as on a real field day at about 55 degrees north in spring: low raking light for hours after sunrise and before sunset, angled light even at noon, soft overcast or broken cloud by default, organic micro-shadows under leaves and bodies, no artificial fill, no god rays, no rim light.

### 3.1 Khóa ánh sáng theo giờ (dán nguyên văn)

| Khóa | Clip | Câu |
|---|---|---|
| L0 bình minh | EST-01 | cool blue pre-dawn twilight turning to soft pale-gold light on the eastern horizon, low river mist lying over still brown water, damp air, muted colours, dew on leaves, long soft shadows |
| L1 sáng sớm | A1-01 → A1-14 | low raking early-morning sunlight from behind the subject, warm side light skimming the grey-brown mud and catching the edges of leaves and skin, thin haze over the river, deep soft shadows, natural documentary exposure |
| L2 giữa sáng | A2-01 → A2-15 | clear humid spring morning, sun at a moderate angle, soft broken cloud, natural dappled shade under small broadleaf trees, crisp detail, true-to-life muted greens and browns |
| L3 trưa | EST-02 → A3-05 | bright overcast midday, high thin cloud diffusing the sun, even soft light with gentle shadows under bodies, humid haze softening distant treelines, natural colour |
| L4 chiều | A3-06a → A3-16 | warm afternoon side light through scattered cumulus, moving cloud shadows sliding across the floodplain, light haze, natural contrast |
| L5 lặng trước va chạm | A3-Q1 → A4-05 | still, warm, slightly hazy spring afternoon, soft diffuse sunlight, birds and insects active, ordinary peaceful light |
| LQ rung | A4-06 → A4-P2 | giữ nguyên ánh sáng clip trước; chỉ chuyển động đổi: trees sway with no wind, water sloshing, dust shaken off branches |
| LG mưa thủy tinh | A4-10 → A4-14 | the sky above streaked with countless thin bright meteor-like trails, tiny glassy beads pattering down like fine hail, pitting the wet mud and dimpling the river surface, daylight turning hazy and brassy-orange |
| LT nhiệt | A4-15 → MASTER, CO | the whole sky glowing a dull orange-red, harsh hot diffuse light with no clear sun, shimmering heat haze, leaves curling and browning, thin smoke rising from dry leaf litter in places |
| LD tối dần | A5-01 → A5-09 | dim brownish-grey sky, sun reduced to a faint pale disc or invisible, flat murky light, fine grey dust settling on every surface, muted desaturated colours, low visibility |

Ref luôn chụp ở ánh sáng u ám trung tính để khóa giờ của từng clip quyết định thời điểm trong ngày.

### 3.2 Từ cấm → thay bằng

| Cấm | Thay |
|---|---|
| phone, smartphone, device, screen, selfie stick, gimbal | "The camera viewpoint and gripping arm are completely outside the visible frame and never seen" |
| trail | wide animal-trampled game corridor |
| god rays, volumetric | natural dappled shade / bright overcast |
| red clay | grey-brown silt, olive-grey clay |
| tree ferns | small broadleaf trees, fan palms, dawn redwoods |
| grass | low herbs, horsetails, leaf litter, moss |
| fireball, meteor shower | không tả gì trên trời trước LG; ở LG dùng thin bright meteor-like trails |
| steam, smoke plume, vapour | clean dry nostrils with faint moisture at the rim only |

### 3.3 Khối anti-CGI (mọi clip có thú)

```
Visceral living megafauna biology: rough non-reflective pachyderm hide, matte polygonal basement scales, prominent conical keratin tubercles, deep biological wrinkles at the neck and flanks, dry keratin horn sheath with hairline micro-fractures, grey-brown silt caked into crevices and on the lower limbs. Clean dry nostrils with faint moisture at the rim only, strictly NO breath vapour, NO steam. Deep focus (f/8), entire frame sharp from foreground to horizon, NO bokeh. Fine 35mm film grain, BBC natural history documentary footage. Strictly NOT a 3D render, NOT a plastic toy, NOT a museum statue, NO specular sheen, NO studio rim light, NO god rays.
```

## §4 CHUỖI NHÂN QUẢ

| # | Mắt xích | Nối |
|---|---|---|
| 1 | Nora tỉnh dậy cạnh suối, cá sấu dưới nước (A1-01) | VÌ VẬY cô im lặng, tránh mép nước |
| 2 | Xác Edmontosaurus có vết cắn (A1-03/04) | NHƯNG cô vẫn tin mình chỉ đứng xem (A1-05) |
| 3 | Thấy hõm khô dưới bờ xa — cá sấu nằm ngay dưới (A1-06) | VÌ VẬY chưa dám tới (cài cho A4-16) |
| 4 | Theo hành lang thú, gặp 3 Triceratops (A1-08 → A1-10) | NHƯNG "to = an toàn" là sai |
| 5 | Bò Đực dọa húc, Nora ngã vào bụi (A1-12) | VÌ VẬY cô quyết ngồi chờ, đọc đàn (A1-14) |
| 6 | Luật 1–2: diềm đỏ, cào chân (A2-03/05) | VÌ VẬY cô trát bùn, che lá cọ để bớt mùi người (A2-07) |
| 7 | Con Non lại ngửi, đàn im phăng (A2-08 → A2-10) | VÌ VẬY cô nấp sau khúc gỗ rêu |
| 8 | T. rex đi ngang 15 bước (A2-12) | VÌ VẬY sự im lặng của đàn thành báo động của cô (A2-14) |
| 9 | Acheroraptor rình rìa, đàn xếp tam giác, Con Cái Già mở chỗ (A2-R1 → R3) | VÌ VẬY Nora thành "đồ đạc" của đàn (A2-15) |
| 10 | Nước cạn, đàn bỏ đi (A2-16, A3-01) | NHƯNG cô trượt ngã, vỡ bình nước (A3-06) |
| 11 | Hết nước — tự lần dấu đàn về phía bắc (A3-08/09) | NHƯNG đàn Edmontosaurus giẫm đạp (A3-D2) |
| 12 | Học nghe đất (A3-D3), tìm lại đàn ở vũng nước (A3-13) | VÌ VẬY cô được đứng trong vòng canh (A3-W1 → W3) |
| 13 | Uống nước, Con Non ngủ cạnh ủng (A3-15 → Q1) | NHƯNG Con Cái Già ngẩng nhìn chân trời trống vài giây (A3-Q2) |
| 14 | False win "almost forgot" (A3-17) | NHƯNG cả đàn im bặt, diềm đỏ, quay về SSE (A4-03) — luật 1 của chính cô |
| 15 | "I'm not watching" — bỏ vai khán giả (A4-04) | VÌ VẬY cô sẵn sàng khi đất rung (A4-06/07) |
| 16 | Đàn tan, bờ sụt chặn lối, T. rex rời đi (A4-08 → P2) | NHƯNG mưa thủy tinh bắt đầu (A4-10) |
| 17 | Không biết đi đâu (A4-12) | VÌ VẬY theo Con Non về suối (A4-14) |
| 18 | Tới hõm khô đã cài ở A1-06 (A4-16) | NHƯNG sông chảy ngược, nước dâng (A4-17) |
| 19 | Nằm bẹp trong bùn dưới lá cọ, chân Con Non đặt cạnh mặt (MASTER) | VÌ VẬY cô sống |
| 20 | Bụi xám, Bò Đực chết (A5-05) | VÌ VẬY khi Con Non đi, cô đứng dậy theo nó — luật 6 (A5-07 → A5-09) |

## §5 OUTLINE 5 ACT

- **Mở phim (LT → L0):** CO cắt từ MASTER 1→8s (7.0s); EST-01 cảnh trên cao lúc rạng sáng + thẻ năm.
- **Act 1 — Arrival (Giờ 0→1, L1):** Sonic Isolation cạnh cá sấu; xác thú; misbelief "I'm just here to watch"; bình mai rùa + hõm khô; hành lang thú; dấu chân; 3 Triceratops; Bò Đực dọa húc (chuỗi A1-12); "warning, not an attack"; nhiệm vụ: ngồi chờ, đọc đàn.
- **Act 2 — Reading the herd (Giờ 1→6, L2→L3):** Con Cái Già là ra-đa; luật 1–3; bùn + lá cọ; Con Non ngửi; T. rex đi ngang (chuỗi A2-12); Acheroraptor + đàn tam giác (chuỗi A2-R2); midpoint "furniture now"; EST-02 trên cao giữa trưa; nước cạn.
- **Act 3 — The water hole (Giờ 6→11, L3→L4→L5):** đàn đi; vỡ bình (chuỗi A3-06); lần dấu; Edmontosaurus giẫm đạp (chuỗi A3-D2), luật 4; Infernodrakon cất cánh (chuỗi A3-12); tìm lại đàn; cá sấu trồi (chuỗi A3-W2), luật 5; uống nước; Con Non ngủ cạnh ủng; Con Cái Già ngẩng nhìn SSE (cài); false win; EST-03.
- **Act 4 — Impact (Giờ 12 → T+~1h, L5→LQ→LG→LT):** lặng giả; đàn im bặt, diềm đỏ, quay về SSE (chuỗi A4-03); "I'm not watching"; sóng P → S/Rayleigh (chuỗi A4-07); đàn tan; bờ sụt; T. rex rời đi (A4-T1/T2); mưa thủy tinh; all is lost; theo Con Non; hõm khô; seiche; bùn; lá cọ; MASTER.
- **Act 5 — The quiet (T+~2h, LD):** hết mưa thủy tinh, trời tối; "still alive"; bụi xám; Con Non gọi, không ai đáp; Bò Đực chết; "Rule six. Follow the kid."; Con Non đi, Nora đứng dậy bước theo, hai bóng tan vào bụi; cắt đen.

## §6 NHỊP DỰNG

| Phần | Lần sinh | Dựng |
|---|---|---|
| Cold open (cắt từ MASTER) + EST-01 | 1 | 12.0s |
| Act 1 | 17 | 106.5s |
| Act 2 + EST-02 | 25 | 135.0s |
| Act 3 + EST-03 | 32 | 169.0s |
| Act 4 + MASTER (6→10s) | 28 | 124.0s |
| Act 5 | 9 | 55.0s |
| **Tổng** | **112** | **601.5s ≈ 10:01** |

- Trim theo Rule 49: 4s `-ss 0.5` → 3.5s; 6s/8s/10s `-ss 1`.
- CO = MASTER 1→8s (7.0s); MASTER trong Act 4 chỉ dùng đoạn 6→10s (4.0s).
- Đổi hình mỗi 3–5s; J-cut khi cắt thẳng; không crossfade, không bumper (`/fk-cinematic-transitions`).
- Âm: ducking thoại, master −14 LUFS / −1 dBTP (`/fk-sound-design`). A5-09 im lặng hoàn toàn rồi cắt đen.

## §7 CHU KỲ GÓC MÁY R1–R6

| Mã | Góc | Dùng khi |
|---|---|---|
| R1 | POV EWS/WS | Quan sát, di chuyển, phong cảnh |
| R2 | POV tay CU | Thao tác 2 tay, chạm đất/bùn/dấu chân |
| R3 | POV nấp | Ẩn nấp, rình, Sonic Isolation |
| R4 | Selfie/OTS MCU/MS | Hook, phản ứng, tâm sự, kết cảnh |
| R5 | Máy cố định MS | Hành động toàn thân, ngã, chạy |
| R6 | Macro ECU | Chi tiết: vết cắn, hạt thủy tinh, nút thắt |

Ràng buộc (Rule 42): không 3 selfie liên tiếp; không 2 khối liền nhau cùng cỡ cảnh + góc máy; một chuỗi 4s tính là một khối; không xoay 180° trong một shot; cánh tay cầm máy luôn ngoài khung (Rule 61).

## §8 VIỆC CỦA MỖI CLIP

Mỗi clip phải làm ít nhất một việc:
1. Tăng nguy hiểm.
2. Đặt một câu hỏi.
3. Đổi quan hệ với đàn.
4. Tiến gần mục tiêu.

## §9 STORYBOARD

**Chú giải cột:**
- **Ref:** N Nora · NB Nora Body · NH Nora Hand · BD Bò Đực · CG Con Cái Già · CN Con Non · TR T. rex · AR Acheroraptor · ED Edmontosaurus · BS Borealosuchus · IN Infernodrakon · CA xác Edmontosaurus · LB bờ suối · LC hành lang thú · LW vũng nước.
- **SF (Start Frame):** **E** = `EDIT_IMAGE` với `source_media_id` = mặt Nora (Rule 63) · **G** = `GENERATE_IMAGE` (không người; cảnh chỉ có tay dùng G + NH) · **P** = khung cuối của mắt xích trước (chuỗi 4s). Tổng: G 57 · E 38 · P 17.
- **Sáng:** khóa ánh sáng §3.1.
- **Từ:** số từ thoại, khớp Rule 49 (4s 0/6–8 · 6s 0/12–15 · 8s 18–22 · 10s 0/24–28). 0 = Sonic Isolation.
- **Việc:** §8. **Beat:** nhịp kịch. **Dựng:** ghi chú cắt/thẻ.

### Mở phim

| Clip | Dur | Shot | Ref | SF | Sáng | Hình | Thoại Nora | Từ | Việc | Beat | Dựng |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **CO** | — | FIXED · MS | (= MASTER) | — | LT | **Cắt từ MASTER 1→8s** (không sinh riêng). Nora ép người dưới vách đất bờ lạch, trời cam đỏ đục, hạt thủy tinh li ti lộp độp xuống bùn xám quanh cô; cô kéo tàu lá cọ sũng nước trùm lên, một chiếc giày còn thò ra. **CẮT ĐEN.** | Down, down, the air is burning hot! / Wet mud on the arms, on everything, stay flat. / Pull the frond, boot's still out! | 22 | 1,2 | Hook: nguy hiểm tột đỉnh trước | 7.0s |
| **EST-01** | 6s | AERIAL · EWS | LB | G | L0 | Bình minh: sương nằm trên lạch nâu uốn khúc giữa đồng ngập phẳng, bãi cát vàng nhạt, rừng lá rộng thấp mùa xuân lốm đốm vài cây cọ quạt; xa xa ba chấm thú đứng ở bãi trống. Không người → **thẻ năm** | *(0 từ)* | 0 | 2 | Thở sau cold open, đặt thế giới | 5.0s |

### ACT 1 — ARRIVAL (HOUR 0 → 1 · L1)

| Clip | Dur | Shot | Ref | SF | Sáng | Hình | Thoại Nora | Từ | Việc | Beat | Dựng |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **A1-01** | 6s | POV · WS | BS,LB | G | L1 | Ngập ngang đùi giữa lạch nâu, sương sớm. Hai dải lưng sần Borealosuchus **đã nằm sẵn** cách ~5 sải tay, trôi chậm về phía máy; máy lùi dần về bãi sỏi | *(0 từ, Sonic Isolation)* | 0 | 1,2 | Nguy hiểm ngay giây 0 (Sonic Isolation: thở gấp qua mũi, nước vỗ) | 5.0s |
| **A1-02** | 8s | SELFIE · MCU | N,NB,BS,LB | E | L1 | Nora quỳ trên sỏi, ướt sũng, ngồi thẳng dậy (khớp A1-01: vừa bò lùi lên bờ). Sau lưng: hai dải lưng đã vào chỗ nước nông | Okey. Ya salí, ya salí del agua. / Eran cocodrilos, dos, y no tenían curiosidad. / Lo que tenían era paciencia. | 19 | 1 | **C1** · punchline "patient" | 7.0s |
| **A1-03** | 8s | POV · WS | CA,LB | G | L1 | Quay lưng khỏi nước: xác Edmontosaurus nằm sẵn trên bãi bùn xám cách ~15 m, lún sâu, sườn trơ, ruồi; máy tiến chậm | Okey, eso es un cuerpo. Uno grande. / Algo se comió media anoche y se fue. / Se fue, o nada más se apartó. | 22 | 1,2 | Câu hỏi: con gì ăn, còn quanh đây không? | 7.0s |
| **A1-04** | 8s | MACRO · ECU | N,NB,NH,CA,LB | G | L1 | Rãnh răng to bằng bàn tay trên xương chậu xác; bàn tay trái Nora đặt phẳng trong rãnh để so | Miren el tamaño de esa mordida. / Mi mano entera cabe en un solo diente. / Estoy parada en su cocina. | 19 | 1 | Gieo T. rex bằng hình, không gọi tên | 7.0s |
| **A1-05** | 8s | SELFIE · MS | N,NB,CA,LB | E | L1 | Nora đứng, xác ở hậu cảnh trái, lạch bên phải. **Lần duy nhất** cô nói vì sao chọn ngày này, và nói ra niềm tin sai | Yo escogí este día a propósito. / En doce horas ese cielo se incendia. / Yo nada más vine a ver. | 19 | 2 | Đồng hồ 12h chạy · misbelief (bị bẻ ở A4-04) | 7.0s |
| **A1-06** | 8s | POV · MS | N,NB,NH,BS,LB | G | L1 | Mai rùa rỗng **nằm sẵn** giữa sỏi (frame 0); hai tay nhặt lên, múc đầy ở mép nước. Ngẩng lên: bên kia lạch, dưới vách đất bùn xám cao ~2 m là **một hốc khô tối**; một dải lưng Borealosuchus nằm ngay dưới miệng hốc | Caparazón de tortuga, tamaño plato de cena. / Hay un hueco seco bajo esa orilla. / Cocodrilos justo abajo. Así que no. | 20 | 4,1 | Gieo mai rùa (vỡ A3-06) + **gieo hốc** (payoff A4-16 / MASTER) | 7.0s |
| **A1-07** | 8s | FIXED · MS | N,NB,LB | E | L1 | Máy kê trên khúc gỗ trôi. Nora đứng ngang eo, xỏ dây sợi cọ qua 2 lỗ ở vành mai, buộc vào đai ngực bên hông TRÁI | Fibra de palma torcida, por los huecos. / Si este nudo se suelta hoy mismo, / me toca beber del charco de cocodrilos. | 21 | 4 | Gieo nút buộc sẽ đứt | 7.0s |
| **A1-08** | 8s | POV · WS | LC | G | L1 | Bìa rừng lá rộng: bụi rậm dây leo, cây gãy, rêu, lá mục, không đọc được; máy lia sang miệng một **hành lang thú** bùn xám rộng chui vào rừng | Este bosque es un muro sólido. / Pero por ahí hay un paso abierto. / Y algo muy grande lo abrió. | 19 | 2,4 | "Cái gì to?" | 7.0s |
| **A1-09** | 8s | MACRO · ECU | N,NB,NH,LC | G | L1 | Dấu chân tròn rộng hơn vai, ngón tù, nước đục đọng trong lòng; mũi giày phải đặt cạnh để so | Huella redonda, más ancha que mis hombros. / El agua sigue turbia, así que es reciente. / Lo que la hizo está cerca. | 21 | 1,2 | Nó ở gần | 7.0s |
| **A1-10** | 8s | OTS · MS | N,NB,BD,CG,CN,LC | E | L1 | Nora 1/3 tiền cảnh nấp sau bụi lá, thì thầm; 2/3 hậu cảnh: ba con Triceratops gặm cây thấp ở bãi trống cách ~40 m | Ahí. Son tres, con cuernos, comiendo. / Son lo más grande de este valle. / Grande quiere decir seguro, ojalá. | 18 | 3,4 | Lần đầu thấy đàn · "I hope" gieo nghi | 7.0s |
| **A1-S1** | 8s | SELFIE · MCU | N,NB,BD,CG,CN,LC | E | L1 | Nora mỉm cười tự tin nhìn vào máy, đàn gặm cây sau lưng; cô bước ra khỏi bụi rậm | Okey, son enormes, pero solo comen plantas. / Ni van a notar algo tan chiquito. / Nada más miren, ahorita lo ven. | 20 | 2,3 | Niềm tin sai chủ quan trước cú xông | 7.0s |
| **A1-11** | 6s | POV · WS | BD,LC | G | L1 | Bước ra mép bãi; Bò Đực ngẩng đầu chậm (~1s), sừng trái gãy, diềm ửng đỏ; máy tiến 2 bước rồi dừng | *(0 từ, Sonic Isolation)* | 0 | 1,3 | Im lặng trước cú xông (Sonic Isolation) | 5.0s |
| **A1-12a** | 4s | POV · MS | BD,LC | G | L1 | **Chuỗi 4s (1/3) — xông.** Bò Đực cúi đầu, lao về máy 3 bước nặng; kết khi đầu nó to bằng nửa khung | *(0 từ)* | 0 | 1,3 | **C2** · HỎNG 1 · chuỗi khó nhất phim | 3.5s |
| **A1-12b** | 4s | POV · MS | BD,LC | P | L1 | **(2/3) — khựng.** Mở bằng Bò Đực giữa bước lao; khựng lại, cào chân trước, bùn văng về máy; máy giật lùi | *(0 từ)* | 0 | 1,3 | Dọa, không giết | 3.5s |
| **A1-12c** | 4s | POV · MS | BD,LC | P | L1 | **(3/3) — ngã.** Mở bằng Bò Đực đứng yên, máy ngả ra sau; máy ngã ngửa vào bụi cây thấp, khung lật lên tán lá non | *(0 từ)* | 0 | 1 | Kết trên tán lá (1 tiếng thét vỡ giọng, không thành lời) | 3.5s |
| **A1-13** | 8s | SELFIE · MCU | N,NB,LC | E | L1 | Nora nằm nghiêng trong bụi cây thấp, lá vắt ngang khung, thở dốc (khớp A1-12c: vừa ngã ngửa) | Se detuvo. Se detuvo a seis metros. / Eso fue una advertencia, no un ataque. / Okey, mensaje recibido, grandote. Híjole. | 19 | 3 | Thả hơi bằng dry humor | 7.0s |
| **A1-14** | 10s | FIXED · MS | N,NB,BD,CG,CN,LC | E | L1 | Máy kê trên gốc cây gãy. Nora ngồi ngang eo ở mép trái, đàn gặm cây hậu cảnh cách ~30 m | Entonces no puedo entrar ahí. Todavía no. / Me siento acá en la orilla, donde me puedan ver. / No me muevo para nada. Y espero. | 24 | 3,4 | Kết Act hỏng: vẫn ở **ngoài** đàn → **thẻ nhiệm vụ** | 9.0s |

### ACT 2 — READING THE HERD (+ EST-02 · HOUR 1 → 6 · L2 → L3)

| Clip | Dur | Shot | Ref | SF | Sáng | Hình | Thoại Nora | Từ | Việc | Beat | Dựng |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **A2-01** | 10s | POV · WS | BD,CG,CN,LC | G | L2 | Sáng muộn. Đàn gặm cây thấp; Con Cái Già ngẩng đầu chậm, đứng im 2 giây rồi cúi xuống lại | Una hora sentada acá, mirando. / Viendo a quién le hacen caso. Y no es el grandote. / Es ella. La vieja, la de la gola descolorida. | 25 | 3,2 | Ai là "radar" của đàn | 9.0s |
| **A2-02** | 6s | POV · CU | CG,LC | G | L2 | Zoom: diềm Con Cái Già ửng hồng đỏ khi nó nhìn về bìa rừng | *(0 từ)* | 0 | 3 | Tín hiệu 1 bằng hình | 5.0s |
| **A2-03** | 8s | SELFIE · MCU | N,NB,CG,LC | E | L2 | Nora thì thầm, đàn mờ hậu cảnh | Cuando la gola se pone roja, / algo les molesta. Gola roja, me alejo. / Gola pálida, avanzo un paso. | 18 | 3,4 | Luật 1 | 7.0s |
| **A2-04** | 6s | POV · WS | BD,LC | G | L2 | Bò Đực nghiêng người cào chân trước, bùn xám văng; máy lùi một bước | *(0 từ)* | 0 | 1,3 | Luật 2 bằng hình | 5.0s |
| **A2-05** | 8s | FIXED · MS | N,NB,LC | E | L2 | Máy kê gốc cây. Nora đứng thẳng ngang eo, xoay vai nghiêng, mắt cụp xuống, diễn lại cho máy | Regla dos: si raspan la pata, vete. / Me pongo de lado, ojos abajo, y aburrida. / Bien aburrida. Pero muy aburrida. | 20 | 3,4 | Học + humor (dùng lại ở A3-14) | 7.0s |
| **A2-06** | 8s | POV · MS | CN,LC | G | L2 | Vũng bùn xám ô liu giữa bãi; Con Non lăn mình, bùn phủ kín bụng và hông | El chiquito se revuelca en ese lodo. / Espanta los bichos y huele a río. / Qué listo está el chamaco, ¿eh? | 20 | 3 | Gieo bùn (payoff Act 4) | 7.0s |
| **A2-07** | 8s | FIXED · MS | N,NB,LC | E | L2 | Bùn xám **có sẵn** trên mép vũng (frame 0). Nora quệt bùn lên cẳng tay và cổ, nhặt tàu lá cọ quạt rụng giơ che đầu | Voy a copiarle todo al chiquito. / Lodo en brazos y cuello, palma arriba. / Ahora huelo igual que él. | 18 | 4 | Gieo bùn + lá cọ (payoff MASTER) | 7.0s |
| **A2-08** | 8s | OTS · MS | N,NB,CN,CG,LC | E | L2 | Nora tiền cảnh đứng im; Con Non tự đi lại, dừng cách ~3 sải tay; Con Cái Già nhìn chằm chằm hậu cảnh | No te muevas. Viene él solito. / Su mamá me está mirando muy feo ahorita. / Hola, amiguito. Hola, hola, chiquito. | 19 | 3 | Quan hệ đầu tiên | 7.0s |
| **A2-09** | 4s | MACRO · ECU | N,NB,NH,CN | G | L2 | Mõm Con Non hít bùn trên cẳng tay Nora (cẳng tay ở đáy khung), kêu 2 nốt cao, rút về | Me está oliendo. / Huelo a río, chiquito. | 7 | 3 | Khoảnh khắc ấm | 3.5s |
| **A2-10** | 6s | POV · WS | BD,CG,CN,LC | G | L2 | **Cả đàn đứng sững**, ngừng nhai, đầu ngẩng chậm; Con Cái Già trước tiên; chim im bặt | *(0 từ, Sonic Isolation)* | 0 | 1,2 | **C3** · tín hiệu đứng sững (Sonic Isolation) | 5.0s |
| **A2-11** | 6s | HIDE · MS | N,NB,NH,LC | G | L2 | Máy lùi thấp, chui sau khúc cây đổ phủ rêu, dừng ở khe giữa gỗ và bụi; tàu lá cọ bỏ lại cạnh gỗ | *(0 từ)* | 0 | 1 | Nấp | 5.0s |
| **A2-12a** | 4s | HIDE · WS | TR,LC | G | L2 | **Chuỗi 4s (1/3) — vào.** Qua khe gỗ: nước vũng rung, bụi cây mép phải rung; đầu + vai T. rex vào từ mép phải, chậm, ruồi quanh mõm | *(0 từ, Sonic Isolation)* | 0 | 1 | Đỉnh căng Act 2 · chuỗi khó thứ 2 (Sonic Isolation) | 3.5s |
| **A2-12b** | 4s | HIDE · WS | TR,LC | P | L2 | **(2/3) — ngang qua.** Mở bằng đầu T. rex giữa khe; thân đi phải→trái cách ~15 bước, không quay đầu về máy | *(0 từ)* | 0 | 1 | Nín thở | 3.5s |
| **A2-12c** | 4s | HIDE · WS | TR,LC | P | L2 | **(3/3) — ra.** Mở bằng thân sau giữa khe; đuôi lướt qua, ra mép trái; hành lang trống, bụi lắc rồi đứng | *(0 từ)* | 0 | 1 | Thả | 3.5s |
| **A2-13** | 6s | MACRO · ECU | N,NB,NH,LC | G | L2 | Bàn tay Nora ép phẳng trên bùn sau gỗ; nước trong một vết chân nhỏ rung theo từng bước đập, yếu dần; tay nhấc lên | *(0 từ)* | 0 | 1 | Âm thanh kể chuyện | 5.0s |
| **A2-14** | 8s | SELFIE · MCU | N,NB,LC | E | L2 | Nora vẫn nằm thấp sau gỗ, quay mặt vào máy (khớp A2-13: tay vừa nhấc khỏi bùn), run | Pasó justito al lado de mí. / Se congelaron antes de que yo oyera algo. / Su silencio ahora es mi alarma. | 20 | 3,4 | Bài học chốt, dùng lại ở Act 4 | 7.0s |
| **A2-R1** | 6s | HIDE · MS | AR,LC | G | L2 | Hai con Acheroraptor cỡ chó sói đồng cỏ, phủ lông nâu xám, bước thận trọng ở mép hành lang bám theo vệt T. rex | *(0 từ, Sonic Isolation)* | 0 | 1 | Kẻ ăn thừa bám vệt T. rex (Sonic Isolation) | 5.0s |
| **A2-R2a** | 4s | POV · WS | BD,CG,CN,LC | G | L2 | **Chuỗi 4s (1/3) — khép.** Con Cái Già khịt trầm, đàn giật mình; ba con xoay sừng ra ngoài, đứng tam giác che Con Non; Nora ở ngoài | *(0 từ)* | 0 | 1,3 | Đàn khép vòng | 3.5s |
| **A2-R2b** | 4s | POV · WS | BD,CG,CN,AR,LC | P | L2 | **(2/3) — rình mép.** Mở bằng tam giác sừng; hai Acheroraptor dừng ở rìa bụi, mắt khóa vào máy, gừ nhẹ | *(0 từ)* | 0 | 1 | Ở mép tức là làm mồi | 3.5s |
| **A2-R2c** | 4s | POV · WS | BD,CG,CN,AR,LC | P | L2 | **(3/3) — khe hở.** Mở bằng raptor mép trái; Con Cái Già nhìn thẳng máy, diềm nhạt đi, nhích chân trước mở một khe giữa nó và Bò Đực | *(0 từ)* | 0 | 3,4 | Đàn mở cửa | 3.5s |
| **A2-R3** | 8s | SELFIE · MCU | N,NB,CG,LC | E | L2 | Nora ngồi nép sát chân trụ Con Cái Già trong tam giác, thở dốc, nhìn ra ngoài nơi raptor đang bỏ đi | Regla tres: en la orilla eres carnada. / Ellos no cerraron el círculo por mí, / pero sí me dejaron entrar. | 19 | 3,4 | Luật 3: ở mép là làm mồi | 7.0s |
| **A2-R4** | 6s | POV · CU | N,NB,NH,CG,AR,LC | G | L2 | Chân trước khổng lồ của Con Cái Già chắn sát sườn Nora (tay Nora áp vào da nó); ngoài xa hai Acheroraptor lủi vào bụi | Quietecita. Ella me tapa. / Se están yendo los dos. / Gracias, señora, en serio. | 13 | 3 | Tấm khiên sống | 5.0s |
| **A2-15** | 8s | FIXED · MS | N,NB,BD,LC | E | L2 | Đàn gặm lại; Nora ngồi ngang eo cách ~20 bước, Bò Đực liếc cô rồi nhai tiếp | A veinte pasos. Me miró y siguió. / Todavía no soy parte de la familia. / Pero ya soy un mueble más. | 20 | 3,4 | **THẮNG MỘT PHẦN** (midpoint) | 7.0s |
| **EST-02** | 4s | AERIAL · EWS | LC | G | L3 | Rất cao, giữa trưa trời mây mỏng: tán rừng lá rộng vô tận, lạch uốn khúc; bóng mây trôi chậm trên tán; ba chấm thú nhỏ cạnh một hố nước đang cạn. Thế giới rộng và vô tư | *(0 từ)* | 0 | 2 | Thời gian trôi · thế giới không hay biết | 3.5s |
| **A2-16** | 8s | POV · CU | N,NB,NH,LC | G | L3 | Hai tay nghiêng mai rùa: chỉ còn một lóng tay nước sóng sánh | Problema. Es toda el agua que queda. / Ya es mediodía, caminé toda la mañana, / y el arroyo está lleno de cocodrilos. | 21 | 1,2 | Đồng hồ thứ hai: nước | 7.0s |

### ACT 3 — THE WATER HOLE (+ EST-03 · HOUR 6 → 11 · L3 → L4 → L5)

| Clip | Dur | Shot | Ref | SF | Sáng | Hình | Thoại Nora | Từ | Việc | Beat | Dựng |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **A3-01** | 8s | SELFIE · MCU | N,NB,BD,CG,CN,LC | E | L3 | Nora bật dậy; sau lưng cả đàn quay đầu cùng một hướng, bắt đầu rời đi | Espera, se van todos, al mismo lado. / Ellos saben exactamente dónde está el agua. / ¡Espérenme, voy con ustedes, ya voy! | 20 | 4,2 | Mục tiêu có hạn chót | 7.0s |
| **A3-02** | 4s | POV · WS | BD,CG,CN,LC | G | L3 | Chạy: đàn đi bước nhanh trên hành lang thú 20 m phía trước; khung giật theo bước | ¡Esperen, esperen! / Corren más que yo. | 6 | 4 | **C4** (thở) | 3.5s |
| **A3-03** | 8s | OTS · MS | N,NB,BD,CG,CN,LC | E | L3 | Nora tiền cảnh đi nhanh, mồ hôi, bùn xám khô nứt trên tay; đàn nhỏ dần hậu cảnh | Caminan más rápido de lo que corro. / Cada minuto me sacan otros cien metros. / Sigue, Nora, sigue moviéndote. Ándale. | 19 | 1,4 | Tụt lại | 7.0s |
| **A3-04** | 4s | MACRO · ECU | N,NB,NH,LC | G | L3 | Giày bước vào một dấu chân tròn mới, nước trong lòng còn rung | Esta huella es nueva. / Siguen cerca. | 6 | 4 | Nhịp dồn | 3.5s |
| **A3-05** | 4s | POV · MS | LW | G | L3 | Trèo xuống bờ đất lở ra bãi bùn khô nứt; rặng cây cao xa xa | Ay, ay, resbala. / Abajo, todo seco. | 6 | 1 | Nhịp dồn (thở) | 3.5s |
| **A3-06a** | 4s | POV · CU | N,NB,NH,LW | G | L4 | **Chuỗi 4s (1/3) — trượt.** Nhìn xuống chân: giày phải đặt lên phiến đá phẳng trơn, trượt; mai rùa văng ra xa hông trái theo dây | *(0 từ)* | 0 | 1 | HỎNG 2 bắt đầu | 3.5s |
| **A3-06b** | 4s | POV · CU | N,NB,NH,LW | P | L4 | **(2/3) — vỡ.** Mở bằng mai rùa lủng lẳng; dây sợi cọ đứt, mai rơi thẳng xuống đá, nứt đôi, nước bắn | *(0 từ)* | 0 | 1 | **C5** · vỡ mai rùa (1 tiếng hớp hơi) | 3.5s |
| **A3-06c** | 4s | POV · CU | N,NB,NH,LW | P | L4 | **(3/3) — ngấm.** Mở bằng hai nửa mai trên đá, nước tràn ra cát; vệt sẫm loang rồi co mất vào cát | *(0 từ)* | 0 | 1 | Mất nước | 3.5s |
| **A3-07** | 8s | SELFIE · MCU | N,NB,LW | E | L4 | Nora quỳ, tay trái cầm hai nửa mai rùa (khớp A3-06c: vệt ướt vừa ngấm); ở hông trái chỉ còn đầu dây đứt | No, no, no. Era toda el agua. / La arena se la tomó en dos segundos. / Y ellos ya se fueron. | 20 | 1 | Mất cả nước lẫn đàn | 7.0s |
| **A3-08** | 6s | MACRO · ECU | N,NB,NH,LW | G | L4 | Nhìn thẳng xuống: dấu chân tròn trên bùn nứt, lòng dấu còn ướt sẫm; ngón tay Nora ấn vào mép dấu, bùn lún mềm; máy ngẩng theo trục dấu tới rặng cây cao xa | Todavía está blandito, mira. / Pasaron hace nada. / Van para esos árboles altos. | 12 | 4 | Cô **tự đọc** được (thở chậm lại) | 5.0s |
| **A3-09** | 8s | POV · EWS | LW | G | L4 | Bãi bùn nứt mênh mông, vệt dấu chân đàn chạy thẳng về rặng cây đầm lầy cao (bách nước) phía bắc; không thấy con nào | Huellas frescas, el lodo sigue mojado adentro. / Van al norte, hacia esos árboles del pantano. / Pantano quiere decir agua. Sigue las patas. | 22 | 1,4 | Bãi trống | 7.0s |
| **A3-D1** | 8s | SELFIE · MCU | N,NB,ED,LW | E | L4 | Nora dừng trên bãi bùn, nhìn sang phải: đàn Edmontosaurus mỏ vịt lững thững đi qua hậu cảnh | Otra manada: Edmontosaurus, con pico de pato. / Quiero leerles la gola, pero no tienen gola. / Cero señales en la cara. | 20 | 2,3 | Không đọc được bằng luật diềm | 7.0s |
| **A3-D2a** | 4s | POV · WS | ED,LW | G | L4 | **Chuỗi 4s (1/3) — giật mình.** Đàn Edmontosaurus đồng loạt ngẩng đầu, rống trầm qua mũi, quay mình | *(0 từ, Sonic Isolation)* | 0 | 1 | Đàn mỏ vịt hoảng (Sonic Isolation) | 3.5s |
| **A3-D2b** | 4s | POV · WS | ED,LW | P | L4 | **(2/3) — đất rung.** Mở bằng đàn hướng về máy; chạy sầm sập cắt ngang trước mặt cách ~10 m, bùn bắn; khung chao | *(0 từ)* | 0 | 1 | Đất rung | 3.5s |
| **A3-D2c** | 4s | POV · MS | N,NB,NH,LW | P | L4 | **(3/3) — áp đất.** Mở bằng bãi trống, bụi lơ lửng; máy hạ thấp, hai bàn tay Nora áp chặt mặt bùn còn rung | *(0 từ)* | 0 | 4 | Cảm nhận rung chấn | 3.5s |
| **A3-D3** | 8s | SELFIE · MCU | N,NB,LW | E | L4 | Nora quỳ, hai tay vẫn áp trên bùn, mắt mở to nhìn theo vệt bụi xa | Regla cuatro: sin cuernos, no hay gola. / ¿No hay caras? Entonces escuchas el suelo. / La tierra les avisó primero. | 19 | 3,4 | Luật 4: nghe đất | 7.0s |
| **A3-10** | 6s | POV · WS | IN,LW | G | L4 | Cách ~60 m: một con Infernodrakon (thằn lằn bay cao ngang người) sải bước bốn chân trên bãi, mổ xuống bùn; máy khựng lại | *(0 từ, Sonic Isolation)* | 0 | 1 | Sinh vật lạ (Sonic Isolation) | 5.0s |
| **A3-11** | 8s | SELFIE · MCU | N,NB,IN,LW | E | L4 | Nora cúi thấp thì thầm, Infernodrakon nhỏ ở hậu cảnh | Un reptil volador caminando, de mi altura. / Anda cazando cosas chiquitas en el lodo. / Y yo soy una cosa chiquita. | 20 | 1 | Dry humor dưới áp lực | 7.0s |
| **A3-12a** | 4s | POV · WS | IN,LW | G | L4 | **Chuỗi 4s (1/2) — bật lên.** Infernodrakon hạ thấp người, chống hai cánh gấp xuống bùn, bật lên | *(0 từ)* | 0 | 2 | Cất cánh | 3.5s |
| **A3-12b** | 4s | POV · WS | IN,LW | P | L4 | **(2/2) — bay đi.** Mở bằng Infernodrakon trên không thấp; vỗ cánh bay xa qua đồng ngập, nhỏ dần | *(0 từ)* | 0 | 2 | Thả | 3.5s |
| **A3-13** | 8s | POV · EWS | BD,CG,CN,LW | G | L4 | Hố nước nâu co hẹp dưới rặng bách nước, vành bùn giẫm nát; ba con đứng trong và quanh nước | ¡Los encontré nada más leyendo sus patas! / Toda la manada, en la única agua cerca. / Despacito ahora. Bajita y aburrida. | 20 | 3,4 | Đuổi kịp nhờ chính mình | 7.0s |
| **A3-W1** | 6s | POV · WS | BD,CG,CN,LW | G | L4 | Đàn không uống cùng lúc: Bò Đực và Con Non cúi uống, Con Cái Già đứng ngẩng đầu canh mép nước đục | *(0 từ, Sonic Isolation)* | 0 | 1,3 | **C6** · uống theo lượt (Sonic Isolation) | 5.0s |
| **A3-W2a** | 4s | POV · CU | BS,CG,LW | G | L4 | **Chuỗi 4s (1/2) — trồi.** Chóp mõm và hai mắt Borealosuchus trồi chậm lên mặt nước đục, không tiếng động, gần chân Con Cái Già | *(0 từ)* | 0 | 1 | Cá sấu rình hố nước | 3.5s |
| **A3-W2b** | 4s | POV · CU | BS,CG,LW | P | L4 | **(2/2) — lặn.** Mở bằng mõm cá sấu; Con Cái Già dậm chân trước xuống nước, sóng tung; cá sấu lặn mất | *(0 từ)* | 0 | 1 | Con canh xua đuổi | 3.5s |
| **A3-W3** | 8s | SELFIE · MCU | N,NB,CG,LW | E | L4 | Nora ngồi chờ ở rìa bùn, quan sát Con Cái Già canh | Regla cinco: turnos. Nunca beben todos juntos. / Siempre hay una cabeza arriba, vigilando el fondo. / Yo bebo cuando ella vigila. | 20 | 3,4 | Luật 5: uống theo lượt | 7.0s |
| **A3-14** | 8s | FIXED · WS | N,NB,BD,LW | E | L4 | Máy kê trên tảng đất cao. Bò Đực chắn mép nước, diềm đỏ; Nora dừng, xoay vai nghiêng, cụp mắt (luật A2-05); diềm nhạt dần, Bò Đực cúi uống; Nora bước một bước | El grandote tapa el agua. Gola roja. / De lado, ojos abajo, aburrida. Muy aburrida. / Gola pálida. Okey. Un paso. | 19 | 3,4 | Bài Act 2 qua kiểm tra | 7.0s |
| **A3-15** | 8s | FIXED · MS | N,NB,LW | E | L4 | Máy kê trên tảng đất. Nora quỳ ngang eo ở mép nước, vốc nước bằng hai tay uống, đàn hậu cảnh | Lodosa, fría, sabe a pata de dinosaurio. / La neta, el mejor trago de mi vida. / No le cuenten a nadie. | 20 | 4 | Thở | 7.0s |
| **A3-16** | 8s | OTS · MS | N,NB,CN,LW | E | L4 | Con Non lội tới đứng cách một sải tay, kêu 2 nốt; Nora tiền cảnh thì thầm | Oye, amiguito, me volviste a encontrar. / A un brazo. Nadie me dejó tan cerca. / Yo con eso me conformo. | 19 | 3 | Quan hệ lên một bậc | 7.0s |
| **A3-Q1** | 8s | FIXED · MS | N,NB,CN,LW | E | L5 | Con Non nằm xuống bùn cạnh chân Nora, đầu tựa vào ống giày cô thở êm; Nora cúi nhìn | Ya nada más queda una hora. / Duerme como si fuera otra tarde cualquiera. / Su pulso me late en la bota. | 20 | 3,2 | **C7** · Con Non ngủ tựa chân | 7.0s |
| **A3-Q2** | 6s | POV · WS | CG,LW | G | L5 | Con Cái Già đang uống bỗng ngừng, ngẩng đầu nhỏ nước, nhìn đăm đăm về chân trời nam-đông nam trống trơn vài giây; rồi cúi xuống uống tiếp. Trời bình thường, chim vẫn bay | *(0 từ)* | 0 | 2 | Cài: "ra-đa" bắt được gì đó (trả ở A4-03) | 5.0s |
| **A3-17** | 10s | SELFIE · MCU | N,NB,BD,CG,CN,LW | E | L5 | Ánh chiều dịu; Nora cười mệt, đàn uống nước sau lưng | Agua. Sombra. Una manada que me aguanta. / Primera vez hoy que me siento segura. Como de vacaciones. / Casi se me olvida qué día es hoy. Casi. | 26 | 2 | THẮNG GIẢ: misbelief quay lại dưới dạng yên ổn | 9.0s |
| **EST-03** | 4s | AERIAL · EWS | LW | G | L5 | Kéo lùi lên cao: đồng ngập vô tận không dấu vết người, ánh lóe hố nước ở tâm khung; một đàn chim nhỏ bay ngang | *(0 từ)* | 0 | 1,2 | Cô lập tuyệt đối · cầu sang Act 4 | 3.5s |

### ACT 4 — IMPACT (+ MASTER · HOUR 12 → T+~1h · L5 → LQ → LG → LT)

| Clip | Dur | Shot | Ref | SF | Sáng | Hình | Thoại Nora | Từ | Việc | Beat | Dựng |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **A4-01** | 6s | POV · WS | BD,CG,CN,LW | G | L5 | 6 giờ chiều, bình yên: đàn gặm cây quanh hố nước, chim và côn trùng hoạt động; máy lia chậm dọc đàn | *(0 từ)* | 0 | 2 | Bình yên giả (deceptive calm) | 5.0s |
| **A4-02** | 8s | SELFIE · MCU | N,NB,CG,LW | E | L5 | Nora thì thầm, đàn gặm bình thường sau lưng | Las seis. Hay sol, cantan los pájaros, / y nada se ve distinto, nada de nada. / A lo mejor me equivoqué de día. | 22 | 2 | Mỉa mai kịch tính | 7.0s |
| **A4-03a** | 4s | POV · WS | BD,CG,CN,LW | G | L5 | **Chuỗi 4s (1/3) — tĩnh.** Nhìn qua hố nước về phía nam-đông nam: Con Cái Già uống nước ở tiền cảnh trái, Bò Đực và Con Non gặm cây ở hậu cảnh; côn trùng rỉ rả, trời chiều yên | *(0 từ)* | 0 | 1,2 | **C8** (J-cut: âm thanh tắt trước hình) | 3.5s |
| **A4-03b** | 4s | POV · WS | BD,CG,CN,LW | P | L5 | **(2/3) — im bặt.** Côn trùng và chim cùng tắt tiếng một lúc; Con Cái Già ngẩng phắt đầu khỏi mặt nước, nước nhỏ từ mỏ, diềm đỏ dần lên. Trời vẫn y nguyên | *(0 từ)* | 0 | 1,2 | Không tiếng động · trả cài A3-Q2 | 3.5s |
| **A4-03c** | 4s | POV · WS | BD,CG,CN,LW | P | L5 | **(3/3) — cả đàn quay.** Mở bằng Con Cái Già ngẩng đầu, diềm đỏ; Bò Đực rồi Con Non lần lượt ngẩng lên, cả ba quay mặt cùng một hướng, nhìn chằm chằm vào chân trời trống trơn, đứng sững | *(0 từ)* | 0 | 1,2 | Khoảnh khắc đắt nhất phim: đàn biết trước Nora | 3.5s |
| **A4-04** | 8s | SELFIE · MCU | N,NB,CG,LW | E | L5 | Nora nhìn qua vai phải: Con Cái Già đứng sững, diềm đỏ, mặt hướng về chân trời trống; rồi Nora nhìn thẳng máy | Sabía la hora, el lugar, la distancia. / Creí que saber era poder quedarme mirando. / Pero yo ya no estoy mirando. | 20 | 1 | **Misbelief bị bẻ** (A1-05 → A4-04) | 7.0s |
| **A4-05** | 6s | POV · WS | BD,CG,CN,LW | G | L5 | Vài phút trôi: đàn đứng sững, diềm Con Cái Già đỏ, Bò Đực cào chân, Con Non ép sát Con Cái Già; chim im | *(0 từ, Sonic Isolation)* | 0 | 1,3 | Chờ (Sonic Isolation) | 5.0s |
| **A4-06** | 4s | MACRO · ECU | LW | G | LQ | Mặt hố nước rung lăn tăn vòng đồng tâm dù không gió; cả bầy chim bật khỏi cây cùng lúc (sóng P, ~6 phút) | ¿Por qué tiembla el agua? / No hay viento. | 8 | 1 | Báo trước | 3.5s |
| **A4-07a** | 4s | POV · WS | LW | G | LQ | **Chuỗi 4s (1/3) — giật.** Mặt đất giật mạnh, cây lay dù không gió, nước hố tạt lên vành bùn, bụi rũ khỏi cành; máy chao | *(0 từ)* | 0 | 1 | Sóng S · chuỗi khó thứ 3 | 3.5s |
| **A4-07b** | 4s | POV · WS | LW | P | LQ | **(2/3) — cuộn.** Mở bằng cây nghiêng; mặt đất cuộn như sóng chậm, bùn nứt; cây bách chết đổ ngang mép nước, nước bắn | *(0 từ)* | 0 | 1 | Sóng Rayleigh | 3.5s |
| **A4-07c** | 4s | POV · WS | LW | P | LQ | **(3/3) — ngã.** Mở bằng cây nằm ngang, máy chao mạnh; máy ngã nhào về trước, khung đập xuống bùn | *(0 từ)* | 0 | 1 | Kết úp trong bùn (thét vỡ giọng) | 3.5s |
| **A4-08** | 8s | SELFIE · MCU | N,NB,BD,CG,CN,LW | E | LQ | Má áp bùn, nhấc đầu lên (khớp A4-07c), bùn xám nâu trên má trái; đàn chạy mờ hậu cảnh | El valle entero rodó como agua. / La manada se rompe, se van corriendo. / ¡Párate, Nora, párate, ya, aguas! | 18 | 1 | Gấp | 7.0s |
| **A4-09** | 4s | POV · WS | BD,CG,CN,LW | G | LQ | Đàn chạy về rặng cây phía bắc, lướt qua cách ~10 m; máy chạy theo, tụt lại | ¡Espérenme! ¡No me dejen! / ¡Ya voy! | 6 | 1,3 | Bị bỏ lại (thở) | 3.5s |
| **A4-P1** | 4s | POV · MS | LW | G | LQ | Bờ đất cao phía trước sạt lở trượt xuống hố nước thành một khối bùn, chắn lối; máy khựng lại | ¡No, no, la orilla! / Se cayó todo. | 7 | 1 | Bờ sạt (thay cây cọ cháy, research) | 3.5s |
| **A4-T1** | 4s | HIDE · EWS | TR,LW | G | LQ | **Chuỗi 4s (1/2) — xuất hiện.** Bên kia bãi trống, xa: T. rex bước nhanh nặng nề ra khỏi rặng cây, đầu thấp, không nhìn về máy | *(0 từ, Sonic Isolation)* | 0 | 1 | T. rex rời đi · không săn (Sonic Isolation) | 3.5s |
| **A4-T2** | 4s | HIDE · EWS | TR,LW | P | LQ | **(2/2) — đi qua.** Mở bằng T. rex giữa bãi; tiếp tục bước nhanh nặng nề, khuất vào rặng cây phía tây; không chạy, không quay đầu | *(0 từ)* | 0 | 1 | Chúa tể cũng là nạn nhân | 3.5s |
| **A4-P2** | 6s | SELFIE · MCU | N,NB,LW | E | LQ | Nora nép sau khối bùn sạt, mặt và tóc dính bụi đất, nhìn theo hướng T. rex vừa khuất | Hasta el rey se va con prisa. / Este valle ya no es de nadie. | 14 | 1 | Không ai bất tử · Rule 51 | 5.0s |
| **A4-10** | 4s | POV · EWS | LW | G | LG | Chạy trên bãi trống; bầu trời phía trên đầy vệt sáng mảnh như sao băng, những hạt thủy tinh đầu tiên lộp độp xuống bùn quanh máy; ánh sáng chuyển màu đồng | ¿Qué cae del cielo? / ¡Pica, pica! | 6 | 1 | Mưa thủy tinh bắt đầu (~15 phút) | 3.5s |
| **A4-11** | 4s | MACRO · ECU | N,NB,NH,LW | G | LG | Hạt thủy tinh li ti (~1 mm) lộp độp xuống bùn xám quanh mũi giày đang chạy, nảy lên, chấm lỗ trên mặt vũng | Rebotan en el lodo. / ¡Y queman tantito! | 7 | 1 | Nhịp ngắn nhất phim | 3.5s |
| **A4-12** | 8s | SELFIE · MCU | N,NB,LW | E | LG | Nora ngồi thụp sau thân cây bách đổ giữa bãi trống, trời màu đồng, hạt thủy tinh lộp độp, dính trên tóc | Está lloviendo vidrio, bolitas, por todos lados. / Los perdí, ya no veo a la manada. / ¿Y ahora para dónde me voy? | 21 | 1,2 | **Đáy Act 4** (all is lost) | 7.0s |
| **A4-13** | 4s | POV · WS | CN,LW | G | LG | Con Non tách đàn lao qua trước máy cách ~5 m, không theo đàn về rừng phía bắc mà chúi xuống dốc về phía lạch | ¿Y el chiquito? / ¿Para dónde vas, chiquito? | 7 | 2,3 | Hai hướng mở ra | 3.5s |
| **A4-14** | 8s | SELFIE · MCU | N,NB,LW | E | LG | Nora vẫn ngồi thụp. 0–3s nhìn sang trái (đàn vào rừng phía bắc); 3–6s nhìn sang phải (Con Non xuống lạch cá sấu); 6–8s nhìn thẳng máy, quyết | La manada va al norte, al bosque. / El chiquito va para abajo, hacia los cocodrilos. / No se ha equivocado. Sigo al chamaco. | 22 | 2,3,4 | **Khủng hoảng:** rừng vs lạch cá sấu, cô chọn lắng nghe | 7.0s |
| **A4-15** | 4s | POV · MS | CN,LC | G | LT | Chạy theo Con Non xuống hành lang thú dốc về lạch; bầu trời đỏ cam đục, nóng, lá cong | ¡Voy, voy, chiquito! / No te me pierdas. | 7 | 4 | Bài học Act 2 dùng lần cuối (thở) | 3.5s |
| **A4-16** | 8s | OTS · MS | N,NB,CN,LB | E | LT | Nora quỳ trên mép vách đất tiền cảnh; dưới lòng lạch, Con Non đang chui vào **đúng cái hốc ở A1-06** | Ese hueco de abajo de la orilla. / El que salté hoy por los cocodrilos. / Ya se metió. Vámonos, vámonos. | 19 | 3,4 | **Payoff gieo A1-06** | 7.0s |
| **A4-17** | 4s | POV · WS | LB,CA | G | LT | Trượt xuống vách đất vào lòng lạch: nước lạch **chảy ngược**, dâng cao, cuốn khúc gỗ và cá chết; mặt nước sát dưới miệng hốc; bên kia, xác Edmontosaurus ngập nửa | ¿El río va al revés? / Está subiendo. | 7 | 1,4 | Sóng dềnh (seiche, research) | 3.5s |
| **A4-18** | 4s | MACRO · ECU | N,NB,NH,LB | G | LT | Hai tay vốc bùn ướt **có sẵn** ở mép lạch, trát lên cẳng tay và cổ | Lodo, como el chamaco. / Todo cubierto. | 6 | 4 | Payoff bùn (A2-06/07) | 3.5s |
| **A4-19** | 4s | POV · MS | N,NB,NH,LB | G | LT | Kéo một tàu lá cọ sũng nước **có sẵn** ở mép lạch, bò vào dưới vách | La palma. Encima. / Adentro, adentro, ya. | 6 | 4 | Dẫn thẳng vào MASTER (thở) | 3.5s |
| **MASTER** | 10s | FIXED · MS | N,NB,CN,LB | E | LT | **MASTER 10s**, dựng đoạn 6→10s ở đây. Máy kê vách hốc. Nora nằm nghiêng dưới vách, bùn kín tay và cổ, tàu lá cọ sũng nước nửa người, một giày thò ra; hạt thủy tinh lộp độp ngoài miệng hốc, trời cam đỏ đục. 8–10s: **bàn chân trước Con Non đặt xuống ngay cạnh mặt cô.** Im | ¡Abajo, abajo, el aire está quemando! / Lodo en los brazos, en todo, pégate al suelo. / ¡Jala la palma, la bota sigue afuera! / No te muevas. | 25 | 3,4 | **PAYOFF** | 4.0s |

### ACT 5 — THE QUIET (T+~2h · LD)

| Clip | Dur | Shot | Ref | SF | Sáng | Hình | Thoại Nora | Từ | Việc | Beat | Dựng |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **A5-01** | 6s | POV · WS | LB,CA | G | LD | Nhìn ra từ hốc: lạch xám dâng, mưa thủy tinh đã ngừng, bụi xám mịn lắng; trời nâu xám mờ, mặt trời chỉ là đĩa nhạt thấp phía tây; vài sợi khói mảnh từ lá mục âm ỉ bờ bên kia | *(0 từ)* | 0 | 1 | Thở sau payoff | 5.0s |
| **A5-02** | 8s | FIXED · MS | N,NB,CN,LB | E | LD | Máy kê vách hốc. Nora ngồi ngang eo, bùn khô, lá cọ trên vai; Con Non nằm ép sát bên | El vidrio dejó de caer hace rato. / El cielo: naranja, luego café, luego gris. / Y acá seguimos. Seguimos vivos. | 19 | 3 | Còn sống | 7.0s |
| **A5-03** | 6s | MACRO · ECU | N,NB,NH,CN | G | LD | Bụi xám mịn lắng lên cẳng tay bùn của Nora và hông bùn của Con Non, phủ thành lớp mỏng | Ceniza. Cae y cae. / Nos está tapando a los dos. / Así empieza el invierno. | 14 | 1 | Mùa đông bắt đầu | 5.0s |
| **A5-04** | 6s | POV · MS | CN,LB | G | LD | Con Non ngẩng đầu kêu 2 nốt về phía rừng; không tiếng đáp; im | *(0 từ)* | 0 | 3 | Im lặng là câu trả lời | 5.0s |
| **A5-05** | 6s | POV · EWS | BD,CA,BS,LB | G | LD | Ra miệng hốc: lớp bụi xám mỏng phủ bãi sỏi; xác Edmontosaurus thành ụ xám; hai dải lưng bất động trong nước xám. Máy lia chậm, dừng ở bìa rừng: **một thân lớn có diềm nằm im dưới bụi, sừng trái gãy cụt** | *(0 từ)* | 0 | 2,3 | **Payoff Bò Đực** · callback mở đầu | 5.0s |
| **A5-06** | 8s | SELFIE · MCU | N,NB,LB | E | LD | Nora, bụi xám trên tóc, nhìn về bãi sỏi | Esta mañana salí gateando de ese arroyo. / Doce horas después, el mundo entero se calló. / Escuchen. Nada más escuchen esto. | 20 | 2 | Vòng tròn khép | 7.0s |
| **A5-07** | 8s | OTS · MS | N,NB,CN,LB | E | LD | Nora tiền cảnh, Con Non cạnh bên. **Câu thoại cuối cùng của phim** | Yo vine acá a ver el final. / Resulta que el final no necesita público. / Regla seis. Sigue al chamaco. | 19 | 3 | Lời cuối · bỏ vai khán giả hẳn (callback A1-05, A4-14) | 7.0s |
| **A5-08** | 6s | MACRO · ECU | N,NB,NH,CN | G | LD | Bàn tay Nora đặt phẳng trên lớp bụi cạnh bàn chân Con Non; bàn chân nhấc lên ra khỏi khung (nó đứng dậy) | *(0 từ)* | 0 | 3 | Khớp động tác vào cảnh cuối | 5.0s |
| **A5-09** | 10s | FIXED · WS | N,NB,CN,LB | E | LD | **Cảnh cuối, 0 từ.** Con Non đi chậm dọc lạch về phía màn bụi xám. Nora chống tay đứng dậy, phủi bụi trên cẳng tay, bước theo sau nó; hai bóng nhỏ dần rồi tan vào bụi. **CẮT THẲNG SANG ĐEN** | *(0 từ)* | 0 | 3 | Kết im lặng · đi theo kẻ sống sót | 9.0s |

## §10 BẢNG VẬT LÝ

### Mở phim

| Clip | Máy | Frame 0 | Chuyển động theo mốc | Thoát khung |
|---|---|---|---|---|
| CO | = MASTER | = MASTER | = MASTER 0–8s | Cắt đen ở 8s |
| EST-01 | Cao ~120 m, trôi chậm về trước, rất êm | Sương trên lạch, bãi cát, rừng lá rộng, 3 chấm thú | Sương trôi chậm trái→phải · thú đứng yên | — |

### ACT 1 — ARRIVAL (HOUR 0 → 1 · L1)

| Clip | Máy | Frame 0 | Chuyển động theo mốc | Thoát khung |
|---|---|---|---|---|
| A1-01 | Ngang ngực, cầm tay, lùi | Mặt nước nâu, hai dải lưng ở giữa khung | 0–2s hai dải lưng trôi về máy chậm · 2–4s máy lùi, bờ sỏi lọt vào đáy khung · 4–6s máy lên bờ, nước tụt khỏi khung | Dải lưng vẫn trong khung (không biến mất) |
| A1-02 | Tay phải giữ máy ngang ngực, tay trái chống sỏi | Nora quỳ, tóc ướt dính trán, hai dải lưng ở nước nông hậu cảnh | Nora thở dốc, quay đầu nhìn nước 3–6s rồi nhìn lại máy | — |
| A1-03 | Ngang ngực, đi bộ chậm | Xác nằm ngang giữa khung, lún bùn, sườn trơ | Máy tiến ~0.5 m/s · ruồi bay quanh sườn · máy dừng ở 6–8s | — |
| A1-04 | Chúc xuống sát xương | Rãnh răng hình chữ U trên xương, tủy dập | 0–3s tay trái vào khung từ dưới · 3–6s đặt phẳng trong rãnh · 6–8s giữ yên | — |
| A1-05 | Tay phải giữ ngang ngực | Nora MS, xác hậu cảnh trái, lạch phải | 3–6s Nora liếc qua vai phải về hướng nam-đông nam rồi nhìn lại | — |
| A1-06 | Chúc xuống rồi ngẩng lên | Mai rùa trên sỏi, hai tay ở đáy khung | 0–3s nhặt, múc nước · 3–6s ngẩng lên bờ bên kia · 6–8s giữ ở hốc + dải lưng | — |
| A1-07 | Kê cố định trên khúc gỗ, ngang eo | Nora ngang eo, mai rùa trong hai tay | Hai tay xỏ dây, thắt nút ở hông trái, kéo thử | — |
| A1-08 | Ngang ngực, lia chậm trái→phải | Bìa rừng rậm, lá non mùa xuân | Lia ~10°/s, dừng ở miệng hành lang 5–8s · lá cành tiền cảnh quệt qua mép khung | — |
| A1-09 | Chúc thẳng xuống | Dấu chân trên bùn xám, nước đục | Mũi giày phải vào khung 0–3s, đặt cạnh dấu · nước trong dấu gợn nhẹ | — |
| A1-10 | Sau vai phải Nora, ngang vai | Vai + gò má Nora tiền cảnh trái, đàn 3 con hậu cảnh | Đàn gặm, đuôi đung đưa · Nora quay nửa mặt về máy 3–6s | — |
| A1-S1 | Tay phải giữ ngang ngực, đi lùi | Nora MCU cười, đàn hậu cảnh | 6–8s Nora quay người bước ra, máy theo | — |
| A1-11 | Ngang ngực, đi bộ | Bò Đực cúi gặm, chiếm 1/3 khung | 0–2s ngẩng đầu chậm · 2–4s máy tiến 2 bước · 4–6s dừng, Bò Đực nhìn thẳng | — |
| A1-12a | Ngang ngực, đứng (giữ nguyên cả chuỗi) | Bò Đực đứng nhìn thẳng (= cuối A1-11) | 0–2s cúi đầu · 2–4s ba bước nặng về máy, bùn bắn | Kết: đầu Bò Đực = 1/2 khung |
| A1-12b | Cùng vị trí 12a | Bò Đực giữa bước lao (= cuối 12a) | 0–2s khựng, chân trước cào · 2–4s bùn văng, máy giật lùi nửa bước | Kết: Bò Đực đứng yên, máy ngả sau |
| A1-12c | Cùng vị trí, rồi ngã ngửa | Bò Đực đứng (= cuối 12b) | 0–2s máy ngả · 2–4s khung lật lên tán lá, lắc rồi dừng | Bò Đực ra mép dưới khi khung lật |
| A1-13 | Tay phải giữ trên mặt, nằm | Nora nằm, lá non tiền cảnh | Nora thở dốc, chớp mắt, cười méo | — |
| A1-14 | Kê trên gốc cây, ngang eo | Nora trái khung, đàn hậu cảnh phải | Nora ngồi xuống 0–3s, rồi tĩnh · đàn gặm | — |

### ACT 2 — READING THE HERD (+ EST-02 · HOUR 1 → 6 · L2 → L3)

| Clip | Máy | Frame 0 | Chuyển động theo mốc | Thoát khung |
|---|---|---|---|---|
| A2-01 | Ngang ngực người ngồi, tĩnh | Ba con gặm ở 1/2 dưới khung | 3–7s Con Cái Già ngẩng đầu chậm (~1s), đứng im · 7–10s cúi xuống | — |
| A2-02 | Ngang ngực, tĩnh, tele | Diềm sờn bạc của Con Cái Già lấp 1/2 khung | 0–2s quay đầu chậm về bìa rừng · 2–6s diềm ửng hồng dần | — |
| A2-03 | Tay phải giữ ngang ngực, ngồi | Nora MCU, đàn hậu cảnh | Nora thì thầm, liếc ra sau 3–6s | — |
| A2-04 | Ngang ngực người đứng | Bò Đực nghiêng người, 1/2 khung | 0–2s cào chân · 2–4s bùn văng · 4–6s máy lùi 1 bước | — |
| A2-05 | Kê trên gốc cây, ngang eo | Nora đứng nhìn máy | 3–6s xoay vai nghiêng, cụp mắt · 6–8s liếc máy, nhếch môi | — |
| A2-06 | Ngang ngực người ngồi | Con Non đứng mép vũng | 0–3s quỳ xuống · 3–6s lăn nghiêng · 6–8s đứng dậy, rũ bùn | — |
| A2-07 | Kê trên rễ cây, ngang eo | Nora quỳ cạnh vũng, bùn sẵn trên mép | 0–3s ngón tay quệt bùn trên mép · 3–6s trát cẳng tay, cổ · 6–8s giơ lá cọ | — |
| A2-08 | Sau vai trái Nora, ngang vai | Vai Nora tiền cảnh, Con Non xa | Con Non đi chậm về máy, dừng 6s · Con Cái Già đứng yên | — |
| A2-09 | Ngang cẳng tay, tĩnh | Cẳng tay bùn đáy khung, mõm Con Non vào từ phải | 0–2s mõm chạm hít · 2–4s kêu 2 nốt, rút về | Mõm ra mép phải |
| A2-10 | Ngang ngực người ngồi, tĩnh | Đàn gặm | 0–2s Con Cái Già ngẩng · 2–4s hai con còn lại ngẩng · 4–6s tĩnh tuyệt đối | — |
| A2-11 | Thấp sát đất, bò lùi | Khúc gỗ rêu tiền cảnh | 0–3s bò lùi · 3–6s dừng ở khe, tay đặt lá cọ xuống | — |
| A2-12a | Sau khe gỗ, giữ nguyên cả chuỗi | Hành lang thú trống qua khe gỗ | 0–2s nước vũng rung · 2–4s đầu + vai vào từ phải, chậm | Kết: đầu ở giữa khe |
| A2-12b | Cùng vị trí | Đầu T. rex giữa khe (= cuối 12a) | Thân trôi phải→trái ~1.5 m/s | Kết: thân sau giữa khe |
| A2-12c | Cùng vị trí | Thân sau giữa khe (= cuối 12b) | 0–2s đuôi lướt · 2–4s hành lang trống | Đuôi ra mép trái ~2s |
| A2-13 | Chúc xuống | Bàn tay phẳng trên bùn, vũng nhỏ cạnh | 0–4s nước rung yếu dần · 4–6s tay nhấc lên | — |
| A2-14 | Tay phải giữ sát mặt, nằm | Nora nằm sau gỗ rêu | Thì thầm, mắt liếc ra khe | — |
| A2-R1 | Sát đất sau khúc gỗ | Bụi rìa hành lang, hai dải chuyển động thấp ở mép phải | Bụi rẽ chậm · hai con bước êm theo vệt, rướn đầu ngửi | Khuất sau bụi ~5s |
| A2-R2a | Ngang ngực người ngồi, giữ nguyên cả chuỗi | Đàn gặm, Con Non ở mép ngoài | 0–2s Con Cái Già khịt, đàn ngẩng · 2–4s xoay sừng ra ngoài, Con Non vào giữa | Kết: tam giác sừng khép |
| A2-R2b | Cùng vị trí | Tam giác sừng (= cuối 2a) | 0–2s hai raptor ló ra mép trái · 2–4s đứng yên nhìn máy | Kết: raptor đứng mép trái |
| A2-R2c | Cùng vị trí | Raptor mép trái (= cuối 2b) | 0–2s Con Cái Già nhìn máy · 2–4s nhích chân, khe mở | Kết: khe mở giữa hai con |
| A2-R3 | Tay phải giữ ngang ngực, ngồi | Nora, chân trụ Con Cái Già sau lưng | Thì thầm, liếc ra ngoài 3–6s | — |
| A2-R4 | Ngang ngực người ngồi | Chân Con Cái Già trái khung, tay Nora trên da | Raptor xa dần, khuất bụi ~4s · chân đứng yên như cột | Raptor ra mép phải |
| A2-15 | Kê trên tảng đất, ngang eo | Nora tiền cảnh trái, Bò Đực hậu cảnh phải | Bò Đực quay đầu chậm nhìn 0–3s rồi cúi gặm | — |
| EST-02 | Rất cao ~400 m, gần như đứng yên | Tán rừng, lạch, hố nước nhỏ, trời mây mỏng | Bóng mây trôi chậm · tán lá lăn tăn | — |
| A2-16 | Chúc xuống ngang ngực | Mai rùa trong hai tay | Nghiêng mai, nước sóng sánh, dựng lại | — |

### ACT 3 — THE WATER HOLE (+ EST-03 · HOUR 6 → 11 · L3 → L4 → L5)

| Clip | Máy | Frame 0 | Chuyển động theo mốc | Thoát khung |
|---|---|---|---|---|
| A3-01 | Tay phải giữ ngang ngực, đứng dậy | Nora MCU, đàn hậu cảnh | Đàn quay đi chậm 0–4s · Nora đứng dậy 6–8s | — |
| A3-02 | Ngang ngực, chạy, cầm tay | Ba con quay lưng trên hành lang | Đàn xa dần · máy chạy ~3 m/s, khung nảy | — |
| A3-03 | Sau vai phải, đi theo | Vai Nora tiền cảnh, đàn xa | Đi nhanh, khung nảy nhẹ · đàn nhỏ dần | — |
| A3-04 | Chúc xuống, đi | Dấu chân tròn đầy nước | 0–2s giày vào khung · 2–4s đạp vào, nước gợn | Giày ra mép trên |
| A3-05 | Ngang ngực, xuống dốc | Bờ đất lở, bãi bùn phía dưới | Máy trượt xuống ~1 m/s | — |
| A3-06a | Chúc xuống chân, giữ nguyên cả chuỗi | Giày phải, phiến đá phẳng | 0–2s đặt chân · 2–4s trượt, mai văng ra | Kết: mai lủng lẳng xa hông |
| A3-06b | Cùng vị trí | Mai lủng lẳng (= cuối 6a) | 0–2s dây đứt · 2–4s mai rơi, nứt đôi, nước bắn | Kết: hai nửa mai trên đá |
| A3-06c | Cùng vị trí | Hai nửa mai (= cuối 6b) | Vệt nước loang rồi ngấm | — |
| A3-07 | Tay phải giữ ngang ngực, quỳ | Nora quỳ, hai nửa mai trong tay trái | Nora nhìn mai, rồi nhìn máy | — |
| A3-08 | Chúc xuống rồi ngẩng | Dấu chân trên bùn nứt | 0–2s ngón ấn mép dấu · 2–4s bùn lún · 4–6s máy ngẩng theo trục | — |
| A3-09 | Ngang ngực, đứng | Vệt dấu chân từ đáy khung chạy lên | Mây trôi bóng trên bãi · máy tĩnh | — |
| A3-D1 | Tay phải giữ ngang ngực | Nora MCU, đàn mỏ vịt hậu cảnh phải | Đàn đi phải→trái chậm · Nora liếc theo | — |
| A3-D2a | Ngang ngực, giữ nguyên cả chuỗi | Đàn mỏ vịt đi ngang giữa khung | 0–2s ngẩng đầu · 2–4s quay mình về máy | Kết: đàn hướng về máy |
| A3-D2b | Cùng vị trí | Đàn hướng về máy (= cuối 2a) | Đàn chạy trái→phải, mỗi con thân riêng, không chồng | Kết: con cuối ra mép phải |
| A3-D2c | Cùng vị trí, hạ thấp | Bãi trống, bụi (= cuối 2b) | 0–2s máy hạ · 2–4s hai tay áp đất | — |
| A3-D3 | Tay phải giữ ngang ngực, quỳ | Nora quỳ, vệt bụi xa | Thì thầm, liếc theo vệt bụi | — |
| A3-10 | Ngang ngực, đứng yên | Infernodrakon đi giữa khung, nhỏ | Đi trái→phải chậm, mổ bùn 1 lần | — |
| A3-11 | Tay phải giữ thấp, cúi | Nora MCU, Infernodrakon xa | Infernodrakon đi chậm hậu cảnh | — |
| A3-12a | Ngang ngực, giữ nguyên chuỗi | Infernodrakon đứng, cánh gấp | 0–2s hạ người · 2–4s bật lên, cánh dang | Kết: trên không thấp |
| A3-12b | Cùng vị trí, ngửa nhẹ theo | Trên không thấp (= cuối 12a) | Bay xa, nhỏ dần thành chấm | Ra mép phải-trên ~3s |
| A3-13 | Ngang ngực, đi chậm rồi dừng | Hố nước, đàn ở giữa khung | Máy tiến chậm, dừng 4s | — |
| A3-W1 | Ngang ngực người ngồi, tĩnh | Ba con ở mép nước | Hai con uống · Con Cái Già đứng yên, mắt quét nước | — |
| A3-W2a | Ngang ngực, tele, giữ nguyên | Mặt nước, chân Con Cái Già mép trái | 0–2s mặt nước lặng · 2–4s mõm + mắt trồi | Kết: mõm trên mặt nước |
| A3-W2b | Cùng vị trí | Mõm trên mặt nước (= cuối W2a) | 0–2s dậm chân · 2–4s cá sấu lặn, sóng loang | — |
| A3-W3 | Tay phải giữ ngang ngực, ngồi | Nora, Con Cái Già hậu cảnh | Thì thầm, liếc ra sau | — |
| A3-14 | Kê trên tảng đất cao, toàn | Nora trái, Bò Đực phải ở mép nước | 0–3s Nora dừng · 3–6s xoay vai, diềm nhạt · 6–8s bước 1 bước | — |
| A3-15 | Kê thấp ngang eo | Nora quỳ mép nước | 0–3s vốc nước · 3–6s uống · 6–8s lau miệng, cười | — |
| A3-16 | Sau vai trái, ngang vai | Vai Nora, Con Non trong nước | Con Non lội tới 0–3s, kêu 3–4s, đứng yên | — |
| A3-Q1 | Kê trên rễ cây, ngang eo | Nora ngồi, Con Non nằm cạnh | Con Non thở chậm, mí mắt khép · Nora cúi nhìn | — |
| A3-Q2 | Ngang ngực người ngồi, tĩnh | Con Cái Già cúi uống, rặng cây phía sau | 0–2s ngẩng đầu · 2–4s nhìn đăm đăm · 4–6s cúi uống lại | — |
| A3-17 | Tay phải giữ ngang ngực, ngồi | Nora MCU, đàn hậu cảnh | Nora cười, ngả đầu · 7–10s nụ cười tắt dần | — |
| EST-03 | Kéo lùi lên, chậm | Hố nước giữa khung | Đàn chim bay ngang trái→phải | Chim ra mép phải ~3s |

### ACT 4 — IMPACT (+ MASTER · HOUR 12 → T+~1h · L5 → LQ → LG → LT)

| Clip | Máy | Frame 0 | Chuyển động theo mốc | Thoát khung |
|---|---|---|---|---|
| A4-01 | Ngang ngực, lia chậm | Đàn quanh hố nước | Lia trái→phải ~8°/s · đàn gặm | — |
| A4-02 | Tay phải giữ ngang ngực | Nora MCU, đàn hậu cảnh | Nora nhún vai 6–8s | — |
| A4-03a | Ngang ngực, giữ nguyên cả chuỗi | Con Cái Già uống trái, Bò Đực + Con Non hậu cảnh, rặng cây | Tĩnh, cành lá lay nhẹ | — |
| A4-03b | Cùng vị trí | = cuối 3a | 0–1s im bặt · 1–2s Con Cái Già ngẩng phắt · 2–4s diềm đỏ dần | Kết: Con Cái Già ngẩng đầu, diềm đỏ |
| A4-03c | Cùng vị trí | Con Cái Già ngẩng, diềm đỏ (= cuối 3b) | 0–2s Bò Đực ngẩng · 2–3s Con Non ngẩng · 3–4s cả ba đứng sững | — |
| A4-04 | Tay phải giữ ngang ngực | Nora MCU, Con Cái Già diềm đỏ sau vai phải | 0–3s nhìn qua vai · 3–8s nhìn máy | — |
| A4-05 | Ngang ngực người ngồi | Đàn đứng sững | 0–2s Bò Đực cào chân · 2–6s Con Non ép sát mẹ | — |
| A4-06 | Chúc xuống mặt nước | Mặt nước lặng | 0–2s vòng sóng rung · 2–4s bóng chim lướt trên mặt nước | — |
| A4-07a | Ngang ngực, cầm tay, giữ nguyên chuỗi | Hố nước, cây bách chết mép bắc | 0–2s đất giật · 2–4s cây lay, nước tạt | Kết: cây bách chết nghiêng |
| A4-07b | Cùng vị trí | Cây nghiêng (= cuối 7a) | 0–2s đất cuộn, bùn nứt · 2–4s cây đổ trái→phải | Kết: cây nằm ngang |
| A4-07c | Cùng vị trí, rồi ngã | Cây nằm ngang (= cuối 7b) | 0–2s chao · 2–4s ngã, khung úp bùn | — |
| A4-08 | Tay phải giữ thấp sát mặt, nằm | Nora úp, má trái dính bùn | 0–3s nhấc đầu · 6–8s chống tay đứng | — |
| A4-09 | Ngang ngực, chạy, cầm tay | Đàn chạy ngang | Đàn trái→phải ~5 m/s, mỗi con thân riêng | Đàn ra mép phải ~3s |
| A4-P1 | Ngang ngực, đang chạy rồi khựng | Bờ đất cao trước mặt | 0–2s bờ nứt · 2–4s khối bùn trượt xuống nước | — |
| A4-T1 | Ngang ngực, đứng sau khối bùn, giữ nguyên | Bãi trống, rặng cây xa | 0–2s cây rẽ · 2–4s T. rex bước ra, đi trái→phải | Kết: T. rex giữa bãi |
| A4-T2 | Cùng vị trí | T. rex giữa bãi (= cuối T1) | Bước nhanh trái→phải, cùng hướng, cùng tốc độ | Ra mép phải ~3.5s |
| A4-P2 | Tay phải giữ ngang ngực, ngồi thụp | Nora MCU, khối bùn sau lưng | Thở dốc, liếc theo | — |
| A4-10 | Ngang ngực, chạy | Bãi trống, trời vệt sáng | Máy tiến ~3 m/s · hạt rơi chéo | Hạt chạm đất là tắt |
| A4-11 | Chúc xuống giày, chạy | Bùn, mũi giày | Hạt rơi, nảy, chấm lỗ vũng · giày bước 2 nhịp | — |
| A4-12 | Tay phải giữ ngang ngực, ngồi thụp | Nora sau thân cây đổ | Nora nhìn quanh, che đầu bằng tay trái 3–6s | — |
| A4-13 | Ngang ngực người ngồi | Bãi trống, đàn xa mép trái | Con Non vào từ trái, lao qua, chúi xuống phải-dưới | Ra mép phải ~2.5s |
| A4-14 | Tay phải giữ ngang ngực | Nora MCU | Quay đầu trái 0–3s, phải 3–6s, nhìn máy 6–8s | — |
| A4-15 | Ngang ngực, chạy xuống dốc | Hành lang dốc, Con Non 15 m trước | Con Non xa dần · máy theo, khung nảy | Con Non khuất khúc cua ~2.5s |
| A4-16 | Sau vai phải, ngang vai | Vai Nora, lòng lạch, hốc | Con Non chui vào hốc 0–5s · Nora chống tay 6–8s | Đuôi Con Non khuất vào hốc |
| A4-17 | Ngang ngực, trượt xuống | Vách đất, lạch dâng | Máy trượt ~1 m/s · nước chảy phải→trái (ngược) | — |
| A4-18 | Chúc xuống | Bùn ướt mép lạch | 0–2s vốc · 2–4s trát cẳng tay | — |
| A4-19 | Ngang ngực, bò | Lá cọ ở mép nước, miệng hốc 2 m | 0–2s tay kéo lá · 2–4s máy tiến vào hốc | Kết trong bóng hốc |
| MASTER | Kê cố định vách hốc | Nora nằm, lá cọ, giày thò ra | 0–3s / 3–7s thoại · 7–8s "Don't move" · 8–10s chân Con Non đặt xuống | — |

### ACT 5 — THE QUIET (T+~2h · LD)

| Clip | Máy | Frame 0 | Chuyển động theo mốc | Thoát khung |
|---|---|---|---|---|
| A5-01 | Trong hốc, nhìn ra, tĩnh | Lòng lạch, bờ bên kia | Bụi lắng chậm · khói mảnh bốc thẳng | — |
| A5-02 | Kê vách hốc, cách 1.5 m | Nora ngồi, Con Non nằm | Con Non thở · tĩnh | — |
| A5-03 | Chúc xuống | Cẳng tay bùn + hông Con Non | Bụi rơi thẳng, chậm, đọng lại | — |
| A5-04 | Ngang ngực người ngồi | Con Non nằm | 0–2s ngẩng đầu chậm · 2–4s kêu · 4–6s đứng im chờ | — |
| A5-05 | Ngang ngực, đứng ở miệng hốc | Bãi sỏi phủ bụi | Lia chậm trái→phải, dừng ở sừng gãy | — |
| A5-06 | Tay phải giữ ngang ngực | Nora MCU, bãi sỏi xám | Nora nhìn bãi 0–6s, nhìn máy, im 6–8s | — |
| A5-07 | Sau vai trái, ngang vai | Vai Nora, Con Non | Tĩnh | — |
| A5-08 | Chúc xuống | Tay Nora + bàn chân Con Non | Bàn chân nhấc chậm 2–4s | Bàn chân ra mép trên ~4s |
| A5-09 | Kê vách hốc, toàn, tĩnh | Nora ngồi, Con Non đứng cạnh | 0–3s Con Non đi trước · 3–6s Nora đứng dậy bước theo · 6–10s hai bóng nhỏ dần | Cả hai tan vào bụi ~9s |

## §11 SỔ LIÊN TỤC

### 11.1 Bờ suối (LB)
- Suối nâu đục rộng ~15 m chảy trái → phải. Tiền cảnh: bãi sỏi xám + cát vàng nhạt, gỗ trôi.
- Bờ xa dựng đứng ~2 m, lớp phù sa xám nâu + sét xám ô liu + dải than bùn đen; rễ treo.
- **Hõm khô** ~1.5 m ngay trên mép nước bờ xa (cài A1-06 → trả A4-16). Cá sấu nằm dưới hõm ở Act 1.
- Trục A: nhìn từ bãi sỏi sang bờ xa. Trục B: dọc dòng suối.

### 11.2 Hành lang thú (LC)
- Bùn phù sa xám nâu bị giày xéo, hố chân tròn đọng nước.
- **Khúc gỗ rêu lớn bên phải** (Nora nấp ở A2-11/A2-12).
- Vũng bùn xám ở khoảng trống (A2-06/07).

### 11.3 Vũng nước (LW)
- Nước nâu ~30 m giữa; mép bùn xám đầy hố chân.
- Lùm thủy sam / cây bách đầm lầy phía **bắc**; **cây bách chết xám nghiêng bên trái lùm** (đổ ở A4-07b; Nora nấp cạnh thân đổ ở A4-12/14).
- Bãi bùn khô nứt ở tiền cảnh. Súng trắng bên phải mặt nước.
- **Tảng đá phẳng ở bờ nam** (Nora trượt ở A3-06).
- A4-P1: bờ đất cao phía trước sạt xuống hố nước thành khối bùn, chắn lối.

### 11.4 Dấu trên người Nora

| Từ clip | Đến clip | Dấu |
|---|---|---|
| A1-01 | A1-14 | Ướt tóc và áo |
| A1-07 | A3-06b | Bình mai rùa bên hông trái |
| A3-07 | hết | Bình mất, đầu dây sợi đứt lủng lẳng bên hông trái (câu khóa §2.3) |
| A2-07 | hết | Bùn xám trên tay và cổ |
| A2-07 | A2-11 | Lá cọ quạt cầm che đầu |
| A4-07c | hết | Bùn trên má trái |
| A4-P2 | hết | Bụi trên mặt và tóc |
| A4-12 | hết | Hạt thủy tinh trong tóc |
| A4-18 | hết | Bùn ướt khắp người |
| A4-19 | MASTER | Lá cọ phủ trên người |
| A5-03 | hết | Bụi xám phủ |

## §12 THỨ TỰ SINH

**Trước hết (không sinh):**
1. Rule 21 flush PENDING → tạo material `cretaceous_documentary` → tạo project + video + 112 scene.
2. PATCH `duration` cho cả 112 scene (thiếu sẽ âm thầm thành 10s) + `narrator_text`.
3. `/fk-script-to-prompts` → prompt JSON → `python tools/lint_prompt.py --file <path>` đạt 0 Critical/High → user duyệt.
4. Upload mặt Nora (`uploads/nora_main_clean.jpg`) và Body trần (`uploads/nora_body_v3_clean.jpg`).

**Sinh (mỗi bước hỏi trước — Rule 29):**
1. Ref: NB (EDIT từ Body trần), NH, BD, CG, CN, TR, AR, ED, BS, IN, CA, LB, LC, LW (14 ảnh) → xóa logo → upload → duyệt.
2. Start Frame + video theo thứ tự **khó trước**: A1-12 → A4-07 → A2-12 → A4-03 → MASTER → A2-R2 → A4-T1/T2 → A3-D2 → A3-06 → A3-W2 → A3-12 → các clip còn lại theo thứ tự phim.
3. Mỗi lô: Start Frame → xóa logo → upload → Review Board ảnh → duyệt → video 720p → `/fk-review-video` → duyệt → upscale 1080p → xóa logo → concat.

> ✅ Kịch bản đã duyệt 2026-10-14 (v2.1). Mỗi bước sinh vẫn phải hỏi trước (Rule 29).
