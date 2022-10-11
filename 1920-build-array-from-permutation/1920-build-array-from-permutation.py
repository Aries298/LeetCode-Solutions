class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for index in nums:
            ans.append(nums[index])
        return ans