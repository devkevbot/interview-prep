import collections


class TimeMap:
    def __init__(self):
        """
        Time: O(1)
        Space: O(1)
        """

        self.data = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Let k = the space needed to store the (value, timestamp) pair
        Time: O(1)
        Space: O(k)
        """

        self.data[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        """
        Let n = the number of value associated with a key
        Time: O(log n)
        Space: O(1)
        """

        if key not in self.data:
            return ""

        values = self.data[key]

        left = 0
        right = len(values) - 1

        candidate = ""

        while left <= right:
            mid = left + (right - left) // 2

            value_prev, timestamp_prev = values[mid]
            if timestamp_prev == timestamp:
                return value_prev

            if timestamp_prev < timestamp:
                candidate = value_prev
                left = mid + 1
            else:
                right = mid - 1

        return candidate


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
