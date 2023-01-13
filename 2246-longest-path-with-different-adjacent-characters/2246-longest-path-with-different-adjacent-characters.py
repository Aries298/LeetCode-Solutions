class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        children = [[] for _ in range(len(s))]
        for i, j in enumerate(parent):
            if j >= 0: children[j].append(i)
        ans = [0]
        
        def dfs(i):
            tmp = [0]
            for j in children[i]:
                curr = dfs(j)
                if s[i] != s[j]:
                    tmp.append(curr)
            tmp = nlargest(2, tmp)
            ans[0] = max(ans[0], sum(tmp) + 1)
            return max(tmp) + 1
        
        dfs(0)
        return ans[0]