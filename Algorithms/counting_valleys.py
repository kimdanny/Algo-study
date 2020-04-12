"""
HackerRank.
Given Gary's sequence of up and down steps during his last hike, find and print the number of valleys he walked through.
For example, if Gary's path is [DDUUUUDD], he first enters a valley 2 units deep. 
Then he climbs out an up onto a mountain 2 units high. Finally, he returns to sea level and ends his hike.
"""
def countingValleys(n, s):
    numOfValleys = 0
    level = 0
    valStart = True

    for x in s:
        if x=='U':
            level+=1
            if level<0 and valStart:
                numOfValleys+=1
                valStart = False
            if level >= 0:
                valStart = True
        else:
            level -= 1
            if level<0 and valStart:
                numOfValleys+=1
                valStart = False
            if level >= 0:
                valStart = True

    return numOfValleys
