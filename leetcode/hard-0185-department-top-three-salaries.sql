-- My solution
SELECT
    Employee,
    Salary,
    Department
FROM (
    SELECT
        e.name AS Employee,
        e.salary AS Salary,
        d.name AS Department,
    DENSE_RANK() OVER (
        PARTITION BY e.departmentId
        ORDER BY e.salary DESC
    ) AS salary_rank
    FROM
        Employee e
    INNER JOIN
        Department d ON e.departmentId = d.id
    ) salaries
WHERE
    salaries.salary_rank <= 3
