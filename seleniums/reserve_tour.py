## dbmongo의 collection 연결
from pymongo import MongoClient
mongoClient = MongoClient("mongodb://192.168.10.240:27017/AI_LKJ")

# database 연결
database = mongoClient["AI_LKJ"]

# collection 작업
collection = database['reserve_tour']
collection.delete_many({})

# 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
webdriver_manager_directory = ChromeDriverManager().install()
import time

# ChromeDriver 실행
from selenium.webdriver.chrome.options import Options

# Chrome 브라우저 옵션 생성
chrome_options = Options()

# User-Agent 설정
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

# WebDriver 생성
webdriver_manager_dricetory = ChromeDriverManager().install()

# chrome browser 열기
browser = webdriver.Chrome(service = ChromeService(webdriver_manager_directory), options=chrome_options)                        

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# 주소 입력
browser.get("https://travel.interpark.com/voucher/list?q=%EB%B6%80%EC%82%B0&disp_q=%EB%B6%80%EC%82%B0&region1=&region2=&category1=&category2=&standard1=&standard2=&geo=")
pass
# html 파일 받음(and 확인)
html = browser.page_source
time.sleep(3)
pass
# 정보 획득
from selenium.webdriver.common.by import By
import time

tour_list = browser.find_elements(by=By.CSS_SELECTOR,value = "div.listProductWrap > ul > li > a")
time.sleep(3)

tour_image_list = []
tour_name_list = []
tour_content_list = []
tour_price_list = []
for tour_item in tour_list :
    try :
        tour_tag = tour_item.find_element(by=By.CSS_SELECTOR, value="div.listProductWrap > ul > li > a > span > img")
        str_tour_image = tour_tag.get_attribute('data-src')
        pass
    except :
        str_tour_image = ""
    tour_image_list.append(str_tour_image)
    pass

    try :
        tour_name = tour_item.find_element(by=By.CSS_SELECTOR, value="a > div > div.productInformation > div.productTitle")
        str_tour_name = tour_name.text
        pass
    except :
        str_tour_name = ""
    tour_name_list.append(str_tour_name)
    pass

    try :
        tour_content = tour_item.find_element(by=By.CSS_SELECTOR, value="a > div > div.productInformation > div.productDescriptionWrap")
        str_tour_content = tour_content.text
        pass
    except :
        str_tour_content = ""
    tour_content_list.append(str_tour_content)
    pass
        
    try :
        tour_price = tour_item.find_element(by=By.CSS_SELECTOR, value="a > div > div.productPriceWrapper > div.productPrice")
        str_tour_price = tour_price.text
        pass
    except :
        str_tour_price = ""
    tour_price_list.append(str_tour_price)
    pass
        
for i in range(len(tour_list)) :
    collection.insert_one({"tour_image" : tour_image_list[i],
                          "tour_name" : tour_name_list[i],
                          "tour_content" : tour_content_list[i],
                          "tour_price" : tour_price_list[i]})
pass

# 브라우저 종료
browser.quit()