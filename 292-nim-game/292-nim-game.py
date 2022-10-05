class Solution:
    def canWinNim(self, n: int) -> bool:
        return n&(n&0b11)