import subprocess

def run_cmd(cmd):
    print(f"\n[RUNNING] {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"[ERROR] Command failed: {cmd}")
        exit(1)

def copy_certificates():
    run_cmd("cp /etc/letsencrypt/live/mail.conglv.click/* /opt/zimbra/ssl/letsencrypt/")
    run_cmd("chown zimbra:zimbra /opt/zimbra/ssl/letsencrypt/*")
    run_cmd("ls -la /opt/zimbra/ssl/letsencrypt/")

def verify_and_deploy_certificates():
    run_cmd("su zimbra")
    run_cmd("cd /opt/zimbra/ssl/letsencrypt/")
    run_cmd("/opt/zimbra/bin/zmcertmgr verifycrt comm privkey.pem cert.pem combined.pem")
    print("\n✅ Kiểm tra chứng chỉ thành công!")

    run_cmd("cp /opt/zimbra/ssl/letsencrypt/privkey.pem /opt/zimbra/ssl/zimbra/commercial/commercial.key")
    run_cmd("/opt/zimbra/bin/zmcertmgr deploycrt comm cert.pem combined.pem")
    run_cmd("zmcontrol restart")

def main():
    print("\n✅ Đang sao chép chứng chỉ vào Zimbra...")
    copy_certificates()

    print("\n✅ Đang triển khai chứng chỉ vào Zimbra...")
    verify_and_deploy_certificates()

    print("\n✅ Chứng chỉ SSL đã được triển khai thành công. Chạy tiếp `config_https.py` để cấu hình chuyển hướng HTTPS.")

if __name__ == "__main__":
    main()
