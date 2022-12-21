class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cols = []
        rows = [row for row in grid]
        for i in range(len(rows)): cols.append([row[i] for row in rows])

        intersection = set()

        for i, row in enumerate(rows):
            for j, col in enumerate(cols):
                if row == col:
                    intersection.add((i,j))
        return len(intersection)

