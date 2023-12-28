from collections import deque


class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        """
        Let m = the numbers of rows in the maze
        Let n = the number of columns in the maze
        Time: O(m * n)
        Space: O(m * n)
        """

        ROWS = len(maze)
        COLS = len(maze[0])

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        er, ec = entrance

        visited = set()

        q = deque()
        q.append((er, ec))

        steps = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                if r < 0 or c < 0 or r == ROWS or c == COLS:
                    continue
                if maze[r][c] == "+":
                    continue
                if (r, c) in visited:
                    continue
                if (
                    maze[r][c] == "."
                    and (r, c) != (er, ec)
                    and (r in (0, ROWS - 1) or c in (0, COLS - 1))
                ):
                    return steps
                visited.add((r, c))
                for dr, dc in dirs:
                    q.append((r + dr, c + dc))

            steps += 1

        return -1
