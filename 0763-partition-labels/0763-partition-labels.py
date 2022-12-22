class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans, max_last_seen, count = [], 0, 0
        last_seen = {char : i for i, char in enumerate(s)}
        for i, char in enumerate(s):
            max_last_seen = max(last_seen[char],max_last_seen)
            count += 1
            if i == max_last_seen:
                ans.append(count)
                count = 0
        return ans
            