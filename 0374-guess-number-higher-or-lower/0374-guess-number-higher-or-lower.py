# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    @cache
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while low <= high:
            g = (high + low) // 2
            res = guess(g)
            if res:
                if res == 1:
                    low = g +1
                else:
                    high = g - 1
            else:
                return int(g)
            
            
