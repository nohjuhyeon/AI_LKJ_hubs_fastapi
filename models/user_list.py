from typing import Optional, List                   # 데이터베이스와 연결하거나 데이터를 상호작용할 때 사용

from beanie import Document, Link                   # 데이터베이스의 데이터를 문서나 링크 형태로 가져올 수 있는 기능을 제공
# from pydantic import BaseModel, EmailStr

# 개발자 실수로 들어가는 field 제한
class User_list(Document): # 상속을 위한 것                 # 데이터 베이스에서 이용할 값들을 설정
    user_email: Optional[str] = None
    user_password: Optional[str] = None
    user_name: Optional[str] = None    
    user_birth : Optional[str] = None
    user_phone_number : Optional[str] = None
    user_address : Optional[str] = None
    user_img : Optional[bytes] = None
    class Settings:                             # 데이터 베이스에서 이용할 collection을 지정
        name = "user_list" # collection의 이름
  
  # beanie는 mongoDB를 비동기적으로 다루기 위한 라이브러리
        

class User_reserve_list(Document):
    user_id : Optional[str] = None
    transfer_id : Optional[str] = None
    dorm_id : Optional[str] = None
    tour_id : Optional[str] = None
    class Settings:
        name = "user_reserve_list"

