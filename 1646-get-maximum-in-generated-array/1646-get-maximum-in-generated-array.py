class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        arr = [0] * (n+1)
        arr[1] = 1
        for i in range(2, n+1):
            if not i % 2:
                arr[i] = arr[int(i/2)]
            else:
                arr[i] = arr[int(i/2)] + arr[int(i/2)+1]
        return max(arr)