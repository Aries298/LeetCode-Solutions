class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = sorted(costs)
        ans = 0
        while coins > 0:
            if costs and costs[0] <= coins:
                coins -= costs[0]
                costs.pop(0)
                ans += 1
            else:
                break
        return ans
                          