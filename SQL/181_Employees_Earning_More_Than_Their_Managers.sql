-- https://leetcode.com/problems/employees-earning-more-than-their-managers/
/*
Employee
+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+
write a SQL query that finds out employees who earn more than their managers.
Output:
+----------+
| Employee |
+----------+
| Joe      |
+----------+
*/

-- Solution 1
/*
Select from two tables will get the Cartesian product of these two tables.
In this case, the output will be 4*4 = 16 records.

output table:
{"headers": ["Id", "Name", "Salary", "ManagerId", "Id", "Name", "Salary", "ManagerId"], "values": [[1, "Joe", 70000, 3, 1, "Joe", 70000, 3], [2, "Henry", 80000, 4, 1, "Joe", 70000, 3], [3, "Sam", 60000, null, 1, "Joe", 70000, 3], [4, "Max", 90000, null, 1, "Joe", 70000, 3], [1, "Joe", 70000, 3, 2, "Henry", 80000, 4], [2, "Henry", 80000, 4, 2, "Henry", 80000, 4], [3, "Sam", 60000, null, 2, "Henry", 80000, 4], [4, "Max", 90000, null, 2, "Henry", 80000, 4], [1, "Joe", 70000, 3, 3, "Sam", 60000, null], [2, "Henry", 80000, 4, 3, "Sam", 60000, null], [3, "Sam", 60000, null, 3, "Sam", 60000, null], [4, "Max", 90000, null, 3, "Sam", 60000, null], [1, "Joe", 70000, 3, 4, "Max", 90000, null], [2, "Henry", 80000, 4, 4, "Max", 90000, null], [3, "Sam", 60000, null, 4, "Max", 90000, null], [4, "Max", 90000, null, 4, "Max", 90000, null]]}
*/
SELECT a.Name AS 'Employee'
FROM Employee a INNER JOIN Employee b
ON a.ManagerId = b.Id
  AND a.Salary > b.Salary

-- Solution 2
SELECT a.Name AS 'Employee'
FROM Employee a, Employee b
WHERE a.ManagerId = b.Id
  AND a.Salary > b.Salary

-- Solution 3 (skrrr! SubQuery Flex solution)
SELECT Name AS 'Employee'
FROM Employee
INNER JOIN
    (SELECT DISTINCT E1.Id AS 'ManId', E1.Salary AS 'ManSalary'
     FROM Employee E1
     INNER JOIN Employee E2
     ON E1.Id = E2.ManagerId) Manager
     ON Employee.ManagerId = Manager.ManId
WHERE Employee.Salary > Manager.ManSalary
