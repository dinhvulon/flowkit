# Voice Bible — Giọng nói & Tính cách Vlogger

`CHARACTER_LOCK` khóa **ngoại hình**, `voice_description` (Laomedeia) khóa **chất giọng**. File này khóa **cách nói**: vlogger là ai, biết gì, nói nhanh hay chậm, đùa kiểu gì, sợ gì, và những câu cô không bao giờ nói. Thiếu lớp này thì thoại tự trượt về giọng AI trung bình: cảm thán, giảng bài, câu chốt khẩu hiệu.

Đọc file này **trước khi viết bất kỳ dòng thoại nào**, và chạy checklist ở mục 6 trên từng dòng trước khi đưa vào `video_prompt`.

---

## 0. Chọn giọng (Slot 7 của Omni Flash `MZZa6b`) — mặc định: **Laomedeia**

Server lấy **từ đầu tiên** của `voice_description` làm voice id (ví dụ `"Laomedeia — upbeat, …"` → `laomedeia`). Nếu clip không gắn entity có voice (như cảnh POV, vốn không gắn ref vlogger), server dùng `narrator_voice` của project, rồi tới mặc định `laomedeia`. **Luôn đặt cả `voice_description` của vlogger lẫn `narrator_voice` của project** để mọi clip cùng một giọng.

**Vì sao đổi từ Achernar sang Laomedeia (user chốt 2026-10-01):** Achernar là giọng "soft, high pitch", chỉ hợp thì thầm. Persona vlogger là nói nhanh, tự tin, hài khô, và phải hét khi gặp nguy hiểm, nên giọng mềm bị yếu. Laomedeia là "upbeat, mid-high": nói nhanh tự nhiên, lúc hét vẫn nghe hoảng thật chứ không gắt.

| Giới | Giọng (id) | Tính chất, cao độ | Dùng cho |
|---|---|---|---|
| Nữ | **laomedeia** | upbeat, mid-high | **Mặc định cho vlogger nữ** |
| Nữ | autonoe | bright, mid | Dự phòng: chuyên gia nghe chín chắn hơn |
| Nữ | zephyr | bright, mid-high | Gần Laomedeia nhưng ít "bốc" hơn |
| Nữ | kore | firm, mid | Nhân vật nghiêm, uy quyền |
| Nữ | leda | youthful, mid-high | Nhân vật trẻ (dưới ~22) |
| Nữ | erinome | clear, mid | Người dẫn rõ ràng, trung tính |
| Nữ | aoede / callirrhoe | breezy / easy-going, mid | Vlog thư giãn, du lịch nhẹ |
| Nữ | gacrux | mature, mid | Nhân vật lớn tuổi |
| Nữ | sulafat / vindemiatrix / despina | warm / gentle / smooth, mid | Thuyết minh êm, KHÔNG hợp cảnh hành động |
| Nữ | achernar | soft, high | Thì thầm, ASMR; yếu khi nói nhanh hoặc hét |
| Không rõ | pulcherrima | forward, mid-high | Tránh dùng cho nhân vật nữ, có thể nghe không ra giới |
| Nam | puck / fenrir | upbeat, mid / excitable, younger | Vlogger nam năng lượng cao |
| Nam | achird / zubenelgenubi / algieba | friendly / casual / easy-going | Vlogger nam thư giãn |
| Nam | charon / rasalgethi / sadaltager | informative / knowledgeable | Thuyết minh tài liệu |
| Nam | orus / alnilam / iapetus / schedar | firm / clear / even, mid-low | Nhân vật nghiêm |
| Nam | algenib / enceladus / umbriel / sadachbia | gravelly / breathy / smooth / lively, low | Giọng trầm, nhân vật đặc biệt |

---

## 1. VOICE_LOCK — khóa tính cách (ghi vào `script.md`, KHÔNG sửa giữa các clip)

Persona đã chốt (user, 2026-10-01; sửa 2026-10-05): **chuyên gia sinh tồn, nói nhanh, liều, chửi thề nhẹ bị bíp — KHÔNG dạy lịch sử**. Người xem ở lại vì cô **làm được việc thật** (biết cách và biết vì sao, nói bằng một câu đời thường), vì cô hài, và vì nguy hiểm leo thang. Cô không phải "cô gái thành phố ngơ ngác" (persona đó đã bị loại), nhưng cũng không phải giảng viên. Chi tiết thế giới được bịa thoải mái (xem "Hư cấu được phép" ở đầu `skills/fk-time-travel-vlog.md`).

```
VOICE_LOCK:
Nora, 29, wilderness survival expert, years of rough fieldwork in brutal places
(backstory from ep 1: trained as an archaeologist — never lectures about it).
Speed: fast, confident, explains while her hands are busy; cuts herself off when something
interesting or dangerous happens ("no, wait—").
Expertise style: says what to do, then the reason in one plain sentence. Field-worker words,
not textbook words. NO history lessons: no dates, no dig sites, no "scientists argue",
no "we find this at sites", no studies.
Signature hook: she's good, but this world keeps out-skilling her — the locals do in seconds
what she fumbles for minutes, and she admits it with dry humor.
Humor: dry, a bit cocky, self-aware ("okay, that was embarrassing").
Tics (max one per clip, rotate): "okay, okay", "no, wait—", "real talk".
Flaw: reckless. Gets too close for the shot. Admits fear only after it's over.
Swearing: mild, cut off mid-word and bleeped in post ("sh—", "what the f—"). See section 3.
Never says: slogans, moral wrap-ups, "humanity", "our ancestors", "fascinating",
"incredible ingenuity", "survival rule number one", "here's the trick", "you won't believe",
"historians say", "archaeologists think".
Relationship with the locals: she knows the principles; they know THIS land, THIS herd,
THIS weather. Hour 1 they're wary → she earns respect with a real skill → she learns
local tricks from them and translates → after the climax she's part of the group.
```

Persona khác (series sau) → viết `VOICE_LOCK` mới theo đúng các trường: **ai + chuyên môn / tốc độ / phong cách giải thích / móc câu riêng / kiểu hài / tật nói / điểm yếu / chửi thề / không bao giờ nói / quan hệ với người bản địa**. Tên trong `VOICE_LOCK` phải trùng tên trong `CHARACTER_LOCK` và tên người nói trong `video_prompt`.

---

## 2. Mật độ thoại (user chốt: nói nhanh để giữ nhịp, không gây buồn ngủ)

| `duration` clip | Số từ tiếng Anh | Khoảng nói |
|---|---|---|
| 10s | **22–28 từ** | ~0.5s → ~9.5s |
| 8s | 18–22 từ | ~0.5s → ~7.5s |
| 6s | 13–16 từ | ~0.5s → ~5.5s |
| 4s | 8–10 từ | ~0.3s → ~3.7s |

- Chỉ chừa **~0.5s đầu và cuối clip** không thoại để cắt chuyển cảnh; không bao giờ cắt ngang câu.
- **Một người nói/clip** (giới hạn 1 giọng của R2V). Clip người bản địa diễn → Nora im lặng phản ứng, thoại dồn sang clip sau.
- Luôn ghi cách diễn đạt trong ngoặc ngay sau tên: `Nora says (fast, hands busy, breath fogging): "..."`. Model video phản ứng với tag này mạnh hơn với tính từ rải trong prompt.
- Đếm từ trước khi chốt. Dưới 22 từ ở clip 10s → thêm lý do, cảm giác cơ thể hoặc một câu đùa khô; không thêm cảm thán, không thêm bài giảng.

---

## 3. Chửi thề bị bíp

- **Trong `video_prompt` chỉ viết từ bị cắt dở**: `"sh—"`, `"what the f—"`, `"holy cr—"`. Không viết đủ từ: tránh bộ lọc nội dung của Flow, và nếu quên bíp thì cũng không lọt từ tục.
- **Hậu kỳ**: phủ tiếng bíp ~0.3s đúng chỗ cắt. Ghi mốc vào Clip JSON: `"bleep_at": "4.2s"`.
- **Tần suất**: tối đa 1 lần / 3 clip. Không chửi trong clip hook mở đầu, không chửi trong beat kết trầm.
- Chỉ chửi **tình huống hoặc chính mình**, không bao giờ nhắm vào người bản địa.
- Chỗ chửi đẹp nhất: thú lớn quay đầu, chạm thứ lạnh buốt, hoặc cô nhận ra mình vừa đứng quá gần.

---

## 4. Ba khuôn beat sinh tồn

Nora giỏi, nên cách làm là lý do người xem ở lại. Nhưng chuyên gia **đọc bài giảng** thì vẫn là giọng AI, và cô **không giảng lịch sử**. Mọi beat theo 1 trong 3 khuôn, luôn gắn với **việc tay cô hoặc người bản địa đang làm trên hình**.

**A. Làm → Vì sao** (beat sinh tồn chính)
Nora vừa làm vừa nói: *làm gì* (mệnh lệnh ngắn) → *vì sao* (1 câu cơ chế, nói như người thường) → *cảm giác / hệ quả ngay lúc đó* (tay hết run, mùi, đau, đói). Không có câu "bằng chứng".

**B. Cách của mình vs cách của họ** (móc câu riêng của persona)
Cô thử theo cách cô biết (hiện đại, sách vở, kinh nghiệm cũ) → thất bại hoặc chậm → người bản địa làm được trong vài giây → cô thừa nhận bằng một câu đùa khô. Cảm xúc là tự ái nghề nghiệp bị đánh bại, không phải "wow".

**C. Người bản địa dạy → Nora làm theo** (Translator POV)
Clip A: người bản địa làm mẫu / ra hiệu (không thoại tiếng Anh). Clip B: Nora làm theo, nói cô vừa hiểu ra điều gì và vì sao nó hiệu quả — bằng cảm nhận thực tế, không bằng kiến thức lịch sử. Dùng khuôn này để Nora không thành kẻ biết tuốt và để bộ lạc có vai trò.

Phân bổ gợi ý trong một video: A ~50%, B ~25%, C ~25%.

**Cách nói mẹo:** mệnh lệnh trực tiếp kiểu người thật ("Don't eat snow. Ever.") thì được. **Nhãn khuôn mẫu** thì cấm ("Survival rule number one:", "Here's the trick:", "Pro tip:"). Đó là dấu hiệu nhận ra văn AI ngay lập tức.

---

## 5. Trước / sau (cùng nội dung, persona chuyên gia, đã đếm từ)

| Giọng AI (tránh) | Giọng Nora | Khuôn |
|---|---|---|
| "I just time travelled 20,000 years into the past... to the Ice Age!" | `Nora says (out of breath, fast): "Hour one. Minus forty-ish, no tent, no jacket of my own, and a man with a spear deciding if I live. Great start."` (23 từ) | Hook |
| "Never eat snow when you're freezing—it plummets your body temperature! Here's the trick: drop glowing basalt rocks into rawhide bags." | `Nora says (fast, hands busy, breath fogging): "Don't eat snow, ever. Your body burns heat just melting it. Hot rocks into a hide bag instead. Slower, but my hands stopped shaking."` (24 từ) | A |
| "Survival rule number one in minus forty: you need pure animal fat. This mammoth marrow packs eight thousand calories!" | `Nora says (chewing, talking fast): "Marrow. Basically pure fat, and fat is everything here. Eat only lean meat in this cold and you get sick. Tastes like warm candle. Still eating."` (26 từ) | A |
| "An eyed bone needle! This single invention allowed humans to survive the freeze." | `Nora says (hushed, dry): "I tried threading this for ten minutes. She does it without looking, mid-conversation, in the dark. Okay, I'm officially the worst seamstress here."` (23 từ) | B |
| "The storm cleared. Torak says the mammoth herds are moving." | `Nora says (whispering fast, crouched): "Trunk up, sniffing. That's the lead female checking the wind. Torak's kept us downwind for an hour. Smart. If she catches our scent, we're done."` (25 từ) | C |
| "The bull mammoth spotted us! Move, move, move!" | `Nora says (sprinting, voice cracking): "She's charging— sh— don't run in the open, she's way faster than us. Get behind the bone pile, something big, make her go around. Go!"` (25 từ, `bleep_at` tại "sh—") | A dưới áp lực |

Ghi chú: các câu mẫu không có chi tiết lịch sử nào — đúng persona. Chi tiết thế giới và mẹo sinh tồn đều có thể bịa — miễn câu hay và tự nhiên.

---

## 6. Checklist chống giọng AI (chạy trên TỪNG dòng thoại)

**Phép thử chung:** đọc to lên. Một cô gái 29 tuổi đang cố sống sót có nói câu này với camera không, hay nghe như lời bình phim tài liệu / bài giảng? Lời bình → viết lại.

**Cấm:**
- [ ] Câu chốt khẩu hiệu / đạo lý: "Pure biological winter armor", "humanity persevered", "brains and brotherhood", "a testament to…".
- [ ] Mô tả lại thứ người xem đang thấy ("Look at the settlement. Four massive lodges!") → thay bằng điều người xem **không tự thấy được**: cách nó hoạt động, vì sao, cô cảm thấy gì.
- [ ] Từ hướng dẫn viên: fascinating, incredible, ingenious, our ancestors, truly, simply.
- [ ] Bộ ba tu từ: "without metal, without electricity, without…".
- [ ] Nhãn khuôn mẫu: "Survival rule number one", "Here's the trick", "Pro tip", "Did you know".
- [ ] Giảng lịch sử: niên đại, tên di chỉ, "scientists argue", "we find this at sites", "archaeologists think", trích nghiên cứu.
- [ ] Số liệu kiểu sách giáo khoa (calo, %, nhiệt độ chính xác). Số chỉ nói làm tròn kiểu người thường ("minus forty-ish").
- [ ] Gạch ngang giải thích kiểu "X—it's what keeps Y". Gạch ngang chỉ dùng cho tự ngắt / tự sửa.
- [ ] Câu cuối clip là câu tổng kết.

**Bắt buộc:**
- [ ] Mỗi beat kiến thức theo đúng 1 khuôn ở mục 4, gắn với hành động đang có trên hình.
- [ ] Lý do (vì sao) nói bằng 1 câu cơ chế đơn giản, không thuật ngữ trừ khi giải thích ngay.
- [ ] Mỗi 3–4 clip có ít nhất 1 chi tiết lạ của thế giới này (thật hay bịa) hiện ra qua việc đang làm trên hình — không giảng.
- [ ] Cứ 2 clip có ít nhất 1 chỗ tự ngắt, tự sửa, hoặc 1 câu đùa khô.
- [ ] Người bản địa có vai trò thật (khuôn C), Nora không đúng mọi lúc về chuyện địa phương.
- [ ] Đúng mật độ từ ở mục 2 (10s: 22–28, 8s: 18–22).

---

## 7. Hư cấu

Mọi thứ trong phim được bịa thoải mái (user chốt 2026-10-05), kể cả mẹo sinh tồn: phong tục, công cụ, hành vi động vật, sự kiện, cách sống sót — không cần nguồn, không cần "probably", không cần đúng ngoài đời. Tiêu chí duy nhất: **câu chuyện hay, thu hút, giữ chân người xem**. Mẹo bịa vẫn phải nói tự tin như chuyên gia và gắn với việc đang làm trên hình (mục 4).
