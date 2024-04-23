## dbmongo의 collection 연결
from pymongo import MongoClient
mongoClient = MongoClient("mongodb://192.168.10.240:27017/AI_LKJ")

# database 연결
database = mongoClient["AI_LKJ"]

# collection 작업
collection = database['reserve_transfer_airport']
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
browser.get("https://flight-web.yanolja.com/flights/list?departurePlaceTypeCode=CITY&departurePlaceCode=SEL&arrivalPlaceTypeCode=CITY&arrivalPlaceCode=PUS&cabinClasses=ECONOMY,BUSINESS&adultsCount=4&outboundDepartureDate=2024-01-20")
pass
# html 파일 받음(and 확인)
html = browser.page_source
time.sleep(2)
pass
# 정보 획득
from selenium.webdriver.common.by import By
import time

airport_list = browser.find_elements(by=By.CSS_SELECTOR,value = "div.css-x97jm9.e1tjxvrm0 > div")

airport_image_list = []
airport_name_list = []
airport_time_list = []
airport_price_list = []
# airport_seat_list = []
for airport_item in airport_list :
    try :
        airport_tag = airport_item.find_element(by=By.CSS_SELECTOR, value = "div > a > div.airlineImageWrapper > img")
        str_airport_image= airport_tag.get_attribute('src')
        pass
    except :
        str_airport_image = ""
    airport_image_list.append(str_airport_image)
    pass
    
    try :
        airport_name = airport_item.find_element(by=By.CSS_SELECTOR, value = "div > div.leftArea > div.css-1grj4oy-TextStyled.e9cha6a0")
        str_airport_name = airport_name.text
        pass
    except :
        str_airport_name = ""
    airport_name_list.append(str_airport_name)
    pass
    
    try :
        airport_time = airport_item.find_element(by=By.CSS_SELECTOR, value = "div > div.leftArea > p.css-1wb6sft-TextStyled.e9cha6a0")
        str_airport_time = airport_time.text
        pass
    except :
        str_airport_time = ""
    airport_time_list.append(str_airport_time)
    pass
    
    try :
        airport_price = airport_item.find_elements(by=By.CSS_SELECTOR, value = " div > div.rightArea > div:nth-child(1) > p >span")
        str_airport_price = airport_price[0].text + airport_price[1].text
        pass
    except :
        str_airport_price = ""
    airport_price_list.append(str_airport_price)
    pass

    # try :
    #     airport_seat = airport_item.find_element(by=By.CSS_SELECTOR, value = "div > div.rightArea > div.css-np7xiy-TextStyled.e9cha6a0")
    #     str_airport_seat = airport_seat.text
    #     pass
    # except :
    #     str_airport_seat = ""
    # airport_seat_list.append(airport_seat_list)
    # pass

for i in range(len(airport_list)) :
    collection.insert_one({"airport_image" : airport_image_list[i],
                          "airport_name" : airport_name_list[i],
                          "airport_time" : airport_time_list[i],
                          "airport_price" : airport_price_list[i], 
                          "transfer_cate": "plane"})
pass
    
# 브라우저 종료
browser.quit()