"""
Lilah has a string, s, of lowercase English letters that she repeated infinitely many times.
Given an integer, n, find and print the number of letter a's in the first n letters of Lilah's infinite string.
For example, if the string s='abcac' and n=10, the substring we consider is abcacabcac, 
the first 10 characters of her infinite string. There are 4 occurrences of 'a' in the substring.
"""

def repeatedString(s, n):
    stringLength = len(s)
    numAs = s.count('a')
    extras = s[0 : n % stringLength]
    reps = n // stringLength

    count = numAs*reps + extras.count('a')
    return count
