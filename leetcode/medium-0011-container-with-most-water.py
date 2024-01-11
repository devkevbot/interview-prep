class BruteForceSolution:
    def area(self, left: int, right: int, height: list[int]) -> int:
        return (right - left) * min(height[left], height[right])

    def max_area(self, height: list[int]) -> int:
        """
        Let n = length of height input
        Time: O(n^2)
        Space: O(1)
        """

        max_area = 0

        for left in range(len(height)):
            for right in range(left, len(height)):
                max_area = max(max_area, self.area(left, right, height))

        return max_area


class TwoPointerSolution:
    def area(self, left: int, right: int, height: list[int]) -> int:
        return (right - left) * min(height[left], height[right])

    def max_area(self, height: list[int]) -> int:
        """
        Let n = length of height input
        Time: O(n)
        Space: O(1)
        """

        max_area = 0

        left = 0
        right = len(height) - 1

        while left < right:
            max_area = max(max_area, self.area(left, right, height))
            """
            Since we start with a maximum width, we know that for a given height, shrinking
            the width won't yield a greater area. This fact means we should try to find another
            height.
            
            The best approach, therefore, is to move the edge which is the smaller height.
            """
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area
