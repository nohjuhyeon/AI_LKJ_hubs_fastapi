# * 웹 크롤링 동작
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
webdriver_manager_directory = ChromeDriverManager().install()
import time
# ChromeDriver 실행

from selenium.webdriver.chrome.options import Options

from pymongo import MongoClient

mongoClient = MongoClient("mongodb://192.168.10.240:27017/")
database = mongoClient["AI_LKJ"]
collection = database['data_tour_pass_review_tmon']
# Chrome 브라우저 옵션 생성
chrome_options = Options()

# User-Agent 설정
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

# WebDriver 생성
webdriver_manager_dricetory = ChromeDriverManager().install()

browser = webdriver.Chrome(service = ChromeService(webdriver_manager_directory), options=chrome_options)                        # - chrome browser 열기

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

pass
browser.get("https://www.tmon.co.kr/deal/10716684222?keyword=%ED%88%AC%EC%96%B4%ED%8C%A8%EC%8A%A4&tl_area=SKJCD&tl_ord=2&searchClick=DL%7CND%7CBM&tab=&thr=hs")                                     # - 주소 입력

pass
html = browser.page_source                          # - html 파일 받음(and 확인)
# print(html)

from selenium.webdriver.common.by import By          # - 정보 획득
from selenium.webdriver.common.keys import Keys
# browser.save_screenshot('./formats.png')     

# 여러개 동영상 collection 있을때 버튼
tour_pass_list = browser.find_elements(by=By.CSS_SELECTOR,value='#CategoryProducts > ul > li > div > a > strong')
title = browser.find_element(by=By.CSS_SELECTOR,value='#view-default-scene-default > section.wrap_deals_basic.center_grid > div.bx_ct.deal_info > article.deal_info_summary > div.deal_title > h2').text
time.sleep(2)
review_btn = browser.find_element(by=By.CSS_SELECTOR,value='#tab-navigation > div > ul > li:nth-child(2) > a')
review_btn.click()
time.sleep(1)
while True:
    review_box = browser.find_elements(by=By.CSS_SELECTOR,value='#_reviewList > li > div')
    for review_element in review_box:
        region = '부산'
        date = review_element.find_element(by=By.CSS_SELECTOR,value='ul.type_bar_list > li:nth-child(2)').text
        date = date.split()[0].split('-')
        date = '.'.join(date) + '.'
        date = date[2:]
        rating = review_element.find_element(by=By.CSS_SELECTOR,value='span.star_rate > span > span').text
        rating = rating.split()[-1]
        content = review_element.find_element(by=By.CSS_SELECTOR,value=' div.review_block_text > div.review_text').text
        print(title)
        print(region)
        print(rating)
        print(date)
        print(content)
        # collection.insert_one({'title':title,
        #     'region':region,
        #     'rating': rating,
        #     'date':date,
        #     'content':content})
    try:
        next_btn = browser.find_element(by=By.CSS_SELECTOR,value='#reviewPaginate > div > a.next_page')
        next_btn.click()
        time.sleep(1)
    except:
        break


    