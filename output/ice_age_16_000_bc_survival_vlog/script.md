# I Survived 24 Hours in an Ice Age Mammoth-Bone Camp — kịch bản

Skill: `/fk-time-travel-vlog` (Survival Preset §5c, voice-bible, §11). Project FlowKit `5fda95b9-ba37-41bf-95ab-f33a50beabe8`.
Trạng thái: **mục 1–5b xong, chờ user duyệt bảng vật lý (5b)** trước khi viết Clip JSON (mục 6).

---

## 1. Giả định

- **Nơi, năm:** Mezhyrich (Межиріч), tỉnh Cherkasy, Ukraine, trên thềm sông chỗ sông Rosava gặp sông Ros, lưu vực trung Dnieper. Khoảng **16.000 BC (~18.000 năm trước)**. Dwelling lớn nhất (MBS 4) có niên đại 18.248–17.764 cal BP, thuộc pha khắc nghiệt nhất của Kỷ Băng Hà cuối.
- **Mùa và ánh sáng:** cuối đông (khoảng tháng 3), ngày dài ~12 giờ. Giờ 0 là lúc trời vừa sáng, cao trào rơi vào hoàng hôn, hồi Di sản diễn ra ban đêm, Giờ 24 là bình minh hôm sau.
- **Độ dài:** 48 clip, tổng khoảng 7:46. 43 clip dài 10s; ở cao trào có 3 clip 8s và 2 clip 6s để tăng nhịp.
- **Khung và chất liệu:** HORIZONTAL 16:9, material `phone_vlog`. R2V qua Omni Flash Ingredients (`GENERATE_VIDEO_REFS`), mỗi clip tối đa 3 ref và luôn có Nora.
- **Preset:** Survival Preset (§5c), đồng hồ 24 giờ. Nora là nhà khảo cổ có kỹ năng sinh tồn. Người bản địa không nói tiếng Anh (Translator POV), chỉ Nora có giọng.

## 2. Character Bible

### CHARACTER_LOCK (dán nguyên văn vào entity `description` của Nora, không sửa)

```
CHARACTER_LOCK:
Nora, a 29-year-old Western woman with a soft rounded oval face and full cheeks, fair skin with a natural
pink flush, grey-green eyes, defined light-brown brows, natural pink glossy lips, honey-blonde hair pulled
into a high wavy ponytail with long curtain bangs framing her face, small gold hoop earrings.
Full, curvy hourglass figure: full bust, narrow defined waist, wide rounded hips, healthy strong build.
She wears a knee-length fitted reindeer-hide parka cut close to the body, cinched at the waist by a wide
leather belt sewn with rows of drilled arctic-fox canine teeth, a white arctic-fox fur hood usually pushed
back onto her shoulders, short rows of tiny mammoth-ivory beads across the chest and cuffs, fur mittens
hanging from a cord at both cuffs, fitted dark hide trousers and fur-lined hide boots.
```

Khuôn mặt lấy từ `uploads/nora_main.jpg`. Ảnh ref là **một sheet 16:9**: mặt chính diện | góc 3/4 | toàn thân mặc trang phục, không có entity Outfit riêng (§2, §11 quy tắc 22).

### voice_description (chỉ Nora có)

```
Achernar — soft, higher-pitched, natural expressive conversational female voice, casual vlog tone, breathy when amazed, hushed whisper when nervous.
```

### VOICE_LOCK (luật viết thoại, không đưa vào prompt)

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
Swearing: mild, cut off mid-word and bleeped in post ("sh—", "what the f—").
Never says: slogans, moral wrap-ups, "humanity", "our ancestors", "fascinating",
"incredible ingenuity", "survival rule number one", "here's the trick", "you won't believe".
Relationship with the locals: she knows the principles; they know THIS land, THIS herd,
THIS weather. Hour 1 they're wary → she earns respect with a real skill → she learns
local tricks from them and translates → after the climax she's part of the group.
```

### Người bản địa (không có giọng, giao tiếp bằng cử chỉ)

- **Torak**, khoảng 40 tuổi, thợ săn dẫn đường: tóc nâu sẫm buộc ra sau, râu ngắn dày dính sương giá, mắt sâu màu sẫm, da màu nâu ô-liu sạm gió. Mặc parka da tuần lộc có mũ viền lông cáo và cầm giáo gỗ mũi đá lửa.
- **Alva**, khoảng 35 tuổi, giữ lửa và may vá: hai bím tóc sẫm quấn dây da, mắt sẫm, da nâu ô-liu. Áo da may khít, đeo chuỗi hạt hổ phách và vỏ ốc hóa thạch, có kim xương giắt ở cổ áo.
- **Sắc tộc:** dân săn bắt hái lượm thời Epigravettian. Dữ liệu aDNA cho thấy màu da sẫm hơn người châu Âu ngày nay (⚠️), nên tả da nâu ô-liu, tóc và mắt sẫm, không viết mắt xanh.

### Entity (8 ref, tất cả 16:9)

| Entity | Loại | Vai trò |
|---|---|---|
| Nora | character | Vlogger. Có voice Achernar. Sheet: mặt, góc 3/4, toàn thân mặc parka |
| Torak | character | Thợ săn dẫn đường. Sheet 3 góc |
| Alva | character | Giữ lửa và may vá. Sheet 3 góc |
| Mezhyrich Camp | visual_asset | 4 dwelling xương voi ma mút trên thềm sông phủ tuyết, có hố và lửa |
| Bone Dwelling Interior | visual_asset | Bên trong dwelling: bếp lửa đốt xương, da treo, túi nước da |
| Mammoth Steppe | visual_asset | Thảo nguyên, thung lũng sông đóng băng, bờ sông dốc có viền băng, khe xương cũ |
| Woolly Mammoth | visual_asset | Voi ma mút cái, chụp ngang toàn thân, tai nhỏ |
| Painted Mammoth Skull | visual_asset | Sọ voi ma mút ở cửa, vẽ chấm và vạch bằng ochre đỏ |

## 3. Research pack — bảng beat

✅ = có nguồn và được đồng thuận. ⚠️ = suy luận hoặc còn tranh cãi; Nora nói kèm "probably" hay "we argue".

| Beat / clip | Sự thật dùng trong thoại hoặc hình | Độ chắc | Nguồn |
|---|---|---|---|
| Hook S01–02 | Mezhyrich ở Ukraine; dwelling lớn nhất có niên đại 18.248–17.764 cal BP, "pha khắc nghiệt nhất của Kỷ Băng Hà cuối" | ✅ | Leiden Univ. (11/2025); Live Science; Sci.News; Archaeology (12/2025) |
| S02, S45 | 4 cấu trúc tròn bằng xương voi ma mút, mỗi cái 12–24 m², xung quanh có hố, khu xưởng, bãi rác | ✅ | Wikipedia "Mezhyrich"; donsmaps.com |
| S07 | Phần chân tường xếp bằng hàm dưới voi ma mút theo kiểu zigzag/xương cá | ✅ | donsmaps (Mezhyrich dwelling 1); hiện vật dựng lại trong bảo tàng ở Kyiv |
| S08 | Chức năng còn tranh cãi (nhà ở, kho, công trình nghi lễ); niên đại mới cho thấy thời gian ở ngắn | ⚠️ / ✅ | Leiden 2025; Earth.com |
| S09 | Bếp ở Mezhyrich có rất ít than củi; xương có thể là nhiên liệu | ✅ / ⚠️ | Marquer et al.; Valladas (taphonomy) |
| S10 | Ăn tuyết tốn nhiệt cơ thể để làm tan | ✅ | Hướng dẫn sinh tồn vùng lạnh (US Army FM 3-05.70) |
| S11 | Đá nứt do nhiệt có ở nhiều di chỉ; đun nước bằng đá nóng thời đồ đá cũ chưa chắc chắn | ✅ / ⚠️ | voice-bible §7 |
| S04–05 | Frostnip làm da trắng và tê; không chà xát, làm ấm bằng da ấm | ✅ | Mayo Clinic "Frostbite: first aid" |
| S06 | Găng hở ngón kiểu mitten ấm hơn găng tay có ngón vì các ngón sưởi cho nhau; buộc dây để không đánh rơi | ✅ (kỹ thuật) | FM 3-05.70. Không nói găng thời đồ đá cũ có bằng chứng |
| S12 | Chỉ ăn thịt nạc khi lạnh sẽ bị "protein poisoning"; mỡ là nguồn năng lượng | ✅ | voice-bible §7; Speth (hunter-gatherer diet) |
| S13 | Hố quanh dwelling, được hiểu là hố trữ thực phẩm; đất đóng băng vĩnh cửu liên tục | ⚠️ / ✅ | donsmaps; tái dựng cổ khí hậu LGM Ukraine |
| S14 | Có rất nhiều xương cáo ở Mezhyrich; da cáo còn đuôi có lẽ được thuộc và mặc | ✅ | donsmaps; Soffer (Mezhyrich fauna) |
| S15 | Mộ Sungir (Nga, ~34.000 năm trước): thắt lưng đính hơn 250 răng nanh cáo Bắc Cực; hàng hạt cho thấy quần áo may khít | ✅ | Wikipedia "Sungir"; Trinkaus & Buzhilova |
| S16 | Đổ mồ hôi làm ướt lớp cách nhiệt, nên phải mở bớt áo trước khi nóng | ✅ | FM 3-05.70 ("avoid overheating") |
| S17 | Tranh cãi: xương được săn hay nhặt từ các bãi xương chết tự nhiên | ⚠️ | Soffer; Leiden 2025 |
| S18 | Gió làm mất nhiệt nhanh hơn ở cùng nhiệt độ (wind chill) | ✅ | NWS Wind Chill chart |
| S19 | Làm ấm bàn tay tê bằng nách; da tê không cảm thấy bỏng nên không hơ sát lửa | ✅ | Mayo Clinic |
| S21 | Voi có khứu giác rất tốt và thị lực kém; voi ma mút được suy ra từ voi | ✅ / ⚠️ | Tài liệu về hành vi voi |
| S22, S24 | Voi bảo vệ con non ở giữa đàn, đàn do con cái đầu đàn dẫn; voi ma mút suy ra từ voi | ⚠️ | Tài liệu về hành vi voi |
| S23 | Voi ma mút tai nhỏ, lông ngoài thô dài và lớp lông tơ dày; có xác đông lạnh ở Siberia | ✅ | Các xác Yuka, Lyuba; Wikipedia "Woolly mammoth" |
| S26 | Voi tấn công thật thường cuộn vòi vào trong và ngẩng đầu | ✅ (voi) / ⚠️ (voi ma mút) | Tài liệu hành vi voi (mock charge vs. real charge) |
| S27–29 | Khi thú lớn lao tới: chạy tới vật cản lớn, đừng chạy ngoài bãi trống; mặt băng làm thú nặng mất bám | ✅ (nguyên lý) | voice-bible §7; §11 quy tắc 27–28 |
| S31 | Voi hay tấn công dọa (mock charge) rồi dừng hoặc quay đầu | ✅ (voi) | Tài liệu hành vi voi |
| S33 | Run tay sau sợ hãi là do adrenaline | ✅ | Kiến thức sinh lý cơ bản |
| S36 | Xương ống bị đập lấy tủy ở các di chỉ đồ đá cũ muộn; tủy gần như toàn mỡ | ✅ | Tài liệu zooarchaeology về tủy xương |
| S38–39 | Kim xương có lỗ: sớm nhất ~40.000 cal BP ở Siberia, ~26.000 ở châu Âu; dùi xương có trước ~80.000 năm; kim còn dùng để đính hạt | ✅ | d'Errico et al. 2018; Science Advances 2024 |
| S40 | Đồ trang sức hổ phách và vỏ ốc hóa thạch được mang tới từ khoảng 350–500 km; vỏ ốc Biển Đen cho thấy trao đổi giữa các nhóm Mezhyrichian, Mezinian và Yudinovian | ✅ | Wikipedia "Mezhyrich"; donsmaps |
| S41–43 | Sọ voi ma mút ở cửa (porch) vẽ chấm và vạch bằng ochre đỏ; mặt trên có vết lõm; xương ống gần đó hư hại khớp với vết lõm. Gọi là "trống" thì còn tranh cãi | ✅ / ⚠️ | Wikipedia "Mezhyrich"; Bibikov (Mezin) |
| S44 | Eliseevichi-1 (~17.000 BP, phía bắc): Sablin & Khlopachev gọi các sọ là "chó Kỷ Băng Hà", nghiên cứu hình thái 3D cho là sói | ⚠️ | Sablin & Khlopachev 2002; Drake et al. 2015 |
| S48 | Nhiệt độ trung bình năm ở Ukraine thời LGM khoảng −6°C, đất đóng băng vĩnh cửu liên tục. Không có số tháng 1 nên thoại **không nói con số nhiệt độ** | ✅ | Tái dựng cổ khí hậu LGM Đông Âu |

**Không dùng:** số calo, nhiệt độ chính xác, "phổi đóng băng", hoại tử trong vài phút, "8.000 calo", tai voi ma mút xòe, giáo chặn voi bằng sức người.

## 4. Outline 7 hồi (đồng hồ 24 giờ)

| Hồi | Giờ | Clip | Thời lượng | Áp lực cơ thể | Nội dung |
|---|---|---|---|---|---|
| 1 Hook | 0–1 | S01–S03 | 0:30 | Sốc lạnh | Ngà voi ma mút lướt qua ống kính, mở ra trại xương. Nora nói rõ nơi, năm, thử thách 24 giờ. Torak cảnh giác ra hiệu đứng yên |
| 2 Đời thường | 1–8 | S04–S19 | 2:40 | Tê tay → run → đói | Nora được tôn trọng nhờ xử lý frostnip trên má Torak. Găng buộc dây; cấu trúc dwelling và tranh cãi về chức năng; bếp đốt xương; không ăn tuyết; đun nước bằng đá nóng; ăn mỡ (máy dựng); hố trữ trong đất đóng băng; da cáo; thắt lưng Sungir; mồ hôi; tranh cãi săn hay nhặt xương; gió nổi; làm ấm tay |
| 3 Quyền lực | 9–12 | S20–S26 | 1:10 | Mệt, tê ngón chân | Torak báo có đàn. Đi theo vết chân, đứng cuối gió. **Reveal #1** (quay gáy): đàn voi ma mút dưới thung lũng. Tai nhỏ; con cái đầu đàn thử gió; Nora liều tới gần; con mẹ phát hiện |
| 4 Cao trào | 12–14 | S27–S34 | 1:06 | Adrenaline | Voi cái lao tới. Nora lội tuyết ngang gối tới bờ sông dốc. Chân trước của voi trượt trên viền băng, nó chao sang bên rồi bỏ đi. Torak kéo Nora lên. Run tay vì adrenaline; Torak đã chọn bờ sông này |
| 5 Hạ nhịp | 15–16 | S35–S37 | 0:30 | Run, cười được | Vào dwelling ban đêm; Alva đập xương lấy tủy cho Nora; được chỗ ngồi gần tường cạnh lửa |
| 6 Di sản | 17–22 | S38–S46 | 1:30 | Kiệt sức, lạnh về đêm | Kim xương có lỗ, thử nhìn tận tay; hổ phách và vỏ ốc. **Reveal #2:** sọ vẽ ở cửa, "trống" gây tranh cãi, ochre dính ngón tay. Mắt sói ngoài bãi xương. **Reveal #3:** toàn cảnh trại ban đêm. Nora chọn vào trong thay vì quay thêm |
| 7 Kết | 23–24 | S47–S48 | 0:20 | Tĩnh, kiệt | Máy dựng cố định: mọi người ngủ; rồi bình minh ở cửa. Không có câu đạo lý |

Tỉ lệ shot: selfie 30 (63%) · POV 9 (19%) · sau gáy 3 (6%) · máy dựng 4 (8%) · toàn cảnh từ chỗ đứng 2 (4%). Không drone.
Khuôn kiến thức: A ~45% · B ~33% · C ~22%. Bíp 3 lần (S18, S27, S44).

## 5. Storyboard

Ref là danh sách `character_names`, tối đa 3 và luôn có Nora. Viết tắt: N = Nora, T = Torak, A = Alva, CAMP = Mezhyrich Camp, INT = Bone Dwelling Interior, STEP = Mammoth Steppe, MAM = Woolly Mammoth, SKULL = Painted Mammoth Skull. Cột "Từ" là số từ của câu thoại. Chuyển cảnh theo §7c: selfie chỉ dùng whip pan, jump cut hoặc look-away; foreground wipe chỉ dùng ở shot POV.

### Hồi 1 — Hook (Giờ 0–1, vừa sáng)

| # | Dur | Shot | Ref | Hành động | Thoại (Nora) | Từ | Vào | Ra | Khung cuối |
|---|---|---|---|---|---|---|---|---|---|
| S01 | 10 | POV | N,T,CAMP | Torak và một thợ săn khiêng một chiếc ngà cong sát ống kính, trái sang phải; ngà rời khung để lộ 4 dwelling xương trên thềm tuyết. Đến giây 8–10 máy lia nhanh sang phải | (khàn, thì thầm nhanh) "Hour one. Central Ukraine, roughly eighteen thousand years ago, coldest stretch of the Ice Age. I've dug at this site. It never looked like this." | 25 | Ngà che kín khung ở giây 0 | Whip pan phải, nhòe | Nhòe chuyển động sang phải |
| S02 | 10 | Selfie | N,CAMP | Mở giữa cú lia rồi dừng trên mặt Nora ở mép thềm, gió thổi tuyết, trại ở sau | (nhanh, hơi thở thành khói, nửa cười) "Twenty-four hours, no tent, no gear, only what they use. These people got through the harshest phase of the Ice Age living around domes of mammoth bone." | 27 | Nhòe lia → dừng | Look-away: cô quay đầu nhìn về trại | Sau gáy, đuôi ngựa kín nửa khung |
| S03 | 10 | Sau gáy → selfie | N,T,CAMP | Mở trên sau gáy; Nora quay lại phía máy. Torak đã đứng sẵn cách ~6 m bên phải, giáo chúc xuống, tay xòe úp ra hiệu dừng | (thì thầm nhanh) "Okay, that's Torak. My name for him. Hand flat, palm down, probably means stay. I stay. A stranger walking into a winter camp? I'd spear me too." | 26 | Sau gáy | Jump cut | Nora đứng yên, Torak nhìn chằm chằm |

### Hồi 2 — Đời thường (Giờ 1–8, ban ngày)

| # | Dur | Shot | Ref | Hành động | Thoại (Nora) | Từ | Khuôn | Vào → Ra |
|---|---|---|---|---|---|---|---|---|
| S04 | 10 | Selfie | N,T,CAMP | Torak đứng gần sau vai Nora; trên gò má trái anh có một mảng da trắng sáp. Nora chỉ vào má mình rồi chỉ sang anh | (thì thầm nhanh) "No, wait— see that white patch on his cheek? Frostnip. Skin's starting to freeze and he can't feel it. Nobody can see their own face out here." | 27 | A | Jump cut → D: cô cúi về phía máy, đưa tay qua ống kính |
| S05 | 10 | POV | N,T,CAMP | Một bàn tay trần của Nora (găng treo ở dây cổ tay) áp nhẹ lên má Torak, giữ yên. Anh nhìn xuống rồi gật chậm | (nhanh, tập trung) "Don't rub it. Rubbing frozen skin just tears it. Warm hand, steady pressure, wait. Field medics still teach exactly this. Okay... he's letting me." | 24 | A | Tay vào khung từ dưới → POV wipe: Torak bước ngang qua ống kính sang phải |
| S06 | 10 | Selfie | N,A,CAMP | Alva đứng cạnh Nora, kéo thử dây găng ở cổ tay cô hai lần rồi gật đầu | (nửa cười, nhanh) "Hour two. Alva just checked my mitten cord, twice. Fair. Mittens beat gloves, fingers share heat. And drop one in this wind, it's gone." | 24 | C | Jump cut → whip pan trái |
| S07 | 10 | Selfie | N,CAMP | Nora đi chậm dọc chân một dwelling; hàm dưới voi ma mút xếp zigzag ở bên trái khung, khói mỏng bốc từ đỉnh | (nhanh, phấn khích nghề) "Lower jaws, stacked in that zigzag. I've walked around the museum reconstruction maybe fifty times. Never once with smoke coming out the top. Okay, okay, focus." | 26 | B | Mở giữa cú lia trái → jump cut |
| S08 | 10 | Selfie → sau gáy | N,CAMP | Đứng trước cửa dwelling có ngà cong làm vòm. Đến giây 8.5 cô quay đầu nhìn vào cửa | (thấp giọng) "Real talk, we still argue what these were. Homes, food stores, maybe monuments. Newer dating says people weren't here long. Someone's clearly sleeping in this one." | 26 | B | Jump cut → walk-through: cô cúi qua tấm da ở cửa, khung tối |
| S09 | 10 | Selfie | N,A,INT | Trong dwelling. Mở từ tối ra ánh lửa. Alva đặt một đầu xương nhiều mỡ vào bếp, lửa liếm lên | (nhanh, tay xoa lại với nhau) "Hardly any trees out here, so Alva burns bone. The greasy ends, mostly. We find barely any charcoal in these hearths. That's why, probably." | 24 | C | Từ tối → D: cô với tay về phía ống kính |
| S10 | 10 | POV | N,A,INT | Bàn tay trần của Nora vốc tuyết đưa lên miệng; tay Alva giữ cổ tay cô lại, lắc đầu | (giọng sau máy, cười khô) "Yeah, I know, I know. Don't eat snow, ever. Your body burns its own heat just melting it. I was testing her. Mostly." | 23 | A | Tay vào từ dưới → hơi bốc từ túi nước phủ ống kính |
| S11 | 10 | Selfie | N,A,INT | Túi nước bằng da treo trên giá ba chân bằng xương; Alva dùng que xương gắp đá nóng thả vào, nước sủi bọt quanh viên đá, hơi nước bốc lên dần | (nhanh, tay bận) "Hot stone into a hide bag. Hide can't sit on a flame, it burns. We dig up heat-cracked rock at sites like this. Probably from exactly this." | 28 | A | Hơi nước tan → jump cut |
| S12 | 10 | Máy dựng | N,A,INT | Máy dựng trên gờ xương, nhìn Nora ngồi ăn bên lửa. Alva đưa cô một miếng mỡ trắng cùng một miếng thịt | (vừa nhai vừa nói nhanh) "Every bite of meat, she hands me a lump of fat. Lean meat alone in this cold makes you sick. The fat's the actual fuel. Tastes like candle." | 27 | A | Tĩnh → cắt thẳng |
| S13 | 10 | Selfie | N,T,CAMP | Ngoài trời, cạnh dwelling. Sau lưng Nora, Torak quỳ cạnh một hố nông có tấm da phủ, lật tấm da lên thấy những tảng thịt đông bên trong | (nhanh, hào hứng) "Hour four. These pits ring every hut. We dig them out full of bone. Ground's frozen year-round here, so most of us think: freezers. And... yep. Meat." | 27 | C | Jump cut → whip pan phải |
| S14 | 10 | Selfie | N,T,CAMP | Torak căng mấy tấm da cáo Bắc Cực trắng, còn nguyên đuôi, lên khung xương ở sau Nora | (nhanh, khô) "Fox pelts, tails still on. We find tons of fox bones at this site and wondered why. Not dinner. Coats. Maybe also dinner." | 23 | C/B | Mở giữa cú lia → jump cut |
| S15 | 10 | Selfie | N,A,CAMP | Alva chỉ vào thắt lưng răng cáo của Nora, chạm thử một chiếc răng rồi gật đầu, cười nhẹ | (nửa cười, tự hào) "She likes my belt. Fox canines, drilled and sewn on. Copied from a burial at Sungir, way north of here, over two hundred teeth. Nailed it, apparently." | 27 | B | Jump cut → jump cut |
| S16 | 10 | Selfie | N,T,STEP | Nora và Torak kéo một xương ống dài trên tuyết. Nora dừng lại, nới dây cổ áo parka; Torak đã nới cổ áo từ trước | (thở gấp, nhanh) "Hour six. Hauling bone makes me sweat, and damp fur stops insulating. So I open up before I'm hot, not after. Torak's already done it." | 25 | A | Jump cut → jump cut |
| S17 | 10 | Selfie | N,T,STEP | Trong một khe trên thảo nguyên, Torak rút một chiếc ngà phong hóa từ đống xương cũ nằm nửa trong tuyết | (nhanh, thở ra khói) "Big debate in my field: did they hunt all these mammoths, or collect bones from old natural piles? This one's been dead for years. So today, collecting." | 27 | B | Jump cut → jump cut |
| S18 | 10 | Selfie | N,T,STEP | Gió mạnh dần, tuyết bị thổi rạp sát mặt đất bay ngang khung. Nora nheo mắt; Torak đã quay lưng đi về phía trại | (hét qua gió, nhanh) "Wind's picking up— sh— that's the real killer, not the temperature. Same cold, twice the wind, you lose heat way faster. Torak's already heading in." | 25 | A | Jump cut → tuyết thổi phủ kín ống kính. `bleep_at` ~1.4s |
| S19 | 10 | Selfie | N,A,INT | Trong dwelling. Nora phủi tuyết, kẹp hai bàn tay vào nách; Alva ở sau cũng đang làm vậy | (run cầm cập, nhanh) "Hour eight. Warm hands in your armpits, not over the fire. Numb skin can't feel a burn. Alva's doing the same thing, so I'm in good company." | 27 | A | Tuyết tan khỏi ống kính → cắt thẳng |

### Hồi 3 — Quyền lực (Giờ 9–12, chiều, nắng xiên)

| # | Dur | Shot | Ref | Hành động | Thoại (Nora) | Từ | Khuôn | Vào → Ra |
|---|---|---|---|---|---|---|---|---|
| S20 | 10 | Selfie | N,T,CAMP | Torak đi từ mép thềm về phía Nora, vung một cánh tay thấp như cái vòi, chỉ về thung lũng, rồi ra hiệu cho cô đi theo | (thì thầm nhanh) "Hour nine. Torak's back from the ridge, arm swinging low like a trunk. Herd. And he wants me along. Not sure if that's trust or bait." | 26 | C | Jump cut → jump cut |
| S21 | 10 | Selfie | N,T,STEP | Nora bước vào đúng vết chân Torak trên tuyết; anh đi trước cách ~3 m, quay lưng | (thở gấp, thấp giọng) "Walk in his tracks. Saves energy, and he knows where the crust holds. We stay downwind too. Mammoths probably smell like elephants do: way better than they see." | 28 | C | Jump cut → look-away: cô quay đầu nhìn qua đỉnh gò |
| S22 | 10 | Sau gáy (Reveal #1) | N,MAM,STEP | Mở trên sau gáy Nora ở bên trái khung. Bên phải, đàn voi ma mút **đã có sẵn từ giây 0** dưới thung lũng xa. Cô hạ thấp người và nhích sang trái, để lộ cả đàn | (thì thầm, nín thở) "Oh. Oh, there they are. Eight, nine... calves in the middle. That's textbook elephant behaviour. I did not expect textbook to be this big." | 24 | B | Sau gáy → selfie flip sang POV |
| S23 | 10 | Toàn cảnh từ chỗ đứng | N,MAM,STEP | Máy cầm tay lia chậm qua đàn voi ở khoảng cách vừa; voi cúi ủi tuyết tìm cỏ | (giọng sau máy, thì thầm nhanh) "Small ears, see? Big ears dump heat, they'd freeze. Shaggy outer hair, dense wool underneath. We have frozen carcasses from Siberia with ears this size." | 25 | B | Mở giữa cú xoay máy → jump cut |
| S24 | 10 | Selfie | N,T,MAM | Nora nằm sấp sau một gờ tuyết, Torak ở sau ra hiệu "nằm thấp". Xa phía sau, con voi cái lớn nhất giơ vòi lên đánh hơi | (thì thầm rất nhanh) "Torak's hand says stay low, and I'm staying low. No, wait— lead female, probably, trunk up, sniffing. She's testing the wind. Is our wind still good?" | 26 | C | Jump cut → jump cut |
| S25 | 10 | Selfie | N,T,MAM | Nora bò về phía trước; Torak lắc đầu, đưa tay giữ lại; cô vẫn đi tiếp | (thì thầm, liều) "Real talk, I need a closer shot. Fifty metres, max. He's shaking his head. I know. I know. Ten more steps and I'm done." | 25 | — | Jump cut → D: cô quay máy về phía đàn voi |
| S26 | 10 | POV | N,MAM,STEP | POV thấp sát tuyết, một bàn tay trần đè lên lớp vỏ tuyết. Con non đi lạc về phía máy; con mẹ quay đầu nhìn thẳng về phía máy, ngẩng đầu, cuộn vòi vào | (thì thầm, nhanh dần) "Calf's wandering this way. Mum's watching it. Mum's watching me now. Okay... head up, trunk tucked, that's the posture. That's the posture before—" | 23 | B | Tay vào từ dưới → cắt khi con mẹ dồn trọng tâm lao tới |

### Hồi 4 — Cao trào (Giờ 12–14, hoàng hôn)

| # | Dur | Shot | Ref | Hành động | Thoại (Nora) | Từ | Khuôn | Vào → Ra |
|---|---|---|---|---|---|---|---|---|
| S27 | 8 | Selfie chạy | N,MAM,STEP | Nora chạy về phía trước, vừa chạy vừa ngoái nhìn qua vai, nắm chặt máy hướng vào mặt. Xa phía sau, voi cái chạy nặng nề tới, tuyết bắn tung; nó to lên chậm | (chạy, giọng vỡ) "She's charging— sh— don't run straight, she's way faster than me. Riverbank. Get something big between us. Go, go!" | 19 | A | Cắt thẳng → whip pan xuống. `bleep_at` ~1.2s |
| S28 | 6 | POV | N,T,STEP | POV lội tuyết ngang gối, máy nảy theo từng bước nặng; phía trước là mép bờ sông, Torak đứng trên đó vẫy | (thở hổn hển) "Knee-deep, I can't run, just big heavy steps. The bank's right there, Torak's waving. Go." | 15 | A | Mở giữa cú lia → máy chúi xuống khi cô trượt qua mép bờ |
| S29 | 8 | Selfie | N,MAM,STEP | Nora trượt xuống bờ sông dốc rồi áp lưng vào vách; phía trên đầu cô là viền băng bóng ở mép bờ. Đầu và vai con voi hiện dần trên mép bờ khi nó tới gần | (thì thầm hổn hển) "Down, down, down. Steep bank, glazed ice on the lip. Something that heavy can't get footing on that. Probably. Please, probably." | 21 | A | Máy chúi → cắt thẳng |
| S30 | 6 | Selfie góc thấp | N,MAM,STEP | Máy chĩa lên qua mặt Nora về phía mép bờ. Hai chân trước của voi cái đạp lên viền băng và mất bám; thân nó chao sang bên, nó hất đầu, xoay người và quay đi; tuyết và mảnh băng rơi xuống | (thì thầm, hoảng) "Oh no no no— she's slipping, she's slipping— she's turning. She's turning away!" | 13 | — | Cắt thẳng → cắt thẳng |
| S31 | 8 | POV | N,MAM,STEP | POV nhìn qua mép bờ: voi cái chạy nước kiệu nặng nề về phía đàn, xa dần và nhỏ dần, tuyết bắn sau chân | (thở ra run run) "Going back to her calf. Warning charge, probably, not a kill. Elephants do that. Didn't feel like a warning." | 19 | A | Cắt thẳng → tay Torak thò xuống qua ống kính |
| S32 | 10 | Selfie | N,T,STEP | Tay Torak nắm cẳng tay trái của Nora kéo cô lên bờ; tay phải cô vẫn giữ máy hướng vào mặt. Anh đang cười | (cười run, nhanh) "Okay, okay. Hand, yes, thank you. He's... laughing at me. Fair. I just did everything I tell my students never to do." | 22 | — | Tay qua ống kính → jump cut |
| S33 | 10 | Selfie | N,T,STEP | Nora ngồi trên tuyết ở mép bờ, hai tay run; Torak ngồi xổm bên cạnh, đưa cho cô một miếng mỡ | (run, chậm dần) "Hour thirteen. Hands won't stop shaking. That's adrenaline dumping, not cold. Eat something, sit, breathe slow. Torak's handing me fat. Of course he is." | 24 | A | Jump cut → look-away: cô quay nhìn về phía thung lũng |
| S34 | 10 | Sau gáy → selfie | N,MAM,STEP | Mở trên sau gáy: dưới mép bờ có rãnh trượt trên viền băng; đàn voi đi xa dưới ánh hoàng hôn. Nora quay lại phía máy | (thấp giọng, đã bình tĩnh) "Watch the snow by the bank. Front feet slid, she twisted, she bailed. Ice turned her, not me. Torak picked this bank on purpose." | 24 | C | Sau gáy → time-skip: trời tối |

### Hồi 5 — Hạ nhịp (Giờ 15–16, đêm, trong dwelling)

| # | Dur | Shot | Ref | Hành động | Thoại (Nora) | Từ | Khuôn | Vào → Ra |
|---|---|---|---|---|---|---|---|---|
| S35 | 10 | Selfie | N,A,INT | Mở từ tối khi Nora cúi qua tấm da ở cửa vào trong dwelling. Alva ngồi bên lửa, đập một xương ống trên tảng đá đe | (mệt, ấm áp) "Hour fifteen. Alva heard. Everyone heard. She's cracking a leg bone for me, which I'm choosing to read as 'welcome to the family'." | 23 | — | Walk-through tối → D: cô với về phía khúc xương |
| S36 | 10 | POV | N,A,INT | Alva cầm khúc xương đã tách đôi; bàn tay trần của Nora dùng một que xương dẹt múc tủy | (vừa ăn vừa nói nhanh) "Marrow. Basically pure fat. We find long bones smashed open at sites like this. That exact break, right through the shaft. And now I'm eating it." | 26 | A | Tay vào từ dưới → cắt thẳng |
| S37 | 10 | Máy dựng | N,A,INT | Máy dựng trên gờ xương. Alva vỗ lên tấm da ở chỗ sát tường bên lửa; Nora ngồi xuống đó | (khẽ, cười) "Alva's giving me a spot by the fire now. Near the wall, not the door. I know what that means. I'm not crying, it's the smoke." | 26 | — | Tĩnh → cắt thẳng |

### Hồi 6 — Di sản (Giờ 17–22, đêm)

| # | Dur | Shot | Ref | Hành động | Thoại (Nora) | Từ | Khuôn | Vào → Ra |
|---|---|---|---|---|---|---|---|---|
| S38 | 10 | Selfie | N,A,INT | Alva khâu một tấm da cáo bằng kim xương, không cần nhìn tay; Nora ghé sát | (thì thầm, gần như nghẹn) "Hour seventeen. An eyed bone needle. I've catalogued broken ones in museum drawers for years, never seen one used. She's stitching without looking. Sorry. Archaeologist." | 25 | B | Jump cut → D: cô đưa tay giữ mép da |
| S39 | 10 | POV | N,A,INT | Một bàn tay trần của Nora giữ mép da; Alva đâm kim qua, da hơi võng quanh mũi kim, sợi gân kéo căng | (nhanh, thì thầm) "Hide flexes, sinew pulls tight. Awls only punch holes. The eye means finer seams, fitted sleeves, no gaps for wind. Also beads. Lots of beads." | 26 | B | Tay vào từ dưới → POV wipe: Alva nâng tấm da che ống kính |
| S40 | 10 | Selfie | N,A,INT | Alva cho Nora xem chuỗi hạt ở cổ: hổ phách vàng mật và vỏ ốc hóa thạch | (phấn khích, nhanh) "Amber and fossil shells, carried here from three to five hundred kilometres away. Some from the Black Sea side. So: neighbours, trading, long before farming." | 25 | B | Tấm da rời khung → walk-through ra ngoài |
| S41 | 10 | Selfie (Reveal #2) | N,SKULL,CAMP | Ngoài trời ban đêm. Ở cửa dwelling lớn nhất, sọ voi vẽ ochre đỏ **đã ở sẵn từ giây 0** bên phải đầu Nora, được ánh lửa chiếu | (thì thầm, run vì phấn khích) "Hour nineteen. That skull by the entrance. Red ochre, dots and lines. It's in the excavation records. I'm about to see it in use. Okay, okay, breathe." | 27 | B | Từ tối → jump cut |
| S42 | 10 | Selfie | N,T,SKULL | Torak gõ lên đỉnh sọ bằng một xương ống dài, tiếng gõ trầm và rỗng; Nora ở bên trái khung | (gần như hét, nhanh) "Calling this a drum is controversial. The top has worn dents, and the long bones near it are damaged to match. Sounds like a drum to me." | 26 | B | Jump cut → D |
| S43 | 10 | POV | N,SKULL | Bàn tay trần của Nora chạm vào các chấm ochre trên sọ rồi nhấc ra; đầu ngón tay dính màu đỏ | (thì thầm) "Ochre. Iron-rich earth, ground up. It's still on my fingertips. Eighteen thousand years in the ground and the red survives. That's how we found it." | 25 | B | Tay vào từ dưới → POV wipe: Torak đi ngang qua ống kính |
| S44 | 10 | Selfie | N,CAMP | Ở mép trại. Sau lưng Nora, ngoài đống xương, có những cặp mắt phản ánh lửa **đã ở sẵn từ giây 0** | (thì thầm, giật mình) "Hour twenty-one. Holy cr— eyes past the bone pile. Wolves, after scraps. Up north we argue whether skulls like theirs were early dogs. From here? Wolves." | 25 | B | Jump cut → selfie flip sang POV. `bleep_at` ~1.6s |
| S45 | 10 | Toàn cảnh từ chỗ đứng (Reveal #3) | N,CAMP | Từ mép thềm cao, máy lia chậm qua cả 4 dwelling có ánh lửa và khói, sông đóng băng ở dưới, ánh trăng nhạt trên tuyết | (giọng sau máy, khẽ) "Four dwellings, hearths going, the river frozen below. On the dig it's a pit with string lines and numbered bags. This is what the string lines meant." | 27 | B | Mở giữa cú xoay máy → whip pan về Nora |
| S46 | 10 | Selfie | N,CAMP | Nora ở mép thềm, trại có ánh lửa ở sau, môi tái, mắt nặng trĩu | (mệt, chậm hơn) "Hour twenty-two. Toes are numb again, so I'm going in. Alva left a gap by the fire for me. I'm not wasting it on a better shot." | 27 | — | Mở giữa cú lia → walk-through vào trong |

### Hồi 7 — Kết (Giờ 23–24)

| # | Dur | Shot | Ref | Hành động | Thoại (Nora) | Từ | Vào → Ra |
|---|---|---|---|---|---|---|---|
| S47 | 10 | Máy dựng | N,A,INT | Máy dựng trên gờ xương. Nora ngồi quấn da lông bên than hồng; Alva ngủ ở phía sau | (thì thầm) "Hour twenty-three. Everyone's asleep. I've spent ten years measuring this floor in centimetres. Never thought about how warm it was. It is. Barely." | 23 | Tĩnh → time-skip sang bình minh |
| S48 | 10 | Máy dựng | N,CAMP | Máy dựng ở cửa dwelling. Nora ngồi trên một xương voi ma mút; thảo nguyên lúc trời vừa sáng ở phía sau | (khẽ, mệt, cười nhẹ) "Hour twenty-four. First light. My hands work, my toes probably work. They do this every single winter. I did one day. One." | 22 | Tĩnh → hết |

## 5b. Bảng vật lý từng clip — CHỜ USER DUYỆT

Quy ước áp dụng cho mọi clip:

- **Selfie:** máy cầm ở tầm tay, tay phải duỗi về góc dưới bên phải, góc nhìn tự nhiên của smartphone, không méo fisheye.
- **POV:** chỉ có một bàn tay trần, không cầm gì.
- **Chạy:** cô nắm chặt máy hướng vào mặt, máy nảy dọc theo từng bước chân.
- **Mặt đất:** đứng yên tuyệt đối, không trôi.
- **Hơi thở:** khói hơi thở ngắn và tan nhanh.

| # | Máy đặt ở đâu, nhìn về đâu | Giây 0 có gì trong khung | Vật di chuyển: hướng, tốc độ, hệ quả trong khung | Vật lý thật | Ai hoặc cái gì rời khung, bằng cách nào |
|---|---|---|---|---|---|
| S01 | Tầm mắt Nora trên thềm, nhìn về trại phía trước | Ngà cong che ~80% khung ngay sát ống kính; 4 dwelling ở sau, đã có sẵn | Hai thợ săn khiêng ngà đi trái sang phải với tốc độ đi bộ, lộ dần trại. Giây 8–10 máy lia nhanh sang phải | Ngà nặng: hai người cúi người, bước ngắn, ngà nhún theo nhịp bước. Tuyết dưới chân bị nén lún | Ngà và người khiêng ra mép phải. Khung kết bằng nhòe lia |
| S02 | Selfie trên mép thềm, máy nhìn về Nora, sau lưng cô là trại | Mở giữa vệt nhòe đang dừng lại; mặt Nora bên trái 1/3 khung, trại bên phải | Gió đông thổi tuyết bột ngang khung từ phải sang trái. Nora đứng yên | Đuôi ngựa và lông viền mũ trễ theo gió | Không ai rời khung. Giây 9 cô quay đầu, sau gáy che nửa khung |
| S03 | Sau gáy Nora, sau đó cô quay lại phía máy | Sau gáy che nửa trái; Torak đứng sẵn bên phải cách ~6 m | Torak bước chậm 2 bước tới gần, giáo chúc xuống, tay xòe úp đưa ra; dừng ở ~4 m | Tuyết lún dưới ủng anh, áo lông nặng nề | Không ai rời khung |
| S04 | Selfie, Torak sau vai phải Nora | Mặt Nora; Torak có mảng trắng trên má trái | Nora chỉ vào má mình rồi chỉ ra sau. Torak đứng yên, nhíu mày | — | Giây 9 cô cúi về phía máy, tay đưa ngang qua ống kính |
| S05 | POV tầm mắt Nora, nhìn mặt Torak cách ~0.6 m | Mặt Torak có mảng trắng; tay Nora vào từ dưới | Tay trần áp lên má anh trong ~5s, giữ yên; găng đung đưa ở dây cổ tay | Da má hơi lún dưới lòng bàn tay; găng lắc theo quán tính | Giây 9 Torak bước ngang qua ống kính sang phải (POV wipe) |
| S06 | Selfie ở khoảng trống giữa trại, Alva đứng bên phải Nora | Hai người, dây găng thấy rõ ở cổ tay trái Nora | Alva kéo dây hai lần; cổ tay Nora bị giật nhẹ theo | Dây căng rồi chùng | Cắt thẳng (jump cut), sau đó whip pan sang trái |
| S07 | Selfie, Nora đi lùi chậm dọc chân dwelling | Tường hàm dưới xếp zigzag bên trái khung | Nora đi lùi ~0.5 m/s, dwelling trượt chậm qua khung; khói bốc thẳng rồi bị gió bẻ | Dwelling đứng yên tuyệt đối | Cắt thẳng (jump cut) |
| S08 | Selfie trước cửa có vòm ngà | Vòm ngà bên phải, mặt Nora bên trái | Giây 8.5 Nora quay đầu nhìn vào cửa | Tấm da cửa lay nhẹ theo gió | Sau gáy che khung; cô cúi bước qua tấm da, khung tối dần |
| S09 | Selfie trong dwelling, bếp lửa ở giữa sau Nora | Khung tối sáng dần lên ánh lửa; Alva ngồi bên bếp | Alva đặt đầu xương vào lửa; lửa bén lên chậm, khói bốc lên lỗ mái | Mỡ xương xèo nhỏ; lửa liếm lên dần, không bùng | Giây 9 Nora với tay về phía máy |
| S10 | POV tầm mắt Nora ngồi trong dwelling | Một bàn tay trần đang vốc tuyết ở dưới khung | Tay đưa tuyết lên về phía ống kính; tay Alva vào từ trái nắm cổ tay dừng lại | Tuyết rơi lả tả khỏi lòng bàn tay | Giây 9 hơi nước từ túi da trôi phủ ống kính |
| S11 | Selfie, túi da treo trên giá xương ở sau vai trái Nora | Túi da, bếp, Alva cầm que xương gắp đá nóng | Viên đá đỏ được thả vào túi; nước sủi bọt quanh viên đá; hơi bốc lên tăng dần | Không sôi bùng; túi da võng xuống theo sức nặng viên đá | Cắt thẳng (jump cut) |
| S12 | Máy dựng trên gờ xương cao ~0.5 m, nhìn ngang vào Nora | Nora ngồi bên lửa, Alva bên phải | Alva đưa mỡ; Nora nhai. Máy đứng yên tuyệt đối | Mỡ mềm nhũn khi cầm | Không ai rời khung |
| S13 | Selfie ngoài trời, hố có da phủ sau vai trái Nora | Torak quỳ cạnh hố, tay đặt trên tấm da phủ | Torak lật tấm da lên từ trái sang phải; lộ thịt đông có sẵn trong hố | Tấm da cứng vì lạnh, gãy góc; tuyết trên tấm da rơi xuống | Cắt thẳng (jump cut), sau đó whip pan sang phải |
| S14 | Selfie, khung căng da cáo ở sau | Mở giữa vệt nhòe, Torak đang căng da | Torak kéo dây gân căng da; đuôi cáo đung đưa | Da cáo căng ra, lông lay theo gió | Cắt thẳng (jump cut) |
| S15 | Selfie, Alva đứng bên phải Nora | Thắt lưng răng cáo thấy được ở mép dưới khung | Alva cúi chạm một chiếc răng, rồi đứng thẳng lên | Các răng va nhẹ vào nhau | Cắt thẳng (jump cut) |
| S16 | Selfie, Nora đi ngang sang trái kéo xương | Nora và Torak cùng kéo một xương ống dài trên tuyết | Đi ngang sang trái rất chậm; xương để lại rãnh trên tuyết | Xương nặng: người ngả về trước, bước ngắn | Cắt thẳng (jump cut) |
| S17 | Selfie trên miệng khe, Torak ở dưới khe sau vai cô | Đống xương phong hóa nằm nửa trong tuyết, có sẵn | Torak giật ngà ra khỏi tuyết bằng hai tay; ngà nhích ra từng chút | Tuyết nứt quanh ngà, mảnh tuyết đá rơi xuống | Cắt thẳng (jump cut) |
| S18 | Selfie trên thảo nguyên, gió từ phải | Tuyết thổi rạp sát mặt đất ngang khung; Torak ở xa sau lưng, quay lưng | Torak đi xa dần về phía trại, nhỏ dần. Gió tăng dần | Nora nheo mắt, nghiêng người tì vào gió | Giây 9 một luồng tuyết phủ kín ống kính |
| S19 | Selfie trong dwelling | Khung trắng vì tuyết, tan ra để lộ Nora | Nora phủi tuyết khỏi mũ trùm, kẹp tay vào nách | Tuyết rơi khỏi lông mũ | Cắt thẳng |
| S20 | Selfie trên thềm, mép thềm ở sau | Torak đã ở trên mép thềm phía sau, đang đi tới | Torak đi tới với tốc độ đi bộ, to dần; vung tay thấp, chỉ về thung lũng | Bước chân lún tuyết | Cắt thẳng (jump cut) |
| S21 | Selfie, Nora đi tới, máy nhìn ngược lại về phía cô | Torak đi trước cô ~3 m, quay lưng | Cả hai đi chậm; ủng Nora đặt đúng vào vết lún của Torak | Lớp vỏ tuyết nứt dưới ủng | Giây 9 cô quay đầu nhìn về phía đỉnh gò |
| S22 | Sau gáy Nora ở bên trái khung, máy nhìn xuống thung lũng | Đàn voi có sẵn ở xa bên phải; sau gáy che nửa trái | Nora hạ người và nhích sang trái; đàn voi đi chậm sang trái rất xa, không lại gần | Thung lũng đứng yên | Giây 9 máy bắt đầu xoay (selfie flip) |
| S23 | Từ chỗ cô đứng trên gờ, máy cầm tay lia chậm từ trái sang phải | Đàn voi ở cự ly vừa, đang cúi kiếm ăn | Voi đi rất chậm, ngà thỉnh thoảng ủi lớp tuyết nông | Lông dài lay chậm theo gió; chân nén tuyết trước khi thân chuyển | Cắt thẳng (jump cut) |
| S24 | Selfie sát mặt tuyết, Nora nằm sau gờ tuyết | Torak nằm bên phải; đàn voi ở xa phía sau | Con cái lớn nhất giơ vòi lên đánh hơi, đứng yên | Vòi cong lên chậm | Cắt thẳng (jump cut) |
| S25 | Selfie, Nora bò về trước, máy nhìn ngược lại về phía cô | Torak ở sau; đàn voi ở xa hơn bên phải | Nora bò ~1 m; Torak lắc đầu, đưa tay ra, không chạm | Khuỷu tay lún tuyết | Giây 9 cô xoay máy về phía đàn voi |
| S26 | POV sát mặt tuyết, nhìn về đàn voi | Con non ở cự ly vừa, con mẹ ở sau nó | Con non đi chậm về phía máy; con mẹ quay đầu, ngẩng lên, cuộn vòi vào | Lông con mẹ trễ theo cú quay đầu | Cắt ở khung con mẹ dồn trọng tâm về trước |
| S27 | Selfie chạy, máy nhìn ngược lại về phía Nora | Mặt Nora; voi cái ở xa phía sau đang lao tới | Nora chạy về phía trước theo hướng máy, ngoái lại. Voi tới gần chậm, to dần, **không** bắt kịp trong clip | Chạy trong tuyết ngang gối: bước ngắn, nặng, ủng lún sâu. Voi nặng: chân nén tuyết, thân trễ, tuyết bắn tung | Giây 7.5 máy chúi xuống (whip pan xuống) |
| S28 | POV chạy, máy nhìn về trước | Mép bờ sông ở trước ~10 m, Torak đứng trên đó vẫy | Máy tiến chậm với tốc độ lội tuyết | Máy nảy dọc theo từng bước; tuyết đùn thành gờ quanh vết chân | Máy chúi xuống khi cô trượt qua mép bờ |
| S29 | Selfie, Nora trượt xuống rồi áp lưng vào vách bờ, máy chĩa lên | Vách bờ phủ tuyết, viền băng bóng ở mép trên | Nora trượt xuống ~2 m rồi dừng. Đầu voi hiện dần trên mép bờ, tới với tốc độ chạy | Tuyết rơi theo cú trượt | Cắt thẳng |
| S30 | Selfie góc thấp chĩa lên, mép bờ cách ~3 m phía trên | Mặt Nora ở dưới khung, mép bờ có viền băng ở trên | Chân trước voi đạp lên viền băng → mất bám → thân chao sang phải → hất đầu → xoay người, quay đi sang phải | Lệch hướng chứ không dừng phanh. Quán tính lớn: chân trượt trước, thân trễ; mảnh băng và tuyết rơi lả tả | Voi rời mép bờ sang phải |
| S31 | POV từ dưới mép bờ, nhìn lên rồi ra xa | Voi đang chạy xa dần về phía đàn | Voi chạy nước kiệu đi xa, nhỏ dần | Lông dài nảy theo bước chạy | Giây 9 tay Torak thò xuống qua ống kính |
| S32 | Selfie, Nora bị kéo lên bờ | Tay Torak nắm cẳng tay trái Nora | Torak kéo lên; Nora leo lên ~1 m, máy lắc theo | Tay phải cô **không bao giờ** buông máy | Cắt thẳng (jump cut) |
| S33 | Selfie, Nora ngồi trên tuyết ở mép bờ | Torak ngồi xổm bên trái cô | Torak đưa miếng mỡ; tay Nora run | Máy rung nhẹ theo tay run | Giây 9 cô quay đầu nhìn về phía thung lũng |
| S34 | Sau gáy rồi selfie, máy hướng ra thung lũng | Rãnh trượt trên viền băng thấy được; đàn voi ở xa đang đi xa | Đàn đi ra xa và nhỏ dần; mặt trời lặn dần | Ánh sáng chuyển dần từ cam sang xanh | Cắt time-skip |
| S35 | Selfie, Nora cúi qua tấm da ở cửa vào trong | Khung tối; tấm da bị đẩy sang bên | Nora đi vào, ngồi xuống; Alva đập xương | Đập xương: các vết nứt lan ra từ điểm va | Giây 9 cô với tay về phía khúc xương |
| S36 | POV tầm mắt Nora ngồi | Alva cầm xương đã tách đôi; tay Nora cầm que xương | Que múc tủy chậm | Tủy mềm sệt, bám vào que | Cắt thẳng |
| S37 | Máy dựng trên gờ xương | Nora, Alva, bếp lửa | Nora dịch tới chỗ sát tường và ngồi xuống; máy đứng yên | Lửa và khói bốc theo đối lưu | Không ai rời khung |
| S38 | Selfie, Alva khâu ở sau vai phải Nora | Kim xương xuyên trong tấm da cáo | Kim vào ra đều tay | Da võng quanh kim | Giây 9 cô với tay giữ mép da |
| S39 | POV, tay Nora giữ mép da | Một bàn tay trần trên mép da; tay Alva cầm kim | Kim đâm, kéo sợi gân căng | Da võng, sợi gân căng rồi nằm êm | Giây 9 Alva nâng tấm da che kín ống kính |
| S40 | Selfie, Alva đứng bên phải | Mở khi tấm da đang rời khung; chuỗi hạt ở cổ Alva | Alva nâng chuỗi hạt lên tay | Hổ phách bắt ánh lửa | Walk-through: Nora cúi bước ra cửa, khung tối |
| S41 | Selfie ngoài trời, đêm | Sọ vẽ ochre ở cửa, bên phải đầu Nora, có sẵn từ giây 0 | Nora đứng yên, chỉ nghiêng đầu nhìn | Ánh lửa từ cửa lay động trên sọ | Cắt thẳng (jump cut) |
| S42 | Selfie, sọ ở giữa sau lưng | Torak cầm xương ống dài đứng cạnh sọ | Torak gõ 3–4 nhịp lên đỉnh sọ | Xương nảy nhẹ sau mỗi nhịp gõ; sọ đứng yên. Không có màng trống | Giây 9 cô cúi về phía sọ |
| S43 | POV, tay Nora chạm sọ | Chấm ochre ngay trước ống kính; tay vào từ dưới | Ngón tay chạm rồi nhấc ra, đầu ngón dính màu đỏ | Bột ochre khô bám lên vân da | Giây 9 Torak đi ngang qua ống kính (POV wipe) |
| S44 | Selfie mép trại, đống xương sau lưng | Các cặp mắt phản ánh lửa ngoài đống xương, có sẵn | Mắt đứng yên, có khi chớp; một cặp lùi về sau | Đêm tối, lửa là nguồn sáng chính | Giây 9 máy xoay (selfie flip) |
| S45 | Từ mép thềm cao, lia chậm từ trái sang phải | Dwelling đầu tiên ở bên trái; cả 4 đều đã có sẵn | Máy lia chậm; khói bốc thẳng | Trăng chỉ phủ ánh xanh nhạt, lửa là nguồn sáng chính | Whip pan kết vào Nora |
| S46 | Selfie mép thềm, trại ở sau | Mở giữa vệt nhòe, dừng trên Nora | Nora đứng yên, rồi quay người đi về phía cửa | — | Walk-through vào tấm da ở cửa |
| S47 | Máy dựng trên gờ xương trong dwelling | Nora quấn da lông, than hồng; Alva ngủ ở sau | Không có gì di chuyển ngoài than đỏ phập phồng và hơi thở | Máy đứng yên tuyệt đối | Không ai rời khung |
| S48 | Máy dựng ở cửa dwelling, nhìn ra Nora và thảo nguyên | Nora ngồi trên xương; chân trời bắt đầu sáng | Ánh sáng tăng dần; Nora đứng yên | Máy đứng yên tuyệt đối | Hết |

**Câu khóa dán vào mọi `video_prompt`** (chèn tên Nora):

- **Selfie:** `The camera is the phone itself recording from Nora's hand, so the viewer looks directly at Nora; no phone, no phone body, no phone screen, no UI or app overlay, no case, and no selfie stick appear anywhere in the shot.`
- **POV:** `First-person point-of-view shot. Nora is completely behind the camera holding it firmly; only her bare empty hand enters the lower frame. No phone, no device, and no selfie stick appear anywhere in the frame.`
- **Chung:**
  - `Natural smartphone perspective, no exaggerated fisheye distortion.`
  - `Only Nora speaks; the locals communicate only with gestures and never speak.`
  - `No subtitles or text appear on screen.`
  - `This looks like raw unedited amateur video posted online, not a movie or a 3D render.`

---

## 6. Clip JSON — chưa viết

Viết theo từng hồi sau khi user duyệt bảng 5b (§11 quy tắc 21).

## 7. Hậu kỳ (tóm tắt)

- **Bíp:** S18 tại ~1.4s, S27 tại ~1.2s, S44 tại ~1.6s, mỗi chỗ ~0.3s.
- **Âm thanh:** nhạc ambient trải liên tục. J-cut ~0.5s ở mỗi mối nối. SFX "vút" ở các cú whip pan.
- **Chữ:** không có chữ trên màn hình; phụ đề chỉ xuất `.srt` rời.
- **Thứ tự sản xuất:** clip khó nhất làm trước: S30 (voi trượt băng), sau đó S27 và S22.
- Gói YouTube nằm trong `youtube_seo.md`.
