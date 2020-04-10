class MinStack:

    def __init__(self):
        self.stack = [] 

    def push(self, x: int) -> None:
        min_value = min(x, self.stack[-1][1]) if len(self.stack) > 0 else x
        self.stack.append((x, min_value))
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        

if __name__ == "__main__":
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    print(str(stack.getMin()))
    stack.pop()
    print(str(stack.top()))
    print(str(stack.getMin()))