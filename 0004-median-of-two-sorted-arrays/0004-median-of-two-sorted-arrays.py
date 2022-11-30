import numpy as np
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        (bigger, smaller) = (nums1, nums2) if len(nums1) > len(nums2) else (nums2, nums1)
        for num in smaller:
            bisect.insort(bigger, num)
        return np.median(bigger)