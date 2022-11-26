class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = sorted(list(zip(startTime,endTime,profit)))
        startTime.sort()
        @cache
        def helper(i):
            if i == n: return 0
            next_job = bisect_left(startTime,jobs[i][1])
            while next_job<n and jobs[i][1]>jobs[next_job][0]: next_job += 1
            return max(jobs[i][2]+helper(next_job), helper(i+1))
        return helper(0)