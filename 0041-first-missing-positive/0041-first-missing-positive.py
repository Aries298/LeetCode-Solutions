class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        maximum = max(nums)
        diff = (set(range(1,len(nums)+1))).difference(set(nums))
        if diff:
            return min(diff)
        else:
            return maximum + 1
        