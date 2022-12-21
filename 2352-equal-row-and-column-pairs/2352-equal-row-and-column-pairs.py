class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = [row for row in grid]
        cols = [[row[i] for row in rows] for i in range(len(rows))]
        intersection = set()
        for i, row in enumerate(rows):
            for j, col in enumerate(cols):
                if row == col: intersection.add((i,j))
        return len(intersection)

