"""
Matrix BFS implementation
"""

from typing import List
from collections import deque

# UP, RIGHT, DOWN, LEFT
DIRECTIONS = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def matrix_bfs(m: List[List[int]]):
    """
    BFS

    Tries to go from top-left of m to the bottom-right of m.

    Any non-zero value is considered a blocked path.
    """

    queue = deque()

    if m[0][0] != 0 or m[-1][-1] != 0:
        return -1

    queue.append((0, 0))
    visited = {(0, 0)}

    current_distance = 1

    while len(queue) > 0:
        for _ in range(len(queue)):
            row, col = queue.popleft()

            if row == len(m) - 1 and col == len(m[0]) - 1:
                return current_distance

            for row_delta, col_delta in DIRECTIONS:
                curr_row = row + row_delta
                curr_col = col + col_delta

                # Already visited
                if (curr_row, curr_col) in visited:
                    continue

                # Out of bounds
                if (
                    curr_row < 0
                    or curr_col < 0
                    or curr_row >= len(m)
                    or curr_col >= len(m[0])
                ):
                    continue

                # Blocked paths
                if m[curr_row][curr_col] != 0:
                    continue

                queue.append((curr_row, curr_col))
                visited.add((curr_row, curr_col))

        current_distance += 1

    return -1


def generic_bfs(matrix, start, target):
    # Define the directions to move in the matrix
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Create a queue for BFS
    queue = deque([start])

    # Create a set to track visited cells
    visited = set([start])

    while queue:
        # Get the next cell to visit
        cell = queue.popleft()

        # Check if we have reached the target cell
        if cell == target:
            return True

        # Otherwise, explore the neighbors of the current cell
        for direction in directions:
            row, col = cell[0] + direction[0], cell[1] + direction[1]

            # Check if the neighbor is within the bounds of the matrix
            if row >= 0 and row < len(matrix) and col >= 0 and col < len(matrix[0]):
                neighbor = (row, col)

                # Check if the neighbor has not been visited before
                if neighbor not in visited:
                    # Add the neighbor to the queue and mark it as visited
                    queue.append(neighbor)
                    visited.add(neighbor)

    # If we reach this point, we have exhausted all possible paths without reaching the target
    return False


if __name__ == "__main__":
    m = [[0, 0, 0, 0], [1, 1, 0, 0], [1, 0, 0, 1], [1, 0, 0, 0]]
    path_length = matrix_bfs(m)
    print(path_length)
