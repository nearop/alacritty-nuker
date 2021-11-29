import os
import requests
import random
from colorama import Fore, Style, init
import time
import json
from os import system, write
import warnings
import re
import twocaptcha
from twocaptcha import TwoCaptcha
import threading
import webbrowser
from pynput.keyboard import Key, Controller
warnings.filterwarnings("ignore")
import pyautogui

out_file = "proxies.txt"
f = open(out_file,'wb')
r1 = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all")
r2 = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt")
f.write(r1.content)
f.write(r2.content)
f.close()



keyboard = Controller()
special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

os.system("title NationGenerator")



init(convert=True)

def banner():
    print(f"""{Fore.LIGHTBLUE_EX}
                                       ╔╗╔╔═╗╔╦╗╦╔═╗╔╗╔  ╔═╗╔═╗╔╗╔╔═╗╦═╗╔═╗╔╦╗╔═╗╦═╗
                                       ║║║╠═╣ ║ ║║ ║║║║  ║ ╦║╣ ║║║║╣ ╠╦╝╠═╣ ║ ║ ║╠╦╝
                                       ╝╚╝╩ ╩ ╩ ╩╚═╝╝╚╝  ╚═╝╚═╝╝╚╝╚═╝╩╚═╩ ╩ ╩ ╚═╝╩╚═
    
    """)

banner()




  
os.system('cls')

banner()
username = input("Insert the username to use (more than 2 characters): ")
n = len(username)
if(special_char.search(username) == None):
    pass
else:
    print("")
    print(f"{Fore.RED}Please do not use special characters!")
    time.sleep(2)
    os.close()
if n == 1:
 print("")
 print(f"{Fore.RED}The name must have 2 or more characters!")
 time.sleep(2)
 os.close()
else:
    os.system('cls')
    banner()
    pass
    

password = input("Insert the password to use (more than 6 characters): ")
n = len(password)
if n == 1:
    print(f"{Fore.RED}The password must have 6 or more characters!")
    time.sleep(2)
    os.close()

elif n == 2:
    print("")
    print(f"{Fore.RED}The password must have 6 or more characters!")
    time.sleep(2)
    os.close()

elif n == 3:
    print("")
    print(f"{Fore.RED}The password must have 6 or more characters!")
    time.sleep(2)
    os.close()

elif n == 4:
    print("")
    print(f"{Fore.RED}The password must have 6 or more characters!")
    time.sleep(2)
    os.close()

elif n == 5:
    print("")
    print(f"{Fore.RED}The password must have 6 or more characters!")
    time.sleep(2)
    os.close()

else :
    pass

inputs:()

os.system('cls')

banner()

proxy = set()

with open("proxies.txt", "r") as f:
        file_lines1 = f.readlines()
        for line1 in file_lines1:
            proxy.add(line1.strip())
            

proxiesRandom = {
        'https': 'http://'+random.choice(list(proxy))}
print(proxiesRandom)

randemail = lines = open("emails.txt").readlines() 
line = lines[0] 
email = line.split() 
emailpicked = random.choice(email)

response = requests.get("https://discord.com/register")
if response.status_code == 200:
    time.sleep(2)
    print ('Successfully started the registration...')

    

else:
    print ('ERROR! cant start the registration.')
    time.sleep(2)
    os.close()



_00.post("https://discord.com/api/v9/auth/register", headers={"Host":"discord.com", "Connection":"keep-alive", "sec-ch-ua":'"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"', "X-Super-Properties":"eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkzLjAuNDU3Ny42MyBTYWZhcmkvNTM3LjM2IEVkZy85My4wLjk2MS40NyIsImJyb3dzZXJfdmVyc2lvbiI6IjkzLjAuNDU3Ny42MyIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiaHR0cHM6Ly9kaXNjb3JkLmNvbS9jaGFubmVscy81NTQxMjU3Nzc4MTg2MTU4NDQvODcwODgxOTEyMzQyODUxNTk1IiwicmVmZXJyaW5nX2RvbWFpbiI6ImRpc2NvcmQuY29tIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk3NTA3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==", "X-Fingerprint": "", "Accept-Language":"en-US", "sec-ch-ua-mobile":"?0", "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47", "Content-Type":"application/json", "Authorization":"undefined", "Accept":"*/*", "Origin":"https://discord.com", "Sec-Fetch-Site":"same-origin", "Sec-Fetch-Mode":"cors", "Sec-Fetch-Dest":"empty", "Referer":"https://discord.com/register", "X-Debug-Options":"bugReporterEnabled", "Accept-Encoding":"gzip, deflate, br", "Cookie": "OptanonConsent=version=6.17.0; locale=th"}, json={"fingerprint": "", "username":f'{__O(8)} | {_________0}', "invite": X , "consent": True, "gift_code_sku_id":"", "captcha_key": X_}).json()

i = 0

while i > 1:
    print()
resp = requests.post('https://discord.com/api/v9/auth/register', proxies=None, headers=header, data=json.dumps(payload))
if resp.status_code == 200 :
    token = response.json()
    data = token['token']
    print("Token successfully created : " + token)
    with open(f"tokens.txt", "a+") as f:
                f.write(str(data + '\n'))
                f.close()
    print("Verifying the email...")
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open("https://accounts.google.com/AddSession/identifier?hl=it&continue=https%3A%2F%2Fmail.google.com%2Fmail&service=mail&ec=GAlAFw&flowName=GlifWebSignIn&flowEntry=AddSession")
    time.sleep(4)
    pyautogui.hotkey('ctrl', 'a')
    keyboard.type('seniorriccardomilos@gmail.com')
    keyboard.press(Key.enter)
    time.sleep(2)
    keyboard.type('3711981601aS..')
    keyboard.press(Key.enter)
    print("successfully verified!")
    os.system("taskkill /im chrome.exe /f")
    time.sleep(2)
    
else :
    print("some error occurred")

time.sleep(2)
