class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        stones = list(stones)
        jewels = set(jewels)
        for stone in stones:
            if stone in jewels:
                ans+=1
        return ans