class Solution:
    def findMaxLength(self, nums):
        hashmap = {0: -1}
        zeros, ones, max_len = 0, 0, 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            else:
                ones += 1
            
            diff = zeros - ones
            if diff in hashmap:
                max_len = max(max_len, i - hashmap[diff])
            else:
                hashmap[diff] = i
        
        return max_len