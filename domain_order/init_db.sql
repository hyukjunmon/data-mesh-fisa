DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    country TEXT
);

INSERT INTO customers (name, country)
VALUES
('Alice', 'USA'),
('Bob', 'UK'),
('Charlie', 'Korea');
