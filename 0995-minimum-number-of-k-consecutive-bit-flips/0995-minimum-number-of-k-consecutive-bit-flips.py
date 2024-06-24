from collections import deque
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        periods = deque()
        total_flips: int = 0
        for idx in range(len(nums)):
            while periods and idx > periods[0]:
                periods.popleft()
            nums[idx] = [nums[idx], int(not nums[idx])][len(periods) % 2]
            if nums[idx] == 0 and idx < len(nums) - k + 1:
                total_flips += 1
                nums[idx] = 1
                periods.append(idx + k - 1)
            elif nums[idx] == 0:
                return -1
        return total_flips