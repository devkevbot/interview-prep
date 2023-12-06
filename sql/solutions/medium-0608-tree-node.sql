-- Union solution
SELECT id, 'Root' AS type
FROM Tree t
WHERE p_id IS NULL
UNION
SELECT id, 'Inner' AS type
FROM Tree t
WHERE EXISTS(SELECT 1 FROM Tree WHERE p_id = t.id) AND p_id IS NOT NULL
UNION
SELECT id, 'Leaf' AS type
FROM tree t
WHERE NOT EXISTS(SELECT 1 FROM Tree WHERE p_id = t.id) AND p_id IS NOT NULL

-- Case solution
SELECT id,
CASE WHEN p_id IS NULL THEN 'Root'
     WHEN id IN (SELECT p_id FROM tree) THEN 'Inner'
     ELSE 'Leaf' end AS type
FROM tree