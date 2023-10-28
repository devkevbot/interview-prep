class Solution:
    @staticmethod
    def erase_overlap_intervals(intervals: list[list[int]]) -> int:
        """
        Let n = the number of intervals
        Time: O(n log n)
        Space: O(1)
        """

        intervals.sort()
        count = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            # Case: non-overlapping
            if start >= prev_end:
                prev_end = end
            # Case: overlapping intervals
            else:
                count += 1
                # "Remove" the interval which ends later
                #    x-----x
                # x-----------x <--- remove this one
                prev_end = min(prev_end, end)

        return count
