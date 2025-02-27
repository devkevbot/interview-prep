-- Solution #1
SELECT product_id, product_name
FROM Product
WHERE product_id IN (
    SELECT DISTINCT product_id FROM Sales
    WHERE sale_date BETWEEN '2019-01-01' AND '2019-03-31' AND
    product_id NOT IN (
        SELECT DISTINCT product_id FROM Sales
        WHERE sale_date < '2019-01-01' OR sale_date > '2019-03-31'
    )
)

-- Solution #2
SELECT p.product_id, p.product_name FROM Product p
INNER JOIN Sales s
ON p.product_id = s.product_id
GROUP BY s.product_id
HAVING MIN(s.sale_date) >= '2019-01-01' AND MAX(s.sale_date) <= '2019-03-31';