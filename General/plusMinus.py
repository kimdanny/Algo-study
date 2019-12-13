# https://www.hackerrank.com/challenges/plus-minus/problem

def plusMinus(arr):
    plusnum = 0
    minusnum = 0
    zeronum = 0
    totalnum = len(arr)

    for x in arr:
        if x>0:
            plusnum+=1
        elif x<0:
            minusnum+=1
        else:
            zeronum+=1

    return round(plusnum/totalnum, 6), round(minusnum/totalnum, 6), round(zeronum/totalnum, 6)


array1 = [-4, 3, -9, 0, 4, 1]
testArray1 = plusMinus(array1)
print(testArray1)