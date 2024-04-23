## dbmongo의 collection 연결
from pymongo import MongoClient
mongoClient = MongoClient("mongodb://192.168.10.240:27017")
# database 연결
database = mongoClient["AI_LKJ"]
# collection 작업
collection = database['tour_contents']
# collection.delete_many({})


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
browser.get("https://travel.naver.com/domestic/01/guide/all")                                     # - 주소 입력

                                                    # - 가능 여부에 대한 OK 받음
pass
html = browser.page_source                          # - html 파일 받음(and 확인)
# print(html)

from selenium.webdriver.common.by import By          # - 정보 획득
from selenium.webdriver.common.keys import Keys
import time

# 돋보기
search_button = "div.header_sub__z2ac0 > button"
element_search = browser.find_element(by=By.CSS_SELECTOR, value=search_button)

element_search.click()

# 지역
region_button = "div.searchbox_svc_tabs__MkKLI > a.searchbox_svc_tab__kjMI2"
element_region = browser.find_elements(by=By.CSS_SELECTOR, value=region_button)


# element_search.click()
# time.sleep(1)

pass
for x in range(14,15):
    
    region_button = "div.searchbox_svc_tabs__MkKLI > a.searchbox_svc_tab__kjMI2"
    element_region = browser.find_elements(by=By.CSS_SELECTOR, value=region_button)
    element_region[x].click()
    region_text = element_region[x].text
    time.sleep(1)
    # 세부지역
    detail_region_button = "div.searchbox_svc_PanelItem__nQUao.as_domestic > a"
    element_detail = browser.find_element(by=By.CSS_SELECTOR, value=detail_region_button)
    element_detail.click()
    time.sleep(1)
    # 여행컨텐츠 버튼
    contents_button = "nav > div > a:nth-child(2)"
    element_contents = browser.find_element(by=By.CSS_SELECTOR, value=contents_button)
    element_contents.click()
    time.sleep(1)   

    while True:
        try :
            #더보기 버튼
            more_button = "div > div > main > div> div.guide_GuidePanel__hO6Rf > div > div > button"
            element_more = browser.find_element(by=By.CSS_SELECTOR, value=more_button)
            # 더보기 버튼을 찾아 클릭
            element_more.click()
            time.sleep(1)
        except :
            break
        
    list_review = []
    # 리뷰 제목
    review_title = "b.guide_name__OKy4W.expandableText_EllipsisText__gaduJ"
    element_review = browser.find_elements(by=By.CSS_SELECTOR, value=review_title)
    for z in range(len(element_review)):
        # 리뷰 제목
        review_title = "b.guide_name__OKy4W.expandableText_EllipsisText__gaduJ"
        element_review = browser.find_elements(by=By.CSS_SELECTOR, value=review_title)
        review_text = element_review[z].text
        
        # MongoDB에 저장
        collection.insert_one({"review_text": review_text , "지역" :region_text })
        
    search_button = "div.header_sub__z2ac0 > button"
    element_search = browser.find_element(by=By.CSS_SELECTOR, value=search_button)
    element_search.click()

pass
browser.quit()                                      # - 브라우저 종료
