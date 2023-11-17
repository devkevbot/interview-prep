from collections import deque


def bfs_2d_matrix(matrix, start):
    """
    Let m = the number of rows
    Let n = the number of columns
    Time: O(m * n)
    Space: O(m * n)
    """
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    queue = deque([start])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up

    while queue:
        current_row, current_col = queue.popleft()
        visited[current_row][current_col] = True

        # Process the current node (you can customize this part)
        print(f"Visiting node: {current_row}, {current_col}")

        # Explore neighbors
        for dr, dc in directions:
            new_row, new_col = current_row + dr, current_col + dc

            # Check if the neighbor is within bounds and not visited
            if (
                0 <= new_row < rows
                and 0 <= new_col < cols
                and not visited[new_row][new_col]
            ):
                queue.append((new_row, new_col))
                visited[new_row][new_col] = True


# Example usage:
matrix_example = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

start_node = (0, 0)
bfs_2d_matrix(matrix_example, start_node)
