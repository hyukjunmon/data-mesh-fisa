DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    country TEXT
);

INSERT INTO customers (name, country)
VALUES
('Zheng Chag Xun', 'CN1'),
('과즙웅상', 'KR1'),
('한자리비어요', 'KR1');
