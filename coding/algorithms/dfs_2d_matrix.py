def dfs_2d_matrix(matrix, start):
    """
    Let m = the number of rows
    Let n = the number of columns
    Time: O(m * n)
    Space: O(m * n)
    """
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up

    def dfs(row, col):
        if not (0 <= row < rows and 0 <= col < cols) or visited[row][col]:
            return

        # Process the current node (you can customize this part)
        print(f"Visiting node: {row}, {col}")
        visited[row][col] = True

        # Explore neighbors
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            dfs(new_row, new_col)

    # Start DFS from the given start node
    dfs(start[0], start[1])


# Example usage:
matrix_example = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

start_node = (0, 0)
dfs_2d_matrix(matrix_example, start_node)
