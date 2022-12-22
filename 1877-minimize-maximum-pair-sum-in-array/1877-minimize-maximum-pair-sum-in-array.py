class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        ans = 0
        first, second = nums[:int(len(nums)/2)], nums[int(len(nums)/2):][::-1]
        return max([a+b for a,b in zip(first,second)])