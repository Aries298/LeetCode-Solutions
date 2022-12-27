class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles)
        print(piles)
        ans = 0
        while piles:
            piles.pop()
            ans += piles.pop()
            piles.pop(0)
        return ans