class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        return "1"*(n1:=s.count('1')-1)+"0"*(len(s)-n1-1)+"1"