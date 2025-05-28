# Lệnh để hiển thị thư mục rút gọn (basename của thư mục hiện tại):
## Theme01

```
echo 'PS1="\[\e[32m\][\u@\h \W]\[\e[0m\] \$ "' >> ~/.bashrc && source ~/.bashrc
```
![image](https://github.com/user-attachments/assets/7114b576-154d-4b84-b19b-28cf0a37031d)

## Theme02

```
echo 'PS1="\[\e[34m\]⏲ \t \[\e[33m\]👤 \u@\h \[\e[32m\]📁>>> \W \[\e[0m\]\$ "' >> ~/.bashrc && source ~/.bashrc
```
![image](https://github.com/user-attachments/assets/7ce72100-a106-4f2f-b39d-20b6f6622c6d)

### Giải thích:

\[\e[33m\]: Đặt màu vàng cho ngày và giờ.

\d: Hiển thị ngày (ví dụ: Thu Mar 13).

\t: Hiển thị thời gian (ví dụ: 07:22:27).

\[\e[32m\]: Đặt màu xanh lá cho tên người dùng và hostname.

\u: Hiển thị tên người dùng.

\h: Hiển thị tên máy (hostname).

\[\e[34m\]: Đặt màu xanh dương cho thư mục hiện tại.

\W: Hiển thị thư mục hiện tại.

\[\e[0m\]: Đặt lại màu về mặc định.

\n: Xuống dòng.

\$: Hiển thị ký hiệu $ (hoặc # nếu là root).

