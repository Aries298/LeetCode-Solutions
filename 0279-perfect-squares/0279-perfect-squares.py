class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        for i in range(len(dp)):
            if int(i**0.5) == i**0.5:
                dp[i] = 1
            else:
                for j in range(int(i**0.5)+1):
                    dp[i] = min(dp[i],dp[i-j*j]+1)
        return dp[n]