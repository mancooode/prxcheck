import requests
import threading
from colorama import init, Fore, Style

init()  # Initialize colorama

# Start menu ASCII art
print("""


 ██▓███   ██▀███  ▒██   ██▒ ▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀
▓██░  ██▒▓██ ▒ ██▒▒▒ █ █ ▒░▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ 
▓██░ ██▓▒▓██ ░▄█ ▒░░  █   ░▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ 
▒██▄█▓▒ ▒▒██▀▀█▄   ░ █ █ ▒ ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ 
▒██▒ ░  ░░██▓ ▒██▒▒██▒ ▒██▒▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄
▒▓▒░ ░  ░░ ▒▓ ░▒▓░▒▒ ░ ░▓ ░░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒
░▒ ░       ░▒ ░ ▒░░░   ░▒ ░  ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░
░░         ░░   ░  ░    ░  ░         ░  ░░ ░   ░   ░        ░ ░░ ░ 
            ░      ░    ░  ░ ░       ░  ░  ░   ░  ░░ ░      ░  ░   
                           ░                       ░               

   """)
print("coded by @mancode")
print("1. HTTPS Proxy Checker")
print("2. SOCKS4 Proxy Checker")
print("3. SOCKS5 Proxy Checker")
print("4. Exit")

choice = input("Enter : ")

if choice == "1":
    proxy_type = "HTTPS"
elif choice == "2":
    proxy_type = "SOCKS4"
elif choice == "3":
    proxy_type = "SOCKS5"
elif choice == "4":
    print("Exiting...")
    exit()
else:
    print("Invalid choice. Exiting...")
    exit()

# Ask for proxies.txt file name
proxy_file_name = input("Enter your proxy list file eg proxies.txt: ")

# Load proxies from file
with open(proxy_file_name, "r") as f:
    proxies = [line.strip() for line in f.readlines()]

# Function to check proxy
def check_proxy(proxy):
    try:
        response = requests.get("http://httpbin.org/ip", proxies={"https": proxy}, timeout=5)
        if response.status_code == 200:
            print(f"{Fore.GREEN}{proxy} is working!{Style.RESET_ALL}")
            with open("working_proxies.txt", "a") as f:
                f.write(proxy + "\n")
        else:
            print(f"{Fore.RED}{proxy} is dead!{Style.RESET_ALL}")
    except requests.exceptions.RequestException:
        print(f"{Fore.RED}{proxy} is dead!{Style.RESET_ALL}")

# Create threads for each proxy
threads = []
for proxy in proxies:
    t = threading.Thread(target=check_proxy, args=(proxy,))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print("Proxy checking complete!")
