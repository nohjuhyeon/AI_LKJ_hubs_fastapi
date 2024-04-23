# * 웹 크롤링 동작
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
# ChromeDriver 실행

from selenium.webdriver.chrome.options import Options

from pymongo import MongoClient
def yeomi_scraping():
    try:
        webdriver_manager_directory = ChromeDriverManager().install()
        mongoClient = MongoClient("mongodb://192.168.10.240:27017/AI_LKJ")

        # database 연결
        database = mongoClient["AI_LKJ"]

        # collection 작업
        collection = database['yeomi_review']
        # collection.delete_many({})
        # Chrome 브라우저 옵션 생성
        check_dict=collection.find({}, {'_id':0,'check_point': 1})
        check_list=[]
        for i in check_dict:
            if i['check_point'] not in check_list:
                check_list.append(i['check_point'])
        pass
        chrome_options = Options()

        # User-Agent 설정
        chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

        # WebDriver 생성
        webdriver_manager_dricetory = ChromeDriverManager().install()

        browser = webdriver.Chrome(service = ChromeService(webdriver_manager_directory), options=chrome_options)                        # - chrome browser 열기

        # Chrome WebDriver의 capabilities 속성 사용
        capabilities = browser.capabilities

        pass
        browser.get("https://www.instagram.com/yeomi.travel/")                                     # - 주소 입력

                                                            # - 가능 여부에 대한 OK 받음
        pass
        time.sleep(5)
        from selenium.webdriver.common.by import By          # - 정보 획득
        from selenium.webdriver.common.keys import Keys
        # 로그인 하기
        login_btn = browser.find_element(by=By.CSS_SELECTOR, value='div._acuq._acur > div > div > div> div:nth-child(1) > a')
        login_btn.click()
        time.sleep(3)

        email_input = browser.find_element(by=By.CSS_SELECTOR,value='#loginForm > div > div:nth-child(1) > div > label > input')
        email_input.send_keys('njh02052720')
        pswd_input = browser.find_element(by=By.CSS_SELECTOR,value='#loginForm > div > div:nth-child(2) > div > label > input')
        pswd_input.send_keys('njh12345!')
        login_check_btn = browser.find_element(by=By.CSS_SELECTOR,value='#loginForm > div > div:nth-child(3) > button')
        login_check_btn.click()
        time.sleep(5)
        pass_btn = browser.find_element(by=By.CSS_SELECTOR,value='div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > section > main > div > div > div > div > div')
        pass_btn.click()
        time.sleep(3)

        # facebook_btn = browser.find_element(by=By.CSS_SELECTOR,value='#loginForm > div > div:nth-child(5) > button')
        # facebook_btn.click()
        # email_input = browser.find_element(by=By.CSS_SELECTOR,value='#email')
        # email_input.send_keys('01038387360')
        # pswd_input = browser.find_element(by=By.CSS_SELECTOR,value='#pass')
        # pswd_input.send_keys('wngus2720!')
        # login_check_btn = browser.find_element(by=By.CSS_SELECTOR,value='#loginbutton')
        # login_check_btn.click()
        # time.sleep(10)
        # user_choice_btn = browser.find_element(by=By.CSS_SELECTOR,value='div.x1tu34mt ')
        # user_choice_btn.click()
        # time.sleep(10)
        pass
        element_body = browser.find_element(by=By.CSS_SELECTOR,value="body")
        previous_scrollHeight = 0
        time.sleep(3)
        for end in range(200):
            # try:
            #     next_btn = browser.find_element(by=By.CSS_SELECTOR,value='body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div:nth-child(1) > div > div > div._aaqg._aaqh > button')
            #     next_btn.click()
            #     time.sleep(1)
            # except:
            #     break
            element_body.send_keys(Keys.END)
            current_scrollHeight = browser.execute_script("return document.body.scrollHeight")
            if previous_scrollHeight >= current_scrollHeight:
                break
            else:
                previous_scrollHeight = current_scrollHeight
            time.sleep(5)
        content_list = browser.find_elements(by=By.CSS_SELECTOR,value='div._aagw')
        content_alt_list = browser.find_elements(by=By.CSS_SELECTOR,value='div.x1lliihq  > a.x1i10hfl')
        element_body = browser.find_element(by=By.CSS_SELECTOR,value="body")
        while True : 
            first_content=''
            content_list = browser.find_elements(by=By.CSS_SELECTOR,value='div._aagw')
            content_alt_list = browser.find_elements(by=By.CSS_SELECTOR,value='div.x1lliihq  > a.x1i10hfl')
            for i in range(len(content_alt_list)):
                if str(content_alt_list[len(content_alt_list)-i-1].get_attribute('href')).split('/')[4] not in check_list:
                    first_content = content_list[len(content_alt_list)-i-1]
                    break
            if first_content == '':
                element_body.send_keys(Keys.PAGE_UP)
                time.sleep(1)
            else:
                break
        first_content.click()

        time.sleep(3)

        pass
        for i in range(36):
            card_content=''
            card_date=''
            card_like=''
            card_watch=''
            card_reviews=[]
            while True:
                try:
                    plus_btn = browser.find_element(by=By.CSS_SELECTOR,value='div.x9f619 > button._abl-')
                    plus_btn.click()
                    time.sleep(2)
                except:
                    break
            card_date = browser.find_element(by=By.CSS_SELECTOR,value='body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x1qjc9v5.xjbqb8w.x1lcm9me.x1yr5g0i.xrt01vj.x10y3i5r.xr1yuqi.xkrivgy.x4ii5y1.x1gryazu.x15h9jz8.x47corl.xh8yej3.xir0mxb.x1juhsu6 > div > article > div > div.x1qjc9v5.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.xdt5ytf.x1iyjqo2.x5wqa0o.xln7xf2.xk390pu.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x65f84u.x1vq45kp.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x11njtxf > div > div > div.x78zum5.xdt5ytf.x1q2y9iw.x1n2onr6.xh8yej3.x9f619.x1iyjqo2.x18l3tf1.x26u7qi.xy80clv.xexx8yu.x4uap5.x18d9i69.xkhd6sd > div.x1yztbdb.x1h3rv7z.x1swvt13 > div > div > a > span > time')
            check_point = browser.find_element(by=By.CSS_SELECTOR,value='body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x1qjc9v5.xjbqb8w.x1lcm9me.x1yr5g0i.xrt01vj.x10y3i5r.xr1yuqi.xkrivgy.x4ii5y1.x1gryazu.x15h9jz8.x47corl.xh8yej3.xir0mxb.x1juhsu6 > div > article > div > div.x1qjc9v5.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.xdt5ytf.x1iyjqo2.x5wqa0o.xln7xf2.xk390pu.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x65f84u.x1vq45kp.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x11njtxf > div > div > div.x78zum5.xdt5ytf.x1q2y9iw.x1n2onr6.xh8yej3.x9f619.x1iyjqo2.x18l3tf1.x26u7qi.xy80clv.xexx8yu.x4uap5.x18d9i69.xkhd6sd > div.x1yztbdb.x1h3rv7z.x1swvt13 > div > div > a')
            check_point.get_attribute('href')
            check_point=str(check_point.get_attribute('href')).split('/')[-2]
            try : 
                card_like = browser.find_element(by=By.CSS_SELECTOR,value='body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x1qjc9v5.xjbqb8w.x1lcm9me.x1yr5g0i.xrt01vj.x10y3i5r.xr1yuqi.xkrivgy.x4ii5y1.x1gryazu.x15h9jz8.x47corl.xh8yej3.xir0mxb.x1juhsu6 > div > article > div > div.x1qjc9v5.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.xdt5ytf.x1iyjqo2.x5wqa0o.xln7xf2.xk390pu.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x65f84u.x1vq45kp.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x11njtxf > div > div > div.x78zum5.xdt5ytf.x1q2y9iw.x1n2onr6.xh8yej3.x9f619.x1iyjqo2.x18l3tf1.x26u7qi.xy80clv.xexx8yu.x4uap5.x18d9i69.xkhd6sd > section.x12nagc.x182iqb8.x1pi30zi.x1swvt13 > div > div > span > a > span > span').text
            except :
                pass
            try : 
                card_watch = browser.find_element(by=By.CSS_SELECTOR,value='body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x1qjc9v5.xjbqb8w.x1lcm9me.x1yr5g0i.xrt01vj.x10y3i5r.xr1yuqi.xkrivgy.x4ii5y1.x1gryazu.x15h9jz8.x47corl.xh8yej3.xir0mxb.x1juhsu6 > div > article > div > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > div > div > section.x1e56ztr > div > span > span > span').text
            except : 
                pass
            try:
                card_content = browser.find_element(by=By.CSS_SELECTOR,value='div._a9zr > div._a9zs >h1').text
            except:
                pass
            try:
                card_reviews = browser.find_elements(by=By.CSS_SELECTOR,value='ul > div:nth-child(3) > div > div > div > ul > div > li > div > div > div._a9zr')
            except:
                pass
            if check_point not in check_list:
                print(card_content)
                print(card_date.get_attribute("title"))
                print(card_like)
                print(card_watch)
                print(check_point)
                print("================================")
                collection.insert_one({'card_content':card_content,
                    'card_date':card_date.get_attribute("title"),
                    'card_like': card_like,
                    'card_watch':card_watch,
                    'check_point':check_point})
                for review_element in card_reviews:
                    review_content = review_element.find_element(by=By.CSS_SELECTOR,value='div._a9zs > span._ap3a')
                    review_date = review_element.find_element(by=By.CSS_SELECTOR,value='div.x9f619 > span.x1lliihq > a > time')
                    review_date=review_date.get_attribute("title")
                    collection.insert_one({'card_content':card_content,
                            'card_date':card_date.get_attribute("title"),
                            'card_like': card_like,
                            'card_watch':card_watch,
                            'check_point':check_point,
                            'review_content':review_content.text,
                            'review_date':review_date})
                    print(card_content)
                    print(card_date.get_attribute("title"))
                    print(card_like)
                    print(card_watch)
                    print(review_content.text)
                    print(review_date)
                    print("---------------------------------")
            time.sleep(2)
            try:
                # next_btn = browser.find_element(by=By.CSS_SELECTOR,value='div._aaqg > button')
                # next_btn.click()
                previos_btn = browser.find_element(by=By.CSS_SELECTOR,value='div._aaqf > button')
                previos_btn.click()
            except:
                break
            time.sleep(2)

        pass    

        browser.quit()                                      # - 브라우저 종료
    except Exception as e:
        # 에러 메시지 출력




        print(f"에러 발생: {str(e)}")

# yeomi_scraping()