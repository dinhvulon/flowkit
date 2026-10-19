# Thoại tiếng Tây Ban Nha Mỹ Latinh (`es-419`) — chế độ ngôn ngữ thoại

> **Phim vs vlog (2026-10-19):** luật viết thoại tiếng Tây Ban Nha Mỹ Latinh (prompt tiếng Anh, chỉ thoại trong ngoặc kép là tiếng Tây Ban Nha, câu khóa accent, số từ Rule 49) áp cho phim. Phần giọng Laomedeia, persona vlogger và "giống một vlogger Mỹ Latinh thật" chỉ áp cho vlog (xem [`vlog-archive.md`](vlog-archive.md)); phim chọn voice id riêng cho từng nhân vật.

Đọc file này khi user chọn thoại **tiếng Tây Ban Nha Mỹ Latinh** (español latinoamericano / "español latino"), ví dụ khi họ đưa video mẫu kiểu *"Hace 300.000 Años: Así Era La Vida En La Edad De Piedra"* và muốn làm bản tiếng Tây Ban Nha. Mặc định của skill vẫn là English. File này chỉ đổi **ngôn ngữ thoại**; mọi luật khác (Rule 49 số từ, Sonic Isolation, prompt-lock, VOICE_LOCK persona) giữ nguyên.

Vì sao cần file riêng: model video lấy giọng từ voice id (Laomedeia) nhưng lấy **ngôn ngữ và accent từ chữ trong ngoặc kép** và câu tả cách nói. Nếu chỉ dịch thoại sang tiếng Tây Ban Nha mà không khóa accent, model hay trôi sang giọng Tây Ban Nha (Castilian, ngọng "th" kiểu Madrid) hoặc chen chữ tiếng Anh. Còn nếu dịch máy từng câu, thoại ra giọng sách vở, không giống một vlogger Mỹ Latinh thật.

---

## 1. Thiết lập dự án

| Trường | Giá trị |
|---|---|
| `language` của project / `--language` cho `/fk-gen-narrator` | `es` (ghi rõ `es-419` trong `script.md`) |
| Giọng | **Laomedeia** (giữ nguyên, Rule 24). Gemini-TTS đa ngữ; accent do chữ + câu khóa accent bên dưới quyết định |
| Accent mặc định | **Mexico City** (thị trường YouTube tiếng Tây Ban Nha lớn nhất, và là giọng Mỹ Latinh model Google ra đúng dễ nhất). Mexico hoặc một nước Trung Mỹ → đọc **`dialogue-es-mx-ca.md`**: hồ sơ giọng từng nước, câu khóa giọng, kho từ, câu mẫu. Nước khác (Colombia, Argentina, Chile…) chưa có hồ sơ; research trước rồi viết theo cùng khuôn |
| `narrator_text` | Đúng nguyên văn câu tiếng Tây Ban Nha trong `video_prompt` (khớp 100%, `/fk-gen-narrator` mục 4) |
| Vietsub cho user duyệt | `vn.json` dịch tiếng Việt từng câu; **không** đưa vào prompt |
| SEO, thumbnail, chữ trên hình | 100% tiếng Tây Ban Nha (CLAUDE.md Rule 20) — xem mục 7 |

---

## 2. Viết vào `video_prompt`

**Phần mô tả cảnh vẫn viết tiếng Anh.** Chỉ chữ trong ngoặc kép là tiếng Tây Ban Nha. Lý do: các câu khóa (ID-LOCK, camera, already-in-place) đã được test bằng tiếng Anh; dịch chúng làm mất tác dụng khóa.

**Câu khóa accent** — đặt 1 lần trong khối `speech.delivery` (JSON) hoặc ngay trước sub-clip đầu tiên có thoại (text):

```
Nora is a native Spanish speaker from Mexico City, in her early twenties. She speaks fast, casual Mexico City Spanish: every "s" crisp and fully pronounced, unstressed vowels relaxed and quick, a light rise-and-fall melody at the end of phrases. She has no American or English accent when she speaks Spanish, never a Spain accent, never lisps the "z" or "c", and says no English words.
```

Câu này ghi thành phố và nói rõ cô là người bản ngữ, vì hai lý do: Google khuyên tả giọng cụ thể tới thành phố, và vlogger trông như người nước ngoài thì model hay cho nói giọng Mỹ. Trung Mỹ → đổi theo công thức `dialogue-es-mx-ca.md` §1a.

**Tag người nói** — giữ khuôn tiếng Anh, thoại tiếng Tây Ban Nha:

```
0-3s: From the very first frame at second 0, Nora says (out of breath, eyes wide): "Menos cuarenta, más o menos. Sin carpa."
```

**JSON (`/fk-script-to-prompts`)** — thêm trường `language` vào `speech`:

```json
"speech": {
  "speaker": "Nora",
  "language": "es-419 Latin American Spanish, neutral Mexican accent",
  "delivery": "Laomedeia, fast confident vlog delivery; <câu khóa accent ở trên>",
  "dialogue": [
    {"t": "0-3s", "speaker": "Nora", "line": "Menos cuarenta, más o menos. Sin carpa."},
    {"t": "3-6s", "speaker": "Nora", "line": "Y un tipo con lanza decidiendo si vivo."},
    {"t": "6-8s", "speaker": "Nora", "line": "No me miren así, chicos."}
  ]
}
```

**Câu kết (prompt-lock khối 8)** đổi `Only <V> speaks English` thành:

```
Only Nora speaks, and only in Latin American Spanish; nobody speaks over anyone else. No subtitles or text appear in the frame.
```

**Nhân vật phụ** vẫn nói ngôn ngữ không hiểu được, nhưng đổi `non-English` thành `non-Spanish`:

```
3-5s: Torak speaks in a gravelly, low-pitched male voice — short guttural non-Spanish sounds, consonant-heavy, no recognizable words; Nora stays silent.
```

Dấu `¡ ¿` giữ nguyên trong thoại: chúng giúp model đọc đúng ngữ điệu cảm thán / câu hỏi.

---

## 3. Số từ (Rule 49 không đổi)

Dùng **đúng bảng Rule 49**: 4s 0 hoặc 6–8 · 6s 12–15 · 8s 18–22 (`0-3s` 6–7 / `3-6s` 7–8 / `6-8s` 5–7) · 10s 24–28. **Không tăng số từ vì "giọng Latinh nói nhanh".** Nghiên cứu đo trực tiếp (Santiago & Mairano 2022, Madrid vs Mexico City, 22 người) cho thấy ngược lại: người Mexico nói **chậm hơn** người Madrid khoảng 7% khi đọc và 12–15% khi nói tự nhiên (~6.5 so với ~7.3 âm tiết/giây). Nữ Mexico nói tự nhiên chậm nhất nhóm (~6.3). Tiếng Tây Ban Nha nhiều âm tiết/giây hơn tiếng Anh nhưng mỗi âm tiết ít thông tin hơn, nên số **từ**/giây gần bằng tiếng Anh. Vì vậy dải Rule 49 dùng nguyên được. Test 1 clip trước khi sinh hàng loạt; nếu đo thấy dead air hay cụt âm thì báo user, không tự đổi dải.

Cách đếm:
- Đếm theo khoảng trắng. `al`, `del` = 1 từ. Động từ dính đại từ (`dámelo`, `agárrate`) = 1 từ.
- `¡ ¿ ! ?` không phải từ. Số viết bằng chữ (`cuarenta`, không `40`) để model đọc đúng.
- Từ bị cắt để bíp (`mier—`) = 1 từ.

---

## 4. VOICE_LOCK bản tiếng Tây Ban Nha

Persona giữ nguyên (`voice-bible.md` §1): chuyên gia sinh tồn, nói nhanh, hài khô, không giảng lịch sử. Chỉ đổi lớp ngôn ngữ:

| Trường | Bản English | Bản es-419 |
|---|---|---|
| Tật nói (tối đa 1/clip, xoay vòng) | "okay, okay", "no, wait—", "real talk" | "a ver, a ver", "no, espera—", "en serio" (Mexico: "la neta"; Trung Mỹ: xem `dialogue-es-mx-ca.md` §4) |
| Gọi người xem | "guys" | "chicos" (cả nhóm hỗn hợp) — dùng ít, tối đa 1 lần / 3 clip |
| Chửi thề bị bíp (`voice-bible.md` §3) | "sh—", "what the f—" | "mier—", "¡qué demon—"; Mexico: "¡no mam—", "¡chin—" (`no manches` là bản nhẹ, nói nguyên câu, không cần bíp) |
| Số làm tròn | "minus forty-ish" | "menos cuarenta, más o menos" |
| Không hiểu người bản địa | "No idea what he said." | "Ni idea de lo que dijo." |

**Không bao giờ nói** (bản tiếng Tây Ban Nha của danh sách cấm ở `voice-bible.md` §6): "fascinante", "increíble ingenio", "nuestros ancestros", "la humanidad", "realmente", "simplemente", "regla número uno de supervivencia", "el truco es", "dato curioso", "¿sabías que…?", "no vas a creer", "los científicos dicen", "los arqueólogos creen", "como vieron antes", "en este video".

---

## 5. Giọng Mỹ Latinh, không phải giọng Tây Ban Nha

Người xem Mỹ Latinh nghe một chữ kiểu Madrid là thấy "giả" ngay. Viết thoại xong, rà bảng này:

| Tránh (Tây Ban Nha) | Dùng (Mỹ Latinh) | Ghi chú |
|---|---|---|
| vosotros, vuestro, "¿habéis visto?" | ustedes, su, "¿ya vieron?" | Lỗi dễ lộ nhất |
| vale | okey, listo, está bien | |
| tío / tía (gọi bạn) | amigo / bỏ hẳn | |
| guay, mola, flipar | qué padre (MX), genial, no lo puedo creer | Chọn trung tính nếu không rõ nước |
| coger | agarrar, tomar | Ở Mỹ Latinh "coger" là từ tục |
| joder, hostia | mier— (bíp) | |
| ¡venga! | ¡vamos!, ¡órale! (MX) | |
| tienda de campaña | carpa | |
| gafas, zumo, conducir | lentes, jugo, manejar | Ít gặp trong vlog tiền sử nhưng hay lọt khi dịch máy |
| aquí (được), allí | acá, allá | `acá/allá` nghe Mỹ Latinh hơn |

Tiếng lóng nặng một nước (`chido`, `bacán`, `che`, `parce`) chỉ dùng khi user chọn nước đó; giọng trung tính thì tối đa một từ đậm Mexico mỗi 3–4 clip.

---

## 6. Mẫu trước / sau (đã đếm theo mục 3)

| Khuôn | Thoại | Số từ |
|---|---|---|
| Hook 8s | `0-3s` "Menos cuarenta, más o menos. Sin carpa." · `3-6s` "Y un tipo con lanza decidiendo si vivo." · `6-8s` "No me miren así, chicos." | 7 + 8 + 5 = 20 |
| A (làm → vì sao) 8s | `0-3s` "No coman nieve. Les roba el calor." · `3-6s` "Piedras calientes en la bolsa. El agua hierve." · `6-8s` "A ver, a ver… ¡ya está!" | 7 + 8 + 6 = 21 |
| C (người bản địa nói) | `3-5s` Torak — `non-Spanish sounds, no recognizable words; Nora stays silent` · `5-8s` Nora whispers: "Ni idea de lo que dijo. No nos movemos." | 9 |
| Nguy hiểm (câu đứt quãng) | "¡Viene hacia acá— mier— detrás de los huesos, ya!" (`bleep_at` tại "mier—") | 9 |
| Cảnh cuối | Không ai nói | 0 |

Dịch kiểu AI cần tránh: *"¡Increíble! Nuestros ancestros usaban esta técnica fascinante para sobrevivir."* — vừa giọng hướng dẫn viên, vừa giảng bài.

---

## 7. Hậu kỳ & đóng gói

- **Chữ trên hình** (chèn hậu kỳ, không viết vào prompt): `HACE 300.000 AÑOS`, `MISIÓN: <MỤC TIÊU> ANTES DE <HẠN CHÓT>`, `HORA 3 — QUEDAN 9 HORAS`. Dấu ngăn nghìn theo thị trường: Mexico/US Hispanic `300,000`; Argentina, Colombia, Chile `300.000`. Theo video mẫu nếu user đưa.
- **Tiêu đề YouTube** theo khuôn của thể loại này: `Hace <N> Años: Así Era La Vida En <Thời kỳ> | <Móc phụ>` (viết hoa chữ đầu mỗi từ như kênh gốc). Mô tả, tag, thumbnail đều tiếng Tây Ban Nha (`/fk-youtube-seo`, `/fk-thumbnail`, Rule 20).
- Phụ đề: xuất `.srt` tiếng Tây Ban Nha từ `narrator_text`; muốn thêm bản khác thì `/translate-capcut-srt`.

---

## 8. Checklist thêm cho thoại es-419 (chạy cùng checklist B của `prompt-lock.md`)

- [ ] Câu khóa accent có trong prompt (một lần), câu kết ghi `only in Latin American Spanish`.
- [ ] Không còn `Only <V> speaks English` hay `non-English` sót từ mẫu cũ.
- [ ] Không có chữ tiếng Anh nào trong ngoặc kép (kể cả "okay" viết kiểu Anh — dùng "okey").
- [ ] Không có từ ở cột "Tránh" mục 5; không `vosotros`.
- [ ] Không có từ thiết bị bằng tiếng Tây Ban Nha trong thoại: `celular`, `teléfono`, `móvil`, `pantalla`, `dispositivo`, `palo de selfie`, và tránh cả `cámara` (nói "miren esto", không nói "miren a la cámara") — cùng lý do với luật cấm `phone` (Bài học 63). `lint_prompt.py` đã bắt các từ này.
- [ ] Số từ đúng dải Rule 49 theo cách đếm mục 3; `narrator_text` khớp 100% thoại trong prompt.
- [ ] `vn.json` có bản dịch tiếng Việt để user duyệt nghĩa.
