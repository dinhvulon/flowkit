# Voice Bible — Giọng nói & Tính cách Vlogger

`CHARACTER_LOCK` khóa **ngoại hình**, `voice_description` (Laomedeia) khóa **chất giọng**. File này khóa **cách nói**: vlogger là ai, biết gì, nói nhanh hay chậm, đùa kiểu gì, sợ gì, và những câu cô không bao giờ nói. Thiếu lớp này thì thoại tự trượt về giọng AI trung bình: cảm thán, giảng bài, câu chốt khẩu hiệu.

Đọc file này **trước khi viết bất kỳ dòng thoại nào**, và chạy checklist ở mục 6 trên từng dòng trước khi đưa vào `video_prompt`. Cấu trúc truyện, mật độ thoại theo loại clip và cách nhân vật phụ nói nằm ở `story-engine.md` (user chốt 2026-10-05); file đó thắng nếu hai file lệch nhau.

---

## 0. Chọn giọng (Slot 7 của Omni Flash `MZZa6b`) — mặc định: **Laomedeia**

Server lấy **từ đầu tiên** của `voice_description` làm voice id (ví dụ `"Laomedeia — upbeat, …"` → `laomedeia`). Nếu clip không gắn entity có voice (như cảnh POV, vốn không gắn ref vlogger), server dùng `narrator_voice` của project, rồi tới mặc định `laomedeia`. **Luôn đặt cả `voice_description` của vlogger lẫn `narrator_voice` của project** để mọi clip cùng một giọng.

**Hai giọng trong một clip (user chốt 2026-10-05):** nhân vật phụ được nói bằng ngôn ngữ không hiểu được. Hiện server chỉ gửi **1 voice id** vào Slot 7 (`request.extend([None, [[v_id]]])` trong `agent/services/flow_batch.py`), nên:
- **Chỉ vlogger có `voice_description`.** Không đặt cho nhân vật phụ, nếu không entity nào đứng trước trong DB sẽ cướp giọng của cả clip.
- Giọng nhân vật phụ **mô tả bằng chữ trong `video_prompt`**, gắn đúng sub-clip: `3-5s: The Leader speaks in a deep, gravelly male voice — short guttural non-English sounds, no recognizable words; Nora stays silent.` Không bao giờ để hai người nói chồng.
- Muốn gửi giọng thứ hai qua payload thật thì phải capture request của Flow UI trước (`docs/CAPTURE.md`); chưa capture thì không sửa code theo phỏng đoán.
- Test 1 clip trước khi gen hàng loạt. Nếu giọng nữ của vlogger phát ra từ miệng nhân vật phụ → clip đó quay về môi khép + cử chỉ (Bài học 49).

**Vì sao đổi từ Achernar sang Laomedeia (user chốt 2026-10-01):** Achernar là giọng "soft, high pitch", chỉ hợp thì thầm. Persona vlogger là nói nhanh, tự tin, hài khô, và phải hét khi gặp nguy hiểm, nên giọng mềm bị yếu. Laomedeia là "upbeat, mid-high": nói nhanh tự nhiên, lúc hét vẫn nghe hoảng thật chứ không gắt.

### Danh sách đầy đủ 30 giọng Pinhole / Gemini-TTS (user cung cấp 2026-10-05, `PINHOLE_VOICES`)

`id` viết thường là giá trị gửi vào Slot 7. Cao độ xếp từ thấp tới cao: **low / lower → mid-low → mid → mid-high / younger → high**.

| id | Giới | Tính chất | Cao độ | Gợi ý vai |
|---|---|---|---|---|
| achernar | Nữ | soft | high | Thì thầm, hồn ma, ASMR; yếu khi nói nhanh hoặc hét |
| achird | Nam | friendly | mid | Người lạ thân thiện, người dẫn đường |
| algenib | Nam | gravelly | low | Thủ lĩnh, già làng uy quyền, kẻ đe dọa |
| algieba | Nam | easy-going | mid-low | Người làng hiền, vlogger nam thư giãn |
| alnilam | Nam | firm | mid-low | Chiến binh, thợ săn cộc cằn, lính gác |
| aoede | Nữ | breezy | mid | Người phụ nữ vui tính, cô gái trong chợ |
| autonoe | Nữ | bright | mid | Phụ nữ lanh lợi, người hiểu biết; dự phòng cho vlogger nữ chín chắn |
| callirrhoe | Nữ | easy-going | mid | Người phụ nữ hiền, hàng xóm |
| charon | Nam | informative | lower | Người kể chuyện, học giả, thuyết minh tài liệu |
| despina | Nữ | smooth | mid | Người mẹ, người chăm sóc; không hợp cảnh hành động |
| enceladus | Nam | breathy | lower | Pháp sư, ông già, thầy thuốc |
| erinome | Nữ | clear | mid | Phụ nữ điềm tĩnh, người truyền tin |
| fenrir | Nam | excitable | younger | Thiếu niên, bé trai, thợ săn trẻ hăng hái |
| gacrux | Nữ | mature | mid | Bà già, nữ trưởng lão |
| iapetus | Nam | clear | mid-low | Người đàn ông điềm tĩnh, người đưa tin |
| kore | Nữ | firm | mid | Nữ thủ lĩnh, nữ chiến binh, người nghiêm khắc |
| **laomedeia** | Nữ | upbeat | mid-high | **Mặc định cho vlogger nữ — không giao cho nhân vật phụ** |
| leda | Nữ | youthful | mid-high | Bé gái, thiếu nữ (dưới ~22) |
| orus | Nam | firm | mid-low | Thủ lĩnh thứ hai, người nghiêm |
| puck | Nam | upbeat | mid | Chàng trai vui vẻ, vlogger nam năng lượng cao |
| pulcherrima | Không rõ giới | forward | mid-high | Sinh vật, nhân vật phi giới; tránh cho người thường |
| rasalgethi | Nam | informative | mid | Thương nhân hiểu biết, thầy giáo |
| sadachbia | Nam | lively | low | Gã to lớn vui tính, người lắm lời |
| sadaltager | Nam | knowledgeable | mid | Người già hiểu biết, thầy thuốc |
| schedar | Nam | even | mid-low | Kẻ lạnh lùng, phản diện bình tĩnh |
| sulafat | Nữ | warm | mid | Người mẹ, người phụ nữ ấm áp |
| umbriel | Nam | smooth | lower | Người đàn ông trầm tĩnh, pháp sư |
| vindemiatrix | Nữ | gentle | mid | Bà cụ hiền, người chữa bệnh |
| zephyr | Nữ | bright | mid-high | Gần Laomedeia nhưng ít "bốc" hơn |
| zubenelgenubi | Nam | casual | mid-low | Người làng xuề xòa, thương nhân |

### 0b. Tự chọn giọng cho nhân vật phụ (bắt buộc khi viết kịch bản, user chốt 2026-10-05)

Mỗi nhân vật phụ **có thoại** (kể cả ngôn ngữ không hiểu được, tiếng cười, một âm tiết) được giao **một voice id riêng** ngay ở bước viết kịch bản. Agent tự chọn, không hỏi user, theo các bước:

1. **Lọc theo giới + tuổi + vai** bằng bảng vai dưới đây; trong cột đó chọn giọng có tính chất khớp tính cách nhất.
2. **Tương phản:**
   - Không hai nhân vật nào trong cùng project dùng chung một id. Nhân vật quay lại ở tập sau giữ id cũ.
   - Hai nhân vật có thể nói trong cùng một clip phải cách nhau ít nhất 1 bậc cao độ.
   - Không bao giờ giao `laomedeia` (hay giọng của vlogger hiện tại) cho nhân vật phụ. Nhân vật nữ người lớn nói cùng clip với vlogger nữ: chọn cao độ mid, không chọn mid-high (zephyr, leda) để người xem không nhầm với vlogger.
   - Không dùng `achernar` và `pulcherrima` cho người thường, trừ khi cố ý (hồn ma, sinh vật).
3. **Khóa vào kịch bản:** thêm cột `Voice` vào bảng nhân vật trong `script.md` (`id — mô tả`). **Không** đặt `voice_description` trên entity nhân vật phụ: server lấy voice từ entity đầu tiên có `voice_description` (`agent/sdk/services/operations.py`), nên nhân vật phụ có trường này sẽ cướp giọng của vlogger trong cả clip.
4. **Viết vào `video_prompt`:** model video không biết tên giọng, nên đổi id thành mô tả theo bảng: `<Tên> speaks in a <tính chất>, <cao độ>-pitched <male/female> voice — <chất ngôn ngữ>, no recognizable words; <Vlogger> stays silent.` Ví dụ `algenib` → `The Leader speaks in a gravelly, low-pitched male voice — short guttural non-English sounds, consonant-heavy, no recognizable words; Nora stays silent.` Dùng **đúng một câu mô tả đó** cho nhân vật này ở mọi clip, để giọng nghe nhất quán.
5. Khi payload nhiều giọng được capture và nối vào code, id ở cột `Voice` là thứ sẽ được gửi; vì vậy luôn ghi id đúng chính tả theo bảng trên.

| Vai | Nam | Nữ |
|---|---|---|
| Thủ lĩnh, già làng uy quyền | algenib, orus | kore |
| Chiến binh, thợ săn, lính gác cộc cằn | alnilam, schedar | kore |
| Thanh niên hăng hái, thiếu niên | fenrir, puck | leda |
| Trẻ em | fenrir (bé trai) | leda (bé gái) |
| Người già, pháp sư, thầy thuốc | enceladus, umbriel, sadaltager | gacrux, vindemiatrix |
| Người mẹ, người chăm sóc | — | sulafat, despina |
| Người lắm lời, vui tính, thương nhân | sadachbia, zubenelgenubi, achird, rasalgethi | aoede, callirrhoe |
| Người hiền, dân làng bình thường | algieba, iapetus | callirrhoe, erinome |
| Phản diện, kẻ đe dọa | schedar, algenib | kore |
| Người lanh lợi, hiểu biết | charon, rasalgethi | autonoe, erinome |

**Chất ngôn ngữ không hiểu được** (ghép sau mô tả giọng): tiền sử / Neanderthal → `short guttural sounds, consonant-heavy`; cổ đại → `a flowing ancient-sounding language with rolling r's`; trung cổ / thời khác → `a fast, unfamiliar old dialect`. Luôn kết bằng `no recognizable words`.

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
Line length: short. Lets the picture do the work; talks less when it gets dangerous.
Never uses meta language: "as you saw earlier", "in this video", "this is where things get
interesting", "I didn't know this yet".
Humor: dry, a bit cocky, self-aware ("okay, that was embarrassing").
Tics (max one per clip, rotate): "okay, okay", "no, wait—", "real talk".
Flaw: reckless. Gets too close for the shot. Admits fear only after it's over.
Swearing: mild, cut off mid-word and bleeped in post ("sh—", "what the f—"). See section 3.
Never says: slogans, moral wrap-ups, "humanity", "our ancestors", "fascinating",
"incredible ingenuity", "survival rule number one", "here's the trick", "you won't believe",
"historians say", "archaeologists think".
Relationship with the locals: she knows the principles; they know THIS land, THIS herd,
THIS weather. They speak a language she can't understand; she never translates their words,
she reads tone and gestures ("No idea what he said. But that was a no.").
Hour 1 they're wary → she fails in front of them → she earns respect with a real skill →
she learns local tricks by watching and copying → after the climax she's part of the group.
```

Persona khác (series sau) → viết `VOICE_LOCK` mới theo đúng các trường: **ai + chuyên môn / tốc độ / phong cách giải thích / móc câu riêng / kiểu hài / tật nói / điểm yếu / chửi thề / không bao giờ nói / quan hệ với người bản địa**. Tên trong `VOICE_LOCK` phải trùng tên trong `CHARACTER_LOCK` và tên người nói trong `video_prompt`.

---

## 2. Mật độ thoại theo loại clip (user chốt 2026-10-05, thay bảng 18–22 / 22–28 từ cũ)

Thoại dày làm phim thành podcast có hình. Hình làm được thì để hình làm.

| Loại clip (8s) | Số từ tiếng Anh của vlogger |
|---|---|
| Bình thường | **8–15** |
| Căng thẳng / nguy hiểm | **3–8** |
| Cảm xúc | 5–12 |
| Giải thích (hiếm) | tối đa 12–18 |
| Nhịp im lặng, cảnh cuối | 0 |

- Clip 10s cộng tối đa ~25%; clip 4–6s giảm theo tỉ lệ. Đây là **trần**, không phải chỉ tiêu: không bao giờ độn cho đủ từ.
- **Show > Tell:** `"Fire."` khi người xem đã thấy tia lửa, không phải `"Now I'm making fire using the flint I found earlier."`
- **Nhịp im lặng:** mỗi Act ít nhất 1 lần không ai nói từ 1s trở lên trước một tiết lộ. Kịch bản ghi `[im lặng 2s]`, prompt ghi `No one speaks for the first 2 seconds; only wind and breathing.`
- **Không nói chồng.** Nhân vật phụ nói (ngôn ngữ không hiểu được) ở sub-clip riêng, Nora im lặng phản ứng trong lúc đó, rồi mới nói.
- Luôn ghi cách diễn đạt trong ngoặc ngay sau tên: `Nora says (hushed, hands busy, breath fogging): "..."`. Model video phản ứng với tag này mạnh hơn với tính từ rải trong prompt.
- Đếm từ trước khi chốt. Vượt trần → cắt phần mô tả thứ người xem đang thấy trước, rồi tới lý do.

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

**C. Người bản địa dạy → Nora làm theo**
Người bản địa làm mẫu, ra hiệu, có thể nói vài tiếng bằng ngôn ngữ không hiểu được (không tiếng Anh, giọng ghi rõ trong prompt). Nora không dịch: cô làm theo, và nói vài từ về điều cô vừa cảm thấy ("Oh. Lighter. Way lighter."). Dùng khuôn này để Nora không thành kẻ biết tuốt và để bộ lạc có vai trò.

Phân bổ gợi ý trong một video: A ~50%, B ~25%, C ~25%.

**Cách nói mẹo:** mệnh lệnh trực tiếp kiểu người thật ("Don't eat snow. Ever.") thì được. **Nhãn khuôn mẫu** thì cấm ("Survival rule number one:", "Here's the trick:", "Pro tip:"). Đó là dấu hiệu nhận ra văn AI ngay lập tức.

---

## 5. Trước / sau (cùng nội dung, persona chuyên gia, đã đếm từ theo mật độ 2026-10-05)

| Giọng AI (tránh) | Giọng Nora | Khuôn |
|---|---|---|
| "I just time travelled 20,000 years into the past... to the Ice Age!" | `Nora says (out of breath): "Minus forty-ish. No tent. And a man with a spear deciding if I live."` (14 từ) | Hook (bình thường) |
| "Never eat snow when you're freezing—it plummets your body temperature! Here's the trick: drop glowing basalt rocks into rawhide bags." | `Nora says (hands busy, breath fogging): "Don't eat snow. It steals your heat. Hot rocks in the bag."` (12 từ) | A |
| "Survival rule number one in minus forty: you need pure animal fat. This mammoth marrow packs eight thousand calories!" | `Nora says (chewing): "Marrow. Pure fat, and out here fat is heat. Tastes like candle. Still eating."` (14 từ) | A |
| "An eyed bone needle! This single invention allowed humans to survive the freeze." | `Nora says (hushed, dry): "Ten minutes trying to thread this. She does it in the dark."` (12 từ) | B |
| "The storm cleared. Torak says the mammoth herds are moving." | `3-5s: Torak speaks low and gravelly — two short guttural non-English words, no recognizable words; Nora stays silent.` → `5-8s: Nora whispers: "No idea what he said. We're not moving."` (8 từ) | C |
| "The bull mammoth spotted us! Move, move, move!" | `Nora says (sprinting, voice cracking): "She's charging— sh— behind the bones. Go!"` (7 từ, `bleep_at` tại "sh—") | A dưới áp lực (căng thẳng) |
| "Finally, after everything, I made it through the night. What an incredible journey." | `No one speaks. Nora looks at the small bone bead in her palm, then up at the cave mouth.` (0 từ) | Cảnh cuối |

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
- [ ] Meta language: "as you saw earlier", "you saw the cold open", "in this video", "this is where things get interesting", "I didn't know this yet".
- [ ] Nhân vật phụ nói tiếng Anh, hoặc Nora dịch nguyên văn lời họ.
- [ ] Hai người nói chồng trong cùng một sub-clip.

**Bắt buộc:**
- [ ] Mỗi beat kiến thức theo đúng 1 khuôn ở mục 4, gắn với hành động đang có trên hình.
- [ ] Lý do (vì sao) nói bằng 1 câu cơ chế đơn giản, không thuật ngữ trừ khi giải thích ngay.
- [ ] Mỗi 3–4 clip có ít nhất 1 chi tiết lạ của thế giới này (thật hay bịa) hiện ra qua việc đang làm trên hình — không giảng.
- [ ] Cứ 2 clip có ít nhất 1 chỗ tự ngắt, tự sửa, hoặc 1 câu đùa khô.
- [ ] Người bản địa có vai trò thật (khuôn C), Nora không đúng mọi lúc về chuyện địa phương.
- [ ] Không vượt trần mật độ ở mục 2 theo loại clip (8s: bình thường 8–15, căng thẳng 3–8, cảm xúc 5–12, giải thích ≤ 12–18).
- [ ] Mỗi Act có ít nhất 1 nhịp im lặng.

---

## 7. Hư cấu

Mọi thứ trong phim được bịa thoải mái (user chốt 2026-10-05), kể cả mẹo sinh tồn: phong tục, công cụ, hành vi động vật, sự kiện, cách sống sót — không cần nguồn, không cần "probably", không cần đúng ngoài đời. Tiêu chí duy nhất: **câu chuyện hay, thu hút, giữ chân người xem**. Mẹo bịa vẫn phải nói tự tin như chuyên gia và gắn với việc đang làm trên hình (mục 4).
