# Given a directed acyclic graph, return a valid topological ordering of the graph.
# There are n nodes in the graph.
def topological_sort(edges: list[list[int]], n: int) -> list[int]:
    # Create the adjacency list
    adj = {}
    for i in range(n):
        adj[i] = []
    for src, dst in edges:
        adj[src].append(dst)

    top_sort = []
    visited = set()

    for i in range(n):
        dfs(i, adj, visited, top_sort)

    top_sort.reverse()
    return top_sort


def dfs(src: int, adj: dict[int, list[int]], visited: set[int], top_sort: list[int]):
    if src in visited:
        return

    visited.add(src)

    for neighbor in adj[src]:
        dfs(neighbor, adj, visited, top_sort)

    top_sort.append(src)
