import collections


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        """
        Let m = the number of rows
        Let n = the number of columns
        Time: O(m * n)
        Space: O(m * n)
        """

        rows = collections.defaultdict(int)
        num_equal_pairs = 0

        NUM_ROWS = len(grid)
        NUM_COLS = len(grid[0])

        # Add each row and update how many times its been seen
        for i in range(NUM_ROWS):
            rows[tuple(grid[i])] += 1

        # Iterate through each column, updating num_equal_pairs if the column matches a row we've seen before
        for j in range(NUM_COLS):
            col = []
            for i in range(NUM_ROWS):
                col.append(grid[i][j])
            col = tuple(col)
            if col in rows:
                num_equal_pairs += rows[col]

        return num_equal_pairs
