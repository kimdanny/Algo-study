# Solution 1 #
# sortArrayByParity(self, A: List[int]) -> List[int]

class Solution1:
    def sortArrayByParity(self, A):
        A.sort(key=lambda x: x%2)
        return A

'''
Runtime: 96 ms
Memory: 14.3 MB
'''

# Solution 2 #
# Bad solution. Don't follow this
class Solution2:
    def sortArrayByParity(self, A):
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
class Solution3:
    def sortArrayByParity(self, A):
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
