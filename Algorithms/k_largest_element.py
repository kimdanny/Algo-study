# https://leetcode.com/problems/kth-largest-element-in-an-array/


import random

class Solution:
    def findKthLargest(self, nums, k):
        
        pivot = random.choice(nums)
        # left =  [x for x in nums if x > pivot]
        # mid  =  [x for x in nums if x == pivot]
        # right = [x for x in nums if x < pivot]
        
        left, mid, right = [], [], []
        for x in nums:
            if x > pivot:
                left.append(x)
            elif x == pivot:
                mid.append(x)
            else:
                right.append(x)
        
        
        L, M = len(left), len(mid)
        
        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]


sol = Solution()
print(sol.findKthLargest([3,2,1,5,6,4], k=2))
print(sol.findKthLargest([3,2,3,1,2,4,5,5,6], k=2))
