from typing import List, Dict, Any
from fastapi import APIRouter, HTTPException

# Models import
from models.plan_trip import Plane, Car, Train

router = APIRouter(
    tags=["Plantrip"]
)

# reserve_transfer_total 데이터 조회
@router.get("/Reserve_transfer_total", response_model=List[Dict[str, Any]])
async def get_reserve_transfer_total():
    try:
        plane_data = await Plane.find_all().to_list()
        car_data = await Car.find_all().to_list()
        train_data = await Train.find_all().to_list()

        combined_data = plane_data + car_data + train_data
        return combined_data
    except Exception as e:
        print(f"Error fetching data: {e}")
        raise HTTPException(status_code=500, detail="Error fetching data")
