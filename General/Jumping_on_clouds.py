# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def jumpingOnClouds(c):
    current = 0
    endIndex = len(c)-1
    jumps = 0

    while current != endIndex:
        try:
            if c[current+2]==0:
                current+=2
            else:
                current+=1

            jumps+=1

        except:
            current+=1
            jumps+=1
    
    return jumps


c1 = [0, 0, 1, 0, 0, 1, 0]
c2 = [0, 0, 0, 1, 0, 0]

testC1 = jumpingOnClouds(c1)
testC2 = jumpingOnClouds(c2)
print(testC1, testC2)   # 4 3