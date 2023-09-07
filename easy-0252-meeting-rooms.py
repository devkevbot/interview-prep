class SortingSolution:
    def can_attend_meetings(self, intervals: list[list[int]]) -> bool:
        """
        Time: O(n log n) where n is the number of intervals
        Space: O(1) or O(n) depending on the sorting algorithm used
        """

        intervals.sort()
        for i in range(len(intervals) - 1):
            if self.overlaps(intervals[i], intervals[i + 1]):
                return False
        return True

    @staticmethod
    def overlaps(interval_a, interval_b):
        start_a, end_a = interval_a
        start_b, end_b = interval_b
        return min(end_a, end_b) > max(start_a, start_b)
