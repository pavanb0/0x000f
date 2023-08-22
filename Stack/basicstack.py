class MinStack:

    def __init__(self):
        self.stack = []
       
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        if len(self.stack)<=0:
            return 0
        self.stack.pop()
        

    def top(self) -> int:
        if len(self.stack)<=0:
            return 0
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.stack) <=0:
            return 0
        st = sorted(self.stack)
        return st[0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()