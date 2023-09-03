import collections


class Solution:
    @staticmethod
    def num_islands(grid: list[list[str]]) -> int:
        """
        Given an m x n grid:
        Time: O(m * n)
        Space: O(m * n)
        """

        def is_on_grid(row: int, col: int) -> bool:
            row_in_bounds = row >= 0 and row < rows
            col_in_bounds = col >= 0 and col < cols
            return row_in_bounds and col_in_bounds

        def is_land(row: int, col: int) -> bool:
            if not is_on_grid(row, col):
                return False
            return grid[row][col] == "1"

        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        number_of_islands = 0
        directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]
        # If changing the input is allowed, we could also directly mark the grid squares with a number
        # that would identify if the grid square has been seen before, improving space complexity.
        seen = set()

        for row in range(rows):
            for col in range(cols):
                if is_land(row, col) and (row, col) not in seen:
                    number_of_islands += 1

                    queue = collections.deque([(row, col)])
                    seen.add((row, col))

                    while queue:
                        r, c = queue.popleft()
                        for dr, dc in directions:
                            nr = r + dr
                            nc = c + dc
                            if is_land(nr, nc) and (nr, nc) not in seen:
                                queue.append((nr, nc))
                                seen.add((nr, nc))

        return number_of_islands
