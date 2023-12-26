import collections


class SlidingWindowLongSolution:
    @staticmethod
    def check_inclusion(s1: str, s2: str) -> bool:
        """
        m = length of s1
        n = length of s2
        Time: O(n)
        Space: O(1)
        """
        if len(s1) > len(s2):
            return False

        s1_count, s2_count = [0] * 26, [0] * 26
        # O(26)
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord("a")] += 1
            s2_count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        # O(26)
        for i in range(26):
            matches += 1 if s1_count[i] == s2_count[i] else 0

        left = 0
        # O(n - m)
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # Update counts for the right edge of the sliding window
            index = ord(s2[right]) - ord("a")
            s2_count[index] += 1
            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] + 1 == s2_count[index]:
                matches -= 1

            # Update counts for the left edge of the sliding window
            index = ord(s2[left]) - ord("a")
            s2_count[index] -= 1
            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] - 1 == s2_count[index]:
                matches -= 1

            left += 1

        return matches == 26


class SlidingWindowShortSolution:
    class Solution:
        @staticmethod
        def check_inclusion(s1: str, s2: str) -> bool:
            """
            m = length of s1
            n = length of s2
            Time: O(n*m)
            Space: O(m)
            """
            if len(s1) > len(s2):
                return False

            # O(m) time and space
            s1_count = collections.Counter(s1)

            left = 0
            right = len(s1)

            # O(n - m) time
            while right <= len(s2):
                # O(m) time and space
                if s1_count == collections.Counter(s2[left:right]):
                    return True
                left += 1
                right += 1

            return False
