# * 웹 크롤링 동작
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
webdriver_manager_directory = ChromeDriverManager().install()
import time
# ChromeDriver 실행

from selenium.webdriver.chrome.options import Options

from pymongo import MongoClient

try :
    mongoClient = MongoClient("mongodb://192.168.10.240:27017/")
    database = mongoClient["AI_LKJ"]
    collection = database['tmon_scrapping']

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
    browser.get("https://www.tmon.co.kr/deal/10716684222?keyword=%ED%88%AC%EC%96%B4%ED%8C%A8%EC%8A%A4&tl_area=SKJCD&tl_ord=2&searchClick=DL%7CND%7CBM&tab=&thr=hs#tab=review")                                     # - 주소 입력

                                                        # - 가능 여부에 대한 OK 받음
    pass
    html = browser.page_source                          # - html 파일 받음(and 확인)
    # print(html)

    from selenium.webdriver.common.by import By          # - 정보 획득
    from selenium.webdriver.common.keys import Keys
    # browser.save_screenshot('./formats.png')         
    
    # # 리뷰 오픈
    # element_review_open = browser.find_element(by=By.CSS_SELECTOR, value="#_dealReviewWrap > div.deal_review > div > button")
    # element_review_open.click() # 리뷰 버튼 클릭
    time.sleep(2)
    # # 맨 아래로 스크롤
    # element_body = browser.find_element(by = By.CSS_SELECTOR, value = "body")
    # element_body.send_keys(Keys.END)
    # time.sleep(2) 

    # 상품 이름 (1)
    element_title = browser.find_element(by=By.CSS_SELECTOR, value="div.deal_title > h2")


    # 리뷰
    element_reivew = browser.find_elements(by=By.CSS_SELECTOR, value="div.review_block")
    # 리뷰 내용 (2)
    element_text = browser.find_elements(by=By.CSS_SELECTOR, value="div.review_block_text > div")
    # 날짜 (3)
    element_date = browser.find_elements(by=By.CSS_SELECTOR, value="div.review_block > ul > li:nth-child(2)")
    # 별점 (4)
    element_star = browser.find_elements(by=By.CSS_SELECTOR, value="span.star_rate > span > span")
    # 지역 (5)
    # 직접 넣기

    # ===================================================================================================


    # 페이지 버튼
    element_pagination = browser.find_elements(by=By.CSS_SELECTOR, value="div#reviewPaginate > div.pagination > a")
    element_pagination[0].click()
    time.sleep(1)
    element_pagination = browser.find_elements(by=By.CSS_SELECTOR, value="div#reviewPaginate > div.pagination > a")
    element_pagination[1].click()
    time.sleep(1)   

    while True:
        # 스크래핑 시작
        element_pagination = browser.find_elements(by=By.CSS_SELECTOR, value="div#reviewPaginate > div.pagination > a")
        for x in range(4,len(element_pagination)-2) : # 페이지 1부터 10번까지
            element_pagination = browser.find_elements(by=By.CSS_SELECTOR, value="div#reviewPaginate > div.pagination > a")
            element_pagination[x].click()
            time.sleep(2)   
        time.sleep(1)
        
        # element_next = browser.find_element(by=By.CSS_SELECTOR, value="#reviewPaginate > div > a.next_page") #다음 버튼 누르기
        element_next = browser.find_element(by=By.XPATH, value='//*[@id="reviewPaginate"]/div/a[13]') #다음 버튼 누르기
        element_next.click()

except :
    browser.quit()
# element_pagination = browser.find_elements(by=By.CSS_SELECTOR, value="div#reviewPaginate > div.pagination > a")
# for x in range(4,len(element_pagination)-2) : # 페이지 1부터 10번까지
#     element_pagination = browser.find_elements(by=By.CSS_SELECTOR, value="div#reviewPaginate > div.pagination > a")
#     element_pagination[x].click()
#     time.sleep(2)   

# element_next = browser.find_element(by=By.CSS_SELECTOR, value="#reviewPaginate > div > a.next_page")
# element_next.click()

# element_pagination = browser.find_elements(by=By.CSS_SELECTOR, value="div#reviewPaginate > div.pagination > a")
# for x in range(4,len(element_pagination)-2) : # 페이지 1부터 10번까지
#     element_pagination = browser.find_elements(by=By.CSS_SELECTOR, value="div#reviewPaginate > div.pagination > a")
#     element_pagination[x].click()
#     time.sleep(2)



# # db에 집어넣기
# collection.insert_one({
#         'title':title,
#         'region':region,
#         'good': rating,
#         'date':date,
#         'content':content})

                                # - 브라우저 종료
