class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        order = [word[-1] for word in s]
        words = [word[:-1] for word in s]
        #print(order)
        #print(words)
        d = dict(zip(order, words))
        d = dict(sorted(d.items()))

        return ' '.join(d.values())