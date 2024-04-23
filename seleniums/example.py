## dbmongo의 collection 연결
from pymongo import MongoClient
mongoClient = MongoClient("mongodb://192.168.10.240:27017")
# database 연결
database = mongoClient["AI_LKJ"]
# collection 작업
collection = database['database_name']
collection.delete_many({})


# * 웹 크롤링 동작
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
# Chrome 브라우저 옵션 생성
chrome_options = Options()
# User-Agent 설정
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
from webdriver_manager.chrome import ChromeDriverManager
webdriver_manager_directory = ChromeDriverManager().install()
# WebDriver 생성
browser = webdriver.Chrome(service = ChromeService(webdriver_manager_directory), options=chrome_options)                        # - chrome browser 열기
# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

pass
browser.get("https://pedia.watcha.com/ko-KR/contents/md76rkk/comments")                                     # - 주소 입력

                                                    # - 가능 여부에 대한 OK 받음
pass
html = browser.page_source                          # - html 파일 받음(and 확인)
# print(html)

from selenium.webdriver.common.by import By          # - 정보 획득
from selenium.webdriver.common.keys import Keys
import time

element_body = browser.find_element(by=By.CSS_SELECTOR,value="body")
previous_scrollHeight = 0

while True:
# for i in range(3):
    element_body.send_keys(Keys.END)
    current_scrollHeight = browser.execute_script("return document.body.scrollHeight")
    if previous_scrollHeight >= current_scrollHeight:
        break
    else:
        previous_scrollHeight = current_scrollHeight
    time.sleep(3)
pass
user_list = element_body.find_elements(by=By.CSS_SELECTOR,value = "div.css-13j4ly.egj9y8a4")
user_name_list = []
grade_list = []
content_list = []
for user_item in user_list:
    try:
        user_name = user_item.find_element(by=By.CSS_SELECTOR,value = "div.css-drz8qh.egj9y8a2")                    # 작성자 정보 추출
        str_user_name = user_name.text
    except: 
        str_user_name = ""
    user_name_list.append(str_user_name)
    try:
        grade = user_item.find_element(by=By.CSS_SELECTOR,value = "div.css-31ods0.egj9y8a0")                        # 별점 점수 정보 추출
        str_grade = grade.text
    except:
        str_grade = ""
    grade_list.append(str_grade)
    try:
        content = user_item.find_element(by=By.CSS_SELECTOR,value = "div.css-2occzs.egj9y8a1")                      # 내용 정보 추출                                                                             # 데이터 데이스에 정보 전달
        str_content = content.text
    except:
        str_content = ""
    content_list.append(str_content)
for i in range(len(user_list)):
    collection.insert_one({"작성자": user_name_list[i],                                                         
                            "별점 점수": grade_list[i],
                            "내용": content_list[i]})

pass
browser.quit()                                      # - 브라우저 종료

# 작성자: div.css-drz8qh.egj9y8a2
# 별점: div.css-31ods0.egj9y8a0
# 내용: div.css-2occzs.egj9y8a1