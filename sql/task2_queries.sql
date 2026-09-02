-- Task 2: SQL Fundamentals

-- Query 1: View all columns
SELECT *
FROM ecommerce_sales
LIMIT 10;
-- TASK 2: SQL FUNDAMENTALS

-- Query 1: Display 10 records
SELECT *
FROM ecommerce_sales
LIMIT 10;


-- Query 2: Select specific columns
SELECT order_id, category, price, quantity
FROM ecommerce_sales
LIMIT 10;


-- Query 3: Find orders with price greater than 100
SELECT order_id, category, price
FROM ecommerce_sales
WHERE price > 100;


-- Query 4: Sort products by highest price
SELECT order_id, category, price
FROM ecommerce_sales
ORDER BY price DESC
LIMIT 10;
