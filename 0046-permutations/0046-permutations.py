class Solution:
    def permute(self, nums):
        return map(list, itertools.permutations(nums))