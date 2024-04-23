from pymongo import MongoClient

# MongoDB 서버에 연결 : Both connect in case local and remote
client = MongoClient('mongodb://192.168.10.240:27017/')   
# client = MongoClient('mongodb://trainings.iptime.org:48003/')   

# 'mydatabase' 데이터베이스 선택 (없으면 자동 생성)
db = client['mydatabase']

# 'users' 컬렉션 선택 (없으면 자동 생성)
collection = db['users']

# 입력할 데이터
user_data = {
    'name': 'John Doe',
    'age': 30,
    'email': 'johndoe@example.com'
}

# 데이터 입력
result = collection.insert_one(user_data)

# 입력된 문서의 ID 출력
print('Inserted user id:', result.inserted_id)
