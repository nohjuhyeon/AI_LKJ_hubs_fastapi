# 데이터명 : 조달청_나라장터 공공데이터개방표준서비스
# from https://www.data.go.kr/iim/api/selectAPIAcountView.do
import requests 
import xmltodict
# url 주소 변수 지정
# sickCd = ['M542','S134']
# medTp = 1,2
import time
from pymongo import MongoClient
mongoClient = MongoClient("mongodb://192.168.10.240:27017")
# database 연결
database = mongoClient["AI_LKJ"]
# collection 작업
collection = database['TRAVEL_APPLICATION_APPLE']
# insert 작업 진행
i = 0
count_reviews = 0
list_app = [284876795,1225499481,1141745032,415458524]
list_app_name = ['tripadvisor','triple','myrealtrip','skyscanner']
for j in  range(len(list_app)):
    i = 0
    while True:
        i += 1
        try:
            url = 'https://itunes.apple.com/kr/rss/customerreviews/page={}/id={}/sortby=mostrecent/json'.format(i,list_app[j])
            pass
            # respose라는 변수로 받음
            response = requests.get(url) 
            pass
            # response의 내용을 출력
            print(response.content) 

            # json 파일을 dictionary 형태로 변환
            import json
            contents = json.loads(response.content)
            for content in contents['feed']['entry']:
                data_dict = {}
                app_name = list_app_name[j]
                user_score = content['im:rating']['label']
                user_date = content['updated']['label']
                user_comments = content['content']['label']
                evaluation = content['im:voteSum']['label']
                data_dict['app_name'] = app_name
                data_dict['user_score'] = user_score
                data_dict['user_date'] = user_date
                data_dict['user_comments'] = user_comments
                data_dict['evaluation'] = evaluation
                print(app_name)
                print(user_score)
                print(user_date)
                print(user_comments)
                print(evaluation)
                count_reviews += 1
                print(count_reviews)

                result = collection.insert_one(data_dict)
        except:
            break
    pass



