class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        ans = 0
        while nums:
            n1, n2 = nums.pop(), nums.pop()
            ans += min(n1, n2)
        return ans