# from pydantic import BaseModel
# from fastapi import FastAPI

# app = FastAPI()

# class carDataIn(BaseModel):
#     brand:str
#     model:str
#     year:int
#     price:float
#     mileage:int
    
# class carDataOut(carDataIn):
#     id:int

# car_database={}

# @app.post("/post", response_model=carDataOut)
# async def createCar(car:carDataIn):
#     car_data=car.model_dump()
#     car_id=len(car_database)
#     new_car={**car_data, "id": car_id}
#     car_database[car_id]=new_car
#     return new_car

# @app.get("/get", response_model=list[carDataOut])
# async def getCars():
#     return list(car_database.values())

# @app.get("/get/{car_id}")
# async def getCarByID(car_id: int):
#     car = car_database.get(car_id) 
#     if not car:
#         return {"error": "Car not found"}
#     lowball_price = round(car["price"] * 0.85, 2)
#     return f"I can do ${lowball_price} only"

from contextlib import asynccontextmanager
from fastapi import FastAPI
from socialapi.database import database
from socialapi.routers.post import router as post_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app= FastAPI(lifespan=lifespan)

app.include_router(post_router)

