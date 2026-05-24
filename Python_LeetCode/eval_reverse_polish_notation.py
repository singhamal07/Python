from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in "+-*/":
                b, a = stack.pop(), stack.pop()
                stack.append(int(a / b) if t == '/' else eval(f"{a}{t}{b}"))
            else:
                stack.append(int(t))
        return stack[0]
