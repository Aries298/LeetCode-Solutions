class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total_steps = len(cost)
        @cache
        def step(i):
            if total_steps <= i:
                return 0
            return cost[i] + min(step(i+1), step(i+2))
        return min(step(0), step(1))