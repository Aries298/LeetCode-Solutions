class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        def dfs(node, end, seen):
            if node == end: return True
            if node in seen: return False
            seen.add(node)
            for n in graph[node]:
                if dfs(n, end, seen): return True
            return False
        
        seen = set()
        return dfs(source, destination, seen)