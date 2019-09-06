# Solution 1 #
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        A.sort(key=lambda x: x%2)
        return A

'''
Runtime: 96 ms
Memory: 14.3 MB
'''

# Solution 2 #
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        for i in range(len(A)):
            if A[i]%2==0:
                A.insert(0, A[i])
                del A[i+1]
        return A

'''
Runtime: 120 ms
Memory: 14.4 MB
'''

# Solution 3 #
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even = []
        odd = []
        for x in A:
            if x%2==0:
                even.append(x)
            else:
                odd.append(x)
        even.extend(odd)
        return even

'''
Runtime: 92 ms
Memory: 14.7 MB
'''
