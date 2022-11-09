class StockSpanner:

    def __init__(self):
        self.stocks = deque()

    def next(self, price: int) -> int:
        res = 1
        if len(self.stocks) < 1:
            res = 1
        else:
            while self.stocks and self.stocks[-1][0] <= price:
                res += self.stocks.pop()[1]
        self.stocks.append((price, res))
        return res
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)