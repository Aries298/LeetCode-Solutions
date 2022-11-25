from itertools import combinations
class Solution:
    def sumSubarrayMins(self, nums: List[int]) -> int:
        #return sum([min(arr[i:i+j+1]) for i in range(0,len(arr)) for j in range(len(arr)-i)])
        modulo = (10 ** 9 + 7)
        ans = 0
        stack = []
        n = len(nums)
        nums.append(0)
        for i, num in enumerate(nums):
            while stack and (i == n or num < nums[stack[-1]]):
                top = stack.pop()
                starts = top - stack[-1] if stack else top + 1
                ends = i - top
                ans += starts * ends * nums[top]
                ans %= modulo
            stack.append(i)
        return ans