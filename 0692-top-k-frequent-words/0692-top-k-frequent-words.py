class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return [x[0] for x in Counter(sorted(words)).most_common(k)]