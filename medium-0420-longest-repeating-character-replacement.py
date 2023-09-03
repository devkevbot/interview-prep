import collections


class SlidingWindowSolution:
    @staticmethod
    def character_replacement(s: str, k: int) -> int:
        """
        Time: O(n*m) where n is the length of s and m is the size of the set of possible characters in the input
        Space: O(m)
        """
        longest_substring = 0
        count = collections.defaultdict(int)

        left = 0
        right = 0

        # Iterating through the input as a sliding window, O(n)
        while left < len(s) and right < len(s):
            count[s[right]] += 1

            window_size = right - left + 1
            # O(m)
            highest_freq = max(count.values())

            replacements_required = window_size - highest_freq
            if replacements_required > k:
                count[s[left]] -= 1
                left += 1
            else:
                longest_substring = max(longest_substring, window_size)

            right += 1

        return longest_substring
