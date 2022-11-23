import requests
from bs4  import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os
import csv
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

filename = 'adidas.csv'
f = open(filename, "w")
f.close()



for i in range(1, 11):
    url = "https://sneakernews.com/category/adidas/page/{}/".format(i)
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'}
    res = requests.get(url, headers = headers)
    soup = BeautifulSoup(res.content, 'lxml')

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
    time.sleep(6)


    # f = open("adidas{}.txt".format(i), "w")
    # f = open(filename, "a")
    # products = soup.find_all("div", {"class": "post-content"})
    # for product in products:
    #     ur = product.find('a')
    #     ur = ur['href']
    #     f.write(ur + '\n')
    # f.close()
    f = open(filename, "a")
    products = soup.find_all("div", {"class": "post-content"})
    for product in products:
        ur = product.find('a')
        ur = ur['href']
        f.write(ur + '\n')
    f.close()




# products = driver.find_elements_by_css_selector('.post-content')