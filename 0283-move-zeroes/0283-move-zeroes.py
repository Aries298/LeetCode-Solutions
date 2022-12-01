class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros, non_zeros = [], []
        for num in nums:
            if num:
                non_zeros.append(num)
            else:
                zeros.append(num)
                
        merged = non_zeros + zeros
        for i in range(len(nums)):
            nums[i] = merged[i]