class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d = {}
        for letter in s:
            try:
                d[letter]
                return letter
            except:
                d[letter] = 1