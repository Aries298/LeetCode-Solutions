class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_time = 0
        colors = list(colors)
        if len(colors) == 1:
            return 0
        for i in range(1, len(colors)):
            if colors[i] == colors[i-1]:
                total_time += min(neededTime[i],neededTime[i-1])
                neededTime[i] = max(neededTime[i], neededTime[i-1])
        return total_time
