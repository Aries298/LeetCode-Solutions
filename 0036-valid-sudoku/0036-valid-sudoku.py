class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grids = [[set() for _ in range(3)] for _ in range(3)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rows[i]:
                    return False
                if board[i][j] in cols[j]:
                    return False
                if board[i][j] in grids[i//3][j//3]:
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                grids[i//3][j//3].add(board[i][j])
        return True
        
        
        # return not sum([len(nums) != len(set(nums)) for nums in [[board[(i*3)+n][(j*3)+m] for n in range(3) for m in range(3) if board[(i*3)+n][(j*3)+m] != "."] for j in range(3) for i in range(3)]] + [len(nums) != len(set(nums)) for nums in [[board[j][i] for j in range(9) if board[j][i] != "."] for i in range(9)]] + [len(nums) != len(set(nums)) for nums in [[el for el in board[i] if el != "."] for i in range(9)]])
