# Solution 1 #
class Solution:
    def removeOuterParentheses(self, string: str) -> str:
        result = []
        count = {
            "head" : 0,
            "(" : 0, 
            ")" : 0
        }
        for i in range(len(string)):
            if string[i]=="(":
                count["("] += 1
            else:
                count[")"] += 1
            
            if count["("] == count[")"]:
                result.append(string[count["head"]+1 : i])
                count["head"] = i+1
                
        return "".join(result)

'''
Runtime: 40 ms
Memory: 13.9 MB
'''

# Solution 2 #
class Solution:
    def removeOuterParentheses(self, string: str) -> str:
        result = []
        head = 0
        opening = 0
        closing = 0
        
        for i in range(len(string)):
            if string[i]=="(":
                opening += 1
            else:
                closing += 1
            
            if opening == closing:
                result.append(string[head+1 : i])
                head = i+1
                
        return "".join(result)

'''
Runtime: 32 ms
Memory: 14.1 MB	
'''
        
