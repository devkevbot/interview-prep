-- Join solution
SELECT
    q1.person_name
FROM
    Queue q1
INNER JOIN
    Queue q2 ON q1.turn >= q2.turn
GROUP BY q1.turn
HAVING SUM(q2.weight) <= 1000
ORDER BY SUM(q2.weight) DESC
LIMIT 1

-- Window function
SELECT
    person_name
FROM
(
    SELECT
        person_name,
        weight,
        turn,
        SUM(weight) OVER(ORDER BY turn) AS cum_sum
    FROM
        Queue
) cum_sums
WHERE
    cum_sum <= 1000
ORDER BY
    turn DESC
LIMIT 1