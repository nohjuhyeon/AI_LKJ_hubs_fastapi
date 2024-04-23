## dbmongo의 collection 연결
from pymongo import MongoClient
mongoClient = MongoClient("mongodb://192.168.10.240:27017")
# database 연결
database = mongoClient["AI_LKJ"]
collection = database['trip_package']
collection.delete_many({})

# 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import requests

import time


# Chrome 드라이버 설치 디렉터리 설정
webdriver_manager_directory = ChromeDriverManager().install()

# Chrome 브라우저 옵션 설정
chrome_options = Options()
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

# WebDriver 생성
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory), options=chrome_options)

# 크롤링할 웹 페이지 URL
url = "https://www.ybtour.co.kr/product/main.yb?menu=DMT&dspSid=AD00000"

# 웹 페이지 열기
html_source = browser.get(url)

# # 제주도 선택
select_jeju = browser.find_element(by=By.CSS_SELECTOR, value='#header > div.gnb_wrap > div > ul > li:nth-child(7) > div > ul.gnb_sub > li:nth-child(1) > a')

# 제주도 클릭
select_jeju.click()

# 제주 지역 선택
num_of_items_first = 4

for i in range(1, num_of_items_first + 1) :
    select_citys = browser.find_element(by=By.CSS_SELECTOR, value=f"#product > div:nth-child(4) > div > ul > li:nth-child({i}) > a") 
    select_citys.click()
    time.sleep(2)

    find_lists_jeju = browser.find_elements(by=By.CSS_SELECTOR, value="#__next > div:nth-child(1) > div.sc-b4e0ae96-3.ckkABC > div > div > div.sc-bc872dfc-7.dWcbgi > div.sc-bc872dfc-8.iyyBjs > div > ul")


    for find_list in find_lists_jeju :
        image = find_list.find_element(by=By.CSS_SELECTOR, value='#__next > div:nth-child(1) > div.sc-b4e0ae96-3.ckkABC > div > div > div.sc-bc872dfc-7.dWcbgi > div.sc-bc872dfc-8.iyyBjs > div > ul > li > div.sc-bc872dfc-12.kDxQpR > div.sc-ccf49e29-0.bYuowP > div.sc-bc872dfc-35.dQqCGX > span > img')
        image_url = image.get_attribute('src')

       
        title = find_list.find_element(by=By.CSS_SELECTOR, value="li > div.sc-bc872dfc-12.kDxQpR > div.sc-3ed68ec3-1.jSqOHV > h5") .text
        departure_period = find_list.find_element(by=By.CSS_SELECTOR, value="dl:nth-child(1) > dd").text
        departure_day = find_list.find_element(by=By.CSS_SELECTOR, value=" dd > span").text
        transportation = find_list.find_element(by=By.CSS_SELECTOR, value="dl > dd:nth-child(2) > div > em").text
        price = find_list.find_element(by=By.CSS_SELECTOR, value="em > strong").text

        # print('image:', image)
        # print('title:', title)
        # print('departure_period:', departure_period)
        # print('departure_day:', departure_day)
        # print('transportation:', transportation)
        # print('price:', price)
        # print('제주')

         # 지역 열 추가적으로 삽입
        add_data = '제주'

        # mongodb 삽입
        data = {
            'region' : add_data,
            'image' : image_url,
            'title': title,
            'departure_period' : departure_period,
            'departure_day' : departure_day,
            'transportation' : transportation,
            'price' : price
        }

        # MongoDB 컬렉션에 데이터 삽입
        # collection.insert_one(data)
        
    browser.back()
    time.sleep(2)

print("데이터가 MongoDB에 성공적으로 삽입되었습니다.")


time.sleep(2)

# 내륙/섬 선택
select_inland = browser.find_element(by=By.CSS_SELECTOR, value='#header > div.gnb_wrap > div > ul > li:nth-child(7) > div > ul.gnb_sub > li:nth-child(2)')

# 내륙/섬 클릭
select_inland.click()

# 내륙 지역 선택
num_of_items_second = 7
region_list = ['','강원','부산/경상','서울/경기','전라','충청','울릉도','홍도,흑산도,백령도']
for i in range(1, num_of_items_second + 1):
    select_citys_inland = browser.find_element(by=By.CSS_SELECTOR, value=f"div:nth-child(4) > div > ul > li:nth-child({i}) > a") 
    select_citys_inland.click()
    time.sleep(2)

    find_lists_inland = browser.find_elements(by=By.CSS_SELECTOR, value="#__next > div:nth-child(1) > div.sc-b4e0ae96-3.ckkABC > div > div > div.sc-bc872dfc-7.dWcbgi > div.sc-bc872dfc-8.iyyBjs > div > ul")

    for find_list_inland in find_lists_inland :
        image_inland = find_list_inland.find_element(by=By.CSS_SELECTOR, value='#__next > div:nth-child(1) > div.sc-b4e0ae96-3.ckkABC > div > div > div.sc-bc872dfc-7.dWcbgi > div.sc-bc872dfc-8.iyyBjs > div > ul > li > div.sc-bc872dfc-12.kDxQpR > div.sc-ccf49e29-0.bYuowP > div.sc-bc872dfc-35.dQqCGX > span > img')
        image_inland_url = image_inland.get_attribute('src')

        title_inland = find_list_inland.find_element(by=By.CSS_SELECTOR, value="li > div.sc-bc872dfc-12.kDxQpR > div.sc-3ed68ec3-1.jSqOHV > h5") .text
        departure_period_inland = find_list_inland.find_element(by=By.CSS_SELECTOR, value="dl:nth-child(1) > dd").text
        departure_day_inland = find_list_inland.find_element(by=By.CSS_SELECTOR, value=" dd > span").text
        transportation_inland = find_list_inland.find_element(by=By.CSS_SELECTOR, value="dl > dd:nth-child(2) > div > em").text
        price_inland = find_list_inland.find_element(by=By.CSS_SELECTOR, value="em > strong").text  

        # print('image_inland:', image_inland)
        # print('title_inland:', title_inland)
        # print('departure_period_inland:', departure_period_inland)
        # print('departure_day_inland:', departure_day_inland)
        # print('transportation_inland:', transportation_inland)
        # print('price_inland:', price_inland) 
        # print(region_list[i])

        # 지역 열 추가적으로 삽입
        add_data_seconnd = region_list[i]

            # mongodb 삽입
        data = {
            'region' : add_data_seconnd,
            'image' : image_inland_url,
            'title': title_inland,
            'departure_period' : departure_period_inland,
            'departure_day' : departure_day_inland,
            'transportation' : transportation_inland,
            'price' : price_inland
        }

        # MongoDB 컬렉션에 데이터 삽입
        # collection.insert_one(data)

    browser.back()
    time.sleep(2)

print("데이터가 MongoDB에 성공적으로 삽입되었습니다.")

# 브라우저 종료
browser.quit()