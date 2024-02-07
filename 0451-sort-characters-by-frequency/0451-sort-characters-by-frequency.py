class Solution:
    def frequencySort(self, s: str) -> str:
        return [pair[0] for pair in Counter(s).most_common() for i in range(pair[1])]