class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        c = Counter(tasks)
        ans = 0
        for i in c:
            if c[i]==1: return -1
            x = c[i]//3
            y = c[i]%3
            if not y: ans += x
            else: ans += (x+1)
        return ans