class Solution:
    def rob(self, nums: List[int]) -> int:
        max3, max2, adj = 0, 0, 0
        for curr in nums:
            max3, max2, adj = max2, adj, max(max3 + curr, max2 + curr)
        return max(max2, adj)