from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Customer, FoodItem, Order
from schemas import OrderCreate, OrderStatusUpdate

router = APIRouter(prefix="/orders", tags=["Orders"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def place_order(
        data: OrderCreate,
        db: Session = Depends(get_db)
):
    customer = db.query(Customer).filter(
        Customer.id == data.customer_id
    ).first()

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    food = db.query(FoodItem).filter(
        FoodItem.id == data.food_item_id
    ).first()

    if not food:
        raise HTTPException(
            status_code=404,
            detail="Food item not found"
        )

    total = food.price * data.quantity

    order = Order(
        customer_id=data.customer_id,
        food_item_id=data.food_item_id,
        quantity=data.quantity,
        total_amount=total,
        status="Placed"
    )

    db.add(order)
    db.commit()

    return {
        "message": "Order Placed",
        "total_amount": total
    }


@router.get("/")
def view_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()


@router.put("/cancel/{order_id}")
def cancel_order(
        order_id: int,
        db: Session = Depends(get_db)
):
    order = db.query(Order).filter(
        Order.id == order_id
    ).first()

    order.status = "Cancelled"

    db.commit()

    return {"message": "Order Cancelled"}


@router.put("/{order_id}")
def update_status(
        order_id: int,
        data: OrderStatusUpdate,
        db: Session = Depends(get_db)
):
    order = db.query(Order).filter(
        Order.id == order_id
    ).first()

    if order.status == "Cancelled":
        raise HTTPException(
            status_code=400,
            detail="Cancelled order cannot be modified"
        )

    order.status = data.status

    db.commit()

    return {"message": "Status Updated"}