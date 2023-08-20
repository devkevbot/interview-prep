from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Time: O(n), where n is the input length
        Space: O(1)
        """
        l = 0
        r = len(numbers) - 1

        while l < r:
            curr_sum = numbers[l] + numbers[r]

            if target == curr_sum:
                return [l + 1, r + 1]

            if target > curr_sum:
                l += 1
            else:
                r -= 1
