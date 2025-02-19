DROP TABLE IF EXISTS orders;

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_name TEXT NOT NULL,
    quantity INTEGER,
    order_date TEXT
);

INSERT INTO orders (customer_id, product_name, quantity, order_date)
VALUES 
(1, '키보드', 10, '2025-02-01'),
(2, '마우스', 2, '2025-02-02'),
(3, '노트북 거치대', 1, '2025-02-05');
