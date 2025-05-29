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
```
# 1.1 Thiết lập bản ghi DNS ban đầu

Đầu tiên để chuẩn bị cấu hình, cài đặt cần phải tạo các bản ghi cho tên miền. Truy cập vào trang quản lý tên miền của các nhà cung cấp và tạo các bản ghi như dưới đây.

```bash
mail	A	43.231.65.31 
autodiscover	CNAME	clouddata.vn 
autoconfig	CNAME	mail.clouddata.vn 
@	MX	mail.clouddata.vn 10
```

## 2. Chuẩn bị neu server NAT IP public
Neu server ban dung IP private va NAT ra ngoai bang IP public, can them IP public vao loopback cua server truoc khi chay script:

Thay 43.231.65.31 bang IP public tuong ung cua ban.

Thêm IP public vào loopback:

```
ip addr add <IP_PUBLIC>/32 dev lo
```
![image](https://github.com/user-attachments/assets/d815dbe0-b078-4b13-8989-a1f586fa8ab9)

## 3. Chay script cai dat Zimbra
Tai file install_all_in_one.py (script gop toan bo cac buoc cai Zimbra).

Chay script voi quyen root hoac sudo:

```bash
sudo python3 install_all_in_one.py
```
Script se hoi ban cac thong tin nhu:
Domain (vi du: mail.example.com)

IP Server (vi du: 192.168.1.10)

![image](https://github.com/user-attachments/assets/202f02ea-e6d4-4e1e-aa4a-45909c103b24)

Chọn 7 sau đó chon 4 để SET pass user "admin'

![image](https://github.com/user-attachments/assets/dd2bc69c-9325-4531-bbef-ff452b6a48f3)

![image](https://github.com/user-attachments/assets/4ff35b26-ca5d-4d2f-bc20-1b5d66e04c8f)

![image](https://github.com/user-attachments/assets/fb88e2c9-7852-4d4b-a28c-687996eebf7a)

![image](https://github.com/user-attachments/assets/1b41821c-454f-46a4-91ad-c95a2bde7dc4)

![image](https://github.com/user-attachments/assets/07ee0211-1662-4fc9-82cf-3e662cdd227f)



Domain de tao DKIM

Domain de xin va cai SSL

Ban chi can nhap dung va theo doi tien trinh cai dat.

Neu script bao loi, kiem tra lai thong bao loi, sua roi chay lai tu buoc bi loi.
