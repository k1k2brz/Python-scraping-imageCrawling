import requests
import os
# import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from bs4 import BeautifulSoup
import urllib.request
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
# # -----------------------
# # import random
# # import concurrent.futures

# #get the list of free proxies
# # def getProxies():
# #     r = requests.get('https://free-proxy-list.net/')
# #     soup = BeautifulSoup(r.content, 'html.parser')
# #     table = soup.find('tbody')
# #     proxies = []
# #     for row in table:
# #         if row.find_all('td')[4].text =='elite proxy':
# #             proxy = ':'.join([row.find_all('td')[0].text, row.find_all('td')[1].text])
# #             proxies.append(proxy)
# #         else:
# #             pass
# #     return proxies

# # def extract(proxy):
# #     #this was for when we took a list into the function, without conc futures.
# #     #proxy = random.choice(proxylist)
# #     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'}
# #     try:
# #         #change the url to https://httpbin.org/ip that doesnt block anything
# #         url = 'https://rateyourmusic.com/charts/'
# #         r = requests.get(url, 'https://httpbin.org/ip', headers=headers, proxies={'http' : proxy,'https': proxy}, timeout=3)
# #         soup = BeautifulSoup(r.content, 'html.parser')
# #         print(r.json(), r.status_code)
# #     except requests.ConnectionError as err:
# #         print(repr(err))
# #     return proxy

# # proxylist = getProxies()
# # with concurrent.futures.ThreadPoolExecutor() as executor:
# #         executor.map(extract, proxylist)

# # keyword = input('파일명 : ')
# # maxImages = int(input('다운로드 시도할 최대 이미지 수 : '))

# # # 프로젝트에 미리 생성해놓은 crawled_img폴더 안에 하위 폴더 생성
# # # 폴더명에는 입력한 키워드, 이미지 수 정보를 표시함
# # path = 'crawled_img/'+keyword+'_'+str(maxImages)

# # try:
# #     # 중복되는 폴더 명이 없다면 생성
# #     if not os.path.exists(path):
# #         os.makedirs(path)
# #     # 중복된다면 문구 출력 후 프로그램 종료
# #     else:
# #         print('이전에 같은 [검색어, 이미지 수]로 다운로드한 폴더가 존재합니다.')
# #         sys.exit(0)
# # except OSError:
# #     print ('os error')
# #     sys.exit(0)
# # =======================================================================================
url = 'https://www.fragrantica.com/notes/Bergamot-75.html'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'}
req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.content, 'html.parser')


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_argument("--proxy-server=socks5://127.0.0.1:9150")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument('--disable-logging')
options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument('--headless')
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36")
# options.add_argument('window-size=1920,1080')
driver = webdriver.Chrome("C:\\python\\selenium\\chromedriver.exe", options=options)

driver.get("https://www.fragrantica.com/notes/Bergamot-75.html")
time.sleep(3)

SCROLL_PAUSE_TIME = 1
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    # if new_height == last_height:
    #     try:
    #         driver.find_element_by_xpath('//*[@id="main-content"]/div[1]/div[1]/div/div[2]/div[1]/div[1]/div/div/img').click()
    #     except:
    #         break
    last_height = new_height
    break

curr_handle = driver.current_window_handle
print(curr_handle)

mylist = []
images = driver.find_elements(By.CSS_SELECTOR, '.link-span')
for span in images:
    mylist.append(span)

count = 1
handles = driver.window_handles

for handle in handles:
    print(f'브라우저 핸들: {handle}')
    driver.switch_to.window(handle)
    print(f'브라우저 제목: {driver.title}')
    
    driver.implicitly_wait(5)
    for image in mylist:
        print(image.get_attribute('src'))
        # try:
#             image.click()
#             time.sleep(3)
#             imgUrl = driver.find_element(By.XPATH, '//*[@id="main-content"]/div[1]/div[1]/div/div[2]/div[1]/div[1]/div/div/img').get_attribute("src")
#             urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
#             print(f"index: {count}")
#             driver.switch_to.window(curr_handle)
#             print(f'브라우저 제목: {driver.title}')
#             time.sleep(1)
#             driver.get("https://www.fragrantica.com/notes/Bergamot-75.html")
#             count = count + 1
#             time.sleep(3)
            
#             time.sleep(5)
#         except:
#             pass

# driver.close()

# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
