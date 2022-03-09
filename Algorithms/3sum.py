# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/
# https://leetcode.com/problems/3sum/

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

from itertools import combinations
from typing import List

class Solution_1:
    def threeSum(self, nums_list: List[int]) -> List[List[int]]:
        nums = sorted(nums_list)
        return_list = []
        for i in range(len(nums)):
            x = nums[i]
            two_sum_list = nums[i+1:]
            two_sum_results = self.twoSum(two_sum_list, target_sum=-x)
            for two_sum_result in two_sum_results:
                three_sum = [x] + two_sum_result
                return_list.append(three_sum)
        
        return return_list


    def twoSum(self, nums: List[int], target_sum):
        return_list = []
        for i in range(len(nums)):
            x = nums[i]
            target_num = target_sum - x
            for j in range(i+1, len(nums)-1):
                if nums[j] == target_num:
                    return_list.append([x, nums[j]])
        
        return return_list


class Solution_2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = set()

        #1. Split nums into three lists: negative numbers, positive numbers, and zeros
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0: 
                n.append(num)
            else:
                z.append(num)

        #2. Create a separate set for negatives and positives for O(1) look-up times
        N, P = set(n), set(p)

        #3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
        #   i.e. (-3, 0, 3) = 0
        if z:
            for num in P:
                if -1*num in N:
                    res.add((-1*num, 0, num))

        #3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
        if len(z) >= 3:
            res.add((0,0,0))

        #4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
        #   exists in the positive number set
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                target = -1*(n[i]+n[j])
                if target in P:
                    res.add(tuple(sorted([n[i],n[j],target])))

        #5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
        #   exists in the negative number set
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                target = -1*(p[i]+p[j])
                if target in N:
                    res.add(tuple(sorted([p[i],p[j],target])))

        return list(map(list, list(res)))


class Solution_3(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        N, result = len(nums), []
        for i in range(N):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = nums[i]*-1
            s,e = i+1, N-1
            while s<e:
                if nums[s]+nums[e] == target:
                    result.append([nums[i], nums[s], nums[e]])
                    s = s+1
                    while s<e and nums[s] == nums[s-1]:
                        s = s+1
                elif nums[s] + nums[e] < target:
                    s = s+1
                else:
                    e = e-1
        return result


if __name__ == '__main__':
    _input = [-1,0,1,2,-1,-4]
    # Output: [[-1,-1,2],[-1,0,1]]
    solution1 = Solution_1()
    solution2 = Solution_2()
    solution3 = Solution_3()
    output = solution3.threeSum(_input)
    print(output)


        