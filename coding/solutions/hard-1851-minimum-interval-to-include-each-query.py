import heapq


class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        """
        Let n = the number of intervals
        Let m = the number of queries
        Time: O(n log n + m log m)
        Space: O(n + m)
        """

        intervals.sort()
        min_heap = []
        result = {}
        i = 0

        for query in sorted(queries):
            # Add candidate intervals to the min_heap
            while i < len(intervals) and intervals[i][0] <= query:
                left, right = intervals[i]
                heapq.heappush(min_heap, (self.interval_size(intervals[i]), right))
                i += 1

            # Remove candidate intervals whose right bound doesn't contain the query.
            # Since we sort the queries, no other subsequent query will be contained
            # in the popped interval either.
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)

            # Record the size of the smallest remaining interval, if there is one
            result[query] = min_heap[0][0] if min_heap else -1

        return [result[q] for q in queries]

    def interval_size(self, interval: list[int]) -> int:
        left, right = interval
        return right - left + 1
