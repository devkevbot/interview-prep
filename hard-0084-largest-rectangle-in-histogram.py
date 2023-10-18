class Solution:
    @staticmethod
    def largest_rectangle_area(heights: list[int]) -> int:
        """
        Let n = the length of heights
        Time: O(n)
        Space: O(n)
        """

        max_area = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            # Start is the left edge of the current rectangle
            start = i

            # If the top of the stack contains a taller bar than the current, we can't extend
            # that taller bar to the right any further, so we pop it and compute the area.
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                # Extend the left edge of the current rectangle back to the index
                # of the tallest element to its left that has been seen so far while popping
                # in the current run of elements.
                start = index

            stack.append((start, h))

        # If there are leftover elements in the stack, they are in monotonically increasing order.
        # We can also compute their areas by using the element's height and its position from
        # the end of the input array as the width.
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area
