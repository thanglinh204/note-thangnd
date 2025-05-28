# Hướng Dẫn Cài Đặt Zimbra Bằng Script Python Trên CentOS 7

## Yêu cầu
- Hệ điều hành: CentOS 7
- Python 3 đã được cài đặt (xem hướng dẫn bên dưới)

---

## 1. Cài Python 3 trên CentOS 7

CentOS 7 mặc định có Python 2.7. Để cài Python 3, bạn chạy lần lượt các lệnh sau:

```bash
sudo yum update -y
sudo yum install epel-release -y
sudo yum install python36 python36-pip -y
