from fastapi import FastAPI, HTTPException
from typing import List

from models import User, Vehicle, Drive
from database import users_db, vehicles_db, drives_db

app = FastAPI()

@app.post("/users/", response_model=User)
def create_user(user: User):
    users_db.append(user.dict())
    return user

@app.get("/users/", response_model=List[User])
def get_users():
    return users_db

@app.post("/vehicles/", response_model=Vehicle)
def create_vehicle(vehicle: Vehicle):
    if vehicle.owner not in [user["email"] for user in users_db]:
        raise HTTPException(status_code=400, detail="User not found")
    vehicles_db.append(vehicle.dict())
    return vehicle

@app.get("/vehicles/", response_model=List[Vehicle])
def get_vehicles():
    return vehicles_db

@app.post("/drives/", response_model=Drive)
def create_drive(drive: Drive):
    if drive.vehicle not in [vehicle["nickname"] for vehicle in vehicles_db]:
        raise HTTPException(status_code=400, detail="Vehicle not found")
    drives_db.append(drive.dict())
    return drive

@app.get("/drives/", response_model=List[Drive])
def get_drives():
    return drives_db
