import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        maxHeap = []
        for val in piles: heapq.heappush(maxHeap, -val)
        while k > 0:
            tmp = heapq.heappop(maxHeap)//2
            heapq.heappush(maxHeap,tmp)
            k -= 1
        return -sum(maxHeap)