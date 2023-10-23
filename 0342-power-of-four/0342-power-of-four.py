class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        y=n
        j=0
        z=1
        while z > 0:
            z=int(n/4)
            n=z
            j+=1
        j-=1
        x = 4**j
        if x==y:
            return True