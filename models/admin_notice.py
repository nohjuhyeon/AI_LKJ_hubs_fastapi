from typing import Optional, List                   # 데이터베이스와 연결하거나 데이터를 상호작용할 때 사용
from datetime import datetime
from beanie import Document, Link                   # 데이터베이스의 데이터를 문서나 링크 형태로 가져올 수 있는 기능을 제공
# from pydantic import BaseModel, EmailStr

############ 숨은 그림을 찾아보세요 ^^ ##############################################

# 개발자 실수로 들어가는 field 제한
class Admin_notice_list(Document) :  # 상속을 위한 것                 # 데이터 베이스에서 이용할 값들을 설정
    title : Optional[str] = None 
    content : Optional[str] = None 
    writer : Optional[str] = None
    date : Optional[str] = None
    class Settings :   # 데이터 베이스에서 이용할 collection을 지정(Settings야 Setting아니고 ^^)
        name = "admin_notices"  # collection의 이름
