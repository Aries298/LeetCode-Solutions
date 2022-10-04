class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        x = 2**32
        for i in range(32,0,-1):
            ans += (n&x)>>i
            x=x>>1
        ans += 1&n
        return ans