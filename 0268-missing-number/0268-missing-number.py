class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        r = set(range(len(nums)+1))
        for num in r:
            if num not in nums:
                return num