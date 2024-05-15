from typing import List, Dict

from beanie import PydanticObjectId
from databases.connections import Database
from fastapi import APIRouter, Depends, HTTPException, status
from models.plan_trip import ReserveTransferTotal, ReserveDorm, ReserveTour

router = APIRouter(
    tags=["Plantrip"]
)

collection_reserve_transfer_total = Database(ReserveTransferTotal)
collection_reserve_dorm = Database(ReserveDorm)
collection_reserve_tour = Database(ReserveTour)

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
