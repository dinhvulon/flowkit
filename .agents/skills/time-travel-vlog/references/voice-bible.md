# Voice Bible — Giọng nói & Tính cách Vlogger

`CHARACTER_LOCK` khóa **ngoại hình**, `voice_description` (Achernar) khóa **chất giọng**. File này khóa **cách nói**: vlogger là ai, biết gì, nói nhanh hay chậm, đùa kiểu gì, sợ gì, và những câu cô không bao giờ nói. Thiếu lớp này thì thoại tự trượt về giọng AI trung bình: cảm thán, giảng bài, câu chốt khẩu hiệu.

Đọc file này **trước khi viết bất kỳ dòng thoại nào**, và chạy checklist ở mục 6 trên từng dòng trước khi đưa vào `video_prompt`.

---

## 1. VOICE_LOCK — khóa tính cách (ghi vào `script.md`, KHÔNG sửa giữa các clip)

Persona đã chốt (user, 2026-10-01): **nhà khảo cổ học có kỹ năng sinh tồn thượng thừa, nói nhanh, liều, chửi thề nhẹ bị bíp**. Người xem ở lại vì cô **dạy được thứ dùng được** (phương pháp sinh tồn + lý do) và **biết lịch sử thật** đằng sau từng thứ cô chạm vào.

```
VOICE_LOCK:
Nora, 29, field archaeologist specialising in Ice Age sites, years of winter fieldwork,
cold-weather survival instructor on the side. She knows the method AND why it works.
Speed: fast, confident, explains while her hands are busy; cuts herself off when something
interesting or dangerous happens ("no, wait—").
Expertise style: says what to do, then the reason in one plain sentence, then the history
("we find this at dig sites"). Uses field-worker words, not textbook words.
Signature hook: she has dug up these objects broken in the ground for years, and now sees
them used. Theory vs reality excites her more than danger — sometimes at the worst moment.
Humor: dry, a bit cocky, self-aware when she nerds out ("sorry, archaeologist").
Tics (max one per clip, rotate): "okay, okay", "no, wait—", "real talk".
Flaw: reckless. Gets too close for the shot. Admits fear only after it's over.
Swearing: mild, cut off mid-word and bleeped in post ("sh—", "what the f—"). See section 3.
Never says: slogans, moral wrap-ups, "humanity", "our ancestors", "fascinating",
"incredible ingenuity", "survival rule number one", "here's the trick", "you won't believe".
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
- Đếm từ trước khi chốt. Dưới 22 từ ở clip 10s → thêm lý do hoặc chi tiết lịch sử, không thêm cảm thán.

---

## 3. Chửi thề bị bíp

- **Trong `video_prompt` chỉ viết từ bị cắt dở**: `"sh—"`, `"what the f—"`, `"holy cr—"`. Không viết đủ từ: tránh bộ lọc nội dung của Flow, và nếu quên bíp thì cũng không lọt từ tục.
- **Hậu kỳ**: phủ tiếng bíp ~0.3s đúng chỗ cắt. Ghi mốc vào Clip JSON: `"bleep_at": "4.2s"`.
- **Tần suất**: tối đa 1 lần / 3 clip. Không chửi trong clip hook mở đầu, không chửi trong beat kết trầm.
- Chỉ chửi **tình huống hoặc chính mình**, không bao giờ nhắm vào người bản địa.
- Chỗ chửi đẹp nhất: thú lớn quay đầu, chạm thứ lạnh buốt, hoặc cô nhận ra mình vừa đứng quá gần.

---

## 4. Ba khuôn beat truyền kiến thức

Nora là chuyên gia, nên kiến thức là lý do người xem ở lại. Nhưng chuyên gia **đọc bài giảng** thì vẫn là giọng AI. Mọi beat kiến thức đi theo 1 trong 3 khuôn, và kiến thức luôn gắn với **việc tay cô hoặc người bản địa đang làm trên hình**.

**A. Làm → Vì sao → Bằng chứng** (beat sinh tồn chính)
Nora vừa làm vừa nói: *làm gì* (mệnh lệnh ngắn) → *vì sao* (1 câu cơ chế, nói như người thường) → *bằng chứng khảo cổ / lịch sử* (thứ cô từng đào được, hoặc "we find this at sites like this").

**B. Lý thuyết vs Thực tế** (móc câu riêng của persona)
Cô từng thấy hiện vật nằm vỡ trong đất hoặc ngăn kéo bảo tàng, giờ thấy nó được dùng. Câu thoại: hiện vật cô biết → điều giới khảo cổ biết hoặc còn tranh cãi (phải là tranh cãi **có thật**) → điều cô đang thấy. Cảm xúc ở đây là sự phấn khích của dân trong nghề, không phải "wow" chung chung.

**C. Người bản địa dạy mẹo địa phương → Nora giải thích** (Translator POV)
Cô biết nguyên lý, họ biết vùng đất này. Clip A: người bản địa làm mẫu / ra hiệu (không thoại tiếng Anh). Clip B: whip pan / selfie về Nora, cô giải thích **vì sao** cách của họ đúng, bằng kiến thức của cô. Dùng khuôn này để Nora không thành kẻ biết tuốt và để bộ lạc có vai trò.

Phân bổ gợi ý trong một video: A ~50%, B ~25%, C ~25%.

**Cách nói mẹo:** mệnh lệnh trực tiếp kiểu người thật ("Don't eat snow. Ever.") thì được. **Nhãn khuôn mẫu** thì cấm ("Survival rule number one:", "Here's the trick:", "Pro tip:"). Đó là dấu hiệu nhận ra văn AI ngay lập tức.

---

## 5. Trước / sau (cùng nội dung, persona chuyên gia, đã đếm từ)

| Giọng AI (tránh) | Giọng Nora | Khuôn |
|---|---|---|
| "I just time travelled 20,000 years into the past... to the Ice Age!" | `Nora says (out of breath, fast): "Hour one. I'm an archaeologist. I've spent ten years digging this exact place up in pieces, and now it's minus forty-ish and the pieces are alive."` (26 từ) | Hook |
| "Never eat snow when you're freezing—it plummets your body temperature! Here's the trick: drop glowing basalt rocks into rawhide bags." | `Nora says (fast, hands busy, breath fogging): "Don't eat snow, ever. Your body burns heat just melting it. Hot rocks into a hide bag instead. That's probably why we keep digging up heat-cracked stones."` (27 từ) | A |
| "Survival rule number one in minus forty: you need pure animal fat. This mammoth marrow packs eight thousand calories!" | `Nora says (chewing, talking fast): "Marrow. Basically pure fat, and fat is everything here. Eat only lean meat in this cold and you get sick. That's why we find these bones smashed open."` (28 từ) | A |
| "An eyed bone needle! This single invention allowed humans to survive the freeze." | `Nora says (hushed, almost giddy): "An eyed bone needle. I've catalogued broken ones in museum drawers for years, never seen one used. She's stitching without even looking. I'm trying hard not to cry."` (28 từ) | B |
| "The storm cleared. Torak says the mammoth herds are moving." | `Nora says (whispering fast, crouched): "Trunk up, sniffing. That's probably the lead female checking the wind. Torak's kept us downwind for an hour. Smart. If she catches our scent, we're done."` (26 từ) | C |
| "The bull mammoth spotted us! Move, move, move!" | `Nora says (sprinting, voice cracking): "She's charging— sh— don't run in the open, she's way faster than us. Get behind the bone pile, something big, make her go around. Go!"` (25 từ, `bleep_at` tại "sh—") | A dưới áp lực |

Ghi chú fact-check cho các câu mẫu: tủy xương chủ yếu là mỡ, và ăn toàn thịt nạc gây "protein poisoning" (✅); đá nứt do nhiệt có mặt ở nhiều di chỉ, nhưng việc dùng để đun nước thời đồ đá cũ là ⚠️ nên có "probably"; đàn do con cái đầu đàn dẫn dắt là suy từ voi hiện đại (⚠️, có "probably"); voi ma mút có **tai nhỏ**, đừng viết "ears flared" như voi châu Phi.

---

## 6. Checklist chống giọng AI (chạy trên TỪNG dòng thoại)

**Phép thử chung:** đọc to lên. Một nhà khảo cổ 29 tuổi đang ở hiện trường có nói câu này với camera không, hay nghe như lời bình phim tài liệu? Lời bình → viết lại.

**Cấm:**
- [ ] Câu chốt khẩu hiệu / đạo lý: "Pure biological winter armor", "humanity persevered", "brains and brotherhood", "a testament to…".
- [ ] Mô tả lại thứ người xem đang thấy ("Look at the settlement. Four massive lodges!") → thay bằng điều người xem **không tự thấy được**: cách nó hoạt động, vì sao, cô từng đào được gì.
- [ ] Từ hướng dẫn viên: fascinating, incredible, ingenious, our ancestors, truly, simply.
- [ ] Bộ ba tu từ: "without metal, without electricity, without…".
- [ ] Nhãn khuôn mẫu: "Survival rule number one", "Here's the trick", "Pro tip", "Did you know".
- [ ] Số liệu không có trong bảng beat ✅ (calo, nhiệt độ chính xác, năm). Số có nguồn thì được nói, nhưng làm tròn kiểu người nói ("about twenty thousand years", "minus forty-ish").
- [ ] Gạch ngang giải thích kiểu "X—it's what keeps Y". Gạch ngang chỉ dùng cho tự ngắt / tự sửa.
- [ ] Câu cuối clip là câu tổng kết.

**Bắt buộc:**
- [ ] Mỗi beat kiến thức theo đúng 1 khuôn ở mục 4, gắn với hành động đang có trên hình.
- [ ] Lý do (vì sao) nói bằng 1 câu cơ chế đơn giản, không thuật ngữ trừ khi giải thích ngay.
- [ ] Mỗi 3–4 clip có ít nhất 1 chi tiết lịch sử / khảo cổ cụ thể (hiện vật, di chỉ, điều giới nghiên cứu biết hoặc tranh cãi).
- [ ] Cứ 2 clip có ít nhất 1 chỗ tự ngắt, tự sửa, hoặc 1 câu đùa khô.
- [ ] Người bản địa có vai trò thật (khuôn C), Nora không đúng mọi lúc về chuyện địa phương.
- [ ] Đúng 22–28 từ cho clip 10s (mục 2).

---

## 7. Fact-check mẹo sinh tồn và lịch sử (Rule 14)

Chuyên gia mà nói sai thì mất uy tín ngay ở phần bình luận. Mỗi mẹo và mỗi chi tiết lịch sử Nora nói phải nằm trong bảng beat của `era-research.md` với nguồn và ✅/⚠️. ⚠️ → nói dạng suy luận của nhà nghề: "probably", "most of us think", "the evidence says… but we argue about it".

Những câu nghe hay nhưng **sai hoặc không có nguồn**, đừng dùng:
- "Hít sâu ở −40°C là phổi bỏng lạnh": **sai**. Mũi và đường thở làm ấm không khí trước khi vào phổi, kể cả ở −50°C; thực tế chỉ rát họng, có thể co thắt phế quản.
- "Rơi găng 3 phút tê cóng, 10 phút hoại tử": **phóng đại**. Thời gian tê cóng phụ thuộc gió (tra bảng wind chill của NWS); hoại tử không xảy ra trong 10 phút.
- "Tủy voi ma mút 8,000 calo": **không có nguồn**. Nói "basically pure fat" thay vì con số.
- Lông mép mũ trùm "không đóng băng": **⚠️**. Mũ lông thời đồ đá cũ chỉ suy ra từ tượng nhỏ Siberia; tính chống đóng băng của từng loại lông còn tranh cãi.
- Câu đúng, dùng được: ăn tuyết tốn nhiệt cơ thể để làm tan; ăn toàn thịt nạc khi lạnh gây bệnh, cần mỡ; trốn sau vật lớn khi thú lớn lao tới; đá nung thả vào túi da tăng nhiệt dần, không sôi bùng ngay (xem §11 quy tắc 29 của skill).
