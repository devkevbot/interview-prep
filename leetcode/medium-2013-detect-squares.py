from collections import defaultdict


class DetectSquares:
    """
    Let n = the number of calls to add
    add:
        - Time: O(1)
    count:
        - Time: O(n)
    Data structure itself:
        - Space: O(n)
    """

    def __init__(self):
        self.x_points = defaultdict(list)
        self.cnt = defaultdict(int)

    def add(self, point: list[int]) -> None:
        x, y = point
        self.x_points[x].append(y)
        self.cnt[(x, y)] += 1

    def count(self, point: list[int]) -> int:
        x1, y1 = point
        ans = 0
        for y2 in self.x_points[x1]:
            if y2 == y1:
                continue  # Skip empty square
            side_len = abs(y2 - y1)

            # Case: p3, p4 points are on the left side of the line p1p2
            x3, y3 = x1 - side_len, y2
            x4, y4 = x1 - side_len, y1
            ans += self.cnt[(x3, y3)] * self.cnt[(x4, y4)]

            # Case 2: p3, p4 points are on the left side of the line p1p2
            x3, y3 = x1 + side_len, y2
            x4, y4 = x1 + side_len, y1
            ans += self.cnt[(x3, y3)] * self.cnt[(x4, y4)]
        return ans
