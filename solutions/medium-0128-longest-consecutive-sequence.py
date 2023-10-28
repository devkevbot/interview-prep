from typing import List


# Set-based solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Time: O(n), where n is the length of the input
        Space: O(n)
        """

        # Edge case: empty list
        if not nums:
            return 0

        # Construct a set for O(1) lookup later on
        seen = set(nums)

        max_longest = 1

        for num in seen:
            # For any number x, if (x-1) exists in the input, then the sequence [x-1, x, ...] will
            # always be longer than the sequence starting at [x, ...]
            if num - 1 in seen:
                continue

            curr_longest = 1
            curr = num

            # While the next require number exists, keep iterating
            while curr + 1 in seen:
                curr_longest += 1
                curr += 1

            max_longest = max(max_longest, curr_longest)

        return max_longest
