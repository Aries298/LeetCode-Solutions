class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def numberToBase(n, b):
            if n == 0:
                return [0]
            digits = []
            while n:
                digits.append(int(n % b))
                n //= b
            return digits[::-1]
        
        for b in range(2, n-1):
            num = ''.join([str(n) for n in numberToBase(n,b)])
            if num[:int(len(num) / 2)] != num[-int(len(num) / 2):][::-1]:
                return False
        return True