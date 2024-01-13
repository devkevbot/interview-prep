class BruteForceSolution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        """
        Let m = the number of rows in the grid
        Let n = the number of columns in the grid
        Time: O(m * n)
        Space: O(1)
        """

        ROWS = len(grid)
        COLS = len(grid[0])

        negative_count = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] < 0:
                    negative_count += 1

        return negative_count


class BinarySearchSolution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        """
        Let m = the number of rows in the grid
        Let n = the number of columns in the grid
        Time: O(m * log n)
        Space: O(1)
        """

        """
        Example:
        [ 4, 3, 2,-1]
        [ 3, 2, 1,-1]
        [ 1, 1,-1,-2]
        [-1,-1,-2,-3]

        Find the first col in each row that has a negative value and derive the number of negative values in the row.
        row 0: first negative value at col 3 => 4 - 3 = 1 negative values in this row
        row 1: first negative value at col 3 => 4 - 3 = 1
        row 2: first negative value at col 2 => 4 - 2 = 2
        row 3: first negative value at col 0 => 4 - 0 = 4
        total: 8 negative values
        """

        ROWS = len(grid)
        COLS = len(grid[0])

        negative_count = 0

        for r in range(ROWS):
            left = 0
            right = COLS - 1
            first_negative_col = None
            while left <= right:
                mid = left + (right - left) // 2
                if grid[r][mid] < 0:
                    first_negative_col = mid
                    right = mid - 1
                else:
                    left = mid + 1
            if first_negative_col is not None:
                negative_count += COLS - first_negative_col

        return negative_count


class OptimalSolution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        """
        Let m = the number of rows in the grid
        Let n = the number of columns in the grid
        Time: O(m + n)
        Space: O(1)
        """

        ROWS = len(grid)
        COLS = len(grid[0])

        r = ROWS - 1
        c = 0
        negative_count = 0

        """
        The negative regions of the matrix will form a "staircase" shape:
        ++++++
        ++++--
        ++++--
        +++---
        +-----
        +-----
        """

        # Traverse the matrix up and right starting from the bottom left
        while r >= 0 and c < COLS:
            if grid[r][c] < 0:
                negative_count += COLS - c
                r -= 1
            else:
                c += 1

        return negative_count
