-- My Solution
SELECT id, SUM(count) AS num
FROM (
    SELECT
        requester_id AS id, COUNT(*) AS count
    FROM
        RequestAccepted
    GROUP BY
        requester_id
    UNION ALL
    SELECT
        accepter_id AS id, COUNT(*) AS count
    FROM
        RequestAccepted
    GROUP BY
        accepter_id
) friends
GROUP BY
    id
ORDER BY
    num DESC
LIMIT 1