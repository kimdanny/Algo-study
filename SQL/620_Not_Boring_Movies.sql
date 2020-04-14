-- https://leetcode.com/problems/not-boring-movies/
/*
cinema
+---------+-----------+--------------+-----------+
|   id    | movie     |  description |  rating   |
+---------+-----------+--------------+-----------+
|   1     | War       |   great 3D   |   8.9     |
|   2     | Science   |   fiction    |   8.5     |
|   3     | irish     |   boring     |   6.2     |
|   4     | Ice song  |   Fantacy    |   8.6     |
|   5     | House card|   Interesting|   9.1     |
+---------+-----------+--------------+-----------+
*/

SELECT * FROM cinema
WHERE id%2 != 0
-- WHERE MOD(id,2)=1    --> same as above
AND description!='boring'
ORDER BY rating DESC
