class Solution:
    @staticmethod
    def merge(intervals: list[list[int]]) -> list[list[int]]:
        """
        Let n = the number of intervals
        Time: O(n log n)
        Space: O(n)
        """
        # Sort by start time in ascending order.
        intervals.sort()

        result = [intervals[0]]

        for start, end in intervals:
            last_end = result[-1][1]

            # If overlapping...
            if start <= last_end:
                result[-1][1] = max(last_end, end)
            else:
                result.append([start, end])

        return result
