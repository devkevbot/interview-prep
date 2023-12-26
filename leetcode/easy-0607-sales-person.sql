-- My Solution
SELECT name FROM SalesPerson
WHERE sales_id NOT IN
(
    SELECT sales_id FROM Orders WHERE com_id IN (
        SELECT com_id FROM Company where name = "RED"
    )
)

-- Alternate Solution
SELECT name FROM SalesPerson
WHERE sales_id NOT IN
(
    SELECT sales_id FROM Orders
    LEFT JOIN Company ON Orders.com_id = company.com_id
    WHERE company.name = "RED"
)
