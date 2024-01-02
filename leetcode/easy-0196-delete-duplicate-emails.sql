WITH unique_emails AS (
    SELECT
    MIN(id) AS id, email
FROM
    Person
GROUP BY
    email
)

DELETE FROM
    Person
WHERE
    (id, email) NOT IN (
        SELECT
            *
        FROM
            unique_emails
    )