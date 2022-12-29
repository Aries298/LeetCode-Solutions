class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        return max(1, -(min(itertools.accumulate(nums)))+1)