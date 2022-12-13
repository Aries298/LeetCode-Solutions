class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        path = [[0 for x in range(n)] for y in range(n)]
        
        # initial state
        path[0] = matrix[0]
        
        for i in range(1, n):
            for j in range(n):
                if 0 < j < n -1:
                    path[i][j] = min(path[i-1][j-1], path[i-1][j], path[i-1][j+1]) + matrix[i][j]
                elif j == 0:
                    path[i][j] = min(path[i-1][j], path[i-1][j+1]) + matrix[i][j]
                else:
                    path[i][j] = min(path[i-1][j-1], path[i-1][j]) + matrix[i][j]
                    
        return min(path[-1])