class Solution:
    def mySqrt(self, x: int) -> int:
        lo = min(1,x)
        hi = max(1,x)
        mid = 0
        while(100*lo*lo<x):
            lo*=10
        while(0.01*hi*hi>x):
            hi*=0.1
        for _ in range(100):
            mid = (lo+hi)/2
            if(mid*mid==x):
                return int(mid)
            if(mid*mid>x):
                hi=mid
            else:
                lo=mid
        return int(mid)