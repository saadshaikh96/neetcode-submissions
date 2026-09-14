class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = "+-*/"
        for token in tokens:
            if token not in operands:
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(self.compute(num1, num2, token))
        return stack.pop()

    def compute(self, num1, num2, operand):
        if operand == '+':
            return num1 + num2
        if operand == '-':
            return num1 - num2
        if operand == '*':
            return num1 * num2
        return int(num1 / num2)