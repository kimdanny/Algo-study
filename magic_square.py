"""
We define a magic square to be an nxn matrix of distinct positive integers from 1 to n^2 
where the sum of any row, column, or diagonal of length n is always equal to the same number: the magic constant.

You will be given a 3x3 matrix s of integers in the inclusive range [1, 9].
We can convert any digit a to any other digit b in the range [1, 9] at cost of |a-b|.
Given s, convert it into a magic square at minimal cost. Print this cost on a new line.
"""

# x and y are 3x3 matrix
def costFunction(x, y):
    total = 0
    cost = 0
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i][j] != y[i][j]:
                cost = abs(x[i][j]-y[i][j])
                total += cost

    return total

# ----- checkers ------
# input: 2D Matrix
# output: Boolean

def rowchecker(s):
    return sum(s[0]) == sum(s[1]) == sum(s[2])

def columnChecker(s):
    sum0 = sum1 = sum2 = 0
    for i in range(len(s)):
        sum0 += s[i][0]
        sum1 += s[i][1]
        sum2 += s[i][2]

    return sum0 == sum1 == sum2

def diagonalChecker(s):
    sumLR = 0
    sumRL = 0
    j = 0
    z = -1
    for i in range(len(s)):
        sumLR += s[i][j]
        sumRL += s[i][z]
        j += 1
        z -= 1
    return sumLR == sumRL

def isDistinct(s):
    lst = []
    for row in s:
        lst.extend(row)

    return len(set(lst)) == len(lst)

def isMagicSquare(s):
    return rowchecker(s) and columnChecker(s) and diagonalChecker(s) and isDistinct(s)

# ------------------------

def formingMagicSquare(s):
    pass
        

matrixTrial = [[5, 3, 4],[1, 5, 8],[6, 4, 2]]
print(formingMagicSquare(matrixTrial)) # output: 7

# For Testing
# wrong = [[5, 3, 4],
#         [1, 5, 8],
#         [6, 4, 2]]

# ms=[[8, 3, 4],
#     [1, 5, 9],
#     [6, 7, 2]]
