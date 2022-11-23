class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Squares
        for i in range(3):
            for j in range(3):
                nums = []
                for n in range(3):
                    for m in range(3):
                        nums.append(board[(i*3)+n][(j*3)+m])
                while "." in nums:
                    nums.remove(".")
                if len(nums) != len(set(nums)):
                    return False
        # Vertical
        for i in range(9):
            nums = []
            for j in range(9):
                nums.append(board[i][j])
            while "." in nums:
                nums.remove(".")
            if len(nums) != len(set(nums)):
                return False

        # Horizontal
        for i in range(9):
            nums = []
            for j in range(9):
                nums.append(board[j][i])
            while "." in nums:
                nums.remove(".")
            if len(nums) != len(set(nums)):
                return False

        return True