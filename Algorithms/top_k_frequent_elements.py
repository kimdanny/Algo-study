# https://leetcode.com/problems/top-k-frequent-elements/
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num not in counter:
                counter.update({num: 1})
            else:
                counter[num] += 1
        
        # sorted_counter = sorted(counter, key=counter.get, reverse=True)
        # return sorted_counter[:k]
        
        sorted_counter = {k: v for k, v in sorted(counter.items(), key=lambda item: item[1], reverse=True)}
        
        return list(sorted_counter.keys())[:k]
        
import heapq
class Solution_2a:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums


        counter = {}
        for num in nums:
            if num not in counter:
                counter.update({num: 1})
            else:
                counter[num] += 1
        
        return heapq.nlargest(k, counter.keys(), key=counter.get)


from collections import Counter
class Solution_2b:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        # counter = {}
        # for num in nums:
        #     if num not in counter:
        #         counter.update({num: 1})
        #     else:
        #         counter[num] += 1
        counter = Counter(nums)
        
        heap = []
        for num, count in counter.items():
            if len(heap) == k:
                heapq.heappushpop(heap, (count, num))
            else:
                heapq.heappush(heap, (count, num))
        
        return [num for count, num in heap]

