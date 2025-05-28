import os
import subprocess

def run_cmd(cmd):
    print(f"\n[RUNNING] {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"[ERROR] Command failed: {cmd}")
        exit(1)

def main():
    domain = input("Nhập domain (VD: mail.example.com): ").strip()
    ip = input("Nhập IP server: ").strip()
    hostname = domain

    # Disable IPv6
    with open("/etc/sysctl.conf", "a") as f:
        f.write("""
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1
""")
    run_cmd("sysctl -p")

    # Disable SELinux
    run_cmd("sed -i 's/SELINUX=.*/SELINUX=disabled/' /etc/selinux/config")

    # Disable Postfix
    run_cmd("systemctl stop postfix")
    run_cmd("yum remove postfix -y")

    # Set hostname
    run_cmd(f"hostnamectl set-hostname {hostname}")
    with open("/etc/hosts", "a") as f:
        f.write(f"{ip}\t{hostname}\t{domain.split('.')[0]}\n")

    print("\n✅ Đã cấu hình xong bước 1. Hãy chạy tiếp `install_2.py`")

if __name__ == "__main__":
    main()
