class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        curr = nums[0]
        for i in range(0,len(nums)-1):
            if nums[i] >= nums[i+1]:
                ans += nums[i] - nums[i+1] + 1
                nums[i+1] = nums[i] + 1
        return ans