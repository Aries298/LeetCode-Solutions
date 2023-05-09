class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        range_mat = (len(matrix)//2) + 1
        size = len(matrix) * len(matrix[0])
        out = []
        
        for x in range(range_mat):
            
			# left to right  ->
            if len(out)<size:
                out += matrix[x][x:len(matrix[0])-x]
            
			# up tp down ⬇
            if len(out)<size:
                for idx in range(x+1,len(matrix)-x):
                    out.append(matrix[idx][-1-x])
            
			# right to left <-
            if len(out)<size:
                out += matrix[-1-x][::-1][x+1:len(matrix[0])-x]
            
			# down to up  
            if len(out)<size:
                rev_mat = matrix[::-1]

                for idx in range(x+1, len(matrix)-(x+1)):
                    out.append(rev_mat[idx][x])
        
        return out