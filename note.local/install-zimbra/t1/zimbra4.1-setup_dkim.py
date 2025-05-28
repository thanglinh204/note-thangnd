import subprocess

def run_cmd(cmd):
    print(f"\n[RUNNING] {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"[ERROR] Command failed: {cmd}")
        exit(1)

def check_domain_in_zimbra(domain):
    # Kiểm tra tên miền đã được cấu hình trong Zimbra
    result = subprocess.run(f"su - zimbra -c 'zmprov gd {domain}'", shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"[INFO] Tên miền {domain} chưa được cấu hình. Đang thêm vào...")
        subprocess.run(f"su - zimbra -c 'zmprov cd {domain}'", shell=True)
        print(f"✅ Đã thêm tên miền {domain} vào Zimbra.")
    else:
        print(f"✅ Tên miền {domain} đã có trong Zimbra.")

def generate_dkim(domain):
    # Tạo DKIM cho domain
    run_cmd(f"su - zimbra -c '/opt/zimbra/libexec/zmdkimkeyutil -a -d {domain}'")

def main():
    domain = input("Nhập tên miền để tạo DKIM (VD: conglv.click): ").strip()

    print("\n✅ Kiểm tra và thêm tên miền vào Zimbra nếu cần...")
    check_domain_in_zimbra(domain)

    print("\n✅ Đang tạo DKIM cho tên miền...")
    generate_dkim(domain)

    print("\n✅ DKIM đã được tạo thành công cho tên miền.")
    print(f"🎯 Công khai bản ghi DKIM vào DNS với selector vừa tạo.\n")

if __name__ == "__main__":
    main()
