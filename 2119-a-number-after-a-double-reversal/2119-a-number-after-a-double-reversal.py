class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return str(num) == (str(num)[::-1].lstrip('0'))[::-1] or num == 0