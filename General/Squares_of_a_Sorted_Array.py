# Solution 1
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(list(map(lambda x: x**2, A)))
        
# Solution 2
