class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        maxSum = sum([max(0, num) for num in nums])
        absNums = sorted([abs(num) for num in nums])
        maxHeap = [(-maxSum + absNums[0], 0)]
        ans = [maxSum]
        while len(ans) < k:
            nextSum, i = heapq.heappop(maxHeap)
            heapq.heappush(ans, -nextSum)
            if i + 1 < len(absNums):
                heapq.heappush(maxHeap, (nextSum - absNums[i] + absNums[i + 1], i + 1))
                heapq.heappush(maxHeap, (nextSum + absNums[i + 1], i + 1))
        return ans[0]