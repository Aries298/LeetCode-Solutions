class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans=0
        mod=10**9+7
        for index,x in enumerate(nums):
            n=bisect.bisect_right(nums,target-x)-1
            if n-index-1>=0:
                ans+=pow(2,n-index,mod)-1
            if x*2<=target:
                ans+=1
            ans%=mod
        return ans%mod            