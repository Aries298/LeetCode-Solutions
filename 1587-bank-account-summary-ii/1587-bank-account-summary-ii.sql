# Write your MySQL query statement below
SELECT name, SUM(amount) balance
FROM Users
LEFT JOIN Transactions
USING(account)
GROUP BY account
HAVING balance > 10000;