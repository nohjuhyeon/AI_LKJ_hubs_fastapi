from typing import List
from beanie import PydanticObjectId
from databases.connections import Database
from fastapi import APIRouter, Depends, HTTPException, status
from models.attraction_search_info import attraction_search_info

router = APIRouter(
    tags=["Event"]
)

@router.get("/Attraction_search_info", response_model=List[attraction_search_info])
async def get_attraction_search_info():
    attractions = await attraction_search_info.find_all().to_list()
    return attractions
