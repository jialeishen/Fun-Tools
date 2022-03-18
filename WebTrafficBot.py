# A bot increasing the pageview/traffic of your website for SEO
# Author: Jialei Shen
# Email: jshen20@syr.edu
# Latest: 03/18/2022

import webbrowser
import time
import os

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
tor_path = 'C:/Users/Jialei Shen/Desktop/Tor Browser/Browser/firefox.exe %s'    # Your Tor browser address

ip = input("Viarable IP (y/n): ")
timed = int(input("View Time (sec) : "))    # The interval time should not be too short when using Tor browser as it requires more time to initilize
url = input("Enter URL: ")
cycles = int(input("Views : "))

for bulk in range(cycles):
    if ip == "y" or "Y" or "1":
        path = tor_path     # CAPTCHA may need to be completed for some websites
        browser = "firefox.exe"
    else:
        path = chrome_path
        browser = "chrome.exe"
    webbrowser.get(path).open_new(url)
    time.sleep(timed)
    taskkill = "taskkill /im " + browser +" /f"
    os.system(taskkill)
os.system(taskkill)
