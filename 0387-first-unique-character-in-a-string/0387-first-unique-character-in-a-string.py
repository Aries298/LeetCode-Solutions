class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = [x for x in Counter(s).most_common() if x[1] == 1]
        if ans:
            return s.index(ans[0][0])
        else:
            return -1