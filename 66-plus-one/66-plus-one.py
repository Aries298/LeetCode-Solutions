class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = map(str, digits)
        s = int(''.join(s))
        s += 1
        s = [num for num in str(s)]
        return s