class Solution():
    def calculate(self, s):
        res, num, sign, stack = 0, 0, 1, []
        for ss in s:
            if ss.isdigit():
                num = 10*num + int(ss)
            elif ss in ["-", "+"]:
                res += sign*num
                num = 0
                sign = [-1, 1][ss=="+"]
            elif ss == "(":
                stack.append(res)
                stack.append(sign)
                sign, res = 1, 0
            elif ss == ")":
                res += sign*num
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res + num*sign


'''
from collections import deque
class Solution:
    def calculate(self, s: str) -> int:
        def calc_expr(expr):
            ans = 0
            expr = expr[1:-1]
            if expr[0] == '-':
                expr = ['0'] + expr
            while len(expr) > 1:
                expr = [str(int(expr[0]) + int(expr[2]))] + expr[3:] if expr[1] == "+" else [str(int(expr[0]) - int(expr[2]))] + expr[3:]
            return expr[0]

        DELIMS = ('+', '-', '(', ')')
        curr = ''
        parsed = deque()
        s = s.replace(" ", "")
        for l in s:
            if l in DELIMS:
                parsed.append(curr)
                parsed.append(l)
                curr = ''
            else:
                curr += l
        if curr:
            parsed.append(curr)

        parsed = [el for el in parsed if el]

        while '(' in parsed:
            id1, id2 = None, None
            for i in range(len(parsed)):
                if parsed[i] == "(":
                    id1 = i
                if parsed[i] == ")":
                    id2 = i
                if id1 is not None and id2 is not None:
                    res = calc_expr(parsed[id1:id2 + 1])
                    parsed = [i for j, i in enumerate(parsed) if j not in range(id1, id2 + 1)]
                    parsed.insert(id1, res)
                    break
        if parsed[0] == '-':
            parsed = ['0'] + parsed
        while len(parsed) > 1:
            parsed = [str(int(parsed[0]) + int(parsed[2]))] + parsed[3:] if parsed[1] == "+" else [str(int(parsed[0]) - int(parsed[2]))] + parsed[3:]
        return int(parsed[0])
'''