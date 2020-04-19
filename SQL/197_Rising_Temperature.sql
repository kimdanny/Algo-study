-- https://leetcode.com/problems/rising-temperature/
/*
Write a SQL query to find all dates' Ids with higher temperature compared to its previous (yesterday's) dates.
+---------+------------------+------------------+
| Id(INT) | RecordDate(DATE) | Temperature(INT) |
+---------+------------------+------------------+
|       1 |       2015-01-01 |               10 |
|       2 |       2015-01-02 |               25 |
|       3 |       2015-01-03 |               20 |
|       4 |       2015-01-04 |               30 |
+---------+------------------+------------------+
For example, return the following Ids for the above Weather table:
+----+
| Id |
+----+
|  2 |
|  4 |
+----+
*/
/*
<What I did at first> --> didnt cover edge cases
SELECT w1.Id
FROM Weather w1, Weather w2
WHERE w1.Id-w2.Id = 1
AND w1.Temperature > w2.Temperature

This worked for above case.
However, the edge case was where DATE is not ordered chronologically.
Such as:
{"headers": {"Weather": ["Id", "RecordDate", "Temperature"]}, "rows": {"Weather": [[1, "2000-12-16", 3], [2, "2000-12-15", -1]]}}
which should output:
{"headers":["Id"],"values":[[1]]}
but instead mine outputs:
{"headers": ["Id"], "values": []}
*/

-- Solution 1
SELECT w1.Id
FROM Weather w1, Weather w2
WHERE DATEDIFF(w1.RecordDate, w2.RecordDate) = 1
AND w1.Temperature > w2.Temperature

-- Solution 2
SELECT w1.Id
FROM Weather w1 INNER JOIN Weather w2
ON DATEDIFF(w1.RecordDate, w2.RecordDate) = 1
AND w1.Temperature > w2.Temperature
