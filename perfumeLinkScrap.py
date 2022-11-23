# ===============
# https://ssamko.tistory.com/27
# ===============


import requests
from bs4  import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
import csv
import pandas as pd

# def createFolder(directory):
#     try:
#         if not os.path.exists(directory):
#             os.makedirs(directory)
#     except:
#         pass

filename = 'perfumebergamot.csv'
f = open(filename, "w")
f.close()

# //*[@id="main-content"]/div[1]/div[1]/div/div[4]/div/div[1]/div/div[2]/div/div[1]/div[3]/h3/a

url = "https://www.fragrantica.com/notes/Bergamot-75.html"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'}
res = requests.get(url, headers = headers)
# soup = BeautifulSoup(res.content, 'lxml')

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--disable-logging')
options.add_argument('--disable-gpu')
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
# options.add_argument('--headless')
driver = webdriver.Chrome("C:\\python\\selenium\\chromedriver.exe", options=options)
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.implicitly_wait(5)

f = open(filename, "a")

products = soup.find_all("div", {"class": "flex-child-auto"})
for product in products:
    ur = product.find('a')
    ur = ur['href']
    print(ur)
    f.write('https://www.fragrantica.com' + ur + '\n')
f.close()


