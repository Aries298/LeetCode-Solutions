class Solution:
    def frequencySort(self, s: str) -> str:
        ans = []
        c = Counter(s).most_common()
        for pair in c:
            for i in range(pair[1]):
                ans.append(pair[0])
        return ans