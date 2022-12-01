class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return next(iter((set(range(len(nums)+1))).difference(set(nums))))