import os
import subprocess

def run_cmd(cmd, as_zimbra=False):
    print(f"\n[RUNNING] {cmd}")
    if as_zimbra:
        cmd = f"su - zimbra -c '{cmd}'"
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"[ERROR] Lennh that bai: {cmd}")
        exit(1)
    return result

def main():
    # Lay thong tin domain tu nguoi dung
    domain = input("Nhap domain (VD: mail.example.com): ").strip()

    # Buoc 1: Dung dich vu Zimbra
    print("\nDung dich vu Zimbra...")
    run_cmd("zmcontrol stop", as_zimbra=True)

    # Buoc 2: Cai dat Certbot va dang ky chung chi SSL
    print("\nCai dat Certbot...")
    run_cmd("yum install certbot -y")
    
    print("\nDang ky chung chi SSL voi Let's Encrypt...")
    run_cmd(f"certbot certonly --standalone -d {domain}")

    # Buoc 3: Xu ly chung chi
    print("\nTai cac file chung chi can thiet...")
    os.chdir(f"/etc/letsencrypt/live/{domain}")
    run_cmd("wget https://letsencrypt.org/certs/isrgrootx1.pem.txt")
    run_cmd("wget https://letsencrypt.org/certs/letsencryptauthorityx3.pem.txt")
    
    print("\nGhep cac file chung chi...")
    run_cmd("cat isrgrootx1.pem.txt letsencryptauthorityx3.pem.txt chain.pem > combined.pem")

    # Buoc 4: Tao thu muc letsencrypt va sao chep chung chi
    print("\nTao thu muc letsencrypt trong /opt/zimbra/ssl/...")
    run_cmd("mkdir -p /opt/zimbra/ssl/letsencrypt")

    print("\nSao chep chung chi den thu muc Zimbra...")
    run_cmd(f"cp /etc/letsencrypt/live/{domain}/* /opt/zimbra/ssl/letsencrypt/")
    run_cmd("chown zimbra:zimbra /opt/zimbra/ssl/letsencrypt/*")

    # Buoc 5: Xac minh va cai dat chung chi
    print("\nXac minh chung chi...")
    os.chdir("/opt/zimbra/ssl/letsencrypt/")
    run_cmd("/opt/zimbra/bin/zmcertmgr verifycrt comm privkey.pem cert.pem combined.pem", as_zimbra=True)

    print("\nCai dat chung chi vao Zimbra...")
    run_cmd("cp /opt/zimbra/ssl/letsencrypt/privkey.pem /opt/zimbra/ssl/zimbra/commercial/commercial.key")
    run_cmd("/opt/zimbra/bin/zmcertmgr deploycrt comm cert.pem combined.pem", as_zimbra=True)

    # Buoc 6: Khoi dong lai Zimbra
    print("\nKhoi dong lai dich vu Zimbra...")
    run_cmd("zmcontrol restart", as_zimbra=True)

    # Buoc 7: Cau hinh chuyen huong HTTPS
    print("\nCau hinh port 80 voi chuyen huong HTTPS...")
    hostname = subprocess.getoutput("zmhostname")
    run_cmd(f"~/libexec/zmproxyconfig -e -w -o -a 8080:80:8443:443 -x https -H {hostname}", as_zimbra=True)
    run_cmd(f"zmprov ms {hostname} zimbraReverseProxyMailMode redirect", as_zimbra=True)

    print("\nHoan tat! Truy cap trang quan tri Zimbra tai:")
    print(f"Link: https://{domain}:7071")

if __name__ == "__main__":
    main()