class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr = 0
        seen = set()
        while ptr < len(nums):
            if nums[ptr] in seen:
                nums.pop(ptr)
            else:
                seen.add(nums[ptr])
                ptr += 1