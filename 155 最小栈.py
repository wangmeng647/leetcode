class MinStack:

    def __init__(self):
        self.stack = []
        self.auxiliary = [float('inf')]
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.auxiliary.append(min(val, self.auxiliary[-1]))
    def pop(self) -> None:
        self.stack.pop()
        self.auxiliary.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.auxiliary[-1]





#2
class MinStack2:

    def __init__(self):
        self.stack = []
        self.min_stack = [float('inf')]
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack[-1] > val:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.min_stack[-1]