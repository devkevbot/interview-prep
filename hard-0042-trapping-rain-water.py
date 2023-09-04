class Solution:
    @staticmethod
    def trap(height: list[int]) -> int:
        """
        Time: O(n), where n is the length of the input
        Space: O(1)
        """

        left = 0
        right = len(height) - 1

        # The maximum height so far to the left
        left_max = height[left]
        # The maximum height so far to the right
        right_max = height[right]

        amount_trapped = 0

        while left < right:
            # The minimum of (left_max, right_max) is the bottleneck for adding water
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                amount_trapped += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                amount_trapped += right_max - height[right]

        return amount_trapped
