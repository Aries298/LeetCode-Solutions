class Solution:
    def restoreString(self, s: str, indices) -> str:
        ans = [""] * len(indices)
        s = list(s)
        for i in range(len(s)):
            ans[indices[i]] = s[i]
        return ''.join(ans)