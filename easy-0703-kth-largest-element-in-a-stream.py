import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        """
        Time: O(nlogn)
        Space: O(n)
        """
        self.min_heap = nums
        self.k = k

        # O(n), where n = length of nums
        heapq.heapify(self.min_heap)

        # Maintain a heap of size k
        # O(n - k)
        while len(self.min_heap) > k:
            # O(log(n))
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        """
        Time: O(logk)
        Space: O(1)
        """

        # O(log(k))
        heapq.heappush(self.min_heap, val)

        # Maintain a heap of size k
        if len(self.min_heap) > self.k:
            # O((log(k)))
            heapq.heappop(self.min_heap)

        # Since heapq implements a min heap, if the heap contains k elements,
        # then the root of the heap will the smallest element, or in the words,
        # the kth largest element.
        return self.min_heap[0]
