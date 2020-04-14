-- https://leetcode.com/problems/rank-scores/
/*
Scores
+----+-------+
| Id | Score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+

output:
+-------+------+
| Score | Rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+
*/
-- Solution 1 (330ms)
SELECT
  Score,
  @rank := @rank + (@prev != (@prev := Score)) Rank
FROM
  Scores,
  (SELECT @rank := 0, @prev := -1) alias
ORDER BY Score DESC

-- Solution 2 (734ms)
-- This one counts, for each score, the number of distinct greater or equal scores.
SELECT
  Score,
  (SELECT COUNT(DISTINCT Score) FROM Scores WHERE Score >= s.Score) AS Rank
FROM Scores s
ORDER BY Score DESC

-- Solution 3 (241ms)
-- Same as the previous one, but faster because I have a subquery
-- that "uniquifies" the scores first.
-- Not entirely sure why it's faster, I'm guessing MySQL makes tmp a temporary table and uses it for every outer Score.
      /*
      SELECT DISTINCT Score s FROM Scores
      output:
      {"headers": ["s"], "values": [[3.50], [3.65], [4.00], [3.85]]}

      SELECT COUNT(*) FROM (SELECT DISTINCT Score s FROM Scores) tmp
      output:
      {"headers": ["COUNT(*)"], "values": [[4]]}

      SELECT
          Score,
          (SELECT COUNT(*) FROM (SELECT DISTINCT Score s FROM Scores) tmp WHERE s>=Score) Rank
      FROM Scores
      output:
      {"headers": ["Score", "Rank"], "values": [[3.50, 4], [3.65, 3], [4.00, 1], [3.85, 2], [4.00, 1], [3.65, 3]]}
      */

SELECT
  Score,
  (SELECT COUNT(*) FROM (SELECT DISTINCT Score s FROM Scores) tmp WHERE s >= Score) Rank
FROM Scores
ORDER BY Score DESC
