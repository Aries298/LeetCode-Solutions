class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        nhold, nhold_cooldown, hold = 0, -2**10, -2**10
        for price in prices:
            hold, nhold, nhold_cooldown = max(hold, nhold - price), max(nhold, nhold_cooldown), hold + price
        return max(nhold, nhold_cooldown)