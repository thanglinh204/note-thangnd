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
    print("\n=== BUOC 1: CAU HINH SERVER ===")
    global domain, ip
    domain = input("NHAP DOMAIN (VD: mail.example.com): ").strip()
    ip = input("NHAP IP SERVER (VD: 192.168.1.10): ").strip()
    hostname = domain

    with open("/etc/sysctl.conf", "a") as f:
        f.write("""
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1
""")
    run_cmd("sysctl -p")
    run_cmd("sed -i 's/SELINUX=.*/SELINUX=disabled/' /etc/selinux/config")
    run_cmd("systemctl stop postfix")
    run_cmd("yum remove postfix -y")
    run_cmd(f"hostnamectl set-hostname {hostname}")
    with open("/etc/hosts", "a") as f:
        f.write(f"{ip}\t{hostname}\t{domain.split('.')[0]}\n")
    print("\n[HOAN THANH BUOC 1]")

def buoc_2_cai_goi():
    print("\n=== BUOC 2: CAI GOI CAN THIET ===")
    run_cmd("yum update -y")
    run_cmd("yum install epel-release -y")
    run_cmd("yum install bind-utils python3-pip net-tools unzip sysstat openssh-clients perl-core libaio nmap-ncat libstdc++.so.6 wget -y")
    os.makedirs("zimbra", exist_ok=True)
    run_cmd("wget https://files.zimbra.com/downloads/8.8.15_GA/zcs-8.8.15_GA_3869.RHEL7_64.20190918004220.tgz -P zimbra")
    run_cmd("tar zxpvf zimbra/zcs-8.8.15_GA_3869.RHEL7_64.20190918004220.tgz -C zimbra")
    print("\n[HOAN THANH BUOC 2]")

def buoc_3_cai_zimbra():
    print("\n=== BUOC 3: CAI ZIMBRA ===")
    os.chdir("zimbra/zcs-8.8.15_GA_3869.RHEL7_64.20190918004220")
    ret = os.system("./install.sh")
    if ret != 0:
        print("[LOI] Cai dat Zimbra bi loi.")
        sys.exit(1)
    os.chdir("../../")
    print("\n[HOAN THANH BUOC 3]")

def buoc_4_firewall():
    print("\n=== BUOC 4: MO FIREWALL ===")
    run_cmd("firewall-cmd --permanent --add-port={25,80,110,143,443,465,587,993,995,5222,5223,9071,7071}/tcp")
    run_cmd("firewall-cmd --reload")
    print("\n[HOAN THANH BUOC 4]")

def buoc_5_dkim():
    print("\n=== BUOC 5: TAO DKIM ===")
    domain_dkim = input("NHAP DOMAIN DE TAO DKIM (VD: example.com): ").strip()
    result = subprocess.run(f"su - zimbra -c 'zmprov gd {domain_dkim}'", shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        run_cmd(f"su - zimbra -c 'zmprov cd {domain_dkim}'")
    run_cmd(f"su - zimbra -c '/opt/zimbra/libexec/zmdkimkeyutil -a -d {domain_dkim}'")
    print("\n[HOAN THANH BUOC 5]")

def buoc_6_stop_zimbra():
    print("\n=== BUOC 6: STOP ZIMBRA ===")
    run_cmd("su - zimbra -c 'zmcontrol stop'")

def buoc_7_ssl_certbot():
    print("\n=== BUOC 7: XIN CHUNG CHI SSL ===")
    global domain
    run_cmd("yum install certbot -y")
    run_cmd(f"certbot certonly --standalone -d {domain} --non-interactive --agree-tos -m admin@{domain}")
    print("\n[HOAN THANH BUOC 7]")

def buoc_8_ssl_deploy():
    print("\n=== BUOC 8: TRIỂN KHAI SSL VAO ZIMBRA ===")
    run_cmd("su - zimbra -c 'zmcontrol start'")
    run_cmd("cd /opt/zimbra/ssl/zimbra/commercial/ || mkdir -p /opt/zimbra/ssl/zimbra/commercial/")
    run_cmd(f"cp /etc/letsencrypt/live/{domain}/privkey.pem /opt/zimbra/ssl/zimbra/commercial/commercial.key")
    run_cmd(f"cp /etc/letsencrypt/live/{domain}/cert.pem /opt/zimbra/ssl/zimbra/commercial/commercial.crt")
    run_cmd(f"wget https://letsencrypt.org/certs/isrgrootx1.pem.txt -O /opt/zimbra/ssl/zimbra/commercial/isrgrootx1.pem")
    run_cmd(f"cat /etc/letsencrypt/live/{domain}/chain.pem /opt/zimbra/ssl/zimbra/commercial/isrgrootx1.pem > /opt/zimbra/ssl/zimbra/commercial/commercial_ca.crt")
    run_cmd("chown zimbra:zimbra /opt/zimbra/ssl/zimbra/commercial/*")
    run_cmd("chmod 640 /opt/zimbra/ssl/zimbra/commercial/*")
    run_cmd("su - zimbra -c '/opt/zimbra/bin/zmcertmgr verifycrt comm /opt/zimbra/ssl/zimbra/commercial/commercial.key /opt/zimbra/ssl/zimbra/commercial/commercial.crt /opt/zimbra/ssl/zimbra/commercial/commercial_ca.crt'")
    run_cmd("su - zimbra -c '/opt/zimbra/bin/zmcertmgr deploycrt comm /opt/zimbra/ssl/zimbra/commercial/commercial.crt /opt/zimbra/ssl/zimbra/commercial/commercial_ca.crt'")
    run_cmd("su - zimbra -c 'zmcontrol restart'")
    print("\n[HOAN THANH BUOC 8]")

def buoc_9_redirect_https():
    print("\n=== BUOC 9: CAU HINH HTTPS ===")
    run_cmd("su - zimbra -c '~/libexec/zmproxyconfig -e -w -o -a 8080:80:8443:443 -x https -H `zmhostname`'")
    run_cmd("su - zimbra -c 'zmprov ms `zmhostname` zimbraReverseProxyMailMode redirect'")

def main():
    print("=== BAT DAU CAI DAT ZIMBRA ALL-IN-ONE ===")
    buoc_1_cau_hinh_server()
    buoc_2_cai_goi()
    buoc_3_cai_zimbra()
    buoc_4_firewall()
    buoc_5_dkim()
    buoc_6_stop_zimbra()
    buoc_7_ssl_certbot()
    buoc_8_ssl_deploy()
    buoc_9_redirect_https()
    print("\n=== CAI DAT HOAN TAT ===")

if __name__ == "__main__":
    main()


# TEST ->>> OK
