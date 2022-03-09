# https://leetcode.com/problems/valid-palindrome-ii/submissions/


class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        
        edited_string_l, edited_string_r = '', ''
        
        # iterate through left and right two pointers
        for l, r in zip(range(len(s)), range(len(s)-1, -1, -1)):
            # if left and right char not the same, there are two options to remove one char
            # you can remove char in index l or r
            if s[l] != s[r]:
                edited_string_l = s[:l] + s[l+1:]
                edited_string_r = s[:r] + s[r+1:]
                break
        
        # check if either removing l or r 'th char makes palindrome
        return edited_string_l == edited_string_l[::-1] or edited_string_r == edited_string_r[::-1]


sol = Solution()
print(sol.validPalindrome('cbbcc'))
print(sol.validPalindrome('aba'))
print(sol.validPalindrome('abca'))  # You could delete the character 'c'.
print(sol.validPalindrome('abc'))