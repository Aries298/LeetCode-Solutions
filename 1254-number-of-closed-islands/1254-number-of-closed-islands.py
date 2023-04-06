class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def is_closed(pos):
            if grid[pos[0]][pos[1]]:
                return 0
            stack = [pos]
            is_closed_state = 1
            while stack:
                i, j = stack.pop()
                grid[i][j] = 1
                for x, y in dirs:
                    nx, ny = i + x, j + y
                    if not (-1 < nx < m and -1 < ny < n):
                        is_closed_state = 0
                        continue
                    if grid[nx][ny]:
                        continue
                    stack.append((nx, ny))
            return is_closed_state
        
        count = 0
        m, n = len(grid), len(grid[0])
        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
        return sum(map(is_closed, product(range(m), range(n))))
