class Solution:
    def possibleBipartition(self, N, dislikes):
        d = defaultdict(set)
        for a,b in dislikes:
            d[a].add(b)
            d[b].add(a)
        group = {i:None for i in range(1, N+1)}
        
        def dfs(node, g):
            if not group[node]: group[node] = g
            else: return group[node] == g
            
            for peeps in d[node]:
                if not dfs(peeps, 2 if g == 1 else 1): return False
            return True
        
        for n in range(1,N+1):
            if not group[n] and not dfs(n,1): return False
        return True