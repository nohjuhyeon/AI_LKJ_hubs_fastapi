from typing import Any, List, Optional
from beanie import init_beanie, PydanticObjectId
from models.user_list import User_list, User_reserve_list
from models.reserve_transfer import transfer_car_list, transfer_train_list,transfer_airport_list,transfer_bus_list,tour_list, transfer_total_list
from models.tour_plan import reco_trip_plan, reco_trip_add
from models.reserve_dorm import Reserve_dorm
from models.admin_notice import Admin_notice_list
from models.one_on_one_CS import One_on_one_CS_list
from models.trip_package import Trip_package_list
from models.one_on_one_CS_inquiry import Inquiry
from models.frequent_CS import FAQ_list
from models.data_chart import data_attraction, data_concept_search, data_consume,data_consume_transition,data_trend_search
from models.attraction_search_info import attraction_search_info
from models.season_concept_info import season_concept_info
from motor.motor_asyncio import AsyncIOMotorClient 
from pydantic_settings import BaseSettings 
from utils.paginations import Paginations
class Settings(BaseSettings):                                                                                  
    DATABASE_URL: Optional[str] = None                                              
    CONTAINER_PREFIX: Optional[str] = None 
    async def initialize_database(self):                                         
        client = AsyncIOMotorClient(self.DATABASE_URL)                             
        await init_beanie(database=client.get_default_database(),                  
                          document_models=[User_list,User_reserve_list,transfer_car_list, transfer_train_list,transfer_airport_list,transfer_bus_list, reco_trip_plan,reco_trip_add,tour_list, transfer_total_list,Reserve_dorm,Admin_notice_list,One_on_one_CS_list,Inquiry,FAQ_list,data_attraction, 
                                           data_concept_search, data_consume,data_consume_transition,data_trend_search, Trip_package_list,attraction_search_info,season_concept_info])

        
    class Config:
        env_file = ".env"                                                

class Database : 
    # model 즉 collection
    def __init__(self, model) -> None:
        self.model = model
        pass

    # 전체 리스트
    async def get_all(self) :
        documents = await self.model.find_all().to_list()         
        pass
        return documents
    
    # 상세 보기
    async def get(self, id: PydanticObjectId) -> Any: 
        doc = await self.model.get(id)               
        if doc:                                  
            return doc
        return False
    
    # 저장
    async def save(self, document) -> None:
        await document.create()
        return None
    
    # 업데이트
    async def update_one(self, id: PydanticObjectId, dic) -> Any:
        doc = await self.model.get(id)
        if doc:
            for key, value in dic.items():
                setattr(doc, key, value)
            await doc.save()
            return True
        return False
    
    # 삭제
    async def delete_one(self, id: PydanticObjectId) -> bool:
        doc = await self.model.get(id)
        if doc:
            await doc.delete()
            return True
        return False

    async def getsbyconditions(self, conditions:dict) -> [Any]:
        documents = await self.model.find(conditions).to_list()  # find({})
        if documents:
            return documents
        return False    
    
    async def getsbyconditionswithpagination(self
                                             , conditions:dict, page_number, records_per_page=10) -> [Any]:
        # find({})
        total = await self.model.find(conditions).count()
        pagination = Paginations(total_records=total, current_page=page_number, records_per_page=records_per_page)
        documents = await self.model.find(conditions).skip(pagination.start_record_number-1).limit(pagination.records_per_page).to_list()
        if documents:
            return documents, pagination
        return pagination    