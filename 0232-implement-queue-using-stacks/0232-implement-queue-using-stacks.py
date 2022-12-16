class MyQueue:

    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()

    def push(self, x: int) -> None:
        self.s2.append(x)
        for num in self.s1:
            self.s2.append(num)
        self.s1, self.s2 = self.s2, deque()

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return not self.s1


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()