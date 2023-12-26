import heapq


class MinHeapSolution:
    @staticmethod
    def min_meeting_rooms(intervals: list[list[int]]) -> int:
        """
        Time: O(n log n), where n is the number of intervals
        Space: O(n)
        """

        if not intervals:
            return 0

        # We need to sort the intervals by their starting times so that
        # we can check meeting times in a way that makes chronological sense.
        intervals.sort()

        # Free rooms will be a min heap contains the end times of meetings.
        # The next available meeting room will be made available when the
        # earliest meeting ends, i.e., the top of the heap.
        free_rooms = []
        heapq.heappush(free_rooms, intervals[0][1])

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            # When this condition is true, this means that an earlier meeting
            # has already ended and that its meeting room is now available.
            # Therefore, we don't need to allocate a new meeting room.
            if free_rooms[0] <= start:
                heapq.heappop(free_rooms)

            heapq.heappush(free_rooms, end)

        return len(free_rooms)
