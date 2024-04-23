from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from pymongo import MongoClient
mongoClient = MongoClient("mongodb://192.168.10.240:27017/")
# database 연결
database = mongoClient["AI_LKJ"]
# collection 작업
collection = database['reserve_transfer_train']
collection.delete_many({})
# 웹드라이버 세팅
driver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(driver_manager_directory))
url = "https://www.letskorail.com/ebizprd/EbizPrdTicketpr21100W_pr21112.do"
browser.get(url)

# 전체 체크박스 선택
total_checkbox = browser.find_element(By.CSS_SELECTOR, "#contents > div.content > form:nth-child(2) > div > div.ticket_box.rtm > div.part_rig > ul > li.wd20 > input[type=radio]")
total_checkbox.click()

# 왕복 체크박스 선택
round_trip_checkbox = browser.find_element(By.CSS_SELECTOR, "#route03")
round_trip_checkbox.click()

# 출발지 입력
departure_input = browser.find_element(By.CSS_SELECTOR, "#txtGoStart")
departure_input.clear()
departure_input.send_keys("서울")

# 도착지 입력
arrival_input = browser.find_element(By.CSS_SELECTOR, "#txtGoEnd")
arrival_input.clear()
arrival_input.send_keys("부산")

# 출발 날짜 선택
departure_year = browser.find_element(By.CSS_SELECTOR, "#selGoYear > option:nth-child(1)")
departure_year.click()
departure_month = browser.find_element(By.CSS_SELECTOR, "#selGoMonth > option:nth-child(1)")
departure_month.click()
departure_day = browser.find_element(By.CSS_SELECTOR, "#selGoDay > option:nth-child(20)")
departure_day.click()
departure_hour = browser.find_element(By.CSS_SELECTOR, "#selGoHour > option:nth-child(1)")
departure_hour.click()

# 돌아오는 날짜 선택
return_year = browser.find_element(By.CSS_SELECTOR, "#selComeYear > option:nth-child(1)")
return_year.click()
return_month = browser.find_element(By.CSS_SELECTOR, "#selComeMonth > option:nth-child(1)")
return_month.click()
return_day = browser.find_element(By.CSS_SELECTOR, "#selComeDay > option:nth-child(25)")
return_day.click()

# 프레임 전환 (만약 결과가 iframe 내부에 있는 경우)
browser.switch_to.frame("go_list")
pass
# 테이블 데이터 추출
for row_num in range(1, 21):
    # 팝업창을 띄우는 버튼 찾기
    button_selector = f'#tableResult > tbody > tr:nth-child({row_num}) > td:nth-child(11) > a > img'
    button = browser.find_element(By.CSS_SELECTOR, button_selector)
    button.click() 

    time.sleep(5)

    # CSS 선택자를 사용해 특정 셀 추출
    category_selector = f"#tableResult > tbody > tr:nth-child({row_num}) > td:nth-child(1)"
    departure_selector = f"#tableResult > tbody > tr:nth-child({row_num}) > td:nth-child(3)"
    arrival_selector = f"#tableResult > tbody > tr:nth-child({row_num}) > td:nth-child(4)"

    try: 
        category_cell = browser.find_element(By.CSS_SELECTOR, category_selector).text
    except:
        category_cell = None
    try: 
        departure_cell = browser.find_element(By.CSS_SELECTOR, departure_selector).text
        if departure_cell:  # 출발지 정보가 있을 경우, 지역과 시간으로 분리
            departure_location, departure_time = departure_cell.split()
        else:
            departure_location, departure_time = None, None
    except:
        departure_cell, departure_location, departure_time = None, None, None
    try: 
        arrival_cell = browser.find_element(By.CSS_SELECTOR, arrival_selector).text
        if arrival_cell:  # 도착지 정보가 있을 경우, 지역과 시간으로 분리
            arrival_location, arrival_time = arrival_cell.split()
        else:
            arrival_location, arrival_time = None, None
    except:
        arrival_cell, arrival_location, arrival_time = None, None, None

    # 예외 처리를 사용해 train_cell 추출
    train_cell_selector = f"#tableResult > tbody > tr:nth-child({row_num}) > td.bg-00"
    train_cell = "None"  # 기본값 설정
    for class_suffix in ['00', '02', '07', '08', '10', '18']:
        try:
            train_cell = browser.find_element(By.CSS_SELECTOR, f"#tableResult > tbody > tr:nth-child({row_num}) > td.bg-{class_suffix}").text
            if train_cell:  # 값이 존재하면 루프 종료
                break
        except Exception as e:
            continue  # 해당 클래스를 가진 셀이 없으면 다음 클래스 시도
        
    if not (category_cell and departure_location and departure_time and arrival_location and arrival_time and train_cell):
        continue  # 필요한 모든 정보가 없으면 다음 행으로 이동

    # 추출한 데이터를 MongoDB에 삽입
    train_info = {
        "train_category": category_cell,
        "train_number": train_cell,
        "train_departure": departure_location,
        "train_departure_time": departure_time,
        "train_arrival": arrival_location,
        "train_arrival_time": arrival_time,
        "transfer_cate": "train"
    }
    collection.insert_one(train_info)

next_button = browser.find_element(By.CSS_SELECTOR,"#train_info > tbody > tr > td > a")
next_button.click()

while True:
    for row_num in range(1, 21): 
        # CSS 선택자를 사용해 특정 셀 추출
        category_selector = f"#tableResult > tbody > tr:nth-child({row_num}) > td:nth-child(1)"
        departure_selector = f"#tableResult > tbody > tr:nth-child({row_num}) > td:nth-child(3)"
        arrival_selector = f"#tableResult > tbody > tr:nth-child({row_num}) > td:nth-child(4)"

        try: 
            category_cell = browser.find_element(By.CSS_SELECTOR, category_selector).text
        except:
            category_cell = None
        try: 
            departure_cell = browser.find_element(By.CSS_SELECTOR, departure_selector).text
            # 출발지와 시간 분리
            departure_location, departure_time = departure_cell.split()
        except:
            departure_location = None
            departure_time = None
        try: 
            arrival_cell = browser.find_element(By.CSS_SELECTOR, arrival_selector).text
            # 도착지와 시간 분리
            arrival_location, arrival_time = arrival_cell.split()
        except:
            arrival_location = None
            arrival_time = None

        # 예외 처리를 사용해 train_cell 추출
        train_cell_selector = f"#tableResult > tbody > tr:nth-child({row_num}) > td.bg-00"
        train_cell = "None"  # 기본값 설정
        for class_suffix in ['00', '02', '07', '08', '10', '18']:
            try:
                train_cell = browser.find_element(By.CSS_SELECTOR, f"#tableResult > tbody > tr:nth-child({row_num}) > td.bg-{class_suffix}").text
                if train_cell:  # 값이 존재하면 루프 종료
                    break
            except Exception as e:
                continue  # 해당 클래스를 가진 셀이 없으면 다음 클래스 시도
        
        if not (category_cell and departure_location and departure_time and arrival_location and arrival_time and train_cell):
            continue  # 필요한 모든 정보가 없으면 다음 행으로 이동

        # 추출한 데이터를 MongoDB에 삽입
        train_info = {
            "train_category": category_cell,
            "train_number": train_cell,
            "train_departure": departure_location,
            "train_departure_time": departure_time,
            "train_arrival": arrival_location,
            "train_arrival_time": arrival_time,
            "transfer_cate": "train"
        }
        collection.insert_one(train_info)
    try:    
        next_button = browser.find_element(By.CSS_SELECTOR,"#train_info > tbody > tr > td > a:nth-child(2)")
        next_button.click()
    except:
        break


browser.switch_to.default_content()
browser.switch_to.frame("come_list")

for row_num in range(1, 21): 
    # CSS 선택자를 사용해 특정 셀 추출
    category_selector = f"#tableResult > tbody > tr:nth-child({row_num}) > td:nth-child(1)"
    departure_selector = f"#tableResult > tbody > tr:nth-child({row_num}) > td:nth-child(3)"
    arrival_selector = f"#tableResult > tbody > tr:nth-child({row_num}) > td:nth-child(4)"

    try: 
        category_cell = browser.find_element(By.CSS_SELECTOR, category_selector).text
    except:
        category_cell = None
    try: 
        departure_cell = browser.find_element(By.CSS_SELECTOR, departure_selector).text
        if departure_cell:  # 출발지 정보가 있을 경우, 지역과 시간으로 분리
            departure_location, departure_time = departure_cell.split()
        else:
            departure_location, departure_time = None, None
    except:
        departure_cell, departure_location, departure_time = None, None, None
    try: 
        arrival_cell = browser.find_element(By.CSS_SELECTOR, arrival_selector).text
        if arrival_cell:  # 도착지 정보가 있을 경우, 지역과 시간으로 분리
            arrival_location, arrival_time = arrival_cell.split()
        else:
            arrival_location, arrival_time = None, None
    except:
        arrival_cell, arrival_location, arrival_time = None, None, None

    # 예외 처리를 사용해 train_cell 추출
    train_cell_selector = f"#tableResult > tbody > tr:nth-child({row_num}) > td.bg-00"
    train_cell = "None"  # 기본값 설정
    for class_suffix in ['00', '02', '07', '08', '10', '18']:
        try:
            train_cell = browser.find_element(By.CSS_SELECTOR, f"#tableResult > tbody > tr:nth-child({row_num}) > td.bg-{class_suffix}").text
            if train_cell:  # 값이 존재하면 루프 종료
                break
        except Exception as e:
            continue  # 해당 클래스를 가진 셀이 없으면 다음 클래스 시도
        
    if not (category_cell and departure_location and departure_time and arrival_location and arrival_time and train_cell):
        continue  # 필요한 모든 정보가 없으면 다음 행으로 이동

    # 추출한 데이터를 MongoDB에 삽입
    train_info = {
            "train_category": category_cell,
            "train_number": train_cell,
            "train_departure": departure_location,
            "train_departure_time": departure_time,
            "train_arrival": arrival_location,
            "train_arrival_time": arrival_time, 
            "transfer_cate": "train"
    }
    collection.insert_one(train_info)

next_button = browser.find_element(By.CSS_SELECTOR,"#train_info > tbody > tr > td > a")
next_button.click()

while True:
    for row_num in range(1, 21): 
        # CSS 선택자를 사용해 특정 셀 추출
        category_selector = f"#tableResult > tbody > tr:nth-child({row_num}) > td:nth-child(1)"
        departure_selector = f"#tableResult > tbody > tr:nth-child({row_num}) > td:nth-child(3)"
        arrival_selector = f"#tableResult > tbody > tr:nth-child({row_num}) > td:nth-child(4)"

        try: 
            category_cell = browser.find_element(By.CSS_SELECTOR, category_selector).text
        except:
            category_cell = None
        try: 
            departure_cell = browser.find_element(By.CSS_SELECTOR, departure_selector).text
            # 출발지와 시간 분리
            departure_location, departure_time = departure_cell.split()
        except:
            departure_location = None
            departure_time = None
        try: 
            arrival_cell = browser.find_element(By.CSS_SELECTOR, arrival_selector).text
            # 도착지와 시간 분리
            arrival_location, arrival_time = arrival_cell.split()
        except:
            arrival_location = None
            arrival_time = None

        # 예외 처리를 사용해 train_cell 추출
        train_cell_selector = f"#tableResult > tbody > tr:nth-child({row_num}) > td.bg-00"
        train_cell = "None"  # 기본값 설정
        for class_suffix in ['00', '02', '07', '08', '10', '18']:
            try:
                train_cell = browser.find_element(By.CSS_SELECTOR, f"#tableResult > tbody > tr:nth-child({row_num}) > td.bg-{class_suffix}").text
                if train_cell:  # 값이 존재하면 루프 종료
                    break
            except Exception as e:
                continue  # 해당 클래스를 가진 셀이 없으면 다음 클래스 시도
        
        if not (category_cell and departure_location and departure_time and arrival_location and arrival_time and train_cell):
            continue  # 필요한 모든 정보가 없으면 다음 행으로 이동

        # 추출한 데이터를 MongoDB에 삽입
        train_info = {
            "train_category": category_cell,
            "train_number": train_cell,
            "train_departure": departure_location,
            "train_departure_time": departure_time,
            "train_arrival": arrival_location,
            "train_arrival_time": arrival_time,
            "transfer_cate": "train"
        }
        collection.insert_one(train_info)
    try:    
        next_button = browser.find_element(By.CSS_SELECTOR,"#train_info > tbody > tr > td > a:nth-child(2)")
        next_button.click()
    except:
        break
    
# 브라우저 종료
browser.quit()
        
