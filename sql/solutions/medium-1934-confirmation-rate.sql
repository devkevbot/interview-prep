SELECT s.user_id, ROUND(
    AVG(
        IF(c.action="confirmed", 1, 0)
    ),
    2) AS confirmation_rate
FROM Signups S
LEFT JOIN Confirmations C ON s.user_id = c.user_id
GROuP BY user_id;