"""
Get absolute difference between sum of two opposing diagonals
"""
# Solution 1 - standard
def diagonalDifference(arr):
    sumLR = 0
    sumRL = 0
    j = 0
    z = -1
    # numOfRows = len(arr)
    for i in range(len(arr)):
        sumLR += arr[i][j]
        sumRL += arr[i][z]
        j += 1
        z -= 1
    return abs(sumLR-sumRL)
    
    
# Solution 2 - numpy
import numpy as np

def diagonalDifference(arr):
    # Write your code here
    arr = np.array(arr)
    diagonal1 = np.diagonal(arr)
    flipped = np.fliplr(arr)
    diagonal2 = np.diagonal(flipped)

    return abs(sum(diagonal1)-sum(diagonal2))
    
    
 
# driver code
lst = [[11, 2, 4],[4, 5, 6],[10, 8, -12]]
print(diagonalDifference(lst))
