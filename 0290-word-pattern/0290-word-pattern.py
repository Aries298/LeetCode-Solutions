class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern = list(pattern)
        s = s.split()
        d = dict()
        if len(pattern) != len(s): return False
        for letter, word in zip(pattern, s):
            try:
                if d[letter] != word: return False
            except:
                if word in d.values(): return False
                d[letter] = word
        return True