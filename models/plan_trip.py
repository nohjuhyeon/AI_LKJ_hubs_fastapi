from pydantic import BaseModel, Field
from typing import Optional, List
from beanie import Document

# ReserveTransferTotal 모델 정의
class ReserveTransferTotal(Document):
    bus_departure: Optional[str] = None
    bus_arrival: Optional[str] = None
    bus_departure_time: Optional[str] = None
    bus_direction: Optional[str] = None
    charge_adult: Optional[str] = None
    charge_child: Optional[str] = None
    charge_youth: Optional[str] = None
    transfer_cate: Optional[str] = None

    class Settings:
        name = "reserve_transfer_total"

# ReserveDorm 모델 정의
class ReserveDorm(Document):
    dorm_image: Optional[str] = None
    dorm_name: Optional[str] = None
    dorm_address: Optional[str] = None
    dorm_price: Optional[str] = None
    dorm_cate: Optional[str] = None

    class Settings:
        name = "reserve_dorm"

# ReserveTour 모델 정의
class ReserveTour(Document):
    tour_image: Optional[str] = None
    tour_name: Optional[str] = None
    tour_content: Optional[str] = None
    tour_price: Optional[str] = None

    class Settings:
        name = "reserve_tour"
