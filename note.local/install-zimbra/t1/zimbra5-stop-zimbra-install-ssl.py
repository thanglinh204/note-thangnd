import subprocess

def run_cmd(cmd):
    print(f"\n[RUNNING] {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"[ERROR] Command failed: {cmd}")
        exit(1)

def stop_zimbra():
    run_cmd("su - zimbra -c 'zmcontrol stop'")

if __name__ == "__main__":
    stop_zimbra()
    print("\n✅ Đã dừng dịch vụ Zimbra. Chạy tiếp `install_ssl.py` để cài đặt chứng chỉ SSL.")
