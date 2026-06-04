from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(40))
    location = Column(String(100))


class FoodItem(Base):
    __tablename__ = "food_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    price = Column(Float)

    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(40))
    phone = Column(String(20))


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)

    customer_id = Column(Integer, ForeignKey("customers.id"))
    food_item_id = Column(Integer, ForeignKey("food_items.id"))

    quantity = Column(Integer)
    total_amount = Column(Float)

    status = Column(String(50), default="Placed")