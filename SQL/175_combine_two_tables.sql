-- https://leetcode.com/problems/combine-two-tables/

/*This is wrong
Using where clause to filter the records will fail 
if there is no address information for a person because it will not display the name information.
*/
-- SELECT p.FirstName, p.LastName, a.City, a.State 
-- FROM Person p, Address a
-- WHERE p.PersonId = a.PersonId

SELECT FirstName, LastName, City, State
FROM Person p LEFT JOIN Address a
ON p.PersonId = a.PersonId