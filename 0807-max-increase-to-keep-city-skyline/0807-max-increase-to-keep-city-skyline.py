import numpy as np
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row, col = list(map(max, grid)), list(map(max, zip(*grid)))
        return sum([min(i,j) for i in row for j in col]) - sum(map(sum,grid))