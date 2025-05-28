import os

def main():
    print("\n🚀 Bắt đầu trình cài đặt Zimbra. Làm theo hướng dẫn hiện ra trên màn hình...")
    os.chdir("zimbra/zcs-8.8.15_GA_3869.RHEL7_64.20190918004220")
    os.system("./install.sh")

if __name__ == "__main__":
    main()
