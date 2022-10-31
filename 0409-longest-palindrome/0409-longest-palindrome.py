class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        ans = 0
        for letter in c:
            while c[letter] > 1:
                c[letter] -= 2
                ans += 2
        return ans+1 if 1 in c.values() else ans