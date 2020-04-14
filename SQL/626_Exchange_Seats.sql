-- https://leetcode.com/problems/exchange-seats/
/*
seat
+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Abbot   |
|    2    | Doris   |
|    3    | Emerson |
|    4    | Green   |
|    5    | Jeames  |
+---------+---------+

output:
+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Doris   |
|    2    | Abbot   |
|    3    | Green   |
|    4    | Emerson |
|    5    | Jeames  |
+---------+---------+
*/
-- Solution 1 (205ms)
SELECT (
    CASE
        WHEN MOD(id,2)=1 AND id!=(SELECT COUNT(*) FROM seat) THEN id+1
        WHEN MOD(id,2)=0 THEN id-1
        ELSE id
    END)id, student
FROM seat
ORDER BY id

-- Solution 2 (344ms)
SELECT (
    CASE
        WHEN ((SELECT MAX(id) FROM seat)%2 = 1)
            AND id = (SELECT MAX(id) FROM seat) THEN id
        WHEN id%2 = 1 THEN id + 1
        ELSE id - 1
    END) AS id, student
FROM seat
ORDER BY id

-- Solution 3 (301ms)
SELECT
    s1.id, COALESCE(s2.student, s1.student) AS student
FROM
    seat s1
        LEFT JOIN
    seat s2 ON ((s1.id + 1) ^ 1) - 1 = s2.id
ORDER BY s1.id;
