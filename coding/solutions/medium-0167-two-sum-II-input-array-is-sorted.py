class Solution:
    @staticmethod
    def two_sum(numbers: list[int], target: int) -> list[int]:
        """
        Time: O(n), where n is the input length
        Space: O(1)
        """
        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if target == total:
                return [left + 1, right + 1]

            if total < target:
                left += 1
            else:
                right -= 1
