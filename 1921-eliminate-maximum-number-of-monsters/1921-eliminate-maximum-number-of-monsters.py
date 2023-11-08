class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n=len(dist)
        monsters_t=[0]*(n+1)

        for i in range(n):
            # the following is ceil function
            t=(dist[i]+speed[i]-1)//speed[i] 
            if t>n: 
                t=n
            monsters_t[t]+=1
        
        shot=1
        monsters=0
        while shot<=n:
            monsters+=monsters_t[shot-1]
            if shot<=monsters: 
                break
            shot+=1
        shot-=1
        return shot