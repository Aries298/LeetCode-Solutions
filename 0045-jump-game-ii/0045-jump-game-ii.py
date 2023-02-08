class Solution:
    def jump(self, nums: List[int]) -> int:
        memo={}
        def min_jumps(index):
            if index>=len(nums)-1:
                return 0
            if index in memo:
                return memo[index]
            ans=float('inf')
            for i in range(index,index+nums[index]):
                ans=min(ans,1+min_jumps(i+1))
            memo[index]=ans
            return ans
        return min_jumps(0)