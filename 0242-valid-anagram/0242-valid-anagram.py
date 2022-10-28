class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = set()
        for letter in s:
            if letter not in seen:
                seen.add(letter)
                if s.count(letter) != t.count(letter):
                    return False
        return True