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
collection = database['youtube_scaping_scrolling']

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
browser.get("https://www.youtube.com/@kimstravel")                                     # - 주소 입력

                                                    # - 가능 여부에 대한 OK 받음
pass
html = browser.page_source                          # - html 파일 받음(and 확인)
# print(html)

from selenium.webdriver.common.by import By          # - 정보 획득
from selenium.webdriver.common.keys import Keys
# browser.save_screenshot('./formats.png')     



# 동영상 버튼
video_button = browser.find_element(by=By.CSS_SELECTOR, value="yt-tab-shape:nth-child(2) > div.yt-tab-shape-wiz__tab")
video_button.click()
time.sleep(1)
#인기순 버튼
best_button = browser.find_element(by=By.CSS_SELECTOR, value="#chips > yt-chip-cloud-chip-renderer:nth-child(2)")
best_button.click()

for x in range(10):    # body 엘리먼트 찾기
    element_body = browser.find_element(by = By.CSS_SELECTOR, value = "body")
    # 스크롤 다운
    element_body.send_keys(Keys.END)                                                        # scroll 길게 함
    # 현재 스크롤 높이 가져오기
    time.sleep(1)
    current_scrollHeight = browser.execute_script("return document.body.scrollHeight")      # 현재의 scrollheight를 while문 안에 넣어 반복하여 길게 함.


    # 여러개 동영상 collection 있을때 버튼
    count_buttons = browser.find_elements(by=By.CSS_SELECTOR, value="#content.style-scope ytd-rich-item-renderer")

    time.sleep(1)

    for count_button in count_buttons :
        count_button.click()
        time.sleep(2)
        # 설명 더보기 버튼
        expand_button = browser.find_element(by=By.CSS_SELECTOR, value="#expand")
        expand_button.click()

        # 스크롤

        for i in range(10):    # body 엘리먼트 찾기
            element_body = browser.find_element(by = By.CSS_SELECTOR, value = "body")
            # 스크롤 다운
            element_body.send_keys(Keys.END)                                                        # scroll 길게 함
            # 현재 스크롤 높이 가져오기
            time.sleep(1)
            current_scrollHeight = browser.execute_script("return document.body.scrollHeight")      # 현재의 scrollheight를 while문 안에 넣어 반복하여 길게 함.
            
            
        time.sleep(1)


        # 제목,날짜,조회수,좋아요,설명
        title = browser.find_element(by=By.CSS_SELECTOR, value="#title > h1")
        date = browser.find_element(by=By.CSS_SELECTOR, value="#info > span:nth-child(3)")
        views = browser.find_element(by=By.CSS_SELECTOR, value="#info > span:nth-child(1)")
        recommend = browser.find_element(by=By.CSS_SELECTOR, value="toggle-button-view-model > button-view-model > button > div.yt-spec-button-shape-next__button-text-content")
        contents = browser.find_element(by=By.CSS_SELECTOR, value="#description-inline-expander > yt-attributed-string")
        time.sleep(1)

        # 댓글리스트
        list_reply = browser.find_elements(by=By.CSS_SELECTOR, value="#content-text > span")
        for reply in list_reply:
            print(reply.text)
            # db에 집어넣기
            # collection.insert_one({
            # "title": title.text,
            # "date": date.text,
            # "views": views.text,
            # "recommend": recommend.text,
            # "contents": contents.text,
            # "reply" : reply.text
            # })

            
        browser.back()
        pass

browser.quit()                                      # - 브라우저 종료
