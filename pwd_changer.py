import requests,os,threading
from time import sleep
from colorama import Fore

if os.name == 'nt':
	os.system("cls")
else:
	os.system("clear")

print(f'''{Fore.LIGHTRED_EX}
░█▀█░█▀█░█▀▀░█▀▀░█░█░█▀█░█▀▄░█▀▄░░▀█▀░█▀█░█░█░█▀▀░█▀█░
░█▀▀░█▀█░▀▀█░▀▀█░█▄█░█░█░█▀▄░█░█░░░█░░█░█░█▀▄░█▀▀░█░█░
░▀░░░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀░░░░▀░░▀▀▀░▀░▀░▀▀▀░▀░▀░
░█▀▀░█░█░█▀█░█▀█░█▀▀░█▀▀░█▀▄░
░█░░░█▀█░█▀█░█░█░█░█░█▀▀░█▀▄░
░▀▀▀░▀░▀░▀░▀░▀░▀░▀▀▀░▀▀▀░▀░▀░ {Fore.RESET}v0.1 by $ffe''')

proxy = input(f"\n{Fore.LIGHTBLUE_EX}Proxy (username:password@ip:port): {Fore.RESET}")

tokens = open("old.txt", 'r').read()
total_tokens = len(open('old.txt').readlines())

if proxy != "":
  proxies = {
    "https": f"http://{proxy}"
  }
else:
  proxies = None

print(f"\n{Fore.LIGHTBLUE_EX}Starting..{Fore.RESET}\n")

def change_pwd(n):
    try:
        while True:

            headers = {
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjkzLjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTMuMCIsImJyb3dzZXJfdmVyc2lvbiI6IjkzLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTAwODA0LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
                "sec-fetch-dest": "empty",
                "x-debug-options": "bugReporterEnabled",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "accept": "*/*",
                "accept-language": "en-GB",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.16 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                "TE": "trailers",
                "referer": "https://discord.com/channels/@me"
            }

            headers_fingerprint = {
                "accept": "*/*",
                "authority": "discord.com",
                "method": "POST",
                "path": "/api/v9/auth/register",
                "scheme": "https",
                "origin": "discord.com",
                "referer": "discord.com/register",
                "x-debug-options": "bugReporterEnabled",
                "accept-language": "en-US,en;q=0.9",
                "connection": "keep-alive",
                "content-Type": "application/json",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA0OTY3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin"
            }

            def request_cookie():
              response1 = requests.get("https://discord.com")
              cookie = response1.cookies.get_dict()
              cookie['locale'] = "us"
              return cookie

            def request_fingerprint():
              response2 = requests.get("https://discordapp.com/api/v9/experiments", headers=headers_fingerprint).json()
              fingerprint = response2["fingerprint"]
              return fingerprint

            headers["authorization"] = tokens.split()[n].split(':')[2]
            headers["x-fingerprint"] = request_fingerprint()

            new_password = "".join("abcdefghjklmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789!?"[c % 59] for c in os.urandom(12))

            payload = {
                "new_password": new_password,
                "password": tokens.split()[n].split(':')[1]
            }

            response = requests.patch("https://discord.com/api/v9/users/@me", headers=headers, json=payload, cookies=request_cookie(), proxies=proxies, timeout=20)
            if response.status_code == 200:
                new_token = response.json()['token']
                print(f"{Fore.GREEN}{Fore.RED}{tokens.split()[n].split(':')[2]} {Fore.LIGHTBLACK_EX}->{Fore.GREEN} {new_token} {Fore.LIGHTBLACK_EX}| Password: {new_password}{Fore.RESET}")
                save_output = open("new.txt", "a")
                save_output.write(f"{tokens.split()[n].split(':')[0]}:{new_password}:{new_token}\n")
                save_output.close()
            else:
                print(f"{Fore.RED}[-] {tokens.split()[n].split(':')[2]} {Fore.LIGHTBLACK_EX}({response.text}){Fore.RESET}")

            break

    except Exception as err:
        print(f"{Fore.RED}[!] {tokens.split()[n].split(':')[2]} {Fore.LIGHTBLACK_EX}({err}){Fore.RESET}")
        pass

threads = []

for i in range(total_tokens):
    t = threading.Thread(target=change_pwd, args=(i,))
    t.daemon = True
    threads.append(t)
 
for i in range(total_tokens):
    threads[i].start()
    sleep(1)
 
for i in range(total_tokens):
    threads[i].join()

input(f"\n{Fore.YELLOW}Finished{Fore.RESET}")