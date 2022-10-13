class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = 0
        signum = -1 if(dividend > 0) ^ (divisor > 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                ans += i
                i <<= 1
                temp <<= 1
        return min(max(-2147483648, ans * signum), 2147483647)