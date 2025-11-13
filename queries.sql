-- 1) Total revenue per customer
SELECT c.customer_id,
    c.customer_name,
    COUNT(DISTINCT o.order_id) AS num_orders,
       SUM(oi.quantity * oi.unit_price) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY c.customer_id, c.customer_name
ORDER BY total_spent DESC;

-- 2) Top 10 products by revenue
SELECT p.product_id,
    p.product_name,
    p.category,
       SUM(oi.quantity * oi.unit_price) AS revenue,
    SUM(oi.quantity) AS total_units_sold
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name, p.category
ORDER BY revenue DESC
LIMIT 10;

-- 3) Monthly revenue for the last 12 months
SELECT strftime('%Y-%m', o.order_date) AS year_month,
       SUM(oi.quantity * oi.unit_price) AS revenue
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY year_month
ORDER BY year_month DESC
LIMIT 12;
