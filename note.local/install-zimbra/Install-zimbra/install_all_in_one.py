import os
import subprocess
import sys

def run_cmd(cmd):
    print(f"\n[THUC HIEN] {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"[LOI] Lenh bi loi: {cmd}")
        sys.exit(1)

def buoc_1_cau_hinh_server():
    print("\n=== BƯỚC 1: CAU HINH SERVER ===")
    domain = input("NHAP DOMAIN (VD: mail.example.com): ").strip()
    ip = input("NHAP IP SERVER (VD: 192.168.1.10): ").strip()
    hostname = domain

    # Tat IPv6
    with open("/etc/sysctl.conf", "a") as f:
        f.write("""
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1
""")
    run_cmd("sysctl -p")

    # Tat SELinux
    run_cmd("sed -i 's/SELINUX=.*/SELINUX=disabled/' /etc/selinux/config")

    # Tat va go bo postfix
    run_cmd("systemctl stop postfix")
    run_cmd("yum remove postfix -y")

    # Cau hinh hostname
    run_cmd(f"hostnamectl set-hostname {hostname}")
    with open("/etc/hosts", "a") as f:
        f.write(f"{ip}\t{hostname}\t{domain.split('.')[0]}\n")

    print("\n[HOAN THANH BUOC 1]")

def buoc_2_cai_dat_goi_can_thiet():
    print("\n=== BƯỚC 2: CAI DAT GOI CAN THIET VA TAI ZIMBRA ===")
    run_cmd("yum update -y")
    run_cmd("yum install epel-release -y")
    run_cmd("yum install bind-utils python3-pip net-tools unzip sysstat openssh-clients perl-core libaio nmap-ncat libstdc++.so.6 wget -y")

    os.makedirs("zimbra", exist_ok=True)
    run_cmd("wget https://files.zimbra.com/downloads/8.8.15_GA/zcs-8.8.15_GA_3869.RHEL7_64.20190918004220.tgz -P zimbra")
    run_cmd("tar zxpvf zimbra/zcs-8.8.15_GA_3869.RHEL7_64.20190918004220.tgz -C zimbra")

    print("\n[HOAN THANH BUOC 2]")

def buoc_3_cai_dat_zimbra():
    print("\n=== BƯỚC 3: CAI DAT ZIMBRA ===")
    os.chdir("zimbra/zcs-8.8.15_GA_3869.RHEL7_64.20190918004220")
    print("\n[MOI BAN THEO DOI VA LAM THEO HUONG DAN TREN MAN HINH]")
    ret = os.system("./install.sh")
    if ret != 0:
        print("[LOI] Cai dat Zimbra bi loi.")
        sys.exit(1)
    os.chdir("../../")
    print("\n[HOAN THANH BUOC 3]")

def buoc_4_mo_firewall():
    print("\n=== BƯỚC 4: MO FIREWALL CHO ZIMBRA ===")
    run_cmd("firewall-cmd --permanent --add-port={25,80,110,143,443,465,587,993,995,5222,5223,9071,7071}/tcp")
    run_cmd("firewall-cmd --reload")
    print("\n[HOAN THANH BUOC 4]")

def buoc_5_tao_dkim():
    print("\n=== BƯỚC 5: TAO DKIM CHO DOMAIN ===")
    domain = input("NHAP DOMAIN DE TAO DKIM (VD: conglv.click): ").strip()

    # Kiem tra domain da co trong Zimbra chua
    print("\n[KIEM TRA VA THEM DOMAIN VAO ZIMBRA NEU CAN]")
    result = subprocess.run(f"su - zimbra -c 'zmprov gd {domain}'", shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"[INFO] Domain {domain} chua duoc them, dang them vao...")
        run_cmd(f"su - zimbra -c 'zmprov cd {domain}'")
        print(f"[OK] Da them domain {domain}.")
    else:
        print(f"[OK] Domain {domain} da co trong Zimbra.")

    # Tao DKIM
    print("\n[TAO DKIM]")
    run_cmd(f"su - zimbra -c '/opt/zimbra/libexec/zmdkimkeyutil -a -d {domain}'")

    print(f"\n[HOAN THANH BUOC 5] Ban can cong khai ban ghi DKIM trong DNS voi selector vua tao.\n")

def buoc_6_dung_zimbra_de_cai_ssl():
    print("\n=== BƯỚC 6: DUNG DICH VU ZIMBRA DE CAI SSL ===")
    run_cmd("su - zimbra -c 'zmcontrol stop'")
    print("\n[HOAN THANH BUOC 6]")

def buoc_7_cai_dat_ssl():
    print("\n=== BƯỚC 7: CAI DAT VA XIN CHUNG CHI SSL ===")
    domain = input("NHAP DOMAIN DE CAI SSL (VD: mail.conglv.click): ").strip()

    print("\n[CAI DAT CERTBOT]")
    run_cmd("yum install certbot -y")

    print(f"\n[HOI CERTBOT CHUNG CHI SSL CHO {domain}]")
    run_cmd(f"certbot certonly --standalone -d {domain}")

    print("\n[TAI VA KET HOP CHUNG CHI]")
    run_cmd(f"cd /etc/letsencrypt/live/{domain} && wget https://letsencrypt.org/certs/isrgrootx1.pem.txt")
    run_cmd(f"cd /etc/letsencrypt/live/{domain} && wget https://letsencrypt.org/certs/letsencryptauthorityx3.pem.txt")
    run_cmd(f"cd /etc/letsencrypt/live/{domain} && cat isrgrootx1.pem.txt letsencryptauthorityx3.pem.txt chain.pem > combined.pem")

    print("\n[HOAN THANH BUOC 7]")

def buoc_8_trien_khai_ssl_vao_zimbra():
    print("\n=== BƯỚC 8: TRIEN KHAI CHUNG CHI SSL VAO ZIMBRA ===")
    domain = input("NHAP LAI DOMAIN DE XAC NHAN (VD: mail.conglv.click): ").strip()

    print("\n[SAO CHEP CHUNG CHI VAO THU MUC ZIMBRA]")
    run_cmd(f"cp /etc/letsencrypt/live/{domain}/* /opt/zimbra/ssl/letsencrypt/")
    run_cmd("chown zimbra:zimbra /opt/zimbra/ssl/letsencrypt/*")
    run_cmd("ls -la /opt/zimbra/ssl/letsencrypt/")

    print("\n[KIEM TRA VA TRIEN KHAI CHUNG CHI]")
    run_cmd("su - zimbra -c '/opt/zimbra/bin/zmcertmgr verifycrt comm /opt/zimbra/ssl/letsencrypt/privkey.pem /opt/zimbra/ssl/letsencrypt/cert.pem /opt/zimbra/ssl/letsencrypt/combined.pem'")
    print("[KIEM TRA CHUNG CHI THANH CONG!]")

    run_cmd("cp /opt/zimbra/ssl/letsencrypt/privkey.pem /opt/zimbra/ssl/zimbra/commercial/commercial.key")
    run_cmd("su - zimbra -c '/opt/zimbra/bin/zmcertmgr deploycrt comm /opt/zimbra/ssl/letsencrypt/cert.pem /opt/zimbra/ssl/letsencrypt/combined.pem'")
    run_cmd("su - zimbra -c 'zmcontrol restart'")

    print("\n[HOAN THANH BUOC 8]")

def buoc_9_cau_hinh_https():
    print("\n=== BƯỚC 9: CAU HINH CHUYEN HUONG HTTPS ===")
    run_cmd("su - zimbra -c '~/libexec/zmproxyconfig -e -w -o -a 8080:80:8443:443 -x https -H `zmhostname`'")
    run_cmd("su - zimbra -c 'zmprov ms `zmhostname` zimbraReverseProxyMailMode redirect'")
    print("\n[HOAN THANH BUOC 9 - HOAN TAT CAU HINH]")

def main():
    print("=== BAT DAU QUY TRINH CAI DAT ZIMBRA TOAN BO TRONG 1 SCRIPT ===")
    buoc_1_cau_hinh_server()
    buoc_2_cai_dat_goi_can_thiet()
    buoc_3_cai_dat_zimbra()
    buoc_4_mo_firewall()
    buoc_5_tao_dkim()
    buoc_6_dung_zimbra_de_cai_ssl()
    buoc_7_cai_dat_ssl()
    buoc_8_trien_khai_ssl_vao_zimbra()
    buoc_9_cau_hinh_https()
    print("\n=== QUY TRINH CAI DAT ZIMBRA HOAN TAT THANH CONG ===")

if __name__ == "__main__":
    main()
