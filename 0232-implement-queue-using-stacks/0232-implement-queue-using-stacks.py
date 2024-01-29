class MyQueue:
    def __init__(self):
        # Enqueue stack
        self.in_stack = []
        # Dequeue stack
        self.out_stack = []

    def push(self, x):
        # Enqueue operation
        self.in_stack.append(x)

    def pop(self):
        if not self.out_stack:
            # Transfer from enqueue stack to dequeue stack
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        # Dequeue operation
        return self.out_stack.pop()

    def peek(self):
        if not self.out_stack:
            # Transfer from enqueue stack to dequeue stack
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        # Peek operation
        return self.out_stack[-1]

    def empty(self):
        # Check if both stacks are empty
        return not self.in_stack and not self.out_stack
