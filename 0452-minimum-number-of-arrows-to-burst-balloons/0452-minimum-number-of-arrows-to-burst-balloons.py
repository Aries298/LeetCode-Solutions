class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[1])
        ans, bow = 1, points[0][1]
        for start, end in points:
            if bow < start:
                bow = end
                ans += 1
        return ans