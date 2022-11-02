class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def check_neighbour(a, b):
            return sum([1 for i in range(len(a)) if a[i]!=b[i]]) == 1
        q = deque([start])
        visited = set()
        ans = 0
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == end:
                    return ans
                if curr not in visited:
                    visited.add(curr)
                    for x in bank:
                        if check_neighbour(curr, x):
                            q.append(x)
            ans += 1
        return -1