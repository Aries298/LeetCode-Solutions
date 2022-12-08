class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        ptr = 0
        counter = 0
        while nums and ptr < len(nums):
            while nums and ptr < len(nums) and nums.count(nums[ptr]) > 1:
                    val = nums[ptr]
                    nums.remove(val)
                    nums.remove(val)
                    counter += 1
            ptr += 1
        return [counter, len(nums)]