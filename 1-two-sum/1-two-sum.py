class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        if 2 > len(nums) or len(nums) > 10**4 or -10**9 > target or target > 10**9:
            return []
        for x in range(len(nums)):
            if target - nums[x] in nums and nums.index(target - nums[x]) != x:
                return [x, nums.index(target - nums[x])]
