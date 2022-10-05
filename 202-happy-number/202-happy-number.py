class Solution:
    def isHappy(self, n: int) -> bool:
        for _ in range(100):
            n = sum([int(n)**2 for n in str(n)])
            if n == 1:
                return True
        return False