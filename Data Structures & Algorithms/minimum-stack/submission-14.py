class MinStack:

    def __init__(self):
        self.array = []
        self.minStack = []
       
    def push(self, val: int) -> None:
        self.array.append(val)
        # Add to minStack: the smaller of val and the current minimum
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.array:
            # If the value being popped is the current minimum, also pop from minStack
            if self.array[-1] == self.minStack[-1]:
                self.minStack.pop()
            self.array.pop()

    def top(self) -> int:
        if self.array:  # Check for non-empty stack
            return self.array[-1]
        return None  # Return None if the stack is empty (or handle as you prefer)

    def getMin(self) -> int:
        if self.minStack:  # Check for non-empty minStack
            return self.minStack[-1]
        return None  # Return None if the stack is empty (or handle as you prefer)
