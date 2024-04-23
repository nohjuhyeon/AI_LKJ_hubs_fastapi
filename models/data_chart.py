from typing import Optional, List                   # 데이터베이스와 연결하거나 데이터를 상호작용할 때 사용

from beanie import Document, Link                   # 데이터베이스의 데이터를 문서나 링크 형태로 가져올 수 있는 기능을 제공
# from pydantic import BaseModel, EmailStr

# 개발자 실수로 들어가는 field 제한
class data_attraction(Document): # 상속을 위한 것                 # 데이터 베이스에서 이용할 값들을 설정
    rank: Optional[int] = None
    attraction_name: Optional[str] = None
    address: Optional[str] = None    
    classification : Optional[str] = None
    attraction_search : Optional[int] = None
    region : Optional[str] = None
    std_year : Optional[int] = None
    class Settings:                             # 데이터 베이스에서 이용할 collection을 지정
        name = "data_attraction" # collection의 이름
  
  # beanie는 mongoDB를 비동기적으로 다루기 위한 라이브러리
        

class data_trend_search(Document): # 상속을 위한 것                 # 데이터 베이스에서 이용할 값들을 설정
    region : Optional[str] = None
    std_year : Optional[int] = None
    std_month : Optional[int] = None
    std_year_month : Optional[int] = None
    tour_trend : Optional[str] = None
    num_mention : Optional[int] = None
    class Settings:                             # 데이터 베이스에서 이용할 collection을 지정
        name = "data_trend_search" # collection의 이름
        
class data_concept_search(Document): # 상속을 위한 것                 # 데이터 베이스에서 이용할 값들을 설정
    destination_type: Optional[str] = None
    destination_search: Optional[int] = None
    region : Optional[str] = None
    std_year : Optional[int] = None
    std_month : Optional[int] = None
    std_year_month : Optional[int] = None
    class Settings:                             # 데이터 베이스에서 이용할 collection을 지정
        name = "data_concept_search" # collection의 이름

class data_consume(Document): # 상속을 위한 것                 # 데이터 베이스에서 이용할 값들을 설정
    industry_major_cate: Optional[str] = None
    industry_middle_cate: Optional[str] = None
    consumption_amount: Optional[float] = None
    region : Optional[str] = None
    std_year : Optional[int] = None
    class Settings:                             # 데이터 베이스에서 이용할 collection을 지정
        name = "data_consume" # collection의 이름

class data_consume_transition(Document): # 상속을 위한 것                 # 데이터 베이스에서 이용할 값들을 설정
    industry_major_cate: Optional[str] = None
    region : Optional[str] = None
    std_year : Optional[int] = None
    std_month : Optional[int] = None
    std_year_month : Optional[int] = None
    consumption_amount: Optional[float] = None
    class Settings:                             # 데이터 베이스에서 이용할 collection을 지정
        name = "data_consume_transition" # collection의 이름