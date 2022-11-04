VOWELS = {'a','e','i','o','u','A','E','I','O','U'}
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_idx = []
        for i in range(len(s)):
            if s[i] in VOWELS:
                vowel_idx.append(i)
        s = list(s)
        for i in range(int(len(vowel_idx)//2)):
            s[vowel_idx[i]], s[vowel_idx[-i-1]] = s[vowel_idx[-i-1]], s[vowel_idx[i]]
        return ''.join(s)
     