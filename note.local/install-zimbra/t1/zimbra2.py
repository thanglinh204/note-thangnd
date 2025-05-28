import subprocess
import os

def run_cmd(cmd):
    print(f"\n[RUNNING] {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"[ERROR] Command failed: {cmd}")
        exit(1)

def main():
    run_cmd("yum update -y")
    run_cmd("yum install epel-release -y")
    run_cmd("yum install bind-utils python3-pip net-tools unzip sysstat openssh-clients perl-core libaio nmap-ncat libstdc++.so.6 wget -y")

    os.makedirs("zimbra", exist_ok=True)
    run_cmd("wget https://files.zimbra.com/downloads/8.8.15_GA/zcs-8.8.15_GA_3869.RHEL7_64.20190918004220.tgz -P zimbra")
    run_cmd("tar zxpvf zimbra/zcs-8.8.15_GA_3869.RHEL7_64.20190918004220.tgz -C zimbra")

    print("\n✅ Đã hoàn tất cài đặt gói cần thiết. Chạy tiếp `install_3.py` để cài đặt Zimbra.")

if __name__ == "__main__":
    main()
