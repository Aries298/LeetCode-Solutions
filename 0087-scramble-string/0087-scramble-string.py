class Solution:
    def isScramble(self,s1: str, s2: str) -> bool:
        n = len(s1)
        if n != len(s2):
            return False
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        dp = [[[None] * n for _ in range(n)] for _ in range(n+1)]
    
        def solve(l, i, j):
            if dp[l][i][j] is not None:
                return dp[l][i][j]
            if s1[i:i+l] == s2[j:j+l]:
                dp[l][i][j] = True
                return True
            if sorted(s1[i:i+l]) != sorted(s2[j:j+l]):
                dp[l][i][j] = False
                return False
            for k in range(1, l):
                if (solve(k, i, j) and solve(l-k, i+k, j+k)) or (solve(k, i, j+l-k) and solve(l-k, i+k, j)):
                    dp[l][i][j] = True
                    return True
                dp[l][i][j] = False
            return False
        
        return solve(n, 0, 0)