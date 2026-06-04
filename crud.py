from sqlalchemy.orm import Session
from models import Restaurant, FoodItem, Customer, Order


# -----------------------------
# Restaurant CRUD
# -----------------------------

def create_restaurant(db: Session, data):
    restaurant = Restaurant(
        name=data.name,
        location=data.location
    )
    db.add(restaurant)
    db.commit()
    db.refresh(restaurant)
    return restaurant


def get_restaurants(db: Session):
    return db.query(Restaurant).all()


def get_restaurant(db: Session, restaurant_id: int):
    return db.query(Restaurant).filter(
        Restaurant.id == restaurant_id
    ).first()


def update_restaurant(db: Session, restaurant_id: int, data):
    restaurant = get_restaurant(db, restaurant_id)

    if restaurant:
        restaurant.name = data.name
        restaurant.location = data.location

        db.commit()
        db.refresh(restaurant)

    return restaurant


def delete_restaurant(db: Session, restaurant_id: int):
    restaurant = get_restaurant(db, restaurant_id)

    if restaurant:
        db.delete(restaurant)
        db.commit()

    return restaurant


# -----------------------------
# Food Item CRUD
# -----------------------------

def create_food(db: Session, data):
    food = FoodItem(
        name=data.name,
        price=data.price,
        restaurant_id=data.restaurant_id
    )

    db.add(food)
    db.commit()
    db.refresh(food)

    return food


def get_foods(db: Session):
    return db.query(FoodItem).all()


def get_food(db: Session, food_id: int):
    return db.query(FoodItem).filter(
        FoodItem.id == food_id
    ).first()


def update_food(db: Session, food_id: int, data):
    food = get_food(db, food_id)

    if food:
        food.name = data.name
        food.price = data.price
        food.restaurant_id = data.restaurant_id

        db.commit()
        db.refresh(food)

    return food


def delete_food(db: Session, food_id: int):
    food = get_food(db, food_id)

    if food:
        db.delete(food)
        db.commit()

    return food


# -----------------------------
# Customer CRUD
# -----------------------------

def create_customer(db: Session, data):
    customer = Customer(
        name=data.name,
        phone=data.phone
    )

    db.add(customer)
    db.commit()
    db.refresh(customer)

    return customer


def get_customers(db: Session):
    return db.query(Customer).all()


def get_customer(db: Session, customer_id: int):
    return db.query(Customer).filter(
        Customer.id == customer_id
    ).first()


# -----------------------------
# Order CRUD
# -----------------------------

def create_order(
    db: Session,
    customer_id: int,
    food_item_id: int,
    quantity: int
):
    food = get_food(db, food_item_id)

    total = food.price * quantity

    order = Order(
        customer_id=customer_id,
        food_item_id=food_item_id,
        quantity=quantity,
        total_amount=total,
        status="Placed"
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    return order


def get_orders(db: Session):
    return db.query(Order).all()


def get_order(db: Session, order_id: int):
    return db.query(Order).filter(
        Order.id == order_id
    ).first()


def cancel_order(db: Session, order_id: int):
    order = get_order(db, order_id)

    if order:
        order.status = "Cancelled"
        db.commit()
        db.refresh(order)

    return order


def update_order_status(
    db: Session,
    order_id: int,
    status: str
):
    order = get_order(db, order_id)

    if order:
        order.status = status
        db.commit()
        db.refresh(order)

    return order