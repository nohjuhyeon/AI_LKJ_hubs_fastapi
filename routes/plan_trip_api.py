from typing import List, Dict, Any
from fastapi import APIRouter, HTTPException

# Models import
from models.plan_trip import Bus, Plane, Car, Train

router = APIRouter(
    tags=["Plantrip"]
)

# reserve_transfer_total 데이터 조회
@router.get("/Reserve_transfer_total", response_model=List[Dict[str, Any]])
async def get_reserve_transfer_total():
    try:
        bus_data = await Bus.find_all().to_list()
        plane_data = await Plane.find_all().to_list()
        car_data = await Car.find_all().to_list()
        train_data = await Train.find_all().to_list()

        combined_data = []

        for bus in bus_data:
            combined_data.append(bus.dict(include={'id', 'transfer_cate', 'bus_departure', 'bus_arrival', 'bus_departure_time', 'bus_direction', 'charge_adult', 'charge_child', 'charge_youth'}))

        for plane in plane_data:
            combined_data.append(plane.dict(include={'id', 'transfer_cate', 'airport_image', 'airport_name', 'airport_time', 'airport_price'}))

        for car in car_data:
            combined_data.append(car.dict(include={'id', 'transfer_cate', 'car_image', 'car_name', 'car_price', 'store_name'}))

        for train in train_data:
            combined_data.append(train.dict(include={'id', 'transfer_cate', 'train_category', 'train_number', 'train_departure', 'train_departure_time', 'train_arrival', 'train_arrival_time'}))

        return combined_data
    except Exception as e:
        print(f"Error fetching data: {e}")
        raise HTTPException(status_code=500, detail="Error fetching data")