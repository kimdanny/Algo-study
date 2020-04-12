# def uniqueOccurrences(self, arr: List[int]) -> bool:

class Solution:
    def uniqueOccurrences(self, arr):
        occurLog = {}
        for x in arr:
            if x not in occurLog:
                occurLog.update({x : 1})
            else:
                occurLog[x] += 1

        valueList = list(occurLog.values())
        dupRemoved = set(valueList)

        return (len(valueList) == len(dupRemoved))
