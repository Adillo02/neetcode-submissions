class MinStack:

    def __init__(self):
        self.MinStack = []
        self.stack = []
        
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.MinStack:
            minimum = min(val, self.MinStack[-1])
            self.MinStack.append(minimum)
        else:
            self.MinStack.append(val)


        

    def pop(self) -> None:
        self.MinStack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.MinStack[-1]
        
