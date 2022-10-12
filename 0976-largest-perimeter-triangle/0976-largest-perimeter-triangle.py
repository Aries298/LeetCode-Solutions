class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for i in range(len(nums)):
            biggest = nums[-i-1]
            for j in range(0, len(nums)-2-i):
                if nums[-j-i-2] + nums[-j-i-3] > biggest:
                    return nums[-j-i-2] + nums[-j-i-3] + biggest
        return 0
