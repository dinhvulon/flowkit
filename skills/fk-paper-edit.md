# fk-paper-edit — Dựng trên giấy: bấm giờ, lời hứa 30s, móc giữ chân, cắt kịch bản trước khi tốn credit Flow

Usage: `/fk-paper-edit <output/<slug>/script.md | .omc/research/<slug>_epNN_script.json …> [--lang vi|en] [--rehook-max 90] [--promise-window 30]`

Skill này kiểm tra kịch bản **trước khi** sinh bất kỳ media nào. Mỗi clip cắt ở bước này tiết kiệm 1 lần sinh video, thường thêm 1 Start Frame, và các lần regen kèm theo.

Phương pháp lấy từ hai skill ngoài, đã chỉnh theo luật FlowKit:

- "Edit on paper first" (khung SCENE, skill `scripting-and-storyboarding`).
- "Click → Hook → AVD" (khung CHAIN, skill `youtube-long-form`).

Phần lịch quay theo bối cảnh, batch-shoot và đăng bài qua WoopSocial của hai skill đó **không áp dụng** cho FlowKit (FlowKit sinh từng clip bằng AI; đăng bằng `/fk-youtube-upload`).

---

## Thứ tự ưu tiên khi mâu thuẫn

1. `CLAUDE.md`: Rule 14 (fact-check), Rule 20 (ngôn ngữ), Rule 29 (hỏi trước khi sinh), Rule 42 (4) (không 2 khối liền nhau cùng cỡ cảnh + góc máy; phần selfie của Rule 42 chỉ áp cho POV vlog), Rule 49 (độ dài clip + số từ), Rule 65 (chuỗi clip liên tục).
2. Skill gọi skill này: `/fk-film` hoặc `/fk-scriptwriter`.
3. Skill này.

## Khi nào chạy

| Luồng | Thời điểm |
|---|---|
| `/fk-film` | Bước 4.5: sau bước 4 (user duyệt storyboard `script.md`), trước bước 5 (`/fk-script-to-prompts`). |
| `/fk-scriptwriter` | Step 5 mục 2: sau khi lưu screenplay JSON, trước Quality Gate 23 điểm. |
| Mọi luồng | Chạy lại sau mỗi lần thêm, bỏ hoặc đổi thứ tự clip. |

Skill này không gọi Flow API và không tốn credit. Rule 29 không áp dụng cho chính skill này.

## Đầu vào

1. **Kịch bản** (một hoặc nhiều file, ghép theo thứ tự truyền vào — dùng cho phim nhiều tập):
   - `script.md` có bảng storyboard với header chứa `Clip` và `Dur` (định dạng storyboard `script.md` của `/fk-film`: `Clip | Dur | Shot | Ref | SF | Sáng | Hình | Thoại | Từ | Việc | Beat | Dựng`), hoặc
   - screenplay JSON của `/fk-scriptwriter` (Section O.1, có mảng `scenes`).
2. **Gói (package):** tiêu đề + ý tưởng thumbnail + lời hứa (1 câu: người xem sẽ thấy gì). Tiêu đề và chữ trên thumbnail theo ngôn ngữ thoại (Rule 20).
   - Vlog: dòng `- **Package:** <tiêu đề> · <thumbnail> · <lời hứa>` ở khối thông tin đầu `script.md`. Tool tự đọc dòng này.
   - Screenplay JSON: field `package`.
   - Không có gói → hỏi user 1 lần. User không trả lời → báo cáo ghi `UNKNOWN — chưa có gói` và bỏ qua Bước 3.

## Luật số từ tool dùng

| Đầu vào | Luật | Dải số từ |
|---|---|---|
| `script.md` (storyboard) | Rule 49 bảng (0) | 4s: 0 hoặc 6–8 · 6s: 12–15 · 8s: 18–22 · 10s: 24–28. Clip 6/8/10s có 0 từ chỉ hợp lệ khi ô thoại/Beat ghi Sonic Isolation, `0 từ` hoặc im lặng (cảnh báo nếu không ghi). |
| Screenplay JSON, clip 8s | `/fk-scriptwriter` Section J | Narrator tiếng Việt 18–22 · tiếng Anh 20–24 · cảnh có thoại (`has_dialogue: true`) 12–16 · hoặc 0. Ngôn ngữ lấy từ `--lang`, hoặc field `language` trong JSON, mặc định `vi`. |
| Screenplay JSON, clip khác 8s | Rule 49 bảng (0) | Như dòng đầu. |

---

## Quy trình

### Bước 1 — Chạy tool

```bash
python tools/paper_edit.py output/<slug>/script.md
# → output/<slug>/paper_edit.md                        (exit 1 nếu có lỗi)

python tools/paper_edit.py .omc/research/<slug>_ep01_script.json
# → .omc/research/<slug>_ep01_script_paper_edit.md

python tools/paper_edit.py ep01.json ep02.json ep03.json --out output/<slug>/paper_edit.md
# → phim ghép nhiều tập: timecode cộng dồn qua các tập
```

Tool tính và ghi vào báo cáo:

| Mục | Nội dung |
|---|---|
| Tóm tắt | Thời lượng dùng được (cột `Dựng` nếu ô là số giây, ví dụ `7.0s`; nếu không thì bảng Rule 49); số lần sinh video theo `duration`; số Start Frame cần sinh ảnh (cột `SF`: G + E; P không sinh); gói |
| Thời lượng theo phần | Số clip, số giây, timecode bắt đầu của mỗi Act |
| Lời hứa trong 30s đầu | Hình + thoại của mọi clip bắt đầu trước giây 30 |
| Bản đồ móc giữ chân | Clip có nhãn `Hook` / `RH` / `Re-hook` + mốc đề xuất cho khoảng trống > 90s |
| Lỗi | Số từ sai dải (kiểm cả số từ đếm được trong ô thoại lẫn cột `Từ`); `duration` ngoài 4/6/8/10; bảng không có cột thoại |
| Cảnh báo | Cột `Từ` lệch số từ thực tế > 1; 0 từ ở clip 6/8/10s không ghi im lặng; dòng có số ô khác header; 2 khối liền nhau cùng `Shot`; khối selfie thứ 3 liên tiếp (Rule 42, chỉ dự án POV vlog) |
| Dòng thời gian AV | Bảng hai lớp hình / tiếng theo timecode — dùng cho Bước 2 |

Một **khối** (Rule 42) gồm clip đầu và các clip nối tiếp nó: chuỗi 4s `a/b/c` cùng gốc ID, hoặc clip có `SF = P` (Start Frame là khung cuối clip trước, Rule 65).

Tool báo `Không tìm thấy bảng clip` → kịch bản có định dạng khác. Agent PHẢI tự lập bảng Dòng thời gian AV theo các cột trên, tính tay, và ghi `tính tay` ở đầu báo cáo.

### Bước 2 — Đọc bấm giờ

Agent đọc Dòng thời gian AV từ đầu đến cuối theo đúng thứ tự người xem. Ghi lại từng clip thuộc một trong các loại sau:

| Mã | Loại | Ví dụ |
|---|---|---|
| D1 | Lặp thông tin: clip nói lại điều clip trước đã cho biết | Hai clip liên tiếp cùng khoe kích thước dấu chân |
| D2 | Không làm việc nào: clip không tăng nguy hiểm, không đặt câu hỏi, không đổi quan hệ, không tiến gần mục tiêu (danh sách "việc của mỗi clip" trong kịch bản, nếu có) | Phong cảnh thứ hai liên tiếp không có tin mới |
| D3 | Thoại kể lại điều hình đã cho thấy (Quality Gate #6 `/fk-scriptwriter`) | "Tôi đang lội qua suối" khi hình là lội suối |
| D4 | Nhịp chậm kéo dài: ≥ 3 clip liên tiếp không có thoại và không có hành động mới | — |

### Bước 3 — Kiểm tra lời hứa (30s đầu)

So bảng "Lời hứa trong 30s đầu" với gói.

- **Đạt:** trong 30s đầu, người xem thấy hoặc nghe điều gói hứa, hoặc một đoạn xem trước rõ ràng của nó (ví dụ cold open cắt từ master).
- **Không đạt:** đề xuất 1 trong 2 cách, kèm lý do:
  1. Đưa cảnh trả lời hứa lên đầu (cold open cắt từ clip sẵn có, không sinh thêm).
  2. Đổi gói cho khớp nội dung mở đầu.

Gói hứa điều phim không có → ghi lỗi `Lệch hứa`. Lệch hứa làm CTR cao nhưng giữ chân thấp (xem `/fk-youtube-analytics` Bước 2).

### Bước 4 — Đặt móc giữ chân

**Định nghĩa:** móc giữ chân (re-hook, nhãn `RH`) là clip đưa vào ít nhất 1 thứ mới: nguy hiểm mới, câu hỏi mới, tiết lộ, đổi địa điểm/thời gian rõ rệt, hoặc lời báo trước "sắp tới".

**Mục tiêu:** khoảng cách giữa 2 móc liên tiếp ≤ 90s dùng được (khuyến nghị 60–90s). Clip đầu phim (hook) tính là móc đầu tiên.

Thao tác:

1. Với mỗi mốc đề xuất của tool, chọn 1 clip trong cửa sổ ±15s đáp ứng định nghĩa.
2. Không clip nào đáp ứng → đề xuất đổi thứ tự clip hoặc rút đoạn trước mốc đó (Bước 5).
3. Ghi nhãn vào kịch bản:
   - `script.md`: thêm `RH · <lý do>` vào đầu cột `Beat`.
   - Screenplay JSON: `"beat": "rehook"`.
4. Chạy lại tool. Bản đồ móc PHẢI hết khoảng trống > 90s, trừ khi user chấp nhận ngoại lệ (ghi lý do vào báo cáo).

Liên kết: mốc re-hook ~3:00 / ~6:00 trong Bảng dựng của `/fk-capcut-edit` NÊN trùng các clip `RH` đã đặt ở bước này.

### Bước 5 — Cắt trên giấy

Chạy bước này khi tổng thời lượng vượt mục tiêu của dự án hoặc Bước 2 có clip D1–D4.

- Cắt phần giữa. Giữ xương sống: hook, điểm đổi Act, các clip `RH`, payoff, cảnh cuối.
- Thứ tự ưu tiên cắt: D1 → D2 → D3 → D4.
- KHÔNG ĐƯỢC cắt clip cài (setup) của một payoff phía sau. Trước khi đề xuất, kiểm tra chuỗi nhân quả của kịch bản (vlog: bảng chuỗi nhân quả sinh tồn ở bước 3–4) và sổ liên tục nếu đã có.
- Cắt 1 mắt xích trong chuỗi 4s hoặc 1 clip `SF = P` → clip kế tiếp mất Start Frame nối tiếp (Rule 65). Ghi rủi ro này vào cột Rủi ro.
- D3 → ưu tiên sửa thoại thay vì cắt clip.

Mỗi đề xuất cắt ghi 4 cột:

| Clip | Giây tiết kiệm | Lần sinh tiết kiệm (video + ảnh) | Rủi ro (cài–trả, liên tục, chuỗi bị ảnh hưởng) |
|---|---|---|---|

### Bước 6 — Kiểm tra trung thực

| Loại phim | Kiểm tra |
|---|---|
| Tài liệu / sự kiện thật (Rule 14) | Mọi dữ kiện trong thoại và chữ trên hình có nguồn trong `.omc/research/`. Dữ kiện không có nguồn → đánh dấu, đề xuất bỏ hoặc chạy `/fk-research`. |
| Vlog hư cấu (ngoại lệ Rule 14) | Không cần nguồn. Kiểm tra: không biếm họa dân tộc/tôn giáo; gói có kế hoạch dòng khai báo tái dựng bằng AI ở mô tả (`/fk-youtube-seo` Step 4, Zone 1). |
| Mọi loại | Tiêu đề và thumbnail không hứa điều phim không có (liên quan Bước 3). |

### Bước 7 — Trình user ⛔

Gửi user trong chat:

1. Tóm tắt: thời lượng, số lần sinh video, số Start Frame cần sinh, số lỗi, số cảnh báo.
2. Kết luận lời hứa 30s.
3. Bản đồ móc giữ chân (đã đặt + đề xuất).
4. Bảng đề xuất cắt (Bước 5).
5. Dữ kiện chưa có nguồn (Bước 6, nếu có).

Dừng chờ user duyệt. Sau khi user duyệt:

1. Sửa `script.md` (hoặc screenplay JSON) theo các mục user chọn.
2. Chạy lại tool đến khi 0 lỗi.
3. Cập nhật khối thông tin đầu `script.md` (`Toán clip`, `Thời lượng`) bằng số liệu tool.
4. Chuyển sang bước kế tiếp của luồng (`/fk-script-to-prompts` hoặc Quality Gate của `/fk-scriptwriter`).

Khi hỏi user trước bước sinh media (Rule 29), agent cộng 3 con số: số video (báo cáo), số Start Frame G + E (báo cáo), số ảnh ref còn thiếu (`GET /api/projects/{pid}`, không có trong báo cáo).

---

## Định nghĩa hoàn thành

- [ ] Báo cáo paper edit mới nhất, 0 lỗi.
- [ ] Có gói; lời hứa được trả trong 30s đầu, hoặc user chấp nhận ngoại lệ có ghi lý do.
- [ ] Không còn khoảng trống móc giữ chân > 90s, hoặc user chấp nhận ngoại lệ có ghi lý do.
- [ ] Đề xuất cắt đã được user duyệt hoặc từ chối.
- [ ] Khối thông tin đầu `script.md` khớp số liệu tool.

## Không làm

- Không gọi Flow API, không sinh media.
- Không sửa prompt JSON (`prompts_actX.json`). Việc đó thuộc `/fk-script-to-prompts`.
- Không tự cắt hoặc đổi thứ tự clip khi user chưa duyệt.
- Không áp số từ theo 130–150 từ/phút. Số từ theo bảng ở mục "Luật số từ tool dùng".

## Ví dụ — Hell Creek 66 Ma v2 (chạy thử 16/10/2026)

`python tools/paper_edit.py output/hell_creek_66_ma_v2/script.md` cho kết quả:

- 9:56.5 dùng được; 111 lần sinh video (43×4s · 22×6s · 40×8s · 6×10s); 93 Start Frame cần sinh ảnh (G 55 · E 38; P 18); 0 lỗi.
- Khối thông tin đầu `script.md` ghi 601.5s, 112 lần sinh (42×8s · 5×10s), G 57 · P 17 — lệch với bảng. Giả thuyết: khối này chưa cập nhật sau khi bỏ A1-03 (15/10) và đổi độ dài vài clip.
- Chưa có dòng `Package`.
- Chỉ cold open mang nhãn hook; tool đề xuất 7 mốc đặt `RH` (1:15, 2:30, 3:45, 5:00, 6:15, 7:30, 8:45).
