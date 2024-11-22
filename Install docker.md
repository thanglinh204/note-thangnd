# Cài đặt Docker

## Bước 1: Cập nhật hệ thống
<p>Trước khi cài Docker, hãy cập nhật các gói của hệ thống:</p>

<div>
    <pre><code id="update">sudo apt update</code></pre>
    <button onclick="copyToClipboard('update')">Copy</button>
</div>

<div>
    <pre><code id="upgrade">sudo apt upgrade</code></pre>
    <button onclick="copyToClipboard('upgrade')">Copy</button>
</div>

## Bước 2: Cài đặt các gói cần thiết
<p>Cài đặt các gói cần thiết để Docker hoạt động ổn định:</p>

<div>
    <pre><code id="install">sudo apt install apt-transport-https ca-certificates curl software-properties-common</code></pre>
    <button onclick="copyToClipboard('install')">Copy</button>
</div>


Bước 3: #Thêm Docker GPG key
#Thêm khóa GPG của Docker vào hệ thống:

<div>
    <pre><code id="install">curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg</code></pre>
    <button onclick="copyToClipboard('install')">Copy</button>
</div>

Bước 4: #Thêm Docker repository
Thêm repository Docker vào hệ thống:




<div>
    <pre><code id="update">echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null</code></pre>
    <button onclick="copyToClipboard('update')">Copy</button>
</div>

Bước 5: #Cài đặt Docker Engine
#Cập nhật lại danh sách gói và cài Docker:

sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io

<div>
    <pre><code id="update">sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io</code></pre>
    <button onclick="copyToClipboard('update')">Copy</button>
</div>

Bước 6: #Kiểm tra cài đặt Docker
#Kiểm tra phiên bản Docker để đảm bảo cài đặt thành công:

<div>
    <pre><code id="update">docker --version</code></pre>
    <button onclick="copyToClipboard('update')">Copy</button>
</div>

2. Cài đặt Docker Compose

Bước 1: #Tải xuống Docker Compose
#Tải phiên bản Docker Compose mới nhất (ví dụ: 2.22.0) và cài đặt:

<div>
    <pre><code id="update">sudo curl -L "https://github.com/docker/compose/releases/download/2.22.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose</code></pre>
    <button onclick="copyToClipboard('update')">Copy</button>
</div>

Bước 2: #Cấp quyền thực thi cho Docker Compose
#Đặt quyền thực thi cho file Docker Compose:



<div>
    <pre><code id="update">sudo chmod +x /usr/local/bin/docker-compose</code></pre>
    <button onclick="copyToClipboard('update')">Copy</button>
</div>

Bước 3: #Kiểm tra cài đặt Docker Compose
#Kiểm tra phiên bản Docker Compose để đảm bảo cài đặt thành công:

<div>
    <pre><code id="update">docker-compose --version</code></pre>
    <button onclick="copyToClipboard('update')">Copy</button>
</div>


3. Thiết lập quyền cho user
#Để sử dụng Docker mà không cần quyền sudo, bạn có thể thêm user của mình vào nhóm docker:

<div>
    <pre><code id="update">sudo usermod -aG docker $USER</code></pre>
    <button onclick="copyToClipboard('update')">Copy</button>
</div>

#Sau đó, đăng xuất và đăng nhập lại để các thay đổi có hiệu lực.

4. Kiểm tra cài đặt
#Sau khi hoàn thành, bạn có thể kiểm tra xem Docker và Docker Compose hoạt động bằng cách tạo và chạy một container thử nghiệm:

<div>
    <pre><code id="update">docker run hello-world</code></pre>
    <button onclick="copyToClipboard('update')">Copy</button>
</div>

#Nếu bạn thấy thông báo "Hello from Docker!", điều đó có nghĩa là Docker đã được cài đặt thành công.

5. Kiểm tra Docker Compose với một tệp docker-compose.yml mẫu
#Bạn có thể tạo một file docker-compose.yml đơn giản để chạy thử Docker Compose:

    <pre><code id="update">
version: '3'
services:
  web:
    image: nginx
    ports:
      - "8080:80"</code></pre>
    <button onclick="copyToClipboard('update')">Copy</button>
