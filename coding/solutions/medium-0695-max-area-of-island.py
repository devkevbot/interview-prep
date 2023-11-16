import collections


class BFSSolution:
    @staticmethod
    def max_area_of_island(grid: list[list[int]]) -> int:
        """
        Let n = the number of grid tiles
        Time: O(n)
        Space: O(n)
        """

        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        visited = set()

        def is_unvisited_land(r: int, c: int):
            row_ok = 0 <= r < rows
            col_ok = 0 <= c < cols
            return row_ok and col_ok and grid[r][c] == 1 and (r, c) not in visited

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        for row in range(rows):
            for col in range(cols):
                if is_unvisited_land(row, col):
                    area = 0

                    visited.add((row, col))
                    queue = collections.deque([(row, col)])

                    while queue:
                        r, c = queue.popleft()

                        if grid[r][c] == 1:
                            area += 1

                        for dr, dc in directions:
                            nr = dr + r
                            nc = dc + c

                            if is_unvisited_land(nr, nc):
                                visited.add((nr, nc))
                                queue.append((nr, nc))

                    max_area = max(max_area, area)

        return max_area
