class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(curr, path):
            if curr == len(graph) - 1: ans.append(path)
            else:
                for i in graph[curr]: dfs(i, path + [i])
        ans = []
        dfs(0, [0])
        return ans
                    
            