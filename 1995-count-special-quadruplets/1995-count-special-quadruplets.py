class Solution:
    def countQuadruplets(self, arr: List[int]) -> int:
        ans = 0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                for k in range(j+1, len(arr)):
                    for l in range(k+1, len(arr)):
                        if arr[i] + arr[j] + arr[k] == arr[l]:
                            ans += 1
        return ans