Hướng dẫn cài đặt và khắc phục lỗi OneDrive Client trên Ubuntu 24.04 Desktop
Tài liệu này trình bày chi tiết cách cài đặt onedrive client (phiên bản mã nguồn của abraunegg) trên Ubuntu 24.04, bao gồm các bước khắc phục các lỗi phổ biến trong quá trình biên dịch và xác thực.

Mục lục
Giới thiệu về onedrive client

Chuẩn bị: Tải mã nguồn và giải nén

Cài đặt các gói phụ thuộc
3.1. Cài đặt Công cụ Biên dịch và Thư viện chung
3.2. Cài đặt Dlang Compiler (DMD)
3.3. Cài đặt Thư viện D-Bus

Biên dịch và cài đặt onedrive
4.1. Khắc phục lỗi quyền sở hữu (nếu có)
4.2. Chạy lệnh configure
4.3. Chạy lệnh make
4.4. Chạy lệnh make install
4.5. Kiểm tra phiên bản onedrive

Xác thực tài khoản OneDrive
5.1. Khắc phục lỗi AADSTS500144 (Client ID)

Thiết lập dịch vụ Systemd cho onedrive (Chạy nền tự động)
6.1. Khắc phục lỗi Unrecognized option --install-user-service

Cấu trúc thư mục OneDrive sau khi đồng bộ hóa

Nguồn tham khảo

1. Giới thiệu về onedrive client
onedrive client là một ứng dụng mã nguồn mở không chính thức nhưng rất mạnh mẽ, cho phép bạn đồng bộ hóa dữ liệu giữa tài khoản Microsoft OneDrive và hệ thống Linux của bạn. Nó hỗ trợ đồng bộ hóa hai chiều, cho phép bạn làm việc với các file OneDrive trực tiếp trên máy tính và tự động cập nhật lên đám mây.

2. Chuẩn bị: Tải mã nguồn và giải nén
Trong hướng dẫn này, chúng ta sẽ biên dịch onedrive từ mã nguồn để đảm bảo có phiên bản mới nhất.

Mở Terminal: Nhấn Ctrl + Alt + T.

Chuyển đến thư mục Downloads:

cd ~/Downloads

Tải mã nguồn onedrive: Truy cập trang GitHub của abraunegg/onedrive Releases để tìm phiên bản ZIP mới nhất (ví dụ: onedrive-2.5.6.zip). Sau đó, sử dụng wget để tải về.

# Lấy phiên bản mới nhất tự động (có thể cần cập nhật URL nếu cấu trúc thay đổi)
VERSION=$(curl -s https://api.github.com/repos/abraunegg/onedrive/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")')
wget "https://github.com/abraunegg/onedrive/archive/refs/tags/$VERSION.zip" -O onedrive.zip

Giải nén file ZIP:

sudo apt install unzip -y # Cài đặt unzip nếu chưa có
unzip onedrive.zip

Lệnh này sẽ giải nén mã nguồn vào một thư mục mới có tên dạng onedrive-X.Y.Z/ (ví dụ: onedrive-2.5.6/).

Chuyển vào thư mục mã nguồn đã giải nén:

cd onedrive-$VERSION/

Dấu nhắc lệnh của bạn bây giờ sẽ là thangnd@Laptop-Nitro5:~/Downloads/onedrive-X.Y.Z$.

3. Cài đặt các gói phụ thuộc
onedrive yêu cầu một số công cụ và thư viện để biên dịch và hoạt động.

3.1. Cài đặt Công cụ Biên dịch và Thư viện chung
sudo apt update
sudo apt install build-essential libcurl4-openssl-dev libsqlite3-dev libnotify-dev libfuse-dev -y

build-essential: Gói chứa các công cụ biên dịch cơ bản (gcc, g++, make, v.v.).

libcurl4-openssl-dev: Thư viện cho các yêu cầu HTTP/HTTPS.

libsqlite3-dev: Thư viện cơ sở dữ liệu SQLite.

libnotify-dev: Thư viện cho thông báo desktop.

libfuse-dev: Thư viện cần thiết cho các ứng dụng liên quan đến hệ thống tập tin ảo (FUSE).

3.2. Cài đặt Dlang Compiler (DMD)
onedrive được viết bằng ngôn ngữ D, vì vậy cần một trình biên dịch D.

Phương án khuyến nghị: Cài đặt DMD bằng Snap

sudo snap install dmd --classic

--classic: Đảm bảo cài đặt ở chế độ tương thích đầy đủ cho các công cụ phát triển.

Kiểm tra cài đặt DMD:
Sau khi cài đặt xong, hãy kiểm tra phiên bản DMD:

dmd --version

Nếu hiển thị thông tin phiên bản, tức là DMD đã được cài đặt thành công.

3.3. Cài đặt Thư viện D-Bus
D-Bus là một hệ thống giao tiếp giữa các tiến trình. onedrive cần các file phát triển của D-Bus.

sudo apt install libdbus-1-dev -y

4. Biên dịch và cài đặt onedrive
Bây giờ bạn đã có tất cả các phụ thuộc, chúng ta sẽ tiến hành biên dịch mã nguồn.

4.1. Khắc phục lỗi quyền sở hữu (nếu có)
Nếu bạn đã giải nén hoặc thao tác với file bằng quyền root trước đó (dấu nhắc lệnh [root@Laptop-Nitro5 ~]), các file có thể thuộc sở hữu của root, gây ra lỗi "Permission denied" trong quá trình configure.

Lỗi nhận biết: mv: cannot move './.config6qXpi2/out' to 'contrib/pacman/PKGBUILD': Permission denied hoặc tương tự.

Cách khắc phục:

Thoát khỏi thư mục mã nguồn:

cd ..

Bạn sẽ ở trong thư mục ~/Downloads/.

Thay đổi quyền sở hữu thư mục mã nguồn về người dùng của bạn: Thay thế onedrive-X.Y.Z bằng tên thư mục thực tế của bạn (ví dụ: onedrive-2.5.6).

sudo chown -R $USER:$USER onedrive-X.Y.Z/

Trở lại thư mục mã nguồn:

cd onedrive-X.Y.Z/

4.2. Chạy lệnh configure
Lệnh này kiểm tra các phụ thuộc và tạo Makefile để biên dịch.

./configure

Nếu không có lỗi, bạn sẽ thấy thông báo configure: creating Makefile và configure: creating .config.status.

4.3. Chạy lệnh make
Lệnh này sẽ biên dịch mã nguồn thành file thực thi.

make

Quá trình này có thể mất vài phút. Nếu có lỗi, hãy kiểm tra lại các gói phụ thuộc và cài đặt DMD.

4.4. Chạy lệnh make install
Sau khi biên dịch thành công, lệnh này sẽ cài đặt file thực thi onedrive vào /usr/local/bin/.

sudo make install

4.5. Kiểm tra phiên bản onedrive
Xác nhận onedrive đã được cài đặt và có thể chạy được.

onedrive --version

Bạn sẽ thấy onedrive vX.Y.Z (phiên bản hiện tại của bạn).

5. Xác thực tài khoản OneDrive
Đây là bước quan trọng để cấp quyền cho onedrive client truy cập tài khoản của bạn.

Chạy lệnh xác thực:

onedrive

Copy URL đầu tiên từ Terminal: Bạn sẽ thấy một URL rất dài bắt đầu bằng https://login.microsoftonline.com/...authorize?client_id=.... Copy toàn bộ URL này.

Mở trình duyệt web: Dán URL đã copy vào thanh địa chỉ của trình duyệt và nhấn Enter.

Đăng nhập và cấp quyền: Đăng nhập vào tài khoản Microsoft OneDrive của bạn và chấp nhận yêu cầu cấp quyền.

Lấy URL phản hồi (Response URI): Sau khi cấp quyền, trình duyệt sẽ chuyển hướng đến một trang (thường là trống hoặc báo lỗi không tìm thấy trang). Copy toàn bộ URL từ thanh địa chỉ của trình duyệt ở trang này.

Dán URL vào Terminal: Quay lại Terminal, dán toàn bộ "response URI" bạn vừa copy vào vị trí con trỏ đang nhấp nháy sau Enter the response uri from your browser: và nhấn Enter.

Nếu thành công, bạn sẽ thấy thông báo The application has been successfully authorised, but no extra command options have been specified.

5.1. Khắc phục lỗi AADSTS500144 (Client ID)
Lỗi nhận biết: AADSTS500144: The request body must contain the following parameter: 'client_id'.

Lỗi này xảy ra khi Client ID mặc định của onedrive client gặp vấn đề hoặc không được truyền chính xác. Giải pháp là tạo và sử dụng Client ID/Secret tùy chỉnh của riêng bạn.

Các bước tạo Client ID/Secret:

Truy cập Azure Portal: https://portal.azure.com/ (Đăng nhập bằng tài khoản Microsoft của bạn).

Tìm "Microsoft Entra ID" (trước đây là Azure Active Directory).

Trong "Microsoft Entra ID", chọn "App registrations" -> "+ New registration".

Name: Đặt tên dễ nhớ (ví dụ: OneDrive-Linux-Client-Custom).

Supported account types: Chọn Accounts in any organizational directory (Any Microsoft Entra ID tenant - Multitenant) and personal Microsoft accounts (e.g. Skype, Xbox).

Redirect URI:

Chọn nền tảng Public client/native (mobile & desktop).

Thêm các URI sau:

https://login.microsoftonline.com/common/oauth2/nativeclient

http://localhost

http://localhost:8080 (Nếu onedrive client sử dụng cổng này)

Lưu các thay đổi.

Lấy Client ID và Secret:

Trên trang tổng quan ứng dụng của bạn, copy "Application (client) ID". Đây là client_id của bạn.

Vào mục "Certificates & secrets" -> "+ New client secret". Đặt mô tả và thời hạn. Copy "Value" của secret này (chỉ hiển thị một lần). Đây là client_secret của bạn.

Cấu hình onedrive với Client ID/Secret tùy chỉnh:

Tạo hoặc chỉnh sửa file cấu hình onedrive:

nano ~/.config/onedrive/config

Thêm/chỉnh sửa các dòng sau:

client_id = "YOUR_APPLICATION_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET_VALUE"

Lưu file (Ctrl+X, Y, Enter).

Xóa thông tin xác thực cũ (nếu có):

onedrive --force-unlink

Chạy lại onedrive để xác thực lại (như Bước 5 ở trên). Nó sẽ sử dụng Client ID/Secret mới của bạn.

6. Thiết lập dịch vụ Systemd cho onedrive (Chạy nền tự động)
Sau khi xác thực, bạn cần cấu hình onedrive để chạy tự động trong nền như một dịch vụ.

6.1. Khắc phục lỗi Unrecognized option --install-user-service
Lỗi nhận biết: Unrecognized option --install-user-service

Nếu lệnh onedrive --install-user-service không hoạt động, có thể phiên bản bạn biên dịch không hỗ trợ tùy chọn này hoặc có lỗi. Chúng ta sẽ tạo file dịch vụ Systemd thủ công.

Dừng dịch vụ onedrive hiện tại (nếu đang chạy):

systemctl --user stop onedrive.service

Tạo thư mục dịch vụ Systemd cho người dùng:

mkdir -p ~/.config/systemd/user

Tạo file dịch vụ onedrive.service:

nano ~/.config/systemd/user/onedrive.service

Dán nội dung sau vào file:

[Unit]
Description=OneDrive Sync Client
After=network-online.target

[Service]
ExecStart=/usr/local/bin/onedrive --monitor --confdir=%h/.config/onedrive
Restart=on-failure
RestartSec=30
Environment=PATH=/usr/local/bin:/usr/bin:/bin:/snap/bin

[Install]
WantedBy=default.target

Lưu file (Ctrl+X, Y, Enter).

Tải lại cấu hình Systemd:

systemctl --user daemon-reload

Kích hoạt và khởi động dịch vụ:

systemctl --user enable onedrive.service
systemctl --user start onedrive.service

Kiểm tra trạng thái của dịch vụ:

systemctl --user status onedrive.service

Bạn sẽ thấy Active: active (running) và các dòng nhật ký đồng bộ hóa.

7. Cấu trúc thư mục OneDrive sau khi đồng bộ hóa
Sau khi dịch vụ onedrive chạy thành công, nó sẽ tạo một thư mục để đồng bộ hóa file của bạn.

Vị trí mặc định: Thư mục OneDrive sẽ được tạo trong thư mục Home của bạn.

/home/ten_nguoi_dung/
└── OneDrive/  <-- Đây là thư mục OneDrive của bạn
    ├── Documents/
    │   └── MyWork.docx
    ├── Pictures/
    │   └── vacation.jpg
    └── My_Projects/
        └── project_plan.pptx

Truy cập:

Mở ứng dụng "Files" (Trình quản lý tệp tin) trên Ubuntu.

Chọn "Home" (biểu tượng ngôi nhà) ở thanh bên trái.

Bạn sẽ thấy thư mục OneDrive trong danh sách.

Mọi thay đổi (thêm, xóa, sửa) trong thư mục ~/OneDrive này sẽ được tự động đồng bộ hóa với tài khoản OneDrive trên đám mây của bạn và ngược lại.

8. Nguồn tham khảo
Abraunegg/onedrive GitHub Repository

Abraunegg/onedrive Wiki: Installation from Source

Abraunegg/onedrive Wiki: Microsoft OneDrive Configuration (for custom Client ID)

Dlang Installation on Linux

Systemd User Services Tutorial

Microsoft identity platform and OAuth 2.0 authorization code flow
