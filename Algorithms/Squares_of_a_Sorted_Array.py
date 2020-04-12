# Solution 1
# def sortedSquares(self, A: List[int]) -> List[int]:

class Solution:
    def sortedSquares(self, A):
        return sorted(list(map(lambda x: x**2, A)))
        