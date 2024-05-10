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
collection = database['toru_pass_review']

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
browser.get("https://search.shopping.naver.com/search/all?adQuery=%ED%88%AC%EC%96%B4%ED%8C%A8%EC%8A%A4&npayType=&origQuery=%ED%88%AC%EC%96%B4%ED%8C%A8%EC%8A%A4&pagingIndex=1&pagingSize=40&productSet=checkout&query=%ED%88%AC%EC%96%B4%ED%8C%A8%EC%8A%A4&sort=review&timestamp=&viewType=list")                                     # - 주소 입력

                                                    # - 가능 여부에 대한 OK 받음
pass
html = browser.page_source                          # - html 파일 받음(and 확인)
# print(html)

from selenium.webdriver.common.by import By          # - 정보 획득
from selenium.webdriver.common.keys import Keys
# browser.save_screenshot('./formats.png')     

# 여러개 동영상 collection 있을때 버튼
tour_pass_list = browser.find_elements(by=By.CSS_SELECTOR,value='div.product_title__Mmw2K > a')

time.sleep(2)
for i in range(len(tour_pass_list)):
    tour_pass_list = browser.find_elements(by=By.CSS_SELECTOR,value='div.product_title__Mmw2K > a')
    if '투어 패스' in tour_pass_list[i].text or '투어패스' in tour_pass_list[i].text:
        if '부산' in tour_pass_list[i].text:
            region = '부산'
        elif '경기' in tour_pass_list[i].text:
            region = '경기'
        elif '강릉' in tour_pass_list[i].text:
            region = '강원'
        elif '강원' in tour_pass_list[i].text:
            region = '강원'
        elif '제주' in tour_pass_list[i].text:
            region = '제주'

        tour_pass_list[i].click()
        
        time.sleep(1)
        # 설명 더보기 버튼
    
    print(tour_pass_list[i].text)
    print(region)
    browser.back()
    pass

browser.quit()                                      # - 브라우저 종료
