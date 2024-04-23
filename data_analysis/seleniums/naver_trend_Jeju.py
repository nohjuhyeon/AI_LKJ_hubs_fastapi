## dbmongo의 collection 연결
from pymongo import MongoClient
mongoClient = MongoClient("mongodb://192.168.10.240:27017")
# database 연결
database = mongoClient["AI_LKJ"]
collection = database['festival_Jeju']
collection.delete_many({})

# 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

import time


# Chrome 드라이버 설치 디렉터리 설정
webdriver_manager_directory = ChromeDriverManager().install()

# Chrome 브라우저 옵션 설정
chrome_options = Options()
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

# WebDriver 생성
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory), options=chrome_options)

# 크롤링할 웹 페이지 URL
url = "https://recomarea.com/festival/FestivalMain"

# 웹 페이지 열기
html_source = browser.get(url)

# 시작 날짜를 입력하는 입력란 찾기
start_date_input = browser.find_element(by=By.CSS_SELECTOR, value='body > section > div.container-fluid.PanelArea > div.container.CtlArea.py-5.mb-4 > div:nth-child(2) > div > div > div > div:nth-child(1) > div > input.form-control.MinTime')

#입력란 클릭하여 포커스 활성화
start_date_input.click()

# 입력란 내용 지우기
start_date_input.clear()

# 입력란에 시작 날짜 입력('2023-01-01)
start_date_input.send_keys('2023')
start_date_input.send_keys(Keys.TAB)
start_date_input.send_keys('0101')


# 엔터 키 입력하여 입력 완료
start_date_input.send_keys(Keys.ENTER)


# 끝나는 날짜 
end_date_input = browser.find_element(by=By.CSS_SELECTOR, value='body > section > div.container-fluid.PanelArea > div.container.CtlArea.py-5.mb-4 > div:nth-child(2) > div > div > div > div:nth-child(1) > div > input.form-control.MaxTime')

# 입력한 클릭하여 포커스 활성화
end_date_input.click()

# 입력란 내용 지우기
end_date_input.clear()

# 입력란에 끝 날짜 입력('2023-12-31')
end_date_input.send_keys('2023')
end_date_input.send_keys(Keys.TAB)
end_date_input.send_keys('1231')

# 엔터 키 입력하여 입력 완료
end_date_input.send_keys(Keys.ENTER)


# 검색창 요소 찾기
search_box = browser.find_element(by=By.CSS_SELECTOR, value = 'body > section > div.container-fluid.PanelArea > div.container.CtlArea.py-5.mb-4 > div:nth-child(2) > div > div > div > div:nth-child(2) > div > input')

# 검색어 입력
search_keyword = '제주'
search_box.send_keys(search_keyword)

# 엔터 키 입력(검색 실행)
search_box.send_keys(Keys.ENTER)

time.sleep(2)

# 프레임 식별
# 텍스트 추출
find_cards = browser.find_elements(by=By.CSS_SELECTOR, value='div.FestivalListArea > div > div > div > div')

for find_card in find_cards :
    title = find_card.find_element(by=By.CSS_SELECTOR, value='h4').text
    span_in_address = find_card.find_elements(by=By.CSS_SELECTOR, value='p:nth-child(1)')
    if span_in_address :
        address = find_card.find_element(by=By.CSS_SELECTOR, value='p:nth-child(4)').text
    else :
        address = find_card.find_element(by=By.CSS_SELECTOR, value='p:nth-child(3)').text
    count_num = len(find_card.find_elements(by=By.CSS_SELECTOR, value='p')) + 1
    date = find_card.find_element(by=By.CSS_SELECTOR, value='p:nth-child({})'.format(count_num)).text        


 # 지역 열 추가적으로 삽입
    add_data = '제주'

    # mongodb 삽입
    data = {
        'region' : add_data,
        'title': title,
        'address' : address,
        'date' : date
    }

    # MongoDB 컬렉션에 데이터 삽입
    collection.insert_one(data)

print("데이터가 MongoDB에 성공적으로 삽입되었습니다.")