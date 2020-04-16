-- https://leetcode.com/problems/classes-more-than-5-students/
/*
Please list out all classes which have more than or equal to 5 students.
courses
+---------+------------+
| student | class      |
+---------+------------+
| A       | Math       |
| B       | English    |
| C       | Math       |
| D       | Biology    |
| E       | Math       |
| F       | Computer   |
| G       | Math       |
| H       | Math       |
| I       | Math       |
+---------+------------+
output:
+---------+
| class   |
+---------+
| Math    |
+---------+
*/
-- Solution 1
/*
DISTINCT keyword was the bug that I couldnt find for 30 mins :(
*/
SELECT class
FROM (
    SELECT class, COUNT(DISTINCT student) AS student_count
    FROM courses
    GROUP BY class) alias
WHERE alias.student_count>=5

-- Solution 2
/*HAVING seems pretty useful!!*/
SELECT class
FROM courses
GROUP BY class
HAVING COUNT(DISTINCT student)>=5
