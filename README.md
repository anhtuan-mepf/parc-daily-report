# parc-daily-report

## Project Health Check (web app)

Thư mục `app/` – web app kiểm tra sức khỏe dự án, 1 file HTML, chạy offline, cài được lên điện thoại (PWA).

**Chạy:** mở `app/index.html` bằng trình duyệt; hoặc bật GitHub Pages (Settings → Pages → branch, thư mục `/`) rồi truy cập `.../app/` → "Add to Home screen" để cài như app.

**9 hạng mục chấm điểm (0–100, trọng số chỉnh trong Cài đặt):**

| Hạng mục | Chỉ số | Cách tính điểm |
|---|---|---|
| Tiến độ (25) | SPI có trọng số theo hệ thống | (SPI − 0,7)/0,3 × 100 |
| Chi phí (15) | CPI = EV/AC, EAC = BAC/CPI | (CPI − 0,7)/0,3 × 100 |
| Dòng tiền (10) | Thu thực tế / kế hoạch lũy kế | (tỷ lệ − 0,6)/0,4 × 100 |
| RFI (10) | Số RFI quá hạn, số ngày quá hạn | 100 − 15×quá hạn − số ngày quá hạn lớn nhất |
| NCR (10) | Major/Minor/Obs mở, quá hạn | 100 − 30×Major − 8×Minor − 2×Obs − 10×quá hạn; có Major → tối đa Vàng |
| Submittal (10) | Chờ duyệt quá hạn, tỷ lệ C | 100 − 12×quá hạn − 50×tỷ lệ C |
| HSE (10) | LTI, LTIFR, first aid, tồn tại | 100 − 4×tồn tại − 3×first aid; có LTI → tối đa 40 |
| Nhân lực (5) | Thực tế / kế hoạch | (tỷ lệ − 0,6)/0,4 × 100 |
| Rủi ro (5) | P×I ≥ 15 cao, 8–14 trung bình | 100 − 15×cao − 5×trung bình |

Xanh ≥ 80, Vàng 60–79, Đỏ < 60. Có hạng mục Đỏ thì tổng thể tối đa Vàng.

Dữ liệu lưu trong trình duyệt (localStorage); dùng Xuất/Nhập JSON để chuyển máy hoặc gửi cho người khác. "Lưu kỳ báo cáo" mỗi tuần để có biểu đồ xu hướng. "Copy tóm tắt" để dán vào Zalo/email.
