class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans, length = 0, len(nums)
        dp = [defaultdict(int) for _ in range(length)]
        
        for i in range(length):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += (1 + dp[j][diff])
                ans += dp[j][diff]
        return ans
        