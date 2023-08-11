from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    email: str
    phone: str

class Vehicle(BaseModel):
    owner: str  # This will be the email of the user
    make: str
    model: str
    year: int
    nickname: str

class Drive(BaseModel):
    vehicle: str  # This will be the the vehicle
    start_location: str
    end_location: str
    type: str  # either 'business' or 'personal'
    date_time_start: str
    date_time_end: str
    distance: float
