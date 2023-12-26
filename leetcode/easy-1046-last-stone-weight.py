import heapq


class Solution:
    @staticmethod
    def last_stone_weight(stones: list[int]) -> int:
        """
        Time: O(n log n), where n is the length of the stones input
        Space: O(n)
        """

        # Edge case: single stone
        if len(stones) == 1:
            return stones[0]

        # Python doesn't have max heaps, so we need to invert values
        # O(n)
        heap = [-x for x in stones]

        # O(n)
        heapq.heapify(heap)

        # O(n)
        while heap:
            # If we get down to one rock, return it
            if len(heap) == 1:
                return -heap[0]

            # O(log n)
            first = -heapq.heappop(heap)
            # O(log n)
            second = -heapq.heappop(heap)

            # Smash rocks
            if first > second:
                # O(log n)
                heapq.heappush(heap, -(first - second))
            elif second > first:
                # O(log n)
                heapq.heappush(heap, -(second - first))

        return 0
