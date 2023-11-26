class Solution:
    def canMouseWin(self, grid: List[str], cj: int, mj: int) -> bool:

        def get_moves(m):
            """Builds a map of locations cat/mouse can move to from any given (i,j)."""
            moves = collections.defaultdict(set)
            for i in range(R):
                for j in range(C):
                    if grid[i][j] != '#':
                        v = {(i,j)}
                        for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                            for s in range(1, m+1):
                                r, c = i + s*dy, j + s*dx
                                if not (0 <= r < R and 0 <= c < C and grid[r][c] != '#'):
                                    break
                                v.add((r,c))
                        moves[(i,j)] = v
            return moves

        def get_locations():
            """Returns the starting locations of the Mouse, Cat, and Food."""
            start = dict()
            for (i, j) in mouse_moves:
                if grid[i][j] in ('M','C','F'):
                    start[grid[i][j]] = (i, j)
            return start['M'], start['C'], start['F']

        @functools.lru_cache(None)
        def helper(turn, cat, mouse):
            """Returns True if mouse wins and False if cat wins."""
            # cat's turn
            if turn & 1:
                if (turn == 1) or {food, mouse} & cat_moves[cat]:
                    return False
                return not any(not helper(turn-1, c, mouse) for c in cat_moves[cat])

            # mouse's turn
            if food in mouse_moves[mouse]:
                return True
            return any(helper(turn-1, cat, m) for m in mouse_moves[mouse])

        R, C = len(grid), len(grid[0])
        cat_moves = get_moves(cj)
        mouse_moves = get_moves(mj)
        mouse, cat, food = get_locations()

        return helper(2*R*C, cat, mouse)