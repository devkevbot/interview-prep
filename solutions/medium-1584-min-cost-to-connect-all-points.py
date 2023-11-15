import heapq


class Solution:
    def min_cost_connect_points(self, points: list[list[int]]) -> int:
        """
        Let n = the number of points
        Time: O(n^2 log n)
        Space: O(n^2)
        """

        n = len(points)
        adj = {}
        for i in range(n):
            adj[i] = []

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                weight = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([weight, j])
                adj[j].append([weight, i])

        # weight, index
        min_heap = [[0, 0]]
        visited = set()
        cost = 0

        while len(visited) < n:
            weight, i = heapq.heappop(min_heap)
            if i in visited:
                continue

            cost += weight
            visited.add(i)
            for weight, neighbor in adj[i]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, [weight, neighbor])

        return cost
