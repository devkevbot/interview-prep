"""
Linked list implementation
"""


class Node:
    def __init__(self, data) -> None:
        self.next = None
        self.data = data


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.len = 0

    def __len__(self) -> int:
        return self.len

    def __str__(self) -> str:
        if self.len == 0:
            return "(EMPTY LIST)"
        curr = self.head
        values = []
        while curr is not None:
            if curr is self.head and curr is self.tail:
                values.append(f"{curr.data} (HEAD/TAIL)")
            elif curr is self.head:
                values.append(f"{curr.data} (HEAD) ")
            elif curr is self.tail:
                values.append(f"{curr.data} (TAIL) ")
            else:
                values.append(str(curr.data))
            curr = curr.next
        return "\n".join(values)

    def append(self, data):
        n = Node(data)
        if len(self) == 0:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n
        self.len += 1

    def search(self, value):
        curr = self.head

        while curr is not None:
            if curr.data == value:
                return curr
            curr = curr.next
        return None

    def remove_head(self):
        if self.head is None:
            return None

        data = self.head.data

        self.head = self.head.next
        self.len -= 1

        return data

    def remove_tail(self):
        if self.tail is None:
            return None

        curr = self.head

        if curr is None:
            return None

        while curr.next is not self.tail:
            curr = curr.next

        data = self.tail.data

        curr.next = None
        self.tail = curr
        self.len -= 1

        return data

    def reverse(self):
        prev = None
        curr = self.head
        next = None

        self.tail = self.head

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.head = prev


if __name__ == "__main__":
    l = LinkedList()
    assert len(l) == 0

    l.append(24)
    assert len(l) == 1

    n = l.search(24)
    assert n is not None

    n = l.search(1231232123)
    assert n is None

    l.append(30)
    assert len(l) == 2

    tail = l.remove_tail()
    assert len(l) == 1
    assert tail == 30

    head = l.remove_head()
    assert len(l) == 0
    assert head == 24

    l.append(3)
    l.append(4)
    l.append(5)
    print(l)

    print()

    l.reverse()
    print(l)
