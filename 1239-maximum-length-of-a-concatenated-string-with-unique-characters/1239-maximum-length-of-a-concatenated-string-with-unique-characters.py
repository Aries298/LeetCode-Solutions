import itertools

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        combs = []
        for L in range(len(arr) + 1):
            for subset in itertools.combinations(arr, L):
                combs.append(subset)

        ans = 0
        for comb in combs:
            tmp = ""
            for el in comb:
                tmp += el
            if len(tmp) == len(set(tmp)):
                ans = len(tmp) if ans < len(tmp) else ans
                
        return ans
        
       