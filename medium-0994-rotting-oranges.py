from collections import deque


class Solution:
    @staticmethod
    def oranges_rotting(grid: list[list[int]]) -> int:
        """
        Let n = the number of rows.
        Let m = the number of columns.
        Time: O(n * m)
        Space: O(n * m)
        """

        if not grid or not grid[0]:
            return -1

        ROWS = len(grid)
        COLS = len(grid[0])

        fresh = 0
        queue = deque()
        time = 0

        # Count the number of fresh oranges and enqueue the rotten oranges.
        # O(n * m) time.
        # O(n * m) space if all oranges are rotten.
        for row in range(ROWS):
            for col in range(COLS):
                # Fresh orange
                if grid[row][col] == 1:
                    fresh += 1
                # Rotten orange
                elif grid[row][col] == 2:
                    queue.append((row, col))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # While we have rotten oranges, convert its neighbours into rotten oranges and decrement the fresh count.
        while fresh and queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1
