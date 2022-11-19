from functools import reduce

class Solution:
    def outerTrees(self, trees):
        def check_clockwise(p1, p2, p3):
            return (p2[1] - p1[1]) * (p3[0] - p1[0]) > (p3[1] - p1[1]) * (p2[0] - p1[0])
        trees = sorted(trees)
        ans = []

        for t in trees:
            while len(ans) > 1 and check_clockwise(ans[-2],ans[-1],t):
                ans.pop()
            ans.append(t)

        if len(ans) == len(trees):
            return ans

        ans.pop()
        for t in reversed(trees):
            while len(ans) > 1 and check_clockwise(ans[-2],ans[-1],t):
                ans.pop()
            ans.append(t)

        ans.pop()
        return ans
