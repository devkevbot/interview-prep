class BruteForceSolution:
    @staticmethod
    def max_area(height: list[int]) -> int:
        """
        Let n = length of height input
        Time: O(n^2)
        Space: O(1)
        """

        def area(left, right):
            return (right - left) * min(height[left], height[right])

        answer = 0

        for left in range(len(height)):
            for right in range(left, len(height)):
                answer = max(answer, area(left, right))

        return answer


class TwoPointerSolution:
    def max_area(self, height: list[int]) -> int:
        """
        Let n = length of height input
        Time: O(n)
        Space: O(1)
        """

        def area(left, right):
            return (right - left) * min(height[left], height[right])

        answer = 0
        left = 0
        right = len(height) - 1

        while left < right:
            answer = max(answer, area(left, right))

            """
            The area of the rectangle is comprised of the height and width.
            
            The height used in the area calculation is the minimum of the heights of the
            left and right edge.
            
            Since we start with a maximum width, we know that for a given height, shrinking
            the width won't yield a greater area. This fact means we should try to find another
            height.
            
            The best approach, therefore, is to move the edge which is the smaller height.
            """
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return answer
