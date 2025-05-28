1. Hướng dẫn cài Python 3 trên CentOS 7
Mặc định CentOS 7 có Python 2.7, để cài Python 3 bạn làm như sau:


# Cập nhật hệ thống
sudo yum update -y

# Cài EPEL repo (nơi chứa Python 3 cho CentOS7)
sudo yum install epel-release -y

# Cài Python 3
sudo yum install python36 python36-pip -y

# Kiểm tra phiên bản Python 3
python3 --version

# Kiểm tra pip3 (quản lý gói python)
pip3 --version


Nếu bạn muốn cho lệnh python chạy Python3, có thể tạo alias (tạm thời):

bash
Sao chép
Chỉnh sửa
alias python=python3
Hoặc chỉnh trong shell profile nếu cần.

2. File README hướng dẫn chạy script Python cài Zimbra
markdown
Sao chép
Chỉnh sửa
# Hướng dẫn cài đặt Zimbra bằng script Python trên CentOS 7

## Yêu cầu:
- Hệ điều hành CentOS 7
- Python 3 đã được cài đặt (xem hướng dẫn cài Python 3 bên dưới)

## Cài Python 3 (nếu chưa có)

```bash
sudo yum update -y
sudo yum install epel-release -y
sudo yum install python36 python36-pip -y
Kiểm tra:


python3 --version
Cách chạy script cài Zimbra
Tải file install_all_in_one.py (file script gộp toàn bộ các bước cài Zimbra).

Chạy script với quyền root hoặc sudo:

'''
sudo python3 install_all_in_one.py
'''
Script sẽ hỏi bạn các thông tin như:

Domain (vd: mail.example.com)

IP Server (vd: 192.168.1.10)

Domain để tạo DKIM

Domain để xin và cài SSL

Bạn chỉ cần nhập đúng và theo dõi tiến trình cài đặt.

Nếu script báo lỗi, kiểm tra lại thông báo lỗi và sửa rồi chạy lại từ bước bị lỗi.