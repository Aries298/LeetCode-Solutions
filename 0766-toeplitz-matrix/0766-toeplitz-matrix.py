import numpy as np
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        a = np.array(matrix)
        for i in range(-a.shape[0]+1,a.shape[1]):
            if len(set(np.diag(a,i))) > 1:
                return False
        return True
