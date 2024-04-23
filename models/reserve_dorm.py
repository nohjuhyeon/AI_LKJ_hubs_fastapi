from typing import Optional, List                   # 데이터베이스와 연결하거나 데이터를 상호작용할 때 사용

from beanie import Document, Link                   # 데이터베이스의 데이터를 문서나 링크 형태로 가져올 수 있는 기능을 제공
# from pydantic import BaseModel, EmailStr

# 개발자 실수로 들어가는 field 제한
class Reserve_dorm(Document): # 상속을 위한 것                 # 데이터 베이스에서 이용할 값들을 설정
    dorm_image : Optional[str] = None
    dorm_name: Optional[str] = None
    dorm_address: Optional[str] = None
    dorm_price : Optional[str] = None
    dorm_cate : Optional[str] = None
    class Settings:                             # 데이터 베이스에서 이용할 collection을 지정
        name = "reserve_dorm" # collection의 이름

