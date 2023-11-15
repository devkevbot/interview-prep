import heapq


# Given a connected graph with n nodes represented by a list of edges,
# where edge[0] = src, edge[1] = dst, and edge[2] = weight,
# find the shortest path from src to every other node in the graph.
#
# Only works with non-negative edge weights.
def find_shortest_path(edges, n, src):
    """
    Let V = the number of vertices
    Let E = the number of edges, equivalent to V * V
    Time: O((V + E) * logV)
        - The outer loop runs as long as the min_heap is not empty, and in each iteration,
        a node is popped from the heap. This operation takes O(log V) time, where V is the number of vertices.
        - The inner loop iterates over the neighbors of the current node, and in each iteration, a node is pushed onto
        the heap. This operation also takes O(log V) time.
        - Since each edge is considered at most twice (once for each endpoint),
        the total time complexity is O((V + E) * log V), where V is the number of vertices and E is the number of edges.
    Space: O(V + E)
        - The adjacency list holds all vertices and edges, which is O(V + E)
    """
    adj = {}
    for i in range(1, n + 1):
        adj[i] = []

    # s = src, d = dst, w = weight
    for s, d, w in edges:
        adj[s].append([d, w])

    shortest = {}
    min_heap = [[0, src]]
    while min_heap:
        w1, n1 = heapq.heappop(min_heap)
        # A lower-cost path to n1 was found earlier due to the min-heap invariant
        if n1 in shortest:
            continue
        shortest[n1] = w1

        for n2, w2 in adj[n1]:
            if n2 not in shortest:
                heapq.heappush(min_heap, [w1 + w2, n2])

    return shortest
