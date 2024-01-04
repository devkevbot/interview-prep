# TODO: verify if this code works

import heapq


def find_shortest_path(edges, n, src, goal):
    """
    Let V = the number of vertices
    Let E = the number of edges
    Time: O((V + E) log V)
    Space: O(V + E)
    """
    adj = {}
    for i in range(1, n + 1):
        adj[i] = []

    # s = src, d = dst, w = weight
    for s, d, w in edges:
        adj[s].append([d, w])

    def heuristic(node):
        # Replace this with your own heuristic function
        # For simplicity, you can use a constant value or implement a more sophisticated heuristic.
        return 0

    shortest = {}

    # The heap store tuples of (f, g, src)
    # f = g + h
    #     f is the total estimated cost of the cheapest path from the start node to the goal node that passes through the current node.
    #     g is the cost of the path from the start node to the current node.
    #     h is a heuristic estimate of the cost from the current node to the goal node.
    # The A* algorithm uses this total cost to prioritize nodes in the search, exploring nodes with
    # lower f values first. This allows A* to explore the most promising paths early, making it
    # more efficient than some other search algorithms.
    min_heap = [[0 + heuristic(src), 0, src]]

    while min_heap:
        f, g1, n1 = heapq.heappop(min_heap)

        # A lower-cost path to n1 was found earlier due to the min-heap invariant
        if n1 in shortest:
            continue

        shortest[n1] = g1

        if n1 == goal:
            break  # Stop once the goal is reached

        for n2, g2 in adj[n1]:
            if n2 not in shortest:
                heapq.heappush(min_heap, [g1 + g2 + heuristic(n2), g1 + g2, n2])

    return shortest
