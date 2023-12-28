SELECT
    DISTINCT num AS ConsecutiveNums
FROM
    (
        SELECT
            id,
            num,
            LAG(num) OVER (ORDER BY id) AS prev,
            LEAD(num) OVER (ORDER BY id) AS next
        FROM
            Logs
    ) prev_next
WHERE
    num = prev
    AND
    prev = next