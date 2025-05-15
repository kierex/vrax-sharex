#!/usr/bin/env python3
# GEH BYPASS MO SAPAKIN KITA E
# WALANG TANIM TO BAKA MASAPAK KO KAYO!
# PEACE LANG DAPAT MWA:))

import requests, os, re, sys, json, time, random
from datetime import datetime
from time import sleep

# Session object
ses = requests.Session()

# Random user agents
ua_list = [
    "Mozilla/5.0 (Linux; Android 10; Wildfire E Lite Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/298.0.0.10.115;]",
    "Mozilla/5.0 (Linux; Android 11; KINGKONG 5 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/320.0.0.12.108;]",
    "Mozilla/5.0 (Linux; Android 11; G91 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/325.0.1.4.108;]"
]
ua = random.choice(ua_list)

# Colored print helper
def color(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def banner():
    os.system("clear")
    print(color("""
 __     _______ ____  _   _ 
 \ \   / / ____|  _ \| \ | |
  \ \ / /|  _| | |_) |  \| |
   \ V / | |___|  _ <| |\  |
    \_/  |_____|_| \_\_| \_|
""", '94'))  # Blue

    print(color("Author  : vrax", '96'))  # Cyan
    print(color("Facebook: https://facebook.com/revn.19", '96'))  # Cyan
    print(color("GitHub  : https://github.com/vraxyxx", '96'))  # Cyan
    print(color("-" * 50, '90'))  # Grey line

def login():
    banner()
    print(color("Lagay mo rito fb cookie mo tanga", '93'))  # Yellow
    cookie_input = input(color("cookie: ", '92'))  # Green input

    cookies = {i.split("=")[0]: i.split("=")[1] for i in cookie_input.split("; ") if "=" in i}

    try:
        data = ses.get("https://business.facebook.com/business_locations", headers={
            "user-agent": ua,
            "referer": "https://www.facebook.com/",
            "host": "business.facebook.com",
            "origin": "https://business.facebook.com",
            "upgrade-insecure-requests": "1",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "content-type": "text/html; charset=utf-8"
        }, cookies=cookies)

        find_token = re.search(r"(EAAG\w+)", data.text)
        if not find_token:
            print(color("\n❌ Token extraction failed. Check your cookie.", '91'))
            return login()

        token = find_token.group(1)
        open("token.txt", "w").write(token)
        open("cookie.txt", "w").write(cookie_input)

        print(color(f"\n✅ Token found: {token}", '92'))  # Green
        time.sleep(3)
        bot()

    except Exception as e:
        if os.path.exists("token.txt"): os.remove("token.txt")
        if os.path.exists("cookie.txt"): os.remove("cookie.txt")
        print(color("Login expired kuha ka ulit bobow.", '91'))  # Red
        login()

def bot():
    os.system("clear")
    banner()
    try:
        token = open("token.txt", "r").read()
        raw_cookie = open("cookie.txt", "r").read()
        cookie = {i.split("=")[0]: i.split("=")[1] for i in raw_cookie.split("; ") if "=" in i}
    except:
        if os.path.exists("token.txt"): os.remove("token.txt")
        if os.path.exists("cookie.txt"): os.remove("cookie.txt")
        print(color("Wala na expired na cookie mo ugok.", '91'))  # Red
        return login()

    link = input(color("Link ng post mo ugok!: ", '96'))  # Cyan
    try:
        limitasyon = int(input(color("limitasyon ng share: ", '96')))  # Cyan
    except ValueError:
        print(color("Limitasyon dapat number, hindi kalokohan.", '91'))
        return bot()

    print(color("Nag loading pa ngani antay ha antay sapakin kita e", '93'))  # Yellow
    start_time = datetime.now()

    try:
        for n in range(1, limitasyon + 1):
            post = ses.post(
                f"https://graph.facebook.com/v13.0/me/feed?link={link}&published=0&access_token={token}",
                headers={
                    "authority": "graph.facebook.com",
                    "cache-control": "max-age=0",
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": ua
                }, cookies=cookie
            ).text

            data = json.loads(post)
            if "id" in data:
                elapsed = str(datetime.now() - start_time).split('.')[0]
                print(color(f"*--> {n}. Sharing na yan antay hanggang matapos baliw!({elapsed})", '92'))  # Green
            else:
                print(color("Ay kawawa suspended cookie mo ayan tanga kasi.", '91'))  # Red
                break

    except requests.exceptions.ConnectionError:
        print(color("(!) hina ng net mo tapon mo nga cp mo!", '91'))
        exit()

if __name__ == "__main__":
    login()
