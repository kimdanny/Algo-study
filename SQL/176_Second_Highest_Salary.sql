-- https://leetcode.com/problems/second-highest-salary/
/*
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+

output:
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
*/


/*
SELECT Salary as SecondHighestSalary
FROM Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 1
*/
/*Above solution will be judged as 'Wrong Answer' if there is no such second highest salary since there might be only one record in this table.*/

-- Solution 1
SELECT
(SELECT DISTINCT Salary
FROM Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 1
) AS SecondHighestSalary

-- Solution 2
SELECT (
    IFNULL(
        (
        SELECT DISTINCT Salary
        FROM Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1
        ),
        NULL
    )
) AS SecondHighestSalary
