class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        ans = 0
        for word in strs:
            if word.isnumeric(): ans = max(int(word),ans)
            else: ans = max(len(word), ans)
        return ans