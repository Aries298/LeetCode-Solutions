class Solution:
    def minimumReplacement(self, A):
        x = A[-1]
        res = 0
        for a in reversed(A):
            k = (a + x - 1) // x
            x = a // k
            res += k - 1
        return res