"""
Queue implementation using the a linked list

"""

import linked_list as ll


class Queue:
    def __init__(self) -> None:
        self.data = ll.LinkedList()

    def __len__(self) -> int:
        return len(self.data)

    def enqueue(self, val) -> None:
        self.data.append(val)

    def dequeue(self):
        return self.data.remove_head()

    def front(self):
        if len(self.data) == 0:
            return None
        return self.data.head.data


if __name__ == "__main__":
    q = Queue()
    assert len(q) == 0

    q.enqueue(5)
    assert len(q) == 1
    assert q.front() == 5

    q.enqueue(10)
    assert len(q) == 2
    assert q.front() == 5

    d = q.dequeue()
    assert len(q) == 1
    assert d == 5
    assert q.front() == 10

    d = q.dequeue()
    assert len(q) == 0
    assert d == 10
    assert q.front() is None
