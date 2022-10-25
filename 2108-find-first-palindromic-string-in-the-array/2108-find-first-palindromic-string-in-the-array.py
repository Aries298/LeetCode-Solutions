class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindrome(s):
            if len(s) < 2:
                return True
            return s[0:int(len(s)/2)] == s[-int(len(s)//2):][::-1]
        for word in words:
            if isPalindrome(word):
                return word
        return ""