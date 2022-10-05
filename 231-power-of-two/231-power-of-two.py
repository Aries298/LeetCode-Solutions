class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        else:
            return bin(n)[2:].count('1') == 1 and n > 0