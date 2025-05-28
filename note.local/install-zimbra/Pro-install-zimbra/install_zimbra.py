import os
import subprocess

def run_cmd(cmd):
    print(f"\n[RUNNING] {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"[ERROR] Lennh that bai: {cmd}")
        exit(1)

def main():
    # Buoc 1: Cai dat goi can thiet va tai Zimbra
    print("\nBat dau cai dat goi can thiet va tai Zimbra...")
    run_cmd("yum update -y")
    run_cmd("yum install epel-release -y")
    run_cmd("yum install bind-utils python3-pip net-tools unzip sysstat openssh-clients perl-core libaio nmap-ncat libstdc++.so.6 wget -y")

    os.makedirs("zimbra", exist_ok=True)
    run_cmd("wget https://files.zimbra.com/downloads/8.8.15_GA/zcs-8.8.15_GA_3869.RHEL7_64.20190918004220.tgz -P zimbra")
    run_cmd("tar zxpvf zimbra/zcs-8.8.15_GA_3869.RHEL7_64.20190918004220.tgz -C zimbra")

    # Buoc 2: Cau hinh he thong
    print("\nCau hinh he thong truoc khi cai dat Zimbra...")
    domain = input("Nhap domain (VD: mail.example.com): ").strip()
    ip = input("Nhap IP server: ").strip()
    hostname = domain

    # Vo hieu hoa IPv6
    with open("/etc/sysctl.conf", "a") as f:
        f.write("""
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1
""")
    run_cmd("sysctl -p")

    # Vo hieu hoa SELinux
    run_cmd("sed -i 's/SELINUX=.*/SELINUX=disabled/' /etc/selinux/config")

    # Vo hieu hoa Postfix
    run_cmd("systemctl stop postfix")
    run_cmd("yum remove postfix -y")

    # Thiet lap hostname
    run_cmd(f"hostnamectl set-hostname {hostname}")
    with open("/etc/hosts", "a") as f:
        f.write(f"{ip}\t{hostname}\t{domain.split('.')[0]}\n")

    # Buoc 3: Cai dat Zimbra
    print("\nBat dau trinh cai dat Zimbra. Lam theo huong dan hien ra tren man hinh...")
    os.chdir("zimbra/zcs-8.8.15_GA_3869.RHEL7_64.20190918004220")
    os.system("./install.sh")

    # Buoc 4: Cau hinh firewall
    print("\nCau hinh firewall...")
    run_cmd("firewall-cmd --permanent --add-port={25,80,110,143,443,465,587,993,995,5222,5223,9071,7071}/tcp")
    run_cmd("firewall-cmd --reload")

    print("\nHoan tat! Truy cap trang quan tri Zimbra tai:")
    print(f"Link: https://mail.{domain}:7071")

if __name__ == "__main__":
    main()

    #da test ok