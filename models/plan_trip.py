from pydantic import BaseModel, Field
from typing import Optional
from beanie import Document

# Plane Model
class Plane(Document):
    transfer_cate: str = "plane"
    airport_image: Optional[str] = None
    airport_name: Optional[str] = None
    airport_time: Optional[str] = None
    airport_price: Optional[str] = None

    class Settings:
        name = "reserve_transfer_total"

# Car Model
class Car(Document):
    transfer_cate: str = "car"
    car_image: Optional[str] = None
    car_name: Optional[str] = None
    car_price: Optional[str] = None
    store_name: Optional[str] = None

    class Settings:
        name = "reserve_transfer_total"

# Train Model
class Train(Document):
    transfer_cate: str = "train"
    train_category: Optional[str] = None
    train_number: Optional[str] = None
    train_departure: Optional[str] = None
    train_departure_time: Optional[str] = None
    train_arrival: Optional[str] = None
    train_arrival_time: Optional[str] = None

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
