class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROW ,COL = len(grid),len(grid[0])
        def dfs(r,c):
            if r < 0 or c < 0 or r == ROW or c == COL or not grid[r][c] or (r,c) in visit:
                return 0
            visit.add((r,c))
            res = 1
            direct = [[0,1],[0,-1],[1,0],[-1,0]]
            for dr , dc in direct:
                res += dfs(r+dr ,c + dc)
            return res

        

        visit = set()
        land, borderLand = 0 ,0
        for r in range(ROW):
            for c in range(COL):
                land += grid[r][c]
                if (grid[r][c] and (r,c) not in visit and (c in [0 , COL -1] or r in [0,ROW-1])):
                    borderLand += dfs(r,c)
        return land - borderLand