# fk-youtube-analytics — Chẩn đoán video sau khi đăng (CTR, giữ chân 30s, AVD) và kế hoạch giữ người xem ở lại kênh

Usage: `/fk-youtube-analytics [slug] [--at 48h|7d]`

Skill này đọc số liệu YouTube Studio của một video đã đăng, chẩn đoán lỗi ở gói (tiêu đề + thumbnail) hay ở nội dung, đề xuất **đổi 1 biến**, và lập kế hoạch "Next" (end screen, playlist, Shorts mồi). Bài học được đưa ngược về `/fk-paper-edit` và kịch bản của video sau.

Phương pháp lấy từ bước Iterate + Next của khung CHAIN (skill ngoài `youtube-long-form`), đã chỉnh theo FlowKit. Phần đăng bài qua WoopSocial của skill đó **không áp dụng**.

---

## Thuật ngữ

Mỗi thuật ngữ dưới đây chỉ dùng cho đúng một chỉ số.

| Thuật ngữ | Định nghĩa | Chỗ xem trong YouTube Studio |
|---|---|---|
| Impressions | Số lần thumbnail được hiển thị | Analytics → Reach |
| CTR | Impressions click-through rate = lượt xem từ impressions / impressions | Analytics → Reach |
| Giữ chân 30s | % người xem còn xem ở 0:30 | Analytics → Engagement → biểu đồ Audience retention (key moment "Intro") |
| AVD | Average view duration — thời lượng xem trung bình (giây) | Analytics → Engagement |
| AVD % | AVD / độ dài video × 100 | Tính từ 2 số trên |
| Điểm tụt | Timecode mà đường giữ chân giảm dốc nhất | Biểu đồ Audience retention |
| End screen CTR | End screen element click rate | Analytics → Engagement |

Lưu ý: bản cũ của `skills/fk-time-travel-vlog/references/post-and-publish.md` §3 gọi chỉ số 30s là "AVD" (đã sửa 16/10/2026). Skill này tách riêng **Giữ chân 30s** và **AVD**.

## Ngưỡng

| Chỉ số | Đạt | Cần hành động | Nguồn |
|---|---|---|---|
| CTR | ≥ 6% | < 4% → đổi gói | `post-and-publish.md` §3 |
| Giữ chân 30s | ≥ 60% | < 60% | `post-and-publish.md` §3 |
| AVD % | ≥ trung vị kênh | < trung vị kênh | Tính từ `output/_channel/analytics_log.jsonl` |

- CTR từ 4% đến dưới 6% là vùng theo dõi: không đổi gì, đo lại ở mốc kế tiếp.
- Log kênh có < 3 dòng cùng định dạng → trung vị AVD % là `UNKNOWN`. Chỉ dùng 2 ngưỡng tuyệt đối ở trên.
- **Chỉ áp dụng cho video dài (long-form).** Shorts trong feed không có CTR theo thumbnail; YouTube Studio đo "Viewed vs. swiped away". Repo chưa có ngưỡng cho Shorts → ghi số liệu, đánh dấu `UNKNOWN: chưa có ngưỡng Shorts`, chỉ so với các Shorts trước của kênh.

---

## Quy trình

### Bước 1 — Thu số liệu

**Nguồn mặc định:** user dán số hoặc gửi ảnh chụp các tab Reach và Engagement trong YouTube Studio. Agent hỏi đủ danh sách sau trong 1 lượt:

1. Mốc đo (số giờ sau khi đăng).
2. Impressions, CTR, views.
3. AVD và độ dài video.
4. Giữ chân 30s.
5. 3 điểm tụt lớn nhất: timecode + % còn lại.
6. End screen CTR.
7. Nguồn traffic (%): Browse, Suggested, Search, Shorts, External.

**Nguồn tùy chọn — YouTube Analytics API:** `youtube/auth.py` hiện chỉ có scope `youtube.upload` và `youtube.readonly`. Analytics API cần thêm scope `https://www.googleapis.com/auth/yt-analytics.readonly`. Thêm scope bắt user đăng nhập OAuth lại. Agent KHÔNG ĐƯỢC tự sửa scope; hỏi user trước.

Quy tắc số liệu:

- KHÔNG ĐƯỢC đoán hoặc bịa số. Số thiếu → ghi `UNKNOWN`.
- Đo ở 2 mốc: 48h và 7 ngày sau khi đăng.
- Đo trước 48h hoặc impressions thấp → mọi kết luận ghi nhãn `sơ bộ` và ghi kèm số impressions.

### Bước 2 — Chẩn đoán

| CTR | Giữ chân 30s | Chẩn đoán | Hành động |
|---|---|---|---|
| < 4% | ≥ 60% | Gói yếu; nội dung giữ được người xem | Đổi thumbnail trước (Bước 3) |
| ≥ 6% | < 60% | Lệch hứa: gói hứa điều mở đầu không trả, hoặc mở đầu chậm | Sửa gói cho khớp nội dung đã có. Video sau: chạy `/fk-paper-edit` Bước 3 chặt hơn |
| < 4% | < 60% | Chủ đề hoặc gói không hợp khán giả kênh | Không sửa video này. Ghi bài học; chọn chủ đề video sau theo `post-and-publish.md` §4 |
| ≥ 6% | ≥ 60% | Tốt | Đầu tư Bước 4 (Next) |
| 4% đến < 6% | bất kỳ | Vùng theo dõi | Không đổi; đo lại ở mốc 7 ngày |

**Điểm tụt → clip:** đổi mỗi timecode điểm tụt thành clip ID.

1. Ưu tiên EDL của bản dựng đã giao: `${OUTDIR}/edit/edit_vN` với N là phiên bản đã đăng (Rule 66).
2. Không có EDL → `output/<slug>/capcut_edit_sheet.md` (timecode Bảng dựng, đã có trailer intro).
3. Không có cả hai → dùng `output/<slug>/paper_edit.md` và cộng thêm độ dài intro/trailer nếu có. Ghi rõ `ước tính` khi dùng cách này.

Với mỗi điểm tụt, ghi giả thuyết nguyên nhân (nhãn `HYPOTHESIS`) theo mã D1–D4 của `/fk-paper-edit` Bước 2, hoặc: hết móc giữ chân (> 90s từ `RH` gần nhất), hình lỗi AI, âm lượng đổi đột ngột.

**AVD %:** so với trung vị kênh. AVD % thấp nhưng giữ chân 30s đạt → vấn đề nằm ở thân phim: kiểm tra bản đồ móc giữ chân của video đó.

### Bước 3 — Đổi 1 biến

- Mỗi lần chỉ đổi 1 biến: thumbnail HOẶC tiêu đề. KHÔNG ĐƯỢC đổi cả hai cùng lúc, vì không biết thay đổi nào có tác dụng. Luật này thay cho cách "đổi tiêu đề và bộ thumbnail dự phòng" cũ ở `post-and-publish.md` §3 mục 2 (đã sửa để trỏ về skill này).
- Thứ tự: thumbnail trước (dùng bộ dự phòng của `/fk-thumbnail`), tiêu đề sau (option khác trong `/fk-youtube-seo` Step 3).
- Có tính năng Test & compare trong YouTube Studio → NÊN dùng thay cho đổi tay.
- User đổi trong YouTube Studio. Agent không gọi API sửa metadata.
- Ghi vào log: biến đã đổi, giá trị cũ, giá trị mới, thời điểm đổi. Đo lại sau ≥ 48h.

### Bước 4 — Next: giữ người xem ở lại kênh

| Việc | Cách làm |
|---|---|
| End screen | 2 phần tử: video kế tiếp cùng series + playlist. YouTube cho end screen dài 5–20s; kịch bản video sau NÊN chừa cảnh cuối đủ dài cho end screen |
| Playlist series | Thứ tự tập theo `output/<slug>/series_manifest.json` (nếu có) |
| Shorts mồi | 3–4 Shorts cắt từ video dài, gắn "Related video" về video dài (`post-and-publish.md` §3.1; kế hoạch cắt ở `/fk-capcut-edit` §7) |
| Câu dẫn sang video sau | Chỉ áp dụng cho video sau: đưa vào kịch bản (`/fk-scriptwriter` Section G2 hoặc `/fk-time-travel-vlog` bước 3) |
| Bình luận ghim | 1 câu hỏi mở về nội dung phim + link playlist |

End screen CTR thấp → đề xuất đổi video được trỏ tới (chọn video có CTR cao nhất kênh), không đổi vị trí phần tử.

### Bước 5 — Ghi kết quả và bài học

1. Báo cáo: `output/<slug>/analytics/analytics_<YYYY-MM-DD>_<mốc>.md` theo mẫu dưới.
2. Thêm 1 dòng JSON vào `output/_channel/analytics_log.jsonl`:

```json
{"date": "2026-10-18", "slug": "hell_creek_66_ma_v2", "format": "long", "at": "48h", "impressions": null, "ctr": null, "ret_30s": null, "avd_s": null, "length_s": null, "avd_pct": null, "end_screen_ctr": null, "change": "thumbnail V1 -> V3"}
```

Giá trị không có → `null`. KHÔNG ĐƯỢC điền số ước đoán.

3. Bài học cho video sau → trình user. Chỉ khi user đồng ý: vlog → thêm vào `skills/fk-time-travel-vlog/references/production-lessons.md` (số bài học kế tiếp, đúng format file); phim tài liệu narrator → ghi chú vào screenplay JSON của tập sau.

---

## Mẫu báo cáo

```markdown
# Analytics — <tiêu đề video> — <mốc đo>

| Chỉ số | Giá trị | Ngưỡng | Kết luận |
|---|---|---|---|
| Impressions | … | — | — |
| CTR | …% | ≥ 6% / < 4% | Đạt / Theo dõi / Hành động |
| Giữ chân 30s | …% | ≥ 60% | … |
| AVD | …s / …s (…%) | trung vị kênh …% hoặc UNKNOWN | … |
| End screen CTR | …% | — | … |

## Chẩn đoán
<1 dòng từ bảng Bước 2>

## Điểm tụt
| Timecode | % còn lại | Clip | Giả thuyết (HYPOTHESIS) |

## Đổi 1 biến
<biến, cũ → mới, ngày đổi, ngày đo lại>

## Next
<end screen, playlist, Shorts, bình luận ghim>

## Bài học cho video sau (chờ user duyệt)
```

## Không làm

- Không bịa hoặc ước đoán số liệu.
- Không mua view, không spam kêu gọi đăng ký.
- Không đổi tiêu đề và thumbnail cùng lúc.
- Không gọi Flow API, không sinh media.
- Không tự thêm OAuth scope.
