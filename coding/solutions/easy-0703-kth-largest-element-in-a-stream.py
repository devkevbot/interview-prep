import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        """
        Time: O(n log n)
        Space: O(n)
        """
        self.min_heap = nums
        self.k = k

        # O(n), where n = length of nums
        heapq.heapify(self.min_heap)

        # Maintain a heap of size k
        # At most O(n - k) iterations
        while len(self.min_heap) > k:
            # O(log n)
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        """
        Time: O(log k)
        Space: O(1)
        """

        # O(log k)
        heapq.heappush(self.min_heap, val)

        # Maintain a heap of size k
        if len(self.min_heap) > self.k:
            # O(log k)
            heapq.heappop(self.min_heap)

        # Since heapq implements a min heap, if the heap contains k elements,
        # then the root of the heap will be the smallest element, or in other words,
        # the kth largest element.
        return self.min_heap[0]
