from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Restaurant
from schemas import RestaurantCreate

router = APIRouter(prefix="/restaurants", tags=["Restaurants"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def add_restaurant(data: RestaurantCreate, db: Session = Depends(get_db)):
    restaurant = Restaurant(**data.dict())
    db.add(restaurant)
    db.commit()
    return {"message": "Restaurant Added"}


@router.get("/")
def view_restaurants(db: Session = Depends(get_db)):
    return db.query(Restaurant).all()


@router.put("/{restaurant_id}")
def update_restaurant(
        restaurant_id: int,
        data: RestaurantCreate,
        db: Session = Depends(get_db)
):
    restaurant = db.query(Restaurant).filter(
        Restaurant.id == restaurant_id
    ).first()

    restaurant.name = data.name
    restaurant.location = data.location

    db.commit()

    return {"message": "Restaurant Updated"}


@router.delete("/{restaurant_id}")
def delete_restaurant(
        restaurant_id: int,
        db: Session = Depends(get_db)
):
    restaurant = db.query(Restaurant).filter(
        Restaurant.id == restaurant_id
    ).first()

    db.delete(restaurant)
    db.commit()

    return {"message": "Restaurant Deleted"}