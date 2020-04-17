-- https://leetcode.com/problems/duplicate-emails/
/*
Write a SQL query to find all duplicate emails in a table named Person.
+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
output:
+---------+
| Email   |
+---------+
| a@b.com |
+---------+
*/
-- Solution 1
SELECT Email
FROM(
SELECT COUNT(Email) as email_count, Email
FROM Person
GROUP BY Email) alias
WHERE alias.email_count>1

-- Solution 2
SELECT Email
FROM Person
GROUP BY Email
HAVING COUNT(Email)>1

-- Solution 3
SELECT DISTINCT p1.Email
FROM Person p1, Person p2
WHERE p1.Email = p2.Email
    AND p1.Id!=p2.Id
