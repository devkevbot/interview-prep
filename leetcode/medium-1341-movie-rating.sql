-- Person who has rated the most movies
SELECT
    user_name AS results
FROM
(
    SELECT
        u.name AS user_name,
        COUNT(*) AS counts
    FROM
        MovieRating AS mr
    JOIN
        Users AS u ON mr.user_id = u.user_id
    GROUP BY
        mr.user_id
    ORDER BY
        counts DESC,
        user_name ASC
    LIMIT 1
) first_query
UNION ALL
-- Movie with highest rating in February 2020
SELECT
    movie_name AS results 
FROM
(
    SELECT
        m.title AS movie_name, 
        AVG(mr.rating) AS grade 
    FROM
        MovieRating AS mr
    JOIN
        Movies AS m ON mr.movie_id = m.movie_id
    WHERE
        MONTH(mr.created_at) = '02' AND YEAR(mr.created_at) = '2020'
    GROUP BY
        mr.movie_id
    ORDER BY 
        grade DESC,
        movie_name ASC
    LIMIT 1
) second_query;