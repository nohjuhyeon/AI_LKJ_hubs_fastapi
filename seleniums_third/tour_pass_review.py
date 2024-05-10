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
browser.get("https://smartstore.naver.com/lscompany01/category/e4a8e9ad47c74cbebb8457c9995f2f38?cp=1")                                     # - 주소 입력

pass
html = browser.page_source                          # - html 파일 받음(and 확인)
# print(html)

from selenium.webdriver.common.by import By          # - 정보 획득
from selenium.webdriver.common.keys import Keys
# browser.save_screenshot('./formats.png')     

# 여러개 동영상 collection 있을때 버튼
tour_pass_list = browser.find_elements(by=By.CSS_SELECTOR,value='#CategoryProducts > ul > li > div > a > strong')

time.sleep(2)
for i in range(len(tour_pass_list)):
    time.sleep(1)
    tour_pass_list = browser.find_elements(by=By.CSS_SELECTOR,value='#CategoryProducts > ul > li > div > a > strong')
    if '투어 패스' in tour_pass_list[i].text or '투어패스' in tour_pass_list[i].text:
        title = tour_pass_list[i].text
        if '부산' in tour_pass_list[i].text:
            region = '부산'
            tour_pass_list[i].click()
        elif '경기' in tour_pass_list[i].text:
            region = '경기'
            tour_pass_list[i].click()
        elif '강릉' in tour_pass_list[i].text:
            region = '강원'
            tour_pass_list[i].click()
        elif '강원' in tour_pass_list[i].text:
            region = '강원'
            tour_pass_list[i].click()
        elif '제주' in tour_pass_list[i].text:
            region = '제주'
            tour_pass_list[i].click()
        elif '여수' in tour_pass_list[i].text:
            region = '전남'
            tour_pass_list[i].click()
        elif '충남' in tour_pass_list[i].text:
            region = '충남'
            tour_pass_list[i].click()
        elif '전북' in tour_pass_list[i].text:
            region = '전북'
            tour_pass_list[i].click()
                    
        time.sleep(2)
        # 설명 더보기 버튼
    
    print(title)
    print(region)
    review_box = browser.find_element(by=By.CSS_SELECTOR,value='#content > div > div.z7cS6-TO7X > div.FtuIjPoTdk > div._2jrC4tvN2w > div > a')
    review_box.click()
    time.sleep(1)
    while True:
        try:
            review_list = browser.find_elements(by=By.CSS_SELECTOR,value='#REVIEW > div > div._2LvIMaBiIO > div._2g7PKvqCKe > ul > li > div > div._3P12lHpgMB > div')
            for review_element in review_list:
                rating = review_element.find_element(by=By.CSS_SELECTOR,value='div._2V6vMO_iLm > em').text
                date = review_element.find_element(by=By.CSS_SELECTOR,value='div.iWGqB6S4Lq > span').text
                content = review_element.find_element(by=By.CSS_SELECTOR,value='div._3z6gI4oI6l > div > span').text
                print(title)
                print(region)
                print(rating)
                print(date)
                print(content)
                collection.insert_one({'title':title,
                            'region':region,
                            'good': rating,
                            'date':date,
                            'content':content})
            next_btn = browser.find_element(by=By.CSS_SELECTOR, value='a._2Ar8-aEUTq')
            next_btn.click()
            time.sleep(1)
        except:
            break    
    pass
    element_body = browser.find_element(by=By.CSS_SELECTOR,value="body")

    element_body.send_keys(Keys.HOME)
    time.sleep(1)
    back_btn = browser.find_element(by=By.CSS_SELECTOR,value='#content > div > div._3U1EEdeAc6 > div._2u_hEOSeOu > div > ul > li:nth-child(2) > a')
    back_btn.click()                                      # - 브라우저 종료
    