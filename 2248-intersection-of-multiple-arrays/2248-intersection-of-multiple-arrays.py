class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ans = set(nums[0])
        for i in range(1,len(nums)):
            ans = ans.intersection(set(nums[i]))
        return sorted(ans)