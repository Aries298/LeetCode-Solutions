class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        s = sorted([point[0] for point in points])
        ans = 0
        for i in range(len(s)-1):
            ans = max(ans, s[i+1]-s[i])
        return ans