from typing import List

from beanie import PydanticObjectId
from databases.connections import Database
from fastapi import APIRouter, Depends, HTTPException, status
from models.admin_notice import Admin_notice_list
from models.frequent_CS import FAQ_list
from models.data_chart import data_attraction, data_concept_search, data_consume,data_consume_transition,data_trend_search

router = APIRouter(
    tags=["Consults"]
)

notice_database = Database(Admin_notice_list)
frequent_CS_database = Database(FAQ_list)
collection_data_attraction=Database(data_attraction)
collection_data_concept_search=Database(data_concept_search)
collection_data_consume=Database(data_consume)
collection_data_consume_transition=Database(data_consume_transition)
collection_data_trend_search=Database(data_trend_search)
#공지사항
@router.get("/user_notice")
async def user_notice() :
    notice = await notice_database.get_all()
    return notice

@router.get("/FAQ_list")
async def user_notice() :
    notice = await frequent_CS_database.get_all()
    return notice

# @router.get("/Data_chart")
# async def user_notice() :
#     notice = await notice_database.get_all()
#     return notice