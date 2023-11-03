import sys
import requests
import time

from selenium import webdriver

 

import time

from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

import subprocess


 

def LoadgiaHan():

    options = Options()
 
    options.add_argument("--disable-infobars")

    options.add_argument("--ignore-certificate-errors")

    options.add_argument("--disable-save-password-bubble")

    options.add_argument("--disable-password-manager-reauthentication")

    options.add_argument("--no-first-run")

    options.add_argument("--no-default-browser-check")

    options.add_argument("--disable-component-update")

    options.add_argument("--disable-browser-side-navigation")

    options.add_argument("--kiosk")

    options.add_experimental_option("useAutomationExtension", False)

    options.add_experimental_option("excludeSwitches",["enable-automation"])


    # Khởi tạo trình duyệt Selenium (chẳng hạn Chrome)

    driver = webdriver.Chrome(options=options)

    # Điều hướng đến trang đăng nhập No-IP

    driver.get("http://localhost:8000/")

   
    while True:

        time.sleep(1)


def CheckIsURL(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False

        
if __name__ == "__main__":

    while True:
        if CheckIsURL("http://127.0.0.1:8000/"):
            LoadgiaHan()
        time.sleep(1)