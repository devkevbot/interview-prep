class Solution:
    @staticmethod
    def insert(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
        """
        Let n = the number of intervals.
        Time: O(n)
        Space: O(n)
        """

        res = []

        for i, interval in enumerate(intervals):
            # If new_interval ends before interval starts
            if new_interval[1] < interval[0]:
                res.append(new_interval)
                # No overlap is possible with subsequent intervals, return immediately
                return res + intervals[i:]
            # If new_interval starts after interval ends
            elif new_interval[0] > interval[1]:
                # Insert the current interval and keep trying to find a spot to insert new_interval
                res.append(interval)
            # There is overlap, merge intervals
            else:
                new_interval = [
                    min(interval[0], new_interval[0]),
                    max(interval[1], new_interval[1])
                ]
        # new_interval either occurs after all other intervals or it is a merged interval;
        # either way, it needs to be inserted
        res.append(new_interval)
        return res
