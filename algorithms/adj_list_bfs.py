"""
Adjacency List BFS implementation
"""

from collections import deque


def bfs_generic(adj_list, start_node, visited, path):
    queue = deque()

    queue.append(start_node)
    visited.add(start_node)
    path.append(start_node)

    while len(queue) > 0:
        curr = queue.popleft()

        for neighbour in adj_list[curr]:
            if neighbour in visited:
                continue
            queue.append(neighbour)
            visited.add(neighbour)
            path.append(neighbour)


def bfs_shortest_path(adj_list, node, target):
    """
    Perform a BFS on adj_list, returning the shortest path from node to target
    """

    queue = deque()
    visited = set()

    queue.append(node)
    visited.add(node)

    path_length = 1

    while len(queue) > 0:
        for _ in range(len(queue)):
            curr = queue.popleft()

            if curr == target:
                return path_length

            for neighbour in adj_list[curr]:
                if neighbour in visited:
                    continue

                queue.append(neighbour)
                visited.add(neighbour)

        path_length += 1

    return -1


def adj_list_from_edges(edges):
    adj_list = {}

    for src, dst in edges:
        if src not in adj_list:
            adj_list[src] = []
        if dst not in adj_list:
            adj_list[dst] = []
        adj_list[src].append(dst)
    return adj_list


if __name__ == "__main__":
    edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]
    adj_list = adj_list_from_edges(edges)
    result = bfs_shortest_path(adj_list, "A", "E")

    visited = set()
    path = []
    bfs_generic(adj_list, "A", visited, path)
    print(path)
