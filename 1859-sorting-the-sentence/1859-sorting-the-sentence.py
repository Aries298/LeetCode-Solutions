class Solution:
    def sortSentence(self, s: str) -> str:
        return ' '.join(dict(sorted((dict(zip([word[-1] for word in s.split()], [word[:-1] for word in s.split()]))).items())).values())