from typing import Optional, List                   # 데이터베이스와 연결하거나 데이터를 상호작용할 때 사용

from beanie import Document, Link                   # 데이터베이스의 데이터를 문서나 링크 형태로 가져올 수 있는 기능을 제공
# from pydantic import BaseModel, EmailStr

# 개발자 실수로 들어가는 field 제한
class reco_trip_plan(Document): # 상속을 위한 것                 # 데이터 베이스에서 이용할 값들을 설정
    concept_number : Optional[str] = None
    concept_name: Optional[str] = None
    day: Optional[int] = None
    tour_list : List[str] = None
    class Settings:                             # 데이터 베이스에서 이용할 collection을 지정
        name = "reco_trip_plan" # collection의 이름
  
  # beanie는 mongoDB를 비동기적으로 다루기 위한 라이브러리
        
class reco_trip_add(Document): # 상속을 위한 것                 # 데이터 베이스에서 이용할 값들을 설정
    reco_list : Optional[str] = None
    class Settings:                             # 데이터 베이스에서 이용할 collection을 지정
        name = "reco_trip_add" # collection의 이름
