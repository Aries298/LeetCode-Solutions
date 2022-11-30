class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        numbers = list(set(nums))
        if len(numbers) < 2:
            return max(nums)
        numbers.remove(max(numbers))
        if len(numbers) < 2:
            return max(nums)
        numbers.remove(max(numbers))
        return max(numbers)