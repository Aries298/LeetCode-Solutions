class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half = int(len(s)/2)
        str1, str2 = s[:half], s[half:]
        ctr1, ctr2 = 0, 0
        for vowel in 'aieouAIEOU':
            ctr1 += str1.count(vowel)
            ctr2 += str2.count(vowel)
        return ctr1 == ctr2