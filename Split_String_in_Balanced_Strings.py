# Solution 1
def balancedStringSplit(s):
    count = 0
    record = {}
    for x in s:
        if x not in record:
            record.update({x:1})
        else:
            record[x] += 1
        
        # check if R and L has the same value
        # skip if their is only one char in the record
        if len(record) == 1:
            continue
        if record['R'] == record['L']:
            count += 1
            record = {}
            
    return count


# Runtime: 36 ms
# Memory: 13.8 MB

# Solution 2
def balancedStringSplit(s):
    substr, l_count, r_count = 0, 0, 0
    for x in s:
        if x=='L':
            l_count += 1
        else:
            r_count += 1

        if l_count==r_count:
            substr += 1
    return substr
    
# Runtime: 36 ms
# Memory: 13.8 MB
