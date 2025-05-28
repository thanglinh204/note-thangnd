import subprocess

def run_cmd(cmd):
    print(f"\n[RUNNING] {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"[ERROR] Command failed: {cmd}")
        exit(1)

def configure_https():
    run_cmd("su - zimbra -c '~/libexec/zmproxyconfig -e -w -o -a 8080:80:8443:443 -x https  -H `zmhostname`'")
    run_cmd("su - zimbra -c 'zmprov ms `zmhostname` zimbraReverseProxyMailMode redirect'")

def main():
    print("\n✅ Đang cấu hình chuyển hướng HTTP sang HTTPS...")
    configure_https()

    print("\n✅ Cấu hình hoàn tất. Bạn có thể truy cập vào Zimbra với HTTPS.")

if __name__ == "__main__":
    main()
