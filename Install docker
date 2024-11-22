Dưới đây là nội dung được chuyển đổi sang Markdown với các đề mục sử dụng #, và các khối code có thể copy dễ dàng khi hiển thị trên GitHub:

markdown
Sao chép mã
# Cài đặt Docker

## Bước 1: Cập nhật hệ thống
Trước khi cài Docker, hãy cập nhật các gói của hệ thống:

```bash
sudo apt update
sudo apt upgrade
Bước 2: Cài đặt các gói cần thiết
Cài đặt các gói cần thiết để Docker hoạt động ổn định:

bash
Sao chép mã
sudo apt install apt-transport-https ca-certificates curl software-properties-common
Bước 3: Thêm Docker GPG key
Thêm khóa GPG của Docker vào hệ thống:

bash
Sao chép mã
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
Bước 4: Thêm Docker repository
Thêm repository Docker vào hệ thống:

bash
Sao chép mã
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
Bước 5: Cài đặt Docker Engine
Cập nhật lại danh sách gói và cài Docker:

bash
Sao chép mã
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io
Bước 6: Kiểm tra cài đặt Docker
Kiểm tra phiên bản Docker để đảm bảo cài đặt thành công:

bash
Sao chép mã
docker --version
Cài đặt Docker Compose
Bước 1: Tải xuống Docker Compose
Tải phiên bản Docker Compose mới nhất (ví dụ: 2.22.0) và cài đặt:

bash
Sao chép mã
sudo curl -L "https://github.com/docker/compose/releases/download/2.22.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
Bước 2: Cấp quyền thực thi cho Docker Compose
Đặt quyền thực thi cho file Docker Compose:

bash
Sao chép mã
sudo chmod +x /usr/local/bin/docker-compose
Bước 3: Kiểm tra cài đặt Docker Compose
Kiểm tra phiên bản Docker Compose để đảm bảo cài đặt thành công:

bash
Sao chép mã
docker-compose --version
Thiết lập quyền cho user
Để sử dụng Docker mà không cần quyền sudo, bạn có thể thêm user của mình vào nhóm docker:

bash
Sao chép mã
sudo usermod -aG docker $USER
Sau đó, đăng xuất và đăng nhập lại để các thay đổi có hiệu lực.

Kiểm tra cài đặt
Sau khi hoàn thành, bạn có thể kiểm tra xem Docker và Docker Compose hoạt động bằng cách tạo và chạy một container thử nghiệm:

bash
Sao chép mã
docker run hello-world
Nếu bạn thấy thông báo "Hello from Docker!", điều đó có nghĩa là Docker đã được cài đặt thành công.

Kiểm tra Docker Compose với một tệp docker-compose.yml mẫu
Bạn có thể tạo một file docker-compose.yml đơn giản để chạy thử Docker Compose:

yml
Sao chép mã
version: '3'
services:
  web:
    image: nginx
    ports:
      - "8080:80"
