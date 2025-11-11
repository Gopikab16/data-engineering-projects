-- 1. View all tables
SELECT name FROM sqlite_master WHERE type='table';

-- 2. Total revenue
SELECT SUM(p.price * o.quantity) AS total_revenue
FROM Orders o
JOIN Products p ON o.product_id = p.product_id;

-- 3. Revenue by city
SELECT c.city, SUM(p.price * o.quantity) AS revenue
FROM Orders o
JOIN Customers c ON o.customer_id = c.customer_id
JOIN Products p ON o.product_id = p.product_id
GROUP BY c.city
ORDER BY revenue DESC;

-- 4. Top 3 customers by revenue
SELECT c.name, SUM(p.price * o.quantity) AS total_spent
FROM Orders o
JOIN Customers c ON o.customer_id = c.customer_id
JOIN Products p ON o.product_id = p.product_id
GROUP BY c.name
ORDER BY total_spent DESC
LIMIT 3;

-- 5. Best-selling products
SELECT p.product_name, SUM(o.quantity) AS total_sold
FROM Orders o
JOIN Products p ON o.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_sold DESC;

-- 6. Average order value
SELECT AVG(total) AS avg_order_value
FROM (
  SELECT SUM(p.price * o.quantity) AS total
  FROM Orders o
  JOIN Products p ON o.product_id = p.product_id
  GROUP BY o.order_id
);

-- 7. Monthly sales trend
SELECT strftime('%m', order_date) AS month, SUM(p.price * o.quantity) AS monthly_revenue
FROM Orders o
JOIN Products p ON o.product_id = p.product_id
GROUP BY month
ORDER BY month;

-- 8. Product category revenue
SELECT p.category, SUM(p.price * o.quantity) AS revenue
FROM Orders o
JOIN Products p ON o.product_id = p.product_id
GROUP BY p.category;

-- 9. Customer order counts
SELECT c.name, COUNT(o.order_id) AS total_orders
FROM Customers c
LEFT JOIN Orders o ON c.customer_id = o.customer_id
GROUP BY c.name;

-- 10. Highest priced product sold
SELECT p.product_name, p.price
FROM Products p
WHERE p.price = (SELECT MAX(price) FROM Products);
