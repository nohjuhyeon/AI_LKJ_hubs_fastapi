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
# database 연결
database = mongoClient["AI_LKJ"]
# collection 작업
collection = database['reserve_transfer_total']
# collection.delete_many({})


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
browser.get("https://rent-car.zzimcar.com/home")                                     # - 주소 입력

                                                    # - 가능 여부에 대한 OK 받음
pass
html = browser.page_source                          # - html 파일 받음(and 확인)
# print(html)
time.sleep(2)
from selenium.webdriver.common.by import By          # - 정보 획득
region_click = browser.find_element(by=By.CSS_SELECTOR,value=" div.zone-list.grid.grid-cols-3.mt-4 > td:nth-child(2)")
region_click.click()
start_date = browser.find_element(by=By.CSS_SELECTOR,value="div.vc-day.id-2024-01-20 > span")
finish_date= browser.find_element(by=By.CSS_SELECTOR,value="div.vc-day.id-2024-01-25 > span")
time.sleep(1)
start_date.click()
finish_date.click()
search_button = browser.find_element(by=By.CSS_SELECTOR,value="#__layout > div > div.layout-body > div > div > div")
search_button.click()
time.sleep(3)

element_list = browser.find_elements(by=By.CSS_SELECTOR,value="#map-parent > section > div > article > div > div:nth-child(2) > div > ul > li")
for element_one in element_list:
    car_name = element_one.find_element(by=By.CSS_SELECTOR,value="dl > dd > div.title-box")
    print(car_name.text)
    pass
    image_tag = element_one.find_element(by=By.CSS_SELECTOR, value = 'li> dl > dt > div > img')
    car_image= image_tag.get_attribute('src')
    print(car_image)
    try:
        more_button = element_one.find_element(by=By.CSS_SELECTOR,value="div.btn-more-box > a")
        more_button.click()
    except:
        pass
    store_list = element_one.find_elements(by=By.CSS_SELECTOR,value=".list-store > li")
    for element_store in store_list:
        store_name = element_store.find_element(by=By.CSS_SELECTOR,value="a > dl > dt > div > strong")
        car_price = element_store.find_element(by=By.CSS_SELECTOR,value=" a > dl > dd > div > div > p")   
        print(store_name.text)
        print(car_price.text)
        collection.insert_one({"car_name": car_name.text,
                               "car_image": car_image,
                               "store_name" : store_name.text,
                               "car_price": car_price.text, 
                               "transfer_cate": "car"
                               })
        pass

browser.quit()                                      # - 브라우저 종료

# table:nth-child(1) > tbody > tr:nth-child(3) > td:nth-child(7) > div
# table:nth-child(1) > tbody > tr:nth-child(4) > td:nth-child(5) > div