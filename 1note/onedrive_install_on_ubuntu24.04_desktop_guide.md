# Hướng dẫn cài đặt và khắc phục lỗi OneDrive Client trên Ubuntu 24.04 Desktop

Tài liệu này trình bày chi tiết cách cài đặt `onedrive` client (phiên bản mã nguồn của abraunegg) trên Ubuntu 24.04, bao gồm các bước khắc phục các lỗi phổ biến trong quá trình biên dịch và xác thực.

---

## Mục lục

-   [1. Giới thiệu về `onedrive` client](#1-gi%E1%BB%9Bi-thi%E1%BB%87u-v%E1%BB%81-onedrive-client)
-   [2. Chuẩn bị: Tải mã nguồn và giải nén](#2-chu%E1%BA%A9n-b%E1%BB%8B-t%E1%BA%A3i-m%C3%A3-ngu%E1%BB%93n-v%C3%A0-gi%E1%BA%A3i-n%C3%A9n)
-   [3. Cài đặt các gói phụ thuộc](#3-c%C3%A0i-%C4%91%E1%BA%B7t-c%C3%A1c-g%C3%B3i-ph%E1%BB%A5-thu%E1%BB%99c)
    -   [3.1. Cài đặt Công cụ Biên dịch và Thư viện chung](#31-c%C3%A0i-%C4%91%E1%BA%B7t-c%C3%B4ng-c%E1%BB%A5-bi%C3%AAn-d%E1%BB%8Bch-v%C3%A0-th%C6%B0-vi%E1%BB%87n-chung)
    -   [3.2. Cài đặt Dlang Compiler (DMD)](#32-c%C3%A0i-%C4%91%E1%BA%B7t-dlang-compiler-dmd)
    -   [3.3. Cài đặt Thư viện D-Bus](#33-c%C3%A0i-%C4%91%E1%BA%B7t-th%C6%B0-vi%E1%BB%87n-d-bus)
-   [4. Biên dịch và cài đặt `onedrive`](#4-bi%C3%AAn-d%E1%BB%8Bch-v%C3%A0-c%C3%A0i-%C4%91%E1%BA%B7t-onedrive)
    -   [4.1. Khắc phục lỗi quyền sở hữu (nếu có)](#41-kh%E1%BA%AFc-ph%E1%BB%A5c-l%E1%BB%97i-quy%E1%BB%81n-s%E1%BB%9F-h%E1%BB%AFu-n%E1%BA%BFu-c%C3%B3)
    -   [4.2. Chạy lệnh `configure`](#42-ch%E1%BA%A1y-l%E1%BB%87nh-configure)
    -   [4.3. Chạy lệnh `make`](#43-ch%E1%BA%A1y-l%E1%BB%87nh-make)
    -   [4.4. Chạy lệnh `make install`](#44-ch%E1%BA%A1y-l%E1%BB%87nh-make-install)
    -   [4.5. Kiểm tra phiên bản `onedrive`](#45-ki%E1%BB%83m-tra-phi%C3%AAn-b%E1%BA%A3n-onedrive)
-   [5. Xác thực tài khoản OneDrive](#5-x%C3%A1c-th%E1%BB%B1c-t%C3%A0i-kho%E1%BA%A3n-onedrive)
    -   [5.1. Khắc phục lỗi `AADSTS500144` (Client ID)](#51-kh%E1%BA%AFc-ph%E1%BB%A5c-l%E1%BB%97i-aadsts500144-client-id)
-   [6. Thiết lập dịch vụ Systemd cho `onedrive` (Chạy nền tự động)](#6-thi%E1%BA%BFt-l%E1%BA%ADp-d%E1%BB%8Bch-v%E1%BB%A5-systemd-cho-onedrive-ch%E1%BA%A1y-n%E1%BB%81n-t%E1%BB%B1-%C4%91%E1%BB%99ng)
    -   [6.1. Khắc phục lỗi `Unrecognized option --install-user-service`](#61-kh%E1%BA%AFc-ph%E1%BB%A5c-l%E1%BB%97i-unrecognized-option---install-user-service)
-   [7. Cấu trúc thư mục OneDrive sau khi đồng bộ hóa](#7-c%E1%BA%A5u-tr%C3%BAc-th%C6%B0-m%E1%BB%A5c-onedrive-sau-khi-%C4%91%E1%BB%93ng-b%E1%BB%99-h%C3%B3a)
-   [8. Nguồn tham khảo](#8-ngu%E1%BB%93n-tham-kh%E1%BA%A3o)

---

## 1. Giới thiệu về `onedrive` client

`onedrive` client là một ứng dụng mã nguồn mở không chính thức nhưng rất mạnh mẽ, cho phép bạn đồng bộ hóa dữ liệu giữa tài khoản Microsoft OneDrive và hệ thống Linux của bạn. Nó hỗ trợ đồng bộ hóa hai chiều, cho phép bạn làm việc với các file OneDrive trực tiếp trên máy tính và tự động cập nhật lên đám mây.

## 2. Chuẩn bị: Tải mã nguồn và giải nén

Trong hướng dẫn này, chúng ta sẽ biên dịch `onedrive` từ mã nguồn để đảm bảo có phiên bản mới nhất.

1.  **Mở Terminal:** Nhấn `Ctrl + Alt + T`.
2.  **Chuyển đến thư mục `Downloads`:**
    ```bash
    cd ~/Downloads
    ```
3.  **Tải mã nguồn `onedrive`:** Truy cập trang [GitHub của abraunegg/onedrive Releases](https://github.com/abraunegg/onedrive/releases) để tìm phiên bản ZIP mới nhất (ví dụ: `onedrive-2.5.6.zip`). Sau đó, sử dụng `wget` để tải về.

    ```bash
    # Lấy phiên bản mới nhất tự động (có thể cần cập nhật URL nếu cấu trúc thay đổi)
    VERSION=$(curl -s [https://api.github.com/repos/abraunegg/onedrive/releases/latest](https://api.github.com/repos/abraunegg/onedrive/releases/latest) | grep -oP '"tag_name": "\K(.*)(?=")')
    wget "[https://github.com/abraunegg/onedrive/archive/refs/tags/$VERSION.zip](https://github.com/abraunegg/onedrive/archive/refs/tags/$VERSION.zip)" -O onedrive.zip
    ```
4.  **Giải nén file ZIP:**
    ```bash
    sudo apt install unzip -y # Cài đặt unzip nếu chưa có
    unzip onedrive.zip
    ```
    Lệnh này sẽ giải nén mã nguồn vào một thư mục mới có tên dạng `onedrive-X.Y.Z/` (ví dụ: `onedrive-2.5.6/`).
5.  **Chuyển vào thư mục mã nguồn đã giải nén:**
    ```bash
    cd onedrive-$VERSION/
    ```
    Dấu nhắc lệnh của bạn bây giờ sẽ là `thangnd@Laptop-Nitro5:~/Downloads/onedrive-X.Y.Z$`.

## 3. Cài đặt các gói phụ thuộc

`onedrive` yêu cầu một số công cụ và thư viện để biên dịch và hoạt động.

### 3.1. Cài đặt Công cụ Biên dịch và Thư viện chung

```bash
sudo apt update
sudo apt install build-essential libcurl4-openssl-dev libsqlite3-dev libnotify-dev libfuse-dev -y
