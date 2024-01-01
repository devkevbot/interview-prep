import collections


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        """
        Let n = the length of the input `arr`
        Time: O(n)
        Space: O(n)
        """
        freq = collections.defaultdict(int)
        for item in arr:
            freq[item] += 1
        unique_values = set(freq.values())
        return len(unique_values) == len(freq.values())
