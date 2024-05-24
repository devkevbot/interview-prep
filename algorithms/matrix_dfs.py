"""
Matrix DFS implementation
"""

from typing import List

# UP, RIGHT, DOWN, LEFT
DIRECTIONS = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def matrix_dfs(m: List[List[int]]):
    path = []
    visited = []
    traverse(m, 0, 0, path, visited)
    return path


def traverse(
    m: List[List[int]],
    row: int,
    col: int,
    path: List[List[int]],
    visited: List[List[int]],
):
    path.append([row, col])

    if reached_end(m, row, col):
        return True

    if not can_walk(m, row, col, visited):
        path.pop()
        return False

    visited.append([row, col])

    for row_delta, col_delta in DIRECTIONS:
        if traverse(m, row + row_delta, col + col_delta, path, visited):
            return True

    return False


def reached_end(m: List[List[int]], row: int, col: int) -> bool:
    return row == len(m) - 1 and col == len(m[0]) - 1


def can_walk(m: List[List[int]], row: int, col: int, visited: List[List[int]]) -> bool:
    # We've been here before
    if [row, col] in visited:
        return False

    # Out of bounds on row
    if row >= len(m) or row < 0:
        return False
    # Out of bounds on col
    if col >= len(m[0]) or col < 0:
        return False

    # Path is unblocked
    return m[row][col] == 0


def generic_dfs(matrix, start, target):
    # Define the directions to move in the matrix
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Create a set to track visited cells
    visited = set([start])

    # Recursive function to explore the neighbors of a cell
    def explore(cell):
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
                    # Mark the neighbor as visited and explore it recursively
                    visited.add(neighbor)
                    if explore(neighbor):
                        return True

        # If we reach this point, we have exhausted all possible paths without reaching the target
        return False

    # Start the search from the starting cell
    return explore(start)


if __name__ == "__main__":
    m = [[0, 0, 0, 0], [1, 1, 0, 0], [1, 0, 0, 1], [1, 0, 0, 0]]
    path = matrix_dfs(m)
    print(path)
