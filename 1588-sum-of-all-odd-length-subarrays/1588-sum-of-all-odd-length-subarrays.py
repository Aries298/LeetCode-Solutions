class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        for i in range(1, len(arr) + 1):
            if i % 2 == 0:
                continue
            else:
                for j in range(len(arr) - i + 1):
                    ans += sum(arr[j:j + i])
        return ans