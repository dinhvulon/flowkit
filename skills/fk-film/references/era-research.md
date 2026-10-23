# Nghiên Cứu Thời Kỳ, Lịch Sử & Xây Dựng Thế Giới Điện Ảnh (`/fk-research`)

> **Quy chuẩn `/fk-film` (Rule 14):** Đọc ở **Bước 1** của `SKILL.md`.
> - Với phim dựa trên sự kiện lịch sử, địa danh, văn hóa hoặc nhân vật có thật: **BẮT BUỘC** chạy `/fk-research` tra cứu và kiểm chứng nguồn thực tế trước khi viết `story-bible.md` và `script.md` (lưu hồ sơ tại `.omc/research/`). Nếu nhân vật lấy cảm hứng từ người thật nổi tiếng, tuân thủ **Rule 15 (Real-people bypass)**: dùng biệt danh theo vai trò/chức danh và chỉ mô tả ngoại hình, tuyệt đối không đưa tên thật vào entity hay prompt.
> - Với phim giả tưởng / thần thoại / hư cấu hoàn toàn: Ghi rõ tính chất hư cấu trong `story-bible.md`, nhưng vẫn phải thiết lập quy tắc vật lý, kiến trúc, trang phục và niên đại nhất quán (`PERIOD LOCK`).

---

## 1. Xây Dựng Hồ Sơ Thế Giới & Chọn Beat Kịch Tính

Khi nghiên cứu bối cảnh cho phim điện ảnh (Cổ đại, Trung cổ, Kỷ Băng Hà, Hàng hải thế kỷ 17, Thảm họa thiên nhiên, v.v.), tập trung khai thác các chất liệu thị giác và xung đột phục vụ trực tiếp cho bộ skill biên kịch `sw-*`:

1. **Bối cảnh Không gian & Thời gian (`Setting & Arena` — `/sw-genre-anatomy`, `/sw-scene-craft`)**:
   - Niên đại cụ thể, địa hình đặc trưng, khí hậu, mùa và nguồn sáng tự nhiên của thời kỳ (đuốc nhựa thông, đèn dầu cá voi, lửa trại, ánh trăng, sương mù).
   - Các giới hạn vật lý của môi trường tạo áp lực sinh tồn (*pressure chamber*): cái lạnh `-40°C`, bão biển, hẻm đá hẹp, rừng cháy, thủy triều dâng.
2. **Chất liệu Thị giác & Phục trang (`Visual Texture & Wardrobe` — `/fk-character-design`, Rule 35)**:
   - **Kiến trúc & Phương tiện:** Vật liệu xây dựng thực tế (gỗ sồi đóng tàu, đá vôi, lều xương voi ma mút, đồng cổ oxy hóa), tuyệt đối không lẫn vật liệu công nghiệp hiện đại.
   - **Trang phục chuẩn lịch sử:** Quần áo may đo nhiều lớp theo đúng khí hậu và tầng lớp xã hội (chiến binh, thủy thủ, học giả, ngư dân). Ví dụ: Kỷ Băng Hà bắt buộc mặc parka da tuần lộc nhiều lớp chống rét (Rule 35), không cởi trần hoặc quấn da thú sơ sài phi thực tế.
3. **Đạo cụ, Vũ khí & Cơ học (`Props & Mechanics` — `/fk-action-choreography`)**:
   - Vũ khí, công cụ hàng hải (hải đồ da cừu, compa đồng, lao móc, kiếm đồng/thép rèn tay) và cách vận hành cơ học thực tế của chúng để đưa vào `props_lock` và `dramatic_craft.prop_and_detail`.
4. **Luật lệ, Tín ngưỡng & Nguồn Xung Đột (`Conflict & Stakes` — `/sw-character-conflict`, `/sw-truby-anatomy`)**:
   - Những điều cấm kỵ, lời nguyền, quy ước hàng hải/bộ lạc, hoặc sự đối lập giá trị đạo đức giữa các nhân vật giúp tạo nên bước ngoặt giá trị (`value_turn`) trong từng cảnh.

---

## 2. Bảng Tổng Hợp Chất Liệu Kịch Bản (Đầu Vào Cho `story-bible.md`)

| # | Hạng mục / Không gian | Chi tiết lịch sử / thế giới quan đã xác thực | Chức năng kịch tính & Xung đột (`sw-*`) | Đạo cụ & Chi tiết thị giác neo vào Prompt |
|---|---|---|---|---|
| 1 | ... | ... | ... | ... |

---

## 3. Những Điều Cấm Kỵ Để Bảo Toàn Tính Chân Thực (`PERIOD LOCK`)

- **Cấm đạo cụ lệch niên đại (Anachronisms):** Không xuất hiện vật liệu nhựa, khóa kéo kim loại hiện đại, đồng hồ đeo tay, kính cường lực, vệt lốp xe cơ giới (Rule 59), hoặc thực vật/động vật chưa tồn tại ở thời kỳ/châu lục đó.
- **Cấm rập khuôn sai lệch hoặc phản cảm:** Không dùng chi tiết giả tưởng sai lịch sử (như mũ sừng Viking trong phim lịch sử chuẩn); không mô tả cảnh bạo lực máu me trực diện gây vi phạm bộ lọc an toàn (`UNSAFE_GENERATION`), thay bằng lực va chạm cơ học và hậu quả lên môi trường theo `/fk-action-choreography`.
