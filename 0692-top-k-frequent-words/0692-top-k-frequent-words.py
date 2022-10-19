from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = sorted(words)
        c = Counter(c)
        c = c.most_common(k)
        c = [x[0] for x in c]
        return c