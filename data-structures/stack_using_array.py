"""
Stack implementation using an array

Operations:
- Push O(1)
- Pop O(1)
- Peek O(1)

"""


class Stack:
    def __init__(self) -> None:
        self.data = []

    def __len__(self) -> int:
        return len(self.data)

    def push(self, val) -> None:
        self.data.append(val)

    def pop(self):
        if len(self.data) == 0:
            return None
        return self.data.pop()

    def peek(self):
        if len(self.data) == 0:
            return None
        return self.data[-1]


if __name__ == "__main__":
    s = Stack()
    assert len(s) == 0
    s.push(10)
    assert len(s) == 1
    assert s.peek() == 10

    s.push(13)
    assert len(s) == 2
    assert s.peek()

    p = s.pop()
    assert p == 13
    assert len(s) == 1
    assert s.peek() == 10

    p = s.pop()
    assert p == 10
    assert len(s) == 0
    assert s.peek() == None

    p = s.pop()
    assert p is None
