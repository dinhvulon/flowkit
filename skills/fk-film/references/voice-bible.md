# Voice Bible — Hệ Thống Giọng Nói & Thoại Nhân Vật Điện Ảnh

> **Quy chuẩn điện ảnh ngôi thứ ba (`fk-film`):** Mỗi nhân vật có thoại được phân định một Voice ID riêng biệt từ danh sách 30 giọng chuẩn Pinhole / Gemini-TTS (§0 và §0b), ghi vào `speech.voices` trong prompt JSON. Độ dài thoại tuân thủ nghiêm ngặt Rule 49 (§2). Không có vlogger, không có độc thoại phá vỡ bức tường thứ 4.

Đọc tài liệu này **trước khi viết bất kỳ dòng thoại nào** cho kịch bản điện ảnh.

---

## 0. Hệ Thống 30 Giọng Pinhole / Gemini-TTS (`PINHOLE_VOICES`)

Server lấy **từ đầu tiên** của `voice_description` làm voice id (ví dụ `"kore — firm, …"` → `kore`). 

Cao độ được phân bổ từ thấp đến cao: **low / lower → mid-low → mid → mid-high / younger → high**.

| ID | Giới tính | Tính chất âm vực | Cao độ | Phân vai gợi ý trong phim |
| :--- | :--- | :--- | :--- | :--- |
| `achernar` | Nữ | soft | high | Tiếng thì thầm, linh hồn, ảo ảnh |
| `achird` | Nam | friendly | mid | Người đồng hành thân thiện, hoa tiêu trẻ |
| `algenib` | Nam | gravelly | low | Thủ lĩnh uy quyền, chiến binh khổng lồ, kẻ đe dọa |
| `algieba` | Nam | easy-going | mid-low | Thủy thủ điềm tĩnh, nhân vật hiền hòa |
| `alnilam` | Nam | firm | mid-low | Chiến binh quả cảm, thợ săn cộc cằn, hoa tiêu sắc sảo |
| `aoede` | Nữ | breezy | mid | Nữ chiến binh nhanh nhẹn, phụ nữ sôi nổi |
| `autonoe` | Nữ | bright | mid | Phụ nữ thông tuệ, nữ học giả, người dẫn đường |
| `callirrhoe` | Nữ | easy-going | mid | Phụ nữ điềm đạm, dân thường |
| `charon` | Nam | informative | lower | Học giả thông thái, người kể chuyện |
| `despina` | Nữ | smooth | mid | Người mẹ, nữ quý tộc |
| `enceladus` | Nam | breathy | lower | Pháp sư, ông già tiên tri, người hấp hối |
| `erinome` | Nữ | clear | mid | Nữ cận vệ điềm tĩnh, người đưa tin |
| `fenrir` | Nam | excitable | younger | Thiếu niên dũng cảm, trinh sát trẻ |
| `gacrux` | Nữ | mature | mid | Nữ trưởng lão, bà lão tiên tri |
| `iapetus` | Nam | clear | mid-low | Sứ giả, chiến binh trầm tính |
| `kore` | Nữ | firm | mid | **Nữ thủ lĩnh, nữ thuyền trưởng, nữ tướng quyết đoán** |
| `laomedeia` | Nữ | upbeat | mid-high | Nữ phiêu lưu năng động, phản ứng nhanh |
| `leda` | Nữ | youthful | mid-high | Thiếu nữ, cô gái trẻ |
| `orus` | Nam | firm | mid-low | Đội phó, thủ lĩnh thứ hai nghiêm nghị |
| `puck` | Nam | upbeat | mid | Chàng trai hăng hái, hoa tiêu hoạt bát |
| `pulcherrima` | Phi giới tính | forward | mid-high | Sinh vật ma thuật, giọng nói thần bí |
| `rasalgethi` | Nam | informative | mid | Thương nhân sành sỏi, nhà hàng hải |
| `sadachbia` | Nam | lively | low | Gã khổng lồ vui tính, tay búa dũng mãnh |
| `sadaltager` | Nam | knowledgeable | mid | Lão hoa tiêu từng trải, người dẫn đường kỳ cựu |
| `schedar` | Nam | even | mid-low | Kẻ lạnh lùng, phản diện thâm trầm |
| `sulafat` | Nữ | warm | mid | Người phụ nữ ấm áp, người chữa thương |
| `umbriel` | Nam | smooth | lower | Pháp sư bóng tối, tu sĩ trầm mặc |
| `vindemiatrix` | Nữ | gentle | mid | Nữ thầy thuốc hiền từ |
| `zephyr` | Nữ | bright | mid-high | Nữ cung thủ sắc sảo |
| `zubenelgenubi` | Nam | casual | mid-low | Thủy thủ phong trần, dân biển |

---

## 0b. Gán Giọng & Phân Vai Cho Từng Nhân Vật

Mỗi nhân vật **có thoại** trong kịch bản phải được chỉ định **một Voice ID riêng biệt**:
1. **Tương phản âm sắc:** Không gán cùng một Voice ID cho hai nhân vật nói chuyện với nhau trong cùng một cảnh. Giọng nam chính và nữ chính phải cách nhau rõ rệt về âm sắc và cao độ.
2. **Khóa vào kịch bản:** Khai báo cột `Voice` trong bảng nhân vật của `script.md` (ví dụ: `kore — Nữ thủ lĩnh dứt khoát`).
3. **Mô tả trong Prompt Video:** Trong timeline hành động, ghi rõ:
   `Nora speaks in a firm, mid-pitched resolute female voice: "..."`  
   `Theron speaks in a weathered, raspy knowledgeable male voice: "..."`

---

## 1. `VOICE_LOCK` — Khóa Tính Cách & Khẩu Khí Nhân Vật

Mỗi nhân vật chính có một khối `VOICE_LOCK` riêng quy định:
- **Tốc độ & Nhịp điệu:** Nói nhanh, dứt khoát khi lâm nguy; trầm ổn, sắc bén khi chỉ huy.
- **Vốn từ vựng:** Dùng ngôn ngữ thực tế của người đi biển, chiến binh phong trần; không dùng từ ngữ triết lý sáo rỗng hay ngôn từ hiện đại.
- **Điểm yếu & Cảm xúc:** Giọng nghẹn lại khi mất mát, gằn giọng khi đối đầu hiểm nguy.
- **Những điều cấm kỵ:** Không bao giờ giảng giải đạo lý, không nói khẩu hiệu sáo mòn, không xưng hô với khán giả.

---

## 2. Độ Dài Thoại Theo Thời Lượng Clip (Rule 49)

Trong điện ảnh AI, thoại quá dài sẽ bị cắt đứt giữa chừng (*cut-off*), thoại quá ngắn sẽ tạo khoảng lặng vô hồn (*dead air*). Tuân thủ nghiêm ngặt bảng số từ:

| Độ dài Clip | Số từ tiếng Anh tối ưu | Phân bổ nhịp timeline |
| :--- | :--- | :--- |
| **Clip 4s** | **0** (hành động thuần túy) hoặc **6–8 từ** | `0-2s` hoặc `2-4s` |
| **Clip 6s** | **12–15 từ** | `0-2s / 2-4s / 4-6s` |
| **Clip 8s** | **18–22 từ** | `0-3s` (6-7 từ) / `3-6s` (7-8 từ) / `6-8s` (5-7 từ) |
| **Clip 10s** | **24–28 từ** | `0-3s / 3-7s / 7-10s` |
| **Cảnh Master / Cảnh Kết** | **0 từ** (Hình ảnh điện ảnh trọn vẹn) | Lắng đọng cảm xúc bằng âm nhạc và tiếng động hiện trường |

---

## 3. Quy Chuẩn Kịch Tính & Chống Giọng AI Sáo Mòn

- **Hành động dẫn dắt thoại (Show > Tell):** Nhân vật chỉ nói khi hành động không đủ diễn tả. Nếu đã thấy ngọn lửa bùng lên, nhân vật không nói *"Lửa đang cháy rồi"*, mà hô mệnh lệnh *"Dạt sang mạn phải!"*.
- **Khoảng lặng kịch tính (Dramatic Pause):** Mỗi trường đoạn căng thẳng cần có những giây im lặng tuyệt đối của nhân vật trước một biến cố bất ngờ (`No dialogue; only ocean wind and heavy breathing`).
- **Thoại gắt & chân thực khi xung đột (Bài học 101):** Trong cảnh tranh cãi hoặc chiến đấu, ngữ điệu phải to, gắt, cộc cằn (`commanding, breathless, shouting over the storm`), cấm kiểu đọc đều đều nhỏ nhẹ.
