from typing import List

from beanie import PydanticObjectId
from databases.connections import Database
from fastapi import APIRouter, Depends, HTTPException, status
from models.admin_notice import Notice
from models.frequent_CS import Frequent_CS
from models.data_chart import Data_chart

router = APIRouter(
    tags=["Consults"]
)

notice_database = Database(Notice)
frequent_CS_database = Database(Frequent_CS)
data_chart_database = Database(Data_chart)

#공지사항
@router.get("/user_notice")
async def user_notice() :
    notice = await notice_database.get(id)
    return notice