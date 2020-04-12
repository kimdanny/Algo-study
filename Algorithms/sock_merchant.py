"""
John works at a clothing store. 
He has a large pile of socks that he must pair by color for sale.
Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
For example, there are n=7 socks with colors ar=[1, 2, 1, 2, 1, 3, 2]. There is one pair of color 1 and one of color 2. 
There are three odd socks left, one of each color. The number of pairs is 2.
"""
from collections import Counter

def sockMerchant(n, ar):
    record = Counter(ar)
    count = 0
    for num in dict(record).values():
        if num%2==0:
            count+=num/2
        else:
            count+= (num-1)/2
    
    return int(count)
