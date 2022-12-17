class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.operators = {
            "+" : lambda y, x: x + y,
            "-" : lambda y, x: x - y,
            "*" : lambda y, x: x * y,
            "/" : lambda y, x: int(x / y)   
        }
        
        if not tokens: return 0
        stack = []
        for token in tokens:
            if token in self.operators:
                stack.append(self.operators[token](stack.pop(), stack.pop()))
            else:
                stack.append(int(token))
        return stack[0]