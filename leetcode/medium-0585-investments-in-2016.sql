-- My solution
SELECT
    ROUND(SUM(i1.tiv_2016), 2) AS tiv_2016
FROM
    Insurance i1
WHERE 
    i1.tiv_2015 IN
    (
        SELECT
            DISTINCT i2.tiv_2015
        FROM
            Insurance i2
        WHERE
            i2.pid != i1.pid
    )
    AND
    (i1.lat, i1.lon) NOT IN
    (
        SELECT
            i3.lat, i3.lon
        FROM
            Insurance i3
        WHERE
            i3.pid != i1.pid
    )

-- Window functions
SELECT
    ROUND(SUM(TIV_2016), 2) AS tiv_2016
FROM
(
    SELECT
        *,
        COUNT(*) OVER(PARTITION BY TIV_2015) AS CNT1,
        COUNT(*) OVER(PARTITION BY LAT, LON) AS CNT2
    FROM
        INSURANCE
) AS TBL
WHERE
    CNT1 >= 2 AND CNT2 = 1