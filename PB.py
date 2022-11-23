# =======================================
# https://sangminem.tistory.com/32
# =======================================


import requests
from bs4  import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os
import csv
import pandas as pd
import re
import numpy as np
import pandas as pd

# import random
# import concurrent.futures

# # get the list of free proxies
# def getProxies():
#     r = requests.get('https://free-proxy-list.net/')
#     soup = BeautifulSoup(r.content, 'html.parser')
#     table = soup.find('tbody')
#     proxies = []
#     for row in table:
#         if row.find_all('td')[4].text =='elite proxy':
#             proxy = ':'.join([row.find_all('td')[0].text, row.find_all('td')[1].text])
#             proxies.append(proxy)
#         else:
#             pass
#     return proxies

# def extract(proxy):
#     #this was for when we took a list into the function, without conc futures.
#     #proxy = random.choice(proxylist)
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'}
#     try:
#         for i in range(1, 5):
#         #change the url to https://httpbin.org/ip that doesnt block anything
#             url1 = "https://www.albumoftheyear.org/ratings/6-highest-rated/2021/"
#             url = url1+str(i)
#             res = requests.get(url, 'https://httpbin.org/ip', headers=headers, proxies={'http' : proxy,'https': proxy}, timeout=3)
#             soup = BeautifulSoup(res.content, 'lxml')
#             print(res.json(), res.status_code)
#     except requests.ConnectionError as err:
#         print(repr(err))
#     return proxy

# proxylist = getProxies()
# with concurrent.futures.ThreadPoolExecutor() as executor:
#         executor.map(extract, proxylist)


# def createFolder(directory):
#     try:
#         if not os.path.exists(directory):
#             os.makedirs(directory)
#     except:
#         pass

# folder_name = "perfume_bergamot"
# current_path = os.getcwd()
# def createFolder(directory):
#     try:
#         if not os.path.exists(directory):
#             os.makedirs(directory)
#     except OSError:
#             print("이미 같은 이름의 폴더가 존재합니다." + directory)
#             pass


# csv 링크 불러오기
links = []
nono = 'None'
count = 1
with open('perfumebergamot.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    # index 제거
    for i in reader:
        links.append(i)
        for lst in i:
            # print(lst)
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'}
            res = requests.get(lst, headers = headers)
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
            driver.get(lst)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            time.sleep(5)

            # 스크롤 다운을 위한 초기 페이지 높이 저장 (댓글 크롤링을 위한 작업)
            # prev_height = driver.execute_script("return document.body.scrollHeight")
            # i = 0
            # review_list = []
            
            # SCROLL_PAUSE_SEC = 1

            # # 스크롤 높이 가져옴
            # last_height = driver.execute_script("return document.body.scrollHeight")

            # while True:
            #     # 끝까지 스크롤 다운
            #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            #     # 1초 대기
            #     time.sleep(SCROLL_PAUSE_SEC)

            #     # 스크롤 다운 후 스크롤 높이 다시 가져옴
            #     new_height = driver.execute_script("return document.body.scrollHeight")
            #     if new_height == last_height:
            #         break
            #     else:
            #         last_height = new_height
            #         i = i+1
            #         print('스크롤 -',i,'회')
            # print('SCROLL FINISH')

            # time.sleep(5)

            # img = driver.find_element_by_xpath('//*[@id="main-content"]/div[1]/div[1]/div/div[2]/div[1]/div[1]/div/div/img').get_attribute("src")
            # PerN = driver.find_element_by_css_selector('#toptop > h1').text

            # # 성별/브랜드/향수이름 각각 추출
            # temp = PerN.split(' for ')
            # GName = re.sub('\n','',temp[len(temp)-1]).strip()
            # pn = temp[0]
            # pnsplit = pn.split(' ')
            # BName = pnsplit[-1].strip()
            # PNList = pnsplit[:-1]
            # PName = '_'.join(PNList).strip()

            # # # r.close()
            # # print(fors.replace(' ', '-'))
            # print("======="+PName, BName, GName+"=======")

            # acco = driver.find_elements_by_css_selector(".cell accord-box")
            while True:
                try:
                    accords = driver.find_element_by_css_selector("div.small-12.medium-12.large-9.cell > div > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div > div > div")
                except:
                    print("None")
                    break
            
            print(accords)

            # df_names = pd.DataFrame(np.array([lst,BName,PName,GName,img]).reshape(1,5),columns = ['URL','Brand','Name','Gender','imgLink'])
            

            
            # PerfumeName = PName.replace(' ', '-')
            # BrandName = BName.replace(' ', '-')