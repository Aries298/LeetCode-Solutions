class Solution:
    def balancedStringSplit(self, s: str) -> int:
        pref = ans = 0
        for char in s:
            pref += 1 if char == "R" else -1
            if not pref: ans += 1
        return ans
