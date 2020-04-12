# def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:

class Solution:
    def flipAndInvertImage(self, A):
        result_matrix =[]
        for row in A:
            row.reverse()
            result = map(lambda x: 1 if x==0 else 0, row)
            result_matrix.append(result)
    
        return result_matrix
        
'''
Runtime: 48 ms	
Memory: 13.9 MB
'''
