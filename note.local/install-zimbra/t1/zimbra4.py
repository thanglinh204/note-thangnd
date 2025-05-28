import subprocess

def run_cmd(cmd):
    print(f"\n[RUNNING] {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"[ERROR] Command failed: {cmd}")
        exit(1)

def main():
    run_cmd("firewall-cmd --permanent --add-port={25,80,110,143,443,465,587,993,995,5222,5223,9071,7071}/tcp")
    run_cmd("firewall-cmd --reload")

    print("\n✅ Hoàn tất! Truy cập trang quản trị Zimbra tại:")
    print("👉 https://mail.tenmiencuaban:7071")

if __name__ == "__main__":
    main()
