# Solution 1
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = bin(x)[2:]
        y = bin(y)[2:]
        lenX, lenY = len(x), len(y)

        # make the length the same
        if lenX > lenY:
            y = (lenX-lenY)*"0" + y
        if lenX < lenY:
            x = (lenY-lenX)*"0" + x

        assert(len(x)==len(y))

        # Start comparing each bit
        count = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                count += 1

        return count

# Runtime: 40 ms
# Memory Usage: 13.8 MB

# Solution 2
# Using XOR Bitwise operator. It sets each bit to 1 if only one of two bits is 1
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')
        
# Runtime: 32 ms
# Memory Usage: 13.7 MB
