class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Let n = the size of the input `x`
        Time: O(log n)
        Space: O(1)
        """
        left = 0
        right = x + 1

        while left < right:
            mid = left + (right - left) // 2
            if mid * mid <= x:
                left = mid + 1
            else:
                right = mid

        return left - 1
