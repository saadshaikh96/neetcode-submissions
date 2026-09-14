class MinStack:

    def __init__(self):
        self.numStack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.numStack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            minValue = min(self.minStack[-1], val)
            self.minStack.append(minValue)

    def pop(self) -> None:
        self.numStack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.numStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
