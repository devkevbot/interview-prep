import heapq


class Solution:
    def network_delay_time(self, times: list[list[int]], n: int, k: int) -> int:
        """
        Let V = the number of vertices
        Let E = the number of edges, equivalent to V * V
        Time: O((V + E) * logV)
        Space: O(V + E)
        """

        adj = {}
        for i in range(1, n + 1):
            adj[i] = []

        for s, d, w in times:
            adj[s].append([d, w])

        shortest = {}
        min_heap = [[0, k]]

        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            if n1 in shortest:
                continue
            shortest[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(min_heap, [w1 + w2, n2])

        # If any node cannot be reached from k, then it will not appear in shortest.
        # Therefore, the length will not be n.
        if len(shortest.keys()) != n:
            return -1

        # The minimum time is the longest time it takes to reach any of the connected nodes.
        return max(shortest.values())
