class Solution:
    def maxSatisfaction(self, A):
        ans = total = 0
        A.sort()
        while A and A[-1] + total > 0:
            total += A.pop()
            ans += total
        return ans