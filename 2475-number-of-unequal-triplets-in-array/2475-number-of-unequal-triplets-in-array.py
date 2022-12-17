class Solution:
    def unequalTriplets(self, arr: List[int]) -> int:
        ans = 0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                for k in range(j+1, len(arr)):
                    if arr[i] != arr[j] and arr[i] != arr[k] and arr[j] != arr[k]:
                        ans += 1
        return ans