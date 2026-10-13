# Thoại tiếng Tây Ban Nha — Mexico & Trung Mỹ (hồ sơ giọng + cách ra lệnh cho model)

Đọc sau `dialogue-es-latam.md` khi project nhắm khán giả **Mexico** (mặc định của chế độ es-419) hoặc một nước **Trung Mỹ** (Guatemala, El Salvador, Honduras, Nicaragua, Costa Rica, Panama). File đó giữ luật chung (prompt tiếng Anh + thoại tiếng Tây Ban Nha, Rule 49, checklist). File này trả lời hai câu: **viết thoại thế nào cho đúng giọng nước đó**, và **viết prompt thế nào để model nói đúng giọng đó**.

Nguồn research (2026-10-13): Wikipedia *Mexican Spanish*, *Central American Spanish*, *Salvadoran Spanish*, *Costa Rican Spanish*; tài liệu Gemini-TTS (Google Cloud, Gemini API); hướng dẫn thoại tiếng Tây Ban Nha cho Veo 3 (Arsturn); các bài về tiếng lóng Mexico/Trung Mỹ. Từ có dấu **†** là chưa xác minh được trong đợt research này. Chỉ dùng khi người bản xứ đã duyệt, và **không** đưa vào câu mẫu.

---

## 0. Model tạo giọng thế nào — và vì sao chữ quyết định giọng

- Omni Flash R2V chỉ nhận **voice id** ở Slot 7 (Laomedeia). Pipeline **không** gửi được `language_code` (`es-MX`, `es-419`). Ngôn ngữ và giọng vùng hoàn toàn do **chữ trong prompt** quyết định: câu khóa giọng + từ ngữ trong ngoặc kép.
- Google khuyên tả giọng **càng cụ thể càng tốt**, tới tận thành phố ("British English accent as heard in Croydon" thắng "British accent"). Vì vậy câu khóa giọng luôn ghi **thành phố + tuổi + 2–3 đặc điểm phát âm**, không chỉ ghi "Mexican accent".
- **Giọng Mexico là giọng Mỹ Latinh "mặc định" của model Google.** Có báo cáo rằng đặt `es-UY` mà người bản xứ vẫn nghe ra giọng Mexico. Hệ quả:
  - Mexico: dễ ra đúng giọng nhất.
  - Trung Mỹ: model có thể vẫn nói giọng gần Mexico. **Bản sắc nước đó phải gánh bằng ngữ pháp và từ vựng**: `vos sos / tenés / mirá`, `usted` của Costa Rica, từ địa phương. Một người Salvador nghe "vos sabés" và "cipotes" thì nhận ra ngay, kể cả khi âm sắc chưa chuẩn 100%.
- Vlogger trông như người nước ngoài (tóc vàng) thì model hay cho cô **nói tiếng Tây Ban Nha giọng Mỹ**. Có người dùng gọi đó là giọng "kiểu Selena Gomez": nghe ra là định nói giọng Mexico nhưng không thật. Câu khóa giọng phải nói rõ cô là **người bản ngữ** (xem §1).

---

## 1. Công thức prompt yêu cầu cách nói

### 1a. Câu khóa giọng (1 lần / clip, đặt trong `speech.delivery` hoặc ngay trước sub-clip thoại đầu)

```
Nora is a native Spanish speaker from <THÀNH PHỐ>, in her early twenties. She speaks fast, casual <TÊN GIỌNG> Spanish: <ĐẶC ĐIỂM 1>, <ĐẶC ĐIỂM 2>, <ĐẶC ĐIỂM 3>. She has no American or English accent when she speaks Spanish, never a Spain accent, never lisps the "z" or "c", and says no English words.
```

Điền `<…>` theo bảng hồ sơ ở §2–§3. Câu này viết **tiếng Anh**, nằm **ngoài** ngoặc kép.

### 1b. Tag cách nói cho từng câu (tiếng Anh, trong ngoặc đơn, ngay sau tên)

Giữ quy ước của `voice-bible.md` §2: `Nora says (hushed, breath shaking): "..."`. Bộ tag dùng được:

| Tình huống | Tag |
|---|---|
| Hook, vui, khoe | `(fast, bright, grinning, rising pitch at the end)` |
| Giải thích lúc tay đang làm | `(quick and matter-of-fact, hands busy)` |
| Rình, nấp | `(fast whisper, barely moving her lips)` |
| Nguy hiểm | `(shouting, voice cracking)` |
| Sau cơn sợ | `(breathless, shaky laugh)` |

Âm phi ngôn ngữ (thở hổn hển, cười, hít mạnh) **ghi bằng tiếng Anh** trong phần mô tả: `she gasps`, `she laughs once`. Tài liệu Gemini-TTS khuyên dùng tag tiếng Anh kể cả khi thoại không phải tiếng Anh. Đừng viết `(jadeando)` hay `(se ríe)`.

### 1c. Viết chữ trong ngoặc kép

- **Đủ dấu**: `á é í ó ú ñ ü` và `¡ ¿`. Dấu quyết định trọng âm: `esta` ≠ `está`, `papa` ≠ `papá`. Thiếu dấu thì model đọc sai trọng âm.
- **Câu ngắn.** Các hướng dẫn thoại tiếng Tây Ban Nha cho Veo đều thấy câu dài và phức tạp dễ bị đọc sai. Khớp với persona nói cụt của Nora.
- **Số viết bằng chữ** (`cuarenta`, không `40`).
- **Chỉ khi một từ bị đọc sai lặp lại** mới viết lại theo cách đọc (ví dụ `Mexico` → `Méjico` để chắc chắn âm "j"). Không viết phiên âm sẵn từ đầu: phiên âm làm narrator_text và phụ đề sai chính tả.
- Không bao giờ đặt chỉ dẫn giọng **bên trong** ngoặc kép: model sẽ đọc to nó lên.

### 1d. Khối JSON hoàn chỉnh (Mexico, clip 8s)

```json
"speech": {
  "speaker": "Nora",
  "language": "es-MX, Mexico City Spanish",
  "delivery": "Laomedeia, fast confident vlog delivery. Nora is a native Spanish speaker from Mexico City, in her early twenties. She speaks fast, casual Mexico City Spanish: every \"s\" crisp and fully pronounced, unstressed vowels relaxed and quick, a light rise-and-fall melody at the end of phrases. She has no American or English accent when she speaks Spanish, never a Spain accent, never lisps the \"z\" or \"c\", and says no English words.",
  "dialogue": [
    {"t": "0-3s", "speaker": "Nora", "line": "¿Qué onda, chicos? No sé dónde estoy."},
    {"t": "3-6s", "speaker": "Nora", "line": "Hace un frío cañón y cero carpas."},
    {"t": "6-8s", "speaker": "Nora", "line": "Híjole. Esto se va a poner feo."}
  ]
}
```

Số từ: 7 + 7 + 7 = 21 (Rule 49, 8s = 18–22).

---

## 2. Mexico (mặc định)

### Ngữ pháp
- **tú** với người ngang hàng; **usted** với người lớn tuổi, người lạ, người bản địa đáng sợ. Miền Bắc dùng `usted` nhiều hơn. **Không** có `vos` (trừ Chiapas). **Không** `vosotros`: luôn `ustedes`.
- Quá khứ hay dùng thì đơn: `Hoy comí` (không `he comido`).
- Thu nhỏ `-ito/-ita` dày đặc, kể cả khi vật không nhỏ: `ahorita`, `rapidito`, `tantito`. Từ tận cùng `-n` → `-cito`: `camioncito`.
- Câu hỏi phủ định cho tự nhiên: `¿No quieres probar?` mềm hơn `¿Quieres probar?`.
- `¿Qué tan…?` thay cho "how…": `¿Qué tan lejos está?`.

### Phát âm → điền vào câu khóa
- **`s` cuối âm tiết giữ rõ, nổi bật** ở miền Trung. Cộng với nguyên âm không nhấn bị rút gọn → chữ "s" nghe sắc. Bờ biển và Yucatán thì yếu "s".
- **Nguyên âm không nhấn bị rút ngắn, nuốt** khi nói nhanh (`trastes` gần như "trasts").
- `seseo` (z/c = s), `yeísmo` (ll = y). `j` là âm cọ xát vòm mềm rõ.
- Ngữ điệu Mexico City có đường cong lên-xuống (circumflex) ở cuối câu, dùng rộng hơn các vùng khác.

Đặc điểm điền vào `<…>`: `every "s" crisp and fully pronounced`, `unstressed vowels relaxed and quick`, `a light rise-and-fall melody at the end of phrases`.

### Kho từ cho Nora (giọng trẻ, YouTube)

| Dùng cho | Từ | Nghĩa | Tần suất |
|---|---|---|---|
| Chào / hook | `¿Qué onda?` | chào thân mật | mở video, 1 lần |
| Tật "real talk" | `La neta…` / `¿Neta?` | "nói thật là…" / "thật hả?" | ≤ 1 / 3 clip |
| Ngạc nhiên | `¡Híjole!`, `¡No manches!` | "trời ơi", "không thể nào" | ≤ 1 / clip |
| Đồng ý / bắt đầu | `¡Órale!` | "được", "đi thôi", "wow" (tùy giọng) | |
| Cảnh báo nguy hiểm | `¡Aguas!` | "coi chừng!" | cảnh nguy hiểm |
| Khen | `qué padre`, `chido` | "hay quá", "ngầu" | |
| Khó / dữ dội | `está cañón` | "căng thật", "khó thật" | |
| Thất vọng | `¡Chale!` | "chán thật", "tiêu rồi" | |
| Lát nữa | `ahorita` | "lát nữa / ngay đây" (mơ hồ có chủ ý) | |
| Vị trí | `atrás de`, `acá`, `allá` | "đằng sau", "ở đây", "ở kia" | thay `detrás`, `aquí` |

**Chửi bị bíp** (luật bíp `voice-bible.md` §3): `¡No mam—` (từ "no mames"), `¡Pin—` (từ "pinche"), `¡Chin—` (từ "chingado"). Chỉ viết phần bị cắt.

**Tránh:** `güey/wey` khi nói với người xem hay người bản địa. Wikipedia xếp nó cùng nhóm từ thô (`güey`, `pinche`, `pedo`, `naco`) và nó còn có nghĩa "đồ ngốc". `No manches` là bản nhẹ, dùng thay. Không dùng `naco` (khinh miệt giai cấp).

### Câu mẫu (đã đếm)

| Clip | Thoại | Từ |
|---|---|---|
| 8s hook | xem §1d | 21 |
| 4s nguy hiểm | `(shouting, voice cracking)` "¡Aguas, aguas! ¡Atrás de la roca, ya!" | 7 |
| 4s bíp | `(gasps)` "¡No mam— se está moviendo! ¡Ya!" (`bleep_at` tại "mam—") | 6 |
| 6s khuôn B | "La neta, yo tardé diez minutos. Ella, tantito. Qué oso, de veras." (`qué oso` = "quê quá") | 12 |

---

## 3. Trung Mỹ

### Luật chung cả vùng (trừ Panama)
- **Voseo** cho ngôi thứ hai số ít thân mật. Chia động từ: bỏ `-r`, thêm `-s` và nhấn trọng âm: `vos tenés`, `vos sabés`, `vos vivís`, `ser` → `vos sos`. Mệnh lệnh: bỏ `-r`, nhấn âm cuối: `mirá`, `vení`, `hablá`; kèm đại từ: `fijate`, `calmate`.
- **Số nhiều luôn là `ustedes`.** Nora nói với người xem (số nhiều) thì giống Mexico. Voseo chỉ lộ ra khi cô nói với **một người** (một người bản địa, chính mình, hoặc "bạn" người xem số ít). Viết ít nhất 1 câu voseo mỗi 2–3 clip để giọng nước đó hiện rõ.
- **`usted` rộng hơn** nơi khác: Guatemala và Honduras dùng với người trẻ, Honduras dùng cả giữa vợ chồng và bạn bè.
- **`j` thành tiếng "h" nhẹ** (bật hơi). `-n` cuối từ thành âm mũi sau, kiểu "ng".
- **Không trộn `tú` với `vos`** trong cùng một người nói. Ở Costa Rica, trộn hai cái bị coi là kém học thức.

### Hồ sơ từng nước

| Nước | Đại từ | Phát âm (điền câu khóa) | Từ đã xác minh | † Chưa xác minh |
|---|---|---|---|---|
| **Guatemala** — `from Guatemala City` | `vos` thân mật; `usted` cả với người trẻ | `the "rr" softly hissed`, `soft breathy "j"`, `crisp "s"` | `chilero` (ngầu), `cabal` (chuẩn, đúng), `patojo/a` (trẻ con), `pisto` (tiền), `chucho` (chó) | `¡a la gran!`, `puchica` |
| **El Salvador** — `from San Salvador` | `vos` chủ đạo; `tú` hiếm; `usted` để tôn trọng | `"s" at the end of syllables often softened to a breathy "h" in casual speech`, `soft breathy "j"` | `cipote` (trẻ con), `pisto` (tiền), `chucho` (chó), `está yuca` (khó quá), `bolo` (say) | `chivo` (ngầu), `vaya pues`, `cabal` |
| **Honduras** — `from Tegucigalpa` | `vos`; `usted` giữa bạn bè, vợ chồng | `"s" softened to "h" at syllable ends`, `"j" as a light "h"` | `cipote`, `güirro`, `chigüín` (trẻ con), `pisto`, `chucho`, `catracho` (người Honduras) | `macizo`, `cheque` |
| **Nicaragua** — `from Managua` | `vos` mạnh, mang tính bản sắc dân tộc; `usted` chỉ khi trang trọng | `"s" softened to "h" at syllable ends`, `word-final "n" nasal and soft` | `chavalo/a`, `chigüín` (trẻ con), `pulpería` (tiệm tạp hóa), `tuani` (tuyệt) | `chele`, `dale pues` |
| **Costa Rica** — `from San José, Costa Rica` | **`usted` chủ đạo, kể cả với bạn thân** (giới trẻ nam dẫn đầu); `vos` giữa bạn bè; `tú` bị coi là "không phải tico" | `the "r" and "rr" soft and almost like an English "r", especially in "tr"`, `word-final "n" like "ng"`, `crisp "s"` | `mae` (ông bạn), `tuanis` (ngầu), `vara` (cái thứ đó), `chante` (nhà), `güila` (trẻ con), `pulpería`, `pura vida` (chào / ổn cả / tạm biệt) | `diay`, `upe`, `qué chiva` |
| **Panama** — `from Panama City` | **`tú`**, không voseo (trừ Chiriquí) | giọng chuyển tiếp sang Caribe (đặc điểm suy ra từ nhóm Caribe, nguồn không ghi riêng): `fast, with "s" often softened at syllable ends` | `pelaíto` (trẻ con) | `¿qué xopá?`, `ofi`, `chuleta` |

Tần suất từ địa phương: tối đa 1 từ đậm chất nước đó mỗi clip. Thoại vẫn phải hiểu được với khán giả Mỹ Latinh nói chung.

### Câu mẫu (đã đếm, chỉ dùng từ đã xác minh)

| Nước | Clip | Thoại | Từ |
|---|---|---|---|
| Guatemala | 4s | "¡Qué chilero! Mirá cómo prende el fuego." | 7 |
| El Salvador | 6s | "Esto está yuca. Mirá, ni fuego ni comida, y ya está oscureciendo." | 12 |
| Honduras | 4s | "Mirá esos cipotes, ya saben cazar." | 6 |
| Nicaragua | 4s | "¡Qué tuani! Vení, vení, mirá esto." | 6 |
| Costa Rica | 6s | "Mae, esta vara está tuanis. Pero fíjense en esas huellas, qué miedo." | 12 |
| Panama | 4s | "Pelaítos de cinco años cazando. Yo, aquí temblando." | 8 |

`Mirá`, `vení` ở trên là Nora nói với một người (người bản địa, hoặc một người xem). `Fíjense` (Costa Rica) là nói với cả nhóm người xem → `ustedes`.

---

## 4. VOICE_LOCK — thêm 1 dòng xuất thân

Thêm vào `VOICE_LOCK` (`voice-bible.md` §1), để mọi câu thoại cùng chọn từ một nước:

```
Origin & dialect: grew up in <THÀNH PHỐ>; native <GIỌNG> Spanish. Uses <tú | vos | usted> with one person,
"ustedes" with the viewers. Signature words: <2–3 từ ở bảng>. Never: vosotros, Spain slang, English words.
```

Tật nói xoay vòng theo nước:
- Mexico: `a ver, a ver` / `no, espera—` / `la neta`
- Trung Mỹ (vos): `a ver, a ver` / `no, esperá—` / `fijate que…`
- Costa Rica: `a ver, a ver` / `no, espere—` / `mae…`

`esperá` (vos) và `espere` (usted) là mệnh lệnh khác nhau, phải khớp đại từ của nước đó.

---

## 5. Giọng bị trôi khi review → sửa prompt thế nào

| Triệu chứng nghe được | Nguyên nhân thường gặp | Sửa |
|---|---|---|
| Giọng Mỹ nói tiếng Tây Ban Nha | Ngoại hình nước ngoài + câu khóa quá chung | Thêm `native Spanish speaker from <thành phố>` và `no American or English accent when she speaks Spanish` |
| Ngọng "th" / giọng Madrid | Câu khóa thiếu `never a Spain accent`; có từ Tây Ban Nha lọt vào | Thêm câu cấm; rà bảng §5 của `dialogue-es-latam.md` |
| Chen chữ tiếng Anh ("okay", "wow") | Persona tiếng Anh cũ còn sót trong tag hoặc thoại | Đổi `okay` → `okey`/`órale`; thêm `says no English words` |
| Trung Mỹ nghe như Mexico | Model mặc định Mexico | Tăng ngữ pháp vos/usted và 1 từ địa phương mỗi clip; ghi đúng thành phố. Không lặp tính từ giọng thêm nữa |
| Đọc sai trọng âm 1 từ | Thiếu dấu | Thêm dấu; vẫn sai thì phiên âm đúng từ đó |
| Đọc to chỉ dẫn | Chỉ dẫn nằm trong ngoặc kép | Đưa ra ngoài ngoặc kép |

Mọi lần sinh lại đều phải hỏi user trước (Rule 29). Lỗi mới thì ghi bài học vào `production-lessons.md` và thêm dòng checklist B (`prompt-lock.md`).
