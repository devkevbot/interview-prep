SELECT customer_id
FROM (
    SELECT c.customer_id, p.product_key
    FROM Customer c
    INNER JOIN Product p
    on c.product_key = p.product_key
) c_p -- Use the inner join to only include products which exist in the Product table
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(DISTINCT product_key) FROM Product)