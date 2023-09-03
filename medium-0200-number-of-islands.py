import collections


class Solution:
    @staticmethod
    def num_islands(grid: list[list[str]]) -> int:
        """
        Given an m x n grid:
        Time: O(mn)
        Space: O(mn)
        """

        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        num_islands = 0
        rows = len(grid)
        cols = len(grid[0])
        # Rather than using a set, it's also possible to modify the grid in-place to signify a seen cell.
        # Using that approach, space complexity can be reduced.
        seen = set()

        def is_unvisited_land(row, col):
            row_ok = row >= 0 and row < rows
            col_ok = col >= 0 and col < cols
            return (
                row_ok and col_ok and (row, col) not in seen and grid[row][col] == "1"
            )

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        for row in range(rows):
            for col in range(cols):
                if is_unvisited_land(row, col):
                    num_islands += 1

                    queue = collections.deque([(row, col)])
                    seen.add((row, col))

                    while queue:
                        r, c = queue.popleft()
                        for dr, dc in directions:
                            nr = r + dr
                            nc = c + dc
                            if is_unvisited_land(nr, nc):
                                queue.append((nr, nc))
                                seen.add((nr, nc))

        return num_islands
