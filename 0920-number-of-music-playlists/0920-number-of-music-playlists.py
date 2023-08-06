class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        @cache
        def fn(i, x): 
            if i == goal: return x == n 
            ans = 0 
            if x < n: ans += (n-x) * fn(i+1, x+1) # a new song
            if k < x: ans += (x-k) * fn(i+1, x) # an old song
            return ans % 1_000_000_007
        
        return fn(0, 0)