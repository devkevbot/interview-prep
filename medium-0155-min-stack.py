# According to the problem statement, methods pop, top and getMin operations will always be called
# on non-empty stacks.
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_val = float("inf")

    def push(self, val: int) -> None:
        """
        Time: O(1)
        Space: O(1)
        """
        self.min_val = min(self.min_val, val)
        self.stack.append((val, self.min_val))

    def pop(self) -> None:
        """
        Time: O(1)
        Space: O(1)
        """
        self.stack.pop()
        if len(self.stack) > 0:
            self.min_val = self.stack[-1][1]
        else:
            self.min_val = float("inf")

    def top(self) -> int:
        """
        Time: O(1)
        Space: O(1)
        """
        return self.stack[-1][0]

    def getMin(self) -> int:
        """
        Time: O(1)
        Space: O(1)
        """
        return self.min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
