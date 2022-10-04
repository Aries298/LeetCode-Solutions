class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        for i in range(33):
            ans += ((2**i)&n)>>i
        return ans