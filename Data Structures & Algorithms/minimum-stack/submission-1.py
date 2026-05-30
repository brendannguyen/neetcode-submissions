class MinStack:

    def __init__(self):
        self.stack = []
        self.minVals = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.minVals) == 0 or val <= self.getMin():
            self.minVals.append(val)

    def pop(self) -> None:
        if self.top() == self.getMin():
            self.minVals.pop()

        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVals[-1]
