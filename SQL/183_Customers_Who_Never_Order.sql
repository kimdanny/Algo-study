-- https://leetcode.com/problems/customers-who-never-order/
/*
Write a SQL query to find all customers who never order anything.
Table: Customers.
+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Table: Orders.
+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
Using the above tables as example, return the following:
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
*/
-- Solution 1
SELECT c.Name AS 'Customers'
FROM Customers c
WHERE c.Id NOT IN(
    SELECT CustomerId
    FROM Orders)

-- Solution 2 (Notable)
/*
SELECT *
FROM Customers c LEFT JOIN Orders o
ON c.Id = o.CustomerId

output:
{"headers": ["Id", "Name", "Id", "CustomerId"], "values": [[3, "Sam", 1, 3], [1, "Joe", 2, 1], [2, "Henry", null, null], [4, "Max", null, null]]}
*/
SELECT c.Name AS 'Customers'
FROM Customers c LEFT JOIN Orders o
ON c.Id = o.CustomerId
WHERE o.CustomerId IS NULL
-- WHERE o.CustomerId = NULL --> NOOO!!!
    -- IS tests against a boolean(True/False/NULL neither) where as = tests equivalency
    -- IS can only be used against variables that return true, false or NULL .
