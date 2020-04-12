# Solution 1 #
class Solution1:
    def peakIndexInMountainArray(self, A) -> int:
        for i in range(len(A)):
            if A[i] > A[i+1]:
                return i

'''
Runtime: 84 ms
Memory Usage: 15.1 MB
'''

# Solution 2 #
class Solution2:
    def peakIndexInMountainArray(self, A) -> int:
        front = 0
        back = 1
        last = len(A)-1
        while back != last:
            if A[front] < A[back]:
                front += 1
                back += 1    
            else:
                break
        
        return front

'''
Runtime: 108 ms
Memory Usage: 15.2 MB
'''
