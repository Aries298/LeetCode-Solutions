class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        for s in str(bin(n)):
            if s == '1':
                ans+=1
        return ans