from typing import Optional, List                   # 데이터베이스와 연결하거나 데이터를 상호작용할 때 사용

from beanie import Document, Link                   # 데이터베이스의 데이터를 문서나 링크 형태로 가져올 수 있는 기능을 제공
# from pydantic import BaseModel, EmailStr

# 개발자 실수로 들어가는 field 제한
class transfer_car_list(Document): # 상속을 위한 것                 # 데이터 베이스에서 이용할 값들을 설정
    car_name: Optional[str] = None
    car_image: Optional[str] = None
    store_name: Optional[str] = None    
    car_price : Optional[str] = None
    class Settings:                             # 데이터 베이스에서 이용할 collection을 지정
        name = "reserve_transfer_car" # collection의 이름
  
  # beanie는 mongoDB를 비동기적으로 다루기 위한 라이브러리
        
class transfer_train_list(Document): # 상속을 위한 것                 # 데이터 베이스에서 이용할 값들을 설정
    train_category: Optional[str] = None
    train_number: Optional[str] = None
    train_departure: Optional[str] = None    
    train_departure_time : Optional[str] = None
    train_arrival: Optional[str] = None    
    train_arrival_time : Optional[str] = None
    class Settings:                             # 데이터 베이스에서 이용할 collection을 지정
        name = "reserve_transfer_train" # collection의 이름

class transfer_airport_list(Document): # 상속을 위한 것                 # 데이터 베이스에서 이용할 값들을 설정
    airport_image: Optional[str] = None
    airport_name: Optional[str] = None
    airport_time: Optional[str] = None
    airport_price: Optional[str] = None    
    class Settings:                             # 데이터 베이스에서 이용할 collection을 지정
        name = "reserve_transfer_airport" # collection의 이름

class transfer_bus_list(Document): # 상속을 위한 것                 # 데이터 베이스에서 이용할 값들을 설정
    bus_departure: Optional[str] = None
    bus_arrival: Optional[str] = None
    bus_departure_time: Optional[str] = None
    bus_direction: Optional[str] = None
    charge_adult : Optional[str] = None
    charge_child: Optional[str] = None
    charge_youth: Optional[str] = None    
    class Settings:                             # 데이터 베이스에서 이용할 collection을 지정
        name = "reserve_transfer_bus" # collection의 이름

class transfer_total_list(Document): # 상속을 위한 것                 # 데이터 베이스에서 이용할 값들을 설정
    bus_departure: Optional[str] = None
    bus_arrival: Optional[str] = None
    bus_departure_time: Optional[str] = None
    bus_direction: Optional[str] = None
    charge_adult : Optional[str] = None
    charge_child: Optional[str] = None
    charge_youth: Optional[str] = None    
    airport_image: Optional[str] = None
    airport_name: Optional[str] = None
    airport_time: Optional[str] = None
    airport_price: Optional[str] = None  
    train_category: Optional[str] = None
    train_number: Optional[str] = None
    train_departure: Optional[str] = None    
    train_departure_time : Optional[str] = None
    train_arrival: Optional[str] = None    
    train_arrival_time : Optional[str] = None
    car_name: Optional[str] = None
    car_image: Optional[str] = None
    store_name: Optional[str] = None    
    car_price : Optional[str] = None
    transfer_cate : Optional[str] = None
    class Settings:                             # 데이터 베이스에서 이용할 collection을 지정
        name = "reserve_transfer_total" # collection의 이름

class tour_list(Document): # 상속을 위한 것                 # 데이터 베이스에서 이용할 값들을 설정
    tour_image: Optional[str] = None
    tour_name: Optional[str] = None
    tour_content: Optional[str] = None
    tour_price: Optional[str] = None
    class Settings:                             # 데이터 베이스에서 이용할 collection을 지정
        name = "reserve_tour" # collection의 이름