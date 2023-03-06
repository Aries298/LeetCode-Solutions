class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        return sorted(list((set([num for num in range(1, max(arr) + 1 + k) if num > 0])).difference(set(arr))))[k - 1]