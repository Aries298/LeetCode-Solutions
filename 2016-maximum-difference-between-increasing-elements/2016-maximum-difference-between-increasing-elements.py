class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = -1
        for i, num in enumerate(nums[:-1]):
            max_diff = max(max_diff, max(nums[i+1:])-nums[i])
        return max_diff if max_diff > 0 else -1