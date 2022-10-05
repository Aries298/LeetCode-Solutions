class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) != 1:
            num = sum([int(num) for num in str(num)])
        return int(num)