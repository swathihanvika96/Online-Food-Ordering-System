from fastapi import FastAPI
from database import engine, Base

from routers import restaurant
from routers import food
from routers import customer
from routers import order

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Food Ordering System")

app.include_router(restaurant.router)
app.include_router(food.router)
app.include_router(customer.router)
app.include_router(order.router)