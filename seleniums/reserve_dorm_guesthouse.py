from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://192.168.10.240:27017/")
database = mongoClient["AI_LKJ"]
collection = database['reserve_dorm']




driver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(driver_manager_directory))
url = "https://www.booking.com/searchresults.ko.html?ss=%EB%B6%80%EC%82%B0&ssne=%EB%B6%80%EC%82%B0&ssne_untouched=%EB%B6%80%EC%82%B0&label=Vit8GNqq0h_49era%7E9RmyvlJBF_JpBNa-QANkJ0NfLVqTd4IsK4wErA%3D%3D&aid=2210273&lang=ko&sb=1&src_elem=sb&src=searchresults&dest_id=-713900&dest_type=city&checkin=2024-01-20&checkout=2024-01-25&group_adults=4&no_rooms=1&group_children=0"
browser.get(url)

time.sleep(10)

popup_cancel = browser.find_element(By.CSS_SELECTOR, "#b2searchresultsPage > div.b9720ed41e.cdf0a9297c > div > div > div > div.dd5dccd82f > div.ffd93a9ecb.dc19f70f85.eb67815534 > div > button > span > span > svg > path")
popup_cancel.click()

guesthouse_checkbox = browser.find_element(By.CSS_SELECTOR, "#filter_group_ht_id_\:rs\: > div:nth-child(10) > label > span.ef785aa7f4 > span > svg")
guesthouse_checkbox.click()

time.sleep(5)

while True:
    elements = browser.find_elements(By.CSS_SELECTOR, 'div.c82435a4b8.a178069f51.a6ae3c2b40.a18aeea94d.d794b7a0f7.f53e278e95.c6710787a4')
    for element in elements:
        guesthouse_image = element.find_element(By.CSS_SELECTOR, 'img.f9671d49b1').get_attribute('src')
        guesthouse_name = element.find_element(By.CSS_SELECTOR, 'div.f6431b446c.a15b38c233').text
        guesthouse_address = element.find_element(By.CSS_SELECTOR, 'span.aee5343fdb.def9bc142a').text
        guesthouse_price = element.find_element(By.CSS_SELECTOR, 'span.f6431b446c.fbfd7c1165.e84eb96b1f').text
        collection.insert_one({
            "dorm_image": guesthouse_image,
            "dorm_name": guesthouse_name,
            "dorm_address": guesthouse_address,
            "dorm_price": guesthouse_price,
            "dorm_cate": "guest_house"
        })
    try:
        next_button = browser.find_element(By.CSS_SELECTOR, '#bodyconstraint-inner > div:nth-child(8) > div > div.af5895d4b2 > div.df7e6ba27d > div.bcbf33c5c3 > div.dcf496a7b9.bb2746aad9 > div.d7a0553560 > div.c82435a4b8.a178069f51.a6ae3c2b40.a18aeea94d.d794b7a0f7.f53e278e95.e49b423746 > nav > nav > div > div.b16a89683f.cab1524053 > button')
        next_button.click()
        time.sleep(5)
    except Exception as e:
        break
