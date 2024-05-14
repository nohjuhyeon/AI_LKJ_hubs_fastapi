from typing import List, Dict

from beanie import PydanticObjectId
from databases.connections import Database
from fastapi import APIRouter, Depends, HTTPException, status
from models.admin_notice import Admin_notice_list
from models.frequent_CS import FAQ_list
from models.data_chart import data_attraction, data_concept_search, data_consume, data_consume_transition, data_trend_search
from models.plan_trip import ReserveTransferTotal, ReserveDorm, ReserveTour

router = APIRouter(
    tags=["Consults"]
)

notice_database = Database(Admin_notice_list)
frequent_CS_database = Database(FAQ_list)
collection_data_attraction = Database(data_attraction)
collection_data_concept_search = Database(data_concept_search)
collection_data_consume = Database(data_consume)
collection_data_consume_transition = Database(data_consume_transition)
collection_data_trend_search = Database(data_trend_search)
collection_reserve_transfer_total = Database(ReserveTransferTotal)
collection_reserve_dorm = Database(ReserveDorm)
collection_reserve_tour = Database(ReserveTour)

# 공지사항
@router.get("/user_notice")
async def user_notice():
    notice = await notice_database.get_all()
    return notice

@router.get("/FAQ_list")
async def faq_list():
    faq = await frequent_CS_database.get_all()
    return faq

@router.get("/Data_chart", response_model=Dict[str, List])
async def get_data_chart():
    # 모든 데이터베이스에서 데이터를 동시에 조회
    data_consume = await collection_data_consume.get_all()
    data_trend_search = await collection_data_trend_search.get_all()
    data_consume_transition = await collection_data_consume_transition.get_all()
    data_concept_search = await collection_data_concept_search.get_all()

    # 모든 결과를 하나의 JSON 객체로 반환
    return {
        "data_consume": data_consume,
        "data_trend_search": data_trend_search,
        "data_consume_transition": data_consume_transition,
        "data_concept_search": data_concept_search,
    }

# reserve_transfer_total 데이터 조회
@router.get("/Reserve_transfer_total", response_model=List[ReserveTransferTotal])
async def get_reserve_transfer_total():
    reserve_transfer_total = await collection_reserve_transfer_total.get_all()
    return reserve_transfer_total

# reserve_dorm 데이터 조회
@router.get("/Reserve_dorm", response_model=List[ReserveDorm])
async def get_reserve_dorm():
    reserve_dorm = await collection_reserve_dorm.get_all()
    return reserve_dorm

# reserve_tour 데이터 조회
@router.get("/Reserve_tour", response_model=List[ReserveTour])
async def get_reserve_tour():
    reserve_tour = await collection_reserve_tour.get_all()
    return reserve_tour
