import bisect
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try: return nums.index(target)
        except: return bisect.bisect_left(nums, target)