import bisect
class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.nums, num)
        
    def findMedian(self) -> float:
        size = len(self.nums)
        half = size >> 1

        if size & 1:
            return self.nums[half]
        else:
            return (self.nums[half-1]+self.nums[half])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()