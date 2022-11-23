class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = [len(nums) == len(set(nums)) for nums in [[board[(i*3)+n][(j*3)+m] for n in range(3) for m in range(3) if board[(i*3)+n][(j*3)+m] != "."] for j in range(3) for i in range(3)]]
        vertical = [len(nums) == len(set(nums)) for nums in [[board[j][i] for j in range(9) if board[j][i] != "."] for i in range(9)]]
        horizontal = [len(nums) == len(set(nums)) for nums in [[el for el in board[i] if el != "."] for i in range(9)]]
        return False not in squares + vertical + horizontal