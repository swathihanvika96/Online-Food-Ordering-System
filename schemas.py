from pydantic import BaseModel


# Restaurant

class RestaurantCreate(BaseModel):
    name: str
    location: str


# Food Item

class FoodCreate(BaseModel):
    name: str
    price: float
    restaurant_id: int


# Customer

class CustomerCreate(BaseModel):
    name: str
    phone: str


# Order

class OrderCreate(BaseModel):
    customer_id: int
    food_item_id: int
    quantity: int


class OrderStatusUpdate(BaseModel):
    status: str