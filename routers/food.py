from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models import FoodItem
from schemas import FoodCreate

router = APIRouter(prefix="/foods", tags=["Food Items"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def add_food(data: FoodCreate, db: Session = Depends(get_db)):
    food = FoodItem(**data.dict())
    db.add(food)
    db.commit()

    return {"message": "Food Added"}


@router.get("/")
def view_foods(db: Session = Depends(get_db)):
    return db.query(FoodItem).all()


@router.put("/{food_id}")
def update_food(food_id: int,
                data: FoodCreate,
                db: Session = Depends(get_db)):
    food = db.query(FoodItem).filter(
        FoodItem.id == food_id
    ).first()

    food.name = data.name
    food.price = data.price
    food.restaurant_id = data.restaurant_id

    db.commit()

    return {"message": "Food Updated"}


@router.delete("/{food_id}")
def delete_food(food_id: int,
                db: Session = Depends(get_db)):
    food = db.query(FoodItem).filter(
        FoodItem.id == food_id
    ).first()

    db.delete(food)
    db.commit()

    return {"message": "Food Deleted"}