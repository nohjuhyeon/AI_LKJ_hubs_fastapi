# * 웹 크롤링 동작
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

browser = webdriver.Chrome(service = ChromeService(webdriver_manager_directory), options=chrome_options)                        # - chrome browser 열기

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

pass
browser.get("https://datalab.visitkorea.or.kr/datalab/portal/loc/getAreaDataForm.do#")                                     # - 주소 입력

                                                    # - 가능 여부에 대한 OK 받음
pass
html = browser.page_source                          # - html 파일 받음(and 확인)
# print(html)
from selenium.webdriver.common.by import By          # - 정보 획득
from selenium.webdriver.common.keys import Keys
date_start = browser.find_element(By.CSS_SELECTOR,"#monthStart")
date_end = browser.find_element(By.CSS_SELECTOR,"#monthEnd")
for i in range(6):
    date_start.send_keys(Keys.BACKSPACE)
date_start.send_keys("202101")
for i in range(6):
    date_end.send_keys(Keys.BACKSPACE)
date_end.send_keys("202112")
date_yes = browser.find_element(By.CSS_SELECTOR,"#lookup-wrap > input")
date_yes.click()
time.sleep(10)
pass
region_menu = browser.find_element(By.CSS_SELECTOR, "#area-select")
region_select = browser.find_elements(By.CSS_SELECTOR,"#srchNatCdList1 > a")
for i in range(0,len(region_select)-1):
    region_menu = browser.find_element(By.CSS_SELECTOR, "#area-select")
    region_menu.click() 
    time.sleep(5)
    region_select[i].click()
    region_yes = browser.find_element(By.CSS_SELECTOR,"#popup1 > div.modal-foot > div > a.button.bg-blue.modal-close")
    region_yes.click()
    time.sleep(5)
    visitor_select= browser.find_element(By.CSS_SELECTOR,"#tab2on")
    visitor_select.click()
    time.sleep(5)
    concept_visitor = browser.find_element(By.CSS_SELECTOR,"#\\31 2762 > div.top > div.menu-more-wrap > a")
    concept_visitor.click()
    concept_downroad = browser.find_element(By.CSS_SELECTOR,"#\\31 2762 > div.top > div.menu-more-wrap > ul > li:nth-child(2) > p:nth-child(2) > a")
    concept_downroad.click()
    time.sleep(5)
    question_check = browser.find_element(By.CSS_SELECTOR,"#dataUtilExmnUl > li:nth-child(3) > label")
    question_check.click()
    question_yes =  browser.find_element(By.CSS_SELECTOR,"#submit")
    question_yes.click()
    time.sleep(15)

    consume_click = browser.find_element(By.CSS_SELECTOR,"#tab4 > a")
    consume_click.click()
    time.sleep(10)

    concept_consume = browser.find_element(By.CSS_SELECTOR,"#\\31 269 > div.top > div.menu-more-wrap > a")
    concept_consume.click()
    concept_consume_downroad = browser.find_element(By.CSS_SELECTOR,'#\\31 269 > div.top > div.menu-more-wrap > ul > li:nth-child(2) > p:nth-child(3) > a')
    concept_consume_downroad.click()
    time.sleep(5)
    question_check = browser.find_element(By.CSS_SELECTOR,"#dataUtilExmnUl > li:nth-child(3) > label")
    question_check.click()
    question_yes =  browser.find_element(By.CSS_SELECTOR,"#submit")
    question_yes.click()
    time.sleep(15)

    concept_consume_entire = browser.find_element(By.CSS_SELECTOR,"#\\31 242 > div.top > div.menu-more-wrap > a")
    concept_consume_entire.click()
    concept_consume_entire_downroad = browser.find_element(By.CSS_SELECTOR,'#\\31 242 > div.top > div.menu-more-wrap > ul > li:nth-child(2) > p:nth-child(3) > a')
    concept_consume_entire_downroad.click()
    time.sleep(5)
    question_check = browser.find_element(By.CSS_SELECTOR,"#dataUtilExmnUl > li:nth-child(3) > label")
    question_check.click()
    question_yes =  browser.find_element(By.CSS_SELECTOR,"#submit")
    question_yes.click()
    time.sleep(15)

    trend_click = browser.find_element(By.CSS_SELECTOR,"#tab5 > a")
    trend_click.click()
    time.sleep(10)

    trend_search = browser.find_element(By.CSS_SELECTOR,"#\\31 273 > div.top > div.menu-more-wrap > a")
    trend_search.click()
    trend_search_downroad = browser.find_element(By.CSS_SELECTOR,'#\\31 273 > div.top > div.menu-more-wrap > ul > li:nth-child(2) > p:nth-child(2) > a')
    trend_search_downroad.click()
    time.sleep(5)
    question_check = browser.find_element(By.CSS_SELECTOR,"#dataUtilExmnUl > li:nth-child(3) > label")
    question_check.click()
    question_yes =  browser.find_element(By.CSS_SELECTOR,"#submit")
    question_yes.click()
    time.sleep(15)

    trend_keyword = browser.find_element(By.CSS_SELECTOR,"#\\31 275 > div.top > div.menu-more-wrap > a")
    trend_keyword.click()
    trend_keyword_downroad = browser.find_element(By.CSS_SELECTOR,'#\\31 275 > div.top > div.menu-more-wrap > ul > li:nth-child(2) > p > a')
    trend_keyword_downroad.click()
    time.sleep(5)
    question_check = browser.find_element(By.CSS_SELECTOR,"#dataUtilExmnUl > li:nth-child(3) > label")
    question_check.click()
    question_yes =  browser.find_element(By.CSS_SELECTOR,"#submit")
    question_yes.click()
    time.sleep(20)
    pass

    attraction_click = browser.find_element(By.CSS_SELECTOR,"#tab6 > a")
    attraction_click.click()
    time.sleep(5)

    attraction_search = browser.find_element(By.CSS_SELECTOR,"#\\31 211 > div.top > div.menu-more-wrap > a")
    attraction_search.click()
    attraction_search_downroad = browser.find_element(By.CSS_SELECTOR,'#\\31 211 > div.top > div.menu-more-wrap > ul > li:nth-child(2) > p > a')
    attraction_search_downroad.click()
    time.sleep(5)
    question_check = browser.find_element(By.CSS_SELECTOR,"#dataUtilExmnUl > li:nth-child(3) > label")
    question_check.click()
    question_yes =  browser.find_element(By.CSS_SELECTOR,"#submit")
    question_yes.click()
    time.sleep(30)

    retaurant = browser.find_element(By.CSS_SELECTOR,"#\\31 212 > div.top > div.menu-more-wrap > a")
    retaurant.click()
    retaurant_downroad = browser.find_element(By.CSS_SELECTOR,'#\\31 212 > div.top > div.menu-more-wrap > ul > li:nth-child(2) > p > a')
    retaurant_downroad.click()
    time.sleep(5)
    question_check = browser.find_element(By.CSS_SELECTOR,"#dataUtilExmnUl > li:nth-child(3) > label")
    question_check.click()
    question_yes =  browser.find_element(By.CSS_SELECTOR,"#submit")
    question_yes.click()
    time.sleep(30)
    pass

date_start = browser.find_element(By.CSS_SELECTOR,"#monthStart")
date_end = browser.find_element(By.CSS_SELECTOR,"#monthEnd")
for i in range(6):
    date_start.send_keys(Keys.BACKSPACE)
date_start.send_keys("202001")
for i in range(6):
    date_end.send_keys(Keys.BACKSPACE)
date_end.send_keys("202012")
date_yes = browser.find_element(By.CSS_SELECTOR,"#lookup-wrap > input")
date_yes.click()
time.sleep(5)
pass
region_menu = browser.find_element(By.CSS_SELECTOR, "#area-select")
region_select = browser.find_elements(By.CSS_SELECTOR,"#srchNatCdList1 > a")
for i in range(0,len(region_select)-1):
    region_menu = browser.find_element(By.CSS_SELECTOR, "#area-select")
    region_menu.click() 
    time.sleep(5)
    region_select[i].click()
    region_yes = browser.find_element(By.CSS_SELECTOR,"#popup1 > div.modal-foot > div > a.button.bg-blue.modal-close")
    region_yes.click()
    time.sleep(10)
    visitor_select= browser.find_element(By.CSS_SELECTOR,"#tab2on")
    visitor_select.click()
    time.sleep(5)
    concept_visitor = browser.find_element(By.CSS_SELECTOR,"#\\31 2762 > div.top > div.menu-more-wrap > a")
    concept_visitor.click()
    concept_downroad = browser.find_element(By.CSS_SELECTOR,"#\\31 2762 > div.top > div.menu-more-wrap > ul > li:nth-child(2) > p:nth-child(2) > a")
    concept_downroad.click()
    time.sleep(10)
    question_check = browser.find_element(By.CSS_SELECTOR,"#dataUtilExmnUl > li:nth-child(3) > label")
    question_check.click()
    question_yes =  browser.find_element(By.CSS_SELECTOR,"#submit")
    question_yes.click()
    time.sleep(15)

    consume_click = browser.find_element(By.CSS_SELECTOR,"#tab4 > a")
    consume_click.click()
    time.sleep(10)

    concept_consume = browser.find_element(By.CSS_SELECTOR,"#\\31 269 > div.top > div.menu-more-wrap > a")
    concept_consume.click()
    concept_consume_downroad = browser.find_element(By.CSS_SELECTOR,'#\\31 269 > div.top > div.menu-more-wrap > ul > li:nth-child(2) > p:nth-child(3) > a')
    concept_consume_downroad.click()
    time.sleep(3)
    question_check = browser.find_element(By.CSS_SELECTOR,"#dataUtilExmnUl > li:nth-child(3) > label")
    question_check.click()
    question_yes =  browser.find_element(By.CSS_SELECTOR,"#submit")
    question_yes.click()
    time.sleep(15)

    concept_consume_entire = browser.find_element(By.CSS_SELECTOR,"#\\31 242 > div.top > div.menu-more-wrap > a")
    concept_consume_entire.click()
    concept_consume_entire_downroad = browser.find_element(By.CSS_SELECTOR,'#\\31 242 > div.top > div.menu-more-wrap > ul > li:nth-child(2) > p:nth-child(3) > a')
    concept_consume_entire_downroad.click()
    time.sleep(2)
    question_check = browser.find_element(By.CSS_SELECTOR,"#dataUtilExmnUl > li:nth-child(3) > label")
    question_check.click()
    question_yes =  browser.find_element(By.CSS_SELECTOR,"#submit")
    question_yes.click()
    time.sleep(15)

    trend_click = browser.find_element(By.CSS_SELECTOR,"#tab5 > a")
    trend_click.click()
    time.sleep(5)

    trend_search = browser.find_element(By.CSS_SELECTOR,"#\\31 273 > div.top > div.menu-more-wrap > a")
    trend_search.click()
    trend_search_downroad = browser.find_element(By.CSS_SELECTOR,'#\\31 273 > div.top > div.menu-more-wrap > ul > li:nth-child(2) > p:nth-child(2) > a')
    trend_search_downroad.click()
    time.sleep(5)
    question_check = browser.find_element(By.CSS_SELECTOR,"#dataUtilExmnUl > li:nth-child(3) > label")
    question_check.click()
    question_yes =  browser.find_element(By.CSS_SELECTOR,"#submit")
    question_yes.click()
    time.sleep(15)

    trend_keyword = browser.find_element(By.CSS_SELECTOR,"#\\31 275 > div.top > div.menu-more-wrap > a")
    trend_keyword.click()
    trend_keyword_downroad = browser.find_element(By.CSS_SELECTOR,'#\\31 275 > div.top > div.menu-more-wrap > ul > li:nth-child(2) > p > a')
    trend_keyword_downroad.click()
    time.sleep(5)
    question_check = browser.find_element(By.CSS_SELECTOR,"#dataUtilExmnUl > li:nth-child(3) > label")
    question_check.click()
    question_yes =  browser.find_element(By.CSS_SELECTOR,"#submit")
    question_yes.click()
    time.sleep(15)
    pass

    attraction_click = browser.find_element(By.CSS_SELECTOR,"#tab6 > a")
    attraction_click.click()
    time.sleep(5)

    attraction_search = browser.find_element(By.CSS_SELECTOR,"#\\31 211 > div.top > div.menu-more-wrap > a")
    attraction_search.click()
    attraction_search_downroad = browser.find_element(By.CSS_SELECTOR,'#\\31 211 > div.top > div.menu-more-wrap > ul > li:nth-child(2) > p > a')
    attraction_search_downroad.click()
    time.sleep(5)
    question_check = browser.find_element(By.CSS_SELECTOR,"#dataUtilExmnUl > li:nth-child(3) > label")
    question_check.click()
    question_yes =  browser.find_element(By.CSS_SELECTOR,"#submit")
    question_yes.click()
    time.sleep(20)

    retaurant = browser.find_element(By.CSS_SELECTOR,"#\\31 212 > div.top > div.menu-more-wrap > a")
    retaurant.click()
    retaurant_downroad = browser.find_element(By.CSS_SELECTOR,'#\\31 212 > div.top > div.menu-more-wrap > ul > li:nth-child(2) > p > a')
    retaurant_downroad.click()
    time.sleep(5)
    question_check = browser.find_element(By.CSS_SELECTOR,"#dataUtilExmnUl > li:nth-child(3) > label")
    question_check.click()
    question_yes =  browser.find_element(By.CSS_SELECTOR,"#submit")
    question_yes.click()
    time.sleep(40)
    pass


browser.quit()                                      # - 브라우저 종료
