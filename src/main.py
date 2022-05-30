""" Minimal Selenium setup with headless chrome webdriver.
This script returns IP provided by Zytes (Must be different for each run).
In the context of a local run, "GH_TOKEN" environment variable must contain your github personal acess token.
"""

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

os.environ["GH_TOKEN"] = "github_personal_acess_token"

HEADLESS_PROXY = "localhost:3128"

webdriver.DesiredCapabilities.CHROME['proxy'] = {
    "httpProxy": HEADLESS_PROXY,
    "sslProxy": HEADLESS_PROXY,
    "proxyType": "MANUAL",
}
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("window-size=1920x1080")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--profile-directory=Default')
options.add_argument('--ignore-certificate-errors') 


with webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) as driver:
    driver.get('https://api.ipify.org/')
    ip_address = driver.find_element(By.TAG_NAME, "body").text
    print(ip_address)
