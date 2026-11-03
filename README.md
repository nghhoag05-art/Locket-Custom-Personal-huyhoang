# Locket Custom Personal — bản giữ nguyên dữ liệu

Đây là **bản đóng gói lại** những dữ liệu/script mà bạn đã cung cấp. Mặc định **không sửa bất kỳ giá trị cấu hình hay thuật toán nào trong ba file JavaScript**. Tên file giữ nguyên để dễ đối chiếu.

## Cấu trúc

```text
Locket_Custom_Personal/
├── scripts/
│   ├── locketfix8.js          # Phản hồi RevenueCat — dữ liệu giữ nguyên
│   ├── header7.js             # Header RevenueCat — dữ liệu giữ nguyên
│   └── forceGold4.3.js        # Firebase Remote Config — 644+ dòng nội dung giữ nguyên
├── backup/                    # Bản sao đối chiếu, KHÔNG sửa khi tùy biến
├── module/
│   ├── locket-custom.template.conf  # Module dùng URL GitHub của bạn
│   └── locket-original-links.conf    # Bản đối chiếu link gốc
├── tools/
│   └── build_module.py       # Tạo module link riêng
├── docs/
│   └── TUY_CHINH.md
├── SHA256SUMS.txt
└── README.md
```

## Dùng tài khoản GitHub của bạn

1. Tạo repository mới (ví dụ `Locket-Custom-Personal`) và upload **toàn bộ thư mục bên trong** dự án.
2. Chạy lệnh ngay tại thư mục dự án:

   ```bash
   python tools/build_module.py --user TEN_GITHUB_CUA_BAN --repo Locket-Custom-Personal
   ```

3. File `module/locket-custom.conf` sẽ được tạo và tham chiếu **3 script trên GitHub của bạn**, không còn trỏ tới nơi đăng gốc.
4. Đưa file `module/locket-custom.conf` mới tạo lên repository.
5. Đường dẫn module là:

   ```text
   https://raw.githubusercontent.com/TEN_GITHUB_CUA_BAN/Locket-Custom-Personal/main/module/locket-custom.conf
   ```

> **Chú ý:** Chưa upload lên GitHub thì link tùy chỉnh trong template sẽ chưa hoạt động. Cấu hình `locket-original-links.conf` giữ lại địa chỉ gốc chỉ để tham chiếu, và vẫn phụ thuộc nguồn bên thứ ba.

## Giữ dữ liệu cũ và sửa sau

- **Chưa sửa gì:** Nội dung `scripts/` và `backup/` được tạo y hệt nhau.
- **Khi cần sửa:** Chỉ sửa file trong `scripts/`, không sửa `backup/`.
- **Muốn quay về bản ban đầu:** Sao chép file từ `backup/` qua `scripts/`.
- Hướng dẫn vị trí các phần nằm trong `docs/TUY_CHINH.md`.
- Đổi tên dự án và URL **không** tự thay đổi cách Locket hoạt động.

## Giới hạn và an toàn

Các script can thiệp phản hồi mạng của ứng dụng; nội dung có thể nhằm giả lập trạng thái trả phí. Không thể xác nhận rằng tất cả cờ tính năng đã bật sẽ hoạt động trong ứng dụng hay được máy chủ chấp nhận. Việc dùng MITM cho phép proxy đọc và thay đổi lưu lượng HTTPS trên các miền cấu hình. Hãy cân nhắc bảo mật dữ liệu tài khoản và quy định dịch vụ.

**Quyền tác giả:** Dự án này chỉ được đóng gói lại từ mã bạn cung cấp; việc tạo repository riêng **không có nghĩa bạn là tác giả gốc**. Giữ nguyên ghi nhận tác giả và kiểm tra quyền sử dụng/phân phối mã nguồn trước khi công khai.
