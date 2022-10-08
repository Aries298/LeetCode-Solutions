class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if not num:
            return True
        return str(num) == (str(num)[::-1].lstrip('0'))[::-1]