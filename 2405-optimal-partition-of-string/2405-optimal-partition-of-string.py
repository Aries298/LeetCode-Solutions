class Solution:
    def partitionString(self, s: str) -> int:
        subset, ans = set(), 1
        for c in s:
            if c in subset:
                ans +=1
                subset = {c}
            else: subset.add(c)
        return ans