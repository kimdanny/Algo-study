# https://www.hackerrank.com/challenges/circular-array-rotation/problem

def circularArrayRotation(arr, k, queries):
    for _ in range(k):
        arr.insert(0, arr.pop(len(arr)-1))

    # print("arr: ", arr)      arr:  [5, 6, 7, 8, 1, 2, 3, 4]
    for x in queries:
        print(arr[x])


import collections
def circularArrayRotation1(arr, k, queries):
    arr = collections.deque(arr, len(arr))
    arr.rotate(k)
    # print(arr)        deque([5, 6, 7, 8, 1, 2, 3, 4], maxlen=8)
    for i in queries:
        print(arr[i])


arr = [1, 2, 3, 4, 5, 6, 7, 8]
q = [0, 2, 5]
circularArrayRotation(arr, 4, q)
print("----")
arr = [1, 2, 3, 4, 5, 6, 7, 8]
circularArrayRotation1(arr, 4, q)
