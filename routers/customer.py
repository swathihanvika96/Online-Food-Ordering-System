from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Customer
from schemas import CustomerCreate

router = APIRouter(prefix="/customers", tags=["Customers"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def add_customer(data: CustomerCreate,
                 db: Session = Depends(get_db)):
    customer = Customer(**data.dict())

    db.add(customer)
    db.commit()

    return {"message": "Customer Added"}


@router.get("/")
def view_customers(db: Session = Depends(get_db)):
    return db.query(Customer).all()