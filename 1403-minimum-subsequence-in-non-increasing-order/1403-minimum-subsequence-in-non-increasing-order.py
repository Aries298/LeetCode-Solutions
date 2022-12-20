class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        ans, nums = [], sorted(nums)
        while sum(ans) <= sum(nums): ans.append(nums.pop())
        return ans