from collections import defaultdict


class TimeMap:
    def __init__(self):
        """
        Time: O(1)
        Space: O(1)
        """

        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Let k = the space needed to store the (value, timestamp) pair
        Time: O(1)
        Space: O(k)
        """

        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        """
        Let n = the number of value associated with a key
        Time: O(log n)
        Space: O(1)
        """

        if key not in self.data:
            return ""

        left = 0
        right = len(self.data[key]) - 1

        candidate = ""

        while left <= right:
            mid = left + (right - left) // 2

            timestamp_prev, value = self.data[key][mid]
            if timestamp_prev == timestamp:
                return value

            if timestamp_prev < timestamp:
                candidate = value
                left = mid + 1
            else:
                right = mid - 1

        return candidate
