"""
Min-heap implementation
"""

from typing import List

import heapq


class MinHeap:
    def __init__(self) -> None:
        self.data = []

    def __str__(self) -> str:
        if len(self.data) == 0:
            return "<EMPTY HEAP>"
        return ",".join(list(map(lambda x: str(x), self.data)))

    def push(self, value) -> None:
        """
        Time Complexity: O(logn)
        Space Complexity: ???
        """
        self.data.append(value)

        pos = len(self.data) - 1

        # Keep swapping the inserted node and its parent while the inserted node is > than its parent
        while self.pidx(pos) >= 0 and self.data[pos] < self.data[self.pidx(pos)]:
            self.data[pos], self.data[self.pidx(pos)] = (
                self.data[self.pidx(pos)],
                self.data[pos],
            )

            pos = self.pidx(pos)

    def pop(self):
        """
        Time Complexity: O(logn)
        Space Complexity: ???
        """
        if len(self.data) == 0:
            return None

        if len(self.data) == 1:
            return self.data.pop()

        # Store current root for later return
        top = self.data[0]

        # Pop the last element and move it into the root position
        last = self.data.pop()
        self.data[0] = last

        self.heapify_down(0)

        return top

    def top(self):
        if len(self.data) == 0:
            return None
        return self.data[0]

    def heapify(self, arr: List[int]):
        """
        Builds a heap from an array

        Time Complexity: O(n)
        """

        self.data = arr

        curr = (len(self.data) - 1) // 2

        while curr >= 0:
            self.heapify_down(curr)
            curr -= 1

    def heapify_down(self, pos):
        lci = self.lcidx(pos)
        rci = self.rcidx(pos)

        while lci < len(self.data):
            if (
                rci < len(self.data)
                and self.data[rci] < self.data[lci]
                and self.data[pos] > self.data[rci]
            ):
                # Swap current with right child
                self.data[pos], self.data[rci] = self.data[rci], self.data[pos]
                pos = self.rcidx(pos)
                lci = self.lcidx(pos)
                rci = self.rcidx(pos)
            elif self.data[pos] > self.data[lci]:
                # Swap current with left child
                self.data[pos], self.data[lci] = self.data[lci], self.data[pos]
                pos = self.lcidx(pos)
                lci = self.lcidx(pos)
                rci = self.rcidx(pos)
            else:
                break

    def lcidx(self, parent) -> int:
        """
        Left-child index
        """
        return (parent * 2) + 1

    def rcidx(self, parent) -> int:
        """
        Right-child index
        """
        return (parent * 2) + 2

    def pidx(self, child) -> int:
        """
        Parent index
        """
        return (child - 1) // 2


if __name__ == "__main__":
    h = MinHeap()
    h.push(40)
    h.push(30)
    h.push(20)
    h.push(10)
    print(h)

    assert h.top() == 10

    assert h.pop() == 10
    print(h)

    assert h.pop() == 20
    print(h)

    assert h.pop() == 30
    print(h)

    assert h.pop() == 40
    print(h)

    assert h.top() == None

    h.heapify([40, 30, 20, 10])
    h2 = [40, 30, 20, 10]
    heapq.heapify(h2)
    assert h.data == h2
