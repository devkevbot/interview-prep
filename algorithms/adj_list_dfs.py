"""
Adjacency List DFS implementation
"""


def dfs_generic(adj_list, node, visited, path):
    if node in visited:
        return

    visited.add(node)
    path.append(node)

    for neighbour in adj_list[node]:
        dfs_generic(adj_list, neighbour, visited, path)


def dfs_num_paths(adj_list, node, target, visited):
    """
    Perform a DFS on adj_list, returning the number of paths from node to target
    """
    if node in visited:
        return 0

    if node == target:
        return 1

    visited.add(node)
    count = 0

    for neighbor in adj_list[node]:
        count += dfs_num_paths(adj_list, neighbor, target, visited)

    visited.remove(node)

    return count


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
    num_paths = dfs_num_paths(adj_list, "A", "E", set())

    visited = set()
    path = []
    dfs_generic(adj_list, "A", visited, path)
    print(path)
