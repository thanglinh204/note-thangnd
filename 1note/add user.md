## Quy trình tạo user Linux và cấp quyền sudo
# Tạo user mới:
Chạy lệnh sau để tạo user mới, thay ten_user bằng tên người dùng bạn muốn:

```bash
sudo adduser kayle
```

Hệ thống sẽ yêu cầu bạn:
Nhập mật khẩu cho user.
Điền một số thông tin cơ bản (họ tên, số điện thoại, v.v.) – có thể nhấn Enter để bỏ qua nếu không cần.
Xác nhận thông tin và hoàn tất.

# Thêm user vào nhóm sudo:
Để user có quyền sử dụng lệnh sudo, thêm user vào nhóm sudo (áp dụng cho hệ thống dựa trên Ubuntu/Debian):

```bash
sudo usermod -aG sudo kayle
```

Lệnh -aG đảm bảo user được thêm vào nhóm mà không làm mất các nhóm khác (nếu có).
Cấp quyền sudo không cần mật khẩu (tùy chọn):
Mở file /etc/sudoers để chỉnh sửa bằng visudo:

```bash
sudo visudo
```
Di chuyển đến cuối file và thêm dòng sau, thay ten_user bằng tên user bạn tạo:

```
kayle ALL=(ALL) NOPASSWD: ALL
```

Lưu file và thoát:
Với nano: Nhấn Ctrl+O, Enter, rồi Ctrl+X.
Với vim: Nhấn :wq rồi Enter.
Lưu ý: Quyền NOPASSWD: ALL cho phép user chạy lệnh sudo mà không cần nhập mật khẩu, giảm tính bảo mật. Chỉ sử dụng nếu cần thiết.
Kiểm tra quyền sudo:
# Đăng nhập bằng user mới:

```bash

su - kayle
```
Kiểm tra quyền bằng lệnh:

```bash
sudo -l
```
Nếu cấu hình đúng, bạn sẽ thấy thông báo về quyền sudo của user, bao gồm khả năng chạy tất cả lệnh (với hoặc không cần mật khẩu tùy cấu hình).
