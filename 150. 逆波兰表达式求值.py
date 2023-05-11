
class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        tokens.reverse()
        if len(tokens) == 1:
            return tokens[0]
        def add(x, y):
            return x + y

        def subtract(x, y):
            return x - y

        def mul(x, y):
            return x * y

        def divide(x, y):
            return int(x / y)

        operator = {'+': add, '-': subtract, '*': mul, '/': divide}

        while True:
            char = tokens.pop()
            if any([char == ope for ope in operator.keys()]):
                b = stack.pop()
                a = stack.pop()
                c = operator[char](int(a), int(b))
                if not tokens:
                    return c
                stack.append(c)
            else:
                stack.append(char)



class Solution2:
    def evalRPN(self, tokens) -> int:
        stack = []

        for char in tokens:
            if char == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)
            elif char == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif char == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(b * a)
            elif char == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(char))

        return stack[0]



class Solution3:
    def evalRPN(self, tokens) -> int:
        stack = []
        for char in tokens:
            if char not in '+-*/':
                stack.append(int(char))
            else:
                b = stack.pop()
                a = stack.pop()
                if char == '+':
                    stack.append(a + b)
                if char == '-':
                    stack.append(a - b)
                if char == '*':
                    stack.append(a * b)
                if char == '/':
                    stack.append(int(a / b))
        return stack[0]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
#tokens = ["2","1","+","3","*"]
s = Solution3()
print(s.evalRPN(tokens))
a = '-1'
a.isalnum()