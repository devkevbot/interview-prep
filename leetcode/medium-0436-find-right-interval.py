class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        """
        Let n = the length of the input `intervals`
        Time: O(n log n)
        Space: O(n)

        Nomenclature:
        - s = start
        - e = end
        """

        # Sort the intervals by start time in ASC order.
        # Also, store the original index at which each interval is present.
        sorted_intervals = list(
            sorted([(s, e, j) for j, [s, e] in enumerate(intervals)])
        )

        right_intervals = []

        for [_, ei] in intervals:
            left = 0
            right = len(sorted_intervals) - 1
            pos = -1

            # Perform a binary search to find the right interval for the current interval
            while left <= right:
                mid = left + (right - left) // 2
                sj, _, j = sorted_intervals[mid]
                if sj >= ei:
                    pos = j
                    right = mid - 1
                else:
                    left = mid + 1

            right_intervals.append(pos)

        return right_intervals
