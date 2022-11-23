#""""""""""""
#
# https://github.com/jhnwr/image-downloader/blob/main/imagedownloader.py
# https://data-make.tistory.com/170
# https://heodolf.tistory.com/80
# https://jamielim.tistory.com/entry/4%EC%A3%BC%EC%B0%A8-web-Crawling
# https://stackoverflow.com/questions/19200497/python-selenium-webscraping-nosuchelementexception-not-recognized


import requests
from bs4  import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os
import csv
import pandas as pd
import re
import urllib.request
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
import numpy as np

# 링크 스크래핑한 파일 불러오기
# df = pd.read_csv('adidas.csv')
# sneakers = df.to_csv('adidas.csv', index=False)

# 저장할 폴더 만들기
folder_name = "sneakers"
current_path = os.getcwd()
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
            print("이미 같은 이름의 폴더가 존재합니다." + directory)
            pass


# csv 링크 불러오기
links = []
nono = 'None'
count = 1
with open('adidas.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    # index 제거
    for i in reader:
        links.append(i)
        for lst in i:
            # print(lst)
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'}
            res = requests.get(lst, headers = headers)
            soup = BeautifulSoup(res.content, 'lxml')

            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            options.add_argument('--disable-logging')
            options.add_argument('--disable-gpu')
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--no-sandbox')
            options.add_argument('--headless')
            driver = webdriver.Chrome("C:\\python\\selenium\\chromedriver.exe", options=options)
            driver.get(lst)
            time.sleep(5)

            # 폴더 생성
            # img_folder_path = 'C:\python\selenium\sneakers'
            # if not os.path.isdir(img_folder_path):
            #     createFolder(current_path + "/" + folder_name)
            # os.chdir(folder_name)

            # 메인 이미지 크롤링
            main_img = driver.find_element_by_xpath('//*[@id="main-content"]/div/div[1]/div[1]/p/img').get_attribute("src")
            # 제품명
            try:
                name = driver.find_element_by_xpath('//*[@id="main-content"]/div/div[1]/div[1]/div[3]/div/blockquote/div/strong[1]').text
            except NoSuchElementException:
                name = driver.find_element_by_xpath('//*[@id="main-content"]/div/div[1]/div[1]/div[3]/div[1]/blockquote/div/strong[1]').text
            score = driver.find_element_by_css_selector('.default-rating-digit.release-first-rating-digit').text
            date = driver.find_element_by_css_selector('blockquote > div').text
            # 평점과 총 투표자 수 나눔
            avrg = score[0:8]
            votes = score[-8:]


            df = pd.DataFrame(np.array([lst,main_img,name.replace(' ', '-').replace('"', ''),avrg.replace(' ', '_')+' | '+
                votes.replace(' ', '_'),date.replace(' ', '-')]).reshape(1,5),columns = ['URL', 'main_img', 'name', 'votes', 'date'])
            df.index = df.index + 1
            df.to_csv(f'adidascrawling.csv', mode='w', encoding='utf-8-sig', header=True, index=True)




            # 사이트 내 div위치, 이름이 제각각이라 좀 더 효율적인 이미지 크롤링 방법 연구 필요
            # while True:
            #     try:
            #         sub_img = driver.find_element_by_xpath('//*[@id="main-content"]/div/div[1]/div[1]/div[3]/p[5]/img[{}]'.format(count))
            #         sub_src = sub_img.get_attribute("src")
            #         print(sub_src)
            #     except NoSuchElementException:
            #         try:
            #             sub_img = driver.find_element_by_xpath('//*[@id="main-content"]/div/div[1]/div[1]/div[3]/p[6]/img')
            #             sub_src = sub_img.get_attribute("src")
            #             print(sub_src)
            #         except NoSuchElementException:
            #             print("sub_img 저장 끝")
            #             break
            #         break
            #     count += 1
            
            # 이미지를 저장
            # with open(name.replace(' ', '-').replace('"', '') + '.jpg', 'wb') as f:
            #     im = requests.get(main_img)
            #     f.write(im.content)
            #     print('Writing: ', name)



            # with open(name.replace(' ', '-').replace('"', '') + '{}'.format(count) + '.jpg', 'ab') as f:
            #     im2 = requests.get(s_img)
            #     f.write(im2.content)
            #     print('Writing: ', name)

          
            

            # sub_img = soup.select()
            # for image2 in img2:
            #     if driver.find_element_by_css_selector('.ebay-after-img'):
            #         print("ebay 이미지 제외")
            #         continue
            #     else:
            #         sub_img = image2.select('p:nth-child(5)' > 'img')
            #     print(sub_img)

                        # while True:

            
            # while True:
            #     try:
            #         sub_img = driver.find_element_by_xpath('//*[@id="main-content"]/div/div[1]/div[1]/div[3]/p[5]/img').get_attribute("src")
            #     except NoSuchElementException:
            #         break
                

# s_img = driver.find_element_by_css_selector('div > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > p:nth-child(5) > img').get_attribute('src')
            
            # sub_img = driver.find_elements_by_css_selector('.sneaker-post-content')
            # for sub in sub_img:
            #     # 이베이 이미지 제외
            #     ebay = sub.find_element_by_css_selector('.ebay-after-img')
            #     if ebay:
            #         print("ebay img 제외")
            #         continue
            # try:
            #     s_img = driver.find_element_by_xpath('//*[@id="main-content"]/div/div[1]/div[1]/div[3]/p[5]/img[{}]'.format(count))
            #     s_img.get_attribute('src')
            #     count += 1
            # except:
            #     pass
                

# with open('adidas.csv', 'r') as f:
#     reader = csv.reader(f)
#     next(reader)
#     for i in reader:
#         print(i)