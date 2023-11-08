import heapq


class MedianFinder:
    def __init__(self):
        # Smaller half of the data stream, max heap, always contains n / 2 elements
        self.small = []
        # Larger half of the data stream, min heap, contains either n / 2 or n / 2 + 1 elements
        self.large = []

    def add_num(self, num: int) -> None:
        """
        Let n = the number of elements processed so far
        Time: O(log n)
        """
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

    def find_median(self) -> float:
        """
        Time: O(1)
        """
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        return float(self.large[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
