class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
            
        zeros = [n for n in nums if not n]
        non_zeros = [n for n in nums if n]
        return non_zeros + zeros