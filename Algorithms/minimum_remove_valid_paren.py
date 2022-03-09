# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution:
    def remove_at_i(self, s: str, i: int) -> str:
        return s[:i] + s[i+1: ]

    def minRemoveToMakeValid(self, s: str) -> str:
        # use stack to validate parenthesis
        # format of element of stack: [(paren, index)]
        stack = []
        for i, c in enumerate(s):
            if c in {'(', ')'}:
                if stack and stack[-1][0] == '(' and c == ')':
                    # cancel out
                    stack.pop()
                else:
                    stack.append(tuple((c, i)))
        
        answer = s
        for paren, i in stack[::-1]:
            answer = self.remove_at_i(answer, i)

        return answer


sol = Solution()
print(sol.minRemoveToMakeValid('lee(t(c)o)de)'))  # "lee(t(c)o)de", "lee(t(co)de)" , "lee(t(c)ode)"
print(sol.minRemoveToMakeValid('a)b(c)d'))  # 'ab(c)d'
print(sol.minRemoveToMakeValid('))(('))  # ''
