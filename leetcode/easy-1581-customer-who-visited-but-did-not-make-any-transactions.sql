-- NOT IN solution
SELECT v.customer_id, COUNT(*) AS count_no_trans
FROM Visits v
WHERE v.visit_id NOT IN (SELECT DISTINCT t.visit_id FROM Transactions t)
GROUP BY v.customer_id

-- LEFT JOIN solution
SELECT customer_id, COUNT(v.visit_id) as count_no_trans 
FROM Visits v
LEFT JOIN Transactions t ON v.visit_id = t.visit_id
WHERE transaction_id IS NULL
GROUP BY customer_id

-- WHERE NOT EXISTS solution
SELECT customer_id, COUNT(visit_id) as count_no_trans 
FROM Visits v
WHERE NOT EXISTS (
	SELECT visit_id FROM Transactions t 
	WHERE t.visit_id = v.visit_id
	)
GROUP BY customer_id