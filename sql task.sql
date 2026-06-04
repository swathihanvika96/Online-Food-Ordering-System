CREATE DATABASE onlineFood_db;

USE onlineFood_db;

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    phone VARCHAR(15)
);

INSERT INTO Customers VALUES
(1, 'Yaswanth', '9876543210'),
(2, 'Neha', '9876543211');

CREATE TABLE Restaurants (
    restaurant_id INT PRIMARY KEY,
    restaurant_name VARCHAR(100),
    location VARCHAR(100)
);

INSERT INTO Restaurants VALUES
(1, 'Spice Hub', 'Bangalore'),
(2, 'A2B', 'Chennai');

CREATE TABLE Food_Items (
    food_id INT PRIMARY KEY,
    food_name VARCHAR(100),
    price DECIMAL(10,2),
    restaurant_id INT,
    FOREIGN KEY (restaurant_id) REFERENCES Restaurants(restaurant_id)
);

INSERT INTO Food_Items VALUES
(1, 'Burger', 150, 1),
(2, 'Biryani', 500, 2);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

INSERT INTO Orders VALUES
(101, 1, '2025-06-01'),
(102, 2, '2025-06-01');

CREATE TABLE Order_Items (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    food_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (food_id) REFERENCES Food_Items(food_id)
);

INSERT INTO Order_Items VALUES
(1, 101, 1, 2),
(2, 101, 2, 1);

SELECT
    f.food_name,
    SUM(oi.quantity) AS total_sold
FROM Food_Items f
JOIN Order_Items oi
ON f.food_id = oi.food_id
GROUP BY f.food_name
ORDER BY total_sold DESC;


SELECT
    c.customer_name,
    COUNT(o.order_id) AS total_orders
FROM Customers c
JOIN Orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_name
HAVING COUNT(o.order_id) > 3;

SELECT
    r.restaurant_name,
    SUM(oi.quantity) AS total_items_sold
FROM Restaurants r
JOIN Food_Items f
ON r.restaurant_id = f.restaurant_id
JOIN Order_Items oi
ON f.food_id = oi.food_id
GROUP BY r.restaurant_name
ORDER BY total_items_sold DESC
LIMIT 1;

SELECT
    order_date,
    COUNT(order_id) AS total_orders
FROM Orders
GROUP BY order_date
ORDER BY order_date;

SELECT
    food_name,
    total_sold,
    RANK() OVER (ORDER BY total_sold DESC) AS sales_rank
FROM (
    SELECT
        f.food_name,
        SUM(oi.quantity) AS total_sold
    FROM Food_Items f
    JOIN Order_Items oi
    ON f.food_id = oi.food_id
    GROUP BY f.food_name
) AS SalesData;

