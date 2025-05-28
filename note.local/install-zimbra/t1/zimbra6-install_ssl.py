import subprocess

def run_cmd(cmd):
    print(f"\n[RUNNING] {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"[ERROR] Command failed: {cmd}")
        exit(1)

def install_certbot():
    run_cmd("sudo yum install certbot -y")

def obtain_ssl_cert(domain):
    run_cmd(f"certbot certonly --standalone -d {domain}")

def download_and_merge_certificates(domain):
    run_cmd(f"cd /etc/letsencrypt/live/{domain}")
    run_cmd("wget https://letsencrypt.org/certs/isrgrootx1.pem.txt")
    run_cmd("wget https://letsencrypt.org/certs/letsencryptauthorityx3.pem.txt")
    run_cmd("cat isrgrootx1.pem.txt letsencryptauthorityx3.pem.txt chain.pem > combined.pem")

def main():
    domain = input("Nhập domain để cài đặt SSL (VD: mail.example.com): ").strip()
    
    print("\n✅ Cài đặt Certbot...")
    install_certbot()

    print(f"\n✅ Đang xin chứng chỉ SSL cho {domain} từ Let’s Encrypt...")
    obtain_ssl_cert(domain)

    print("\n✅ Tải và kết hợp chứng chỉ...")
    download_and_merge_certificates(domain)

    print("\n✅ Đã cài đặt chứng chỉ SSL. Chạy tiếp `install_zimbra_ssl.py` để triển khai chứng chỉ vào Zimbra.")

if __name__ == "__main__":
    main()
