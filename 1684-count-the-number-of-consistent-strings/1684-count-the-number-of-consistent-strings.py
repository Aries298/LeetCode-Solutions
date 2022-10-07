class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        for word in words:
            for letter in allowed:
                word = word.replace(letter,"")
            if not len(word):
                ans += 1
        return ans
            