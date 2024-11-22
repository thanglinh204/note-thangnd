#Linux shell prompt: Để thay đổi màu sắc của prompt trên host Linux, bạn cần thay đổi biến PS1 trong file cấu hình shell như .bashrc, .zshrc, v.v. Ví dụ:
#Mở file .bashrc:

vi ~/.bashrc

#Tìm hoặc thêm dòng sau để thay đổi màu sắc của prompt:

PS1='\[\033[1;32m\]\u@\h:\w\$ \[\033[0m\]'

#Lưu và áp dụng:

source ~/.bashrc

#Trong lệnh trên:

	• \033[1;32m #là mã màu cho màu xanh lá cây (32).
	• \u #là tên người dùng.
	• \h #là tên host.
      \w #là thư mục hiện tại.