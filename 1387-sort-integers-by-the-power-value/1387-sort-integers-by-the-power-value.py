class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def transform(x):
            ans = 0
            while x != 1:
                if not x%2: x /= 2
                else: x = 3*x+1
                ans += 1
            return ans
        
        return list(dict(sorted({num: transform(num) for num in range(lo, hi+1)}.items(), key=lambda item: item[1])).keys())[k-1]