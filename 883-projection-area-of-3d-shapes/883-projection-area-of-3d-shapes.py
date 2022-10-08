class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        top = sum([1 if val else 0 for val in sum(grid,[])])
        side1 = sum([max(val) for val in grid])
        side2 = 0
        for j in range(len(grid)):
            side2 += max([i[j] for i in grid])
        return top + side1 + side2