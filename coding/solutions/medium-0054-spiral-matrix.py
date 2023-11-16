class Solution:
    @staticmethod
    def spiral_order(matrix: list[list[int]]) -> list[int]:
        """
        Let m = the number of rows
        Let n = the number of cols
        Time: O(m * n)
        Space: O(m * n)
        """

        right = 0
        down = 1
        left = 2
        up = 3
        direction = right

        total_elements = len(matrix) * len(matrix[0])

        top_bound = 0
        right_bound = len(matrix[0])
        left_bound = -1
        bottom_bound = len(matrix)

        res = []

        while len(res) < total_elements:
            if direction == right:
                for i in range(left_bound + 1, right_bound):
                    res.append(matrix[top_bound][i])
                right_bound -= 1
                direction = down
            elif direction == down:
                for i in range(top_bound + 1, bottom_bound):
                    res.append(matrix[i][right_bound])
                bottom_bound -= 1
                direction = left
            elif direction == left:
                for i in reversed(range(left_bound + 1, right_bound)):
                    res.append(matrix[bottom_bound][i])
                left_bound += 1
                direction = up
            elif direction == up:
                for i in reversed(range(top_bound + 1, bottom_bound)):
                    res.append(matrix[i][left_bound])
                top_bound += 1
                direction = right
        return res
