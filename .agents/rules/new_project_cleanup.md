# Quy tắc khởi tạo Dự án mới (New Project Initialization)

Mỗi khi người dùng yêu cầu tạo một dự án mới (hoặc gọi các skill tạo kịch bản/dự án như `/fk-create-project`, `/fk-vlog-japan`, `/fk-time-travel-vlog`, v.v.):

1. **BẮT BUỘC DỌN SẠCH HÀNG ĐỢI CŨ**:
   Chạy lệnh sau trước khi bắt đầu tạo dự án hoặc kịch bản mới:
   ```bash
   # Trong môi trường Windows PowerShell:
   python -c "import sqlite3; conn = sqlite3.connect('flow_agent.db'); conn.execute('UPDATE request SET status=\'FAILED\' WHERE status=\'PENDING\''); conn.commit()"
   ```
   Mục đích: Hủy bỏ ngay lập tức toàn bộ các request `PENDING` còn sót lại từ các dự án trước để tránh worker ngầm tự động retry và gây lỗi `PUBLIC_ERROR_UNUSUAL_ACTIVITY`.
