class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        diff = (set(range(1,len(nums)+1))).difference(set(nums))
        if diff:
            return min(diff)
        else:
            return max(nums) + 1