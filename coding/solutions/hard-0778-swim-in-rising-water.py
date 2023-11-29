import collections
import heapq


class BFSSolution:
    def swim_in_water(self, grid: list[list[int]]) -> int:
        """
        Let t = the minimum time needed
        Let n = the side length of the n x n grid
        Time: O(t * n^2)
        Space: O(n^2)
        """

        n = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        time = 0

        while True:
            queue = collections.deque([(0, 0)])
            visited = set()

            while queue:
                r, c = queue.popleft()
                # Out of bounds or visited
                if r < 0 or c < 0 or r == n or c == n or (r, c) in visited:
                    continue
                # Water too high
                if grid[r][c] > time:
                    continue
                # At goal location
                if (r, c) == (n - 1, n - 1):
                    return time

                visited.add((r, c))

                for dr, dc in directions:
                    queue.append((r + dr, c + dc))

            time += 1


class DjikstrasSolution:
    def swim_in_water(self, grid: list[list[int]]) -> int:
        """
        Let n = the side length of the n x n grid
        Time: O(n^2 log n)
        Space: O(n^2)
        """

        n = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        visited = {(0, 0)}
        min_h = [(grid[0][0], 0, 0)]  # (max height along path, row, column)

        while min_h:
            t, r, c = heapq.heappop(min_h)
            # At goal location
            if r == n - 1 and c == n - 1:
                return t

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Out of bounds or visited
                if nr < 0 or nc < 0 or nr == n or nc == n or (nr, nc) in visited:
                    continue

                visited.add((nr, nc))
                heapq.heappush(min_h, (max(t, grid[nr][nc]), nr, nc))
