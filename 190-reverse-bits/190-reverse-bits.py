class Solution:
    def reverseBits(self, n: int) -> int:
        n = (str(bin(n)))[2:]
        while len(n) != 32:
            n='0'+n
        return int(n[::-1],2)