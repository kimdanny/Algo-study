class Solution:
    def strStr1(self, haystack: str, needle: str) -> int:
        # imperative style
        if len(needle)==0:
            return 0
        if len(haystack)==0 or len(haystack)<len(needle):
            return -1
        
        for i, hay in enumerate(haystack):
            for k in range(0,len(needle)):
                if haystack[i+k]==needle[k]:
                    continue
                else:
                    break
        return i

    def strStr2(self, haystack: str, needle: str) -> int:
        # using 'in' and 'index slicing' (pytonic)
        if len(needle)==0:
            return 0
        if needle not in haystack:
            return -1
        
        for i in range(len(haystack)):
            if haystack[i : i+len(needle)]==needle:
                return i
        

    def strStr3(self, haystack: str, needle: str) -> int:
        # pythonic one line solution
        return haystack.find(needle)
        

sol = Solution()
answer = sol.strStr2("hello", "ll")
print(answer)

'''
strStr1.
Runtime: xxxx ms
Memory Usage: xxxxx MB

strStr2.
Runtime: 24 ms
Memory Usage: 12.8 MB

strStr3.
Runtime: 24 ms
Memory Usage: 12.8 MB

'''