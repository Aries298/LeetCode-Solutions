class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {0: -1}
        nsum = 0
        for i, n in enumerate(nums):
            nsum = (nsum + n) % k
            if nsum in dic:
                if i - dic[nsum] >= 2:
                    return True
            else:
                dic[nsum] = i
        return False