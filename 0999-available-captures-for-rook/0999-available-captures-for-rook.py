class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        n = 8
        for i in range(n):
            for j in range(n):
                if board[i][j] == 'R':
                    x, y = i, j
                    break
        
        ans = 0
        for i in range(x-1, -1, -1):
            if board[i][y] == 'p':
                ans += 1
                break
            if board[i][y] == 'B': break

        for i in range(x+1, n):
            if board[i][y] == 'p':
                ans += 1
                break
            if board[i][y] == 'B': break

        for j in range(y-1, -1, -1):
            if board[x][j] == 'p':
                ans += 1
                break
            if board[x][j] == 'B': break

        for j in range(y+1, n):
            if board[x][j] == 'p':
                ans += 1
                break
            if board[x][j] == 'B': break
                
        return ans