class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        row=len(mat)
        col=len(mat[0])
        s=0
        for x in range(row):
            for y in range(col):
                if x==y or x==col-y-1 or y==row-x-1:
                    s+=mat[x][y]
        return s   