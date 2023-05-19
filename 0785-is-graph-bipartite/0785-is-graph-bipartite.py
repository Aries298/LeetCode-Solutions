class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0] * n

        for i in range(n):
            if colors[i] != 0:
                continue

            q = collections.deque([i])
            colors[i] = 1

            while q:
                curr = q.popleft()
                for neighbor in graph[curr]:
                    if colors[neighbor] == 0:
                        colors[neighbor] = -colors[curr]
                        q.append(neighbor)
                    elif colors[neighbor] == colors[curr]:
                        return False

        return True