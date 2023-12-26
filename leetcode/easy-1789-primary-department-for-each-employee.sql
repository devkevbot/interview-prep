SELECT
    employee_id,
    department_id 
FROM
    Employee
WHERE
    primary_flag = 'Y'
UNION
SELECT
    employee_id,
    department_id -- Not part of the GROUP BY, which could error in some RDBMS
FROM
    Employee 
GROUP BY
    employee_id
HAVING
    COUNT(employee_id) = 1