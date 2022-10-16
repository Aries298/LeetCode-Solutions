class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        @cache
        def helper(intended, end):
            if intended == 1:
                 return max(jobDifficulty[:end])
            res, mx = math.inf, 0
            for done in range(1, end-intended+2):
                mx = max(mx, jobDifficulty[end-done])
                res = min(helper(intended-1, end-done) + mx, res)
            return res
        return helper(d, len(jobDifficulty)) if len(jobDifficulty) >= d else -1
        
    