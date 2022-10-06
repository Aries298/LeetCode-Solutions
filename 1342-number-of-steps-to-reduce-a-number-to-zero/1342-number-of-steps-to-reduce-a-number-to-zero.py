class Solution:
    def numberOfSteps(self, num: int) -> int:
        ans = 0
        while num:
            num -= 1 if num & 1 else num >> 1
            ans += 1
        return ans