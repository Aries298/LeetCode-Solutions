class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ans = set()
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i == j: continue
                if nums[i]==nums[j] and not (i*j)%k:
                    ans.add((i,j))
        return (len(ans))