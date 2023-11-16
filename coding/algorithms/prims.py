import heapq


# Given a list of edges of a connected undirected graph,
# with nodes numbered from 1 to n,
# return a list edges making up the minimum spanning tree.
def minimum_spanning_tree(edges, n):
    """
    Let V = the number of vertices
    Let E = the number of edges
    Time: O(E log V)
    Space: O(V + E)
    """
    adj = {}
    for i in range(1, n + 1):
        adj[i] = []

    for n1, n2, weight in edges:
        # Undirected graph, so we need to add an edge from
        # n1 to n2 and from n2 to n1
        adj[n1].append([n2, weight])
        adj[n2].append([n1, weight])

    # Initialize the heap by choosing a single node
    # (in this case 1) and pushing all its neighbors.
    min_heap = []
    for neighbor, weight in adj[1]:
        heapq.heappush(min_heap, [weight, 1, neighbor])

    min_spanning_tree = []
    visited = {1}

    while len(visited) < n:
        weight, n1, n2 = heapq.heappop(min_heap)
        if n2 in visited:
            continue

        min_spanning_tree.append([n1, n2])
        visited.add(n2)
        for neighbor, weight in adj[n2]:
            if neighbor not in visited:
                heapq.heappush(min_heap, [weight, n2, neighbor])

    return min_spanning_tree
