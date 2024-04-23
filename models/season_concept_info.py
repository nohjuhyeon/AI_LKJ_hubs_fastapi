from typing import Optional, List                   # 데이터베이스와 연결하거나 데이터를 상호작용할 때 사용
from datetime import datetime
from beanie import Document, Link                   # 데이터베이스의 데이터를 문서나 링크 형태로 가져올 수 있는 기능을 제공
# from pydantic import BaseModel, EmailStr


# 개발자 실수로 들어가는 field 제한
class season_concept_info(Document) :  # 상속을 위한 것                 # 데이터 베이스에서 이용할 값들을 설정
    season : Optional[str] = None
    concept : Optional[str] = None
    region : Optional[str] = None 
    frequency : Optional[int] = None 
    class Settings :  
        name = "season_concept_info"  # collection의 이름
