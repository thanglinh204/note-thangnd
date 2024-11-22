# Hướng dẫn thêm người dùng

## Dưới đây là các lệnh để thêm một người dùng mới và cấp quyền `sudo` cho họ:

```bash
# Thêm người dùng
sudo adduser thangnd

```bash
# Thêm quyền sudo
sudo usermod -aG sudo thangnd
