import bisect


class SnapshotArray:
    """
    Let n = the number of calls
    Let k = the length
    Time: O(n log n + k)
    Space: O(n + k)
    """

    def __init__(self, length: int):
        self.id = 0
        self.data = [[[self.id, 0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        # Optimization: remove the last record if its id is the same as self.id
        # to ensure that all ids at this index are unique
        if self.data[index][-1][0] == self.id:
            self.data[index].pop()

        self.data[index].append([self.id, val])

    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        snap_index = bisect.bisect_right(self.data[index], [snap_id, 10**9])
        return self.data[index][snap_index - 1][1]
