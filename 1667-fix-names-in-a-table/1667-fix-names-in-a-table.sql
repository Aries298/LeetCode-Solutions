# Write your MySQL query statement below
SELECT user_id, CONCAT(UPPER(SUBSTRING(name,1,1)), LOWER(SUBSTRING(name,2,LENGTH(name)))) as name
FROM Users
ORDER BY Users.user_id ASC