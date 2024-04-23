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
browser.get("http://192.168.10.240:8000/")                                     # - 주소 입력

                                                    # - 가능 여부에 대한 OK 받음
pass
html = browser.page_source                          # - html 파일 받음(and 확인)
# print(html)

from selenium.webdriver.common.by import By          # - 정보 획득
# browser.save_screenshot('./formats.png')           
time.sleep(5)
login = browser.find_element(by=By.CSS_SELECTOR,value="body > div.container > div > div > header > ul > li:nth-child(1) > a")
login.click()
time.sleep(3)
insert = browser.find_element(by=By.CSS_SELECTOR,value="body > div > main > div > form > div > div:nth-child(5) > button:nth-child(2)")
insert.click()
time.sleep(2)
email_input = browser.find_element(by=By.CSS_SELECTOR,value="#email")
password_input = browser.find_element(by=By.CSS_SELECTOR,value="#password")
password_check = browser.find_element(by=By.CSS_SELECTOR,value="#password_check")
user_name = browser.find_element(by=By.CSS_SELECTOR,value="#user_name")
user_date = browser.find_element(by=By.CSS_SELECTOR,value="#user_birth")
user_phone = browser.find_element(by=By.CSS_SELECTOR,value="#phone")
user_address = browser.find_element(by=By.CSS_SELECTOR,value="#address")

email_input.send_keys("njh2205@gmail.com")
password_input.send_keys("1234")
password_check.send_keys("12345")
user_name.send_keys("주현")
user_date.send_keys("19980205")
user_phone.send_keys("01012345678")
user_address.send_keys("서울")
time.sleep(5)
browser.quit()                                      # - 브라우저 종료
