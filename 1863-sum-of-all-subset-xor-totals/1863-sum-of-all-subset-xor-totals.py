class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        combs = []
        for L in range(1, len(nums) + 1):
            for subset in itertools.combinations(nums, L):
                combs.append(subset)
        ans = 0
        for comb in combs:
            tmp = comb[0]
            for i in range(1,len(comb)):
                tmp ^= comb[i]
            ans += tmp
        return ans