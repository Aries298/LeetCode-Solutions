from copy import copy
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        tmp = copy(s)
        for i in range(len(s)):
            s[i] = tmp[-i-1]