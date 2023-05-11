
'''class Solution:
    def calculate(self, s: str) -> int:
        dic = {'+': 0, '-': 1, '*': 2, '/': 3, '^': 4, '!': 5, '(': 6, ')': 7}
        pattern = [['>'] * 8 for _ in range(8)]
        pattern[4][5] = '<'
        pattern[7][6] = '='
        for i in range(0, 2):
            for j in range(2, 6):
                pattern[0][j] = '<'
        for i in range(2, 4):
            for j in range(4, 6):
                pattern[i][j] = '<'
        for i in range(6, 8):
            for j in range(6):
                pattern[i][j] = '<'
        for i in range(5):
            pattern[i][6] = '<'
        def operation(num1, num2, op):
            if op == '+':
                return num1 + num2
            elif op == '-':
                return num1 - num2
            elif op == '*':
                return num1 * num2
            elif op == '/':
                return num1 / num2
            elif op == '^':
                return num1 ** num2
        def factorial(num):
            x = 1
            for i in range(1, num + 1):
                x *= i
            return x
        stack_num = [0]
        stack_op = []
        num = 0
        denominator = 10
        mul = True
        for char in s:
            if char.isdigit() or char == '.':
                if char == '.':
                    mul = False
                else:
                    if mul:
                        num += num * 10 + int(char)
                    else:
                        num += int(char) / denominator
                        denominator *= 10
            else:
                if num != 0:
                    stack_num.append(num)
                    denominator = 10
                    mul = True
                    num = 0
                if char == '!':
                    stack_num.append(factorial(stack_num.pop()))
                elif not stack_op or pattern[dic[stack_op[-1]]][dic[char]] == '<':
                    stack_op.append(char)
                elif stack_op and pattern[dic[stack_op[-1]]][dic[char]] == '>':
                    while stack_op and pattern[dic[stack_op[-1]]][dic[char]] == '>':
                        b = stack_num.pop()
                        a = stack_num.pop()
                        c = operation(a, b, stack_op.pop())
                        stack_num.append(c)
                        if stack_op and stack_op[-1] == '(' and char == ')':
                            stack_op.pop()
                            break
                    if char == ')':
                        continue
                    stack_op.append(char)

        if len(stack_num) == 1:
            return operation(stack_num.pop(), num, stack_op.pop())
        else:
            stack_num.append(num)
            while stack_op:
                b = stack_num.pop()
                a = stack_num.pop()
                stack_num.append(operation(a, b, stack_op.pop()))
            return stack_num.pop()'''
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        pre = '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in '+-*/' or i == len(s) - 1:
                if pre == '+':
                    stack.append(num)
                if pre == '-':
                    stack.append(-num)
                if pre == '*' or pre == '/':
                    a = stack.pop()
                    if pre == '*':
                        stack.append(a * num)
                    else:
                        stack.append(int(a / num))
                pre = s[i]
                num = 0
        return sum(stack)


#2
class Solution2:
    def calculate(self, s: str) -> int:
        num = 0
        stack = []
        pre = '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in '+-*/' or i == len(s) - 1:
                if pre == '*':
                    stack.append(stack.pop() * num)
                if pre == '/':
                    stack.append(int(stack.pop() / num))
                if pre == '-':
                    stack.append(-num)
                if pre == '+':
                    stack.append(num)
                num = 0
                pre = s[i]
        return sum(stack)


class Solution3:
    def calculate(self, s: str) -> int:
        stack = []
        n = 0
        pre = '1'
        for char in s:
            if char.isdigit():
                n = n * 10 + int(char)
            if char in '+-*/':
                if pre in '+-*/':
                    b = stack.pop()
                    if pre == '*':
                        stack.append(b * n)
                    if pre == '/':
                        stack.append(int(b / n))
                    if pre == '-':
                        stack.append(b)
                        stack.append(-n)
                    if pre == '+':
                        stack.append(b)
                        stack.append(n)
                else:
                    stack.append(n)
                pre = char
                n = 0
        if stack:
            b = stack.pop()
        else:
            stack.append(n)
        if pre == '*':
            stack.append(b * n)
        if pre == '/':
            stack.append(int(b / n))
        if pre == '-':
            stack.append(b)
            stack.append(-n)
        if pre == '+':
            stack.append(b)
            stack.append(n)
        return sum(stack)

s = Solution3()
ss = "3+2*22"
print(s.calculate(ss))