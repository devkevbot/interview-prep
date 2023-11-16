class Solution:
    @staticmethod
    def partition_labels(s: str) -> list[int]:
        """
        Let n = the size of the input s
        Time: O(n)
        Space: O(n)
        """

        window_sizes = []

        last_occurrence = {}
        for i, c in enumerate(s):
            last_occurrence[c] = i

        pos = 0
        curr_length = 0
        end = 0

        while pos < len(s):
            letter = s[pos]
            # Continue to expand end with the last occurrence of the current letter.
            end = max(end, last_occurrence[letter])
            curr_length += 1

            # Eventually, end will stop changing for a given window. When this occurs, we will be able to reach end.
            if pos == end:
                window_sizes.append(curr_length)
                curr_length = 0

            pos += 1

        return window_sizes
