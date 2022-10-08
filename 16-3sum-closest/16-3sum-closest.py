class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_sum = 2**31
        nums.sort()
        for i in range(len(nums)):
            j, k = i + 1, len(nums)-1
            while j<k:
                curr_sum = nums[i] + nums[j] + nums[k]
                if curr_sum == target:
                    return curr_sum
                if abs(curr_sum-target) < abs(closest_sum-target):
                    closest_sum = curr_sum
                if curr_sum < target:
                    j += 1
                else:
                    k -= 1
        return closest_sum