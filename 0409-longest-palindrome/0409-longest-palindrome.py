class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        c = Counter(s)
        for val in c.values():
            ans += int(val / 2)
        for val in c.values():
            if val % 2 == 1:
                return 2 * ans + 1
        return 2 * ans