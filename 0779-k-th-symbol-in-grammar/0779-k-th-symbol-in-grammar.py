class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        x = 2 ** (n - 2)
        if k > x:
            return 1 ^ self.kthGrammar(n - 1, k - x)
        return self.kthGrammar(n - 1, k)